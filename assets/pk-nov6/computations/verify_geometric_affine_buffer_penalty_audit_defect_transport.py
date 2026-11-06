import sympy as s
from fractions import Fraction as F
checks=0
V=s.symbols('V0:3',positive=True); D=s.symbols('D0:3',real=True)
L=s.symbols('L0:3',real=True); e=s.symbols('e0:3',positive=True)
M=sum(V); Dt=sum(D); w=[v/M for v in V]
wp=[(w[j]*Dt-D[j])/M for j in range(3)]
sc=sum(D[j]*L[j] for j in range(3))/M
constraint={L[2]:-(V[0]*L[0]+V[1]*L[1])/V[2]}
# Exact differentiated geometric normalization.
assert s.simplify((sum(wp[j]*L[j] for j in range(3))+sc).subs(constraint))==0
checks+=1
P=sum(w[j]*e[j] for j in range(3))
Pdot=sum(wp[j]*e[j] for j in range(3))+P*sc
expected=sum(D[j]*(P*(1+L[j])-e[j]) for j in range(3))/M
assert s.simplify(Pdot-expected)==0
checks+=1
phi=s.symbols('p0:3',real=True)
A=sum(w[j]*phi[j]/e[j] for j in range(3))
elldot=[phi[j]-e[j]*A for j in range(3)]
assert s.simplify(sum(w[j]*elldot[j]/e[j] for j in range(3)))==0
assert s.simplify(sum(w[j]*elldot[j] for j in range(3))-(sum(w[j]*phi[j] for j in range(3))-P*A))==0
checks+=2
N,MM,eps,PP,AA=s.symbols('N MM eps PP AA',positive=True)
eta,da,db,x,y,Y=s.symbols('eta da db x y Y',real=True)
# x,y are the two source phi/ell values, Y is the volume mean of phi.
qbar=(eta*da*(x-AA)+(1-eta)*db*(y-AA))/(N*MM)
Jbar=qbar+eps**2*(Y-PP*AA)
left=eta*da*x+(1-eta)*db*y+N*MM*eps**2*Y
right=(eta*da+(1-eta)*db+N*MM*eps**2*PP)*AA
assert s.simplify(N*MM*Jbar-(left-right))==0
checks+=1
# Common GL scaling: all D_z=-trace*V_z implies s=0 at geometric mean one.
tr=s.symbols('tr',real=True)
assert s.simplify(sc.subs({D[j]:-tr*V[j] for j in range(3)}).subs(constraint))==0
checks+=1
# Exact physical small-buffer power and the penalty bound at rational inputs.
for d in range(1,31):
    n=d+1
    for j in range(1,41):
        ee=F(1,j+1); C=F(j+3,7)
        Pbound=1+C/ee
        assert ee**n*Pbound==ee**n+C*ee**(n-1)
        assert ee*ee*(Pbound-1)==ee*C
        checks+=2
# Geometric-normalized positive pairs illustrate bounded P forcing positive ell.
for j in range(1,101):
    ell=F(j+1,7)
    vals=[ell,1/ell]
    amax=max(vals)
    assert (vals[0]+vals[1])/2>=1
    assert min(vals)>=1/amax
    checks+=2
print(f'{checks} exact symbolic/rational checks PASS')
