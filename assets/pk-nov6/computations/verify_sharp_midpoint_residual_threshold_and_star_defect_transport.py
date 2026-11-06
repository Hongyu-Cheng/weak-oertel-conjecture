"""Exact rational diagnostics for the sharp threshold theorem and forest limit."""
from fractions import Fraction as F

checks = 0
assert F(3, 2)-(2-F(3, 2)) == 1
assert F(5, 4)**2-(2-F(5, 4))**2 == 1
assert 1-(F(5, 4)/2)**2 == F(39, 64)
assert F(39, 64)>F(1, 2)>F(4, 9)
checks += 4
for d in range(1, 81):
    gamma = F(d, d+1)**d
    assert gamma>F(1, 3)
    if d>=2:
        assert F(5, 4)**d-F(3, 4)**d>=1
        assert 1-F(5, 8)**d>=F(39, 64)>gamma
        assert 2**d*(1-gamma)>2**(d-1)
        checks += 3
    t = 1+F(1, 4*d)
    a = 2-t
    assert t**d<1+a**d
    assert a**d+t**d>=2
    residual = t/4
    p = 1-residual**d
    assert 0<p<1
    assert t/2-residual==t/4
    checks += 5

for d in range(2, 13):
    gamma = F(d, d+1)**d
    for count in [2, 3]:
        n = 40*d*count
        volumes = [F(k, n)**d for k in range(n+1)]
        total = sum(volumes, F(0))
        assert total>=F(n, d+1)>2
        assert max(volumes)<total/2
        checks += 2
        incoming = F(0)
        for j in range(1, 2*count+1):
            i = -n//2+j
            m = n+i
            c = F(m, n)
            opposite = 2*c-1
            assert 0<opposite and c<=F(1, 2)+F(1, 20*d)
            # Strict row failure without evaluating an algebraic root.
            assert (2*c)**d*(1-gamma)<1
            assert 1>c**d+opposite**d
            cap = sum(volumes[:m], F(0))+gamma*c**d
            assert cap/total<F(30983, 192000)<F(1, 6)<gamma/2
            assert 1>2**d*(1-gamma)*c**d
            incoming += c**d
            checks += 5
        assert incoming>F(2*count, 2**d)
        checks += 1

print(f"PASS: {checks} exact threshold, growth, cap-budget, and star checks")
