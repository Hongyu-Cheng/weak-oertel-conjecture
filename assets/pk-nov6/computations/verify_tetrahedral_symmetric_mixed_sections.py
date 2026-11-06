from fractions import Fraction as F

def f(x):return 9*(1-3*x+4*x**3)/(17-43*x)
checks=0
for n in range(101):
 a=F(1,6)+F(n,600);b=F(1,2)-a
 A=F(27,2)*b*(2*a-b);B=F(27,2)*a*(2*b-a);Q=24*a*b
 FA=27*a*b*b;FB=27*a*a*b;FQ=1-12*a*a+16*a**3
 RV=(B*FA+A*FB)/(A+B)
 assert RV==27*a*a*b*b/(1-6*(a*a+b*b))
 assert F(27,64)<=RV<=F(1,2)
 assert (B*FQ+Q*FB)/(B+Q)==f(a)
 assert (Q*FA+A*(1-FQ))/(A+Q)==f(b)
 for x in (a,b):
  assert F(4,9)<f(x)<=F(1,2)
  assert F(1,2)-f(x)==(1-3*x)*(24*x*x+8*x-1)/(2*(17-43*x))
  assert f(x)-F(4,9)==(13-71*x+324*x**3)/(9*(17-43*x))
 positive=[(A,FA),(B,1-FB),(Q,FQ)]
 negative=[(A,1-FA),(B,FB),(Q,1-FQ)]
 for s,c in positive:
  for t,d in negative:
   if s and t:assert (t*c+s*d)/(s+t)>=F(27,64)
   elif not s:assert c==F(1,2)
   elif not t:assert d==F(1,2)
 checks+=1
assert 1053**2-71**2*213==35076
print('Exact coefficient, pair enumeration and endpoint checks passed:',checks)
