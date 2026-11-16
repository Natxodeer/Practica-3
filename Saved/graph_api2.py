import unreal
out=[]
for nm in ['get_graph_editor_by_name','get_graph_editor','create_and_edit_function_graph']:
 out.append(nm+' DOC '+str(getattr(unreal.BlueprintGraphEditor,nm).__doc__))
for path in ['/Game/BP_BowlingBall','/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube']:
 bp=unreal.load_asset(path); out.append('BP '+path+' '+str(bp)+' parent='+str(unreal.BlueprintEditorLibrary.get_blueprint_parent_class(bp)))
 sub=unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
 for i,h in enumerate(sub.k2_gather_subobject_data_for_blueprint(bp)):
  d=sub.k2_find_subobject_data_from_handle(h); o=unreal.SubobjectDataBlueprintFunctionLibrary.get_object(d)
  out.append(' '+str(i)+' '+str(o)+' class='+str(o.get_class().get_name()))
  if o.get_class().get_name()=='StaticMeshComponent': out.append('  mesh='+str(o.get_editor_property('static_mesh')))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\graph_api2.txt','w',encoding='utf8').write('\n'.join(out))
