"""Independent source-signature, transport, and finite-absorption checks."""
from submission_text import read_submission
from fractions import Fraction as F
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
checks = 0


def require(value):
    global checks
    assert value
    checks += 1


beta = F(40, 93)
P = [(x, y) for x in range(-4, 5) for y in range(-4, 5)
     if min(-x-y, 2*x-y, 2*y-x) >= -4]
require(len(P) == 31)
coefficients = {}
high, low = [], []
for x, y in P:
    ell = (-x-y, 2*x-y, 2*y-x)
    values = []
    for tier in range(3):
        t = F(2*tier+1, 6)
        lambdas = (F(0), t, 1-t)
        captured = sum(lambdas[i] - F(1, 3) + ell[i] >= 0
                       for i in range(3))
        require(captured in (1, 2))
        values.append(F(captured, 3))
        (high if captured == 2 else low).append([x, y, tier])
    coefficient = 120 * (1 - sum(values) / (3*beta))
    require(coefficient.denominator == 1)
    coefficients[x, y] = coefficient

computed = []
for x in range(-4, 5):
    row = [F(0)] * 6
    for z, coefficient in coefficients.items():
        if z[0] != x:
            continue
        xx, yy = z
        for j, monomial in enumerate((1, xx, yy, xx*xx, xx*yy, yy*yy)):
            row[j] += coefficient * monomial
    computed.append([x] + row)

# Parse the actual printed table instead of duplicating its constants.
source = read_submission('8ac2ff347361aad9')
printed = []
for line in source.splitlines():
    if re.fullmatch(r"\|-?\d+(?:\|-?\d+){6}\|", line.strip()):
        printed.append([F(v) for v in line.strip().strip("|").split("|")])
require(computed == printed)
totals = [sum(row[j] for row in computed) for j in range(1, 7)]
require(totals == [0, 0, 0, 1420, 524, 1420])
require((totals[3] + totals[5])/120 == F(71, 3))

# Reconstruct the source-to-full-capacity stress from the saved exact flow.
data = json.loads((root / "r4_facet_martingale_exact_slab_recovery.json").read_text())
require(high == data["high"])
require(low == data["low"])
out = [F(0) for _ in high]
incoming = [F(0) for _ in low]
bary = [[F(0)]*3 for _ in high]
energy = F(0)
for i, j, numerator, denominator in data["edges"]:
    mass = F(numerator, denominator)
    require(mass > 0)
    out[i] += mass
    incoming[j] += mass
    for coordinate in range(3):
        bary[i][coordinate] += mass*low[j][coordinate]
    # dt=dr/3 and pi is divided by 40 to match W/beta-1.
    energy += mass/F(120) * sum((low[j][r]-high[i][r])**2 for r in (0, 1))
for i in range(len(high)):
    require(out[i] == 22)
    for coordinate in range(3):
        require(bary[i][coordinate] == 22*high[i][coordinate])
for mass in incoming:
    require(mass == 9)
require(F(2, 3)/beta == 1 + F(22, 40))
require(F(1, 3)/beta + F(9, 40) == 1)
require(energy == F(71, 3))

# Exact finite absorption calibration: transient loop plus an isolated loop.
# At zero: f(0,-1)=f(0,1)=1 and f(0,0)=3. At2: f(2,2)=7.
# The isolated loop is deleted; its source and sink injections are zero.
states = (-1, 0, 1, 2)
flow = {(0, -1): F(1), (0, 1): F(1), (0, 0): F(3), (2, 2): F(7)}
a = {p: sum(flow.get((p,q), F(0)) for q in states) for p in states}
b = {p: sum(flow.get((q,p), F(0)) for q in states) for p in states}
ss = {p: max(a[p]-b[p], F(0)) for p in states}
tt = {p: max(b[p]-a[p], F(0)) for p in states}
mm = {p: a[p]+tt[p] for p in states}
for p in states:
    require(sum(flow.get((p,q), F(0))*(q-p) for q in states) == 0)
    require(mm[p] == b[p]+ss[p])
require(ss[2] == tt[2] == 0)
require(all(flow.get((p, 2), F(0)) == 0 for p in states if p != 2))
require(ss[0]/(1-F(3, 5)) == mm[0] == 5)
require(mm[0]*F(1, 5) == tt[-1] == tt[1] == 1)
require(sum(tt[p]*p*p - ss[p]*p*p for p in states)
        == sum(mass*(q-p)**2 for (p,q), mass in flow.items()) == 2)
print(f"PASS: {checks} independent exact cap-signature, flow, and absorption checks")
