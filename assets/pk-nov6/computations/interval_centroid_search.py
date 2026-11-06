from fractions import Fraction as F
from random import Random
from itertools import combinations
r=Random(99382)
def hull(P):
 P=sorted(set(P))
 def cr(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
 L=[]
 for p in P:
  while len(L)>=2 and cr(L[-2],L[-1],p)<=0:L.pop()
  L.append(p)
 U=[]
 for p in P[::-1]:
  while len(U)>=2 and cr(U[-2],U[-1],p)<=0:U.pop()
  U.append(p)
 return L[:-1]+U[:-1]
def fibers(P):
 D={}
 for k in range(min(x for x,y in P),max(x for x,y in P)+1):
  ys=[]
  for (a,b),(c,d) in zip(P,P[1:]+P[:1]):
   if min(a,c)<=k<=max(a,c):
    if a==c:ys.extend([F(b),F(d)])
    else:ys.append(F(b)+F(k-a,c-a)*(d-b))
  D[k]=(min(ys),max(ys))
 return D
def depth(D,k):
 l,u=D[k];m=(l+u)/2
 slopes=set(F(e-m,j-k) for j,B in D.items() if j!=k for e in B)
 tot=sum(u-l for l,u in D.values())
 if not tot:return F(0),None
 best=min(sum(u-l for j,(l,u) in D.items() if j<k)+(D[k][1]-D[k][0])/2,sum(u-l for j,(l,u) in D.items() if j>k)+(D[k][1]-D[k][0])/2)
 arg=None
 for a in slopes:
  above=sum(max(F(0),min(u-l,u-m-a*(j-k))) for j,(l,u) in D.items())
  cur=min(above,tot-above)
  if cur<best:best=cur;arg=a
 return best/tot,arg
if __name__=='__main__':
 worst=F(1)
 for it in range(5000):
  P=hull([(r.randrange(-7,8),r.randrange(-15,16)) for z in range(r.randrange(4,12))])
  if len(P)<3:continue
  D=fibers(P); total=sum(u-l for l,u in D.values()); cum=F(0)
  if not total:continue
  mids=[]
  for k,(l,u) in D.items():
   if cum<=total/2<=cum+u-l:mids.append(k)
   cum+=u-l
  vals=[(depth(D,k)[0],k) for k in mids]
  v,k=max(vals)
  if v<worst:
   worst=v
   print('worst median',it,float(v),v,'k',k,'poly',P,flush=True)
  if v<F(1,4):
   print('MEDIAN FAIL',D,vals,flush=True)
   allv=[(depth(D,k)[0],k) for k in D]
   print('ALL',allv,flush=True)
   if max(allv)[0]<F(1,4):break
