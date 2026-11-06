"""Exact identities and rational checks; the source contains the proof."""
from fractions import Fraction as F
import random
import sympy as s

checks = 0


def check(x):
    global checks
    assert x
    checks += 1


p, q, U, V = s.symbols('p q U V', positive=True)
D = p + q - 2*p*q
f_i2 = 4*p*p*(1-q)/D
f_j2 = 4*q*q*(1-p)/D
prod = 8*p*q*(1-p)*(1-q)/D
C = 8 + prod
ff = p*(1-q)/D
gg = q*(1-p)/D
rr = ff*gg*(1-p)*(1-q)/(1-p*q)
A = 1 + (2*f_i2+prod)*f_i2/(4*C*(p*U)**2) - f_i2/(2*p*U)
B = 1 + (2*f_j2+prod)*f_j2/(4*C*(q*V)**2) - f_j2/(2*q*V)
check(s.factor(A - ((U-ff)**2+rr)/U**2) == 0)
check(s.factor(B - ((V-gg)**2+rr)/V**2) == 0)

f, u, v = s.symbols('f u v', real=True)
ell = u+v-1
AA = ((u-f)**2+f*(1-f))/u**2
BB = ((v-1+f)**2+f*(1-f))/v**2
Z = (1-v)**2*AA+(1-u)**2*BB-ell**2*(AA+BB-1)
check(s.factor(Z + 2*(u-1)*(v-1)*(f*u-f*v+u*v-u)/(u*v)) == 0)
check(s.factor(Z**2 - 4*(1-u)**2*(1-v)**2*AA*BB
               + 4*f*(1-f)*(1-u)**2*(1-v)**2*ell**2/(u*u*v*v)) == 0)


def disk_check(U, V, F0, R):
    L = U+V-1
    A = ((U-F0)**2+R)/U**2
    B = ((V-1+F0)**2+R)/V**2
    Z = (1-V)**2*A+(1-U)**2*B-L*L*(A+B-1)
    cross_square = 4*(1-U)**2*(1-V)**2*A*B
    check(Z > 0 or (Z == 0 and cross_square > 0)
          or (Z < 0 and cross_square > Z*Z))


random.seed(940031)
for _ in range(2000):
    U = F(random.randrange(1, 100), 100)
    V = F(random.randrange(1, 100), 100)
    if U+V <= 1:
        continue
    F0 = F(random.randrange(1, 100), 100)
    R = F0*(1-F0)*F(random.randrange(11), 10)
    disk_check(U, V, F0, R)

# Actual triangle data: rational cubic-boundary vectors and all positive
# signed-row realizations from a finite barycentric source grid.
for fv in [[F(1), F(1), F(1)],
           [F(7, 4), F(1, 2), F(1, 2)],
           [F(6, 5), F(66, 65), F(10, 13)]]:
    c = [z/2 for z in fv]
    w = [1-c[1]**2, c[0]+c[1]*c[2], c[2]+c[0]*c[1]]
    uu = [c[i]*w[(i+1) % 3]/w[i] for i in range(3)]
    dd = [F(0)]*3
    for i in range(3):
        dd[(i+1) % 3] = sum(uu)-1-uu[i]
    slack = 1-sum(abs(z) for z in dd)
    for x in range(1, 9):
        for y in range(1, 10-x):
            weight = [F(x, 10), F(y, 10), F(10-x-y, 10)]
            ss = [abs(dd[i])+slack*weight[i] for i in range(3)]
            aa = [(1-dd[(i+1) % 3]+dd[(i+2) % 3]-ss[i])/2
                  for i in range(3)]
            bb = [[F(0)]*3 for _ in range(3)]
            for i in range(3):
                bb[i][(i+1) % 3] = (ss[i]+dd[i])/2
                bb[i][(i+2) % 3] = (ss[i]-dd[i])/2
            P = fv[0]*fv[1]*fv[2]
            C0 = 8+P
            E = [2*z*z+P for z in fv]
            At = [C0+E[i]*fv[i]**2/(4*aa[i]**2)
                  - C0*fv[i]**2/(2*aa[i]) for i in range(3)]
            for i in range(3):
                j = (i+1) % 3
                p0 = aa[i]+bb[i][j]
                q0 = aa[j]+bb[j][i]
                D0 = p0+q0-2*p0*q0
                F0 = p0*(1-q0)/D0
                G0 = 1-F0
                R = F0*G0*(1-p0)*(1-q0)/(1-p0*q0)
                U0, V0 = aa[i]/p0, aa[j]/q0
                check(F(0) < R < F0*G0)
                check(At[i]/C0 == ((U0-F0)**2+R)/U0**2)
                check(At[j]/C0 == ((V0-G0)**2+R)/V0**2)
                disk_check(U0, V0, F0, R)

print(f'PASS: {checks} exact disk, derivative, and actual triangle checks')
