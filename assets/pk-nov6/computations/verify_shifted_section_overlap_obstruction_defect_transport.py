"""Exact actual-body certificate; no global depth optimality is asserted."""
from fractions import Fraction as F
from itertools import product

checks=0
def check(v):
    global checks
    assert v
    checks+=1
def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def area(P):
    return sum(P[i][0]*P[(i+1)%len(P)][1]-P[i][1]*P[(i+1)%len(P)][0] for i in range(len(P)))/2
def clip(P,u,b):
    ans=[]
    for x,y in zip(P,P[1:]+P[:1]):
        vx=u[0]*x[0]+u[1]*x[1]-b
        vy=u[0]*y[0]+u[1]*y[1]-b
        if vx>=0: ans.append(x)
        if (vx<0<vy) or (vy<0<vx):
            t=vx/(vx-vy)
            ans.append(tuple(x[j]+t*(y[j]-x[j]) for j in range(2)))
    return ans
def contains(P,p):
    return all(cross(P[i],P[(i+1)%len(P)],p)>=0 for i in range(len(P)))

A=[(F(-10),F(-10)),(F(61,100),F(59,100)),(F(59,100),F(61,100))]
B=[(F(1),F(1)),(F(-2),F(1)),(F(1),F(-2))]
lower=-F(1079,1061); upper=-F(1041,1059)
s=upper-lower; a=(upper+lower)/2; b=1-2*s
R=F(32); c=-s*(a+b)/R
p=R/2+c; m=-R/2+c
K0=[(p,F(0)),(F(0),p),(-R/2,R/2),(m,F(0)),(F(0),m),(R/2,-R/2)]
normals=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]
acaps=[area(clip(A,u,F(-1))) for u in normals]
k0caps=[area(clip(K0,u,F(0))) for u in normals]
extra=acaps[2]+k0caps[2]-acaps[0]-k0caps[0]
check(extra>0)
h=extra/p
newvertex=(p/2+h,p/2+h)
K=[K0[0],newvertex]+K0[1:]
for P in [A,B,K0,K]:
    check(area(P)>0)
    for i in range(len(P)):
        check(cross(P[i],P[(i+1)%len(P)],P[(i+2)%len(P)])>0)
check(area(K)-area(K0)==extra)
for aa,bb in product(A,B):
    check(contains(K,tuple((aa[j]+bb[j])/2 for j in range(2))))
check(contains(K,(F(0),F(0))))
kcaps=[area(clip(K,u,F(0))) for u in normals]
Q=[acaps[i]+kcaps[i] for i in range(3)]
check(Q[0]==Q[1]==Q[2])
missed=[area(A)-a for a in acaps]
kappa=sum(missed)/area(A)
check(kappa>F(5,4))
check(missed[0]/area(A)==F(270000,374533))
check(missed[2]/area(A)==1-F(105,106)**2)

# The prescribed section moments and strict facet allocations.
check(s*a+R*c+s*b==0)
allocation_interval=(1-3*s,1-s)
check(F(-2)<allocation_interval[0]<allocation_interval[1]<1)
check(F(1,2)*(allocation_interval[1]-allocation_interval[0])==s)
check(sum(allocation_interval)/2==b)
delta=-R*c/s
check(delta==a+b)
J=(-upper+delta,-lower+delta)
check(sum(J)/2==b)
check(F(-2)<J[0]<J[1]<1)
check(c/R < F(1,8))  # stronger than the universal ~0.134 bound
check(F(7,1060)<1)
check(area(K)>area(A)+area(B))
check(F(0)<c<F(1,10000))
check(F(1,10)<extra<F(1,5))
check(F(0)<h<F(1,80))
check(abs(delta)<F(8,100))
check(all(F(0)<v<area(A)<area(B) for v in acaps))
# Fixed-continuous-normal global tilt bound: A projection density <1/20,
# while emerging B cap mass is >=(3/2)(beta+1) for -1<=beta<=2.
for normal in normals:
    projections=[normal[0]*x+normal[1]*y for x,y in A]
    check(2*area(A)/(max(projections)-min(projections))<F(1,20))

print('PASS',checks,'exact checks')
for name,value in [('A_area',area(A)),('B_area',area(B)),('K_area',area(K)),('extra',extra),('bulge_h',h),('Q',Q[0]),('kappa',kappa),('kappa_minus_5over4',kappa-F(5,4))]:
    print(name, value)
