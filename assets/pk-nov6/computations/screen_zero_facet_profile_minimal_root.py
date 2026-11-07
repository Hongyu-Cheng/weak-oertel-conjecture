exec(open('./screen_facet_capacity_overlap_mixed_area_root.py').read().split('rng=np.random')[0])
from scipy.optimize import linprog
rng=np.random.default_rng(161803)
count=0
for j in range(20000):
    v=rng.normal(size=(rng.integers(3,11),2))
    try:p=v[ConvexHull(v).vertices]
    except Exception:continue
    th=rng.uniform(0,np.pi);R=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
    p=(p*np.exp(rng.uniform(-2,2,size=2)))@R.T+rng.normal(size=2)*rng.uniform(0,2)
    vals=p@U.T
    if not np.all((vals.min(0)<-1)&(vals.max(0)>-1)):continue
    ss=np.array([section(p,u,-1) for u in U])
    if np.max(ss)>3+1e-8:continue
    a=area(p);b=4.5;S=sum(vals.max(0));m=(a+b+3*S)/4
    caps=np.array([area(clip(p,u,-1)) for u in U]);cs=np.sort(caps);F=cs[0]+cs[1]+cs[2]/4
    extr=(caps+3*(vals.max(0)+1))/4
    r=[]
    for u in U:
        ar=clip(p,-u,1);r.append((area(ar)+b+3*sum((ar@U.T).max(0)))/4)
    # variables k,Q, epsilon positive margin below target
    AA=[];bb=[]
    def le(row, rhs):AA.append(row);bb.append(rhs)
    le([-1,0,0],-m);le([-1,0,0],-abs(a-b));le([1,0,0],a+b)
    for v in [a,b]:le([0,-1,0],-(4/9)*v)
    le([4/9,-1,0],0)
    for v in caps:le([0,-1,0],-v)
    # no residual bound
    le([1,-9/4,0],-F);le([-2/9,1,1],(2/9)*(a+b))
    sol=linprog([0,0,-1],A_ub=AA,b_ub=bb,bounds=[(0,None),(0,None),(0,None)],method='highs')
    count+=1
    if sol.success and sol.x[2]>1e-7:
        print('FEASIBLE',j,'a',a,'U',caps,'S',S,'sections',ss,'kQeps',sol.x,'p',p.tolist(),flush=True);break
else:print('no feasible')
print('candidate A tested',count)
