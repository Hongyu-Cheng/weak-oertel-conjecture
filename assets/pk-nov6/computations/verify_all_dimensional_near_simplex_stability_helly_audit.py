"""Independent exact arithmetic audit of the all-d finite stability proof."""
from fractions import Fraction as F
from math import prod

gauge_checks=strip_checks=budget_checks=candidate_checks=locality_checks=0
for d in range(2,31):
    m=d+1
    Gamma=F(d,m)**d
    c=(1-F(1,d**(d-1)))/((d-1)**2*m)
    assert 0<c<1
    C=8*m
    eta=min(F(1,8*m),Gamma*c/(4*C*2**(d+1)))
    E=C*eta*2**(d+1)
    assert 0<E<=Gamma*c/4
    delta=min(F(1,4),c/(4*d))
    assert eta/(1-delta)<=F(1,4*m)
    assert (1-delta)**d>=1-c/4
    assert (1-c)/(1-c/4)<=1-3*c/4
    assert Gamma*(1-c)*(1-delta)**(-d)+E<=Gamma*(1-c/2)
    budget_checks+=1
    for i in range(1,31):
        rho=1+delta/(1-delta)*F(i,30)
        f=rho-1;w=1-rho**(-d)
        assert w/f==sum(rho**(-a) for a in range(1,d+1))
        assert d*(1-delta)**d*f<=w<=d*f
        gauge_checks+=1
    k=d-1;b=F(1,m);r=F(1,4)*min(b,(1-b)/k)
    assert r==F(1,4*m)
    for i in range(-10,11):
        t=b+r*F(i,10)
        assert 0<t-r<t+r<1
        x=r/(1-t)
        assert x<=F(1,4*k-1)
        assert (1-x)**(k-1)>F(1,2)
        assert ((1-t)/(1-t-r))**(k-1)<2
        strip_checks+=1
    B=F(2**d)/Gamma
    tau=min(Gamma/2,Gamma*c/(4*B),d*delta)/11
    for pattern in range(11):
        raw=[F((i+1)*(pattern+3)%17,17) for i in range(m)]
        scale=min(F(1),m*Gamma*(1-c/2)/max(sum(raw),F(1,100)))
        L=[tau*scale*x for x in raw]
        mean=sum(L)/m
        assert all(0<=li<=tau for li in L)
        assert mean<=Gamma*(1-c/2)*tau
        shifts=[(mean-li)/(m*Gamma) for li in L]
        lam=[b+z for z in shifts]
        assert sum(lam)==1
        assert all(x>=b/2>delta/m for x in lam)
        for i in range(m):
            vertex=d**d*prod(lam[j] for j in range(m) if j!=i)
            assert vertex>=Gamma-m*Gamma*shifts[i]-B*tau*tau
            assert vertex-L[i]>=Gamma-mean-B*tau*tau
        bound=Gamma-Gamma*(1-c/2)*tau-B*tau*tau
        assert bound/(1-tau)-Gamma>=Gamma*c*tau/4
        candidate_checks+=1
    large=8*(d+1)**3
    delta_d=min(delta,tau/d)
    eps=min(F(1,64*(d+1)**3),delta_d/(d*(d+1)*(large+1)))
    assert eps<=F(1,64*d**3)
    assert 8*d**3*eps<=large*eps
    assert -delta_d/F(d*(d+1))+large*eps<=-eps
    locality_checks+=1

print(f'PASS: {gauge_checks} exact gauge identities, {strip_checks} strip constants, '
      f'{budget_checks} loss budgets, {candidate_checks} balanced candidate/product '
      f'checks, {locality_checks} locality conversions (dimensions2..30).')
