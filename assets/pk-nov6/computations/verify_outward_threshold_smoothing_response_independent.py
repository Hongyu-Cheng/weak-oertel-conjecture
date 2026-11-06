"""Exact rational checks for the uniform-kernel response and facet linkage."""
from fractions import Fraction as F
from random import Random

rng=Random(92173)
checks=0

def clamp(x):
    return max(F(0),min(F(1),1+x))

# Uniform kernel integrated on [0,1], at either side of its upper endpoint.
# Choose width <=1/2, so the other endpoint never participates in the layer.
for den in range(2,25):
    h=F(1,den)
    for num in range(-3*den,3*den+1):
        s=F(num,den)
        if s < -1 or s > 2:
            continue
        w=clamp(-s)
        outside_section=max(F(0),min(F(1),1-s))
        inside_section=max(F(0),min(F(1),s))
        assert outside_section==w
        assert inside_section==1-w
        assert clamp(-s)+clamp(-1+s)==1
        checks+=3

# Reconstruct the exact physical separator coefficient from group equalization.
for trial in range(300):
    d=rng.randint(1,8); N=d+1
    M=F(rng.randint(2,20)); beta=F(rng.randint(1,7),10)
    D=F(rng.randint(-5,5),3)
    groups=[]
    for i in range(3):
        raw=[rng.randint(1,9) for _ in range(rng.randint(1,4))]
        rho=[F(x,sum(raw)) for x in raw]
        S=[F(rng.randint(1,9),3) for _ in raw]
        Aj=[-F(rng.randint(0,9),100) for _ in raw]
        Bj=[F(rng.randint(-9,9),5) for _ in raw]
        Jj=[F(rng.randint(-9,9),7) for _ in raw]
        B=sum(r/s for r,s in zip(rho,S))
        groups.append(dict(rho=rho,S=S,Aj=Aj,Bj=Bj,Jj=Jj,B=B,
                           b=F(rng.randint(1,9),20),E=F(rng.randint(1,9)),
                           V=F(rng.randint(1,9)),CE=F(rng.randint(-9,9),4),
                           Dp=F(rng.randint(-9,9),6)))
    raw=[rng.randint(1,9) for _ in groups]
    lam=[F(x,sum(raw)) for x in raw]
    lhs=-beta*D; rhs=-beta*D; Delta=F(0); Abar=F(0); omega_total=F(0)
    for la,g in zip(lam,groups):
        k=la/g['B']; e=k*g['b']; Delta+=e
        alpha=g['b']*(g['CE']/(N*g['E'])+g['Dp']/(d*N*g['V'])
             +sum(r*j for r,j in zip(g['rho'],g['Jj']))/(2*M)
             -F(d+2,2*d)*D/M)
        capterm=F(0)
        rhs+=e*(g['CE']/(N*g['E'])+g['Dp']/(d*N*g['V']))
        for r,S,A,B,J in zip(g['rho'],g['S'],g['Aj'],g['Bj'],g['Jj']):
            om=k*r/S; omega_total+=om; Abar+=om*A
            capterm+=r*(B+A*(D-J)/(2*M))/S
            rhs+=om*B+(e*r-om*A)*J/(2*M)
            assert e*r-om*A>=0
            checks+=1
        lhs+=la*(alpha+capterm)/g['B']
    rhs-=F(d+2,2*d)*Delta*D/M
    rhs+=Abar*D/(2*M)
    assert omega_total==1
    assert lhs==rhs
    checks+=2

# Uniform-kernel positive-support concavity, and the forbidden zero-extension claim.
for _ in range(1000):
    x=F(rng.randint(-40,40),20); y=F(rng.randint(-40,40),20)
    t=F(rng.randint(0,20),20)
    g=lambda z:F(3,2)-z*z+F(1,3)*z
    tau=lambda z:min(F(1),max(F(0),g(z)))
    if g(x)>0 and g(y)>0:
        assert tau((1-t)*x+t*y)>=(1-t)*tau(x)+t*tau(y)
        checks+=1
assert max(F(0),1-F(1)) < (max(F(0),1-F(0))+max(F(0),1-F(2)))/2
checks+=1
print(f'Uniform-threshold response: {checks} exact checks PASS')
