import numpy as np
from scipy.optimize import linprog
import json

def depths(lo, hi):
    lo=np.asarray(lo,dtype=float); hi=np.asarray(hi,dtype=float)
    n=len(lo); z=np.arange(n); w=hi-lo; M=w.sum()
    out=[]; marks=[]
    for p in z:
        others=z[z!=p]; den=others-p
        def bounds(x):
            slopes=np.r_[(lo[others]-x)/den,(hi[others]-x)/den]
            cuts=x+slopes[:,None]*(z-p)[None,:]
            sums=np.minimum(w[None,:],np.maximum(0,hi[None,:]-cuts)).sum(1)
            return sums.min(), M-sums.max()
        l,r=lo[p],hi[p]
        for _ in range(45):
            x=(l+r)/2; up,down=bounds(x)
            if up>down: l=x
            else: r=x
        x=(l+r)/2
        out.append(min(bounds(x)));marks.append(x)
    return np.array(out),np.array(marks)

def random_chain(rng,n):
    end=rng.integers(1,20,2)
    base=np.linspace(end[0],end[1],n)
    z=np.arange(n)
    low=base.copy();up=base.copy()
    for j in range(1,n-1):
        tent=np.minimum(z*(n-1-j),(n-1-z)*j)
        low+=(rng.integers(1,20) if rng.random()<0.15 else 0)*tent
        up+=(rng.integers(1,20) if rng.random()<0.15 else 0)*tent
    return -low,up

def main():
    rng=np.random.default_rng(7832)
    for it in range(1500):
        n=int(rng.integers(4,9));lo,hi=random_chain(rng,n)
        # Determine the exact deepest-source chamber numerically; generic
        # bodies usually have one source, so also equalize one roof parameter.
        Qs,ys=depths(lo,hi);M=sum(hi-lo);Q=max(Qs);beta=Q/M
        active=np.where(Qs>Q-1e-7)[0]
        eps=1e-4
        slopes=[]
        for p in [0,n-1]:
            L=lo.copy();H=hi.copy();L[p]+=eps/2;H[p]-=eps/2
            q,_=depths(L,H)
            slopes.append((q-Qs)/eps+beta)
        A=np.array(slopes).T[active]
        res=linprog([0,0,-1],A_ub=np.c_[A,np.ones(len(active))],b_ub=np.zeros(len(active)),A_eq=[[1,1,0]],b_eq=[1],bounds=[(0,None),(0,None),(None,None)],method='highs')
        if res.success and res.x[-1]<-1e-6:
            print(json.dumps(dict(iteration=it,lo=lo.tolist(),hi=hi.tolist(),depths=Qs.tolist(),marks=ys.tolist(),beta=beta,A=A.tolist(),margin=res.x[-1])))
            return
        if it%100==0: print('checked',it,flush=True)
    print('none')

def ties():
    rng=np.random.default_rng(7298)
    found=0
    for it in range(700):
        n=int(rng.integers(4,9)); l0,u0=random_chain(rng,n);l1,u1=random_chain(rng,n)
        q0,_=depths(l0,u0);q1,_=depths(l1,u1)
        p=int(q0.argmax());q=int(q1.argmax())
        if p==q:continue
        left,right=0.,1.
        for _ in range(38):
            t=(left+right)/2;lo=(1-t)*l0+t*l1;hi=(1-t)*u0+t*u1
            vals,_=depths(lo,hi)
            if vals[p]>=max(np.delete(vals,p)):left=t
            else:right=t
        t=(left+right)/2;lo=(1-t)*l0+t*l1;hi=(1-t)*u0+t*u1
        vals,ys=depths(lo,hi);M=sum(hi-lo);Q=max(vals);beta=Q/M
        eps=1e-3; slopes=[]
        for theta in np.linspace(0,1,41):
            L=lo.copy();H=hi.copy()
            L[0]+=eps*theta/2;H[0]-=eps*theta/2
            L[-1]+=eps*(1-theta)/2;H[-1]-=eps*(1-theta)/2
            vv,_=depths(L,H)
            slopes.append((max(vv)/(M-eps)-beta)/eps)
        found+=1
        if min(slopes)>1e-8:
            print(json.dumps(dict(kind='tie',iteration=it,l0=l0.tolist(),u0=u0.tolist(),l1=l1.tolist(),u1=u1.tolist(),t=t,lo=lo.tolist(),hi=hi.tolist(),depths=vals.tolist(),marks=ys.tolist(),beta=beta,slopes=slopes)),flush=True)
            return
        if found%20==0:print('ties checked',found,flush=True)
    print('no tie counter',found)

def symmetric():
    rng=np.random.default_rng(28729)
    for it in range(3000):
        n=int(rng.choice([4,6,8,10])); l,u=random_chain(rng,n)
        lo=(l-u[::-1])/2;hi=(u-l[::-1])/2
        vals,ys=depths(lo,hi);M=sum(hi-lo);Q=max(vals);beta=Q/M
        eps=1e-3; L=lo.copy();H=hi.copy()
        L[[0,-1]]+=eps/2;H[[0,-1]]-=eps/2
        vv,_=depths(L,H)
        derivative=(max(vv)/(M-2*eps)-beta)/eps
        if derivative>1e-8:
            slopes=[]
            for theta in np.linspace(0,1,41):
                L=lo.copy();H=hi.copy()
                L[0]+=eps*theta/2;H[0]-=eps*theta/2
                L[-1]+=eps*(1-theta)/2;H[-1]-=eps*(1-theta)/2
                v,_=depths(L,H)
                slopes.append((max(v)/(M-eps)-beta)/eps)
            print(json.dumps(dict(kind='symmetric',it=it,lo=lo.tolist(),hi=hi.tolist(),depths=vals.tolist(),marks=ys.tolist(),beta=beta,derivative=derivative,slopes=slopes)),flush=True)
            return
        if it%100==0:print('symmetric checked',it,flush=True)
    print('no symmetric counter')

if __name__=='__main__':symmetric()
