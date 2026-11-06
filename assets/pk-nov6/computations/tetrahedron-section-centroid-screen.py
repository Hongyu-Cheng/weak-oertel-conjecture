from fractions import Fraction as F
from itertools import combinations
import random

def cap(t):
 # Distinct vertex values, with none zero.
 v=F(0);grad=[F(0)]*4
 for i in range(4):
  if t[i]<=0:continue
  den=F(1)
  for j in range(4):
   if j!=i:den*=t[i]-t[j]
  val=t[i]**3/den;v+=val
  grad[i]+=3*t[i]**2/den-val*sum((1/(t[i]-t[j]) for j in range(4) if j!=i),F(0))
  for k in range(4):
   if k!=i:grad[k]+=val/(t[i]-t[k])
 s=sum(grad);l=[x/s for x in grad]
 assert 0<v<1 and s>0 and all(x>0 for x in l) and sum(l)==1
 assert sum(t[i]*l[i] for i in range(4))==0
 q=[s*(t[i]-t[0]) for i in range(1,4)]
 return v,s,l,q

def solve(rows,rhs,tol=0):
 mat=[list(row)+[b] for row,b in zip(rows,rhs)];nr=len(rows);nc=len(rows[0]);piv=[];k=0
 for j in range(nc):
  i=max(range(k,nr),key=lambda i:abs(mat[i][j]),default=None)
  if i is None or abs(mat[i][j])<=tol:continue
  mat[k],mat[i]=mat[i],mat[k];a=mat[k][j];mat[k]=[x/a for x in mat[k]]
  for i in range(nr):
   if i!=k:
    a=mat[i][j]
    if a:mat[i]=[x-a*y for x,y in zip(mat[i],mat[k])]
  piv.append(j);k+=1
  if k==nr:break
 if k<nc:return None
 if any(abs(row[-1])>tol for row in mat[k:]):return None
 out=[0]*nc
 for i,j in enumerate(piv):out[j]=mat[i][-1]
 return out

def data(t):
 v,s,l,q=cap(t);caps=[('Q',v,q),('-Q',1-v,[-x for x in q])]
 for i in range(4):
  if any(l[j]>F(1,3) for j in range(4) if j!=i):continue
  fi=F(27)
  for j in range(4):
   if j!=i:fi*=l[j]
  ti=[F(3) if j==i else 3-1/l[j] for j in range(4)]
  qi=[fi*(ti[j]-ti[0]) for j in range(1,4)]
  caps.extend([(f'V{i}',fi,qi),(f'-V{i}',1-fi,[-x for x in qi])])
 return l,caps

def run(t):
 l,caps=data(t);best=1.;bestinds=None
 for k in range(2,5):
  for inds in combinations(range(len(caps)),k):
   rows=[[float(caps[j][2][i]) for j in inds] for i in range(3)]+[[1.]*k]
   th=solve(rows,[0.,0.,0.,1.],1e-8)
   if th is None or min(th)<-1e-8:continue
   val=sum(th[i]*float(caps[j][1]) for i,j in enumerate(inds))
   if val<best:best=val;bestinds=inds
 if best<F(27,64)-1e-8:
  inds=bestinds;rows=[[caps[j][2][i] for j in inds] for i in range(3)]+[[F(1)]*len(inds)]
  th=solve(rows,[F(0),F(0),F(0),F(1)])
  assert th is not None and min(th)>=0
  val=sum(th[i]*caps[j][1] for i,j in enumerate(inds))
  if val<F(27,64):
   print('EXACT COUNTER',t,'lambda',l,'caps',[caps[j] for j in inds],'weights',th,'mean',val,flush=True);raise SystemExit
 return best
if __name__=='__main__':
 random.seed(541873);best=1
 for it in range(1200):
  a,b=random.sample(range(1,16),2);c,d=random.sample(range(1,16),2)
  t=list(map(F,[a,b,-c,-d]));cur=run(t);best=min(best,cur)
  if it%100==0:print('screen',it,'best',best,flush=True)
 print('no counter; screened best',best,flush=True)
