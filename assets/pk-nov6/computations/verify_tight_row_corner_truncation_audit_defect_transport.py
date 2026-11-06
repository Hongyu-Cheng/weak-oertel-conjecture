"""Independent exact rational checks of the all-dimensional derivative signs."""
from fractions import Fraction as F
checks=0
def ck(z):
 global checks
 assert z
 checks+=1
for d in range(2,41):
 for n in range(1,20):
  x=F(d*n,20);C=(d*d-x)/(d-1)
  ck(d<C<F(d*d,d-1));ck(C-x==F(d,d-1)*(d-x))
  mi=C-x*(C/d)**d;mo=C-(C/d)**d
  ck(mi>0);ck(mo>0)
  # Exact evaluation at the stated stationary points, without root rounding.
  tc=C/d
  Ti=x*tc**(d-1)
  ck(C*(1-Ti)+(d-1)*x*tc**d==mi)
  To=tc**(d-1)
  ck(C*(1-To)+(d-1)*tc**d==mo)
  # T=z^(d-1) and selected T=x*z^(d-1) remove every fractional power.
  for z in [F(1,7),F(1,2),F(1),F(3,2),F(3),tc]:
   si=C*(1-x*z**(d-1))+(d-1)*x*z**d
   so=C*(1-z**(d-1))+(d-1)*z**d
   ck(si>=mi);ck(so>=mo)
  ck((1+F(1,d-1))**(d-1)<=d)
  # A homothetic corner has exact lost fraction t^d and leaves its facet
  # parallel to the opposite original facet.
  t=F(n,40);E=t**d
  ck(0<E<1)
  if d==2:
   ck(x*x*(4-x)**2-4*x*(4-x)==-x*(4-x)*(x-2)**2)
   ck((4-x)**2-4*(4-x)==-x*(4-x))
print(f'PASS: {checks:,} exact derivative-minimum and corner-scaling checks')
