import unreal
out=[]
for path,name,msg in [('/Game/BP_BowlingBallXR','AlLanzar','Lanza la bola hacia los bolos'),('/Game/BP_BowlingPinXR','AlCaer','Bolo derribado')]:
 bp=unreal.load_asset(path)
 try:
  ge=unreal.BlueprintGraphEditor.create_and_edit_function_graph(bp,name)
  entry=ge.find_graph_entry_pin()
  node=ge.add_call_function_node('/Script/Engine.KismetSystemLibrary.PrintString')
  node.find_input_pin('InString').set_pin_value(msg)
  entry.try_create_connection(node.find_execute_pin())
  node.set_node_pos(unreal.IntPoint(300,0))
  ok=unreal.BlueprintEditorLibrary.compile_blueprint(bp)
  unreal.EditorAssetLibrary.save_asset(path)
  check=unreal.BlueprintGraphEditor.get_graph_editor_by_name(bp,name)
  out.append(path+' compile='+str(ok)+' graphs='+str(unreal.BlueprintEditorLibrary.list_graph_names(bp))+' nodes='+str(len(check.list_all_nodes())))
 except Exception as e: out.append(path+' ERROR '+repr(e))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\verify_bowling_nodes.txt','w',encoding='utf8').write('\n'.join(out))
