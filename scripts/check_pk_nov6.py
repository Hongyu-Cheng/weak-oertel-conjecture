"""Validate the PK intake's records and supporting files, not its mathematics."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'assets/pk-nov6'
manifest = json.loads((DATA / 'intake.json').read_text())
state = json.loads((ROOT / 'state.json').read_text())


def require(ok, message):
    if not ok:
        raise SystemExit(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def path_for(relative):
    path = (ROOT / relative).resolve()
    require(ROOT in path.parents, 'Path escapes repository: ' + relative)
    require(path.is_file(), 'Missing file: ' + relative)
    return path


seen = set()
for record in manifest['records']:
    cid = record['candidate_id']
    require(cid not in seen, 'Duplicate candidate ID: ' + cid)
    seen.add(cid)
    path = path_for('candidates/' + cid + '.json')
    require(digest(path) == record['candidate_sha256'], 'Candidate hash: ' + cid)
    candidate = json.loads(path.read_text())
    require(candidate['intake_batch'] == manifest['batch'], 'Batch mismatch: ' + cid)
    require(candidate['source_sha256'] == record['source_sha256'], 'Source hash: ' + cid)
    require(state['candidates'][cid]['status'] in {'pending', 'rejected'}, 'Unnormalized note accepted: ' + cid)
    require(not state['candidates'][cid]['runs'], 'Historical review promoted to a run: ' + cid)
    require(set(candidate['unaccepted_references']) <= state['candidates'].keys(), 'Missing candidate reference: ' + cid)
    require(set(candidate['related_facts']) <= state['facts'].keys(), 'Missing related fact: ' + cid)
    require(set(candidate['depends_on']) <= state['facts'].keys(), 'Unaccepted predecessor: ' + cid)
    for relative in candidate.get('historical_review_comments', []):
        comment = json.loads(path_for(relative).read_text())
        require(cid in comment['candidate_references'], 'Nonreciprocal review comment: ' + cid)
    # References not in the formal dependency list remain explicitly pending.
    text_ids = set(re.findall(r'\bcandidate ([0-9a-f]{16})\b', candidate['proof']))
    require(text_ids <= state['candidates'].keys(), 'Dangling proof reference: ' + cid)

files = manifest['supporting_files'] + manifest.get('historical_review_comments', [])
for item in files:
    path = path_for(item['path'])
    require(digest(path) == item['sha256'], 'Asset hash: ' + item['path'])
    if '/review-comments/' in item['path']:
        comment = json.loads(path.read_text())
        require(comment['is_approval'] is False and comment['review_executed_for_this_intake'] is False, 'Invented review approval')
        require(set(comment['candidate_references']) <= seen, 'Missing review subject')
        for cid in comment['candidate_references']:
            candidate = json.loads((ROOT / 'candidates' / (cid + '.json')).read_text())
            require(item['path'] in candidate['historical_review_comments'], 'Missing reciprocal review reference')

private = re.compile(r'/(?:Users|home|root)/|/tmp/oertel-|My Drive|chatgpt\.com/(?:c|share)/|claude\.ai/(?:chat|share)/|codex://|\bgh[pousr]_[A-Za-z0-9]{20,}|\bgithub_pat_[A-Za-z0-9_]{20,}', re.I)
paths = [ROOT / 'candidates' / (cid + '.json') for cid in seen]
paths += [p for p in DATA.rglob('*') if p.is_file() and p.suffix != '.npz']
for path in paths:
    require(not private.search(path.read_text()), 'Private context: ' + str(path.relative_to(ROOT)))

for path in (DATA / 'computations').glob('*.py'):
    compile(path.read_text(), str(path.relative_to(ROOT)), 'exec')
print('OK: %s pending mathematical submissions; %s supporting files; %s historical mathematical comments.' % (
    len(seen), len(manifest['supporting_files']), len(manifest.get('historical_review_comments', []))))
print('Packaging and reference checks only; no mathematical approval.')
