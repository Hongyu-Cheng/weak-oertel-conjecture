import sympy as s
import numpy as np
from itertools import product
p,q,r,t=s.symbols('p q r t',positive=True)
v=s.Matrix([p,q,r,t])
P=s.cancel((p**3/((p+r)*(p+t))-q**3/((q+r)*(q+t)))/(p-q))
g=s.Matrix([s.diff(P,z)*sg for z,sg in zip(v,[1,1,-1,-1])])
H=s.Matrix(4,4,lambda i,j:s.diff(P,v[i],v[j])*([1,1,-1,-1][i]*[1,1,-1,-1][j]))
fun=s.lambdify((p,q,r,t),[P,g,H],'numpy')
count=0
for a in product(range(1,10),repeat=4):
    pp,gg,hh=fun(*a); gg=np.asarray(gg).ravel(); b=gg/gg.sum()
    if not ((b[0]>1/3+1e-10 and b[1]<=1/3) or (b[1]>1/3+1e-10 and b[0]<=1/3)): continue
    count+=1
    vp=np.array([gg[1],-gg[0],0,0]); vn=np.array([0,0,gg[3],-gg[2]])
    Q=np.array([[vp@hh@vp,vp@hh@vn],[vn@hh@vp,vn@hh@vn]])
    if np.linalg.eigvalsh(Q)[0]>=-1e-12:
        print('OBSTRUCTION',a,'b',b,'Q',Q,'eigen',np.linalg.eigvalsh(Q)); break
else: print('No obstruction',count)
print('P',s.factor(P))
