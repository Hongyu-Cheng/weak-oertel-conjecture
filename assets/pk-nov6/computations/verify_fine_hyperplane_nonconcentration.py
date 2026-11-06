"""Exact arithmetic calibrations for hyperplane nonconcentration."""
from fractions import Fraction as F
from itertools import product


for r in range(1,8):
    # Rectangular lattices: rho^2=sum lengths^2/4 and dual minimum=1/max.
    for lengths in [list(map(F,range(1,r+1))),[F(1,r+1)]*r,[F(2**j) for j in range(r)]]:
        rho_sq=sum(a*a for a in lengths)/4
        dual_sq=1/max(lengths)**2
        elementary_C=F(r**(r+1),2)
        assert rho_sq*dual_sq<=elementary_C**2

    # A cube grid has maximum hyperplane fraction 1/(2N+1):
    # solve a hyperplane equation for any coordinate with nonzero coefficient.
    for N in range(1,10):
        total=(2*N+1)**r
        max_plane=(2*N+1)**(r-1)
        xi=F(max_plane,total)
        assert xi==F(1,2*N+1)
        # Fine projection is in radius sqrt(r) N; square the bound.
        bound_sq=F(r**(2*r+2))*r*N*N*(xi/(1-xi))**2
        assert F(r,4)<=bound_sq

# Exact rank-one three-slice obstruction and sharp counting-to-mesh equality.
xi=F(1,3)
R=F(1)
rho=F(1,2)
assert rho==R*xi/(1-xi)
assert xi<F(1,2)
for h in [F(1,7),F(1,100),F(3,17)]:
    coarse=2*h
    fine=3*h
    assert coarse/fine==F(2,3)
    A=1/h
    assert A*h/2==rho

# The coupled-normal factor J is attained by an actual narrow diagonal tube.
for J in range(2,31):
    eps=F(1,3)
    fine=[(z,u) for z in range(J) for u in range(-1,J+1)
          if abs(F(u-z))<=eps]
    assert fine==[(z,z) for z in range(J)]
    eta_u=F(max(sum(u==t for z,u in fine) for t in range(J)),len(fine))
    eta_coupled=F(sum(u-z==0 for z,u in fine),len(fine))
    assert eta_u==F(1,J) and eta_coupled==J*eta_u==1

# Exact block section/covolume conversion in both normalizations.
for r,s in [(1,0),(1,2),(2,1),(3,3)]:
    for source_mass,total_mass,v in [(F(2,7),F(9,7),F(1,11)),(F(3),F(20),F(1,100))]:
        # Arbitrary fine-block determinant, with the continuous determinant
        # fixed by the required full determinant. The s=0 case fixes detC=1.
        detA=1/source_mass if s==0 else F(5,3)
        detC=F(1) if s==0 else 1/(source_mass*detA)
        assert v*detA*detC==v/source_mass
        scalar_power=source_mass/total_mass
        assert scalar_power*detA*detC==1/total_mass

print("PASS: lattice calibrations, quantitative mesh bounds, coupled-normal factor, block Jacobians, and three-slice obstruction.")
