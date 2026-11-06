import mpmath as mp,random,json
mp.mp.dps=70
rng=random.Random(291771)
def scaled_sum(d,q):
 s=mp.mpf(0);j=0
 while j<q:
  t=mp.power(1-mp.mpf(j)/q,d);s+=t;j+=1
  if t<mp.mpf('1e-65') and j>20:break
 return s
best=mp.inf;info=None
for it in range(1500):
 d=rng.randint(201,30000)
 if it%3==0:
  m=rng.randint(1,8)
 else:m=int(mp.exp(rng.uniform(0,11)))
 rho=mp.mpf(rng.randint(1,999))/1000;q=m+rho;p=mp.mpf(1)/(d+1)
 # Common scaling by q^(d/(d+1)).
 vals=[]
 for t in [q-1,q,q+1]:
  vals.append(mp.exp((1-p)*mp.log(t/q)+p*mp.log(scaled_sum(d,t))))
 gap=2*vals[1]-vals[0]-vals[2]
 if gap<best:best=gap;info={'d':d,'q':str(q),'gap':str(gap)}
 if gap<mp.mpf('-1e-50'):
  print('CANDIDATE',json.dumps(info),flush=True);break
 if it%250==0:print('progress',it,'best',json.dumps(info),flush=True)
else:print('FINISHED',json.dumps(info),flush=True)
