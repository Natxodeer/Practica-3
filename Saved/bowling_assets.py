import unreal
out=[]
tools=unreal.EditorAssetLibrary
src='/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube'
items=[('/Game/BP_BowlingBallXR','/Game/mesh/bolos/bowling_pin_ball'),('/Game/BP_BowlingPinXR','/Game/mesh/bolos/bowling')]
sub=unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
for dst,meshpath in items:
 try:
  bp=tools.load_asset(dst)
  if not bp:
   bp=tools.duplicate_asset(src,dst)
  if not bp: raise Exception('duplicate failed')
  mesh=tools.load_asset(meshpath)
  handles=sub.k2_gather_subobject_data_for_blueprint(bp)
  for h in handles:
   data=sub.k2_find_subobject_data_from_handle(h)
   obj=unreal.SubobjectDataBlueprintFunctionLibrary.get_object(data)
   if obj and obj.get_class().get_name()=='StaticMeshComponent':
    obj.set_editor_property('static_mesh',mesh)
    obj.set_editor_property('simulate_physics',True)
    obj.set_editor_property('mobility',unreal.ComponentMobility.MOVABLE)
    obj.set_editor_property('collision_profile_name','PhysicsActor')
    out.append(dst+' mesh='+str(obj.get_editor_property('static_mesh')))
  ok=unreal.BlueprintEditorLibrary.compile_blueprint(bp)
  tools.save_asset(dst)
  out.append(dst+' compile='+str(ok)+' saved')
 except Exception as e: out.append(dst+' ERROR '+repr(e))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\bowling_assets_log.txt','w',encoding='utf8').write('\n'.join(out))
