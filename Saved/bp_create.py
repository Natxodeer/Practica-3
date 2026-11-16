import unreal
out=[]
path='/Game/BP_BowlingBall'
bp=unreal.load_asset(path)
if not bp:
 out.append('ERROR: asset not found')
else:
 try:
  ge=unreal.BlueprintGraphEditor.create_and_edit_function_graph(bp,'MostrarMensaje')
  entry=ge.find_graph_entry_pin()
  node=ge.add_call_function_node('/Script/Engine.KismetSystemLibrary.PrintString')
  node.find_input_pin('InString').set_pin_value('¡Lanza la bola a los bolos!')
  entry.try_create_connection(node.find_execute_pin())
  node.set_node_pos(unreal.IntPoint(300,0))
  ok=unreal.BlueprintEditorLibrary.compile_blueprint(bp)
  out.append('compile='+str(ok))
  unreal.EditorAssetLibrary.save_asset(path)
  out.append('saved='+str(unreal.EditorAssetLibrary.does_asset_exist(path)))
  out.append('graphs='+str(unreal.BlueprintEditorLibrary.list_graph_names(bp)))
 except Exception as e: out.append('ERROR '+repr(e))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\bp_create_result.txt','w',encoding='utf8').write('\n'.join(out))
