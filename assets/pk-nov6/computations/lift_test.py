import math
import numpy as np
from scipy.optimize import differential_evolution, minimize

T=[(0.,0.),(1.,0.),(0.,1.)]
B=[(0.,0.),(1/3,0.),(1/3,2/3),(0.,1.)]
F=[(-1,B),(0,T),(1,B)]

def area(p):
    return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p))))/2 if p else 0.

def cut(p,a,b,t):
    out=[]
    for i,u in enumerate(p):
        v=p[(i+1)%len(p)]
        fu=a*u[0]+b*u[1]-t
        fv=a*v[0]+b*v[1]-t
        if fu>=0: out.append(u)
        if (fu<0<fv) or (fv<0<fu):
            r=fu/(fu-fv)
            out.append((u[0]+r*(v[0]-u[0]),u[1]+r*(v[1]-u[1])))
    return area(out)

total=sum(area(p) for _,p in F)
def mass(x,y,theta,slope):
    a,b=math.cos(theta),math.sin(theta)
    t=a*x+b*y
    return sum(cut(p,a,b,t-slope*z) for z,p in F)/total

# Restricted family of continuous normals gives a rigorous upper certificate
# once its maximum is bounded analytically. Numerics identify that certificate.
dirs=np.linspace(0,2*np.pi,61)[:-1]
def restricted_depth(pt):
    x,y=pt
    if x<0 or y<0 or x+y>1:return -10
    return min(mass(x,y,t,0) for t in dirs)

opt=differential_evolution(lambda pt:-restricted_depth(pt),[(0,1),(0,1)],tol=1e-10,seed=1)
x,y=opt.x
full=differential_evolution(lambda p:mass(x,y,p[0],p[1]),[(0,2*np.pi),(-3,3)],tol=1e-10,seed=2)
print('max restricted',opt.x,-opt.fun,'full at candidate',full.fun,full.x,'target lift',56/171)
print('marginal beta',14/19,'OC',2/9)
