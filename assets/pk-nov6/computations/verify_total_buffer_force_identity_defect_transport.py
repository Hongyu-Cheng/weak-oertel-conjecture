"""Exact entropy algebra and the genuine one-interval sharp calibration."""
from fractions import Fraction as F
import sympy as s

checks = 0
def check(ok):
    global checks
    assert ok
    checks += 1

rho = (s.Rational(1, 2), s.Rational(1, 2))
coarea = (1/s.sqrt(3), 1/s.sqrt(3))
B = sum(r/T for r,T in zip(rho, coarea))
check(s.simplify(B-s.sqrt(3)) == 0)
K = 1/B
check(s.simplify(K-1/s.sqrt(3)) == 0)
for n in range(1, 50):
    epsilon = s.Rational(n, 50)
    Delta = epsilon*K
    check(s.simplify(Delta-epsilon/s.sqrt(3)) == 0)
    check(epsilon/s.sqrt(3) < 1)
    check(s.simplify(s.log(epsilon*K/Delta)) == 0)

# Finite rational algebra only: these arrays are not asserted geometric rows.
for k1 in (s.Rational(1, 3), s.Rational(1), s.Rational(3)):
    for k2 in (s.Rational(1, 2), s.Rational(2)):
        for d1 in (s.Rational(1, 5), s.Rational(2, 5)):
            for d2 in (s.Rational(1, 4), s.Rational(1, 2)):
                eps = s.Integer(1)
                N = s.Integer(2)
                E = (s.Rational(1, 2), s.Rational(3, 4))  # E_a/M
                kap = (k1, k2)
                delta = (d1, d2)
                totalK = sum(kap)
                totalDelta = sum(k*d for k,d in zip(kap,delta))
                w = tuple(k/totalK for k in kap)
                sig = tuple(k*d/totalDelta for k,d in zip(kap,delta))
                L = tuple((d/eps)**N/e for d,e in zip(delta,E))
                check(all(0 < ell <= 1 for ell in L))
                KV = -sum(q*s.log(ell) for q,ell in zip(sig,L))
                KL = sum(q*s.log(q/p) for q,p in zip(sig,w))
                cost = sum(q*s.log(1/e) for q,e in zip(sig,E))
                defect = s.log(eps*totalK/totalDelta)-KL-(KV+cost)/N
                check(s.simplify(s.expand_log(defect, force=True)) == 0)
                check(sum(sig) == 1 and sum(w) == 1)
                check(totalDelta <= eps*totalK)

print(f"PASS: {checks} exact total-buffer-force identity checks")
