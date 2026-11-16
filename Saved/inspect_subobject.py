import unreal
out=[]
def log(v):
 s=str(v); out.append(s); unreal.log(s)
bp=unreal.EditorAssetLibrary.load_asset('/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube')
try:
 ss=unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
 log('SUBSYSTEM '+str(ss)+' DIR '+str([x for x in dir(ss) if 'subobject' in x.lower() or 'handle' in x.lower()]))
 handles=ss.k2_gather_subobject_data_for_blueprint(bp)
 log('HANDLES '+str(len(handles)))
 for h in handles:
  d=ss.k2_find_subobject_data_from_handle(h)
  log('HANDLE '+str(h)+' DATA '+str(d))
  if d:
   log('DATA DIR '+str([x for x in dir(d) if not x.startswith('_')]))
   for p in ['object','handle','display_name','class','parent_handle']:
    try: log('DATAPROP '+p+' '+str(d.get_editor_property(p)))
    except Exception as e: pass
except Exception as e:log('ERROR '+repr(e))
with open(r'C:\Users\nacho\Downloads\Practica3\Saved\inspect_subobject.txt','w',encoding='utf-8') as f:f.write('\n'.join(out))
