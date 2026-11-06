from fractions import Fraction as R

X=R(400,401)**40
Y=R(200,201)**40
F=2*X-Y
mu=R(40,401)/(1-Y/X)-1
D=2*X-R(401,201)*Y
assert 0<F<1 and 0<mu<1 and D>0
ratio=mu*D/(F*(1-F))
assert R(997,1000)<ratio<R(998,1000)
print('Exact finite-phase left-endpoint payment counterexample PASS')
