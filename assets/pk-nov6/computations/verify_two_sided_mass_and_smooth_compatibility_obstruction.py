"""Exact algebra checks for the accompanying geometric proof.

The geometry and limiting statements are proved in the note. These finite
checks audit the cap-budget signs, the planar tangent formulas, and the
all-dimensional lower bound; they are not substitutes for those proofs.
"""
from fractions import Fraction as F
from math import comb
from random import Random

rng = Random(94731)
counts = {"planar_tangent": 0, "binomial_bound": 0,
          "signed_circuit": 0, "no_heavy": 0}

for denominator in range(3, 27):
    for numerator in range(1, denominator):
        r = F(numerator, denominator)
        a = (1 + r*r)/(1-r*r)
        s = 2*r/(1-r*r)
        tangent = (1/a, s/a)
        assert a*a - s*s == 1
        assert tangent[0]**2 + tangent[1]**2 == 1
        assert (a-tangent[0])*tangent[0] - tangent[1]**2 == 0
        assert (a-tangent[0])**2 + tangent[1]**2 == s*s
        triangle_area = tangent[1]*(a-tangent[0])
        # Disk cap = theta-s/a^2. The theta coefficient is -1.
        assert triangle_area + s/(a*a) == s
        # Coefficient vectors for pi, s, theta.
        area = (F(1), F(1), F(-1))
        perimeter = (F(2), F(2), F(-2))
        unit_ball = (F(1), F(0), F(0))
        middle = tuple((x+y+z)/4 for x,y,z in zip(area, perimeter, unit_ball))
        assert middle == (F(1), F(3,4), F(-3,4))
        assert F(3,4)/(1+F(3,4)) == F(3,7)
        counts["planar_tangent"] += 1

for d in range(2, 25):
    for numerator in range(1, 31):
        # u=(1+x)^(1/d) is chosen rational, making x rational exactly.
        u = 1 + F(numerator, 17)
        x = u**d-1
        excess = ((u+1)/2)**d - 1 - x/F(2**d)
        expansion = sum(F(comb(d,k))*(u**k-1)
                        for k in range(1,d))/2**d
        assert excess == expansion > 0
        # Any Delta1>=Delta0/2^d has nonlocal proportion >=1/(2^d+1).
        delta0 = x
        delta1 = delta0/F(2**d)
        assert delta1/(delta0+delta1) == F(1,2**d+1)
        counts["binomial_bound"] += 1

for _ in range(1000):
    caps = rng.randrange(2,8)
    points = rng.randrange(1,9)
    rho = [F(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(caps)]
    slopes = [F(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(caps)]
    xi = [F(rng.randrange(-10,11),rng.randrange(1,10)) for _ in range(points)]
    incidence = [[F(rng.randrange(2)) for _ in range(points)] for _ in range(caps)]
    weights = [r/s for r,s in zip(rho,slopes)]
    kappa = [w/sum(weights) for w in weights]
    g = [sum(x*i for x,i in zip(xi,row)) for row in incidence]
    response = sum(k*x for k,x in zip(kappa,g))
    shifts = [(x-response)/s for x,s in zip(g,slopes)]
    assert sum(r*b for r,b in zip(rho,shifts)) == 0
    assert all(x-s*b == response for x,s,b in zip(g,slopes,shifts))
    A = [sum(k*row[i] for k,row in zip(kappa,incidence)) for i in range(points)]
    assert sum(a*x for a,x in zip(A,xi)) == response
    beta = F(rng.randrange(1,30),30)
    assert response-beta*sum(xi) == sum((a-beta)*x for a,x in zip(A,xi))
    counts["signed_circuit"] += 1

for n in range(1,19):
    for d in range(2,20):
        V=F(1)
        original_mass=3*2**(n-1)*V
        delta0=F(1,5)
        delta1=delta0/F(2**d)
        assert V < original_mass/F(2**n)
        assert V+delta0 < (original_mass+delta0+delta1)/F(2**n)
        counts["no_heavy"] += 1

print("PASS", counts, "total", sum(counts.values()))
