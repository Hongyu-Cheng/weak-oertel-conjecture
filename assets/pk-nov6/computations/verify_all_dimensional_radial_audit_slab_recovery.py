"""Independent weighted Schur factors, deficient-rank calculus, and nonlinear null example."""
from itertools import product
from math import factorial
import sympy as s

checks=0
def eq(a,b):
    global checks
    assert s.factor(a-b)==0,(a,b)
    checks+=1
def yes(p):
    global checks
    assert p
    checks+=1

t=s.symbols('t')
# A genuine full-dimensional thin projection with the noncoordinate rank-two
# complete base z3=z1+z2, z1,z2 in {-1,0,1}.
P=[(i,j,i+j) for i,j in product([-1,0,1],repeat=2)]
r0=[1-s.Rational(z[0]**2+z[1]**2,30) for z in P]
vel=[s.Rational(z[0]+2*z[1],200)+s.Rational(z[0]**2-z[1]**2,300) for z in P]
for d in range(2,9):
    V=s.Rational((d+1)**d,factorial(d));c=s.Rational(d**d,factorial(d))
    gamma=s.Rational(d,d+1)**d
    eq(c,gamma*V);yes(2*gamma<1)
    H=s.eye(d-1)-s.ones(d-1)/d
    eq(H.det(),s.Rational(1,d));yes(all(e>0 for e in H.eigenvals()))
    weights=[r**(d-2) for r in r0]
    G=s.Matrix(3,3,lambda i,j:sum(w*z[i]*z[j] for w,z in zip(weights,P)))
    yes(G.rank()==2);Gp=G.pinv()
    m=s.Matrix([sum(w*v*z[i] for w,v,z in zip(weights,vel,P)) for i in range(3)])
    eq((G*Gp*m-m).norm()**2,0)
    bp=-d*Gp*m
    F=sum((d*(r+t*v)+t*(s.Matrix(z).T*bp)[0])**d for r,v,z in zip(r0,vel,P))/factorial(d)
    Q0=c*sum(r**d for r in r0);M=V*sum((r+t*v)**d for r,v in zip(r0,vel))
    mm=(m.T*Gp*m)[0]
    eq(s.diff(F,t,2).subs(t,0),c*d*(d-1)*(sum(w*v*v for w,v in zip(weights,vel))-mm))
    eq(s.diff(M*Q0/F,t).subs(t,0),0)
    eq(s.diff(M*Q0/F,t,2).subs(t,0),V*d*(d-1)*mm)
    # Full abstract sampled-array rank, correctly separated from admissibility.
    Z=s.Matrix([[w*z[i] for w,z in zip(weights,P)] for i in range(3)])
    yes((Z.T*Gp*Z).rank()==2)
    # Invisible coefficient (1,1,-1) vanishes on every actual base.
    yes(all(z[0]+z[1]-z[2]==0 for z in P))

js=[-2,-1,0,1,2]
rs=[s.Rational(1,2),s.Integer(1),s.Rational(5,4),s.Integer(1),s.Rational(1,2)]
vs=[0,2,1,0,2]
eq(sum(r*v*z for r,v,z in zip(rs,vs,js)),0)
eq(sum((r+t*v)**2*z for r,v,z in zip(rs,vs,js)),4*t*t)
for i in range(1,4):yes(rs[i-1]-2*rs[i]+rs[i+1]<0)
for tv in [s.Rational(-1,100),s.Rational(1,100)]:
    new=[r+tv*v for r,v in zip(rs,vs)]
    yes(min(new)>0)
    for i in range(1,4):yes(new[i-1]-2*new[i]+new[i+1]<0)
    yes(sum(r*r*z for r,z in zip(new,js))>0)
print(f'PASS {checks} exact checks')
