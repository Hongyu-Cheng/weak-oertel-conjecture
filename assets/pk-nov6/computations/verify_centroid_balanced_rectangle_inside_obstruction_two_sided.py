"""Exact identity and actual finite-cap checks for the centroid obstruction."""
from fractions import Fraction as F
import sympy as S

checks = 0
def ck(condition):
    global checks
    assert condition
    checks += 1

rr = S.symbols('r0:5')
hh = S.symbols('h0:5')
b, delta = S.symbols('b delta')
bases = [-2, -1, 0, 1, 2]
B = sum(j*r*h for j, r, h in zip(bases, rr, hh))
Q = 2*rr[0]*hh[0]+rr[1]*(hh[1]+b+delta)+rr[2]*(hh[2]+delta)+rr[3]*(hh[3]-b+delta)
R = 2*rr[3]*hh[3]+2*rr[4]*hh[4]+rr[2]*(hh[2]+delta)
ck(S.expand(R-Q-B+b*(rr[1]-rr[3])+delta*(rr[1]+rr[3])) == 0)

r = [F(1), F(51, 50), F(51, 50), F(203, 200), F(101, 100)]
d = F(1, 4000)
a = (F(3, 200)-F(403, 40)/8000)/F(409, 200)
H = [1-d*j/2+a*v for j, v in zip(bases, [0, 3, 2, 1, 0])]
ck(a == F(4397, 654400))
ck(H == [F(4001, 4000), F(834591, 818000), F(331597, 327200),
         F(411697, 409000), F(3999, 4000)])
ck(all(H[i+1]-H[i] >= H[i+2]-H[i+1] for i in range(3)))
ck(all(r[i+1]-r[i] >= r[i+2]-r[i+1] for i in range(3)))
ck(sum(j*width*height for j, width, height in zip(bases, r, H)) == 0)
M = 2*sum(width*height for width, height in zip(r, H))
ck(M == F(835355607, 81800000))
for lo in range(5):
    for hi in range(lo, 5):
        if lo == 0 and hi == 4:
            continue
        k = len({v % 2 for v in bases[lo:hi+1]})
        ck(2*sum(r[i]*H[i] for i in range(lo, hi+1)) < k*M/2)

def mass(tilt):
    return sum(width*max(F(0), min(2*height, height+tilt*j+d))
               for j, width, height in zip(bases, r, H))

Q = mass(-F(1, 2))
R = mass(F(2))
ck(Q == F(1668671531, 327200000))
ck(R == F(416921767, 81800000))
ck(R-Q == -F(2407, 800000))
ck(R-Q == -F(1, 2)*(r[1]-r[3])-d*(r[1]+r[3]))
ck(H[0] == 1+d and H[4] == 1-d)
ck(all(abs(-F(j, 2)+d) < H[i] for i, j in enumerate(bases) if abs(j) <= 1))
for j, height in zip(bases, H):
    if j < 0:
        ck(2*j+d < -height)
    elif j > 0:
        ck(2*j+d > height)
    else:
        ck(d < height)
for den in [10000, 100000, 1000000]:
    h = F(1, den)
    ck((mass(-F(1, 2)-h)-Q)/h == r[1]-r[3])
    ck((mass(-F(1, 2)+h)-Q)/h == 2*r[4]-2*r[0]+r[3]-r[1])
print(f'PASS: {checks} exact checks')
