"""Exact supplementary arithmetic; the source supplies the continuum proofs."""
from fractions import Fraction as F
checks=0
def check(v):
    global checks
    assert v
    checks+=1
a,b=F(1),F(3,2)
M=a+b
Sigma=(a**3+b**3)/(12*M)
c2=Sigma/M
check(Sigma==F(7,48))
check(c2==F(7,120))
check(F(1,16)/c2==F(15,14))
ecrit10=F(1,2)**4*F(1,4)**6/b**3
check(ecrit10==F(1,221184))
check(ecrit10/c2**5==F(120**5,221184*7**5))
for j in range(1,25):
    q=F(3,4)+F(j,100)
    da,db=q-F(1,2),q-F(3,4)
    e10=da**4*db**6/b**3
    check(0<e10<ecrit10)
    check(da+F(1,2)==db+F(3,4)==q)
    # Relative multiplier t/t_opt=s^6 preserves its normalization.
    for s in [F(i,10) for i in range(1,31)]:
        Qa=min(a,F(1,2)+da*s**3)
        Qb=min(b,F(3,4)+db/s**2)
        check(max(Qa,Qb)>=q)
        check((max(Qa,Qb)==q)==(s==1))
for lam in [F(1),F(11,10),F(3,2),F(2),F(3)]:
    for s in [F(i,10) for i in range(1,31)]:
        Qa=min(a,F(1,2)+lam*F(1,2)*s**3)
        Qb=min(b,F(3,4)+lam*F(1,4)/s**2)
        check(max(Qa,Qb)>=1)
check(b/2> M/4)
print(f'PASS: {checks} exact checks')
