"""Exact arithmetic checks for the ambient-simplex identities."""
from fractions import Fraction as F
from math import comb, factorial
from itertools import permutations

def dd_power(knots,s,p):
    hs=sorted(map(F,knots));n=len(hs)
    tab=[(h-s)**p if h>s else F(0) for h in hs]
    for k in range(1,n):
        nxt=[]
        for i in range(n-k):
            if hs[i+k]==hs[i]:
                # Interior repeated knots require at most p-1 derivatives.
                if hs[i]==s and k>=p:raise ValueError("Use the inward endpoint rule")
                v=F(comb(p,k))*(hs[i]-s)**(p-k) if k<=p and hs[i]>s else F(0)
            else:v=(tab[i+1]-tab[i])/(hs[i+k]-hs[i])
            nxt.append(v)
        tab=nxt
    return tab[0]
def density(knots,s):
    hs=list(map(F,knots));s=F(s);m=len(hs)-1;lo=min(hs);hi=max(hs)
    assert lo<hi
    if s<lo or s>hi:return F(0)
    if s in (lo,hi):
        if hs.count(s)!=m:return F(0)
        other=next(x for x in hs if x!=s)
        return F(m)/abs(other-s)
    return m*dd_power(hs,s,m-1)
def mom(knots,s,i):
    return density([*knots,knots[i]],s)/len(knots)
def clip(P,a,b,c):
    if not P:return []
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        v=a*p[0]+b*p[1]+c;w=a*q[0]+b*q[1]+c
        if v>=0:out.append(p)
        if (v<0<w) or (w<0<v):
            t=v/(v-w);out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return out
def moments(P):
    if len(P)<3:return F(0),F(0),F(0)
    cr=[p[0]*q[1]-p[1]*q[0] for p,q in zip(P,P[1:]+P[:1])]
    area=sum(cr)/2
    ix=sum((p[0]+q[0])*v for p,q,v in zip(P,P[1:]+P[:1],cr))/6
    iy=sum((p[1]+q[1])*v for p,q,v in zip(P,P[1:]+P[:1],cr))/6
    assert area>=0
    return area,ix,iy
def fiber(hs,z):
    a,b,h1,h2=hs
    T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
    P=clip(T,-(h1-a),-(h2-a),z-a)
    return clip(P,h1-b,h2-b,b-z)
checks=0

# All knot multiplicities, including positive full-dimensional endpoint facets.
for d in range(1,9):
    m=d+1
    for a,b in ((F(0),F(1)),(F(-2),F(3))):
        hs=[a]*m+[b]
        assert density(hs,a)==F(m)/(b-a)
        assert density(hs,b)==0
        assert density([a]+[b]*m,b)==F(m)/(b-a)
        for i in range(m+1):
            J=mom(hs,a,i)
            assert J==(density(hs,a)/m if i<m else 0)
        for s in (a+(b-a)/4,a+(b-a)/2,a+3*(b-a)/4):
            assert density(hs,s)==F(m)*(b-s)**(m-1)/(b-a)**m
            assert sum(mom(hs,s,i) for i in range(m+1))==density(hs,s)
            assert sum(hs[i]*mom(hs,s,i) for i in range(m+1))==s*density(hs,s)
            checks+=1
# Nonconstant multi-height repeated vectors: density and moment constraints.
for hs in ([F(0),F(1),F(1),F(2),F(4)],
           [F(0),F(4),F(19,10),F(21,10),F(2),F(2),F(2)],
           [F(-1),F(0),F(0),F(2),F(2),F(3)]):
    for s in sorted(set([*hs,*[F(k,4) for k in range(-4,17)]])):
        f=density(hs,s)
        assert f>=0
        assert sum(mom(hs,s,i) for i in range(len(hs)))==f
        assert sum(hs[i]*mom(hs,s,i) for i in range(len(hs)))==s*f
        checks+=1

# Geometric planar slices of genuine 3D simplices, including vertical caps.
cases=[[F(0),F(4),F(1),F(2)],
       [F(0),F(1),F(0),F(0)], # positive minimum endpoint facet
       [F(0),F(1),F(1),F(1)], # positive maximum endpoint facet
       [F(-1),F(3),F(0),F(2)],
       [F(0),F(4),F(2),F(2)]]
for hs in cases:
    a,b,h1,h2=hs;V=(b-a)/6
    for z in range(int(a),int(b)+1):
        P=fiber(hs,F(z));w,ix,iy=moments(P)
        assert w==V*density(hs,F(z))
        js=[((b-z)*w-(b-h1)*ix-(b-h2)*iy)/(b-a),
            ((z-a)*w-(h1-a)*ix-(h2-a)*iy)/(b-a),ix,iy]
        assert js==[V*mom(hs,F(z),i) for i in range(4)]
        checks+=1
    for c in (F(0),F(1,5),F(1,3),F(1,2),F(4,5)):
        for i in range(4):
            actual=F(0)
            for z in range(int(a),int(b)+1):
                P=fiber(hs,F(z))
                margins=[(h1-b,h2-b,b-z-c*(b-a)),
                         (-(h1-a),-(h2-a),z-a-c*(b-a)),
                         (F(1),F(0),-c),(F(0),F(1),-c)]
                actual+=moments(clip(P,*margins[i]))[0]
            formula=(1-c)**2*V*sum(density(hs,(F(z)-c*hs[i])/(1-c)) for z in range(int(a),int(b)+1))
            assert actual==formula
            checks+=1

# A concrete n=2,d=2 block normal form and its constant fiber Jacobian.
def det(A):
    n=len(A);total=F(0)
    for p in permutations(range(n)):
        term=F((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n):term*=A[i][p[i]]
        total+=term
    return total
normal=[(0,0,0,0),(3,0,0,0),(0,1,0,0),(1,2,1,0),(-1,1,0,1)]
def old(v):
    z1,z2,x1,x2=map(F,v)
    return (z1,z2,2*x1+x2+z1,3*x2-z2)
original=list(map(old,normal))
vol=lambda vs:abs(det([[F(vs[j+1][i])-F(vs[0][i]) for j in range(4)] for i in range(4)]))/factorial(4)
assert vol(normal)==F(1,8) and vol(original)==F(3,4)
Qarea=F(3,2)
J=factorial(2)*Qarea/(factorial(4)*vol(original))
assert J==F(1,6)==vol(normal)/vol(original)
checks+=1

# Exact nonhomothetic d5 simplex, its mixed true centroid and actual cap.
d=5;e=F(1,10);m=d+1;VT=F(1,factorial(d));VC=F(4,factorial(d+1))
hs=[F(0),F(4),2-e,2+e]+[F(2)]*(d-2)
a=F(2)**(2-d)/(4-e*e);W=2/(2+e);mass=W+2*a
assert [VC*density(hs,F(z))/VT for z in range(5)]==[0,a,W,a,0]
Ji=[sum(VC*mom(hs,F(z),i) for z in range(5)) for i in range(len(hs))]
assert sum(h*J for h,J in zip(hs,Ji))/(mass*VT)==2
# Remaining barycentrics are exactly the continuous x coordinates.
centroid=[J/(mass*VT) for J in Ji[2:]]
q=sum(centroid)
q_formula=(W*(d-e/(2+e))+2*a*(F(d,2)+e*e/(4-e*e)))/(m*mass)
assert q==q_formula==F(310337,387828)
assert centroid[0]==centroid[1]==F(15301,96957)
assert centroid[2:]==[F(157,972)]*3
assert a==F(25,798) and W==F(20,21) and mass==F(135,133)
assert F(10,19)<q<F(20,21) and q<F(161,200)
G=F(5,6)**5
assert G*mass-((F(161,200))**5+2*a)==F(2763786689203,383040000000000)>0
H=q**d+2*a
assert H<G*mass
assert G*W/mass==F(59375,157464)>G/2
# Projected count failure occurs at interior points with open stable counts.
for s,expected in ((F(2,5),3),(F(3,5),1),(F(4,5),1)):
    lower=2*s;upper=4-2*s
    count=sum(lower<=z<=upper for z in range(5))
    assert count==expected and lower.denominator!=1 and upper.denominator!=1
checks+=1
print("PASS:",checks,"exact knot, moment, geometric slice, closed-cap, Jacobian, and d5 checks.")
print("d5 actual through-centroid cap / total mass:",float(H/mass))
print("Gamma5:",float(G),"; certified safe middle-centroid bound:",float(G*W/mass))
