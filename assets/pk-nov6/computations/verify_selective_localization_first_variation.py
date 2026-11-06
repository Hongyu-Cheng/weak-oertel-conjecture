"""Exact rational checks for minimal-cover one-vertex variation formulas."""
from fractions import Fraction as F

n=1
d=2
N=2**n
c=F(1,4)
q=(1-c)**d
tau=q/N
D_same=d*c*(1-c)**(d-1)
D_other=q
assert q==F(9,16)
assert tau==F(9,32)
assert D_same==F(3,8)
assert D_other==F(9,16)
assert -F(d,N)*(1-c)**(d-1)*(F(1,d+1)-c)==-F(1,16)
assert q*F(N-1,N*N)==F(9,64)
assert -q/F(N*N)==-F(9,64)

# Standard simplex gradients for lambda0,lambda1,lambda2.
grad=[(-1,-1),(1,0),(0,1)]
for j in range(3):
    for hx in range(-4,5):
        for hy in range(-4,5):
            if hx==hy==0: continue
            r=[F(a*hx+b*hy) for a,b in grad]
            assert sum(r)==0 and max(r)>0
            affected=[F(1,N)*(D_same if i==j else D_other)*r[i]
                      +q*F(N-1,N*N)*r[j] for i in range(3)]
            unaffected=[-q*F(1,N*N)*r[j]]*3
            assert max(affected+unaffected)>0

# General sign proof is in the note; this finite check verifies its rational
# specialization and catches coefficient/normalization errors only.
print("PASS: exact first-variation constants and rational specialization")
