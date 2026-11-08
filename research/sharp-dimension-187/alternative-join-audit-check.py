"""Independent exact audit of the simplified n=132,d=99 simplex-join example."""
from fractions import Fraction as F
from itertools import combinations
from math import comb

D, d, n, N, cutoff = 100, 99, 132, 44, 30
a, delta, epsilon = F(63,100), F(329,10000), F(1,10**13)
b, Q = 1-a, 1-a+a*a
eta = (1-delta)/2
v = delta/D+(1-delta)*a*epsilon/Q

def determinant(columns):
    x,y,z = columns
    return (x[0]*(y[1]*z[2]-y[2]*z[1])
            -y[0]*(x[1]*z[2]-x[2]*z[1])
            +z[0]*(x[1]*y[2]-x[2]*y[1]))

def scores(x):
    return tuple(x[j]-a*x[(j+1)%3]-b*x[(j+2)%3] for j in range(3))

e0 = (F(1),F(0),F(0))
c = (F(1,3),)*3
left = (1/(1+b),b/(1+b),F(0))
right = (1/(1+a),F(0),a/(1+a))
# Enumerate every vertex of lambda>=0, sum(lambda)=1, f1<=0, f2<=0.
planes = [(F(1),F(0),F(0)), (F(0),F(1),F(0)), (F(-1),F(-1),F(-1)),
          (a-b,1+a,a), (-(1+a),-(1+b),F(-1))]
vertices = set()
for (p,q,r),(u,w,t) in combinations(planes,2):
    det = p*w-q*u
    if det:
        x,y = (r*w-q*t)/det,(p*t-r*u)/det
        z = 1-x-y
        point=(x,y,z)
        if min(point)>=0 and max(scores(point)[1:])<=0:
            vertices.add(point)
assert vertices == {e0,left,c,right}

positive = determinant((e0,c,right))
negative = determinant((e0,left,c))+positive
cap = determinant((e0,(a/(1+a),1/(1+a),F(0)),(b/(1+b),F(0),1/(1+b))))
assert positive == a/(3*(1+a))
assert negative == (a/(1+a)+b/(1+b))/3
assert cap == 1/((1+a)*(1+b))
weights = [epsilon/a,F(3,D)-3*a*epsilon/Q,epsilon*(2*a-1)*(1+a)/(a*Q)]
assert min(weights)>0 and sum(weights)+F(D-3,D)==1
center = tuple(F(1,D)+epsilon*w/Q for w in (F(1),-a,-b))
assert tuple(sum(weight*vertex[j] for weight,vertex in zip(weights,(e0,c,right))) for j in range(3)) == center
assert scores(center)==(2*epsilon,-epsilon,-epsilon)
assert 1-cutoff*D*v>0 and F(1,D)-a*epsilon/Q>0
assert 0<eta<1-delta and 2*epsilon<1
for k in range(1,n+1):
    residual = -delta/D-(k-delta)*a*epsilon/Q+k*v
    assert residual == (k-1)*delta*(F(1,D)-a*epsilon/Q) >= 0
    assert k*eta-k+delta<0
    assert 1+delta+2*epsilon*(k-delta)<k+1

gamma = F(d,D)**d
m = positive*(1+delta)**d
alphas = [negative*(1-r*D*v)**d for r in range(1,cutoff+1)]
E = 3*sum(comb(N,r)*alphas[r-1] for r in range(1,cutoff+1))
margins = [1+E-m,gamma*m-cap-E/3,gamma*m-alphas[0]]
assert min(margins)>0 and all(0<x<=alphas[0] for x in alphas)
print('Independent rational vertex, determinant, center, facet, cut, and mass checks passed.')
print('Orientation-only decimal margins:',*[float(x) for x in margins])
