import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, hstack, eye
import sys
n=int(sys.argv[1]) if len(sys.argv)>1 else 80
Mn=int(sys.argv[2]) if len(sys.argv)>2 else 272
Md=100
p=(2*np.arange(1,n+1)-1)/n**2
rhs=np.concatenate((p,2*p))
triples=[]; seen=set()
def matrix():
    rr=[]; cc=[]; dd=[]
    for col,(i,j,k) in enumerate(triples):
        rr.extend((i,n+j,n+k));cc.extend((col,col,col));dd.extend((1,1,1))
    return coo_matrix((dd,(rr,cc)),shape=(2*n,len(triples))).tocsr()
for it in range(300):
    mat=matrix()
    res=linprog(np.concatenate((np.zeros(len(triples)),np.ones(2*n))),
                A_eq=hstack((mat,eye(2*n)),format='csr'),b_eq=rhs,
                bounds=(0,None),method='highs')
    if not res.success: raise RuntimeError(res.message)
    if it%5==0: print(n,Mn,it,len(triples),res.fun,flush=True)
    if res.fun<1e-9:
        vals=res.x[:len(triples)]; pos=vals>1e-10
        np.savez('./beta_weighted_coupling_column_root.npz',n=n,Mn=Mn,Md=Md,
                 triples=np.array(triples)[pos],mass=vals[pos])
        print('FEASIBLE',sum(pos),flush=True);break
    ya=res.eqlin.marginals[:n]; yb=res.eqlin.marginals[n:]
    best=np.maximum.accumulate(yb)
    arg=np.empty(n,dtype=int);bi=0
    for k in range(n):
        if yb[k]>yb[bi]:bi=k
        arg[k]=bi
    candidates=[]
    for i in range(n):
        for j in range(n):
            cap=(Mn*n)//Md-2*(i+1)-(j+1)
            if cap<1:continue
            k=int(arg[min(n,cap)-1])
            jj,kk=sorted((j,k));key=(i,jj,kk)
            violation=ya[i]+yb[jj]+yb[kk]
            if violation>1e-8 and key not in seen:
                candidates.append((violation,key))
    candidates.sort(reverse=True)
    added=0
    for _,key in candidates:
        if key in seen:continue
        seen.add(key);triples.append(key);added+=1
        if added>=max(100,2*n):break
    if added==0:
        np.savez('./beta_weighted_coupling_dual_root.npz',n=n,Mn=Mn,Md=Md,
                 dual=res.eqlin.marginals,objective=res.fun)
        print('NO POSITIVE PRICING',res.fun,flush=True);break
else: print('ITERATION LIMIT',flush=True)
