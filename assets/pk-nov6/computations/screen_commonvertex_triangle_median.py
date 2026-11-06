exec(open('./screen_simplex_chain_positive_normal.py').read().split('best=None')[0])
best=(10,None)
for trial in range(160):
 N=random.randint(3,16)
 slopes=sorted([random.randrange(-50,51)/20 for _ in range(N-1)],reverse=True)
 raw=[0.]
 for s in slopes:raw.append(raw[-1]+s)
 rs=np.array(raw)+random.choice([.1,.3,1.,2.])-min(raw)
 weights=rs**2; M=sum(weights)
 med=[j for j in range(N) if sum(weights[:j])<=M/2+1e-8 and sum(weights[j+1:])<=M/2+1e-8]
 vals=[]
 for j in med:
  q=rs[j]/3
  B=max(max(q,abs(q-r))/abs(i-j) for i,r in enumerate(rs) if i!=j)
  opt=differential_evolution(lambda v:obj(v,rs,j),[(.5,1.),(-B,B)],tol=1e-8,popsize=12,seed=trial,polish=True)
  vals.append((opt.fun/M,j,opt.x.tolist()))
 ratio=max(x[0] for x in vals)
 if ratio<best[0]:
  best=(ratio,[rs.tolist(),vals]);print('best',trial,best,flush=True)
 if ratio<2/9-1e-6:break
print('done',best)
