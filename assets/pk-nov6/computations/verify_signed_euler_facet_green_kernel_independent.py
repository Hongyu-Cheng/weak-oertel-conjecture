from fractions import Fraction as F
U=[(1,0),(0,1),(-1,-1)]
Q=[[[236,236,-520],[-267,31,260]],[[225,197,-565],[-192,139,203]],[[197,225,-565],[-336,-33,363]],[[271,271,-656],[-371,100,328]]]
Q=[[[F(v,100) for v in row] for row in q] for q in Q]
L=[[-1,-1,F(1,10)],[1,-2,-F(9,10)],[-2,1,-F(9,10)],[1,1,-F(19,10)]]
R=[(F(1,20),F(1,20)),(F(19,20),F(1,40)),(F(1,40),F(19,20)),(F(19,20),F(19,20))]
Z=[(0,0),(1,0),(0,1),(1,1),(2,1),(1,2)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def ev(q,z):return [dot(row,(*z,1)) for row in q]
def margin(s,j,z,x):return dot(U[j],[xx-yy for xx,yy in zip(x,ev(Q[s],z))])+dot(L[s],(*z,1))
mi=100
for s,r in enumerate(R):
 x=ev(Q[s],r)
 for t in range(4):
  for j in range(3):
   m=margin(t,j,r,x)
   if t==s:assert m==0
   else:assert m<0;mi=min(mi,-m)
print('crosscontact minimum',mi)
W=[1,1,1,100,100,100]
def cap_fraction(s,j,z,rad):
 poly=[(-rad,-rad),(rad,-rad),(rad,rad),(-rad,rad)]
 out=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  va=margin(s,j,z,a);vb=margin(s,j,z,b)
  if va>=0:out.append(a)
  if (va<0<vb) or (vb<0<va):
   t=va/(va-vb);out.append(tuple(aa+t*(bb-aa) for aa,bb in zip(a,b)))
 if len(out)<3:return F(0)
 area=abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(out,out[1:]+out[:1])))/2
 return area/(4*rad*rad)
allm=[]
for s in range(4):
 caps=[];masses=[]
 for j,u in enumerate(U):
  fr=[]
  for i,z in enumerate(Z):
   rad=F(1,1000) if i<3 else F(1,100)
   fr.append(cap_fraction(s,j,z,rad))
  caps.append(fr);masses.append(sum(W[i]*fr[i] for i in range(6)))
 allm.append(masses)
 print(s,caps,masses)
print('summax',sum(max(m) for m in allm),'gM',F(4,9)*sum(W),'gap',F(4,9)*sum(W)-sum(max(m) for m in allm))
assert allm == [[F(3),F(0),F(0)],[F(3),F(0),F(0)],[F(3),F(0),F(1,2)],[F(103),F(100),F(100)]]
assert F(4,9)*sum(W)-sum(max(m) for m in allm)==F(68,3)
assert mi==F(923,2000)
assert [(a,b) for a in range(-2,5) for b in range(-2,5) if a>=0 and b>=0 and abs(a-b)<=1 and a+b<=3]==[(0,0),(0,1),(1,0),(1,1),(1,2),(2,1)]
def green_integral(t):
 cuts=sorted(set([F(0),F(1,3),t,F(2,3),F(1)]));ans=F(0)
 for a,b in zip(cuts,cuts[1:]):
  m=(a+b)/2;w=F(2,9) if F(1,3)<m<F(2,3) else -F(1,9)
  if m<t: ans+=w*(1-t)*(b*b-a*a)/2
  else: ans+=w*t*((b-a)-(b*b-a*a)/2)
 return ans
for i in range(301):
 t=F(i,300)
 expected=t*t/18 if t<=F(1,3) else ((6*t*(1-t)-1)/54 if t<=F(2,3) else (1-t)**2/18)
 assert green_integral(t)==expected
 assert expected>=0
# Product certificate and its raw strict budget.
t=F(3,10);a=F(1,3)-t;q=(1-t)**2;alpha=F(99,200)
assert a==F(1,30) and 2*a-1==-F(14,15)
assert F(4,9)<q<alpha<F(1,2)
print('PASS: exact cap clipping, lattice data, 301 Green-kernel values, and strict floating-body arithmetic.')
