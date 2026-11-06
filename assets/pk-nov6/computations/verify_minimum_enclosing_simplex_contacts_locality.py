"""Exact finite arithmetic checks for enclosing-simplex contacts/locality.

Attainment and the nonsmooth separation argument are analytic proofs
in the source. These tests verify the exact facet-tilt volume formula,
actual convex source feasibility, and the dimensional locality bounds.
"""
from fractions import Fraction as F
from math import prod

tilt_checks=0
for m in range(2,21):
    for variant in range(1,6):
        v=[F((j+1)**variant,m**variant) for j in range(m)]
        mean=sum(v)/m
        s=(v[0]+mean)/2
        assert v[0]<s<mean
        eta=F(1,4)
        eps=F(1,1000*m)
        # K=conv((1-eta)T,e1) is full dimensional. Its only contact
        # with sum x_i=1 is e1, whose value is strictly below s.
        assert -1-eps*s<0 # zero vertex
        assert eps*(v[0]-s)<0 # contact e1
        for vi in v:
            assert -eta+eps*((1-eta)*vi-s)<0
        assert 1+eps*s>0 and all(1+eps*vi>0 for vi in v)
        ratio=(1+eps*s)**m/prod(1+eps*vi for vi in v)
        assert ratio<1
        assert m*s-sum(v)==m*(s-mean)<0
        # New intercept-simplex determinant is exactly this ratio.
        intercepts=[(1+eps*s)/(1+eps*vi) for vi in v]
        assert prod(intercepts)==ratio
        tilt_checks+=1

locality_checks=matching_checks=0
for m in range(1,41):
    deltas=[F(1,8*m*m*k) for k in (1,2,7,31)]
    deltas += [F(1,64*m*m*m*k) for k in (1,3,11)]
    for delta in deltas:
        a=2*m*delta
        inner=(1-a)**m
        outer=(1+a)**m
        Delta=(outer-inner)/(1-a)**(m-1)
        E=Delta-delta
        assert 0<a<=F(1,4*m)
        assert (1-a)**(m-1)>=F(3,4)
        assert (1+a)**(m-1)<=F(4,3)
        assert 4*m*m*delta<=Delta<=8*m*m*delta
        assert E>=m*delta
        assert max(delta,m*E)<=8*m**3*delta
        # Both coordinate and upper-sum cone bounds are exactly the
        # volume budget outer-inner with the displayed facet factor.
        assert Delta*(1-a)**(m-1)==outer-inner
        assert 1-m*delta+Delta<=1+E
        locality_checks+=1
        if delta<=F(1,64*m**3):
            assert m*E<=F(1,8)
            assert delta+(m-1)*E<=m*E
            assert m*delta+(m-1)*E<=m*E
            matching_checks+=1

print(f'PASS: {tilt_checks} actual full-dimensional facet-tilt sources, '
      f'{locality_checks} exact dimensional locality/cone constants, '
      f'{matching_checks} vertex/facet matching cases (dimensions1..40).')
