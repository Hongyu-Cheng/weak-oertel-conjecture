"""Exact calibration and finite combinatorial checks; no OC assertion."""
from fractions import Fraction as F
from itertools import product
import sympy as s

checks=0
lengths=[F(1),F(3,2)]
M=sum(lengths)
Sigma=sum(L**3/F(12) for L in lengths)/M
assert M==F(5,2) and Sigma==F(7,48)
checks+=2
ell=[F(6),F(1)]
eps2=F(5,7)
deltas2=[eps2*Sigma*ell[j]*lengths[j]/M for j in range(2)]
assert deltas2==[F(1,4),F(1,16)]
checks+=1
for j,L in enumerate(lengths):
    delta=[F(1,2),F(1,4)][j]
    assert L/F(2)+delta==1
    for n in range(-39,40):
        y=L*F(n,80)
        energy=(L*L-4*y*y)/L
        dd=eps2*Sigma*ell[j]*energy/M
        assert dd==delta**2*(1-4*y*y/(L*L))
        # Exact upper bound sqrt(dd)<=delta; the -|y| term gives
        # strict uniqueness away from zero without evaluating a radical.
        assert 0<dd<=delta**2
        assert L/2-abs(y)+delta<=1
        if y:
            assert L/2-abs(y)+delta<1
        checks+=3+bool(y)

# Homothetic same-cap status identity, including non-unit Gamma.
l,f0,e,g,u,Y=s.symbols('l f0 e g u Y',positive=True)
assert s.expand((u*l*Y+e*l*f0*g)/l-(u*Y+e*f0*g))==0
checks+=1

# Exhaust actual weighted BASE halfspaces in 1D. Only the midpoint
# heredity hypotheses proved analytically above are imposed on I,J;
# these scalar cases are not claimed to be realized buffered bodies.
instances=0
for count in range(2,6):
    P=list(range(count))
    for weights in product(range(1,4),repeat=count):
        total=sum(weights)
        depth=[min(sum(weights[:p+1]),sum(weights[p:])) for p in P]
        for lo in P:
            for hi in range(lo,count):
                I=set(range(lo,hi+1))
                for Q in range(1,min(depth[p] for p in I)+1):
                    J={p for p in I if depth[p]>Q}
                    A=I-J
                    if not A:
                        continue
                    hereditary=all((p+q)//2 not in J or (p in J and q in J)
                                   for p in I for q in I if (p+q)%2==0)
                    if not hereditary:
                        continue
                    rows=[]
                    for p in sorted(A):
                        # An attained mass-Q cap containing p.
                        if sum(weights[:p+1])==Q:
                            rows.append((-1,-p,1))
                        else:
                            assert sum(weights[p:])==Q
                            rows.append((1,p,count))
                    candidates=[range(b,U+1) for a,b,U in rows]
                    best=None
                    for thresholds in product(*candidates):
                        if all(any(a*p>=c for (a,_,_),c in zip(rows,thresholds)) for p in A):
                            score=sum(thresholds)
                            if best is None or score>best[0]:
                                best=(score,thresholds)
                    assert best is not None
                    active=[(a,c) for (a,b,U),c in zip(rows,best[1]) if c<U]
                    witnesses=[]
                    for i,(a,c) in enumerate(active):
                        ws=[p for p in A if a*p==c and all(aa*p<cc for j,(aa,cc) in enumerate(active) if i!=j)]
                        assert ws
                        witnesses.append(ws[0])
                        assert sum(weights[p] for p in P if a*p>=c)==Q
                        assert all(a*j<c for j in J)
                        checks+=3
                    assert len({p%2 for p in witnesses})==len(witnesses)
                    assert not ({p%2 for p in witnesses}&{p%2 for p in J})
                    assert len(active)+len({p%2 for p in J})<=len({p%2 for p in I})
                    checks+=3
                    instances+=1

print(f'{checks} exact checks PASS; {instances} finite compression instances')
