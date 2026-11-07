#!/usr/bin/env python3
"""Exact arithmetic premises for the support and equal-block obstructions."""
from fractions import Fraction as F
from math import factorial
import json

theta=F(3,32)
e_lower=sum((F(1,factorial(j)) for j in range(9)),F(0))
assert e_lower==F(109601,40320)
m0=11*e_lower/(16*(4-e_lower))
assert m0==F(1205611,826864)
bound=4*theta*((1+theta/m0)**12-1)
assert bound<F(417120,10**6)<F(458052,10**6)<m0-1
assert e_lower*F(99,100)**99>F(201,200)
assert F(60,65536)<F(1,200)
q=F(2**51,32764)
assert q==68727866368+F(1024,8191)
print(json.dumps({'status':'PASS_EXACT_OBSTRUCTION_PREMISES',
 'support_minimum_d':68727866368,
 'equal_block_method_minimum_n':52,
 'method_scope':'Current equal-block family and its existing sufficient inequalities, not arbitrary counterexamples.',
 'm0':str(m0),'N12_outer_upper':str(bound)},indent=2))
