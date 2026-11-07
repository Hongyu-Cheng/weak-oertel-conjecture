import numpy as np
from scipy.optimize import linprog
rng=np.random.default_rng(83472)
gamma=27/64;kappa=10/27
for attempt in range(30000):
 a=np.exp(rng.uniform(-4,2))
 x=np.sort(rng.uniform(0,1,4));u=a*x
 f=x[0]+x[1]+kappa*x[2]
 if f>=1 or x[3]+x[2]+kappa*x[1]<1:continue
 Q=gamma*(1+a*(1-f))
 if np.max(u)>=8*Q/9:continue
 P=(np.sqrt(32*Q-33*u)-np.sqrt(3*u))**2/4
 if P@u<=4*a:continue
 H=P/(3/4)
 moment_factor=1+x/2-(3/4)*x**(-1/3)
 if H@moment_factor<4:continue
 patterns=np.array([[int(mask>>j&1) for j in range(4)] for mask in range(1,16)])
 patterns=patterns[patterns@P>3+1e-8]
 mat=np.vstack([np.ones(len(patterns)),patterns.T])
 sol=linprog(np.zeros(len(patterns)),A_eq=mat,b_eq=np.r_[a,u],bounds=(0,None),method='highs')
 if not sol.success:continue
 print('FEASIBLE',attempt,'a',a,'u',u,'Q',Q,'P',P,'moment',P@u/(4*a),'residual moment',H@moment_factor,'k',Q/gamma-a*f,'patterns',[(list(p),w) for p,w in zip(patterns,sol.x) if w>1e-8]);break
else:print('NO FORMAL ROW FOUND')
