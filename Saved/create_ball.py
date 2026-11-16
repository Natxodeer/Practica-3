import unreal
out=[]
bp=unreal.load_asset('/Game/BP_BowlingBall')
sub=unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
handles=sub.k2_gather_subobject_data_for_blueprint(bp)
mesh=unreal.load_asset('/Game/mesh/bolos/bowling_pin_ball')
out.append('mesh='+str(mesh))
try:
 p=unreal.AddNewSubobjectParams(parent_handle=handles[1],new_class=unreal.StaticMeshComponent,blueprint_context=bp)
 out.append('params='+str(p))
 res=sub.add_new_subobject(p)
 out.append('res='+repr(res)+' type='+str(type(res)))
 hs=sub.k2_gather_subobject_data_for_blueprint(bp)
 for i,h in enumerate(hs):
  d=sub.k2_find_subobject_data_from_handle(h)
  o=unreal.SubobjectDataBlueprintFunctionLibrary.get_object(d)
  out.append('obj%d %s %s'%(i,o,o.get_class().get_name()))
  if o.get_class().get_name()=='StaticMeshComponent':
   o.set_editor_property('static_mesh',mesh)
   o.set_editor_property('simulate_physics',True)
   o.set_editor_property('mobility',unreal.ComponentMobility.MOVABLE)
   out.append('set mesh '+str(o.get_editor_property('static_mesh')))
 unreal.BlueprintEditorLibrary.compile_blueprint(bp)
 unreal.EditorAssetLibrary.save_asset('/Game/BP_BowlingBall')
except Exception as e: out.append('ERR '+repr(e))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\create_ball_log.txt','w',encoding='utf8').write('\n'.join(out))
