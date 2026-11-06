"""Exact calibrations only; the analytic fixed-point theorem is proved in the note."""
from fractions import Fraction as Q
from math import factorial, comb
checks=0

def check(c):
    global checks
    assert c
    checks+=1

# Integer beta integrals, hence radial-body scale and the genuine body's
# volume coefficient after factoring out omega_q*|T_r|.
for r in range(1,10):
    for q in range(1,10):
        beta=sum(((-1)**j*Q(comb(q,j),r+j) for j in range(q+1)),Q(0))
        check(beta==Q(factorial(r-1)*factorial(q),factorial(r+q)))
        scale=r*beta
        section=q*sum(((-1)**j*Q(comb(r,j),q+j) for j in range(r+1)),Q(0))
        check(scale==section==Q(1,comb(r+q,r)))

# Canonical simplex normals balance and have exactly the required values
# at all vertices; strict paired cap excess in the valid proper regime.
for r in range(2,10):
    verts=[tuple(-1 for _ in range(r))]
    verts += [tuple(r if j==i else -1 for j in range(r)) for i in range(r)]
    normals=[tuple(1 if j==i else 0 for j in range(r)) for i in range(r)]
    normals += [tuple(-1 for _ in range(r))]
    check(all(sum(u[j] for u in normals)==0 for j in range(r)))
    for u in normals:
        values=sorted(sum(u[j]*v[j] for j in range(r)) for v in verts)
        check(values==[-1]*r+[r])
    gamma=Q(r,r+1)**r
    check(Q(r+1,r+2)**(r+1)<gamma<Q(1,2))
    for s in [Q(1,100),Q(1,7),Q(1,2),Q(3,4)]:
        paired=((r-s)**r+(r+s)**r)/((r+1)**r)
        check(paired>2*gamma)

# Scalar nonuniform-density calibration f(t)=2t, 0<=t<=1.
for x in [Q(i,100) for i in range(101)]:
    a_minus=x*x
    a_plus=1-x*x
    length=a_minus+a_plus
    first_moment=(a_plus*a_plus-a_minus*a_minus)/2
    check(length==1)
    check(first_moment/length==(1-2*x*x)/2)
check((1-2*Q(0)**2)/2>0)
check((1-2*Q(1)**2)/2<0)
print(f'PASS: {checks} exact calibrations (not a numerical proof of the analytic theorem)')
