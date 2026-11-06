"""Exact symbolic derivatives and rational physical paths for fixed cap budgets."""
import sympy as S
from fractions import Fraction as Q

z = S.symbols("x0 y0 x1 y1 x2 y2")
vertices = list(zip(z[::2], z[1::2]))
reference = dict(zip(z, (0,0,1,0,0,1)))
area = S.det(S.Matrix([[1,x,y] for x,y in vertices]))/2
c = [
    [S.Rational(2,3)-x-y for x,y in vertices],
    [x-S.Rational(1,3) for x,y in vertices],
    [y-S.Rational(1,3) for x,y in vertices],
]
caps = [area*c[i][i]**2/S.prod(c[i][i]-c[i][j]
                              for j in range(3) if j != i)
        for i in range(3)]
G = S.Matrix([[S.diff(f,x).subs(reference) for x in z] for f in caps])
expected_G = S.Matrix([[-4,-4,0,-2,-2,0],
                       [0,-2,4,0,2,2],
                       [-2,0,2,2,0,4]])/9
assert G == expected_G
lagrangian = area-S.Rational(3,4)*sum(caps)
assert all(S.diff(lagrangian,x).subs(reference) == 0 for x in z)
H = S.hessian(lagrangian,z).subs(reference)
p,q,r = S.symbols("p q r")
delta = S.Matrix([p/2-q/2+r,-p-r,-p/2-q/2-r,p,q,r])
assert G*delta == S.zeros(3,1)
assert G.rank() == 3
assert S.expand((delta.T*H*delta)[0]
                +((p+q+r)**2+2*(p-q)**2+3*r*r)/8) == 0
v = S.Matrix([1,1,0,0,0,0])
assert (v.T*H*v)[0] == S.Rational(1,3)

t = S.symbols("t")
shift = t*t/3
length = 1+S.Rational(7,18)*t*t
F0 = sum(length*(S.Rational(2,3)-2*k)**2/(2*(length-2*k))
         for k in (shift+t,shift-t))
F1 = sum((length-2*k)*(length-S.Rational(1,3))**2/(2*(length-k))
         for k in (shift+t,shift-t))
gap0 = (4*t*t*(35*t**6-1303*t**4-2892*t*t+108)/
        (9*(5*t*t-36*t-18)*(5*t*t+36*t-18)))
gap1 = (t*t*(245*t**6+36120*t**4+105948*t*t+7776)/
        (324*(t*t-18*t+18)*(t*t+18*t+18)))
assert S.cancel(S.Rational(4,9)-F0-gap0) == 0
assert S.cancel(S.Rational(4,9)-F1-gap1) == 0
assert S.expand(length*(length-2*shift)-1-t*t/9+35*t**4/324) == 0
assert Q(108)-Q(2892,100)-Q(1303,10000) == Q(789497,10000) > 0

checks = 0
for denominator in range(10,101):
    a = Q(1,denominator)
    b = a*a/3
    L = 1+Q(7,18)*a*a
    assert b+a < Q(1,3) < L
    assert L > Q(2,3) and L-2*(b+a)>0
    mass = L*(L-2*b)
    c0 = sum(L*(Q(2,3)-2*k)**2/(2*(L-2*k)) for k in (b+a,b-a))
    c1 = sum((L-2*k)*(L-Q(1,3))**2/(2*(L-k)) for k in (b+a,b-a))
    assert mass > 1 and c0 < Q(4,9) and c1 < Q(4,9)
    checks += 1
    if denominator == 10:
        assert mass == Q(648713,648000)
        assert c0 == Q(685451117,1546212500)
        assert c1 == Q(923058069551,2080858248000)
print(f"PASS: symbolic cap gradients/Hessians, exact critical-tangent square form, "
      f"rational gap factorizations, and {checks} actual improving two-fiber paths")
