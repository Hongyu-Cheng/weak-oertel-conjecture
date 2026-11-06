import math,random,json
rng=random.Random(748924)
def logder(d,q):
 terms=[math.log1p(-j/q) for j in range(math.ceil(q))]
 sp=sum(math.exp((d-1)*t) for t in terms)
 sd=sum(math.exp(d*t) for t in terms)
 return -math.log(q)/(d+1)+math.log(sp)-d/(d+1)*math.log(sd)
best=-1e100;info=None
for it in range(150000):
 d=rng.randint(2,300)
 q=math.exp(rng.uniform(-9,6))
 if it%3==0:q=rng.randint(0,100)+rng.random()
 delta=logder(d,q+1)-logder(d,q)
 if delta>best:best=delta;info={'d':d,'q':q,'delta':delta}
 if delta>1e-10:
  print('COUNTER',json.dumps(info),flush=True);break
else:print('FINISHED',json.dumps(info),flush=True)
