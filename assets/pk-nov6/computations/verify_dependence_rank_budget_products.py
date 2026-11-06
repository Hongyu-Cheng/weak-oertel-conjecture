"""Exact seed verification and product rank-cost certificates."""
from fractions import Fraction
from math import comb
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name('verify_dependence_component_rank_budget.py')))

for q in range(1,21):
    counts=[comb(q,j) for j in range(q+1)]
    assert sum(counts)==2**q
    rank_cost=sum(count*2**(3*j) for j,count in enumerate(counts))
    assert rank_cost==9**q
    assert Fraction(rank_cost,2**(3*q))==Fraction(9,8)**q

assert 9**4==6561
assert Fraction(3,2)*2**12==6144
assert 9**4-Fraction(3,2)*2**12==417
assert 9**6==531441
assert 2**19==524288
assert 9**6-2**19==7153

print('PASS: exact product components; k=12 rank cost exceeds 3/2 budget; '
      'k=18 rank cost exceeds factor-two budget; unbounded (9/8)^q ratio')
