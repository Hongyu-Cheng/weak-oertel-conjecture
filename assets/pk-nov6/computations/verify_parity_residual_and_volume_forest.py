"""Exact scalar and homothetic-profile certificates; no numerical premise."""
from fractions import Fraction as F

# Closed residual threshold, including the zero-residual algebra.
for N in [2,4,8,16,32]:
    for rho in [F(1,2),F(1,7),F(1,100)]:
        c=rho/(1+rho)
        assert 0<c<1
        threshold=c/F(N)
        assert threshold/(F(1,N)-threshold)==rho
        assert F(0)/(F(1,N)-F(0))==0

# Exact four-fiber full-body profiles and vanishing-growth bound.
for d in range(1,21):
    for q in [4,5,10,100,1000]:
        eps=F(1,q)
        f=[1-i*eps for i in range(4)]
        w=[x**d for x in f]
        root=[0,1,0,1]
        target=[0,1,1,2]
        assert w[0]>w[2] and w[1]>w[3]
        for i in range(4):
            assert 2*f[target[i]]==f[i]+f[root[i]]
            assert w[target[i]]-w[i]>=F(1,2**d)*(w[root[i]]-w[i])
        R=w[2]+w[3]
        growth=sum(w[target[i]]-w[i] for i in [2,3])
        assert growth==w[1]-w[3]>0
        assert growth/R==F((q-1)**d-(q-3)**d,(q-2)**d+(q-3)**d)
        # A direct mean-value upper bound certifies the limit in (15).
        assert growth/R<=F(2*d*(q-1)**(d-1),(q-3)**d)

print("PASS: exact residual threshold, strict parity maxima, midpoint equality,")
print("volume-growth inequality, and rational vanishing-growth certificate.")
