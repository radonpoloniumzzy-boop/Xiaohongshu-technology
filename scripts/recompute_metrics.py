"""Recompute core metrics from the archived snapshot. No network or filesystem mutation."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1];snap=root/'data/snapshots/2026-11-08';d=json.loads((snap/'account.json').read_text('utf-8-sig'))['data'];p=d['periods'];rows=[]
for name in ['previous_seven','seven','thirty']:
 r=p[name];rows.append({'window':name,'views':r['views'],'follows':r['follows'],'follows_per_1000_views':round(r['follows']/r['views']*1000,4),'likes_per_1000_views':round(r['likes']/r['views']*1000,4),'saves_per_1000_views':round(r['saves']/r['views']*1000,4)})
registry=json.loads((snap/'note-registry-41.json').read_text('utf-8-sig'));total=sum(r['read_count'] for r in registry);top=max(registry,key=lambda r:r['read_count']);out={'periods':rows,'cumulative_top_note':{'title':top['title'],'views':top['read_count'],'all_visible_views':total,'share_pct':round(top['read_count']/total*100,4),'not_a_monthly_share':True},'follower_source_display':d['source_follows']['rows'],'scope':'Count density, not unique-user conversion. Follower-source window unknown.'};print(json.dumps(out,ensure_ascii=False,indent=2))
