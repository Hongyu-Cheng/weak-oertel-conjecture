import mpmath as mp
mp.mp.dps=60
def barrier(d,q):
 p=mp.mpf(1)/(d+1);a=(1+1/q)**d
 def h(f):return (f+a)**p+(f-1)**p-2*f**p
 lo=mp.mpf(1);hi=mp.mpf(2)
 while h(hi)<0:hi*=2
 for _ in range(150):
  mid=(lo+hi)/2
  if h(mid)<=0:lo=mid
  else:hi=mid
 return (lo+hi)/2*q**d
best=mp.inf;info=None
for d in range(2,31):
 for num in range(5,101,3):
  q=mp.mpf(num)/4
  b=barrier(d,q);bp=barrier(d,q+1)
  gap=(bp-b)/(q+1)**d-1
  if gap<best:best=gap;info=(d,str(q),str(gap))
  if gap<mp.mpf('-1e-35'):
   print('COUNTER',info,flush=True);raise SystemExit
 print('d',d,'best',info,flush=True)
