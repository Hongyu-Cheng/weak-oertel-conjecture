import sys;import sympy as s
h,k=s.symbols('h k', positive=True)
p=h;q=s.Integer(2);r=s.Integer(1);t=s.Integer(1)
a=p*t/((p+r)*(p+t)*(q+t));b=q*r/((p+r)*(q+t)*(q+r));tau=a/(a+b)
S=3*(a+b);l0=(r/(p+r)+tau*t/(p+t))/3
F=p*(a+b)+q*q/((q+t)*(q+r))
print('upperF',s.factor(F),'upperS',s.factor(S),'upperL',s.factor(l0))
print('upperMoment',s.factor(h*h*S*l0))
print('stationary',s.factor(h*h*S*l0-8*k*k/(9*(k+2)**2)))
u=s.symbols('u', positive=True)
fm=8/(9*(k+2));sm=4/(3*(k+2));T=h*S+k*sm
mean=(T*k+3*h*F+3*k*fm)/((h+k)*(T+3))
sub={h:(u*u-1)/(4-u*u),k:2*u*(u*u-1)/(6-u*(u*u-1))}
mu=s.factor(mean.subs(sub));print('mean_param',mu)
print('gapgamma',s.factor(mu-s.Rational(27,64)))
print('gapreverse',s.factor(1-mu-s.Rational(27,64)))
for uv in [s.Rational(11,10),s.Rational(3,2),s.Rational(19,10)]:print('case',uv,'h,k',s.factor(sub[h].subs(u,uv)),s.factor(sub[k].subs(u,uv)),'mean',mu.subs(u,uv))
