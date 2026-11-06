"""Exact actual-interval and clipped-polygon first-variation checks."""
from fractions import Fraction as F
from itertools import product

checks = 0
def check(p):
    global checks
    assert p
    checks += 1

for l,r,w in product(range(5),range(5),range(-5,6)):
    direct = -2*max(l-w,r+w)
    check(direct == -(l+r)-abs(r-l+2*w))
    for den in (100,1000):
        e = F(1,den)
        T = 2*min(1+e*(w-l),1-e*(r+w))
        check(T == 2+e*direct)

def clip(poly, normal, threshold):
    out=[]
    dot=lambda p: normal[0]*p[0]+normal[1]*p[1]-threshold
    for p,q in zip(poly,poly[1:]+poly[:1]):
        vp,vq=dot(p),dot(q)
        if vp>=0:
            out.append(p)
        if (vp<0<vq) or (vq<0<vp):
            t=-vp/(vq-vp)
            out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return out

def moments(poly):
    twice=mx=my=F(0)
    if len(poly)<3:
        return F(0),F(0),F(0)
    for p,q in zip(poly,poly[1:]+poly[:1]):
        cr=p[0]*q[1]-p[1]*q[0]
        twice+=cr
        mx+=(p[0]+q[0])*cr
        my+=(p[1]+q[1])*cr
    return twice/2,mx/6,my/6

K=[(F(0),F(0)),(F(4),F(0)),(F(4),F(3)),(F(0),F(3))]
normals=[(1,0),(0,1),(1,1),(2,-1),(-1,2),(-2,-3)]
rates=[(F(l),F(r),F(b),F(t)) for l,r,b,t in
       [(0,1,2,1),(1,0,0,2),(2,1,1,0),(1,1,1,1),
        (0,0,1,0),(1,0,0,0),(0,1,0,0),(0,0,0,1)]]
h=F(1,10000)

def rect(e, rates):
    l,r,b,t=rates
    return [(e*l,e*b),(4-e*r,e*b),(4-e*r,3-e*t),(e*l,3-e*t)]

def affine_positive_integral(v0,v1,length):
    if v0>=0 and v1>=0:
        return length*(v0+v1)/2
    if v0<=0 and v1<=0:
        return F(0)
    pos=max(v0,v1)
    return length*pos*pos/(2*abs(v1-v0))

for normal in normals:
    values=[normal[0]*x+normal[1]*y for x,y in K]
    low,high=min(values),max(values)
    thresholds=sorted(set(values+[F(low)+F(i,12)*(high-low) for i in range(12)]))
    for threshold in thresholds:
        original=moments(clip(K,normal,threshold))
        V,Ix,Iy=original
        if V<=0:
            continue
        y=(Ix/V,Iy/V)
        denom=normal[0]*y[0]+normal[1]*y[1]-threshold
        check(denom>0)
        u=(F(normal[0])/denom,F(normal[1])/denom)
        L=lambda p: 1+u[0]*(p[0]-y[0])+u[1]*(p[1]-y[1])
        for rate in rates:
            data=[moments(clip(rect(j*h,rate),normal,threshold)) for j in range(4)]
            # Cap area has degree <=2, first moments degree <=3 on a fixed
            # one-sided clipping cell. All chosen h samples stay in that cell.
            area_der=(-3*data[0][0]+4*data[1][0]-data[2][0])/(2*h)
            derivatives=[]
            for coordinate in (1,2):
                derivatives.append((-11*data[0][coordinate]+18*data[1][coordinate]
                    -9*data[2][coordinate]+2*data[3][coordinate])/(6*h))
            velocity=((derivatives[0]*V-Ix*area_der)/V**2,
                      (derivatives[1]*V-Iy*area_der)/V**2)
            l,r,b,t=rate
            # CCW edges bottom/right/top/left have inward speeds b/r/t/l.
            speeds=[b,r,t,l]
            lengths=[F(4),F(3),F(4),F(3)]
            cost=sum(speed*affine_positive_integral(L(p),L(q),length)
                for p,q,speed,length in zip(K,K[1:]+K[:1],speeds,lengths))
            predicted=-cost-V*(u[0]*velocity[0]+u[1]*velocity[1])
            check(predicted==area_der)
            # Independently check exact polynomial reconstruction of area.
            check(data[3][0]-3*data[2][0]+3*data[1][0]-data[0][0]==0)

for l,r,b,t in rates:
    D=3*(l+r)+4*(b+t)
    B=(6*(r-l),6*(t-b))
    for wx,wy in product(range(-2,3),repeat=2):
        v=(-B[0]-12*wx,-B[1]-12*wy)
        gauge=max(abs(v[0])/2,abs(v[1])/F(3,2))
        # Negative-polar optimizer vertices: (+/-1/2,0),(0,+/-2/3).
        values=[-D-q[0]*(B[0]+12*wx)-q[1]*(B[1]+12*wy)
                for q in [(F(1,2),0),(F(-1,2),0),(0,F(2,3)),(0,F(-2,3))]]
        check(min(values)==-D-gauge)

for num in range(1,20):
    e=F(num,100)
    M=2*(1-e)
    mark=e*e
    check((1-e)/M==F(1,2))
    check((1-e-mark)/M<F(1,2))
    check(2*(1-e-mark)/M<1)

print(f'PASS: {checks} exact checks')
