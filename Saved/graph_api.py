import unreal
out=[]
for nm in ['BlueprintGraphEditor','BlueprintGraphPin','BlueprintEditorLibrary']:
 c=getattr(unreal,nm)
 out.append('CLASS '+nm+' '+str(c.__doc__))
 out.append('DIR '+repr([x for x in dir(c) if not x.startswith('_')]))
 for f in ['create','add_branch_node','add_call_function_node','add_custom_event_node','add_comment_node','connect_pins','connect_nodes','add_get_member_variable_node','add_set_member_variable_node']:
  if hasattr(c,f): out.append(f+' DOC '+str(getattr(c,f).__doc__))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\graph_api.txt','w',encoding='utf8').write('\n'.join(out))
