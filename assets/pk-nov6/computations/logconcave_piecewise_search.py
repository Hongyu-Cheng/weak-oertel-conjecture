import numpy as np, json
from scipy.optimize import linprog

rng=np.random.default_rng(312758)
N=85
points=np.array([(i/N,j/N) for i in range(N+1) for j in range(N+1-i)],float)
angles=np.linspace(0,2*np.pi,96,endpoint=False)
normals=np.stack([np.cos(angles),np.sin(angles)],axis=1)
projections=points@normals.T
order=np.argsort(projections,axis=0)
proj_sort=np.take_along_axis(projections,order,axis=0)
def check(weights):
    cw=np.cumsum(weights[order],axis=0)
    ix=np.argmax(cw>=cw[-1]*4/9,axis=0)
    qq=proj_sort[ix,np.arange(len(angles))]
    opt=linprog([0,0],A_ub=-normals,b_ub=-qq,bounds=[(None,None),(None,None)],method='highs')
    return opt.success,qq

for iteration in range(5000):
    if iteration%2==0:
        # Convex piecewise-affine potential, hence log-concave density.
        coeff=rng.normal(size=(rng.integers(2,7),3))*rng.choice([.2,1,3,10])
        val=np.max(points@coeff[:,:2].T+coeff[:,2],axis=1)
        weights=np.exp(-(val-val.min()))
        kind='piecewise_exponential'
    else:
        # Product of positive affine factors is log-concave.
        verts=np.exp(rng.uniform(-3,3,size=(rng.integers(1,5),3)))
        bary=np.column_stack([1-points.sum(axis=1),points])
        coeff=verts
        weights=np.prod(bary@verts.T,axis=1)
        kind='polynomial'
    good,qq=check(weights)
    if not good:
        out={'iteration':iteration,'kind':kind,'coeff':coeff.tolist(),'quantiles':qq.tolist()}
        print(json.dumps(out),flush=True)
        with open('./logconcave_piecewise_candidate.json','w') as f:json.dump(out,f,indent=2)
        break
    if iteration%500==0:print('tested',iteration,flush=True)
