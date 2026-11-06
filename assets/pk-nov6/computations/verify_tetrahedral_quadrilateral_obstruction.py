from fractions import Fraction as F
from functools import reduce

def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
p,q,r,s=map(F,[6,7,24,6]);t=[p,q,-r,-s]
a=p*s/((p+r)*(p+s)*(q+s));d=q*r/((p+r)*(q+s)*(q+r));tau=a/(a+d)
A=[r/(p+r),0,p/(p+r),0];B=[s/(p+s),0,0,p/(p+s)];C=[0,s/(q+s),0,q/(q+s)];D=[0,r/(q+r),q/(q+r),0]
l=[(A[i]+C[i]+tau*B[i]+(1-tau)*D[i])/3 for i in range(4)]
normal=[q-p,-r-p,-s-p]
assert cross(sub(B[1:],A[1:]),sub(C[1:],A[1:]))==[-a*x for x in normal]
assert cross(sub(C[1:],A[1:]),sub(D[1:],A[1:]))==[-d*x for x in normal]
S=3*(a+d);vol=p*(a+d)+q*q/((q+s)*(q+r))
assert l==[F(851,2610),F(11218,35061),F(4657,40455),F(1621,6786)]
assert all(0<x<F(1,3) for x in l)
assert S==F(261,4030) and vol==F(506,2015) and dot(l,t)==0
N=52425025485892802
weights=[F(v,N) for v in [23097356755453943,13014678602879811,15094034160118200,1218955967440848]]
assert sum(weights)==1 and min(weights)>0
caps=[(1-vol,[-S*x for x in normal])]
prod=reduce(lambda x,y:x*y,l,F(1))
for i in range(3):
 fi=27*prod/l[i]
 ti=[F(3) if j==i else 3-1/l[j] for j in range(4)]
 ni=[ti[j]-ti[0] for j in range(1,4)]
 caps.append((fi,[fi*x for x in ni]))
assert all(sum(w*c[1][j] for w,c in zip(weights,caps))==0 for j in range(3))
mean=sum(w*c[0] for w,c in zip(weights,caps));den=1-3*sum(x*x for x in l);baseline=27*prod/den
assert mean==F(12431494665571935,26212512742946401)
assert baseline==F(36033317871223,75836660403033)
assert F(27,64)<mean<baseline
slack=den*(1-vol)-S*sum(l[i]**2*t[i] for i in range(4))-27*prod
assert slack==F(-76232299376,232609319856225)
assert mean-F(27,64)==F(87877814537051013,1677600815548569664)
print('All geometric, centroid, coarea, circuit-balance and strict-ratio certificates pass exactly.')
