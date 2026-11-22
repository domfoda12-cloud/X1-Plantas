"""Renderiza a casa exportada (GLB) no Blender Cycles, com luz de sol e céu físicos.

Chamado por render-realista.cjs:
    blender -b --factory-startup -P cycles.py -- casa.glb pasta-de-saida [amostras] [escala] [so]
ou, com o pacote bpy do Python:
    python cycles.py -- casa.glb pasta-de-saida [amostras] [escala] [so]

Sai um PNG de 2000 x 2500 (vezes a escala) para cada câmera do GLB.
"""
import math
import os
import sys

import bpy

args = sys.argv[sys.argv.index("--") + 1:]
GLB, DESTINO = args[0], args[1]
AMOSTRAS = int(args[2]) if len(args) > 2 and args[2] else 160
ESCALA = float(args[3]) if len(args) > 3 and args[3] else 1.0
SO = args[4] if len(args) > 4 else ""

bpy.ops.wm.read_factory_settings(use_empty=True)
import addon_utils  # noqa: E402
addon_utils.enable("cycles")
addon_utils.enable("io_scene_gltf2")
bpy.ops.import_scene.gltf(filepath=GLB)
cena = bpy.context.scene

# ------------------------------------------------------------------ render
cena.render.engine = "CYCLES"
cy = cena.cycles
cy.device = "CPU"
cy.samples = AMOSTRAS
cy.use_adaptive_sampling = True
cy.adaptive_threshold = 0.02
cy.use_denoising = True
cy.max_bounces = 6
cy.diffuse_bounces = 3
cy.glossy_bounces = 3
cy.transmission_bounces = 6
cy.transparent_max_bounces = 8
cy.caustics_reflective = False
cy.caustics_refractive = False
cena.render.resolution_x = 2000
cena.render.resolution_y = 2500
cena.render.resolution_percentage = round(100 * ESCALA)
cena.render.image_settings.file_format = "PNG"
cena.render.image_settings.color_mode = "RGB"
cena.render.threads_mode = "AUTO"
try:
    cena.view_settings.view_transform = "AgX"
    cena.view_settings.look = "AgX - Medium High Contrast"
except TypeError:
    cena.view_settings.view_transform = "Filmic"
cena.view_settings.exposure = 0.35

# ------------------------------------------------------------------ luz: céu físico + sol da manhã
mundo = bpy.data.worlds.new("ceu")
cena.world = mundo
mundo.use_nodes = True
nt = mundo.node_tree
nt.nodes.clear()
ceu = nt.nodes.new("ShaderNodeTexSky")
ELEV, ROT = math.radians(48), math.radians(-128)
for tipo in ("MULTIPLE_SCATTERING", "NISHITA", "HOSEK_WILKIE"):
    try:
        ceu.sky_type = tipo
        break
    except TypeError:
        continue
for nome, valor in (("sun_elevation", ELEV), ("sun_rotation", ROT), ("sun_disc", False),
                    ("air_density", 1.0), ("dust_density", 0.6), ("ozone_density", 1.0)):
    try:
        setattr(ceu, nome, valor)
    except (AttributeError, TypeError):
        pass
fundo = nt.nodes.new("ShaderNodeBackground")
fundo.inputs["Strength"].default_value = 0.22
sai = nt.nodes.new("ShaderNodeOutputWorld")
nt.links.new(ceu.outputs[0], fundo.inputs["Color"])
nt.links.new(fundo.outputs[0], sai.inputs["Surface"])

for o in list(bpy.data.objects):  # as luzes do motor em tempo real não servem aqui
    if o.type == "LIGHT":
        bpy.data.objects.remove(o)
sol = bpy.data.lights.new("sol", "SUN")
sol.energy = 4.2
sol.angle = math.radians(2.2)  # sombra com borda levemente suave
sol.color = (1.0, 0.95, 0.88)
osol = bpy.data.objects.new("sol", sol)
cena.collection.objects.link(osol)
# Sol vindo da frente-esquerda da casa (a frente fica no alto da imagem), a 48 graus de altura
osol.rotation_euler = (math.radians(90 - 48), 0, math.radians(-128 + 180))


# ------------------------------------------------------------------ materiais
def principled(mat):
    if not mat or not mat.use_nodes:
        return None
    return next((n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)


def cor_base(p):
    return tuple(p.inputs["Base Color"].default_value[:3])


def tem_textura(p):
    return bool(p.inputs["Base Color"].links)


def ruido_cor(mat, p, escala, forca, relevo=0.0):
    """Varia a cor (e opcionalmente o relevo) com ruído, para a superfície não ficar chapada."""
    nt = mat.node_tree
    r = nt.nodes.new("ShaderNodeTexNoise")
    r.inputs["Scale"].default_value = escala
    r.inputs["Detail"].default_value = 6
    coord = nt.nodes.new("ShaderNodeTexCoord")
    nt.links.new(coord.outputs["Object"], r.inputs["Vector"])
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.blend_type = "MULTIPLY"
    mix.inputs["Factor"].default_value = forca
    origem = p.inputs["Base Color"].links[0].from_socket if tem_textura(p) else None
    if origem:
        nt.links.new(origem, mix.inputs["A"])
    else:
        mix.inputs["A"].default_value = (*cor_base(p), 1)
    rampa = nt.nodes.new("ShaderNodeValToRGB")
    rampa.color_ramp.elements[0].position = 0.3
    rampa.color_ramp.elements[0].color = (0.55, 0.55, 0.55, 1)
    rampa.color_ramp.elements[1].position = 0.75
    rampa.color_ramp.elements[1].color = (1, 1, 1, 1)
    nt.links.new(r.outputs["Fac"], rampa.inputs["Fac"])
    nt.links.new(rampa.outputs["Color"], mix.inputs["B"])
    nt.links.new(mix.outputs["Result"], p.inputs["Base Color"])
    if relevo:
        b = nt.nodes.new("ShaderNodeBump")
        b.inputs["Strength"].default_value = relevo
        b.inputs["Distance"].default_value = 0.02
        r2 = nt.nodes.new("ShaderNodeTexNoise")
        r2.inputs["Scale"].default_value = escala * 12
        r2.inputs["Detail"].default_value = 8
        nt.links.new(coord.outputs["Object"], r2.inputs["Vector"])
        nt.links.new(r2.outputs["Fac"], b.inputs["Height"])
        nt.links.new(b.outputs["Normal"], p.inputs["Normal"])


def relevo_da_textura(mat, p, forca):
    """Usa a própria textura do piso como relevo: as juntas das tábuas e do porcelanato afundam."""
    nt = mat.node_tree
    origem = p.inputs["Base Color"].links[0].from_node
    b = nt.nodes.new("ShaderNodeBump")
    b.inputs["Strength"].default_value = forca
    b.inputs["Distance"].default_value = 0.004
    nt.links.new(origem.outputs["Color"], b.inputs["Height"])
    nt.links.new(b.outputs["Normal"], p.inputs["Normal"])


def eh_verde(c):
    return c[1] > c[0] * 1.12 and c[1] > c[2] * 1.2


def eh_claro(c):
    return min(c) > 0.55 and max(c) - min(c) < 0.12


feitos = set()
for obj in bpy.data.objects:
    if obj.type != "MESH":
        continue
    dim = obj.dimensions
    for slot in obj.material_slots:
        mat = slot.material
        p = principled(mat)
        if not p or mat.name in feitos:
            continue
        feitos.add(mat.name)
        c = cor_base(p)
        alpha = p.inputs["Alpha"].default_value
        grande = max(dim.x, dim.y) > 30
        if alpha < 0.95 and not tem_textura(p):  # vidro de janela e do box
            p.inputs["Base Color"].default_value = (0.86, 0.94, 0.95, 1)
            p.inputs["Roughness"].default_value = 0.03
            p.inputs["Transmission Weight"].default_value = 1.0
            p.inputs["IOR"].default_value = 1.45
            p.inputs["Alpha"].default_value = 1.0
            mat.blend_method = "BLEND" if hasattr(mat, "blend_method") else mat.blend_method
        elif grande and tem_textura(p):  # gramado
            p.inputs["Roughness"].default_value = 1.0
            p.inputs["Specular IOR Level"].default_value = 0.1
            ruido_cor(mat, p, 0.35, 0.55, relevo=0.6)
        elif tem_textura(p):  # pisos e tapetes
            rug = p.inputs["Roughness"].default_value
            if rug < 0.9:  # madeira e porcelanato: leve brilho, juntas em relevo
                p.inputs["Roughness"].default_value = 0.38
                p.inputs["Coat Weight"].default_value = 0.15
                p.inputs["Coat Roughness"].default_value = 0.25
                relevo_da_textura(mat, p, 0.25)
            else:  # tapete
                p.inputs["Sheen Weight"].default_value = 0.6
                relevo_da_textura(mat, p, 0.5)
        elif eh_verde(c):  # copas e plantas
            p.inputs["Roughness"].default_value = 0.7
            p.inputs["Subsurface Weight"].default_value = 0.0
            ruido_cor(mat, p, 2.2, 0.7)
        elif eh_claro(c) and p.inputs["Roughness"].default_value >= 0.85:  # paredes e reboco
            ruido_cor(mat, p, 1.2, 0.12, relevo=0.12)
        elif p.inputs["Metallic"].default_value > 0.3:
            p.inputs["Roughness"].default_value = 0.25

# Copas das árvores e arbustos: de poliedro facetado para volume orgânico
tex = bpy.data.textures.new("copa", "CLOUDS")
tex.noise_scale = 0.55
for obj in bpy.data.objects:
    if obj.type != "MESH" or not obj.material_slots:
        continue
    p = principled(obj.material_slots[0].material)
    if not p:
        continue
    c = cor_base(p) if not tem_textura(p) else None
    verde = False
    if c is None:  # depois do ruído a cor passa a vir de um nó; olha o nome do mix
        mix = p.inputs["Base Color"].links[0].from_node
        if mix.type == "MIX" and not mix.inputs["A"].links:
            verde = eh_verde(tuple(mix.inputs["A"].default_value[:3]))
    else:
        verde = eh_verde(c)
    if verde and len(obj.data.polygons) <= 400 and max(obj.dimensions) < 6:
        sub = obj.modifiers.new("sub", "SUBSURF")
        sub.levels = sub.render_levels = 3
        d = obj.modifiers.new("desl", "DISPLACE")
        d.texture = tex
        d.texture_coords = "GLOBAL"
        d.strength = 0.22 * max(obj.dimensions)
        d.mid_level = 0.5
        for pol in obj.data.polygons:
            pol.use_smooth = True

# ------------------------------------------------------------------ câmeras e render
os.makedirs(DESTINO, exist_ok=True)
cams = sorted((o for o in bpy.data.objects if o.type == "CAMERA"), key=lambda o: o.name)
for cam in cams:
    nome = cam.name.split(".")[0]
    if SO and SO not in nome:
        continue
    cam.data.sensor_fit = "VERTICAL"
    cam.data.sensor_height = 24
    cam.data.lens = 12 / math.tan(math.radians(30) / 2)  # campo de visão vertical de 30 graus
    cam.data.clip_start, cam.data.clip_end = 0.1, 500
    cena.camera = cam
    cena.render.filepath = os.path.join(DESTINO, nome + ".png")
    bpy.ops.render.render(write_still=True)
    print("imagem", nome)
