# Falsification screen only: six actual radial endpoints with necessary area envelopes.
import numpy as np
from scipy.optimize import minimize
from pathlib import Path
import json
c=128/279

def env(a,b,r,t):
    D=r*a+t*b-a*b
    N=a*b*(a*t+b*r)-r*t*(a-b)**2
    return D,N

def cons(z):
    A,a,B,b,r,t=z[:6]
    X=z[6:9];Y=z[9:12]
    coreX=np.array([A*r,B*t,a*b])/2
    coreY=np.array([a*t,b*r,A*B])/2
    q=X+Y.sum()-Y
    out=list(X-coreX)+list(Y-coreY)+list(c-q)
    out.append(1-(q.sum()-.75*q.max()))
    # Six radial convexity inequalities.
    out += [r*(A+b)-A*b,t*(a+B)-a*B,A*(B+r)-B*r,a*(b+t)-b*t,B*(A+t)-A*t,b*(a+r)-a*r]
    # Envelope: if determinant<=0 the inequality has not been proved; use no bound.
    for val,args in zip(np.r_[X,Y],[(r,A,B,b),(B,t,a,A),(a,b,r,t),(t,a,b,B),(b,r,A,a),(A,B,t,r)]):
        D,N=env(*args)
        out.append(N-2*D*val if D>0 else 1.)
    # Target chord 1 longest; index relabel symmetry permits this.
    out += [B+b-A-a,B+b-r-t]
    return np.array(out)

def obj(z):
    A,a,B,b,r,t=z[:6]
    s=np.array([B+b,A+a,r+t])
    return 1/s[0]/np.sum(1/s)

def eq(z):return z[6:].sum()-1
rng=np.random.default_rng(290929)
best=1
for it in range(130):
    # Centered simplex has rays sqrt(2/9), unique areas2/9 and double1/9.
    z=np.r_[np.full(6,np.sqrt(2/9)),np.full(3,2/9),np.full(3,1/9)]
    if it:z[:6]*=np.exp(rng.normal(0,.26,6));z[6:]*=np.exp(rng.normal(0,.2,6));z[6:]/=z[6:].sum()
    sol=minimize(obj,z,method='SLSQP',bounds=[(.005,3)]*6+[(.000001,1)]*6,
        constraints=[{'type':'ineq','fun':cons},{'type':'eq','fun':eq}],options={'maxiter':1400,'ftol':2e-12})
    if sol.success and min(cons(sol.x))>=-1e-8 and abs(eq(sol.x))<1e-8 and sol.fun<best:
        best=sol.fun
        record={'iteration':it,'objective':float(best),'x':sol.x.tolist(),'minimum_constraint':float(min(cons(sol.x))),'equality':float(eq(sol.x))}
        Path('./six_sector_ordinary_relaxation_root_best.json').write_text(json.dumps(record,indent=2))
        print(record,flush=True)
    if best<2/9-1e-7:break
print('DONE',best,flush=True)
