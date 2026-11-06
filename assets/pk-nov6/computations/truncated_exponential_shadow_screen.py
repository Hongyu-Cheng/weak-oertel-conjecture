import random,json,numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog,minimize_scalar
src=open('./logconcave_shadow_increment_screen.py').read().split('random.seed(351082)')[0]
exec(src)
N=61;v=np.linspace(0,1,N)
thetas=[0,-1,1,-2,2,-5,5,-10,10,-20,20,-50,50,-.1,.1,-.5,.5,-3,3,-7,7,-15,15,-30,30]
def basis(theta):
    if theta==0:return v
    if theta>0:return (np.exp(theta*(v-1))-np.exp(-theta))/(1-np.exp(-theta))
    return (1-np.exp(theta*v))/(1-np.exp(theta))
EE=[basis(t) for t in thetas]
random.seed(851793)
for iteration in range(5000):
    pts=list(set((random.randint(0,random.choice([3,5,9,15])),random.randint(-20,20)) for _ in range(random.randint(4,20))))
    if len(pts)<3:continue
    try:poly=[pts[i] for i in ConvexHull(pts).vertices]
    except:continue
    f=fibers(poly);M=sum(u-l for l,u in f.values())
    if M<=0:continue
    med=[k for k in f if sum(u-l for j,(l,u) in f.items() if j<k)<=M/2+1e-9
         and sum(u-l for j,(l,u) in f.items() if j>k)<=M/2+1e-9]
    allbad=[]
    for k in med:
        t,A,B=bands(f,k,N)
        iu=np.flatnonzero(B<1-1e-8);il=np.flatnonzero(A>1e-8)
        found=False
        for theta,E in zip(thetas,EE):
            AA=np.array([[0,1],[-1,-1]]+[[E[i],1] for i in iu]+[[-E[i],-1] for i in il])
            bb=np.concatenate([[0,-1],B[iu],-A[il]])
            op=linprog([0,0],A_ub=AA,b_ub=bb,bounds=[(None,None),(None,None)],method='highs')
            if op.success:found=True;break
        if not found:
            def slack(theta):
                E=basis(theta)
                AA=np.array([[0,1,1],[-1,-1,1]]+[[E[i],1,1] for i in iu]+[[-E[i],-1,1] for i in il])
                bb=np.concatenate([[0,-1],B[iu],-A[il]])
                op=linprog([0,0,-1],A_ub=AA,b_ub=bb,bounds=[(None,None)]*3,method='highs')
                return op.x[2]
            fine=np.linspace(-12,12,49)
            scores=[slack(x) for x in fine]
            j=int(np.argmax(scores))
            op=minimize_scalar(lambda x:-slack(x),bounds=(fine[max(0,j-1)],fine[min(len(fine)-1,j+1)]),method='bounded')
            found=-op.fun>=0
        if found:break
        allbad.append(k)
    else:
        out={'polygon':poly,'fibers':f,'median_fibers':allbad}
        print(json.dumps(out,indent=2),flush=True)
        with open('./truncated_exponential_shadow_candidate.json','w') as ff:json.dump(out,ff,indent=2)
        break
    if iteration%500==0:print('tested',iteration,flush=True)
