import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, csr_matrix
from scipy.spatial import ConvexHull
import json, random
random.seed(9938)

def setup(bot,top,k,nq=10):
    lens=np.array(top)-np.array(bot); M=lens.sum(); L=lens[:k].sum()/M; R=lens[k+1:].sum()/M
    X=[];Y=[];aw=[];bw=[]
    for z in range(len(lens)):
        pts=bot[z]+lens[z]*(np.arange(nq)+.5)/nq
        if z<k: coeff=2*lens[z]/M
        elif z==k: coeff=1-2*L
        else: coeff=0
        if coeff>1e-12:
            X.extend((z,x) for x in pts);aw.extend([coeff/nq]*nq)
        if z>k: coeff=2*lens[z]/M
        elif z==k: coeff=1-2*R
        else: coeff=0
        if coeff>1e-12:
            Y.extend((z,x) for x in pts);bw.extend([coeff/nq]*nq)
    nx=len(X);ny=len(Y);T=np.empty((nx,ny))
    for i,(zi,x) in enumerate(X):
        for j,(zj,y) in enumerate(Y):
            T[i,j]=((zj-k)*x+(k-zi)*y)/(zj-zi) if zi!=zj else (x+y)/2
    A=lil_matrix((nx+ny,nx*ny+1))
    for i in range(nx):A[i,i*ny:(i+1)*ny]=1
    for j in range(ny):A[nx+j,j:nx*ny:ny]=1
    obj=np.zeros(nx*ny+1);obj[-1]=-1
    return T.ravel(),csr_matrix(A),np.r_[aw,bw],obj

def vals(bot,top,k,ys,nq=10):
    T,A,b,c=setup(bot,top,k,nq)
    ans=[]
    for y in ys:
        Aup=np.vstack([np.r_[-(T<=y+1e-10).astype(float),1],np.r_[-(T>=y-1e-10).astype(float),1]])
        res=linprog(c,A_ub=csr_matrix(Aup),b_ub=[0,0],A_eq=A,b_eq=b,bounds=(0,None),method='highs')
        assert res.success,res.message
        ans.append(-res.fun)
    return np.array(ans)

best=(0,None)
for it in range(200):
    N=random.randrange(2,8)
    zz=np.arange(N+1)
    lower=np.zeros(N+1);upper=np.ones(N+1)*random.uniform(.8,3)
    for j in range(1,N):
        s=random.uniform(0,.4)
        lower+=s*np.maximum(0,zz-j)
        upper-=random.uniform(0,.4)*np.maximum(0,zz-j)
    upper+=np.linspace(0,max(0,lower[-1]-upper[-1]+random.uniform(.2,2)),N+1)
    if min(upper-lower)<=0:continue
    weights=upper-lower; k=int(np.searchsorted(np.cumsum(weights),weights.sum()/2))
    if k in (0,N):continue
    ys=np.linspace(lower[k],upper[k],17)
    vv=vals(lower,upper,k,ys)
    for i in range(1,len(ys)-1):
        gap=(vv[i-1]+vv[i+1])/2-vv[i]
        if gap>best[0]+1e-6:
            best=(float(gap),dict(lower=lower.tolist(),upper=upper.tolist(),k=k,ys=ys.tolist(),values=vv.tolist(),i=i))
            print(it,json.dumps(best),flush=True)
print('FINAL',json.dumps(best))
