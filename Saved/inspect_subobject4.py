import unreal
out=[]
bp=unreal.load_asset('/Game/BP_BowlingBall')
sub=unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
handles=sub.k2_gather_subobject_data_for_blueprint(bp)
lib=unreal.SubobjectDataBlueprintFunctionLibrary
for i,h in enumerate(handles):
 d=sub.k2_find_subobject_data_from_handle(h)
 out.append('H%d type=%s data=%s'%(i,type(h),type(d)))
 for fn in ['get_object','get_display_name','get_class','is_component','is_root_component','is_default_scene_root']:
  try: out.append(fn+'='+str(getattr(lib,fn)(d)))
  except Exception as e: out.append(fn+' ERR '+repr(e))
out.append('subdir='+str([x for x in dir(sub) if not x.startswith('_')]))
open(r'C:\Users\nacho\Downloads\Practica3\Saved\inspect_subobject4.txt','w',encoding='utf8').write('\n'.join(out))
