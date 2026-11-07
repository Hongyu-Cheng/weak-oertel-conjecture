from fractions import Fraction as F
from math import comb
from itertools import permutations
checks=0
def ck(p,msg):
 global checks
 assert p,msg
 checks+=1
def rho(d):
 return sum(((-1)**j)*comb(d+1,j)*max(F(0),1-F(2*j,d+1))**d for j in range(d+2))
expected=[F(1),F(2,3),F(1,2),F(46,125),F(22,81),F(3364,16807),F(151,1024)]
for d,r in enumerate(expected,1):ck(rho(d)==r,'exact simplex intersection ratio')
for d in range(5,8):ck(rho(d)<F(1,3),'finite low-index intersection bound')
ck(3*7**9<8**9,'all remaining dimensions via the proved product bound')
ck(F(81,376)-F(27,128)==F(27,6016),'exact dimension-three target margin')
ck(F(81,376)/F(27,128)==F(48,47),'dimension-three multiplicative margin')
ck(2-(1+F(46,125)+F(4,3)*F(256,625))==F(161,1875),'dimension-four denominator margin')
ck(1/((1+F(46,125))/F(256,625)+F(4,3))==F(768,3589),'dimension-four exact conclusion')
for d in range(2,21):
 g=F(d,d+1)**d;kap=1/g-2;m=d+1
 ck(0<=kap<1,'top-three profile coefficient range')
 for shift in [0,1,3]:
  for power in [1,2,3]:
   U=[F((j+shift)**power,3) for j in range(1,m+1)]
   excess=U[-1]+U[-2]+kap*U[-3]-U[0]-U[1]-kap*U[2]
   if d==2:
    ck(excess==(1-kap)*(U[-1]-U[0]),'three-cap cancellation')
    bound=(1-kap)*U[-1]
   elif d==3:
    ck(excess==U[3]-U[0]+(1-kap)*(U[2]-U[1]),'four-cap cancellation')
    bound=(2-kap)*U[-1]
   elif d==4:
    ck(excess==U[4]+U[3]-U[0]-U[1],'five-cap exact common-term cancellation')
    bound=2*U[-1]
   else:bound=U[-1]/g
   ck(excess<=bound,'sorted profile correction upper bound')
# Exact determinants of permutation actions on sum-zero barycentric space.
def det(A):
 A=[[F(v) for v in row] for row in A];out=F(1)
 for j in range(len(A)):
  p=next(i for i in range(j,len(A)) if A[i][j])
  if p!=j:A[p],A[j]=A[j],A[p];out=-out
  pivot=A[j][j];out*=pivot
  for i in range(j+1,len(A)):
   ratio=A[i][j]/pivot
   for k in range(j+1,len(A)):A[i][k]-=ratio*A[j][k]
 return out
for d in range(1,6):
 B=[[int(i==j)-int(i==d) for j in range(d)] for i in range(d+1)]
 for pi in permutations(range(d+1)):
  ck(abs(det([B[pi[i]] for i in range(d)]))==1,'finite group action determinant')
print(f'{checks} exact rational checks passed.')
