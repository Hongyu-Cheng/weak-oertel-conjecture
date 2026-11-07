#!/usr/bin/env python3
"""Replay the new n=52 parameters with the independent log/exp enclosure.

The power algorithm is imported from the separately authored integration
audit, not from this directory's binary-power parameter checker. All
acceptance predicates are exact fractions. The geometric specialization is
proved in improved-n52.md and independently reviewed in this directory.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import importlib.util
import json


def main():
    here = Path(__file__).resolve().parent
    source = here.parents[1] / 'scripts' / 'check_one_over_e_independently.py'
    spec = importlib.util.spec_from_file_location('independent_taylor_audit', source)
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    power = audit.power_interval
    n, N, h, ell = 52, 13, 2747786, 1350000000000000000
    theta, beta = F(3,32), F(27,64)
    s, t, q = F(500000001,10**9), F(999999997,10**9), F(1000001,2000000)
    pl, ph = power(2*q,h)
    ml, mh = theta*(2*s)**3*pl, theta*(2*s)**3*ph
    El = Eh = F(0)
    for r in range(1,N+1):
        lo, hi = power(1-r*(2*q-1),h)
        factor = 4*comb(N,r)*theta*(1-r*(1-t))**3
        El += factor*lo
        Eh += factor*hi
    mlo, mhi = F(1463251505373,10**12), F(1463251505374,10**12)
    Elo, Ehi = F(465699293757,10**12), F(465699293758,10**12)
    assert mlo < ml <= mh < mhi
    assert Elo < El <= Eh < Ehi
    el, eh = audit.exp_nonnegative_interval(F(1),F(1))
    gl, gh = power(F(ell,ell+1),ell)
    Wl = (2**n-1)*ml+1+El
    middle_upper = (beta+Eh/4)/Wl
    exposed_upper = gh*mh/Wl
    uniform_upper = max(middle_upper,exposed_upper)
    relative_gap = 1-eh*2**n*uniform_upper
    absolute_gap = 1/(eh*2**n)-uniform_upper
    padding = 1+El-mh-2**n*mh/(2*ell-1)
    assert relative_gap > 0 and absolute_gap > 0 and padding > 0
    report = {
        'status': 'PASS_INDEPENDENT_RATIONAL_TAYLOR_ENCLOSURE',
        'method': 'Rational log/exp Taylor intervals from scripts/check_one_over_e_independently.py; no binary-power enclosure from the new checker is used.',
        'n': n, 'd': str(3+h+ell), 'h': h, 'ell': str(ell),
        'm_interval': list(map(str,(ml,mh))),
        'E_interval': list(map(str,(El,Eh))),
        'Gamma_ell_interval': list(map(str,(gl,gh))),
        'e_interval': list(map(str,(el,eh))),
        'uniform_normalized_depth_upper': str(uniform_upper),
        'relative_violation_lower': str(relative_gap),
        'absolute_violation_lower': str(absolute_gap),
        'padding_margin_lower': str(padding),
        'display': {key: audit.decimal(value) for key,value in {
            'm': (ml+mh)/2, 'E': (El+Eh)/2,
            'relative_violation_lower': relative_gap,
            'absolute_violation_lower': absolute_gap,
            'padding_margin_lower': padding,
        }.items()},
        'scope': 'Independent arithmetic replay of the new parameter specialization. Geometry is proved and separately reviewed; not Lean-formalized.'
    }
    output = here/'improved-n52-independent-taylor.json'
    output.write_text(json.dumps(report,indent=2)+'\n')
    print(report['status'])
    print(json.dumps(report['display'],indent=2))


if __name__ == '__main__':
    main()
