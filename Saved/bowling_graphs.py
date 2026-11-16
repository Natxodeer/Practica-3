import unreal
out=[]
for path,func,msg in [('/Game/BP_BowlingBallXR','AlLanzar','¡Lanza la bola a los bolos!'),('/Game/BP_BowlingPinXR','AlCaer','¡Bolo derribado!')]:
 bp=unreal.load_asset(path)
 try:
  ge=unreal.BlueprintGraphEditor.create_and_edit_function_graph(bp,func)
  entry=ge.find_graph_entry_pin()
  node=ge.add_call_function_node('/Script/Engine.KismetSystemLibrary.PrintString')
  node.find_input_pin('InString').set_pin_value(msg)
  entry.try_create_connection(node.find_execute_pin())
  node.set_node_pos(unreal.IntPoint(300,0))
  ok=unreal.BlueprintEditorLibrary.compile_blueprint(bp)
  unreal.EditorAssetLibrary.save_asset(path)
  out.append(path+' compile='+str(ok)+' saved')
 except Exception as e: out.append(path+' ERR '+repr(e))
# Open the ball Blueprint so its components and graphs are visible.
unreal.EditorAssetLibrary.open_editor_for_asset(unreal.load_asset('/Game/BP_BowlingBallXR'))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\bowling_graphs_log.txt','w',encoding='utf8').write('\n'.join(out))
