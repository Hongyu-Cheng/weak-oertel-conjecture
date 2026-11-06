#!/usr/bin/env python3
"""Exact identities and regression checks; the note proves the uniform bounds."""
from fractions import Fraction as F
from itertools import combinations
import sympy as sy

s,b=sy.symbols('s b',positive=True)
a=1+b
f=(1+sy.sqrt(1+3*s*s))/9-s*s/3
M=(1-s*s)/2+(2*a-s)**2/8+b*b/2
assert sy.simplify(-sy.diff(f,s)-(s/3)*(2-1/sy.sqrt(1+3*s*s)))==0
assert sy.simplify(-sy.diff(M,s)-(2*a+3*s)/4)==0
U=(2*a-s)**2/18+b*b/2
lower=sy.Rational(2,9)-s*s/3
expected=2*a*s/9-7*s*s/18-4*b/9-13*b*b/18
assert sy.expand(lower-U-expected)==0
checks=3
for power in range(4,18):
    ep=F(1,2**power); bb=ep*ep; aa=1+bb
    for frac in [F(1,2),F(5,8),F(3,4),F(7,8),F(1)]:
        ss=ep*frac
        masses=[(1-ss*ss)/2,(2*aa-ss)**2/8,bb*bb/2]
        MM=sum(masses)
        flower=F(2,9)-ss*ss/3
        gaplower=2*ss/9-7*ss*ss/18-4*bb/9-13*bb*bb/18
        assert gaplower>=7*ep/144>0
        assert flower>F(1,5) and MM<2
        assert 2*ss/3*MM-flower*(2*aa+3*ss)/4<=-F(1,60)
        expected_vertices=[{(ss,F(0)),(F(1),F(0)),(F(0),F(1)),(F(0),ss)},
                           {(aa/2,aa/2),(aa/2,(ss-aa)/2),((ss-aa)/2,aa/2)},
                           {(F(0),F(0)),(bb,F(0)),(F(0),bb)}]
        for z in range(3):
            upper=1-(1-bb)*z/2
            planes=[(F(1),F(0),upper),(F(0),F(1),upper),
                    (-F(1),F(0),(aa-ss)*z/2),(-F(1),F(0),(aa-ss)*(2-z)/2),
                    (F(0),-F(1),(aa-ss)*z/2),(F(0),-F(1),(aa-ss)*(2-z)/2),
                    (-F(1),-F(1),-ss*(1-F(z,2))),
                    (F(1),F(1),1+bb*z),(F(1),F(1),2+bb-z)]
            vertices=set()
            for (A,B,h),(C,D,k) in combinations(planes,2):
                det=A*D-B*C
                if not det: continue
                x=(h*D-B*k)/det; y=(A*k-h*C)/det
                if all(E*x+G*y<=l for E,G,l in planes): vertices.add((x,y))
            assert vertices==expected_vertices[z]
            checks+=1
        checks+=3
print(f'PASS {checks} exact derivative, all-fiber shared-plane, active-gap, and dilution checks')
