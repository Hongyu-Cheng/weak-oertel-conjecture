"""Exact certificates for the companion H height/menu note; not an OC proof."""
from fractions import Fraction as F
import sympy as s

checks = 0
def check(a, b):
    global checks
    assert s.simplify(a-b) == 0, (a, b)
    checks += 1

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

K = [(F(4),F(-2)),(F(-4,5),F(8,5)),(F(-4,5),F(-4,5))]
E,V=F(9,2),F(144,25)
normals=[(1,0),(0,1),(-1,-1)]
def cap_edge_interval(a,b,n):
    va,vb=dot(a,n),dot(b,n)
    if va>=0 and vb>=0: return F(0),F(1)
    if va<=0 and vb<=0: return None
    root=-va/(vb-va)
    return (F(0),root) if va>=0 else (root,F(1))

def power_integral(pa,pb,lo,hi,p):
    slope=pb-pa
    if not slope: return (hi-lo)*pa**(-p)
    return ((pa+slope*hi)**(1-p)-(pa+slope*lo)**(1-p))/(slope*(1-p))

expected=[(F(4,9),F(1,3),F(25,36),F(49,108)),
          (F(4,9),F(1,2),F(8,27),F(35,81)),
          (F(4,9),F(1,2),F(8,27),F(35,81))]
for n, target in zip(normals,expected):
    cone=energy=volume=F(0)
    for a,b in zip(K,K[1:]+K[:1]):
        interval=cap_edge_interval(a,b,n)
        if interval is None: continue
        lo,hi=interval
        flux=cross(a,b)
        pa,pb=1+a[0]/4,1+b[0]/4
        cone += flux*power_integral(pa,pb,lo,hi,2)/(2*E)
        energy += flux*power_integral(pa,pb,lo,hi,3)/(2*E)
        volume += flux*(hi-lo)/(2*V)
    height=F(2,3)*energy+F(1,3)*volume
    for actual,want in zip((cone,energy,volume,height),target):check(actual,want)

t,q=s.symbols('t q',real=True)
G=s.sqrt((1-t+t*t)/2)
Fq=(2-t+q*G)**2/(9*(1-t))
check(s.simplify(s.diff(Fq,t).subs(t,0)),0)
check(s.diff(Fq,t,2).subs({t:0,q:0}),s.Rational(2,9))
check(s.factor(Fq.subs(q,0)-s.Rational(4,9)),t*t/(9*(1-t)))
Q=12*t*t-12*t+4
check(s.integrate(Q,(t,0,1)),2)
check(s.Rational(2,3)*s.integrate(Q,(t,s.Rational(1,3),1)),s.Rational(64,81))
check((s.Rational(4,9)+s.Rational(64,81))/3,s.Rational(100,243))
check(s.Rational(4,9)-s.Rational(100,243),s.Rational(8,243))

N,beta,A,B,x=s.symbols('N beta A B x',positive=True)
f=(A*x**(-N)+B)**(-1/beta)
positive_factor=f*(N/beta)*A/(x*x*(A+B*x**N)**2)
check(s.simplify(s.diff(f,x,2)/positive_factor-
                 ((N/beta-1)*A-(N+1)*B*x**N)),0)

# Exact one-group fixed-menu stress algebra, including width normalization.
W,bet,Abar,M,J,D=s.symbols('W bet Abar M J D',real=True)
loss=(W-bet)*D+Abar*(D-J)/(2*M)
density_integral=(W-bet+Abar/(2*M))*D-Abar*J/(2*M)
check(s.expand(loss-density_integral),0)
print(f'PASS: {checks} exact rational/symbolic height, cap, and stress certificates')
