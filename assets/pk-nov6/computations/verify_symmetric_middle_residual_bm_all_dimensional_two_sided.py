from fractions import Fraction as F
from math import comb

checks=0
def check(v):
    global checks
    assert v
    checks+=1

def parameters(d):
    gamma=F(d,d+1)**d
    rho=F(d-1,d+1)**d
    beta=gamma/(1+2*gamma+rho)
    return gamma,rho,beta

for d in range(1,41):
    gamma,rho,beta=parameters(d)
    odd=2*sum(comb(d,j)*d**(d-j) for j in range(1,d+1,2))
    check(odd==(d+1)**d-(d-1)**d)
    check(odd>=2*d**d)
    check((odd==2*d**d)==(d<=2))
    check(gamma<=F(1,2))
    check(2*gamma+rho<=1)
    check(beta>=gamma/2)
    check((beta==gamma/2)==(d<=2))
    check(beta<=F(1,4))
    check(gamma/(1+2*gamma+rho)==beta)
    check(F(1,2)**d*(1+F(d-1,d+1))**d==gamma)
    check(2*gamma<=1+rho)
    if d>=2:
        r=F(d,d+1);small=F(d-1,d+1)
        check((1+small)/2==r)
        check(small**d==rho)
        check(2*r**d==2*gamma)
        check(r-1<F(1,d+1))
        check(small-2<F(1,d+1))
        check(gamma/(rho+2*gamma+1)==beta)

for d in range(1,13):
    gamma,rho,beta=parameters(d)
    for j in range(0,31):
        root=F(j,20)
        h=root**d
        s=max(F(0),2*root-1)
        t=s**d
        for i in range(0,41):
            a=F(i,40)
            value=max(gamma,h+max(F(0),a-t))/(1+a+2*h)
            check(value>=beta)
        if h<=gamma:
            a0=gamma-h+t
            check(0<=a0<=1)
            check(a0>=t)
            value=max(gamma,h+max(F(0),a0-t))/(1+a0+2*h)
            check(value==gamma/(1+gamma+h+t))
            check(value>=beta)
        elif h<=1:
            check(rho<=t<=1)
            check(h==F(1,2)**d*(1+s)**d)
            check(h*(1+rho)>=gamma*(1+t))
            check(h/(1+t+2*h)>=beta)

check(parameters(1)[2]==F(1,4))
check(parameters(2)[2]==F(2,9))
check(parameters(3)[2]==F(3,14))
for i in range(1,41):
    a=F(i,40)
    check(((1+a)/2)/(2*(1+a))==F(1,4))

# Exact planar actual selector equality.
def area(vertices):
    return abs(sum(x*y2-y*x2 for (x,y),(x2,y2) in
                   zip(vertices,vertices[1:]+vertices[:1])))/2
B=[(F(-1),F(0)),(F(1),F(0)),(F(0),F(1))]
A=[(x/3,y/3) for x,y in B]
K=[(-F(2,3),F(0)),(F(0),-F(2,3)),
   (F(2,3),F(0)),(F(0),F(2,3))]
check(area(B)==1)
check(area(A)==F(1,9))
check(area(K)==F(8,9))
check(area(A)+area(B)+area(K)==2)
check(area(K)/2==F(4,9))
check(F(2,3)**2==F(4,9))
check(max(y-1 for x,y in K)<F(1,3))
check(max(y-2 for x,y in A)<F(1,3))

# The previous failing density certificate is below target exactly.
a=F(4,25);k=F(6272,7425);v=F(49,100)
old=k/2+a*(1-k/(2*v))
target=F(2,9)*(1+a+k)
check(old==F(4,9))
check(target-old==F(14,13365))
# Root-free certificate that the residual bound is strictly larger:
# h+a-(sqrt(2k)-1)^2-target = a-1-3k/2+2sqrt(2k)-target.
rhs=target-a+1+F(3,2)*k
check(rhs>0)
check(8*k>rhs*rhs)

# Exact fixed-h optimizer for the ordinary-depth-sigma extension.
for d in range(1,9):
    gamma=F(d,d+1)**d
    for m in range(11):
        sigma=gamma+(F(1,2)-gamma)*F(m,10)
        r=sigma/(1-sigma)
        H=gamma/r
        for j in range(21):
            root=F(j,16);h=root**d;t=max(F(0),2*root-1)**d
            if h<=H:
                a0=gamma-r*h+t
                check(0<=a0<=1)
                value=max(gamma,r*h+max(F(0),a0-t))/(1+a0+(1+r)*h)
                check(value==gamma/(1+gamma+h+t))
                astar=a0
            elif h<=1:
                astar=t
            else:
                astar=F(1)
            best=max(gamma,r*h+max(F(0),astar-t))/(1+astar+(1+r)*h)
            for i in range(21):
                aa=F(i,20)
                value=max(gamma,r*h+max(F(0),aa-t))/(1+aa+(1+r)*h)
                check(value>=best)
check(11520<11881)
check(11520>11449)

# Planar ratio-dependent threshold and the exact endpoint certificates.
for j in range(20,61):
    x=F(j,60);aa=x*x;DD=17+18*x+17*x*x
    sigma=2*(5+2*x+5*x*x)/DD
    v=(1+x)**2/4
    kl=1-aa;ku=DD/28;hl=(1-sigma)*kl
    check(1-sigma==7*(1+x)**2/DD)
    check(F(1,2)-sigma==(3*x-1)*(3-x)/(2*DD))
    check(sigma-F(4,9)==2*(11*x*x-18*x+11)/(9*DD))
    check(F(4,9)<sigma<=F(1,2))
    check(ku==F(4,9)*(1+aa)/(2*sigma-F(4,9)))
    check(ku-kl==(3*x-1)*(15*x+11)/28)
    check((1-sigma)*ku==v)
    check(sigma*ku==F(2,9)*(1+aa+ku))
    check(4*DD-63*(1+x)**2*(1-x*x)==
          (3*x-1)*(21*x**3+49*x*x+39*x-5))
    check(0<=hl<=F(4,9))
    if hl<=F(1,4):
        check(1-hl>=F(3,4))
    else:
        # 4sqrt(h)-5h>=4/9, with both sides of the square positive.
        check(16*hl>=(5*hl+F(4,9))**2)
    for m in range(1,11):
        lower=sigma-F(m,1000)
        if lower<F(4,9):
            continue
        if x>F(1,3):
            check((1-lower)*ku>v)
            check(max(F(4,9),lower*ku)<F(2,9)*(1+aa+ku))
for j in range(1,21):
    x=F(j,60)
    check(4*(F(5,9)-x*x)-(1+x)**2==(1-3*x)*(15*x+11)/9)
    check(F(4,9)/(1-x*x)<=F(1,2))
xx=F(2,5)
check(2*(5+2*xx+5*xx*xx)/(17+18*xx+17*xx*xx)==F(330,673))

print(f'PASS: {checks} exact checks')
