#!/usr/bin/env python3
"""Independent exact arithmetic audit of sharp-n168-d99.md.

Finite checks support the analytic arguments in join_audit.md.  No third-party
packages, floating-point predicates, or data from the author's checker are used.
"""
from fractions import Fraction as F
from math import comb, factorial
from decimal import Decimal, localcontext
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
PROOF = HERE / 'sharp-n168-d99.md'
checks = {}

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks[name] = True

def dec(x):
    with localcontext() as ctx:
        ctx.prec = 55
        return str(Decimal(x.numerator) / Decimal(x.denominator))

def rat(x):
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator),
            'decimal': dec(x)}

def det(A):
    A = [[F(x) for x in row] for row in A]
    answer = F(1)
    for j in range(len(A)):
        pivot = next((i for i in range(j,len(A)) if A[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            A[j], A[pivot] = A[pivot], A[j]
            answer = -answer
        p = A[j][j]
        answer *= p
        for i in range(j + 1,len(A)):
            q = A[i][j]/p
            for k in range(j + 1,len(A)):
                A[i][k] -= q*A[j][k]
    return answer

D, d, N, n = 100, 99, 56, 168
eps = F(1,10**14)
delta = F(3258435,10**8)
delta_prime = delta + F(1,10**10)
t = 1-delta_prime
eta = 1-(delta+delta_prime)/2
R = F(3*(n+1))
theta, beta = F(5,36), F(49,108)
gamma = F(99,100)**99
v = delta/D + (1-delta)*F(35,39)*eps
cmin = F(1,D)-F(35,39)*eps
cmax = F(1,D)+F(49,39)*eps
basis = [[F(i==j) for i in range(D)] for j in range(D)]
p = [F(i<3,3) for i in range(D)]

# Work in the barycentric affine hyperplane sum(lambda)=1.  Functions f have
# zero coefficient sum, so their values equal those of the corresponding
# linear functionals in the centered hyperplane L.
def f(a, lam):
    return lam[a]-F(2,7)*lam[(a+1)%3]-F(5,7)*lam[(a+2)%3]

simplices = []
centers = []
max_positive_scores = {}
for a in range(3):
    an, ao = (a+1)%3, (a+2)%3
    q = [(7*basis[a][j]+5*basis[an][j])/12 for j in range(D)]
    vertices = [p,basis[a],q]+basis[3:]
    simplices.append(vertices)
    check(f'T{a}_vertex_count',len(vertices)==D)
    check(f'T{a}_vertices_in_B',all(sum(x)==1 and min(x)>=0 for x in vertices))
    # Columns p,e_a,q_a span the first-three-coordinate block.  Remaining
    # columns are an identity block, so this is the full barycentric determinant.
    determinant = abs(det([[vertices[j][i] for j in range(3)] for i in range(3)]))
    check(f'T{a}_determinant',determinant==theta)
    check(f'T{a}_all_facets_have_zero_minimum',all(min(x[j] for x in vertices)==0 for j in range(D)))
    check(f'T{a}_own_f_range',min(f(a,x) for x in vertices)==0 and max(f(a,x) for x in vertices)==1)
    for j in range(3):
        if j != a:
            check(f'T{a}_missed_f{j}_maximum',max(f(j,x) for x in vertices)==0)
    center = [F(1,D) for _ in range(D)]
    center[a] += F(49,39)*eps
    center[an] -= F(14,39)*eps
    center[ao] -= F(35,39)*eps
    centers.append(center)
    weights = [F(3,100)-F(35,13)*eps,F(7,5)*eps,F(84,65)*eps]+[F(1,100)]*97
    check(f'c{a}_strict_T_interior',min(weights)>0 and sum(weights)==1)
    rebuilt = [sum(w*x[j] for w,x in zip(weights,vertices)) for j in range(D)]
    check(f'c{a}_reconstruction',rebuilt==center)
    check(f'c{a}_barycentric_range',min(center)==cmin and max(center)==cmax)
    check(f'c{a}_scores',all(f(j,center)==(2 if j==a else -1)*eps for j in range(3)))
    # Exact positive cap of f_a on B: cut the two incident edges of its
    # first-three-coordinate face, then join to the remaining vertices.
    edge_n = [(2*basis[a][j]+7*basis[an][j])/9 for j in range(D)]
    edge_o = [(5*basis[a][j]+7*basis[ao][j])/12 for j in range(D)]
    cap = [basis[a],edge_n,edge_o]+basis[3:]
    capdet = abs(det([[cap[j][i] for j in range(3)] for i in range(3)]))
    check(f'f{a}_B_cap_volume',capdet==beta)
    check(f'f{a}_cap_edge_roots',f(a,edge_n)==0 and f(a,edge_o)==0)

check('sum_f_identically_zero',all(sum(f(a,e) for a in range(3))==0 for e in basis))
check('f_B_bounds',all(-1<=f(a,e)<=1 for a in range(3) for e in basis))
check('parameter_order',0<delta<delta_prime<F(1,30) and 0<t<eta<1-delta)
check('eta_eps_bound',0<eta*eps<1)

# Affine barycentric constants: lambda(Au+Bc)=A lambda(u)+B lambda(c)
# +(1-A-B)/100, as sum(lambda)=1 only for barycentric coordinates.
positive_origin_min = None
negative_origin_min = None
for a in range(3):
    for k in range(1,n+1):
        A, B = 1+delta,k-delta
        check(f'K_affine_constant_{a}_{k}',(1-A-B)/D == -F(k,D))
        vals = [(k-delta)*centers[a][j]-F(k,D)+k*v for j in range(D)]
        low = min(vals)
        if positive_origin_min is None or low<positive_origin_min: positive_origin_min=low
        check(f'K_origin_facets_{a}_{k}',low>=0)
    for r in range(1,31):
        tr=1-r*delta_prime
        A, B=tr,-r*t
        check(f'G_scale_{a}_{r}',tr>0)
        check(f'G_affine_constant_{a}_{r}',(1-A-B)/D==F(r,D))
        vals = [-r*t*centers[a][j]+F(r,D)-r*v for j in range(D)]
        low = min(vals)
        if negative_origin_min is None or low<negative_origin_min: negative_origin_min=low
        check(f'G_origin_facets_{a}_{r}',low>0)
origin_slope_gap = F(delta_prime-delta,D)-((1-delta)*F(35,39)+t*F(49,39))*eps
check('origin_gap_formula',negative_origin_min==origin_slope_gap)

# Middle cuts: maximize the complete affine functional over all vertices
# for every feasible positive cardinality/block-intersection/type case.
max_positive = None
min_paid_negative = None
max_unpaid_negative = None
positive_cases = 0
for j in range(3):
    for a in range(3):
        source_max = max(f(j,x) for x in simplices[a])
        for k in range(1,n+1):
            for s in range(max(0,k-2*N),min(N,k)+1):
                if a==j and s==0: continue
                if a!=j and k-s==0: continue
                val=(1+delta)*source_max+(k-delta)*f(j,centers[a])-R*s+(k-s)*eta*eps
                check(f'positive_middle_{j}_{a}_{k}_{s}',val<0)
                positive_cases+=1
                if max_positive is None or val>max_positive: max_positive=val
        for r in range(1,31):
            tr=1-r*delta_prime
            integer_score=r*R if a==j else -r*eta*eps
            vals=[tr*f(j,x)-r*t*f(j,centers[a])+integer_score for x in simplices[a]]
            if a==j:
                low=min(vals)
                check(f'negative_paid_middle_{j}_{r}',low>0)
                if min_paid_negative is None or low<min_paid_negative: min_paid_negative=low
            else:
                high=max(vals)
                check(f'negative_unpaid_middle_{j}_{a}_{r}',high<0)
                if max_unpaid_negative is None or high>max_unpaid_negative: max_unpaid_negative=high

# Exposure is audited by exhaustive cardinality/intersection summaries.
# Every pair of supports has one such summary; no full cube enumeration needed.
rho=F(1,n+1)
positive_same_gap=None
positive_negative_gap=None
negative_same_gap=None
negative_positive_gap=None
for k in range(1,n+1):
    for l in range(n+1):
        for q in range(max(0,k+l-n),min(k,l)+1):
            if k==l==q: continue
            gap=k-(q-rho*(l-q))
            check(f'pos_expose_pos_{k}_{l}_{q}',gap>0)
            positive_same_gap=gap if positive_same_gap is None else min(positive_same_gap,gap)
    for r in range(1,31):
        for q in range(max(0,k+r-n),min(k,r)+1):
            gap=k-(-q+rho*(r-q))
            check(f'pos_expose_neg_{k}_{r}_{q}',gap>0)
            positive_negative_gap=gap if positive_negative_gap is None else min(positive_negative_gap,gap)
for r in range(1,31):
    for l in range(1,31):
        for q in range(min(r,l)+1):
            if r==l==q: continue
            gap=r-(q-rho*(l-q))
            check(f'neg_expose_neg_{r}_{l}_{q}',gap>0)
            negative_same_gap=gap if negative_same_gap is None else min(negative_same_gap,gap)
    for k in range(n+1):
        for q in range(max(0,r+k-n),min(r,k)+1):
            gap=r-(-q+rho*(k-q))
            check(f'neg_expose_pos_{r}_{k}_{q}',gap>0)
            negative_positive_gap=gap if negative_positive_gap is None else min(negative_positive_gap,gap)

m=theta*(1+delta)**d
terms=[F(3)*theta*comb(N,r)*(1-r*delta_prime)**d for r in range(1,31)]
E=sum(terms,F(0))
s=1+E-m
middle=beta+E/3
margin=gamma*m-middle
W=(2**n-1)*m+1+E
max_depth=gamma*m/W
sharp=gamma/F(2**n)
check('all_negative_fiber_volumes_below_m',all(theta*(1-r*delta_prime)**d<m for r in range(1,31)))
check('positive_total_formula',W==2**n*m+s)
check('mass_margin_at_least_0_00038',s>F(38,100000))
check('middle_margin_at_least_0_00038',margin>F(38,100000))
check('strict_sharp_counterexample',max_depth<sharp)
check('middle_strictly_below_positive_centroid',middle/W<max_depth)
e_lower=sum((F(1,factorial(j)) for j in range(5)),F(0))
check('e_lower_bound_65_24',e_lower==F(65,24))
check('not_a_1_over_e_counterexample',e_lower*gamma>1+s/(2**n*m))
check('d_target_met',d<100)
check('n_target_not_met',n>=100)

results={
 'status':'PASS',
 'construction':{'n':n,'d':d,'D':D,'block_size':N,'negative_support_max':30},
 'proof_sha256':hashlib.sha256(PROOF.read_bytes()).hexdigest(),
 'exact_predicate_count':len(checks),'positive_middle_cases':positive_cases,
 'parameters':{k:rat(x) for k,x in [('delta',delta),('delta_prime',delta_prime),('eps',eps),('eta',eta),('t',t),('R',R)]},
 'scalar_obligations':{k:rat(x) for k,x in [('theta',theta),('beta',beta),('gamma',gamma),('m',m),('E',E),('mass_margin',s),('middle_margin',margin),('origin_slope_gap',origin_slope_gap)]},
 'bounds':{k:rat(x) for k,x in [('positive_origin_facet_min',positive_origin_min),('negative_origin_facet_min',negative_origin_min),('positive_middle_max',max_positive),('paid_negative_middle_min',min_paid_negative),('unpaid_negative_middle_max',max_unpaid_negative),('positive_vs_positive_exposure_gap_min',positive_same_gap),('positive_vs_negative_exposure_gap_min',positive_negative_gap),('negative_vs_negative_exposure_gap_min',negative_same_gap),('negative_vs_positive_exposure_gap_min',negative_positive_gap)]},
 'normalized_depth_decimal':dec(max_depth),
 'sharp_bound_decimal':dec(sharp),
 'relative_sharp_deficit_decimal':dec(s/W),
 'scope':{'sharp_conjecture_counterexample':True,'one_over_e_counterexample':False,'both_dimensions_below_100':False,'lean_formalized':False},
 'qualification':'Analytic geometry and all-points arguments are proved in join_audit.md; this finite exact checker validates their algebra and extremal vertex cases.'
}
out=HERE/'join_audit_results.json'
out.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({k:results[k] for k in ['status','construction','exact_predicate_count','positive_middle_cases','normalized_depth_decimal','sharp_bound_decimal','relative_sharp_deficit_decimal','scope']},indent=2))
for k in ['m','E','mass_margin','middle_margin','origin_slope_gap']:
    print(k,results['scalar_obligations'][k]['decimal'])
