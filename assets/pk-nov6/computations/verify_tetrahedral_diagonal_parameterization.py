from fractions import Fraction as F

def centroid(E):
 x,y,z,w=E
 return (x*(1/(x+z)+1/(x+w)-1)/3,
         y*(1/(y+z)+1/(y+w)-1)/3,
         z*(1/(x+z)+1/(y+z)-1)/3,
         w*(1/(x+w)+1/(y+w)-1)/3)
def data(E):
 x,y,z,w=E;P=x+y;R=z+w;a=x*y;b=z*w;D=(x+z)*(x+w)*(y+z)*(y+w)
 assert D==(a-b)**2+a*R+b*P
 p,q,r,s=1/x,1/y,1/z,1/w
 alpha=p*s/((p+r)*(p+s)*(q+s));delta=q*r/((p+r)*(q+s)*(q+r))
 cap=p*(alpha+delta)+q*q/((q+r)*(q+s))
 assert cap==b*(P-a+b)/D
 assert 1-cap==a*(R+a-b)/D
 assert alpha+delta==x*y*z*w/D
 scalar=3*(alpha+delta)*(p+q-r-s)/4
 assert scalar==3*(b*P-a*R)/(4*D)
 lam=centroid(E);assert sum(lam)==1;assert all(l>0 for l in lam)
 assert sum(t*l for t,l in zip((p,q,-r,-s),lam))==0
 return lam,cap,scalar
for ints in [(1,2,3,4),(2,2,3,3),(7,4,8,2),(12,7,3,3),(7,12,3,3),(56,56,19,19)]:
 E=tuple(F(i,sum(ints))for i in ints);data(E)
lam=tuple(F(i,150)for i in (56,56,19,19))
for ints in [(12,7,3,3),(7,12,3,3)]:
 result=data(tuple(F(i,25)for i in ints))
 assert result==(lam,F(4,25),-F(111,400))
assert centroid(lam)==lam
for t in [(7,12,-28,-28),(12,7,-28,-28),(19,19,-56,-56)]:assert sum(l*v for l,v in zip(lam,t))==0
print('PASS: exact formulas and three distinct same-centroid sections in one partition.')
L=[F(8,25),F(31,100),F(1,20),F(8,25)]
def uv_cap(u,v):
 p=u/L[0];q=(1-u)/L[1];r=v/L[2];s=(1-v)/L[3]
 al=p*s/((p+r)*(p+s)*(q+s));de=q*r/((p+r)*(q+s)*(q+r))
 return p*(al+de)+q*q/((q+r)*(q+s))
values=[uv_cap(F(3,5),F(i,1000))for i in (9,10,11)]
assert values[0]+values[2]-2*values[1]==-F(216696601290923321682823000,135221182702189782497027701155183)
print('PASS: exact obstruction to the global convex-in-v shortcut.')
for ints in [(1,2,3,4),(12,7,3,3),(7,4,8,2),(9,1,6,4)]:
 E=tuple(F(i,sum(ints))for i in ints);x,y,z,w=E;a=x*y;b=z*w;D=(a-b)**2+a*(z+w)+b*(x+y);lam=centroid(E)
 assert 3*(lam[0]-lam[1])==(x-y)*(b-(a-b)**2)/D
 assert 3*(lam[2]-lam[3])==(z-w)*(a-(a-b)**2)/D
 if max(lam)<=F(1,3):assert (a-b)**2<min(a,b)
print('PASS: within-pair difference identities and central-region examples.')
