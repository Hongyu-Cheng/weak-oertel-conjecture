import numpy as np
from scipy.optimize import linprog
rng=np.random.default_rng(271828)
gamma=27/64;kappa=10/27
hits=0
for attempt in range(20000):
 a=np.exp(rng.uniform(-6,2))
 x=np.sort(rng.uniform(0,1,4));u=a*x
 f=x[0]+x[1]+kappa*x[2]
 if f>=1 or x[3]+x[2]+kappa*x[1]<1:continue
 Q=.999*gamma*(1+a*(1-f));k=Q/gamma-a*f
 if k<max(1-a,a-1) or Q<gamma*max(a,1,k) or np.max(u)>=8*Q/9:continue
 Pmax=(np.sqrt(32*Q-33*u)-np.sqrt(3*u))**2/4
 if 32*k-a-4<0 or 8*k-a-1<0:continue
 Smax=3+(np.sqrt(32*k-a-4)-np.sqrt(3*a))**2/4
 g=1+x/2-(3/4)*x**(-1/3)
 rows=[-g,-u,-np.array([0.,0.,1.,1.]),-np.ones(4),np.ones(4)]
 rhs=[-3,-4*a,-3,-3*(1+a**(1/3)),Smax]
 for i in range(4):
  row=-np.ones(4);row[i]=0;rows.append(row);rhs.append(-3)
 rows=[np.r_[row,1.] for row in rows]
 for i,pp in enumerate(Pmax):
  row=np.zeros(5);row[i]=1;row[4]=1;rows.append(row);rhs.append(pp)
 sol=linprog([0,0,0,0,-1],A_ub=rows,b_ub=rhs,bounds=[(0,None)]*5,method='highs')
 if not sol.success or sol.x[4]<1e-5:continue
 hits+=1
 print('FORMAL SUPPORT FEASIBLE',attempt,'a',a,'u',u,'Q',Q,'k',k,'P',sol.x[:4],'slack',sol.x[4],'Pmax',Pmax,'GdotP',g@sol.x[:4],'moment',sol.x[:4]@u/(4*a),'Smax',Smax,flush=True)
 break
else:print('NO FORMAL SUPPORT FOUND')
print('hits',hits)
