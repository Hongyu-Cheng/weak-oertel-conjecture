"""Falsification screen for necessary one-dimensional log-concave target bands.

Numerical results are not certificates. No OC conclusion is drawn here.
"""
import numpy as np
from scipy.spatial import ConvexHull
from itertools import combinations

rng=np.random.default_rng(96381)

def intervals(poly):
    out=[]
    for z in range(int(np.ceil(poly[:,0].min())),int(np.floor(poly[:,0].max()))+1):
        vals=[]
        for a,b in zip(poly,np.roll(poly,-1,axis=0)):
            if min(a[0],b[0])<=z<=max(a[0],b[0]):
                if a[0]==b[0]: vals.extend([a[1],b[1]])
                else: vals.append(a[1]+(z-a[0])*(b[1]-a[1])/(b[0]-a[0]))
        if vals and max(vals)>min(vals)+1e-8:
            out.append([z,min(vals),max(vals)])
    return np.array(out)

def bands(fib,k,grid):
    z,l,u=fib.T; widths=u-l; M=widths.sum(); delta=z-k
    idx=np.flatnonzero(delta)
    upper=[];lower=[]
    for t in grid:
        slopes=np.r_[(l[idx]-t)/delta[idx],(u[idx]-t)/delta[idx]]
        left=np.clip(t+slopes[:,None]*delta-l,0,widths).sum(axis=1)
        central=np.clip(t-l[delta==0][0],0,widths[delta==0][0])
        tails=[widths[delta<0].sum()+central,widths[delta>0].sum()+central]
        cap_min=min(left.min(),*tails)
        cap_max=max(left.max(),*tails)
        upper.append(min(1,2*cap_min/M))
        lower.append(max(0,1-2*(M-cap_max)/M))
    return np.array(lower),np.array(upper)

def violation(grid,lo,hi):
    # If log F is concave, its value at j is bounded below by the chord
    # through any prescribed lower bounds at i,k. Also apply to 1-F.
    best=(0,None)
    for a,b in [(lo,hi),(1-hi[::-1],1-lo[::-1])]:
        for i in range(len(grid)-2):
            if a[i]<=0: continue
            for k in range(i+2,len(grid)):
                if a[k]<=0: continue
                js=np.arange(i+1,k)
                q=(grid[k]-grid[js])/(grid[k]-grid[i])
                required=np.exp(q*np.log(a[i])+(1-q)*np.log(a[k]))
                dif=required-b[js]
                j=int(np.argmax(dif))
                if dif[j]>best[0]:best=(float(dif[j]),(i,int(js[j]),k))
    return best

if __name__=='__main__':
    best=0
    for it in range(1200):
        raw=rng.integers([-5,-9],[6,10],size=(rng.integers(4,12),2)).astype(float)
        try: poly=raw[ConvexHull(raw).vertices]
        except Exception: continue
        fib=intervals(poly)
        if len(fib)<2:continue
        z,l,u=fib.T; w=u-l; M=w.sum()
        meds=[int(j) for j in range(len(z)) if w[z<z[j]].sum()<=M/2+1e-10 and w[z>z[j]].sum()<=M/2+1e-10]
        checks=[]
        for j in meds:
            grid=np.linspace(l[j],u[j],31)
            lo,hi=bands(fib,z[j],grid)
            gap,indices=violation(grid,lo,hi)
            checks.append((gap,z[j],indices))
        if checks and min(c[0] for c in checks)>1e-7:
            print('CANDIDATE',it,poly.tolist(),checks,flush=True)
            break
        if it%100==0:print('screened',it,flush=True)
    else:print('No necessary-CDF-condition violation found; this is not a proof.',flush=True)
