"""Exact certificate; uses the previously audited exhaustive base verifier."""
from fractions import Fraction as F
from pathlib import Path
from contextlib import redirect_stdout
import io
import runpy
import sympy as s

root = Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    data = runpy.run_path(str(root / 'verify_actual_thirteen_point_strict_minor_quotas_two_sided.py'))
P, w, reps = data['P'], data['w'], data['rep_rows']
checks = 0

def check(test):
    global checks
    assert test
    checks += 1

tight = []
mat = []
for p, ids, lam in reps:
    gap = w[p] - sum(F(t) * w[j] for j, t in zip(ids, lam))
    check(gap >= 0)
    if gap == 0:
        tight.append((p, ids, lam))
        row = [F(0)] * len(P)
        row[p] = 1
        for j, t in zip(ids, lam):
            row[j] -= F(t)
        mat.append(row)

check(len(tight) == 22)
L = s.Matrix(mat)
check(L.rank() == 7)
check(len(P) - L.rank() == 6)
aff = s.Matrix([[1, *p] for p in P])
check(aff.rank() == 4)
check(aff.row_join(s.Matrix(w)).rank() == 5)
check(w[5] - (w[2] + w[11]) / 2 == F(19, 7280))
check(all(2 * P[5][j] == P[2][j] + P[11][j] for j in range(3)))

I = {3,4,5,6,7,8,9,10,11}
check(len(I) == 9)
for p, ids, lam in tight:
    check(not set(ids) <= I)
check(len({tuple(x % 2 for x in p) for p in P}) == 7)

eps = F(1,100)
for p, ids, lam in reps:
    gap = w[p] - sum(F(t) * w[j] for j,t in zip(ids,lam))
    shift = eps * w[p] - sum(F(t) * eps * w[j] for j,t in zip(ids,lam))
    check(abs(shift) <= gap / 2)
check((F(1,2)-eps)/7 > F(1,16))
check((F(1,2)-eps)/7 > F(4,9)/7)
check(all(w[j+1]-w[j] == -F(143,14560) for j in (1,2,3)))
check(min(w[1]+w[2],w[2]+w[3]+w[4])/2 == F(443,5824))
check(F(443,5824)-F(1,14) == F(27,5824))
check(sum(w[1:5]) == F(1929,7280) < F(2,7))

# Exact atomic depth: a finite complement B is strictly separable from
# the candidate iff that candidate does not lie in conv(B).
supports = [[] for _ in P]
for p,ids,lam in tight:
    supports[p].append(sum(1 << j for j in ids))
weights = [F(0)] * (1 << len(P))
for mask in range(1,len(weights)):
    bit = mask & -mask
    weights[mask] = weights[mask-bit] + w[bit.bit_length()-1]
depths = []
for p in range(len(P)):
    largest_complement = max(weights[mask] for mask in range(len(weights))
        if not (mask >> p & 1)
        and not any(mask & support == support for support in supports[p]))
    depths.append(1-largest_complement)
check(max(depths) == depths[2] == F(443,2912))
check(max(depths) > F(1,7))
print('PASS', checks, 'new exact checks; inherited 2112-check quota certificate; 22 tight rows, rank7, nine-point graph witness')
