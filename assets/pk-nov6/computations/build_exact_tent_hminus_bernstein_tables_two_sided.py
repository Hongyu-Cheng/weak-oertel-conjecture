"""Generate/check exact finite polynomial identities, not a numerical screen."""
import sympy as s
from pathlib import Path
R,u,x,y=s.symbols('R u x y')
A=18*R**3*u**3-39*R**3*u**2+18*R**3*u+3*R**3-36*R**2*u**3+51*R**2*u**2+36*R**2*u-33*R**2+18*R*u**3-18*R*u**2-24*R*u+47*R+6*u**2-17
B=-45*R**5*u**3+129*R**5*u**2-123*R**5*u+39*R**5-9*R**4*u**3-48*R**4*u**2+135*R**4*u-78*R**4+54*R**3*u**3-9*R**3*u**2-111*R**3*u+60*R**3-54*R**2*u**2+81*R**2*u-28*R**2-6*R*u+R+6
C=27*R**5*u**3+234*R**5*u**2+576*R**5*u+288*R**5-483*R**4*u**2-984*R**4*u-208*R**4-54*R**3*u**3+276*R**3*u**2+1080*R**3*u-192*R**3+54*R**2*u**2-648*R**2*u+240*R**2+27*R*u**3-78*R*u**2+168*R*u-64*R-3*u**2
rat=s.Rational
rects=[('A1',A,rat(1,2),rat(3,5),rat(5,9),1),('A2',A,rat(3,5),rat(5,8),rat(19,45),1),('A3',A,rat(5,8),rat(7,9),0,1),('B1',B,rat(2,9),rat(1,2),0,1),('B2',B,rat(1,2),rat(3,5),0,1),('B3',B,rat(3,5),rat(7,10),0,rat(5,9)),('C',C,rat(1,2),rat(7,9),0,1)]
checks=0
out=['\n## Appendix A. Exact tensor Bernstein certificates\n','For a rectangle [r0,r1] times [u0,u1], substitute R=r0+(r1-r0)x and u=u0+(u1-u0)y. A matrix (b_ij) of degrees(m,n) below means the polynomial equals\n','    sum_(i=0)^m sum_(j=0)^n b_ij binom(m,i)binom(n,j)\n        x^i(1-x)^(m-i)y^j(1-y)^(n-j).\n','Each basis factor is nonnegative on the unit square. Rows index i and columns index j. The following are full exact identities obtained by expanding the displayed polynomials; all entries are rational.\n']
for name,pol,r0,r1,u0,u1 in rects:
    P=s.Poly(s.expand(pol.subs({R:r0+(r1-r0)*x,u:u0+(u1-u0)*y})),x,y);m,n=P.degree_list()
    coeffs=[[s.factor(sum(P.coeff_monomial(x**a*y**b)*s.binomial(i,a)/s.binomial(m,a)*s.binomial(j,b)/s.binomial(n,b)for a in range(i+1)for b in range(j+1)))for j in range(n+1)]for i in range(m+1)]
    expansion=sum(coeffs[i][j]*s.binomial(m,i)*s.binomial(n,j)*x**i*(1-x)**(m-i)*y**j*(1-y)**(n-j)for i in range(m+1)for j in range(n+1))
    assert s.expand(expansion-P.as_expr())==0
    assert all(v>=0 for row in coeffs for v in row)
    checks+=1+sum(len(row) for row in coeffs)
    if name!='C':
        out.append(f'Certificate {name}: rectangle [{r0},{r1}] times [{u0},{u1}], degrees({m},{n}).\n\n```\n')
        out.extend('['+', '.join(map(str,row))+']\n' for row in coeffs)
        out.append('```\n')
# Whole-edge rational identities.
a=(1-2*R+3*R**2)/2+3*R*(1-R)*u/2
D=a-R**2;T=1-2*R+a;S=1-T/3;L=1-a
pair=1-T**2/(9*D)
qa=S/2-L/4+(S-L)**2/(4*R**2)
qb=S/(2*R)-rat(1,4)+(S-R)**2/(4*L)
assert s.factor(qa+pair-rat(4,3)-A/(24*(3*R*u-R+1)))==0
assert s.factor(qb+pair-rat(4,3)-B/(24*R*(3*R+1-3*R*u)*(3*R*u-R+1)))==0
D=(1-R)*((2*R-1)/(5*R-1)+(1-(2*R-1)/(5*R-1))*u)
a=(1+D)/2;T=((1-R)*(2*R-1)+(R+1)*D)/(2*R)
N=(6*a-5)*T**2-6*(2*a-1)*T+24*a*a-18*a+3
assert s.factor(N-3*(1-R)*C/(4*(5*R-1)**3))==0
checks+=3
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--write-appendix',action='store_true');p.add_argument('--output',default='tent-hminus-bernstein-appendix.md');args=p.parse_args()
    if args.write_appendix:
        # Export the generated appendix without editing the pending submission.
        Path(args.output).write_text('\n'.join(out),encoding='utf-8')
    print(f'PASS: {checks:,} exact identities/coefficient checks')
