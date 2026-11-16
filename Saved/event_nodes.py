import unreal
out=[]
for path,msg in [('/Game/BP_BowlingBallXR','Bola de bolos lista. Agarrala y lanzala.'),('/Game/BP_BowlingPinXR','Bolos listos para derribar.')]:
 bp=unreal.load_asset(path)
 try:
  ge=unreal.BlueprintGraphEditor.get_graph_editor_by_name(bp,'EventGraph')
  begin=None
  for n in ge.list_all_nodes():
   title=unreal.BlueprintEditorLibrary.get_node_title(n)
   if str(title).lower()=='event beginplay': begin=n; break
  if not begin: raise Exception('BeginPlay node not found')
  call=ge.add_call_function_node('/Script/Engine.KismetSystemLibrary.PrintString')
  call.find_input_pin('InString').set_pin_value(msg)
  ge.find_then_pin(begin).try_create_connection(call.find_execute_pin())
  call.set_node_pos(unreal.IntPoint(480,80))
  ok=unreal.BlueprintEditorLibrary.compile_blueprint(bp)
  unreal.EditorAssetLibrary.save_asset(path)
  out.append(path+' compile='+str(ok)+' nodes='+str(len(ge.list_all_nodes())))
 except Exception as e: out.append(path+' ERR '+repr(e))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\event_nodes_log.txt','w',encoding='utf8').write('\n'.join(out))
