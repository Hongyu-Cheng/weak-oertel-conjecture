import numpy as np,json
from math import exp,expm1,cos,sin,pi
from scipy.optimize import brentq,linprog

def clip(poly,n,c):
    out=[]
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        a=float(np.sum(p*n))-c;b=float(np.sum(q*n))-c
        if a>=-1e-14:out.append(p)
        if (a<0<b) or (b<0<a):out.append(p+a/(a-b)*(q-p))
    return out

def mass(poly,co):
    if len(poly)<3:return 0.
    A,B,C=-co
    norm=A*A+B*B
    if norm<1e-16:
        return exp(C)*sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1]))/2
    ans=0.
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        dx=q[0]-p[0];dy=q[1]-p[1]
        z=A*dx+B*dy
        phi=expm1(z)/z if abs(z)>1e-8 else 1+z/2+z*z/6
        ans+=(A*dy-B*dx)/norm*exp(A*p[0]+B*p[1]+C)*phi
    return ans

def cells(coeff):
    T=[np.array(p,float) for p in [(0,0),(1,0),(0,1)]]
    ans=[]
    for i,c in enumerate(coeff):
        P=T
        for j,cc in enumerate(coeff):
            if i==j:continue
            P=clip(P,c[:2]-cc[:2],cc[2]-c[2])
        if len(P)>2:ans.append((P,c))
    return ans

def evaluate(coeff,angles=192,alpha=4/9):
    cc=cells(coeff)
    M=sum(mass(P,c) for P,c in cc)
    def prob(n,t):return sum(mass(clip(P,-n,-t),c) for P,c in cc)/M
    nn=np.array([[cos(a),sin(a)] for a in np.linspace(0,2*pi,angles,endpoint=False)])
    qq=[]
    for n in nn:
        lo=min(0,n[0],n[1]);hi=max(0,n[0],n[1])
        qq.append(brentq(lambda t:prob(n,t)-alpha,lo-1e-8,hi+1e-8,xtol=1e-12))
    # Maximize the minimum signed spatial slack for a stable margin.
    opt=linprog([0,0,-1],A_ub=np.column_stack([-nn,np.ones(angles)]),b_ub=-np.array(qq),
                bounds=[(None,None)]*3,method='highs')
    return opt,nn,np.array(qq),cc,M

if __name__=='__main__':
    data=json.load(open('./logconcave_piecewise_candidate.json'))
    co=np.array(data['coeff'])
    opt,nn,qq,cc,M=evaluate(co)
    print('mass',M,'opt',opt.x,'objective',opt.fun)
    print('active',[(i,nn[i].tolist(),float(qq[i])) for i,v in enumerate(opt.ineqlin.residual) if abs(v)<1e-8])
