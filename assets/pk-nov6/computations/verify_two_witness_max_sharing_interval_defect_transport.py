from fractions import Fraction as F
import sympy as s
count=0
def check(x):
    global count
    assert x
    count+=1
P=[-1,0,1,2]
gf=[0,1,2,4];gr=gf[::-1]
gm=[max(a,b) for a,b in zip(gf,gr)]
gs=[a+b for a,b in zip(gf,gr)]
check(gm==[4,2,2,4]);check(gs==[4,3,3,4])
check(gf[2]==max(1,2*gf[1]))
check(gf[3]==max(3*gf[1],F(3,2)*gf[2],2*gf[2]))
for g in [gf,gr,gm,gs]:
    check(all(g[i+2]-g[i+1]>=g[i+1]-g[i] for i in range(2)))
    # Every extreme anchored relation, not only adjacent midpoints.
    for j,p in enumerate(P):
        for li,l in enumerate(P):
            for ri,r in enumerate(P):
                if l<p<r:
                    check(g[j]<=(F(r-p,r-l)*g[li]+F(p-l,r-l)*g[ri]))

def cap_mass(g,e,p,tilt):
    # cap x + tilt*(z-p)>=0; symmetry handles -x identically.
    return sum(max(F(0),min(2*(1-e*u),(1-e*u)+tilt*(z-p)))
               for z,u in zip(P,g))
for e in [F(0),F(1,10000),F(1,100),F(1,16),F(1,9)]:
    for g,loss,cost in [(gm,10,24),(gs,11,28)]:
        check(sum(2*(1-e*u) for u in g)==8-cost*e)
        check(cap_mass(g,e,0,-1)==3-loss*e)
        check(cap_mass(g,e,1,1)==3-loss*e)
        check(1-4*e<=1-g[1]*e)
        check(1-4*e<3-loss*e)
    check(cap_mass(gm,e,0,-F(1,2))==3-8*e)
    check(cap_mass(gm,e,1,F(1,2))==3-8*e)
    if e:
        check(F(3-10*e,8-24*e)<F(3-11*e,8-28*e)<F(3,8))
check(10-F(3,8)*24==1);check(11-F(3,8)*28==F(1,2))
check(8-F(3,8)*24==-1)
check([min(a,b) for a,b in zip(gf,gr)]==[0,1,1,0])
check(1-F(3,8)*4==-F(1,2));check(2-F(3,8)*4==F(1,2))
check(10-F(3,8)*28==-F(1,2))
e=s.symbols('e')
qmax=(3-10*e)/(8-24*e);qsum=(3-11*e)/(8-28*e)
check(s.diff(qmax,e).subs(e,0)==-s.Rational(1,8))
check(s.diff(qsum,e).subs(e,0)==-s.Rational(1,16))
check(s.expand((3-10*e)*(8-28*e)-(3-11*e)*(8-24*e))==-4*e+16*e**2)
check(s.diff((3-5*e)/(6-6*e),e).subs(e,0)==-s.Rational(1,3))
check(s.cancel((3-5*e)/(6-10*e))==s.Rational(1,2))
for ee in [F(1,10000),F(1,100),F(1,16),F(1,5)]:
    check(1<3-5*ee)
    check((3-5*ee)/(6-6*ee)<F(1,2))
    check((3-5*ee)/(6-10*ee)==F(1,2))
print(f'{count} exact checks PASS')
