"""Offline checks for Issue #1 evidence boundaries. Does not fetch sites or touch media."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import subprocess
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/research'


def load_json(name):
    return json.loads((DATA / name).read_text(encoding='utf-8-sig'))


def load_csv(name):
    with (DATA / name).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def main():
    errors = []
    log = load_json('research-access-log-20261109.json')
    rows = load_csv('primary-source-evidence-ledger-20261109.csv')
    candidates = load_csv('xhs-competitor-candidates-20261109.csv')
    costs = load_csv('resource-cost-fields-20261109.csv')
    flags = load_json('metric-consistency-check-20261109.json')
    by_id = {r['id']: r for r in rows}
    if len(rows) != len(by_id):
        errors.append('duplicate evidence ids')
    required = {'id', 'type', 'URL', 'author_or_publisher', 'content_date', 'checked_at', 'platform',
                'access_status', 'observed_fields', 'window', 'evidence_tier', 'limitations', 'decision_use'}
    if not required.issubset(rows[0]):
        errors.append('missing ledger fields')
    categories = set()
    for row in rows:
        categories.update(row['category'].split(';'))
        if row['checked_at'] != '2026-11-09' or urlparse(row['URL']).scheme != 'https':
            errors.append('invalid date/url: ' + row['id'])
        if row['parent_evidence_id'] and row['parent_evidence_id'] not in by_id:
            errors.append('unresolved evidence parent: ' + row['id'])
        if not row['limitations'] or not row['decision_use']:
            errors.append('missing evidence boundary: ' + row['id'])
    if not set('ABCDEFG').issubset(categories):
        errors.append('A-G coverage incomplete')
    docs = [r for r in rows if r['type'] == 'external_document']
    statistics = log['source_statistics']
    counts = dict(Counter(r['access_status'] for r in docs))
    if len(docs) != statistics['external_documents'] or counts != statistics['exclusive_access_status_counts']:
        errors.append('external source count mismatch')
    if len(rows) != statistics['evidence_ledger_rows'] or len(rows) != 45:
        errors.append('ledger total mismatch')
    figures = [r for r in rows if r['type'] == 'reference_figure']
    if len(figures) != 3 or any(len(r['local_reference_sha256']) != 64 for r in figures):
        errors.append('reference figure count/hash mismatch')
    for c in candidates:
        if c['source_evidence_id'] not in by_id:
            errors.append('candidate source missing: ' + c['candidate_id'])
        if c['qualification_status'] != 'archival_lead_not_verified':
            errors.append('unsupported qualification: ' + c['candidate_id'])
        if any(c[k] for k in ['author_id', 'profile_url', 'note_id', 'note_url', 'published_at',
                               'current_follower_count', 'current_visible_metrics', 'metrics_as_of']):
            errors.append('unverified field populated: ' + c['candidate_id'])
        if c['outlier_status'] != 'unassessable_no_baseline' or c['baseline_n'] != '0':
            errors.append('unobserved baseline claimed: ' + c['candidate_id'])
        if c['video_playable'] != 'not_tested_no_original':
            errors.append('unverified playback claimed: ' + c['candidate_id'])
    if len(candidates) != 9 or sum(c['selected_for_metadata_case'] == 'True' for c in candidates) != 6:
        errors.append('candidate/card count mismatch')
    if any(log['achieved'][k] != 0 for k in ['verified_accounts', 'verified_public_notes', 'verified_outliers',
            'full_verified_cases', 'actual_video_playbacks', 'raw_comment_samples']):
        errors.append('unsupported completion count')
    if any(log['safety_scope'].values()):
        errors.append('research scope exceeded')
    for c in costs:
        if any(c[k] for k in ['project_id', 'actual_minutes', 'external_cost_amount', 'revision_count',
                              'license_proof_reference']):
            errors.append('invented historical cost/license')
    if len(costs) != 7:
        errors.append('cost stage schema mismatch')
    expected = {'6ab93a8f000000001b032079', '6ab93a7c000000001a030f02'}
    if {r['note_id'] for r in flags['flagged_records']} != expected or flags['inspected_indexed_notes'] != 23:
        errors.append('conditional flag cohort mismatch')
    for record in flags['flagged_records']:
        lower = record['completion_pct'] * record['indexed_duration_seconds'] / 100
        if abs(lower - record['conditional_lower_bound_seconds']) > 1e-8:
            errors.append('conditional formula mismatch')
        if record['average_watch_seconds'] >= lower or record['original_fields_modified']:
            errors.append('invalid conditional flag')
    for rel, expected_hash in log['snapshots_before_sha256'].items():
        raw = (ROOT / rel).read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected_hash:
            errors.append('snapshot changed since research start: ' + rel)
        baseline = subprocess.run(['git', 'show', log['base_commit'] + ':' + rel], cwd=ROOT,
                                  capture_output=True, check=False)
        if baseline.returncode != 0 or baseline.stdout != raw:
            errors.append('snapshot differs from pinned Git baseline: ' + rel)
    report_names = ['industry-primary-source-audit-20261109.md', 'xhs-competitor-outlier-sample-20261109.md',
                    'industry-ops-gap-and-priorities-20261109.md', 'CODEX-COMPLETION-20261109.md']
    for name in report_names:
        if not (ROOT / 'reports' / name).exists():
            errors.append('missing required report: ' + name)
    # The contract lists four substantive reports plus the evidence ledger: no extra fifth report is invented.
    allowed = {'PROJECT-STATE.md', 'CHANGELOG.md', 'MANIFEST.json', 'scripts/validate_research_audit.py'}
    diff = subprocess.check_output(['git', 'diff', '--name-only', log['base_commit']], cwd=ROOT,
                                   text=True, encoding='utf-8').splitlines()
    untracked = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], cwd=ROOT,
                                        text=True, encoding='utf-8').splitlines()
    for rel in set(diff + untracked):
        if rel not in allowed and rel not in {'reports/' + n for n in report_names} and not rel.startswith('data/research/'):
            errors.append('out-of-scope change: ' + rel)
    result = dict(status='pass' if not errors else 'fail', evidence_rows=len(rows),
                  external_documents=len(docs), access_status_counts=counts, archival_candidates=len(candidates),
                  metadata_cards=6, verified_public_notes=0, full_verified_cases=0,
                  original_comment_samples=0, conditional_flags=len(flags['flagged_records']),
                  snapshot_files_byte_identical_to_base=len(log['snapshots_before_sha256']),
                  scope='offline structure/arithmetic/immutability; not live source revalidation or audiovisual review',
                  errors=errors)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
