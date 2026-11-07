from fractions import Fraction as F
exec(open('./verify_free_mixture_selector_simplex_obstruction.py').read())
gamma=F(5,6)**5
l=F(1,6)-F(1,300000)
s0=l/F(7,10)
assert s0>F(1,5)
capbound=l**5/(s0*((1-s0)/4)**4)
assert capbound>gamma*(1+F(1,200000))
assert 1-(1-T)/F(7,10)>F(1,2)
assert -F(2,11)*F(3,7)+F(20,11)*F(15,56)==F(9,22)>0
assert F(1,1024)>F(1,100000)
assert 1-F(9,10)*gamma-F(16,5)*gamma*F(1,100000)>0
print('PASS: every one-vertex middle-trace branch at the explicit escape point')
assert F(4,5)**4-F(12,100000)>gamma*(1+F(1,200000))
print('PASS: exact multi-vertex gap using the proved signed-exponential comparison')
