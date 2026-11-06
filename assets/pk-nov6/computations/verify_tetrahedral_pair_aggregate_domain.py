from fractions import Fraction as F
from random import Random
rng=Random(266019)
for _ in range(3000):
 ints=[rng.randint(1,80)for _ in range(4)];x,y,z,w=[F(q,sum(ints))for q in ints]
 P=x+y;R=z+w;a=x*y;b=z*w;k=a-b;D=k*k+a*R+b*P
 Ds=[(x+z)*(x+w),(y+z)*(y+w),(x+z)*(y+z),(x+w)*(y+w)]
 delta=[(b-k*x)/Ds[0],(b-k*y)/Ds[1],(a+k*z)/Ds[2],(a+k*w)/Ds[3]]
 lam=[(1-t)/3 for t in delta];assert sum(lam)==1;assert all(t>0 for t in lam)
 central=all(t>=0 for t in delta)
 assert central==all(g>=0 for g in [2*b-k*P,b*b-b*k*P+k*k*a,2*a+k*R,a*a+a*k*R+k*k*b])
 U=P*(b+k*k)-2*k*(a+b);V=b*b-b*k*P+k*k*a;W=R*(a+k*k)+2*k*(a+b);Z=a*a+a*k*R+k*k*b
 assert U+W==D
 assert [sum(delta[:2]),delta[0]*delta[1],sum(delta[2:]),delta[2]*delta[3]]==[U/D,V/D,W/D,Z/D]
 m1=(W-U)*W+2*(V-Z)*D;m2=(W-U)**2*Z+(W-U)*(V-Z)*W+(V-Z)**2*D
 middle=min(delta[:2])<=min(delta[2:])<=max(delta[2:])<=max(delta[:2])
 assert middle==(m1<=0 and m2>=0)
 B=2*D-3*W+4*Z;N=D-W+Z
 if B!=0:
  c=F(4,3)*N/B
  assert c==4/(12-1/lam[2]-1/lam[3])
  f=b*(P-a+b)/D;s=3*(b*P-a*R)/(4*D)
  assert f-c*s==(b*(P-a+b)*B-N*(b*P-a*R))/(D*B)
print('PASS: exact pair aggregate identities, centrality equivalence, and middle-pair equivalence; no positivity inference.')
