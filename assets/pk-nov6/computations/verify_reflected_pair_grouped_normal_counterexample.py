from fractions import Fraction as F

checks=0
r=F(9,10);t=F(1,4);a=F(5,9);b=F(2,9)
candidate=2*(a*r-t)**3/(a*(a-b)**2)
assert candidate==F(81,160)
grouped=[2*(r-t)**3,F(608,1000),r**3-(6*t-r)**3]
assert grouped==[F(2197,4000),F(608,1000),F(513,1000)]
assert min(grouped)-candidate==F(27,4000)
checks+=3

def tail(k,x):
    if x<=0:return F(1)
    if x>=1:return F(0)
    return [(1-x)**3,1-3*x*x+2*x**3,1-x**3][k-1]
for k in (1,2,3):
    q=k*t/r
    for shift in [F(i,360) for i in range(721)]+[q,1-q]:
        val=r**3*(tail(k,q-shift)+tail(k,q+shift))
        assert val>=grouped[k-1]
        checks+=1

for d in range(2,41):
    t=F(1,d+1);G=(1-t)**d
    for h in range(1,21):
        r=F(d,d+1)+F(h,20*(d+1))
        L=(d+1)*r-d;D=d*d-(d*d-1)*r
        a=1/D;b=(d+1)*(1-r)/D
        left=1-(d-1)*t/r
        assert a+(d-1)*b==1 and 0<=b<a<=1
        assert a-left==(d-1)*L*L/(D*(d+1)*r)>=0
        assert t-b*r==L*L/((d+1)*D)>=0
        assert (a*r-t)**d/(a*(a-b)**(d-1))==G*L
        for z in [left,(left+a)/2,a,(a+1)/2,F(1)]:
            logder=d*r/(z*r-t)-1/z-F(d*(d-1),1)/(d*z-1)
            assert logder==t*(z*D-1)/(z*(z*r-t)*(d*z-1))
            val=(z*r-t)**d/(z*((d*z-1)/(d-1))**(d-1))
            assert val>=G*L
            checks+=2
        checks+=4
print(f'PASS {checks} exact checks')
