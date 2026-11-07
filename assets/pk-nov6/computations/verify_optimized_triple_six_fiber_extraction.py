"""Exact algebraic certificates for optimized triple/six-fiber extraction.
No numerical optimization is used here.
"""
from fractions import Fraction as F
import sympy as s

a,b,c,d,e,T,L,h,A,small=s.symbols('a b c d e T L h A small')
# Four-fiber budget decompositions: all terms on the right are <=0.
assert s.expand((L+h+c+d)-2*(h+2*c)-
                ((L-h-c-d)+2*(d-c)))==0
assert s.expand((b+c+A+small)-2*(c+2*A)-
                ((b-c-A-small)+2*(small-A)))==0
# Five-fiber concavity bounds and their final ratios.
M=a+b+c+d+e
assert s.expand(M-(2*c+3*T)-
 ((a-T)+2*(d-T)+(b-2*c+d)+(e-2*d+c)))==0
assert s.expand(2*c+3*T-s.Rational(7,4)*(c+2*T)-(c-2*T)/4)==0
assert s.expand(M-(b+4*T)-((a-T)+3*(d-T)+(c+e-2*d)))==0
assert s.expand(b+4*T-s.Rational(5,3)*(b+2*T)+s.Rational(2,3)*(b-T))==0
# Five/six-point exact concavity quadratures.
w=s.symbols('w0:6')
q=[w[i]-2*w[i+1]+w[i+2]for i in range(4)]
assert s.expand(sum(w[:5])-5*w[2]-(q[0]+3*q[1]+q[2]))==0
assert s.expand(sum(w)-3*(w[2]+w[3])-(q[0]+3*q[1]+3*q[2]+q[3]))==0
assert s.expand(sum(w)-(w[0]+5*w[3])-(q[1]+3*q[2]+q[3]))==0
assert s.expand(sum(w)-3*(w[1]+w[4])-(q[0]+q[3]))==0
# Plateau intersection endpoint bounds, with ell=(a+c)/2 and l=min, A=max.
ell=(A+small)/2
assert s.expand(b-ell+small/2-(b-A/2))==0

def overlap(x,y,center):
    return max(F(0),min(x,y,2*center,x+y-2*center))
def maximum_at_base(widths,j):
    candidates={F(0), widths[j], widths[j]/2}
    N=len(widths)
    for i in range(N):
        k=2*j-i
        if not 0<=k<N: continue
        x,y=widths[i],widths[k]
        candidates.update([min(x,y)/2,max(x,y)/2,(x+y)/2])
    candidates={t for t in candidates if 0<=t<=widths[j]}
    return max(sum(overlap(widths[i],widths[2*j-i],t)
                   for i in range(N) if 0<=2*j-i<N)
               for t in candidates)
widths=[F(1),F(5),F(3),F(1)]
assert [maximum_at_base(widths,j)for j in range(4)]==[1,5,5,1]
assert max(maximum_at_base(widths,j)for j in range(4))==sum(widths)/2
widths=[F(2),F(6),F(10),F(3)]
assert [maximum_at_base(widths,j)for j in range(4)]==[2,10,12,3]
for eps in [F(1,10),F(1,100),F(1,1000)]:
    widths=[1+eps,3+eps,2+eps,1+eps,eps]
    assert all(widths[i]-2*widths[i+1]+widths[i+2]<=0 for i in range(3))
    R=max(maximum_at_base(widths,j)for j in range(5))
    assert F(4,7)*sum(widths)<=R<=4+5*eps
print('PASS: plateau algebra, all four/five/six-fiber concavity identities, and exact sharp calibrations')
