"""Exact arithmetic certificate for the arbitrary-shape volume payment."""
from fractions import Fraction as F
from pathlib import Path
from contextlib import redirect_stdout
import io
import runpy
from functools import reduce
from operator import mul

with redirect_stdout(io.StringIO()):
    data=runpy.run_path(str(Path(__file__).resolve().parent /
        'verify_actual_thirteen_point_strict_minor_quotas_two_sided.py'))
P,w=data['P'],data['w']
checks=0
def check(test):
    global checks
    assert test
    checks+=1
check(all(3*P[7][j]==P[12][j]+P[1][j]+P[9][j] for j in range(3)))
v=w[7]; b=[w[12],w[1],w[9]]; B=F(1,100)
check(v==F(58,455))
check(b==[F(58,455),F(1179,14560),F(13,168)])
check(min(b)>B)
gap=reduce(mul,(x-B for x in b),F(1))-(7*v/11)**3
check(gap==F(1348713982727,48144144048000000)>0)
check(F(8,3)+F(5,96)==F(87,32)<F(11,4))
check(F(1,7)-v==F(1,65))
check(B-F(1,130)==F(3,1300)>0)
for d in range(1,101):
    gamma=F(d,d+1)**d
    check(F(4,11)<gamma<=F(1,2))
    check(gamma*v+B>=gamma/7+F(3,1300))
print('PASS',checks,'exact checks, plus inherited 2112 quota checks; all-dimensional inequalities are proved analytically in source')
