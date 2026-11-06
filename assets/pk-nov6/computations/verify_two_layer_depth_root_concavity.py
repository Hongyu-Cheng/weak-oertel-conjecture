from fractions import Fraction as F

def tri_tail(p,t,vol):
    a,b,c=sorted(p)
    if t<=a:return vol
    if t>=c:return F(0)
    if t>=b:return vol*(c-t)**2/((c-a)*(c-b))
    return vol*(1-(t-a)**2/((c-a)*(b-a)))

def optimized(p,q,theta,s):
    v=F(1,2)
    pts=sorted(set(list(p)+[(s-theta*t)/(1-theta) for t in q]))
    def fun(t):
        return tri_tail(p,t,v)+tri_tail(q,(s-(1-theta)*t)/theta,v)
    best=min([v]+[fun(t) for t in pts])
    for l,r in zip(pts,pts[1:]):
        mid=(l+r)/2;fl,fm,fr=fun(l),fun(mid),fun(r)
        aa=2*(fl+fr-2*fm)/(r-l)**2
        bb=(fr-fl)/(r-l)-aa*(l+r)
        if aa>0:
            t=-bb/(2*aa)
            if l<t<r:best=min(best,fun(t))
    return best

def sqrt_mid_concave(a,m,b):
    d=4*m-a-b
    return d>=0 and d*d>=4*a*b

A=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
C=[(F(0),F(0)),(F(2),F(0)),(F(0),F(1,2))]
count=0
for u in [(1,0),(0,1),(1,1),(1,-1),(2,1),(1,2)]:
 p=[u[0]*x+u[1]*y for x,y in A]
 q=[u[0]*x+u[1]*y for x,y in C]
 for theta in [F(1,3),F(1,2),F(2,3)]:
  lo=(1-theta)*min(p)+theta*min(q)
  hi=(1-theta)*max(p)+theta*max(q)
  xs=[lo+(hi-lo)*F(i,12) for i in range(13)]
  vals=[optimized(p,q,theta,x) for x in xs]
  assert vals[0]==F(1,2) and vals[-1]==0
  for i in range(len(xs)):
   for j in range(i,len(xs)):
    mid=optimized(p,q,theta,(xs[i]+xs[j])/2)
    assert sqrt_mid_concave(vals[i],mid,vals[j]),(u,theta,i,j)
    count+=1
print(f'PASS: {count} exact quadratic-profile root-concavity checks with unequal shapes, nonmidpoint bases, full/empty caps and moving cutoffs')
def dependent_interval_depth(x):
    return min(x+min(2*x,1),2-x+min(2*max(F(0),1-x),1))
assert dependent_interval_depth(F(3,4))==F(7,4)
assert dependent_interval_depth(F(1))==1
assert dependent_interval_depth(F(5,4))==F(3,4)
assert dependent_interval_depth(F(1))<(F(7,4)+F(3,4))/2
print('PASS: exact affinely dependent three-layer failure of root concavity')
