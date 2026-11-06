exec(open('./cap_multiplicity_search.py').read().split('for it in range')[0])
best=(-9,None)
for it in range(500000):
 P=hull([(r.randrange(-100,101),r.randrange(-100,101)) for _ in range(r.randrange(3,9))])
 if len(P)<3:continue
 M=area(P); caps=[area(clip(P,*v))/M for v in norms]
 if max(caps)>.5 or min(caps)<.3:continue
 Es=[]
 for i in range(3):
  Q=P
  for j,(a,b) in enumerate(norms):Q=clip(Q,a if i==j else -a,b if i==j else -b)
  Es.append(area(Q)/M)
 gap=sum(Es)-1.5*max(caps)
 if gap>best[0]:best=(gap,(P,caps,Es));print('BEST',it,best,flush=True)
 if gap>1e-6:print('COUNTER',best,flush=True);break
else:print('FINISHED',best)
