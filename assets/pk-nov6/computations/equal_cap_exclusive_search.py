exec(open('./cap_multiplicity_search.py').read().split('for it in range')[0])
def quantile(P,a,b,tau):
 M=area(P);vals=[a*x+b*y for x,y in P];lo,hi=min(vals),max(vals)
 for j in range(44):
  mid=(lo+hi)/2
  if area(clip(P,a,b,mid))/M>tau:lo=mid
  else:hi=mid
 return (lo+hi)/2
best=(-1,None)
for it in range(30000):
 P=hull([(r.randrange(-100,101),r.randrange(-100,101)) for _ in range(r.randrange(3,9))])
 if len(P)<3:continue
 tau=r.choice([.445,.45,.455,.46,.47,.475,.48,.49,.495,.499])
 bs=[quantile(P,a,b,tau) for a,b in norms]
 if sum(bs)>=-1e-7:continue
 M=area(P);Es=[]
 for i in range(3):
  Q=P
  for j,(a,b) in enumerate(norms):Q=clip(Q,a if i==j else -a,b if i==j else -b,bs[j] if i==j else -bs[j])
  Es.append(area(Q)/M)
 gap=sum(Es)-1.5*tau
 if gap>best[0]:
  best=(gap,(P,tau,bs,Es));print('BEST',it,best,flush=True)
 if min(Es)>1e-8 and gap>1e-6:
  print('COUNTEREXAMPLE',best,flush=True);break
else:print('FINISHED',best)
