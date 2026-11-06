"""Exact algebra only; the all-m inequalities are audited separately."""
import sympy as s

E, x, h, m = s.symbols('E x h m', positive=True)
Ep = m*(1+E)/(1-x)
Z = E*((m+1)*x-1)+m*x
D = x*(m*h+(m+1)*E)-E*h
A = (E+x)**2-(E+1)*(E-m*x)
assert s.expand(A-Z-x*(E+x)) == 0
Llog = (Ep-m)/(E-m*x)+m*(Ep+1)/(E+x)-(m+1)*Ep/E
assert s.factor(Llog-m*(m+1)*x*Z/((1-x)*E*(E-m*x)*(E+x))) == 0

# Write R/rho=(E+h)-(E+h)^2 a, with a=(h-x)^m/h^(m+1).
a = s.symbols('a')
R = (E+h)-(E+h)**2*a
Rx = -m*R/(1-x)+Ep*(1-2*(E+h)*a)+(E+h)**2*m*a/(h-x)
a_stationary = 1/((E+h)*(2+(E+h)*(m/(h-x)-(m+1)/h)))
assert s.factor(Rx.subs(a,a_stationary)/R.subs(a,a_stationary)
                -m*(m+1)*x*(1-h)/((1-x)*D)) == 0
Rt_over_R = (E+h)**2*(1-h)*a_stationary/(h-x)**2/R.subs(a,a_stationary)
assert s.factor(Rt_over_R-h*(1-h)/((h-x)*D)) == 0
assert s.expand(E*(h-x)*A-h*(E+x)*Z
                -x*(h*(E+1)*(E-m*x)-E*A)) == 0
hb = E*A/((E+1)*(E-m*x))
hc = x+Z/E
assert s.factor(hb-hc-Z**2/(E*(E+1)*(E-m*x))) == 0

r,y = s.symbols('r y', positive=True)
cubic=(r+(r+1)*y)*(r+((m+1)*r-1)*y+m*(r+1)*y*y)
assert s.expand(cubic).coeff(y,0) == r*r
assert s.factor(s.expand(cubic).coeff(y,1)-r*r*(m+2)) == 0
assert s.factor(s.expand(cubic).coeff(y,2)-r*r*(m+2)*(m+1)/2
                -(-m*(m-1)*r*r/2+2*m*r-1)) == 0
assert s.factor(s.expand(cubic).coeff(y,3)-m*(r+1)**2) == 0
assert s.factor(cubic.subs(r,1/m)
                -(1+(m+1)*y)*(1+y+m*(m+1)*y*y)/m**2) == 0

pade_derivative = ((m-1)/(2+(m-1)*x)
                    +(m+1)/(2-(m+1)*x)-m/(1-x))
assert s.factor(pade_derivative-m*(m-1)*(m+1)*x*x/
                ((1-x)*(2+(m-1)*x)*(2-(m+1)*x))) == 0
print('All-m exact differential, stability, cubic, and Pade identities PASS')
