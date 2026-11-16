import unreal
out=[]
def log(v):
 s=str(v); out.append(s); unreal.log(s)
bp=unreal.EditorAssetLibrary.load_asset('/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube')
ss=unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
for i,h in enumerate(ss.k2_gather_subobject_data_for_blueprint(bp)):
 d=ss.k2_find_subobject_data_from_handle(h)
 log('HANDLE %d DICT %s'%(i,str(d.to_dict())))
 log('TUPLE %s'%str(d.to_tuple()))
with open(r'C:\Users\nacho\Downloads\Practica3\Saved\inspect_subobject2.txt','w',encoding='utf-8') as f:f.write('\n'.join(out))
