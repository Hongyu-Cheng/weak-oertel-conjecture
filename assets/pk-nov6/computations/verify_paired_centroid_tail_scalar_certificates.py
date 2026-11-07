"""Exact algebra certificates for the paired-centroid-tail auxiliary theorem."""
from fractions import Fraction as F

def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]
def scale(a,c): return [c*x for x in a]
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out
def power(a,n):
    out=[1]
    for _ in range(n): out=mul(out,a)
    return out
def derivative(a): return [i*a[i] for i in range(1,len(a))]
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def equal(a,b): assert trim(a)==trim(b),(a,b)

# d=2: 9(c^2-r^2) = (1-r^2) - 8r^3(1-r)/(1+r)^2.
A=[1,1];N=[1,1,4]
lhs=add(power(N,2),scale(mul([0,0,1],power(A,2)),-9))
rhs=add(mul([1,0,-1],power(A,2)),[0,0,0,-8,8])
equal(lhs,rhs)

# d=3 target T <=5/32.
A=[1,1,1];N=[1,1,1,3]
P=add(mul([5,0,0,27],power(A,3)),scale(power(N,3),-4))
Q=[1,4,10,8,23,80,90,108,81]
equal(P,mul([1,-1],Q));assert all(x>0 for x in Q)

# J=-log(v)-N/D, N=(1-v)(7+5v), D=2(1+5v).
N=[7,-2,-5];D=[2,10]
# J' numerator with common denominator v D^2.
numerator=add(scale(power(D,2),-1),
              scale(mul([0,1],add(mul(derivative(N),D),
                                      scale(mul(N,derivative(D)),-1))),-1))
equal(numerator,scale(mul(mul([-1,1],[-1,5]),[-2,5]),2))

# Exact lower bound log5 > four positive atanh terms >8/5.
log_lower=2*sum((F(2,3)**(2*j+1)/F(2*j+1) for j in range(4)),F(0))
assert log_lower>F(8,5)
assert F(1)-2*F(4,5)**4>F(1,6)

# Sample exact frustum evaluation only as a consistency check, not a proof.
for d in range(2,21):
    gamma=F(d,d+1)**d
    for j in range(100):
        r=F(j,100)
        m=F(d,d+1)*(1-r**(d+1))/(1-r**d)
        assert 2*m-1>=r
        T=((2*m-1)**d-r**d)/(1-r**d)
        assert T<=1-2*gamma
        assert T<=F(1,6)

print('PASS: exact paired-tail scalar certificates')
print('four-term log5 lower bound minus8/5 =',log_lower-F(8,5))
print('dimension4 target minus1/6 =',F(1)-2*F(4,5)**4-F(1,6))
