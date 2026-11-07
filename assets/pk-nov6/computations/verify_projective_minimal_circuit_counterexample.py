from fractions import Fraction as F
from math import prod
p,q,r,s=map(F,[14,11,22,4]);t=[p,q,-r,-s]
a=p*s/((p+r)*(p+s)*(q+s));b=q*r/((p+r)*(q+s)*(q+r));tau=a/(a+b)
l=[(r/(p+r)+tau*s/(p+s))/3,(s/(q+s)+(1-tau)*r/(q+r))/3,(p/(p+r)+(1-tau)*q/(q+r))/3,(q/(q+s)+tau*p/(p+s))/3]
assert l==[F(191,846),F(518,2115),F(527,2538),F(2041,6345)]
assert sum(l)==1 and all(0<x<F(1,3) for x in l)
def cap(t):
 pp=[x for x in t if x>0];nn=[-x for x in t if x<0]
 if len(pp)==1:return pp[0]**3/prod(pp[0]+x for x in nn)
 if len(nn)==1:return 1-nn[0]**3/prod(nn[0]+x for x in pp)
 p,q=pp;r,s=nn;a=p*s/((p+r)*(p+s)*(q+s));b=q*r/((p+r)*(q+s)*(q+r));return p*(a+b)+q*q/((q+s)*(q+r))
records=[(t,3*(a+b))]
for i,sign in [(3,1),(0,-1),(1,-1)]:
 tt=[F(3) if j==i else 3-1/l[j] for j in range(4)];records.append(([sign*x for x in tt],27*prod(l[j] for j in range(4) if j!=i)))
qs=[[co*(tt[j]-tt[0]) for j in range(1,4)] for tt,co in records]
w=[F(x,646372709662) for x in [220438125401,35599660824,204746742725,185588180712]]
assert sum(w)==1 and min(w)>0
assert all(sum(ww*qq[j] for ww,qq in zip(w,qs))==0 for j in range(3))
a,b,c=qs[:3];det=a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
assert det==F(-1007454833,210241575)
before=[cap(tt) for tt,co in records];after=[cap([4*l[j]*tt[j] for j in range(4)]) for tt,co in records]
assert before==[F(626,1215),F(26070163,84096630),F(352142512,630724725),F(299138843,504579780)]
assert after==[F(7600699714514571,14642033640793712),F(1308023834,3094640563),F(668014703,1190605028),F(2063099,3673043)]
P=sum(x*y for x,y in zip(w,before));PP=sum(x*y for x,y in zip(w,after))
assert P==F(1570274946076,2908677193479)
assert P>F(2699,5000)>F(2697,5000)>PP>F(1,2)
assert P-PP==F(28806586307638718783098471763459517260148517939,52713492989801516599920096514147547346967285659744)
assert F(27,64)<1-P<1-PP<F(1,2)
print('PASS: exact centroid equations, rank-three minimal positive circuit, original/projective cap fractions, and strict contraction failure.')
