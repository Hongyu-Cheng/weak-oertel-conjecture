"""Exact interval frontier and planar reserve diagnostics, not proof by sampling."""
from fractions import Fraction as F

checks = 0
for a in [F(1, 4), F(1), F(7, 3)]:
    for r in [F(1, 2), F(1), F(3)]:
        for left in [F(-1), F(0), F(2, 3)]:
            for excess in [F(0), F(1, 3), F(2)]:
                # A=[0,a], R=[2left,2left+r].
                ld = left
                hd = left + (a+r)/2
                lk, hk = ld-excess, hd+excess
                b, m = hk-lk, min(a, r)
                def fk(s):
                    return max(F(0), min(b, hk-s))
                def pair(s):
                    return max(F(0), min(m, 2*(hd-s)))
                def g(s):
                    return fk(s)+pair(s)
                breaks = sorted({lk, hk, *[s for s in [hd-m/2, hd] if lk<s<hk]})
                for j in range(1, 8):
                    budget = F(j, 8)*(b+m)
                    sb = None
                    for lo, hi in zip(breaks, breaks[1:]):
                        if g(lo)>=budget>=g(hi):
                            sb = lo+(hi-lo)*(g(lo)-budget)/(g(lo)-g(hi))
                            break
                    assert sb is not None and g(sb)==budget
                    pmin, pmax = max(F(0), budget-b), min(m, budget)
                    crossing = F(2, 3)*(hd-hk+budget)
                    candidates = {pmin, pmax, max(pmin, min(pmax, crossing))}
                    vals = []
                    for p in candidates:
                        k = budget-p
                        terms = []
                        if k<b:
                            terms.append(hk-k)
                        if p<m:
                            terms.append(hd-p/2)
                        assert terms
                        vals.append(max(terms))
                    assert min(vals)==sb
                    assert fk(sb)+pair(sb)==budget
                    checks += 3

alpha, beta, s0, s1 = F(1, 2), F(1), F(1, 4), F(0)
weight = alpha+beta
mean = (alpha*s0+beta*s1)/weight
reserve = alpha*beta*(s0-s1)**2/weight
assert (weight, mean, reserve)==(F(3, 2), F(1, 12), F(1, 48))
checks += 1
for j in range(1, 49):
    s = -F(j, 72)
    cost = alpha*(s0-s)**2+beta*(s1-s)**2
    assert cost==weight*(mean-s)**2+reserve
    assert ((mean-s)**2)==(cost-reserve)/weight
    checks += 2
assert alpha*(s0+F(1, 4))**2+beta*F(1, 4)**2 == F(3, 16)
checks += 1
print(f"PASS: {checks} exact frontier and reserve checks")
