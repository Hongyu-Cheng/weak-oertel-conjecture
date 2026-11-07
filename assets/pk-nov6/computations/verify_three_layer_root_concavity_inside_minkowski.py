from fractions import Fraction as F
delta=F(1,8);rB=F(7,4)
a=F(1,2);b=F(2);U=rB*rB/2
M=a+b+U;gamma=F(4,9)
assert U==F(49,32) and M==F(129,32)
assert max(a,b,U)<M/2
assert rB-2*delta==F(3,2)
assert F(2)>rB-2*delta
vals=[]
for t in [F(1,16),F(1,8),F(3,16)]:
    assert 0<t and 2*t<F(3,2)
    assert 3*t<=1
    assert 3*(t+delta)<=rB
    assert 2*t<=1 and 2*(t+delta)<=rB
    endpoint=2*gamma*(3*t)**2/2
    middle=gamma*(3*(t+delta))**2/2
    assert endpoint==4*t*t
    assert middle==2*(t+delta)**2
    exact=endpoint+middle
    cap=2*(2*t)**2/2+(2*(t+delta))**2/2
    assert cap==exact
    vals.append(exact)
assert vals==[F(11,128),F(24,128),F(43,128)]
D=4*vals[1]-vals[0]-vals[2]
assert D>0 and D*D<4*vals[0]*vals[2]
assert 441<473
assert gamma*M/2==F(43,48)<1
assert gamma*(F(3,2)**2/2)+a==1
assert gamma*b<gamma*M/2
assert gamma*M/2-gamma*b==F(1,144)
print('PASS: actual nonheavy unequal-simplex fibers, all-cap exact profile, interior root-concavity failure, and explicit OC-safe point')
