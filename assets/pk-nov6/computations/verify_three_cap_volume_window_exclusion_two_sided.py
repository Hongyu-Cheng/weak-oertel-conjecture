from fractions import Fraction as F
a=F(1,4);b=F(121,100);Q=F(41,75);x=F(302,675)
s=a-Q+x;t=1-x;Z=4*t+b-s
assert s==F(407,2700) and t==F(373,675) and Z==F(2207,675)
assert F(484,25)*t-Z*Z==F(703,91125)>0
assert 4*t>b
assert Q-a==F(89,300)<x
assert 1+a/4==F(27,16)*x+F(9,16)*Q==F(17,16)
assert F(5,8)>Q
print('PASS: strict residual-root bound and exact three-cap distal contradiction.')
