import numpy as np,json
from logconcave_exact_polygon_search import evaluate
rng=np.random.default_rng(31219)
best=1
for i in range(1000):
    coeff=rng.normal(size=(rng.integers(2,5),3))*rng.choice([.1,.3,1.,3.,10.])
    # Ensure multiple potential facets remain relevant.
    if i%2:
        coeff[:,2]=-np.sum(coeff[:,:2],axis=1)/3+rng.uniform(-.2,.2,size=len(coeff))
    try:opt,nn,qq,cc,M=evaluate(coeff,angles=64)
    except Exception:continue
    slack=opt.x[2]
    if slack<best:
        best=slack
        print('best',i,best,coeff.tolist(),flush=True)
    if slack< -1e-6:
        out={'coeff':coeff.tolist(),'slack':float(slack),'point':opt.x.tolist()}
        with open('./logconcave_exact_counterexample_candidate.json','w') as f:json.dump(out,f,indent=2)
        break
