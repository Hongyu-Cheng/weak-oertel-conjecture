"""Exact finite-base entropy identities and certified scalar calibrations."""
from fractions import Fraction as F
from itertools import product

checks=0
def check(ok):
    global checks
    assert ok
    checks+=1

# Generate exact stationary denominators, with balanced escort masses.
for N in range(1,9):
    for w,c,j in product([F(1,3),F(1),F(7,2)],
                          [F(1,2),F(2),F(9)],range(-5,6)):
        alpha=F(j,6)
        L=[1-alpha,F(1),1+alpha]
        escort=[w,c,w]
        masses=[e*l**(N+1) for e,l in zip(escort,L)]
        E=c+2*w
        check(sum(m/l**N for m,l in zip(masses,L))==E)
        check(sum(m/l**(N+1) for m,l in zip(masses,L))==E)
        check(-masses[0]/L[0]**(N+1)+masses[2]/L[2]**(N+1)==0)
        T=c+2*min(masses[0],masses[2])
        D=c+min(masses[0],masses[2])
        check(E>=T>=D)
        tangent_defect=sum(m*(l**(-N)-max(F(0),1-N*(l-1))) for m,l in zip(masses,L))
        check(E-T>=tangent_defect>=0)
        check((E==T)==(alpha==0))
        check(E<=sum(masses))
        factor=min(L)**(N+1)
        check(all(factor*e<=m for e,m in zip(escort,masses)))
        check(factor*E<=T)

# Exact Holder-dual comparisons: all powers are rational because masses
# and unnormalized test probabilities are integer powers of rationals.
roots=[F(1,2),F(1),F(2),F(3)]
for N in range(1,7):
    D=N+1
    for a,b,c,t,w in product(roots,roots,roots,roots,roots):
        E=b**D+2*((a+c)/2)**D
        Z=2*t**D+w**D
        dual=((a+c)*t**N+b*w**N)**D/Z**N
        check(dual<=E)
    for a,b,c in product(roots,repeat=3):
        t=(a+c)/2
        w=b
        Z=2*t**D+w**D
        dual=((a+c)*t**N+b*w**N)**D/Z**N
        check(dual==Z)

# The actual compatible triangle example, in units of |T|.
N=3
m=[F(1),F(9),F(16)]
L=[F(2,3),F(1),F(4,3)]
e=[x/l**4 for x,l in zip(m,L)]
E=sum(x/l**3 for x,l in zip(m,L))
check(e==[F(81,16),F(9),F(81,16)])
check(E==F(153,8))
check(E>16>1)
check([x/E for x in e]==[F(9,34),F(8,17),F(9,34)])
check(F(16,81)*E==F(34,9)<13)
check(F(52,9)-5==F(7,9))
check(F(64,9)-F(52,9)==F(4,3))
check(F(4,9)*E==F(17,2)>5)
check(sum(x*(l**(-3)-max(F(0),1-3*(l-1))) for x,l in zip(m,L))==E-11==F(65,8))

# Five strictly convex lattice vertices: every minimal face is singleton.
P=[(0,0),(2,0),(3,1),(1,3),(0,2)]
for i in range(5):
    a,b,c=P[i],P[(i+1)%5],P[(i+2)%5]
    check((b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])>0)
check(F(1)<F(5,4))
print(f"PASS: {checks:,} exact checks")
