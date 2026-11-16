import unreal
out=[]
for path,fn in [('/Game/BP_BowlingBallXR','AlLanzar'),('/Game/BP_BowlingPinXR','AlCaer'),('/Game/BP_BowlingBall','MostrarMensaje')]:
 bp=unreal.load_asset(path)
 if bp and fn in [str(n) for n in unreal.BlueprintEditorLibrary.list_graph_names(bp)]:
  unreal.BlueprintEditorLibrary.remove_function_graph(bp,fn)
  unreal.EditorAssetLibrary.save_asset(path)
  out.append(path+' removed '+fn)
pin=unreal.load_asset('/Game/BP_BowlingPinXR')
try:
 event=unreal.BlueprintEditorLibrary.add_event_override(pin,'ReceiveHit',unreal.IntPoint(-400,100))
 ge=unreal.BlueprintGraphEditor.get_graph_editor_by_name(pin,'EventGraph')
 destroy=ge.add_call_function_node('/Script/Engine.Actor.DestroyActor')
 unreal.BlueprintEditorLibrary.find_then_pin(event).try_create_connection(unreal.BlueprintEditorLibrary.find_execute_pin(destroy))
 destroy.set_node_pos(unreal.IntPoint(-100,100))
 ok=unreal.BlueprintEditorLibrary.compile_blueprint(pin)
 unreal.EditorAssetLibrary.save_asset('/Game/BP_BowlingPinXR')
 out.append('pin hit->destroy compile='+str(ok))
except Exception as e: out.append('PIN ERROR '+repr(e))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\mechanics_log.txt','w',encoding='utf8').write('\n'.join(out))
