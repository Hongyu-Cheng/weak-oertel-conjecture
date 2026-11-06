from random import Random
r=Random(82731)
def dep(D,k,x):
 total=sum(u-l for l,u in D)
 best=min(sum(D[j][1]-D[j][0] for j in range(k))+x-D[k][0],sum(D[j][1]-D[j][0] for j in range(k))+D[k][1]-x,sum(D[j][1]-D[j][0] for j in range(k+1,len(D)))+x-D[k][0],sum(D[j][1]-D[j][0] for j in range(k+1,len(D)))+D[k][1]-x)
 for i,(l,u) in enumerate(D):
  if i==k:continue
  for e in (l,u):
   a=(e-x)/(i-k)
   above=sum(max(0,min(hi-lo,hi-x-a*(j-k))) for j,(lo,hi) in enumerate(D))
   best=min(best,above,total-above)
 return best/total
def opt(D):
 best=(0,None,None)
 for k,(l,u) in enumerate(D):
  left,right=l,u
  for it in range(45):
   x=left+(right-left)/3; y=right-(right-left)/3
   if dep(D,k,x)<dep(D,k,y):left=x
   else:right=y
  x=(left+right)/2; best=max(best,(dep(D,k,x),k,x))
 return best
def body(L,A):
 low=[0.,0.]
 for i,a in enumerate(A,1):
  curv=2*L[i]-L[i-1]-L[i+1]
  low.append(2*low[-1]-low[-2]+a*curv)
 return [(l,l+w) for l,w in zip(low,L)]
for it in range(2000):
 N=r.randrange(4,7)
 # Generate concave positive length profiles by slopes with nonnegative curvature.
 slopes=sorted([r.randrange(-20,21) for j in range(N-1)],reverse=True)
 L=[0]
 for s in slopes:L.append(L[-1]+s)
 off=1-min(L);L=[x+off for x in L]
 A=[r.choice([0.,.25,.5,.75,1.]) for j in range(N-2)]
 index=r.randrange(N-2)
 bodies=[];vals=[]
 for t in [0.,.5,1.]:
  AA=A.copy();AA[index]=t
  D=body(L,AA);bodies.append(D);vals.append(opt(D))
 if vals[1][0]+.002<min(vals[0][0],vals[2][0]):
  print('QUASICONCAVITY FAIL',it,'L',L,'A',A,'index',index,'vals',vals,'bodies',bodies,flush=True)
  break
 if it%100==0:print('progress',it,flush=True)
