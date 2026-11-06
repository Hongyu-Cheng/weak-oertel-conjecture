"""Exact physical cap Hessians, variance correction, and equal-budget stability."""
from fractions import Fraction as F
from random import Random
import sympy as S


class Jet:
    def __init__(self, x, dx=0, q=0):
        self.c = (F(x),F(dx),F(q))
    @staticmethod
    def cast(b):
        return b if isinstance(b,Jet) else Jet(b)
    def __add__(self,b):
        b=self.cast(b)
        return Jet(*(self.c[i]+b.c[i] for i in range(3)))
    __radd__=__add__
    def __neg__(self):
        return Jet(*(-x for x in self.c))
    def __sub__(self,b):
        return self+-self.cast(b)
    def __rsub__(self,b):
        return self.cast(b)-self
    def __mul__(self,b):
        b=self.cast(b)
        return Jet(*(sum(self.c[j]*b.c[i-j] for j in range(i+1))
                     for i in range(3)))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=self.cast(b)
        c0=1/b.c[0]
        c1=-b.c[1]/b.c[0]**2
        c2=b.c[1]**2/b.c[0]**3-b.c[2]/b.c[0]**2
        return self*Jet(c0,c1,c2)
    def __pow__(self,n):
        ans=Jet(1)
        for _ in range(n):
            ans*=self
        return ans


def determinant(a):
    a=[r[:] for r in a]
    ans=Jet(1)
    for j in range(len(a)):
        pivot=a[j][j]
        assert pivot.c[0]
        ans*=pivot
        for i in range(j+1,len(a)):
            f=a[i][j]/pivot
            for k in range(j+1,len(a)):
                a[i][k]-=f*a[j][k]
    return ans


def physical_jet(B, groups):
    m=len(B); d=m-1
    W=[[Jet(i==j,B[i][j]) for j in range(m)] for i in range(m)]
    vol=determinant(W)
    L=vol
    for i,rows in enumerate(groups):
        for a,ell in rows:
            cap=vol*(W[i][i]-a)**d
            for j in range(m):
                if i!=j:
                    cap/=W[i][i]-W[i][j]
            L-=ell*cap
    return L


def effective_Q(B,e,mu):
    m=len(B);d=m-1
    T=sum(B[i][i] for i in range(m))
    tr2=sum(B[i][j]*B[j][i] for i in range(m) for j in range(m))
    ans=T*T-tr2
    for i in range(m):
        b=B[i][i]
        row=sum(B[i][j] for j in range(m) if j!=i)
        ans-=e*((T+row+d*(mu-1)*b)**2-tr2-d*mu*mu*b*b
                    +sum((b-B[i][j])**2 for j in range(m) if j!=i))
    return ans


def stats(rows,d):
    eta=[ell*(1-a)**d for a,ell in rows]
    e=sum(eta)
    mu=sum(x/(1-a) for x,(a,ell) in zip(eta,rows))/e
    var=sum(x*(1/(1-a)-mu)**2 for x,(a,ell) in zip(eta,rows))/e
    return e,mu,var


rng=Random(89103)
checks=0
for d in range(2,7):
    m=d+1
    for trial in range(15):
        # Each vertex has a different two-threshold law with the same mean.
        mu=F(m,d)+F(trial%3,10)
        e=1/(d*mu)
        groups=[]
        for i in range(m):
            low=F(1)+F(rng.randrange(1,5),10)*(mu-1)
            high=mu+F(rng.randrange(1,8),5)
            prob=(mu-low)/(high-low)
            rows=[]
            for X,p in [(low,1-prob),(high,prob)]:
                a=1-1/X
                rows.append((a,e*p/(1-a)**d))
            assert stats(rows,d)[:2]==(e,mu)
            groups.append(rows)
        B=[[F(0) for _ in range(m)] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if i!=j:
                    B[i][j]=F(rng.randrange(-5,6),7)
        for j in range(m):
            B[j][j]=-sum(B[i][j] for i in range(m) if i!=j)
        jet=physical_jet(B,groups)
        assert jet.c[1]==0
        correction=d*(d-1)*e*sum(stats(groups[i],d)[2]*B[i][i]**2
                                       for i in range(m))
        assert 2*jet.c[2]==effective_Q(B,e,mu)-correction
        checks+=1

# Concurrent groups and negative definiteness in every tested dimension.
for d in range(2,21):
    m=d+1
    high=1-F(d,3*m);low=F(1,3*m)
    etaH=F(1,3*m*m);etaL=F(3*m-1,3*m*m*d)
    assert high+d*low==1
    rows=[(high,etaH/(1-high)**d)]+[(low,etaL/(1-low)**d)]*d
    e,mu,var=stats(rows,d)
    assert (e,mu,var)==(F(1,m),F(m,d),F(4*m*m,d*d*(3*m-1)))
    theta=d*(d-1)*e*var
    assert F(1,d)-theta==-F(m*(4*d-7)+1,d*(3*m-1))<0
    checks+=1

# The separately stated planar concurrent example.
rows=[(F(4,5),F(5,6))]+[(F(1,10),F(5,27))]*2
assert stats(rows,2)==(F(1,3),F(3,2),F(49,36))
assert F(1,2)-F(2,3)*F(49,36)==-F(11,27)

# Two actual exposed triangles: all SIX global caps have one common mass.
low,high=F(1,10),F(4,5)
assert (1-low)**2+(1-high)**2==F(17,20)
ell=F(5,11)
rows=[(low,ell),(high,ell)]
e,mu,var=stats(rows,2)
assert (e,mu,var)==(F(17,44),F(22,17),F(196,289))
indices=[(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]
basis=[]
for i,j in indices:
    B=[[F(0)]*3 for _ in range(3)]
    B[i][j]=F(1);B[j][j]=F(-1)
    basis.append(B)

def q(B):
    jet=physical_jet(B,[rows]*3)
    assert jet.c[1]==0
    return 2*jet.c[2]

Q=S.zeros(6)
for i in range(6):
    Q[i,i]=S.Rational(q(basis[i]))
    for j in range(i):
        both=[[basis[i][k][l]+basis[j][k][l] for l in range(3)] for k in range(3)]
        Q[i,j]=Q[j,i]=S.Rational((q(both)-q(basis[i])-q(basis[j]))/2)
x=S.symbols('x')
target=(11*x+6)*(11*x+7)*(121*x*x+143*x+27)**2/S.Integer(1771561)
assert S.expand(Q.charpoly(x).as_expr()-target)==0
expected=[S.Rational(13,22),S.Rational(36,121),S.Rational(234,1331),
          S.Rational(1127,14641),S.Rational(12987,322102),S.Rational(30618,1771561)]
assert [(-Q)[:i,:i].det() for i in range(1,7)]==expected
assert all(v>0 for v in expected)
assert F(17,40)>F(2,9)
print('PASS:',checks,'exact second-order variance and concurrent-family checks;')
print('planar examples, equal global budgets, complete Hessian characteristic polynomial and principal minors')
