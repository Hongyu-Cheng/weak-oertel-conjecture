import numpy as np
from scipy.optimize import linprog
rng=np.random.default_rng(141421)
# a,k,Q,S,H1,H2,H3,epsilon
b=4.5;count=0
for j in range(10000):
    x=np.sort(rng.uniform(0,1,3));f=x[0]+x[1]+x[2]/4;g=x[2]+x[1]+x[0]/4
    if g<1 or f>=1:continue
    aa=[];bb=[]
    def le(d,c):
        row=np.zeros(8)
        for i,v in d.items():row[i]=v
        aa.append(row);bb.append(c)
    le({0:1,1:-4,3:3},-b)
    le({0:1,1:-1},b);le({0:-1,1:-1},-b);le({0:-1,1:1},b)
    le({0:4/9,2:-1},0);le({1:4/9,2:-1},0);le({2:-1},-(4/9)*b)
    le({0:f,1:1,2:-9/4},0)
    le({0:-2/9,1:-2/9,2:1,7:1},(2/9)*b)
    for i,xx in enumerate(x):
        le({4+i:1,3:-np.sqrt(xx)},0)
        le({4+i:3,0:5*xx,2:-4},0)
    eq=np.zeros((1,8));eq[0,3]=-1;eq[0,4:7]=1
    sol=linprog([0,0,0,0,0,0,0,-1],A_ub=aa,b_ub=bb,A_eq=eq,b_eq=[3],bounds=[(0,None)]*8,method='highs')
    count+=1
    if sol.status==3:print('UNBOUNDED',x);break
    if sol.success and sol.x[7]>1e-8:
        print('FEASIBLE fractions',x,'f,g',f,g,'a,k,Q,S,H1,H2,H3,eps',sol.x,flush=True);break
else:print('NO FEASIBLE')
print('count',count)
