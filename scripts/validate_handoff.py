"""Validate the portable handoff; standard library only, no network or platform writes."""
from pathlib import Path
import argparse,hashlib,json,re,sys,urllib.parse
ROOT=Path(__file__).resolve().parents[1]
IGNORE={'.git','__pycache__','node_modules'}
ALLOWED={'.md','.json','.csv','.py'}
SECRET_PATTERNS=[r'gh[pousr]_[A-Za-z0-9]{20,}',r'github_pat_[A-Za-z0-9_]{30,}',r'sk-[A-Za-z0-9_-]{24,}',r'(?i)Bearer\s+[A-Za-z0-9._~-]{20,}',r'(?i)[A-Z]:[\\/]+Users[\\/]+',r'(?i)[?&]xsec_token=[A-Za-z0-9%_~-]{8,}']
def included():
 return sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(x in IGNORE for x in p.relative_to(ROOT).parts) and not p.name.endswith('.local.json') and p.name!='MANIFEST.json')
def records():
 return [{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in included()]
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--refresh-manifest',action='store_true');args=parser.parse_args();errors=[]
 if args.refresh_manifest:
  manifest={'export_date':'2026-11-09','evidence_snapshot_date':'2026-11-08','scope':'Shareable text and aggregate data only; local media and secrets excluded','files':records()};(ROOT/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 manifest=json.loads((ROOT/'MANIFEST.json').read_text('utf-8-sig'));expected={x['path']:x for x in manifest['files']};actual={x['path']:x for x in records()}
 if set(expected)!=set(actual):errors.append('manifest file set differs')
 for key,row in actual.items():
  if expected.get(key)!=row:errors.append('manifest hash/size mismatch: '+key)
 for p in included():
  rel=p.relative_to(ROOT).as_posix()
  if p.suffix not in ALLOWED and p.name not in {'.gitignore','.gitattributes'}:errors.append('unapproved file type: '+rel)
  text=p.read_text('utf-8-sig')
  for pattern in SECRET_PATTERNS:
   if re.search(pattern,text):errors.append('sensitive-pattern candidate: '+rel);break
  if p.suffix=='.json':
   try:json.loads(text)
   except Exception:errors.append('invalid JSON: '+rel)
  if p.suffix=='.md':
   for raw in re.findall(r'\]\((<[^>]+>|[^)]+)\)',text):
    target=raw.strip('<>')
    if target.startswith(('#','https://','http://','mailto:')):continue
    part=urllib.parse.unquote(target.split('#',1)[0]);dest=(p.parent/part).resolve()
    if not dest.is_relative_to(ROOT) or not dest.exists():errors.append('missing/outside Markdown target: '+rel+' -> '+part)
 snap=ROOT/'data/snapshots/2026-11-08';load=lambda name:json.loads((snap/name).read_text('utf-8-sig'))
 notes=load('notes-41.json');registry=load('note-registry-41.json');aud=load('note-audiences.json');timing=load('timing-23.json')['records'];reviews=load('review-evidence-23.json')['records'];acc=load('account.json')['data'];projects=json.loads((ROOT/'data/projects/inventory.json').read_text('utf-8-sig'))
 checks={'notes':len(notes),'unique_notes':len({x['id'] for x in notes}),'eligible':sum(x['views']>=100 and '限制' not in x['status'] for x in notes),'audiences_nonempty':sum(bool(x['gender']) for x in aud),'timing':len(timing),'reviews':len(reviews),'projects':len(projects['records'])}
 if checks!={'notes':41,'unique_notes':41,'eligible':23,'audiences_nonempty':23,'timing':23,'reviews':23,'projects':56}:errors.append('cohort coverage mismatch')
 if sum(x['read_count'] for x in registry)!=36364:errors.append('registry view sum mismatch')
 for k in ['seven','thirty']:
  if sum(x['value'] for x in acc['source_views'][k])!=100:errors.append('view source shares '+k)
 if abs(sum(x['ui_share_pct'] for x in acc['source_follows']['rows'])-100)>1e-6:errors.append('follower source display sum')
 if acc['fans']['female_current_pct']!=39 or acc['periods']['seven']['follows']!=70:errors.append('account fact mismatch')
 if {x['id'] for x in reviews}!={x['id'] for x in timing}:errors.append('review/timing IDs differ')
 output={'status':'pass' if not errors else 'fail','files':len(actual),'bytes':sum(r['bytes'] for r in actual.values()),'coverage':checks,'errors':errors};print(json.dumps(output,ensure_ascii=False,indent=2));return 1 if errors else 0
if __name__=='__main__':sys.exit(main())
