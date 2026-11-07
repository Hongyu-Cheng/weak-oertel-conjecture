"""Exact checks of the common-normal AM-GM and saturated cap comparison."""
from fractions import Fraction as F

checks = 0
for d in range(2, 9):
    for gaps in [list(range(1, d+1)), [1]*(d-1)+[3], [2]*d]:
        peak = F(sum(gaps), d+1)
        product = F(1)
        for gap in gaps:
            product *= gap
        coefficient = (F(d, d+1)/peak)**d
        assert coefficient <= 1/product
        checks += 1
        for radius in [F(1, 3), F(1), F(5, 2)]:
            for height in [F(0), radius*min(gaps)/3,
                           radius*min(gaps), radius*max(gaps)*2]:
                if 0 < height <= radius*min(gaps):
                    original = height**d/product
                    replacement = min(radius**d, coefficient*height**d)
                    assert replacement <= original
                    checks += 1
print(f'PASS {checks} exact AM-GM and saturated replacement checks')
