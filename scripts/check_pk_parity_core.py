"""Check the directly reviewed PK parity-core normalization, not general proofs.

All arithmetic regressions use exact fractions. They supplement, rather than
replace, the mathematical review recorded under verifications/.
"""
import argparse
import hashlib
import itertools
import json
import re
import subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'reviews/pk-parity-core-issue2.json').read_text())
state = json.loads((ROOT / 'state.json').read_text())
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--integration-baseline', action='store_true', help='Check this original six-node integration against its baseline; not for later unrelated additions.')
args = parser.parse_args()
baseline = manifest['baseline_commit']
old = json.loads(subprocess.check_output(['git', 'show', baseline + ':state.json'], cwd=ROOT, text=True)) if args.integration_baseline else None


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


nodes = manifest['nodes']
ids = {r['candidate_id'] for r in nodes}
runs = {r['run_id'] for r in nodes}
require(len(nodes) == len(ids) == len(runs) == 6, 'Expected six distinct normalized claims and reviews')
# The ordinary mode validates this chain without freezing the rest of the graph.
# Strict preservation is a one-time integration audit, enabled explicitly.
if args.integration_baseline:
    for family in ('candidates', 'facts', 'runs', 'subgoals'):
        require(all(state[family].get(k) == v for k, v in old[family].items()), 'Existing ledger record changed: ' + family)
    require(set(state['candidates']) - set(old['candidates']) == ids, 'Unexpected candidate additions')
    require(set(state['facts']) - set(old['facts']) == ids, 'Unexpected accepted-fact additions')
    require(set(state['runs']) - set(old['runs']) == runs, 'Unexpected review additions')
    require(state['problem_sha256'] == old['problem_sha256'], 'Locked target changed')
    require(sum(c['status'] == 'pending' for c in state['candidates'].values()) == manifest['original_candidates_pending'], 'Original pending statuses changed')

for r in nodes:
    cid, rid = r['candidate_id'], r['run_id']
    cp, fp, vp = ROOT / 'candidates' / (cid + '.json'), ROOT / 'facts' / (cid + '.md'), ROOT / 'verifications' / (rid + '.json')
    require(digest(cp) == r['sha256'], 'Normalized candidate changed after review: ' + cid)
    require(digest(fp) == r['fact_sha256'], 'Normalized fact changed after review: ' + cid)
    require(digest(vp) == r['verification_sha256'], 'Direct review changed: ' + rid)
    c, v = json.loads(cp.read_text()), json.loads(vp.read_text())
    require(c['depends_on'] == r['depends_on'] == state['facts'][cid]['depends_on'], 'Dependency mismatch: ' + cid)
    require(set(c['depends_on']) <= ids, 'Unexpected dependency outside the reviewed six-node chain')
    require(all(state['facts'][p]['status'] == 'accepted' for p in c['depends_on']), 'Unaccepted premise: ' + cid)
    require(v['verdict'] == 'APPROVED' and v['candidate_id'] == cid, 'Missing direct approval: ' + cid)
    require(v['candidate_sha256'] == digest(cp), 'Review not bound to exact candidate bytes: ' + cid)
    require(v['proof_sha256'] == hashlib.sha256(c['proof'].encode()).hexdigest(), 'Proof hash mismatch: ' + cid)
    require(v['source_candidate_sha256'] == r['source_candidate_sha256'] == c['source_candidate_sha256'], 'Source provenance mismatch')
    for sid, sha in c['source_candidate_sha256'].items():
        require(digest(ROOT / 'candidates' / (sid + '.json')) == sha, 'Intake original changed: ' + sid)
        if args.integration_baseline:
            require(state['candidates'][sid] == old['candidates'][sid], 'Intake status changed: ' + sid)
    text = c['statement'] + c['proof']
    cited = set(re.findall(r'`([0-9a-f]{16})`', text))
    require(cited <= set(c['depends_on']), 'Undeclared mathematical reference: ' + cid)
    require(not any(ord(ch) < 32 and ch not in '\n\t' for ch in text), 'Broken escape/control character: ' + cid)
    require(text.count('$') % 2 == 0, 'Unbalanced math delimiter: ' + cid)
    require('## Statement\n\n' + c['statement'] + '\n## Proof\n\n' + c['proof'] in fp.read_text(), 'Fact does not reproduce reviewed statement/proof: ' + cid)

# In strict integration mode, protect all original mathematical files.
if args.integration_baseline:
    diff = subprocess.check_output(['git', 'diff', '--name-status', baseline, '--', 'facts', 'candidates', 'verifications', 'problem_statement.md'], cwd=ROOT, text=True)
    allowed = {f'facts/{c}.md' for c in ids} | {f'candidates/{c}.json' for c in ids} | {f'verifications/{r}.json' for r in runs}
    for line in diff.splitlines():
        status, path = line.split('\t', 1)
        require(status == 'A' and path in allowed, 'Original mathematical file modified/deleted: ' + line)
index = (ROOT / 'INDEX.md').read_text()
for fid in state['facts']:
    require(index.count(f'[{fid}](facts/{fid}.md)') == 1, 'Fact missing or duplicated in index: ' + fid)

# Exact arithmetic regressions of identities used in the written proofs.
# They are finite calibrations, not substitutes for the dimension-general arguments.
arithmetic_cases = 0
for d in range(2, 61):
    N = d + 1
    J = (N + 1) // 2
    q = N - J + 1
    gamma = F(d, N) ** d
    alpha = (gamma + F(J, N)) / 2
    require(q == N // 2 + 1 and 2 * q > N, 'Row-margin exponent identity')
    require(gamma < F(1, 2) <= F(J, N) and alpha > gamma, 'Strict repair credit gap')
    require(d * F(d, N) ** (d - 1) == N * gamma, 'Simplex coarea density identity')
    e, V = F(1, 1000), F(7, 5)
    credits = [e * F((7 * i) % 11, 11) for i in range(N)]
    mean = sum(credits, F(0)) / N
    rhs = [(c - mean) / (N * gamma * V) for c in credits]
    require(sum(rhs, F(0)) == 0, 'Balanced displacement compatibility')
    require(sum(x*x for x in rhs[1:]) <= d*(e/(N*gamma*V))**2, 'Displacement squared-norm bound')
    arithmetic_cases += 1

reflection_cases = 0
for n in range(1, 7):
    points = [tuple(bit + 2 * (3*i + 5*k)**2 for k, bit in enumerate(bits))
              for i, bits in enumerate(itertools.product((0, 1), repeat=n))]
    by_parity = {tuple(x % 2 for x in p): p for p in points}
    require(len(by_parity) == 2**n, 'Not a complete test transversal')
    point_set = set(points)
    seen = {}
    for w in points:
        for v in points:
            if w == v:
                continue
            p = tuple(2*a-b for a,b in zip(w,v))
            require(p not in point_set, 'Reflected base unexpectedly in its transversal')
            require(by_parity[tuple(x%2 for x in p)] == v, 'Same-parity partner mismatch')
            require(tuple((a+b)//2 for a,b in zip(p,v)) == w, 'Midpoint mismatch')
            require(p not in seen, 'Different target pairs generated the same base')
            seen[p] = (w, v)
            reflection_cases += 1
    require(len(seen) == len(points)*(len(points)-1), 'Reflection pair count')

for n in range(1, 6):
    L = 2**n
    volumes = [F(1) + F((7*i)%5, 1000) for i in range(L)]
    E = F(1, 8)
    avg, m = sum(volumes, F(0))/L, min(volumes)
    require(all(v < avg + E/L for v in volumes), 'Failure-regime test input invalid')
    require(avg < m+(L-1)*E/L and max(volumes) < m+E, 'Failure volume algebra')
    gamma, alpha = F(4,9), F(5,9)
    require((gamma*sum(volumes)+alpha*E)/L > gamma*(sum(volumes)+E)/L, 'Strict averaged surplus')

print('OK: six directly reviewed atomic nodes, exact review hashes, closed dependencies, preserved source bytes and complete current fact index.')
if args.integration_baseline:
    print('OK: strict integration snapshot preserves every original ledger record and mathematical file.')
print(f'OK: {arithmetic_cases} exact dimension calibrations, {reflection_cases} arbitrary-transversal reflection checks, and five strict averaging calibrations.')
print('These checks validate records and finite regressions; mathematical approval is documented in the six direct-review records.')
