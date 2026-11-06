"""Exact scalar identities and actual shared-normal/all-tilt peak checks."""
from fractions import Fraction as F
import sympy as S

a,b,c,e,h,v=S.symbols('a b c e h v',real=True)
def eq(x,y):assert S.factor(x-y)==0,(x,y,S.factor(x-y))
T1=S.Rational(2,9)*(1+b*b+c*c+(2*b-1)**2)
hp=b-S.Rational(4,3)*(1-c)
Q=S.Rational(4,9)+hp*hp/2-T1
eq(Q.subs(c,b+v),(5*b-4)**2/18+(S.Rational(8,3)*b-S.Rational(16,9))*v+S.Rational(2,3)*v*v)
eq(Q.subs(c,b+v)-S.Rational(2,3)*(v-S.Rational(4,3)+2*b)**2,
   -(69*b*b-72*b+16)/54)
assert (69*b*b-72*b+16).subs(b,S.Rational(1,2))==-S.Rational(11,4)
assert (69*b*b-72*b+16).subs(b,S.Rational(2,3))==-S.Rational(4,3)
roof=S.Rational(11,2)*b-S.Rational(89,16)*b*b-1
assert roof.subs(b,S.Rational(1,2))==S.Rational(23,64)
assert roof.subs(b,S.Rational(4,7))==S.Rational(16,49)
R1=10*b*b-8*b+2*c*c
R2=14*c*c+6*b*b-6
D1=S.expand(9*(7*h*h-R1).subs({b:1-e,c:h+S.Rational(4,3)*e}))
D2=S.expand(9*(35*h*h-R2).subs({b:1-e,c:h+S.Rational(4,3)*e}))
eq(D1,45*(h-S.Rational(8,15)*e)**2+108*e-S.Rational(674,5)*e*e-18)
eq(D2,189*(h-S.Rational(8,9)*e)**2+e*(108-S.Rational(1282,3)*e))
assert (108-S.Rational(1282,3)*e).subs(e,S.Rational(1,4))==S.Rational(7,6)
g=108*e-S.Rational(674,5)*e*e-18
assert g.subs(e,S.Rational(1,4))==S.Rational(23,40)
assert g.subs(e,S.Rational(3,7))==S.Rational(864,245)
g0=108*e-18-122*e*e
assert g0.subs(e,S.Rational(1,4))==S.Rational(11,8)
assert g0.subs(e,S.Rational(1,3))==S.Rational(40,9)

def bounds(aa,bb,cc):
    hh=max(F(0),min(bb,cc)-F(4,3)*(1-max(bb,cc)))
    return (4*bb*bb+7*aa*aa)/9,(4+7*hh*hh)/9

def cap(rr,q,u):
    lo,mid,hi=sorted([F(0),u[0]*rr,u[1]*rr])
    if q<=lo:return rr*rr
    if q>=hi:return F(0)
    if q<=mid:return rr*rr*(1-(q-lo)**2/((mid-lo)*(hi-lo)))
    return rr*rr*(hi-q)**2/((hi-lo)*(hi-mid))

def minimum(rs,j,u):
    q0=(u[0]+u[1])*rs[j]/3
    breaks=sorted({(q0-q)/(k-j) for k,r in enumerate(rs) if k!=j
                   for q in (F(0),u[0]*r,u[1]*r)})
    def value(beta):
        return sum(cap(r,q0-beta*(k-j),u) for k,r in enumerate(rs))
    candidates=[value(beta) for beta in breaks]
    for L,H in zip(breaks,breaks[1:]):
        z0,z1,z2=(3*L+H)/4,(L+H)/2,(L+3*H)/4
        f0,f1,f2=value(z0),value(z1),value(z2);step=z1-z0
        A=(f2-2*f1+f0)/(2*step*step)
        B=(f2-f0)/(2*step)-2*A*z1
        if A>0:
            beta=-B/(2*A)
            if L<beta<H:candidates.append(value(beta))
    return min(candidates)

scalar=actual=0
for ib in range(11,21):
    bb=F(ib,20)
    for ia in range(1,2*ib-20+1):
        aa=F(ia,20)
        for ic in range(1,21):
            cc=F(ic,20);L1,L2=bounds(aa,bb,cc)
            target=F(2,9)*(aa*aa+bb*bb+1+cc*cc)
            assert max(L1,L2)>=target
            scalar+=1

normals=[(1,0),(0,1),(1,1),(1,2),(1,3),
         (-1,0),(-1,-1),(-1,-2),(1,-1),(1,-2),(-1,2)]
for ib in range(5,9):
    bb=F(ib,8)
    for ia in range(1,2*ib-8+1):
        aa=F(ia,8)
        for ic in range(1,9):
            cc=F(ic,8);rs=[aa,bb,F(1),cc];L1,L2=bounds(aa,bb,cc)
            for j,L in [(1,L1),(2,L2)]:
                for ui in normals:
                    u=tuple(F(t) for t in ui)
                    assert minimum(rs,j,u)>=L,(rs,j,u,minimum(rs,j,u),L)
                    actual+=1
                # Closed vertical through-caps retain the entire anchor fiber.
                assert sum(rs[k]**2 for k in range(j+1))>=L
                assert sum(rs[k]**2 for k in range(j,4))>=L
print("PASS: all scalar completion identities;",scalar,"exact radius triples;")
print(actual,"actual normal/all-tilt lower bounds plus closed vertical caps.")
