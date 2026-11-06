"""Exploratory only: exact piecewise tail formula evaluated numerically."""
import numpy as np
from scipy.optimize import minimize_scalar
from math import sin,cos,pi,sqrt

def tail(v,s):
    l,m,h=sorted(v)
    if s<=l: return 1.
    if s>=h: return 0.
    if s<m: return 1-(s-l)**2/((m-l)*(h-l))
    return (h-s)**2/((h-m)*(h-l))

def densityline(v,s):
    l,m,h=sorted(v)
    if not l<s<h:return 0.,0.
    if s<m:return 2/((m-l)*(h-l)), -2*l/((m-l)*(h-l))
    return -2/((h-m)*(h-l)),2*h/((h-m)*(h-l))

def pair(v,s):
    knots=sorted(set([0.]+[abs(s-vv) for vv in v]))
    cand=knots+[knots[-1]+2]
    for l,h in zip(knots,knots[1:]):
        a=(l+h)/2
        ap,bp=densityline(v,s+a)
        am,bm=densityline(v,s-a)
        # derivative -rho(s+a)+rho(s-a)
        aa=-ap-am; bb=(-ap+am)*s+bm-bp
        if abs(aa)>1e-14:
            root=-bb/aa
            if l<root<h:cand.append(root)
    vals=[tail(v,s+a)+tail(v,s-a) for a in cand]
    j=int(np.argmin(vals));return vals[j],cand[j]

def directional(r,t,theta):
    x,y=cos(theta),sin(theta); s=t*(x+y); v=[0,x,y]
    p,a=pair(v,s)
    return r*r*tail(v,s/r)+p,a

def dep(r,t,details=False):
    angs=np.linspace(-pi,pi,73)
    vals=[directional(r,t,h)[0] for h in angs]
    poss=[]
    for i in range(1,len(angs)-1):
        if vals[i]<=vals[i-1] and vals[i]<=vals[i+1]:
            res=minimize_scalar(lambda th:directional(r,t,th)[0],bounds=(angs[i-1],angs[i+1]),method='bounded',options={'xatol':1e-12})
            poss.append((res.fun,res.x,directional(r,t,res.x)[1]))
    poss.extend((directional(r,t,h)[0],h,directional(r,t,h)[1]) for h in [-3*pi/4,pi/4,0,pi/2,-pi])
    ans=min(poss)
    return (ans,sorted(poss)) if details else ans[0]

for r in [1,1.05,1.2,1.41,1.4142135623730951,1.5,1.75,2,2.5,3,4,6]:
    res=minimize_scalar(lambda t:-dep(r,t),bounds=(max(.0001,r/5),r/2-.0001),method='bounded',options={'xatol':1e-10})
    val=-res.fun;t=res.x
    ans,ps=dep(r,t,True)
    close=[p for p in ps if p[0]<val+1e-5]
    print('r',r,'t',t,'D',val,'norm',val/(2+r*r),'caps',close,flush=True)
