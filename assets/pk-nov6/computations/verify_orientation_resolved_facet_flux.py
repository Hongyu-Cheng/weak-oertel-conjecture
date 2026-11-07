from fractions import Fraction as F

for h in [F(k, 13) for k in range(-100, 101)]:
    delta = max(F(0), -h, h-1)
    empty = max(h-1, 0)-min(h, 0)
    full = min(h-1, 0)-max(h, 0)
    assert empty == delta
    assert full == -1-delta

for n in range(1, 11):
    proper = 3**n
    supporting = 5**n-proper
    exterior = 2*5**(n-1)*F(1, 2)
    assert exterior == 5**(n-1)
    assert proper+supporting+exterior == 6*5**(n-1)>0
    assert (proper <= exterior) == (n>=4)

print('PASS: oriented flux identities and exact opposite-cap obstruction')
