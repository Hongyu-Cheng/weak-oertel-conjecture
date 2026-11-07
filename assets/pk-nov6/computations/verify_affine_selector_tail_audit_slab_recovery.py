"""Exact actual polygon checks; the all-body proof is in the audited source."""
from fractions import Fraction as F
import sympy as s

checks=0
def eq(a,b):
    global checks
    assert s.simplify(a-b)==0,(a,b)
    checks+=1
def yes(p):
    global checks
    assert p
    checks+=1
def clip(poly,u,c):
    out=[]
    for i,P in enumerate(poly):
        Q=poly[(i+1)%len(poly)]
        f=u[0]*P[0]+u[1]*P[1]+c;g=u[0]*Q[0]+u[1]*Q[1]+c
        if f>=0:out.append(P)
        if (f>0 and g<0) or (f<0 and g>0):
            q=f/(f-g);out.append(tuple(x+q*(y-x) for x,y in zip(P,Q)))
    return out
def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly))))/2
def toxy(t,x):return (x,-t-x)

for eps in [F(1,200),F(1,100),F(1,50),F(1,25)]:
    for bottom_ratio in [F(0),F(1,4),F(1,2)]:
        # Center selectors include both nonpositive slopes and one positive slope.
        for slope,intercept in [(F(-1,2),F(0)),(F(1,10),F(-3,2)),(F(-11,10),F(3,2))]:
            X=lambda t:slope*t+intercept
            ptx=[(F(-2),X(F(-2))-bottom_ratio*eps),
                 (F(6),X(F(6))-eps),
                 (F(6),X(F(6))+eps),
                 (F(-2),X(F(-2))+bottom_ratio*eps)]
            poly=[toxy(t,x) for t,x in ptx]
            a=area(poly);W=2*eps;H=F(7)
            eq(a,8*eps*(1+bottom_ratio))
            ux=area(clip(poly,(1,0),1));vy=area(clip(poly,(0,1),1))
            u,v=sorted([ux,vy])
            yes(0<v<a/2)
            Fthreshold=area(clip(poly,(1,1),2-2*W))
            # t<=c is x+y+c>=0.
            yes(Fthreshold<=v)
            low2=area(clip(poly,(1,1),2))
            tail2=area(clip(poly,(-1,-1),-2))
            eq(low2+tail2,a)
            yes(tail2>=a-v-2*W*W)
            yes(W<=2*a/F(8));yes(W<2*a/H)
            yes(tail2>=a-v-8*a*a/(H*H))
            e=area(clip(poly,(1,1),-1))
            yes(0<e<a)
            # For H=7, quadratic (5)=C-24sqrt(ae); certify without floating point.
            C=(v-e)*H*H+6*H*e+8*a*a-9*a-9*e
            yes(C>=0);yes(C*C>=24*24*a*e)

a,e,v,H=s.symbols('a e v H',positive=True)
Delta=s.sqrt(a)-s.sqrt(e)
eq((v*H*H+8*a*a)-(H*s.sqrt(e)+3*Delta)**2,
   (v-e)*H*H-6*s.sqrt(e)*Delta*H+8*a*a-9*Delta*Delta)
eq(s.Matrix([[0,1],[-1,-1]]).det(),1)
print(f'PASS {checks} exact checks')
