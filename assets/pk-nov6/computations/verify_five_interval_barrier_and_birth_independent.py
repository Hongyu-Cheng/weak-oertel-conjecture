from fractions import Fraction as F
from itertools import product

checks=0
base_lo=[-F(v,2) for v in [13,11,9,7,5]]
base_hi=[F(v,2) for v in [13,11,9,7,5]]

def cap(z,lo,hi,p,y,a,up=True):
    value=sum(min(H-L,max(F(0),H-y-a*(i-p)))
              for i,L,H in zip(z,lo,hi))
    return value if up else sum(H-L for L,H in zip(lo,hi))-value

def extrema(lo,hi,p,y):
    z=list(range(5))
    knots=sorted(set((e-y)/F(i-p) for i in z if i!=p for e in [lo[i],hi[i]]))
    values=[cap(z,lo,hi,p,y,a) for a in knots]
    return min(values),max(values)

# The exact knot-order / status chamber is checked at every vertex of the
# claimed ten-dimensional endpoint box. Each underlying comparison is affine.
for signs in product([-1,1],repeat=10):
    lo=[v+F(s,100) for v,s in zip(base_lo,signs[:5])]
    hi=[v+F(s,100) for v,s in zip(base_hi,signs[5:])]
    w=[H-L for L,H in zip(lo,hi)];c=[(L+H)/2 for L,H in zip(lo,hi)]
    M=sum(w);y1=sum(c[:3])/3;y2=c[2]
    q1=sum(w[:3])/2;q2=w[2]/2+w[3]+w[4]
    for p,y,q in [(1,y1,q1),(2,y2,q2)]:
        mn,mx=extrema(lo,hi,p,y)
        assert mn==q and mx==M-q
        checks+=2
    assert cap(range(5),lo,hi,1,y1,F(2))==q1
    assert cap(range(5),lo,hi,1,y1,-F(2),False)==q1
    assert cap(range(5),lo,hi,2,y2,-F(10))==q2
    assert cap(range(5),lo,hi,2,y2,F(10),False)==q2
    checks+=4

for j in range(300):
    u=F(j,100);z=list(range(-1,6))
    lo=[F(15,2)-u]+base_lo+[-u/4]
    hi=[F(15,2)]+base_hi+[u/4]
    assert all(lo[i]-2*lo[i+1]+lo[i+2]>=0 for i in range(5))
    assert all(hi[i]-2*hi[i+1]+hi[i+2]<=0 for i in range(5))
    M=sum(H-L for L,H in zip(lo,hi));Q=F(33,2)+u/2
    assert M==45+3*u/2
    assert cap(z,lo,hi,1,u/6,F(2))==Q
    assert cap(z,lo,hi,1,u/6,-F(2),False)==Q
    assert cap(z,lo,hi,2,F(0),-F(10))==Q
    assert cap(z,lo,hi,2,F(0),F(10),False)==Q
    assert (Q/M<F(11,30))==(u>0)
    checks+=8

assert F(11,30)-F(34,93)==F(1,930)
checks+=1
print(f'PASS: {checks} exact neighborhood-corner, cap-budget, roof, and birth checks')
