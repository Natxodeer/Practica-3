import unreal
out=[]
def log(v):
 s=str(v); out.append(s); unreal.log(s)
bp=unreal.EditorAssetLibrary.load_asset('/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube')
try:
 log('PARENT '+str(bp.get_blueprint_parent_class()))
 gc=bp.generated_class(); cdo=unreal.get_default_object(gc)
 log('CDODIR '+str([n for n in dir(cdo) if 'root' in n.lower() or 'component' in n.lower()]))
 for prop in ['root_component','root','components']:
  try:
   v=cdo.get_editor_property(prop); log('PROP '+prop+' '+str(v)+' '+(v.get_class().get_name() if v else ''))
  except Exception as e: log('ERR '+prop+' '+repr(e))
 log('BPEditorLibrary '+str([n for n in dir(unreal.BlueprintEditorLibrary) if 'component' in n.lower() or 'blueprint' in n.lower() or 'compile' in n.lower()]))
except Exception as e: log('ERR '+repr(e))
with open(r'C:\Users\nacho\Downloads\Practica3\Saved\inspect_bp_api4.txt','w',encoding='utf-8') as f:f.write('\n'.join(out))
