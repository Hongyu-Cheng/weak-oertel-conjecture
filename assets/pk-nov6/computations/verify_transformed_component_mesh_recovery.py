"""Exact block-Jacobian and dense-versus-fixed component mesh checks."""
from fractions import Fraction as F

for L in range(6,91,3):
    h=F(1,L*L); eps=h*h; a=F(1,L); M=4*eps
    A0=F(1); C0=1/(4*eps)
    A1=1/(2*a); C1=a/(2*eps); B1=-1/(2*eps)
    assert A0*C0==A1*C1==1/M
    assert h*A0==h
    assert h*A1==F(1,2*L)
    assert (h/2)/M==F(L*L,8)
    # Exact sample covolume times continuous Jacobian.
    assert (h*A0)*C0==h/M
    assert (h*A1)*C1==h/M
    points=[(-a,F(-1)),(a,F(1)),(F(0),2*eps/a)]
    assert all((u/h).denominator==1 for u,x in points)
    assert [(A1*u,B1*u+C1*x) for u,x in points]==[
        (F(-1,2),F(0)),(F(1,2),F(0)),(F(0),F(1))]
    N=int(a/h)
    assert N==L
    tent=sum((1-F(abs(i),N) for i in range(-N,N+1)),F(0))
    assert tent==N
    sampled_second=h*(2*eps/a)*tent
    assert sampled_second==2*eps

print('PASS: exact block Jacobians, transformed meshes, and sampled tent masses.')
