import unreal
out = []
def log(s):
    out.append(str(s))
    unreal.log(str(s))
paths = [
    '/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube',
    '/Game/mesh/bolos/bowling',
    '/Game/mesh/bolos/bowling_pin_ball',
    '/Game/mesh/dardos/SM_DartboardDarts_Cylinder',
    '/Game/mesh/dardos/SM_DartboardDarts_Cylinder_001',
    '/Game/mesh/Mr_Potato/Señor_potato_29_Cuerpo',
    '/Game/mesh/Mr_Potato/Señor_potato_29_Gorra',
    '/Game/mesh/pinata/pinata_mesh'
]
for p in paths:
    a = unreal.EditorAssetLibrary.load_asset(p)
    log('ASSET %s => %s' % (p, a.get_class().get_name() if a else 'MISSING'))
base = unreal.EditorAssetLibrary.load_asset(paths[0])
try:
    cls = unreal.BlueprintEditorLibrary.get_blueprint_generated_class(base)
    log('GENERATED CLASS %s' % cls.get_name())
    cdo = unreal.get_default_object(cls)
    for c in cdo.get_components_by_class(unreal.ActorComponent):
        log('COMP %s %s' % (c.get_name(), c.get_class().get_name()))
        if isinstance(c, unreal.StaticMeshComponent):
            log('MESH %s' % (c.get_editor_property('static_mesh').get_name() if c.get_editor_property('static_mesh') else 'NONE'))
except Exception as e:
    log('BLUEPRINT INSPECT ERROR %s' % repr(e))
with open(r'C:\Users\nacho\Downloads\Practica3\Saved\inspect_practice.txt','w',encoding='utf-8') as f:
    f.write('\n'.join(out))
