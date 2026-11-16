import unreal
out=[]
bp=unreal.load_asset('/Game/BP_BowlingBall')
grab=unreal.load_asset('/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube')
base=unreal.BlueprintEditorLibrary.generated_class(grab)
out.append('base='+str(base))
try:
 unreal.BlueprintEditorLibrary.reparent_blueprint(bp,base)
 out.append('reparented')
 sub=unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
 for i,h in enumerate(sub.k2_gather_subobject_data_for_blueprint(bp)):
  d=sub.k2_find_subobject_data_from_handle(h); o=unreal.SubobjectDataBlueprintFunctionLibrary.get_object(d)
  lib=unreal.SubobjectDataBlueprintFunctionLibrary
  out.append('%d %s %s comp=%s inherited=%s'%(i,o,o.get_class().get_name(),lib.is_component(d),lib.is_inherited_component(d)))
  if o.get_class().get_name()=='StaticMeshComponent':
   out.append('before='+str(o.get_editor_property('static_mesh')))
   o.set_editor_property('static_mesh',unreal.load_asset('/Game/mesh/bolos/bowling_pin_ball'))
   out.append('after='+str(o.get_editor_property('static_mesh')))
 ok=unreal.BlueprintEditorLibrary.compile_blueprint(bp); out.append('compile='+str(ok))
 unreal.EditorAssetLibrary.save_asset('/Game/BP_BowlingBall'); out.append('saved')
except Exception as e: out.append('ERR='+repr(e))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\ball_reparent_log.txt','w',encoding='utf8').write('\n'.join(out))
