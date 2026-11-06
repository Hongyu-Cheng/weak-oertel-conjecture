from fractions import Fraction as F

checks=0
def ck(x):
    global checks
    assert x
    checks+=1

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(points):
    points=sorted(set(points))
    if len(points)<2:return points
    lo=[];hi=[]
    for p in points:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi)>1 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2
def dot(u,p):return u[0]*p[0]+u[1]*p[1]
def clip(poly,u,b):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=dot(u,p)-b;fq=dot(u,q)-b
        if fp>=0:out.append(p)
        if (fp<0<fq) or (fq<0<fp):
            z=fp/(fp-fq)
            out.append(tuple(p[j]+z*(q[j]-p[j]) for j in (0,1)))
    return hull(out)

T=hull([(F(1),F(1)),(F(1),F(-2)),(F(-2),F(1))])
normals=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]
A=[(F(3,5)*x,F(3,5)*y) for x,y in T]
K=[(-x,-y) for x,y in T]
B=[(-F(4,5)*x,-F(4,5)*y) for x,y in T]
aa,kk,bb=map(area,(A,K,B))
ck((aa,kk,bb)==(F(81,50),F(9,2),F(72,25)))
ck(aa+kk+bb==9)
Q=F(181,50);r=Q/9
for p in A:
    for q in B:
        midpoint=tuple((p[j]+q[j])/2 for j in (0,1))
        ck(all(dot(v,midpoint)>=-1 for v in normals))
for v in normals:
    ck(area(clip(A,v,-F(8,5)))==aa)
    ck(area(clip(K,v,0))==2)
    ck(area(clip(B,v,F(8,5)))==0)
    ck(area(clip(A,v,-F(8,5)))+area(clip(K,v,0))+area(clip(B,v,F(8,5)))==Q)
for ux in range(-3,4):
    for uy in range(-3,4):
        if ux==uy==0:continue
        u=(F(ux),F(uy))
        for j in range(-20,21):
            alpha=F(j,3)
            pair=area(clip(A,u,alpha))+area(clip(B,u,-alpha))
            ck(pair>=aa)
            ck(pair+area(clip(K,u,0))>=Q)
ck(aa/2<Q and bb/2<Q)
ck(F(1,3)<r<F(4,9))

# Exact step-function integration on a unit face.
pieces=[(F(0),F(1,3),F(1,3)-r),
        (F(1,3),F(2,3),F(2,3)-r),
        (F(2,3),F(1),F(1,3)-r)]
def linear_integral(l,h,slope,intercept):
    out=F(0)
    for a,b,value in pieces:
        left=max(l,a);right=min(h,b)
        if left<right:
            out+=value*(slope*(right*right-left*left)/2+intercept*(right-left))
    return out
def potential(t):
    return (1-t)*linear_integral(0,t,1,0)+t*linear_integral(t,1,-1,1)
left_derivative=linear_integral(0,1,-1,1)
right_derivative=-linear_integral(0,1,1,0)
ck(left_derivative>0 and right_derivative<0)
for j in range(1,60):
    t=F(j,60)
    cost=linear_integral(0,t,1/t,0)+linear_integral(t,1,-1/(1-t),1/(1-t))
    ck(cost==potential(t)/(t*(1-t)))
    ck(cost>=F(1,2)*(F(4,9)-r))
    ck(potential(t)>0)
for a0,b0,c,d in [(F(1,5),F(4,5),F(2,5),F(3,5)),
                  (F(0),F(4,5),F(1,3),F(1,2)),
                  (F(1,10),F(1),F(1,2),F(3,4)),
                  (F(1,4),F(3,4),F(1,2),F(1,2))]:
    integral=linear_integral(0,c,1/(c-a0),-a0/(c-a0))
    integral+=linear_integral(c,d,0,1)
    integral+=linear_integral(d,1,-1/(b0-d),b0/(b0-d))
    boundary=(potential(c)-a0*left_derivative)/(c-a0)
    boundary+=(potential(d)+(1-b0)*right_derivative)/(b0-d)
    ck(integral==boundary)
print(f'PASS: {checks} exact actual-body and Green-interface checks')
