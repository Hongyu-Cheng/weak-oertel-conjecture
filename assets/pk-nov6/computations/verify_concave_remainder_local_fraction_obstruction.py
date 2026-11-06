from fractions import Fraction as F

# Finite exact consistency checks; the note proves every d symbolically.
# Radical-free volume identities use c^d=a and (c^2)^d=a^2.
for d in range(2,101):
    gamma=F(d,d+1)**d
    a=1-gamma
    assert F(0)<gamma<F(1,2)
    assert F(0)<a<F(1)
    middle=1-a
    endpoint=a-a*a
    total=1+2*a
    assert middle==gamma
    assert endpoint==gamma*a
    assert endpoint<middle
    assert middle<gamma*total/2
# Exact detection of the uncorrected d=4 coefficient.
d=4
gamma=F(d,d+1)**d
a=1-gamma
assert a-a**d>gamma
print('PASS: exact volume identities through d=100, strict budgets, coefficient defect')
