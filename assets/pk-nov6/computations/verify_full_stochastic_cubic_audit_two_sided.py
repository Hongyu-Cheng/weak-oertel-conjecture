from fractions import Fraction as F
from itertools import product
import sympy as s

checks=0
def check(v):
    global checks
    assert v
    checks+=1

rr,ss,tt,aa,cc,LL,zz=s.symbols('r s t a c L z')
Z=(ss+tt-ss*tt)*(rr+tt-rr*tt)
identities=[
    (Z-(rr*(ss+tt)-ss*tt),tt*(1-rr)*(tt*(1-ss)+2*ss)),
    (Z-(ss*(rr+tt)-rr*tt),tt*(1-ss)*(tt*(1-rr)+2*rr)),
    (Z-(tt*(rr+ss)-rr*ss),tt**2*(1-rr)*(1-ss)+2*rr*ss*(1-tt)),
    ((1-zz-LL*aa)*(1-zz-LL*cc)-LL**2*aa*cc*zz,
     (1-zz)*((1-aa*LL)*(1-cc*LL)-zz))]
for lhs,rhs in identities:
    check(s.expand(lhs-rhs)==0)

la,lb,lc=s.symbols('la lb lc',positive=True)
def Q(v,j):
    others=[i for i in range(3) if i!=j]
    k,l=others
    return v[j]*(v[k]+v[l])-v[k]*v[l]
v=(0,lc,-lb)
check(s.expand(Q(v,0)-lb*lc)==0)
v=(1,1,-(la+lb)/lc)
check(s.simplify(Q(v,0))==1)
check(s.simplify(Q(v,1))==1)
check(s.simplify(la*v[0]+lb*v[1]+lc*v[2])==0)
q,l,r,t=s.symbols('q l r t',positive=True)
second=s.diff(s.sqrt(q+l*t+r*t*t),t,2).subs(t,0)
check(s.simplify(second-(r/s.sqrt(q)-l*l/(4*q**s.Rational(3,2))))==0)
x,y,z=s.symbols('x y z',positive=True)
branches=[s.sqrt(Q((x,y,z),j)) for j in range(3)]
grad_diff=[s.simplify((s.diff(branches[0],v)-s.diff(branches[1],v)).subs(y,x))
           for v in (x,y,z)]
check(grad_diff==[z/x,-z/x,0])

def rowF(row):
    x,y,z=sorted(row)
    return z*(x+y)-x*y
def cubic(Fs):
    gap=1-sum(Fs)
    check(gap>=0)
    check(gap*gap>=4*Fs[0]*Fs[1]*Fs[2])

den=5
cols=[(F(a,den),F(b,den),F(den-a-b,den))
      for a in range(den+1) for b in range(den+1-a)]
for columns in product(cols,repeat=3):
    X=list(zip(*columns))
    cubic([rowF(row) for row in X])

def dot(u,v):return sum(a*b for a,b in zip(u,v))
def sub(p,q):return tuple(a-b for a,b in zip(p,q))
def clip(poly,u,c):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=dot(u,p)-c;fq=dot(u,q)-c
        if fp>=0:out.append(p)
        if fp*fq<0:
            t=fp/(fp-fq)
            out.append(tuple(p[j]+t*(q[j]-p[j]) for j in range(2)))
    return out
def area(poly):
    if not poly:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(poly,poly[1:]+poly[:1])))/2
def section(poly,u,c):
    pts=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=dot(u,p)-c;fq=dot(u,q)-c
        if fp==0:pts.append(p)
        if fp*fq<0:
            t=fp/(fp-fq)
            pts.append(tuple(p[j]+t*(q[j]-p[j]) for j in range(2)))
    pts=list(dict.fromkeys(pts))
    check(len(pts)==2)
    delta=sub(pts[1],pts[0])
    return abs(delta[0]/(-u[1])) if u[1] else abs(delta[1]/u[0])
def edge_fraction(f,g):
    if f>=0 and g>=0:return F(1)
    if f<=0 and g<=0:return F(0)
    return f/(f-g) if f>0 else g/(g-f)

T=[(F(0),F(0)),(F(3),F(0)),(F(0),F(2))];V=area(T)
ys=[(F(1),F(2,3)),(F(3,4),F(1,2)),(F(3,2),F(1,2)),(F(3,4),F(1))]
norms=[(F(i),F(j)) for i,j in product(range(-3,4),repeat=2) if (i,j)!=(0,0)]
twocaps=vertexcuts=0
for idx,u in enumerate(norms):
    for v in norms[::7]:
        if u[0]*v[1]-u[1]*v[0]==0:continue
        w=tuple(-u[j]-v[j] for j in range(2));ns=[u,v,w]
        for source in ys:
            qs=[];Ss=[];Es=[]
            for n in ns:
                level=dot(n,source)
                vals=[dot(n,p)-level for p in T]
                twocaps+=sum(t>0 for t in vals)==2
                vertexcuts+=any(t==0 for t in vals)
                cap=clip(T,n,level);Qcap=area(cap)/V
                sig=section(T,n,level);S=sig/V
                check(0<Qcap<1 and S>0)
                erow=[]
                for j in range(3):
                    k,l=[i for i in range(3) if i!=j]
                    e=edge_fraction(vals[k],vals[l])
                    check(e==Qcap-vals[j]*S/2)
                    erow.append(e)
                qs.append(Qcap);Ss.append(S);Es.append(erow)
            M=sum(q/sig for q,sig in zip(qs,Ss))
            X=[[e/(sig*M) for e in erow] for erow,sig in zip(Es,Ss)]
            for j in range(3):check(sum(X[i][j] for i in range(3))==1)
            Fs=[rowF(row) for row in X]
            for Frow,q,S in zip(Fs,qs,Ss):check(Frow==q/(S*S*M*M))
            cubic(Fs)

check(twocaps>0 and vertexcuts>0)
print(f'PASS: {checks} exact checks; {twocaps} two-vertex caps; {vertexcuts} vertex cuts')
