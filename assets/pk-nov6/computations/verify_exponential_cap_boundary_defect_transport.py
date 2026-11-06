import sympy as s
p,q,r=s.symbols('p q r',positive=True)
h=1-q/p
x=[h*r/(q+r),h]
rho=s.prod(1-v for v in x);E=1/rho-1
L=(1-sum(x)/E)*s.prod(1+v/E for v in x)
R=rho*(E+h)
P=1-r*r/((p+r)*(q+r))
nuq=1+q*s.diff(P,q)/P
nur=1+r*s.diff(P,r)/P
M=(p+q)/P-r
X0=p/(p+r)
assert s.cancel((L-R)-h*M/(p*X0)*(nuq*nur-P))==0
# One nonzero boundary coordinate is exact equality in every ambient dimension.
x=h;rho=1-h;E=1/rho-1
assert s.cancel((1-x/E)*(1+x/E)-rho*(E+h))==0
print('Exact actual three-phase entropy/boundary transfer and singleton equality PASS')
