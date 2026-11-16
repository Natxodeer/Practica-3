import unreal
out=[]
def log(v):
 s=str(v); out.append(s); unreal.log(s)
bp=unreal.EditorAssetLibrary.load_asset('/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube')
try:
 scs=bp.simple_construction_script()
 log('SCS '+str(scs)+' DIR '+str([x for x in dir(scs) if 'node' in x.lower() or 'component' in x.lower()]))
 nodes=scs.get_all_nodes()
 for n in nodes:
  log('NODE '+str(n)+' DIR '+str([x for x in dir(n) if 'component' in x.lower() or 'template' in x.lower()]))
  for prop in ['component_template','component_class','variable_name']:
   try: log('NODEPROP '+prop+' '+str(n.get_editor_property(prop)))
   except Exception as e: log('NODEPROPERR '+prop+' '+repr(e))
except Exception as e: log('SCSERR '+repr(e))
with open(r'C:\Users\nacho\Downloads\Practica3\Saved\inspect_scs.txt','w',encoding='utf-8') as f:f.write('\n'.join(out))
