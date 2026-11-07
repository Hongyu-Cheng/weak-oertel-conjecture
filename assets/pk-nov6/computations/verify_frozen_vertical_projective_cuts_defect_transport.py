"""Exact checks for frozen-base facet speeds and the interval prism.

The general convex-extension and normal-stress arguments are analytic in
the companion Markdown source. These checks verify its concrete actual
polytope, crease, affine normalization, and all-slope interval formulas.
"""
from fractions import Fraction as F
import sympy as sp

checks = 0


def check(x):
    global checks
    assert x
    checks += 1


def clamp(x, lo, hi):
    return min(max(x, lo), hi)


# The tent has an integer-base crease and unequal ambient intercepts.
P = [-1, 0, 1, 2]
rad = {z: min(2 + z, 4 - z) for z in P}
check([rad[z] for z in P] == [1, 2, 3, 2])
for sign in [-1, 1]:
    for den in range(20, 51):
        t = F(sign, den)
        rt = {z: min(2 + z - 2*t*z, 4 - z - 4*t*z) for z in P}
        check(all(v > 0 for v in rt.values()))
        check(all(rt[z] * 2 >= rt[z-1] + rt[z+1] for z in [0, 1]))
        check((rad[1] - rt[1])/abs(t) == (4 if sign > 0 else -2))
        # Every new endpoint satisfies all four actual nonvertical cuts.
        for z in P:
            for x in [-rt[z], rt[z]]:
                check(-z + x + 2*t*z <= 2)
                check(-z - x + 2*t*z <= 2)
                check(z + x + 4*t*z <= 4)
                check(z - x + 4*t*z <= 4)

# Exact same-normal interpolation at the crease example's collinear triple.
vp = {-1: -2, 0: 0, 1: 4, 2: 8}
vm = {-1: 2, 0: 0, 1: -2, 2: -8}
check(vp[0] < F(vp[-1] + vp[1], 2))
check(vm[0] == F(vm[-1] + vm[1], 2))
check(vp[1] + vm[1] == 2)

# Symbolic prism endpoints and the exact fiber-affine map.
t, a, h, z = sp.symbols('t a h z')
xp = (1-t*a*z)/(1+t*h)
xm = -(1-t*a*z)/(1-t*h)
center = -t*h*(1-t*a*z)/(1-t*t*h*h)
radius = (1-t*a*z)/(1-t*t*h*h)
check(sp.factor((xp+xm)/2-center) == 0)
check(sp.factor((xp-xm)/2-radius) == 0)
for x, target in [(xp, 1-t*a*z), (xm, -(1-t*a*z))]:
    check(sp.factor((1-t*t*h*h)*x+t*h*(1-t*a*z)-target) == 0)
check(sp.factor(sum(2*radius.subs(z, zz) for zz in [-1,0,1])
                - 6/(1-t*t*h*h)) == 0)
check(sp.factor(sp.diff(6/(1-t*t*h*h), t, 2).subs(t,0)-12*h*h) == 0)

# For each rational radius asymmetry the pair cap function is piecewise
# affine. Its global minimum is attained at one of the four saturation
# thresholds or on an exterior ray, hence the complete exact breakpoint
# check proves the formula for this instance for every real slope.
for den in range(3, 41):
    for num in range(-den+1, den):
        s = F(num, den)
        rminus, rplus = 1+s, 1-s
        breaks = sorted(set([-rminus, rminus, -rplus, rplus]))
        slopes = breaks + [breaks[0]-1, breaks[-1]+1]

        def pair_cap(k):
            return clamp(rminus-k, 0, 2*rminus) + clamp(rplus+k, 0, 2*rplus)

        expected = 2*min(rminus, rplus)
        check(min(pair_cap(k) for k in slopes) == expected)
        check(all(pair_cap(k) >= expected for k in slopes))
        # Every affine segment is checked at both endpoints; interiors are
        # checked as redundant independent arithmetic calibrations.
        for left, right in zip(breaks, breaks[1:]):
            check(pair_cap((left+right)/2) >= expected)
        if abs(s) < F(2,3):
            q = 1+expected
            check(q > max(rminus, rplus))
            check(q/F(6) == F(1,2)-abs(s)/3)
            check(2+2*min(rminus,rplus) > q)

# Rational full frozen paths retain the exact original-coordinate costs.
for aa in [F(-2), F(-1,2), F(0), F(2,3), F(3)]:
    for hh in [F(-2), F(0), F(1), F(3,2)]:
        for tt in [F(-1,20), F(-1,50), F(1,50), F(1,20)]:
            det = 1-tt*tt*hh*hh
            rr = [(1-tt*aa*zz)/det for zz in [-1,0,1]]
            m = sum(2*x for x in rr)
            q = (3-2*abs(aa*tt))/det
            check(det > 0 and min(rr) > 0)
            check(m == 6/det)
            check(q/m == F(1,2)-abs(aa*tt)/3)

print(f'PASS: {checks} exact frozen-vertical facet and prism checks')
