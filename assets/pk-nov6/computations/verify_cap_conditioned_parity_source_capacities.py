"""Exact counted-source test, including closed cap boundaries and all label cuts."""
from fractions import Fraction as F
from itertools import product, combinations

P=(0,1,2)
caps=(lambda z:z<=1,lambda z:z>=1)
pairs=[]
for z,w in product(P,repeat=2):
    if (z-w)%2:
        continue
    mass=F(1,sum(v%2==z%2 for v in P))
    common=[i for i,H in enumerate(caps) if H(z) and H(w)]
    j=(z+w)//2
    assigned=min(common or [i for i,H in enumerate(caps) if H(j)])
    pairs.append((z,w,mass,(assigned,j)))
assert sum(m for _,_,m,_ in pairs)==3
for z in P:
    assert sum(m for a,_,m,_ in pairs if a==z)==1
labels=sorted({lab for *_,lab in pairs})
for lab in labels:
    sub=[p for p in pairs if p[3]==lab]
    t=sum(p[2] for p in sub)
    assert sum((z-lab[1])*m for z,_,m,_ in sub)==0
    assert caps[lab[0]](lab[1])
for k in range(1,len(labels)+1):
    for subset in combinations(labels,k):
        inds={i for i,_ in subset}
        U=lambda z:any(caps[i](z) for i in inds)
        sub=[p for p in pairs if p[3] in subset]
        t=sum(p[2] for p in sub)
        kap=sum(m for z,w,m,_ in sub if U(z) and U(w))
        nu=sum(m for z,_,m,_ in sub if U(z))
        union=sum(U(z) for z in P)
        capsum=sum(sum(caps[i](z) for z in P) for i in inds)
        overlap=capsum-union
        assert t+kap==2*nu<=2*union
        assert t+kap+2*overlap<=2*capsum
targets={j:sum(m for _,_,m,(_,jj) in pairs if jj==j) for j in P}
assert targets=={0:F(1,2),1:F(2),2:F(1,2)}
drop=sum(z*z for z in P)-sum(j*j*t for j,t in targets.items())
assert drop==sum((z-j)**2*m for z,_,m,(_,j) in pairs)==1
assert any(z%2!=j%2 for z,_,m,(_,j) in pairs if m)

# The rectangle's two bad centroid caps fail coverage; the four larger caps cover.
clamp=lambda t:max(F(0),min(F(1),t))
R=(-1,0,1,2)
bad0=[clamp(F(3,10)-F(z,5)) for z in R]
bad1=[clamp(1-(F(9,10)-F(z,5))) for z in R]
assert sum(bad0)==sum(bad1)==F(9,10)
assert not(F(1,2)<=F(3,10) or F(1,2)>=F(9,10))
good=[sum(clamp(F(1,2)-F(z,2)) for z in R),
      sum(clamp(1-(F(1,2)+F(z,2))) for z in R),
      sum(clamp(1-(1-F(z,2))) for z in R),
      sum(clamp(F(z,2)) for z in R)]
assert good==[F(3,2)]*4
assert 1-2*F(4,9)==F(1,9)>0
print('PASS: all joint label capacities, closed counting boundaries, variance drop, parity flip, and calibrations.')
