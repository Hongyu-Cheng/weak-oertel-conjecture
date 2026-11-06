"""Exact boundary and section calculations; no numerical optimization."""
from fractions import Fraction as F
import sympy as s
checks=0
def ck(v):
 global checks
 assert v
 checks+=1

t=s.symbols('t',real=True)
w=lambda a,b: s.integrate(t,(t,a,b))
# Exact margin-potential integrals on a triangle edge.
maximum=2*s.integrate(s.Rational(2,3)-t,(t,0,s.Rational(1,2)))
middle=2*s.integrate(s.Rational(2,3)-t,(t,s.Rational(1,3),s.Rational(1,2)))
ck(maximum==s.Rational(5,12));ck(middle==s.Rational(1,12))
ck(s.Rational(1,3)+middle/(3*maximum)==s.Rational(2,5))
total_sum=2*s.integrate(s.Rational(2,3)-t,(t,0,s.Rational(1,3)))+s.Rational(1,9)
ck(total_sum==s.Rational(4,9));ck(s.Rational(1,3)+s.Rational(1,9)/(3*total_sum)==s.Rational(5,12))
# A family of actual edge convex powers verifies the exact midpoint integration identity.
for j in range(2,15):
 f=t**j
 middle=s.integrate(f,(t,s.Rational(1,3),s.Rational(2,3)))
 total=s.integrate(f,(t,0,1))
 ck(total>3*middle)
# Hamming base hinges exactly isolate their measured fibers.
from itertools import product
for n in range(6):
 P=list(product((0,1),repeat=n))
 for z in P:
  values=[max(0,1-sum((1-pj)*zj+pj*(1-zj) for pj,zj in zip(p,z))) for p in P]
  ck(sum(values)==1);ck(values[P.index(z)]==1)

h=F(20,97);tt=F(100,291);ee=F(1,100);ss=3*tt-1
rho=[4*tt-1,F(1),F(1)]
theta=[(4*tt-1)/(6*tt-1),tt/(6*tt-1),tt/(6*tt-1)]
ck(sum(theta)==1);ck(h*h==12*tt*tt-4*tt)
normals=[(F(-1),F(-1)),(tt,ss),(ss,tt)]
ck(all(sum(rho[i]*normals[i][j] for i in range(3))==0 for j in range(2)))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(ps):return sum(cross(a,b) for a,b in zip(ps,ps[1:]+ps[:1]))/2
def cap(poly,v,c):
 out=[];cuts=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  fa=sum(x*y for x,y in zip(a,v))-c;fb=sum(x*y for x,y in zip(b,v))-c
  if fa>=0:out.append(a)
  if fa*fb<0:
   q=tuple(a[j]+fa/(fa-fb)*(b[j]-a[j]) for j in range(2));out.append(q);cuts.append(q)
 return out,cuts
mass=[F(0)]*3; section=[F(0)]*3; moment=[[F(0)]*3 for _ in range(3)]
weighted_boundary=s.Integer(0);perimeter=s.Integer(0)
for z in [-1,0,1]:
 rr=1+ee*z; poly=[(h,F(0)),(rr,F(0)),(F(0),rr),(F(0),h)]
 for i,v in enumerate(normals):
  c=-2*tt if i==0 else tt*(4*tt-1)+ee*tt*z
  cut,ends=cap(poly,v,c)
  ck(len(ends)==2);ck(area(cut)==2*tt*(1-2*tt))
  sig=abs(ends[1][0]-ends[0][0])/abs(v[1]) if v[1] else abs(ends[1][1]-ends[0][1])/abs(v[0])
  ck(sig==(2*tt if i==0 else 2))
  mass[i]+=area(cut);section[i]+=sig
  center=(F(z),(ends[0][0]+ends[1][0])/2,(ends[0][1]+ends[1][1])/2)
  for j in range(3):moment[i][j]+=sig*center[j]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  dx=b[0]-a[0];dy=b[1]-a[1]
  length=s.sqrt(s.Rational(dx)**2+s.Rational(dy)**2)
  perimeter+=length
  for i,v in enumerate(normals):
   c=-2*tt if i==0 else tt*(4*tt-1)+ee*tt*z
   fa=sum(x*y for x,y in zip(a,v))-c;fb=sum(x*y for x,y in zip(b,v))-c
   if fa>=0 and fb>=0:frac=F(1)
   elif fa<=0 and fb<=0:frac=F(0)
   elif fa>0:frac=fa/(fa-fb)
   else:frac=fb/(fb-fa)
   weighted_boundary+=s.Rational(theta[i]*frac)*length
for i in range(3):
 ck(mass[i]==6*tt*(1-2*tt))
 for j,e in enumerate([F(0),tt,tt]):ck(moment[i][j]==section[i]*e)
ck(section==[6*tt,F(6),F(6)])
root2=s.sqrt(2);T=s.Rational(tt);H=s.Rational(h)
expected_perim=3*((2+root2)+(root2-2)*H)
expected_weight=3*(4*(2+root2)*T*T+(root2-2)*H*(4*T-1))/(6*T-1)
ck(s.simplify(perimeter-expected_perim)==0)
ck(s.simplify(weighted_boundary-expected_weight)==0)
gap=4*(2+root2)*(T-s.Rational(1,3))**2+(root2-2)*H*(4*T/3-s.Rational(5,9))
ck(s.simplify((weighted_boundary-s.Rational(4,9)*perimeter)*(6*T-1)/3-gap)==0)
ck(F(1,3)<tt<F(5,12));ck(h>0)


# Signed radial boundary identity on the actual oblique example.
# On one oriented edge, n ds=(dy,-dx) du, so no radicals occur.
for A in [(F(0),F(0)),(F(1,3),F(-2,5)),(F(10),F(-7))]:
 total=F(0);captured=[F(0)]*3
 for z in [-1,0,1]:
  rr=1+ee*z;poly=[(h,F(0)),(rr,F(0)),(F(0),rr),(F(0),h)]
  center=(tt+A[0]*z,tt+A[1]*z)
  for aa,bb in zip(poly,poly[1:]+poly[:1]):
   dx=bb[0]-aa[0];dy=bb[1]-aa[1]
   density=dy*(aa[0]-center[0])-dx*(aa[1]-center[1])
   total+=density
   for i,v in enumerate(normals):
    c=-2*tt if i==0 else tt*(4*tt-1)+ee*tt*z
    fa=sum(x*y for x,y in zip(aa,v))-c;fb=sum(x*y for x,y in zip(bb,v))-c
    if fa>=0 and fb>=0:frac=F(1)
    elif fa<=0 and fb<=0:frac=F(0)
    elif fa>0:frac=fa/(fa-fb)
    else:frac=fb/(fb-fa)
    captured[i]+=density*frac
 expected_mass=sum(((1+ee*z)**2-h*h)/2 for z in [-1,0,1])
 ck(total==2*expected_mass)
 for value in captured:ck(value==2*mass[0])


# Actual exposed-endpoint radial localization in the oblique example.
endpoint_sections=[2*tt,F(2),F(2)]
Tvec=[sum(theta[j]*endpoint_sections[j]*normals[j][i] for j in range(3)) for i in range(2)]
ck(Tvec==[F(0),F(0)])
area_A=((1-ee)**2-h*h)/2;delta=2*tt*(1-2*tt)
endpoint_eff=(delta-2*ee*tt*tt/(6*tt-1))/area_A
ck(endpoint_eff==F(12368000000,27259241181))
ck(endpoint_eff-F(4,9)==F(758345092,81777723543))
# Independent boundary computation at z=-1, with the actual centroid of A.
rr=1-ee
g=(rr**3-h**3)/(3*(rr**2-h**2))
poly=[(h,F(0)),(rr,F(0)),(F(0),rr),(F(0),h)]
radial_den=F(0);radial_num=F(0)
for aa,bb in zip(poly,poly[1:]+poly[:1]):
 dx=bb[0]-aa[0];dy=bb[1]-aa[1]
 density=dy*(aa[0]-g)-dx*(aa[1]-g)
 ck(density>0)
 radial_den+=density
 for i,v in enumerate(normals):
  c=-2*tt if i==0 else tt*(4*tt-1)-ee*tt
  fa=sum(x*y for x,y in zip(aa,v))-c;fb=sum(x*y for x,y in zip(bb,v))-c
  if fa>=0 and fb>=0:frac=F(1)
  elif fa<=0 and fb<=0:frac=F(0)
  elif fa>0:frac=fa/(fa-fb)
  else:frac=fb/(fb-fa)
  radial_num+=theta[i]*density*frac
ck(radial_den==2*area_A)
ck(radial_num==2*delta-4*ee*tt*tt/(6*tt-1))
ck(radial_num/radial_den==endpoint_eff)
ck(2*F(101,100)**2<4)
print(f'PASS: {checks} exact critical-cap, coarea, boundary and potential checks')
