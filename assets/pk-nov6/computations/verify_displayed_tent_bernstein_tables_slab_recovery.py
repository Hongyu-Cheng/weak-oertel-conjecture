"""Independent audit of the rational matrices actually printed in the proof."""
from submission_text import read_submission
from pathlib import Path
import re
import runpy
import sympy as s

ns = runpy.run_path('./build_exact_tent_hminus_bernstein_tables_two_sided.py')
text = read_submission('443fb78ca8dd4f80')
R,u,x,y = (ns[z] for z in ('R','u','x','y'))
checks = 0
for name,poly,r0,r1,u0,u1 in ns['rects']:
    if name == 'C':
        block = text.split('matrix of degrees(5,3)')[1].split('All entries')[0]
    else:
        block = text.split('Certificate '+name+':')[1].split('```')[1]
    rows = [[s.Rational(v.strip()) for v in line.split(',')]
            for line in re.findall(r'\[([^\[\]\n]+)\]', block)
            if ',' in line]
    m,n = s.Poly(poly,R,u).degree_list()
    assert len(rows)==m+1 and all(len(row)==n+1 for row in rows)
    assert all(v>=0 for row in rows for v in row)
    printed = sum(rows[i][j]*s.binomial(m,i)*s.binomial(n,j)
                  *x**i*(1-x)**(m-i)*y**j*(1-y)**(n-j)
                  for i in range(m+1) for j in range(n+1))
    original=poly.subs({R:r0+(r1-r0)*x,u:u0+(u1-u0)*y})
    assert s.expand(printed-original)==0
    checks += 2 + (m+1)*(n+1)

# Independently derive the equal-slope-line numerator from the actual cap.
a,T=s.symbols('a T')
D=2*a-1
J=(1-T/3)**2/(2*(1-D))+1-T*T/(9*D)
N=(6*a-5)*T*T-6*(2*a-1)*T+24*a*a-18*a+3
assert s.factor(J-s.Rational(4,3)-N/(36*(1-a)*(2*a-1)))==0
checks+=1
print(f'PASS: {checks} exact printed-table and algebra checks')
