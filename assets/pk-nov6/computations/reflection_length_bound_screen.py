import random
random.seed(1532)
best=1
for it in range(50000):
 n=random.randrange(2,80)
 a=random.randrange(1,50);d=random.randrange(-20,20);w=[a]
 for i in range(n-1):
  d-=random.randrange(0,6)
  w.append(w[-1]+d)
 add=1-min(w)
 if add>0:w=[x+add for x in w]
 vals=[]
 for j,b in enumerate(w):
  vals.append(b+2*sum(min(w[j-k],w[j+k],max(0,w[j-k]+w[j+k]-b)) for k in range(1,min(j,n-j-1)+1)))
 ratio=max(vals)/sum(w)
 if ratio<best:
  best=ratio
  if best<.55:print(it,n,ratio,w,vals,flush=True)
 if ratio<.5:
  print('LENGTH_BOUND_FAIL',flush=True);break
print('best',best)
