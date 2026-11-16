import unreal
out=[]
def log(v):
 s=str(v); out.append(s); unreal.log(s)
lib=unreal.SubobjectDataBlueprintFunctionLibrary
log('LIB '+str([x for x in dir(lib) if not x.startswith('_')]))
bp=unreal.EditorAssetLibrary.load_asset('/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube')
ss=unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
for i,h in enumerate(ss.k2_gather_subobject_data_for_blueprint(bp)):
 log('H '+str(i))
 for fn in ['get_object','get_display_name','get_class','is_component','is_root','get_component_template']:
  try: log(fn+' '+str(getattr(lib,fn)(h)))
  except Exception as e: log(fn+' ERR '+repr(e))
with open(r'C:\Users\nacho\Downloads\Practica3\Saved\inspect_subobject3.txt','w',encoding='utf-8') as f:f.write('\n'.join(out))
