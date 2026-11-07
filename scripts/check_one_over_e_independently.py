#!/usr/bin/env python3
"""Independent rational audit of the n=76 and n=52 Oertel witnesses.

Run from the repository root:
    python3 -B scripts/check_one_over_e_independently.py --output reviews/pr4-8-independent-arithmetic.json

This uses log/exp Taylor enclosures independently of the source binary-power
checkers. Displayed decimal values are informative; all assertions and the
stored interval bounds use exact rational arithmetic. Finite vertex and
support-function checks supplement the analytic proof review. They do not
enumerate the enormous integer support or replace the all-point argument.
"""
from fractions import Fraction as F
from math import comb, factorial
from itertools import product
from decimal import Decimal, localcontext
from pathlib import Path
import argparse
import json

SCALE = 10**65


def down(x):
    return F(x.numerator * SCALE // x.denominator, SCALE)


def up(x):
    return F(-((-x.numerator * SCALE) // x.denominator), SCALE)


def log_interval(a):
    """log(a)=2*sum y^(2j+1)/(2j+1), y=(a-1)/(a+1)."""
    assert a > 0
    y = (a-1)/(a+1)
    assert abs(y) < 1
    terms = 10
    center = 2*sum((y**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    error = 2*abs(y)**(2*terms+1)/(F(2*terms+1)*(1-y*y))
    return center-error, center+error


def exp_nonnegative_interval(lo, hi):
    """Taylor at x/64, exact geometric remainder, then six interval squarings."""
    assert 0 <= lo <= hi < 64
    ulo, uhi = down(lo/64), up(hi/64)
    assert 0 <= ulo <= uhi < 1
    degree = 64
    def partial(u):
        term = F(1)
        total = term
        for k in range(1, degree+1):
            term *= u/k
            total += term
        remainder = (term*u/F(degree+1))/(1-u/F(degree+2))
        return total, total+remainder
    left = down(partial(ulo)[0])
    right = up(partial(uhi)[1])
    for _ in range(6):
        left, right = down(left*left), up(right*right)
    return left, right


def power_interval(base, exponent):
    assert base > 0 and exponent >= 0
    if base == 1 or exponent == 0:
        return F(1), F(1)
    lo, hi = log_interval(base)
    lo, hi = exponent*lo, exponent*hi
    if base > 1:
        return exp_nonnegative_interval(lo, hi)
    a, b = exp_nonnegative_interval(-hi, -lo)
    return down(1/b), up(1/a)


def decimal(x, digits=65):
    with localcontext() as ctx:
        ctx.prec = digits
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def tetra_vertices(a):
    """Vertices of T_a represented by four barycentric coordinates."""
    other = [j for j in range(4) if j != a]
    for bits in product((0,1), repeat=3):
        lam = [F(0)]*4
        for j, bit in zip(other, bits):
            lam[j] = F(bit,4)
        lam[a] = 1-sum(lam)
        yield lam


def check_n52():
    N, n, h, ell = 13, 52, 274781, 2**61
    L = 2**n
    s, t, q = F(500000001,10**9), F(999999997,10**9), F(100001,200000)
    eps, eta = F(1,10**12), F(399999999,400000000)
    ds, dt, dq = 2*s-1, 1-t, 2*q-1
    theta, beta = F(3,32), F(27,64)
    v, R = ds/4+(1-ds)*eps, 3*(n+1)
    assert 0 < eps < F(1,4) and F(1,2) < s < 1 and F(1,2) < q < 1
    assert 0 < t < eta < 2*(1-s)
    assert N*dt < 1 and N*dq < 1
    assert N*(ds+4*eps*(3*t+1-ds)) < 1
    assert theta == F(1,4)**3 / F(1,6)
    assert beta == F(3,4)**3

    geometry = {'positive_vertices':0, 'negative_vertices':0,
                'affine_facet_inequalities':0, 'cut_sign_inequalities':0}
    min_facet = None
    min_exclusion = None
    for a in range(4):
        fc = [3*eps if j == a else -eps for j in range(4)]
        for k in range(1,n+1):
            assert 2*q <= 1+k*dq
            for lam in tetra_vertices(a):
                f = [2*s*(lam[j]-F(1,4))+(k-ds)*fc[j] for j in range(4)]
                assert sum(f) == 0
                geometry['positive_vertices'] += 1
                for j in range(4):
                    margin = F(1,4)+f[j]+v*k
                    assert margin >= 0
                    min_facet = margin if min_facet is None else min(min_facet,margin)
                    geometry['affine_facet_inequalities'] += 1
                    # Minimum possible number of selected coordinates in row j.
                    # Other three blocks each have at most N coordinates; a(I)=a
                    # additionally requires a nonempty intersection with block a.
                    kj = max(1 if j == a else 0, k-3*N)
                    assert 0 <= kj <= N
                    integer_score = -R*kj+eta*eps*(k-kj)
                    assert f[j]+integer_score < 0
                    gap = -(f[j]+integer_score)
                    min_exclusion = gap if min_exclusion is None else min(min_exclusion,gap)
                    geometry['cut_sign_inequalities'] += 1
        for r in range(1,N+1):
            tr, ur = 1-r*dt, 1-r*dq
            assert 0 < tr < 1 and 0 < ur < 1
            assert ur == 1-r*dq
            for lam in tetra_vertices(a):
                f = [tr*(lam[j]-F(1,4))-r*t*fc[j] for j in range(4)]
                assert sum(f) == 0
                geometry['negative_vertices'] += 1
                for j in range(4):
                    margin = F(1,4)+f[j]-v*r
                    assert margin >= 0
                    min_facet = min(min_facet,margin)
                    geometry['affine_facet_inequalities'] += 1
                    score = f[j]+(r*R if j == a else -r*eta*eps)
                    assert score > 0 if j == a else score < 0
                    min_exclusion = min(min_exclusion,abs(score))
                    geometry['cut_sign_inequalities'] += 1

    # Independent small-size calibration of the integer exposing functionals.
    # The general proof uses the coordinate-extremum census and the displayed
    # strict bounds, not this finite calibration.
    exposing_checks = 0
    for blocksize in (1,2):
        dim = 4*blocksize
        positive = list(range(1,2**dim))
        negative = []
        for a in range(4):
            for bits in range(1,2**blocksize):
                negative.append(bits << (a*blocksize))
        support = [(0,0)] + [(1,b) for b in positive] + [(-1,b) for b in negative]
        for sign, mask in support[1:]:
            selected = mask.bit_count()
            own = (dim+1)*selected
            for other_sign, other_mask in support:
                if (other_sign,other_mask) == (sign,mask):
                    continue
                intersection = (mask & other_mask).bit_count()
                outside = other_mask.bit_count()-intersection
                # Scale the rational exposing functional by dim+1.
                score = sign*other_sign*((dim+1)*intersection-outside)
                assert score < own
                exposing_checks += 1

    pl, ph = power_interval(2*q,h)
    ml, mh = theta*(2*s)**3*pl, theta*(2*s)**3*ph
    El = Eh = F(0)
    terms = []
    for r in range(1,N+1):
        tr, ur = 1-r*dt, 1-r*dq
        lo, hi = power_interval(ur,h)
        al, ah = theta*tr**3*lo, theta*tr**3*hi
        El += 4*comb(N,r)*al
        Eh += 4*comb(N,r)*ah
        terms.append({'r':r,'alpha_lower':str(al),'alpha_upper':str(ah)})
    assert F(1463268,10**6) < ml <= mh < F(1463269,10**6)
    assert F(465669,10**6) < El <= Eh < F(465670,10**6)
    el, eh = exp_nonnegative_interval(F(1),F(1))
    gl, gh = power_interval(F(ell,ell+1),ell)
    Wl, Wh = (L-1)*ml+1+El, (L-1)*mh+1+Eh
    middle_upper = (beta+Eh/4)/Wl
    exposed_upper = gh*mh/Wl
    uniform_upper = max(middle_upper, exposed_upper)
    relative_gap_lower = 1-eh*L*uniform_upper
    absolute_gap_lower = 1/(eh*L)-uniform_upper
    assert relative_gap_lower > 0 and absolute_gap_lower > 0
    padding_margin = 1+El-mh-L*mh/(2*ell-1)
    assert padding_margin > 0
    short_mlo, short_mhi = F(1463268,10**6), F(1463269,10**6)
    short_Elo, short_Ehi = F(465669,10**6), F(465670,10**6)
    eplus = F(1359141,500000)
    series_upper = sum((F(1,factorial(i)) for i in range(9)),F(0))+F(10,9*factorial(9))
    assert series_upper < eplus
    assert short_mlo/eplus-beta-short_Ehi/4 == F(40641,2970800000)
    assert 1+short_Elo-short_mhi == F(3,1250)
    short_padding = F(3,1250)-L*short_mhi/(2*ell-1)
    assert short_padding == F(139939647533841645493,144115188075855871968750) > 0

    result = {
        'status':'PASS',
        'method':'Independent rational log/exp Taylor enclosures; exact barycentric vertices; analytic geometry audited separately.',
        'n':n,'d':3+h+ell,'h':h,'ell':ell,
        'geometry_calibrations':geometry,
        'minimum_origin_facet_margin':str(min_facet),
        'minimum_nonzero_cut_sign_gap':str(min_exclusion),
        'finite_exposing_calibrations':exposing_checks,
        'm_interval':list(map(str,(ml,mh))),
        'E_interval':list(map(str,(El,Eh))),
        'e_interval':list(map(str,(el,eh))),
        'Gamma_ell_interval':list(map(str,(gl,gh))),
        'padding_margin_lower':str(padding_margin),
        'uniform_normalized_depth_upper':str(uniform_upper),
        'relative_violation_lower':str(relative_gap_lower),
        'absolute_violation_lower':str(absolute_gap_lower),
        'display':{
            'm':decimal((ml+mh)/2), 'E':decimal((El+Eh)/2),
            'Delta':decimal(1+(El+Eh)/2-(ml+mh)/2),
            'middle_cut_relative_upper':decimal(eh*L*middle_upper),
            'exposed_cut_relative_upper':decimal(eh*L*exposed_upper),
            'relative_violation_lower':decimal(relative_gap_lower),
            'absolute_violation_lower':decimal(absolute_gap_lower),
        },
        'outer_power_intervals':terms,
        'scope':'Upper bounds on all point depths; not an exact value of maximum depth and not a disproof of the unspecified smaller-positive-constant conjecture.'
    }
    return result


def check_n76(label, h, s, t, eta, ell):
    """Independent geometry and arithmetic for either explicit n=76 witness."""
    N, n = 19, 76
    q, eps = F(500001, 10**6), F(1, 10**10)
    theta, beta = F(3, 32), F(27, 64)
    ds, u = 2*s-1, 2*(1-q)
    cmin, cmax = F(1,4)-eps, F(1,4)+3*eps
    kappa = cmax/cmin
    assert F(1,2) < s < 1 and F(1,2) < q < 1
    assert 0 < eps < F(1,4) and 0 < t < eta < 2*(1-s)
    assert 2*kappa*t < 3-2*s
    R = 3*(n+1)
    geometry = {'singleton_origin_facets':0, 'mixed_origin_lower_bounds':0,
                'positive_vertices':0, 'negative_vertices':0,
                'cut_sign_inequalities':0, 'free_box_inclusions':0}
    min_sign_gap = None
    for k in range(1, n+1):
        assert 2*q+k*u <= k+1
        geometry['free_box_inclusions'] += 1
    for a in range(4):
        ca = [cmax if j == a else cmin for j in range(4)]
        fc = [x-F(1,4) for x in ca]
        vertices = list(tetra_vertices(a))
        # The singleton source and outer body have the same type. Check
        # every vertex sum; affine inequalities then cover the whole sum.
        for lp in vertices:
            for la in vertices:
                for j in range(4):
                    value = 2*((1-s)*ca[j]+s*lp[j])+t*(la[j]-ca[j])
                    assert value >= 0
                    geometry['singleton_origin_facets'] += 1
        # For k>=2 this uses the minimum over all possible outer types.
        # It verifies the proof's uniform Minkowski-sum bound without
        # enumerating exponentially many integer subsets.
        for k in range(2, n+1):
            for j in range(4):
                min_ta = F(1,4) if j == a else F(0)
                bound = 2*s*min_ta+(k+1-2*s)*ca[j]-k*t*cmax
                assert bound >= 0
                geometry['mixed_origin_lower_bounds'] += 1
        for k in range(1, n+1):
            for lam in vertices:
                f = [2*s*(lam[j]-F(1,4))+(k-ds)*fc[j] for j in range(4)]
                assert sum(f) == 0
                geometry['positive_vertices'] += 1
                for j in range(4):
                    kj = max(1 if j == a else 0, k-3*N)
                    assert 0 <= kj <= N
                    score = f[j]-R*kj+eta*eps*(k-kj)
                    assert score < 0
                    gap = -score
                    min_sign_gap = gap if min_sign_gap is None else min(min_sign_gap,gap)
                    geometry['cut_sign_inequalities'] += 1
        for lam in vertices:
            f = [t*(lam[j]-ca[j]) for j in range(4)]
            assert sum(f) == 0
            geometry['negative_vertices'] += 1
            for j in range(4):
                score = f[j]+(R if j == a else -eta*eps)
                assert score > 0 if j == a else score < 0
                min_sign_gap = min(min_sign_gap,abs(score))
                geometry['cut_sign_inequalities'] += 1

    pl, ph = power_interval(2*q,h)
    ml, mh = theta*(2*s)**3*pl, theta*(2*s)**3*ph
    al, ah = power_interval(u,h)
    al, ah = theta*t**3*al, theta*t**3*ah
    el, eh = exp_nonnegative_interval(F(1),F(1))
    gl, gh = power_interval(F(ell,ell+1),ell)
    L = 2**n
    Wl = (L-1)*ml+1+n*al
    middle = (beta+N*ah)/Wl
    exposed = gh*mh/Wl
    upper = max(middle,exposed)
    relative = 1-eh*L*upper
    absolute = 1/(eh*L)-upper
    assert relative > 0 and absolute > 0
    assert ml/eh-beta-N*ah > 0
    assert 1+n*al-mh > 0
    # Compare a lower bound for m with an upper bound for alpha.
    assert ml > ah
    return {
        'status':'PASS', 'label':label, 'n':n, 'h':h, 'ell':ell, 'd':3+h+ell,
        'geometry_calibrations':geometry,
        'minimum_nonzero_cut_sign_gap':str(min_sign_gap),
        'm_interval':list(map(str,(ml,mh))), 'alpha_interval':list(map(str,(al,ah))),
        'e_interval':list(map(str,(el,eh))), 'Gamma_ell_interval':list(map(str,(gl,gh))),
        'uniform_normalized_depth_upper':str(upper),
        'relative_violation_lower':str(relative), 'absolute_violation_lower':str(absolute),
        'display':{key:decimal(value) for key,value in {
            'm':(ml+mh)/2, 'alpha':(al+ah)/2,
            'Delta':1+n*(al+ah)/2-(ml+mh)/2,
            'middle_cut_relative_upper':eh*L*middle,
            'exposed_cut_relative_upper':eh*L*exposed,
            'relative_violation_lower':relative,
            'absolute_violation_lower':absolute}.items()},
        'scope':'Exact arithmetic and finite generator inequalities supplement the separately reviewed analytic proof; integer support and the all-point ambient-tilt argument are not exhaustively enumerated.'
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Write the full exact JSON certificate to this path.')
    args = parser.parse_args()
    cases = [
        check_n76('n76-original', 1372126, F(500001,10**6),
                  F(999997,10**6), F(399999,400000), 2**94),
        check_n76('n76-improved', 1372128, F(5000001,10**7),
                  F(9999997,10**7), F(3999999,4000000), 2**93),
        check_n52(),
    ]
    cases[-1]['label'] = 'n52'
    result = {
        'schema_version':1, 'status':'PASS',
        'arithmetic':'Exact Fraction arithmetic: atanh-series log enclosures with rational remainders; degree-64 exp Taylor enclosures at x/64 followed by six outward-rounded squarings.',
        'rounding_scale':str(SCALE),
        'reviewed_proof_refs':{
            'n76':'3497df590ae6f7b8abaad88a5abe853ab993582e',
            'n52':'2ffd469d639402e465de448fb31dd920eaf7f40a'},
        'scope':'Independent numerical certificate and finite generator checks. The analytic fiber census, origin fiber, closed ambient cuts, and uniform all-point argument require the companion proof review. No claim of a fully formalized mixed-integer measure theorem.',
        'cases':cases,
    }
    text = json.dumps(result,indent=2)+'\n'
    if args.output is None:
        print(text,end='')
    else:
        args.output.write_text(text,encoding='utf-8')
        for case in cases:
            print('PASS '+case['label']+': relative gap > '+case['display']['relative_violation_lower'])
        print('Saved '+args.output.name)


if __name__ == '__main__':
    main()
