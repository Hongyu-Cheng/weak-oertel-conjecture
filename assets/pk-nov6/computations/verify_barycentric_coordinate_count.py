from fractions import Fraction as F
from math import comb, factorial

d, N, r, k = 15, 16, 13, 3
volume = sum((-1)**j * comb(r,j) * F(N-j,N)**d for j in range(r+1))
assert volume == F(29158754625,562949953421312)
assert volume-F(1,2)**d == F(11978885441,562949953421312)>0
assert F(N,2)*F(d,N)**d-k == F(5548326153291759,144115188075855872)>0
assert r*F(1,32)+k*F(19,96)==1
assert F(1,32)<F(1,N)<F(19,96)

lower=F(factorial(30)*18**4, factorial(4)*31**30)
assert lower*2**30 == F(
    1245772453542801712398066946425728532480000000,
    550618520345910837374536871905139185678862401)>1
assert F(31,2)*F(30,31)**30-5 == F(
    14136127281855010100881149692719486180828645,
    17761887753093897979823770061456102763834271)>0

# Squaring the Hadamard product avoids irrational square roots.
for N in range(2,31):
    for k in range(1,N+1):
        r=N-k
        squared_product=F(1,4*N)**r * F(N,4)**(k-1) * N
        assert squared_product == F(N)**(2*k-N)/F(2)**(2*N-2)

print('PASS: exact counterexamples, Jensen certificate, and determinant exponents')
