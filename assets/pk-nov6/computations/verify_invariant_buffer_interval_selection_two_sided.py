from fractions import Fraction as F
checks=0
def ck(p):
 global checks
 assert p; checks+=1
K=[(F(47,50),F(26,25)),(-F(11,10),F(1)),(-F(23,25),F(23,25)),(-F(9,100),F(9,100))]
L=[u-l for l,u in K]; M=sum(L); Sigma=sum(t**3 for t in L)/(12*M); c2=Sigma/M
ck(M==F(211,50));ck(Sigma==F(1937167,6330000));ck(c2==F(1937167,26712600))
ck(c2*max(L)==F(13560169,89042000));ck(c2*max(L)<1);ck(c2<1)
def energy(i,y):
 l,u=K[i];return 4*(y-l)*(u-y)/(u-l)
def ep(i,y):
 l,u=K[i];return -8*(y-(l+u)/2)/(u-l)
ck(energy(1,F(0))==F(44,21));ck(energy(2,F(0))==F(46,25));ck(energy(1,0)-energy(2,0)==F(134,525))
ck(ep(1,F(0))==F(-4,21));ck(ep(1,0)/(2*energy(1,0))==F(-1,22))
eta=F(1,1000); emax=F(1,10000); Q=F(11,10)
# Every status is checked under the full independent displacement interval.
# Margin u*x+a*(z-p); threshold lies between +/- (eta+emax).
rho=eta+emax
for p,u,a,expected in [(1,1,-F(1),'FP00'),(1,-1,-F(93,100),'0P00'),(2,1,F(2),'00PF'),(2,-1,F(2),'00PF')]:
 mass=F(0)
 for z,(lo,hi) in enumerate(K):
  mm=sorted([u*lo+a*(z-p),u*hi+a*(z-p)])
  st=expected[z]
  if st=='F':ck(mm[0]>rho);mass+=hi-lo
  elif st=='0':ck(mm[1]<-rho)
  else:
   ck(mm[0]<-rho);ck(mm[1]>rho)
   mass+=mm[1] # |u|=1
 ck(mass==Q)
for i in (1,2):
 for y in (-eta,eta):ck(energy(i,y)>1);ck(abs(ep(i,y))<1)
ck(Q-eta+4*emax==Q-F(3,5000));ck(max(L[0],L[3])/2==F(9,100))
ck(F(11,5)>Q+emax);ck(F(101,50)>Q+emax)
# Independent algebraic balance, all rational delta in a grid spanning range.
for j in range(1001):
 delta=F(j,10**7)
 plus=(1-delta/22)/2;minus=(1+delta/22)/2
 ck(plus>0 and minus>0);ck(plus+minus==1);ck(plus-minus==-delta/22)
print(f'{checks} exact checks PASS')
