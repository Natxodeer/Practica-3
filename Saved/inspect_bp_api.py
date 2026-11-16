import unreal
out=[]
def log(v):
    s=str(v); out.append(s); unreal.log(s)
bp=unreal.EditorAssetLibrary.load_asset('/Game/XRFramework/Blueprints/BP_Grabbable_SmallCube')
log('BP DIR '+str([n for n in dir(bp) if 'class' in n.lower() or 'component' in n.lower()]))
for prop in ['generated_class','simple_construction_script','parent_class']:
    try:
        v=bp.get_editor_property(prop); log('PROP '+prop+' '+str(v)+' '+str(type(v)))
        if prop=='generated_class' and v:
            log('CLASS DIR '+str([n for n in dir(v) if 'default' in n.lower() or 'component' in n.lower()]))
            try:
                cdo=unreal.get_default_object(v); log('CDO '+str(cdo))
                log('CDO DIR '+str([n for n in dir(cdo) if 'component' in n.lower()]))
                try:
                    comps=cdo.get_components_by_class(unreal.ActorComponent)
                    for c in comps: log('COMP '+c.get_name()+' '+c.get_class().get_name())
                except Exception as e: log('COMP ERR '+repr(e))
            except Exception as e: log('CDO ERR '+repr(e))
    except Exception as e: log('PROP ERR '+prop+' '+repr(e))
log('UNREAL HELPERS '+str([n for n in dir(unreal) if 'default_object' in n.lower() or 'blueprint' in n.lower() and 'library' in n.lower()]))
with open(r'C:\Users\nacho\Downloads\Practica3\Saved\inspect_bp_api.txt','w',encoding='utf-8') as f:f.write('\n'.join(out))
