"""Exact actual-fiber checks for the full-target midpoint bridge."""
from fractions import Fraction as F


def length_above(interval, threshold):
    lo,hi=interval
    return max(F(0),hi-max(lo,threshold))


def data(a):
    k=(3-a)/4
    A=(k-a/2,k+a/2)
    B=(F(0),F(1))
    C=(k-F(1,2),k+F(1,2))
    D=((A[0]+C[0])/2,(A[1]+C[1])/2)
    s=(1+a)/2; M=2+a; L=(1+a)/a; r=a/s
    g=(F(1,2)+(1+a)*k)/M
    assert D==((1-a)/2,F(1))
    assert B[0]<=D[0]<=D[1]<=B[1]
    assert all(v<M/2 for v in (a,F(1),F(1)))
    assert abs(F(1)-F(1))<a
    assert L*r==2
    assert g==(5+2*a-a*a)/(4*(2+a))
    assert D[0]<g<1
    assert g-1<A[0] and g+1>C[1]
    eta_cap=r*length_above(D,g)
    cost=length_above(B,g)+eta_cap
    actual=sum(length_above(K,g+z) for z,K in [(-1,A),(0,B),(1,C)])
    assert actual==1-g+a
    assert actual/M==(5*a*a+10*a+3)/(4*(2+a)**2)
    assert actual==cost+a-eta_cap
    assert a-eta_cap>0
    reflected=(1-A[1],1-A[0])
    assert C[0]<=reflected[0]<=reflected[1]<=C[1]
    symmetric_mid=((A[0]+reflected[0])/2,(A[1]+reflected[1])/2)
    assert symmetric_mid==((1-a)/2,(1+a)/2)
    safe=(1+2*a)/(2*M)
    assert safe>F(1,4)
    return g,cost,actual,M,safe,eta_cap


checks=0
for denominator in range(2,31):
    for numerator in range(1,denominator):
        data(F(numerator,denominator))
        checks+=1

g,cost,actual,M,safe,eta_cap=data(F(1,10))
assert g==F(173,280)
assert cost==F(1391,3080)
assert F(21,40)-cost==F(113,1540)
assert actual==F(27,56)
assert F(21,40)-actual==F(3,70)
assert F(1,10)-eta_cap==F(47,1540)
assert safe==F(2,7)

g,cost,actual,M,safe,eta_cap=data(F(1,100))
s2=F(121,400);s=F(101,200)
assert s2<s<=1
assert F(1,100)/s==F(2,101)<F(4,121)==F(1,100)/s2
assert g==F(16733,26800)
assert actual==F(2067,5360)
assert actual/M==F(3445,17956)
assert F(2,9)-actual/M==F(4907,161604)>0
assert cost<actual<F(2,9)*M
assert safe==F(17,67)>F(2,9)

print(f'PASS: {checks} exact compatible interval/product parameter checks; '
      'd1 sharp-density and d2 full-volume actual cap countercertificates; '
      'uniform-coupling moments, strict endpoint isolation and safe reflected subbody.')
