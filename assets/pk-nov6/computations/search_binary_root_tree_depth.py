"""Bounded falsification screen. Any output witness needs exact independent verification."""
from itertools import product
import numpy as np, random, time, json
random.seed(9187)
def bc(x): return bin(x).count("1")
J=4;L=3;e=np.eye(J,dtype=np.int64)
K=set(map(tuple,e))
for j in range(J):
 for word in product(range(J),repeat=L):
  K.add(tuple(2**L*e[j]-sum((2**b*e[c] for b,c in enumerate(word)),np.zeros(J,dtype=np.int64))))
K=np.array(sorted(K),dtype=np.int64);N=len(K);P=K[:,1:];lookup={tuple(k):i for i,k in enumerate(K)}
par=[];anc=[]
for k in K:
 c=np.where(k%2)[0];assert len(c)==1
 par.append(lookup[tuple((k+e[c[0]])//2)])
for i in range(N):
 bits=0;j=i
 while not(bits>>j&1):bits|=1<<j;j=par[j]
 anc.append(bits)
rootbits=sum(1<<lookup[tuple(r)] for r in e)
U=np.array([q for q in product(range(-6,7),repeat=3) if q!=(0,0,0)],dtype=np.int64)
# Add a fixed reproducible random family, only as a search accelerator.
U=np.vstack([U,np.random.default_rng(87).integers(-10000,10001,size=(3000,3))])
V=P@U.T
caps=[]
for i in range(N):
 cap=set()
 for j in range(len(U)):
  inds=np.where(V[:,j]>=V[i,j])[0]
  cap.add(sum(1<<int(t) for t in inds))
 caps.append(sorted(cap,key=bc))
print('universe',N,'caps',sum(map(len,caps)),flush=True)
order=sorted(range(N),key=lambda i:(np.max(K[i]),tuple(K[i])))
start=time.time();tries=0;best=1
while time.time()-start<100:
 density=random.random()**2*.7
 mask=rootbits
 for i in range(N):
  if random.random()<density:mask|=anc[i]
 count=bc(mask);target=(count-1)//4
 if target<1:continue
 cert=[];ok=True
 for i in order:
  if not(mask>>i&1):continue
  good=None
  for c in caps[i]:
   v=bc(mask&c)
   if v<=target:good=(c,v);break
  if good is None:ok=False;break
  cert.append((i,*good))
 tries+=1
 if ok:
  out={'K':K.tolist(),'mask':mask,'cert':cert,'N':count,'target':target}
  open('./binary_root_tree_depth_search_witness.json','w').write(json.dumps(out))
  print('FOUND',count,target,tries,flush=True);break
else:print('no witness',tries,flush=True)
