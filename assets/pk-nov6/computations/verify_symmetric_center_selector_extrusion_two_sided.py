from fractions import Fraction as F
from itertools import product

checks=0
def check(x):
    global checks
    assert x
    checks+=1

def interval_cap(l,h,threshold,positive=True):
    upper=max(F(0),min(h-l,h-threshold))
    return upper if positive else h-l-upper

s=F(11,20);L=F(279,220);c=L/2;width=s+L
fibers={-1:((-F(1,20),F(1,20)),(-F(1,20),F(1,20))),
         0:((-s/2,s/2+L),(-s/2,s/2)),
         1:((-F(1,2),F(1,2)),(-F(1,2),F(1,2)))}
areas={z:(x[1]-x[0])*(y[1]-y[0]) for z,(x,y) in fibers.items()}
M=sum(areas.values())
check(width==F(20,11))
check(c==F(279,440))
check(s/2+L==F(679,440))
check(M==F(201,100))
check(max(areas.values())<M/2)

# Cap x+alpha*z>=threshold for the three explicitly printed candidates.
for alpha,threshold,expected in [(F(0),c,F(1,2)),(F(2),F(2),F(1,2)),(-F(2),F(2),F(1,200))]:
    mass=sum(interval_cap(*x,threshold-alpha*z)*(y[1]-y[0]) for z,(x,y) in fibers.items())
    check(mass==expected)
    check(mass<M/4)
check(M/4-F(1,2)==F(1,400))
check(F(2,9)*M==F(67,150))
check(F(1,2)-F(67,150)==F(4,75))

# Actual endpoint midpoint fits the continuously translated middle box.
for j in range(-40,41):
    t=F(j,40)
    check(t*c-width/2<=-s/2)
    check(t*c+width/2>=s/2)
    check(width*s==1)

for n in range(1,10):
    total=(2**(n-1))*M
    check(total/(2**(n+1))==F(201,400))
for j in range(1,41):
    shift=F(j,40)
    old=F(2);new=old+2*shift
    shifted_cap=interval_cap(-1+shift,1+shift,F(0),positive=False)
    check(old/2-shifted_cap==(new-old)/2)

# The positive equal-volume bridge is valid for all nonnegative k,v.
for k,v in product([F(i,9) for i in range(1,40)],repeat=2):
    check(k/2+max(F(0),v-k/2)==max(k/2,v))
    check(max(k/2,v)>=(k+2*v)/4)
for i in range(0,101):
    u=F(i,100)
    for j in range(0,151):
        k=F(j,25)
        value=max(F(1),k,(1-u)*k+2*u*u)/(1+u*u+k)
        check(value>=F(4,9))
        check((value==F(4,9))==(u==F(1,2) and k==1))
    if F(1,2)<u<1:
        k0=(1-2*u*u)/(1-u)
        check(F(9,4)-(1+u*u+k0)==(2*u-1)*(2*u*u+3*u-1)/(4*(1-u)))
        check(2*u/(1+u)**2-F(4,9)==2*(2*u-1)*(2-u)/(9*(1+u)**2))
for d in range(1,31):
    # At the sole relaxed equality parameters, strict actual AM-GM
    # is equivalent to ((1+x)/2)^2>x for x=(1/4)^(1/d)!=1.
    # Certify an exact representative root-power inequality instead:
    # endpoint root ratio1/2 gives a=2^-d and v*=(3/4)^d>sqrt(a).
    aa=F(1,2)**d; vv=F(3,4)**d
    check(vv*vv>aa)
radii={j:1-F(abs(j),4) for j in range(-3,4)}
volumes={j:r*r for j,r in radii.items()}
check(sum(volumes.values())==F(11,4))
expected={0:F(9,16),1:F(13,32),2:F(5,32),3:F(1,32)}
for p in radii:
    bound=volumes[p]/2
    for z in radii:
        w=2*p-z
        if z>=w or w not in radii:
            continue
        a=min(volumes[z],volumes[w])
        vstar=((radii[z]+radii[w])/2)**2
        bound+=a*max(F(0),1-volumes[p]/(2*vstar))
    check(bound==expected[abs(p)])
    check(bound<F(11,18))
check(F(11,18)-F(9,16)==F(7,144))
check(F(3,2)*F(9,16)==F(27,32))
check(F(27,32)>F(11,18))
Y=F(5,8);left=-F(11,40);right=F(679,440);height=F(11,20)
check(c-Y==F(1,110))
check(height*(c-Y)==F(1,200))
check(height*(right-Y)==F(101,200))
check(height*(F(1,2)-left)+F(1,100)==F(349,800))
check(F(349,800)<F(101,200))
check(F(101,200)-F(201,400)==F(1,400))
check(F(16,9)<F(36,11))
check(2*min(Y-left,right-Y)/height==F(36,11))
check(F(9,20)*(1+F(16,9))==2*Y)
check(F(1,2)-F(1,200)+F(1,100)==F(101,200))
print(f"PASS: {checks} exact checks")
