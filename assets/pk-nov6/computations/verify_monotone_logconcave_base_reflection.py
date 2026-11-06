from fractions import Fraction as F
from itertools import product

def audit(w):
    N=len(w)-1;M=sum(w)
    assert all(x>0 for x in w)
    assert all(w[i]>=w[i+1] for i in range(N))
    assert all(w[i]**2>=w[i-1]*w[i+1] for i in range(1,N))
    S=[sum(w[i:]) for i in range(N+1)]+[F(0)]*(N+3)
    R=[sum(min(w[i],w[2*j-i]) for i in range(N+1) if 0<=2*j-i<=N) for j in range(N+1)]
    for j in range(N+1):
        assert R[j]==S[j]+S[j+1]-2*S[2*j+1]
    for i in range(N+1):
        for k in range(N+1):assert S[i+k]*M<=S[i]*S[k]
    j=max(i for i in range(N+1) if S[i]>=M/2)
    a,b,c=S[j]/M,S[j+1]/M,S[2*j+1]/M
    assert R[j]/M-F(1,2)==(a-F(1,2))*(1-2*b)+2*(a*b-c)
    assert R[j]>=M/2
    if N>=2:assert max(R)>M/2
    return j,R[j],M

profiles=[]
for N in range(0,13):
 for q in [F(1),F(1,2),F(2,3),F(3,4),F(4,5),F(9,10)]:
  profiles.append([q**i for i in range(N+1)])
 for d in [1,2,3,5]:
  profiles.append([F(N+2-i)**d for i in range(N+1)])
for N in range(1,10):
 for denominator in [N+2,2*N+3]:
  w=[F(1)]
  for i in range(N):w.append(w[-1]*F(denominator-i-1,denominator))
  profiles.append(w)
for w in profiles:audit(w)
for fs in [profiles[11:13],profiles[21:24],[[F(1),F(1)]]*4]:
 results=[audit(w) for w in fs];j=tuple(r[0] for r in results)
 P=list(product(*[range(len(w)) for w in fs]))
 def weight(p):
  ans=F(1)
  for w,i in zip(fs,p):ans*=w[i]
  return ans
 R=F(0)
 for p in P:
  q=tuple(2*j[k]-p[k] for k in range(len(fs)))
  if all(0<=q[k]<len(fs[k]) for k in range(len(fs))):R+=min(weight(p),weight(q))
 prodR=F(1);M=F(1)
 for _,r,m in results:prodR*=r;M*=m
 assert R>=prodR>=M/F(2**len(fs))
print(f'PASS: {len(profiles)} exact finite monotone log-concave profiles, survival deficits, and tensorized box retention')
