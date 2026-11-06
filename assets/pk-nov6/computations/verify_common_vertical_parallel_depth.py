"""Exact checks of the all-slope formula and rational quasiconcavity dip.

The accompanying note proves the clamp identity and all-parameter theorem.
This verifies formulas over exact rational breakpoints, not sampled normals.
"""
from fractions import Fraction as F

def clamp(t, a):
    return max(F(0), min(a, t))

def endpoint_min(x, a):
    breaks = {x, -x, a-x, x-a, F(0)}
    far = 1+max(abs(v) for v in breaks)
    breaks.update((-far,far))
    # Between breakpoints this objective is affine, and it is constant
    # beyond the two tails. Thus this finite minimization is exact.
    return min(clamp(x+v,a)+clamp(x-v,a) for v in breaks)

cases = 0
for den in range(1,13):
    a = F(1)
    for num in range(den, 8*den+1):
        b = F(num,den)
        x = (b+a)/4 if b<=3*a else (b-a)/2
        lower = x+endpoint_min(x,a)
        upper = b-x+endpoint_min(a-x,a)
        expected = (b+5*a)/4 if b<=3*a else (b+a)/2
        assert lower == upper == expected
        assert expected>a/2
        for j in range(21):
            xx = b*F(j,20)
            assert endpoint_min(xx,a)==min(2*xx,a)
            assert endpoint_min(a-xx,a)==min(max(2*(a-xx),F(0)),a)
            own = min(xx+endpoint_min(xx,a),b-xx+endpoint_min(a-xx,a))
            assert own<=expected
        cases += 1

def exact_flow(t):
    return ((3+2*t)/(7+6*t) if t<=F(1,2)
            else (5+6*t)/(2*(7+6*t)))

assert exact_flow(F(0))==F(3,7)
assert exact_flow(F(1,2))==F(2,5)
assert exact_flow(F(3))==F(23,50)
assert exact_flow(F(1,2))<min(exact_flow(F(0)),exact_flow(F(3)))
assert exact_flow(F(-1,2))==F(1,2)
print(f"PASS: {cases} rational all-slope cases; exact 3/7,2/5,23/50 dip.")
