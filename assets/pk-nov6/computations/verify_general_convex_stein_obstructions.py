from fractions import Fraction as F

# Exact polynomial integration on a rational interval.
def integrate(coefficients, left, right):
    return sum(c*(right**(i+1)-left**(i+1))/F(i+1)
               for i,c in enumerate(coefficients))

def multiply(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def derivative(a):
    return [F(i)*a[i] for i in range(1,len(a))]

cases=[
    (F(1),F(2),[F(4),F(-2)],F(4,3),[F(-2,3),F(1),F(-1,3)]),
    (F(0),F(6),[F(1,3),F(-1,18)],F(2),[F(0),F(2),F(-1,3)]),
]
for left,right,f,mean,tau in cases:
    assert integrate(f,left,right)==1
    assert integrate([F(0)]+f,left,right)==mean
    assert derivative(multiply(tau,f))==multiply([mean,F(-1)],f)

for t in [F(5,4),F(3,2),F(7,4)]:
    m1=(2-t)/2; m2=(3*t-2)/2
    assert m1+m2==t
assert F(-1,2)<0 and F(3,2)>1

t=F(1,2)
assert 2-F(2,3)*t>1
assert t<F(2)-1
assert F(-1,18)<0

print('PASS: conditional means, exact projection densities, Stein identities, and mode-bound failure')
