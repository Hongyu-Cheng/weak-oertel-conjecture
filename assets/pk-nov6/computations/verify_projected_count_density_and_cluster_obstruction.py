from fractions import Fraction as F
from itertools import product


gamma=F(5,6)**5
assert gamma==F(3125,7776)
assert gamma-F(648,2401)==F(2464277,18670176)>0
assert gamma/2-F(1,6)==F(533,15552)>0
checks=0
for N in [3,4,5,10,100]:
    for epsilon in [F(1,7),F(1,10),F(1,50),F(1,100)]:
        e=epsilon**5;theta=e/(10*N);c=F(5,6)
        a0=F(1,6)+5*theta;ai=F(1,6)-theta
        assert a0+5*ai==1
        assert 0<ai<1 and 0<a0<1
        assert ai>epsilon and a0<1-epsilon
        assert c-5*theta>=F(4,5) and c+theta<=F(6,7)
        b0=N*(c-5*theta)**5+e
        bi=N*(c+theta)**5
        assert b0<=N*gamma-F(3,125)*e
        assert bi<=N*gamma+F(648,2401)*e
        assert b0<N*gamma<bi<gamma*(N+e)
        assert N*gamma/(N+e)>gamma/2
        assert F(1,N+e)<F(1,2)
        for S in [F(0),epsilon/2,epsilon,(1+epsilon)/2,F(1)]:
            upper=min(F(N),F(N)-(S-epsilon)/(1-epsilon))
            count=upper.numerator//upper.denominator+1
            assert count==(N+1 if S<=epsilon else N)
            checks+=1

N=3;e=F(1,7)**5;theta=e/(10*N)
assert theta==F(1,504210)
upper=N*(F(5,6)+theta)**5/(N+e)
assert gamma-upper==F(155843157400146337951811,48882920662787036620227300000)>0

d=5;delta=F(1,10);g=(F(1,6),)*d
vertices=[(F(0),)*d]+[tuple(F(int(i==j)) for i in range(d)) for j in range(d)]

def bary(x):
    return (1-sum(x),)+x

clusters=[[tuple(v[i]+delta*(w[i]-g[i]) for i in range(d)) for w in vertices] for v in vertices]
for i,Q in enumerate(clusters):
    for x in Q:
        lam=bary(x)
        assert lam[i]>=1-delta/6>F(1,6)
        assert all(lam[j]<=5*delta/6<F(1,6) for j in range(6) if j!=i)
        checks+=1

for u in product(range(-2,3),repeat=d):
    if not any(u):
        continue
    margin=lambda x:sum(F(u[i])*(x[i]-g[i]) for i in range(d))
    values=[margin(v) for v in vertices]
    assert sum(values)==0
    m=max(values);assert m>0
    i=values.index(m)
    assert min(values)>=-5*m
    assert min(margin(x) for x in clusters[i])>0
    checks+=1

# A middle cluster coordinate separates it from every interpolation of
# points in two other clusters, independently of interpolation weights.
for i,j,k in product(range(6),repeat=3):
    if len({i,j,k})!=3:
        continue
    for t in [F(1,10),F(1,2),F(9,10)]:
        x=clusters[i][0];y=clusters[k][-1]
        z=tuple((1-t)*x[a]+t*y[a] for a in range(d))
        assert bary(z)[j]<=5*delta/6<1-delta/6
        checks+=1

# Every midpoint between different vertex neighborhoods misses ALL
# neighborhoods, the geometric input to the general parity bound.
for i,j in product(range(6),repeat=2):
    if i==j:
        continue
    for x,y in product(clusters[i],clusters[j]):
        z=tuple((x[a]+y[a])/2 for a in range(d))
        assert max(bary(z))<=F(1,2)+d*delta/(d+1)<1-delta/(d+1)
        checks+=1

print(f'PASS: {checks} exact count/cap/cluster checks, all rational budget gaps, and the six-cluster ordinary depth certificate.')
