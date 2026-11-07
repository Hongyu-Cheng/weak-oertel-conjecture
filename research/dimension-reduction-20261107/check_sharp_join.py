#!/usr/bin/env python3
"""Exact scalar/source certificate for sharp-n168-d99.md.

All proof assertions use fractions.Fraction and integers. Decimal output is
for readability only. The analytic note proves the all-fibers and all-points
statements; this program certifies its fixed rational premises.
"""
import argparse
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def determinant(rows):
    a = [list(map(F, r)) for r in rows]
    ans = F(1)
    for i in range(len(a)):
        j = next((j for j in range(i, len(a)) if a[j][i]), None)
        if j is None:
            return F(0)
        if j != i:
            a[i], a[j] = a[j], a[i]
            ans = -ans
        z = a[i][i]
        ans *= z
        for j in range(i+1, len(a)):
            q = a[j][i] / z
            for k in range(i+1, len(a)):
                a[j][k] -= q * a[i][k]
    return ans


def check(variant):
    d, D, N, n, cutoff = 99, 100, 56, 168, 30
    if variant == 'original':
        delta = F(3258435, 10**8)
        delta_prime = delta + F(1, 10**10)
        epsilon = F(1, 10**14)
        requested_margin = F(38, 100000)
    else:
        delta, delta_prime, epsilon = F(4073,125000), F(325841,10**7), F(1,10**10)
        requested_margin = F(29, 100000)
    t, eta = 1-delta_prime, 1-(delta+delta_prime)/2
    theta, beta, gamma = F(5,36), F(49,108), F(99,100)**99
    p, e, q = [F(1,3)]*3, [F(1),F(0),F(0)], [F(7,12),F(5,12),F(0)]
    columns = [p,e,q]
    assert abs(determinant(list(zip(*columns)))) == theta
    cap_columns = [e,[F(2,9),F(7,9),F(0)],[F(5,12),F(0),F(7,12)]]
    assert abs(determinant(list(zip(*cap_columns)))) == beta
    fan = [[F(1),-F(2,7),-F(5,7)],[-F(5,7),F(1),-F(2,7)],[-F(2,7),-F(5,7),F(1)]]
    scores = [[sum(a*b for a,b in zip(row,v)) for v in columns] for row in fan]
    assert min(scores[0]) == 0 and max(scores[1]) == max(scores[2]) == 0
    c_shift = [F(49,39)*epsilon,-F(14,39)*epsilon,-F(35,39)*epsilon]
    assert [sum(a*b for a,b in zip(row,c_shift)) for row in fan] == [2*epsilon,-epsilon,-epsilon]
    weights = [F(3,D)-F(35,13)*epsilon,F(7,5)*epsilon,F(84,65)*epsilon]
    assert min(weights) > 0 and sum(weights)+(D-3)*F(1,D) == 1
    assert [sum(weights[k]*columns[k][j] for k in range(3)) for j in range(3)] == [F(1,D)+x for x in c_shift]
    facet_price = delta/D+(1-delta)*F(35,39)*epsilon
    facet_margin = delta_prime/D-t*F(49,39)*epsilon-facet_price
    assert 0 < delta < delta_prime < 1
    assert t < eta < 1-delta and eta*epsilon < 1
    assert facet_margin > 0
    assert F(1,D)-F(35,39)*epsilon > 0
    assert 1-cutoff*delta_prime > 0 and 1-(cutoff+1)*delta_prime < 0
    R = 3*(n+1)
    assert 2*n-R < 0 and R-2*t*epsilon > 0
    # The largest unpaid positive-fiber score occurs at k=1.
    assert delta-(1-eta) < 0
    alpha = [theta*(1-r*delta_prime)**d for r in range(1,cutoff+1)]
    assert all(0 < a < theta for a in alpha)
    mass = theta*(1+delta)**d
    outer = 3*sum((F(comb(N,r))*alpha[r-1] for r in range(1,cutoff+1)),F(0))
    surplus = 1+outer-mass
    cut_margin = gamma*mass-beta-outer/3
    assert mass > 1
    assert surplus > requested_margin and cut_margin > requested_margin
    total = (2**n-1)*mass+1+outer
    scaled_depth = gamma*mass*2**n/total
    assert scaled_depth < gamma
    # e > 65/24, so this proves that this witness still satisfies the 1/e bound.
    assert scaled_depth > F(24,65)
    return {
        'status':'PASS_EXACT_RATIONAL_SOURCE_AND_SCALAR_CERTIFICATE',
        'variant':variant,'n':n,'d':d,'block_size':N,'negative_subset_cutoff':cutoff,
        'parameters':{k:str(v) for k,v in {'delta':delta,'delta_prime':delta_prime,'epsilon':epsilon,'eta':eta,'t':t,'theta':theta,'beta':beta}.items()},
        'exact':{k:str(v) for k,v in {'m':mass,'E':outer,'Gamma':gamma,'surplus':surplus,'middle_cut_margin':cut_margin,'facet_price':facet_price,'facet_margin':facet_margin,'relative_sharp_improvement':surplus/total}.items()},
        'decimal_for_orientation_only':{k:float(v) for k,v in {'m':mass,'E':outer,'surplus':surplus,'middle_cut_margin':cut_margin,'facet_margin':facet_margin,'relative_sharp_improvement':surplus/total}.items()},
        'negative_fiber_count':str(3*sum(comb(N,r) for r in range(1,cutoff+1))),
        'scope':'Sharp Gamma_99/2^168 counterexample, not a 1/e counterexample. Source/scalar certificate supplements the full analytic proof; not Lean formalized.'
    }


if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--variant',choices=['original','simplified'],default='original')
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    result=check(args.variant)
    destination=args.output or Path(__file__).with_name('sharp-join-'+args.variant+'-certificate.json')
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],args.variant)
    print(json.dumps(result['decimal_for_orientation_only'],indent=2))
    print('Saved',destination.name)
