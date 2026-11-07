"""Numerical falsification only for 3 T_h + (2h+1) max(w) >= sum(w).

For each finite support/anchor and h, normalize sum(w)=1 and minimize
3 T_h+(2h+1)m, with m>=w_i, concavity, nonnegativity, and zero first
moment. Zero widths are allowed, a stronger closure test.
"""
import json, sys
import numpy as np
from scipy.optimize import linprog

def solve(L,R,h):
    z=np.arange(-L,R+1,dtype=float); N=len(z)
    rows=[]
    for i in range(1,N-1):
        row=np.zeros(N+1); row[i-1:i+2]=[1,-2,1]; rows.append(row)
    for i in range(N):
        row=np.zeros(N+1);row[i]=1;row[-1]=-1;rows.append(row)
    c=np.zeros(N+1);c[:-1]=3*(z>h);c[-1]=2*h+1
    eq=np.zeros((2,N+1));eq[0,:-1]=1;eq[1,:-1]=z
    res=linprog(c,A_ub=np.array(rows),b_ub=np.zeros(len(rows)),
        A_eq=eq,b_eq=[1,0],bounds=[(0,None)]*(N+1),method='highs')
    if not res.success:return None
    return dict(L=L,R=R,h=h,value=res.fun,w=res.x[:-1].tolist(),
        m=res.x[-1],dual_eq=res.eqlin.marginals.tolist(),
        dual_ub=res.ineqlin.marginals.tolist())

if __name__=='__main__':
    bound=int(sys.argv[1]) if len(sys.argv)>1 else 12
    best=10;count=0
    for L in range(1,bound+1):
        for R in range(1,bound+1):
            for h in range(min(L,R)+1):
                a=solve(L,R,h)
                if a is None:continue
                count+=1
                if a['value']<best-1e-10:
                    best=a['value'];print(json.dumps(a),flush=True)
                if a['value']<1-1e-8:
                    print('COUNTEREXAMPLE_CANDIDATE',flush=True);sys.exit()
    print(json.dumps(dict(count=count,best=best,bound=bound)),flush=True)
