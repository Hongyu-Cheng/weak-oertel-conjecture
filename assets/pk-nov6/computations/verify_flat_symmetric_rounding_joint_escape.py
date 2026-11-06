"""Exact simplex algebra plus a high-precision active-compatibility test.

The all-dimensional C² proof is in the companion note. The rounded
planar cap formula below independently implements its face tubes.
No finite numerical screen is used as the all-parameter theorem.
"""
from fractions import Fraction as F
import mpmath as mp

d=2;m=3;Gamma=F(4,9);V=F(1,2)
Bq=[[F(0),F(1,2),-F(1,2)],
    [F(1,6),-F(1,3),F(1,6)],
    [-F(1,6),-F(1,6),F(1,3)]]
omegaq=[F(-1),F(1),F(0)]
assert all(sum(Bq[i][j] for i in range(m))==0 for j in range(m))
tr=sum(Bq[i][i] for i in range(m))
assert tr==0
assert all(tr+sum(row)==0 for row in Bq)
diag=[Bq[i][i] for i in range(m)]
Ri=[sum((diag[i]-Bq[i][j])**2 for j in range(m) if j!=i) for i in range(m)]
Qww=F(m,d)*sum(b*b for b in diag)-F(1,m)*sum(Ri)
Qwa=-F(m,d)*sum(diag[i]*omegaq[i] for i in range(m))
Q=Qww+2*Qwa
assert Qww==-F(1,6) and Qwa==F(1,2) and Q==F(5,6)

def rightinverse_q(f):
    z=[q/(m*Gamma*V) for q in f];Z=sum(z)
    return [[z[i] if i==j else z[i]-Z/d for j in range(m)] for i in range(m)]
Rq=[]
for j in range(m):
    f=[F(int(i==j)) for i in range(m)]
    R=rightinverse_q(f);Rq.append(R)
    assert all(sum(R[i][k] for i in range(m))==0 for k in range(m))
    T=sum(R[i][i] for i in range(m))
    assert [V*Gamma*(T+sum(row)) for row in R]==f

mp.mp.dps=70
def mm(q):return mp.mpf(q.numerator)/q.denominator if isinstance(q,F) else mp.mpf(q)
I=mp.eye(3);B=mp.matrix([[mm(q) for q in row] for row in Bq])
omega=mp.matrix([mm(q) for q in omegaq])
RB=[mp.matrix([[mm(q) for q in row] for row in R]) for R in Rq]
astar=mp.matrix([mp.mpf(1)/3]*3)
U=[mp.matrix([-1,-1]),mp.matrix([1,0]),mp.matrix([0,1])]
vertices0=[mp.matrix([-mp.mpf(1)/3,-mp.mpf(1)/3]),
           mp.matrix([mp.mpf(2)/3,-mp.mpf(1)/3]),
           mp.matrix([-mp.mpf(1)/3,mp.mpf(2)/3])]
def dot(a,b):return sum(a[i]*b[i] for i in range(len(a)))
def norm(a):return mp.sqrt(dot(a,a))
def Rof(r):
    out=mp.zeros(3)
    for j in range(3):out+=r[j]*RB[j]
    return out
def verts(W):
    return [sum((W[i,j]*vertices0[i] for i in range(3)),mp.zeros(2,1))
            for j in range(3)]
def area(vs):
    return sum(vs[i][0]*vs[(i+1)%3][1]-vs[(i+1)%3][0]*vs[i][1]
               for i in range(3))/2
def perimeter(vs):return sum(norm(vs[(i+1)%3]-vs[i]) for i in range(3))
def volume(W,tau):
    vs=verts(W)
    return area(vs)+tau*perimeter(vs)+mp.pi*tau*tau
def cap(W,a,tau,i):
    vs=verts(W);u=U[i];threshold=a[i]-mp.mpf(1)/3
    hi=dot(u,vs[i])-threshold
    others=[j for j in range(3) if j!=i]
    denominators=[dot(u,vs[i]-vs[j]) for j in others]
    out=area(vs)*hi*hi/(denominators[0]*denominators[1])
    edge1=edge2=mp.mpf(0)
    for j,Dij in zip(others,denominators):
        edge=vs[j]-vs[i]
        L=norm(edge)
        if j==(i+1)%3:oriented=edge
        else:oriented=-edge
        normal=mp.matrix([oriented[1],-oriented[0]])/L
        edge1+=L*hi/Dij
        edge2+=L*dot(u,normal)/Dij
    e0,e1=(vs[j]-vs[i] for j in others)
    exterior=mp.pi-mp.acos(dot(e0,e1)/(norm(e0)*norm(e1)))
    return out+tau*edge1+tau*tau*(exterior+edge2)/2
def constraint(t,r,eps):
    W=I+t*B+Rof(r);a=astar+t*omega
    return mp.matrix([cap(W,a,eps,i)-cap(I,a,eps,i) for i in range(3)])

zeros=mp.zeros(3,1)
curvatures=[]
for eps in [mp.mpf(0),mp.mpf('0.000001'),mp.mpf('0.0001'),
            mp.mpf('0.001'),mp.mpf('0.01')]:
    J=mp.matrix(3)
    for i in range(3):
        for j in range(3):
            J[i,j]=mp.diff(lambda q:cap(I+q*RB[j],astar,eps,i),0)
    first=mp.matrix([mp.diff(lambda t:constraint(t,zeros,eps)[i],0)
                     for i in range(3)])
    rp=-mp.lu_solve(J,first)
    direction=B+Rof(rp)
    second=mp.matrix([mp.diff(
        lambda t:cap(I+t*direction,astar+t*omega,eps,i)
                 -cap(I,astar+t*omega,eps,i),0,2) for i in range(3)])
    rpp=-mp.lu_solve(J,second)
    reduced=mp.diff(lambda t:volume(I+t*direction,eps),0,2)
    reduced+=sum(rpp[j]*mp.diff(lambda q:volume(I+q*RB[j],eps),0)
                 for j in range(3))
    assert reduced>0
    if eps==0:
        assert max(abs(x) for x in rp)<mp.mpf('1e-55')
        assert abs(reduced-mp.mpf(5)/12)<mp.mpf('1e-55')
        assert max(abs(J[i,j]-int(i==j)) for i in range(3) for j in range(3))<mp.mpf('1e-55')
    curvatures.append((eps,reduced))

# Actual source with initially ACTIVE midpoint equality:
# fibers -K, (K-K)/2, K at -1,0,1; phi=(1,2,1).
eps=mp.mpf('0.001');t=eps/100
solutions=[]
for tt in [t,-t]:
    def equations(r0,r1,r2):
        return tuple(constraint(tt,mp.matrix([r0,r1,r2]),eps))
    r=mp.matrix(mp.findroot(equations,(0,0,0),tol=mp.mpf('1e-60'),verify=True))
    W=I+tt*B+Rof(r)
    gain=volume(W,eps)-volume(I,eps)
    solutions.append((gain,tt,r,W))
gain,tt,r,W=max(solutions,key=lambda row:row[0])
assert gain>0
eta=min(gain*mm(Gamma)/10,t*t/1000)
def strict_equations(r0,r1,r2):
    return tuple(q+eta for q in constraint(tt,mp.matrix([r0,r1,r2]),eps))
rnew=mp.matrix(mp.findroot(strict_equations,tuple(r),tol=mp.mpf('1e-60'),verify=True))
Wnew=I+tt*B+Rof(rnew)
newgain=volume(Wnew,eps)-volume(I,eps)
assert newgain>0
assert max(abs(q+eta) for q in constraint(tt,rnew,eps))<mp.mpf('1e-55')
displacement=max(norm(a-b) for a,b in zip(verts(Wnew),vertices0))
assert displacement<eps
# This guarantees (moving endpoint + reflected endpoint)/2
# lies inside (K-K)/2+2eps B: half displacement+eps <2eps.
assert displacement/2+eps<2*eps
for i in range(3):
    heights=[dot(U[i],z)-(astar[i]+tt*omega[i]-mp.mpf(1)/3)
             for z in verts(Wnew)]
    assert heights[i]>mp.mpf('0.5')
    assert all(heights[j]<-mp.mpf('0.2') for j in range(3) if j!=i)

M=mp.mpf(7)/4
perim=2+mp.sqrt(2)
Meps=M+4*perim*eps+6*mp.pi*eps*eps
alpha2=M/Meps
assert alpha2*(Meps+newgain)>M
assert alpha2*(Meps/2-eta)<M/2

print("PASS exact d=2 critical algebra, right inverse, and face-tube reduced curvature at zero.")
print("High-precision rounded curvatures:",[(mp.nstr(e,5),mp.nstr(q,16)) for e,q in curvatures])
print("Active-midpoint actual test: normalized mass gain",mp.nstr(alpha2*newgain,16),
      "; each cap reduction",mp.nstr(alpha2*eta,16),
      "; vertex displacement",mp.nstr(displacement,10),"< epsilon",eps)
