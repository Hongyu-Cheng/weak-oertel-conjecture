from fractions import Fraction as F
from itertools import product

n=0
def check(p):
    global n
    assert p
    n+=1

P=(-1,0,1)
radii={-1:F(1),0:F(2),1:F(1)}
zeros=[(F(2),F(1),F(0)),(F(2),F(-1),F(0)),(F(2),F(0),F(0))]
A1=[(F(2),F(1),F(1))]+zeros
A2=[(F(2),F(-1),F(1))]+zeros
e=F(1,100)
for i,j in product(range(11),repeat=2):
    t1,t2=F(i,4),F(j,4)
    tuples=[((a[0]+b[0])/2,(a[1]+b[1])/2,t1*a[2]+t2*b[2])
            for a,b in product(A1,A2)]
    new={z:min([radii[z]]+[c+s*z-e*v for c,s,v in tuples]) for z in P}
    expected={-1:1-e*t1,0:2-e*(t1+t2),1:1-e*t2}
    check(new==expected)
    check(new[-1]+new[1]<=2*new[0])
    check(sum(2*radii[z]-2*new[z] for z in P)==4*e*(t1+t2))
    # Closed ambient cap x+z>=0; its interval length is clipped exactly.
    mass=lambda rad: sum(max(F(0),rad[z]-max(-rad[z],F(-z))) for z in P)
    check(mass(radii)-mass(new)==e*(t1+3*t2))
    for z in P:
        active=[v for c,s,v in tuples if c+s*z==radii[z]]
        old1=max([v for c,s,v in A1 if c+s*z==radii[z]])
        old2=max([v for c,s,v in A2 if c+s*z==radii[z]])
        check(max(active)==t1*old1+t2*old2)

print(f'PASS: {n} exact checks')
