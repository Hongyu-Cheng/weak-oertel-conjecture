from fractions import Fraction as F
for e,L in [(F(1,4),F(1)),(F(1,10),F(1)),(F(1),F(1)),(F(2),F(3))]:
    V=4*L*e; I=4*e*e; r=e/L
    B=(V+I)/2
    assert B==2*e*(L+e)==(1+r)*V/2
    assert V/2<=B<=V
    middle=(L+e)**2
    exact=middle/2+B
    assert middle+V>=exact>V/2
    assert middle/V==(1+r)**2/(4*r)
V=F(1); B=F(5,8); gamma=F(4,9)
assert B<2*gamma*V
assert 2*gamma*V-B==F(19,72)
assert V/2>gamma*V
print('PASS: exact two-layer midplane budget, covering-cap masses, and forced middle-volume accounting')
a,b=F(1,4),F(1)
w,I=F(9,16),a
gamma=F(4,9)
assert max(b,w+a+I)==F(17,16)<2*gamma*(a+b)==F(10,9)
K=max(b,w+a+I)/2
U=K/gamma
assert max(gamma*U,K)/(U+a+b)<gamma/2
print('PASS: asymmetric common-core criterion and its explicitly unresolved mass window')
