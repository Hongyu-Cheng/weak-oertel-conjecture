from fractions import Fraction as F

delta = F(1, 100)
small = F(1, 5) + F(16, 5) * delta**2
assert small < F(13, 45)
assert 3**2 < 13 < 4**2
assert delta < F(1, 6) < F(1, 3) < F(1, 2)
assert 57**2 < 16**2 * 13

# Reduce the equality and cap value using s^2=13 and t=(s-2)/6.
# The pair (a,b) denotes a+b*s.
def add(x, y):
    return x[0] + y[0], x[1] + y[1]

def mul(x, y):
    return x[0]*y[0] + 13*x[1]*y[1], x[0]*y[1] + x[1]*y[0]

def scale(c, x):
    return c*x[0], c*x[1]

t = (-F(1, 3), F(1, 6))
assert add(add(scale(3, mul(t, t)), scale(2, t)), (-F(3, 4), F(0))) == (0, 0)
left = scale(F(4, 5), mul(add((F(1), F(0)), scale(-1, t)), add((F(1), F(0)), scale(-1, t))))
right = add((F(1, 5), F(0)), scale(F(16, 5), mul(t, t)))
assert left == right == (F(77, 45), -F(16, 45))
print('PASS: exact radical cap balance, full-component threshold bounds, and strict Gamma gap')
