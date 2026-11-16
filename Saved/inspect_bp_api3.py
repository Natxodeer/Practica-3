import unreal
out=[]
def log(v):
 s=str(v); out.append(s); unreal.log(s)
bp=unreal.EditorAssetLibrary.load_asset('/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube')
try:
 gc=bp.generated_class()
 log('GEN '+str(gc)+' type '+str(type(gc)))
 cdo=unreal.get_default_object(gc)
 log('CDO '+str(cdo)+' class '+cdo.get_class().get_name())
 for c in cdo.get_components_by_class(unreal.ActorComponent):
  log('COMP '+c.get_name()+' '+c.get_class().get_name())
  if isinstance(c,unreal.StaticMeshComponent):
   sm=c.get_editor_property('static_mesh'); log('SM '+(sm.get_name() if sm else 'NONE'))
except Exception as e: log('ERROR '+repr(e))
with open(r'C:\Users\nacho\Downloads\Practica3\Saved\inspect_bp_api3.txt','w',encoding='utf-8') as f:f.write('\n'.join(out))
