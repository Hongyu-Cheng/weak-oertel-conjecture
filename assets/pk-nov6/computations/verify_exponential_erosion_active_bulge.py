"""Exact symbolic checks of the all-cap corrected interval bulge.

All sign proofs use rational bounds on 0 <= delta <= 1/4.
No sampled slopes or numerical minimization enter the certificate.
"""
import sympy as s

t=s.symbols('delta', real=True)
z=[-1,0,1,2]
l=[-s.Rational(5,2)+t/38,-s.Rational(9,4)+t/19,
   -s.Rational(3,2)+2*t/19,-s.Rational(1,2)+4*t/19]
r=[s.Rational(5,2)-t/38,s.Rational(9,4)-t/19,
   s.Rational(3,2)+17*t/19,s.Rational(1,2)-4*t/19]
w=[s.expand(b-a) for a,b in zip(l,r)]
assert s.expand(sum(i*wi for i,wi in zip(z,w))) == 0
m=s.expand(sum(w))
assert m == s.Rational(27,2)+4*t/19
moment=s.expand(sum((b*b-a*a)/2 for a,b in zip(l,r)))
c=s.factor(moment/m)
assert s.simplify(c-3*t*(5*t+19)/(8*t+513)) == 0
removed=[t/s.Integer(19),2*t/19,4*t/19,8*t/19]
assert s.expand(sum(removed)) == 15*t/19
assert s.expand(sum(i*ri for i,ri in zip(z,removed))) == t

# Upper/lower interpolation remains concave/convex on the whole interval.
def nonnegative_by_coefficient_bound(poly, upper=s.Rational(1,4)):
    p=s.Poly(s.expand(poly),t)
    # Positive monomials may be discarded; bound negative ones at upper.
    bound=s.Rational(0)
    for (power,),coef in p.terms():
        if power == 0: bound += coef
        elif coef < 0: bound += coef*upper**power
    assert bound >= 0, (poly,bound)
    return bound
for j in range(2):
    nonnegative_by_coefficient_bound((r[j+1]-r[j])-(r[j+2]-r[j+1]))
    nonnegative_by_coefficient_bound((l[j+2]-l[j+1])-(l[j+1]-l[j]))
for wi in w:
    assert nonnegative_by_coefficient_bound(wi)>0

breaks=[l[0]-c,c-r[2],(c-r[3])/2,(c-l[3])/2,c-l[2],r[0]-c]
expected_num=[860*t*t-13319*t+19494,
              2*t*t+1978*t+2565,19-8*t,
              30*t*t+154*t+2565,19494-2489*t-1116*t*t]
expected_den=[38*(8*t+513),4*(8*t+513),38,
              4*(8*t+513),38*(8*t+513)]
for a,b,num,den in zip(breaks,breaks[1:],expected_num,expected_den):
    assert s.factor(b-a-num/den)==0
    assert nonnegative_by_coefficient_bound(num)>0
# The proper-index sums between these ordered events give these slopes.
proper_sets=[[],[-1],[-1,1],[-1,1,2],[-1,1],[-1],[]]
assert [sum(a) for a in proper_sets]==[0,-1,0,2,0,-1,0]

left=w[0]+r[1]-c
low=r[0]+r[1]+r[2]-3*c
high=low+w[3]
right=w[2]+w[3]+r[1]-c
Q=[right,m-high,m-left,low]
beta=s.Rational(25,54)
expected_gaps=[t*(28215-6799*t)/(513*(8*t+513)),
 t*(43858*t+27189)/(1026*(8*t+513)),
 t*(8591*t+86697)/(513*(8*t+513)),
 t*(202635-40274*t)/(1026*(8*t+513))]
for Qi, gap in zip(Q,expected_gaps):
    assert s.factor(Qi-beta*m-gap)==0
    assert Qi.subs(t,0)==s.Rational(25,4)
for numerator in [28215-6799*t,43858*t+27189,
                  8591*t+86697,202635-40274*t]:
    assert nonnegative_by_coefficient_bound(numerator)>0
assert [s.diff(g,t).subs(t,0) for g in expected_gaps] == [
    s.Rational(55,513),s.Rational(53,1026),
    s.Rational(169,513),s.Rational(395,1026)]
# Own fiber remains proper, so vertical full-fiber caps dominate tail limits.
assert nonnegative_by_coefficient_bound(s.together(r[1]-c).as_numer_denom()[0])>0
assert nonnegative_by_coefficient_bound(s.together(c-l[1]).as_numer_denom()[0])>0
print('PASS: exact moments, convexity, ordered clipping events, all four cap deficits, and closed vertical limits')

# Uniform near-gamma extension: a >= 3, 0 <= delta <= 1/4.
a=s.symbols('a', real=True)
l_a=[-(a+2)/2+t/38,-3*a/4+t/19,-a/2+2*t/19,-s.Rational(1,2)+4*t/19]
r_a=[(a+2)/2-t/38,3*a/4-t/19,a/2+17*t/19,s.Rational(1,2)-4*t/19]
w_a=[s.expand(rr-ll) for ll,rr in zip(l_a,r_a)]
m_a=s.expand(sum(w_a)); M_a=m_a.subs(t,0)
c_a=s.factor(sum((rr*rr-ll*ll)/2 for ll,rr in zip(l_a,r_a))/m_a)
beta_a=(7*a+4)/(2*(7*a+6)); P=133*a+8*t+114
assert M_a==(7*a+6)/2
assert s.factor(c_a-t*(19*a+15*t)/P)==0
assert s.expand(sum(zi*wi for zi,wi in zip(z,w_a)))==0
left_a=w_a[0]+r_a[1]-c_a
low_a=sum(r_a[:3])-3*c_a
high_a=low_a+w_a[3]
right_a=w_a[2]+w_a[3]+r_a[1]-c_a
Q_a=[right_a,m_a-high_a,m_a-left_a,low_a]
nums=[1197*a*a+4750*a+3192-t*(1771*a+1486),
4921*a*a-3496*a-6612+t*(11354*a+9796),
6251*a*a+9082*a+3192+t*(2219*a+1934),
9975*a*a+31160*a+19380-t*(10458*a+8900)]
dens=[19*(7*a+6)*P,38*(7*a+6)*P,19*(7*a+6)*P,38*(7*a+6)*P]
A=s.symbols('A', nonnegative=True)
def positive_uniform(poly):
    coeffs=s.Poly(s.expand(poly.subs(a,A+3)),A).all_coeffs()
    bounds=[nonnegative_by_coefficient_bound(c) for c in coeffs]
    assert bounds[-1]>0, (poly,bounds)
for Qi,num,den in zip(Q_a,nums,dens):
    assert s.factor(Qi-beta_a*m_a-t*num/den)==0
    positive_uniform(num)
B_a=[l_a[0]-c_a,c_a-r_a[2],(c_a-r_a[3])/2,
     (c_a-l_a[3])/2,c_a-l_a[2],r_a[0]-c_a]
B_nums=[5054*a+4332-t*(3211*a+3686)+860*t*t,
266*a*a+95*a-114+510*a*t+2*t*t+448*t,
19-8*t,266*a*a+95*a-114+(54*a-8)*t+30*t*t,
5054*a+4332-1045*a*t+646*t-1116*t*t]
B_dens=[38*P,4*P,38,4*P,38*P]
for x,y,num,den in zip(B_a,B_a[1:],B_nums,B_dens):
    assert s.factor(y-x-num/den)==0
    positive_uniform(num)
first=[(9*a+28)/(19*(7*a+6)),(37*a-58)/(38*(7*a+6)),
       (47*a+28)/(19*(7*a+6)),5*(15*a+34)/(38*(7*a+6))]
for Qi,di in zip(Q_a,first):
    assert s.factor(s.diff(Qi-beta_a*m_a,t).subs(t,0)-di)==0
    numerator=s.together(di-s.Rational(53,1026)).as_numer_denom()[0]
    coefficients=s.Poly(s.expand(numerator.subs(a,A+3)),A).all_coeffs()
    assert all(coef>=0 for coef in coefficients)
assert first[1].subs(a,3)==s.Rational(53,1026)
assert s.factor(s.diff(first[1],a))==s.Rational(314,19)/(7*a+6)**2
assert s.limit(beta_a,a,s.oo)==s.Rational(1,2)
print('PASS: uniform all-cap extension a>=3 and beta_a increasing to gamma_1')
