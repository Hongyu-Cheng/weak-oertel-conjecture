"""Exact, complete one-normal-dimensional depth certificate."""
from fractions import Fraction as F

checks=0
def check(value):
    global checks
    assert value
    checks+=1

I=[(F(47,50),F(26,25)),(F(-11,10),F(1)),
   (F(-23,25),F(23,25)),(F(-9,100),F(9,100))]
lo=[I[j+1][0]-I[j][0] for j in range(3)]
up=[I[j+1][1]-I[j][1] for j in range(3)]
check(lo==[F(-51,25),F(9,50),F(83,100)])
check(up==[F(-1,25),F(-2,25),F(-83,100)])
check(lo==sorted(lo));check(up==sorted(up,reverse=True))
M=sum(u-l for l,u in I);Q=F(11,10)
check(M==F(211,50));check(Q/M==F(55,211))
check(Q/M-F(1,4)==F(9,844))
for l,u in I: check(u-l<M/2)
for start in range(4):
    for stop in range(start,4):
        if (start,stop)==(0,3): continue
        mass_block=sum(I[z][1]-I[z][0] for z in range(start,stop+1))
        quota=F(1,2) if start==stop else F(1)
        check(quota-mass_block/M>=F(1,422))

def mass(p,t):
    return sum(max(F(0),min(u-l,u-t*(z-p))) for z,(l,u) in enumerate(I))

tables={1:[(F(-26,25),F(151,50)),(F(-47,50),F(78,25)),
           (F(-23,25),F(78,25)),(F(-9,200),F(449,200)),
           (F(9,200),F(79,40)),(F(23,25),Q)],
        2:[(F(-1),Q),(F(-13,25),F(79,50)),
           (F(-47,100),F(173,100)),(F(-9,100),F(211,100)),
           (F(9,100),F(211,100)),(F(11,10),F(78,25))]}
for p,table in tables.items():
    knots=sorted({e/(z-p) for z,lr in enumerate(I) if z!=p for e in lr})
    check(knots==[t for t,v in table])
    for t,v in table:
        check(mass(p,t)==v)
        check(Q<=v<=M-Q)
    for (s,fs),(t,ft) in zip(table,table[1:]):
        # The exact complete knot list ensures affinity on this whole cell.
        for q in range(1,20):
            lam=F(q,20)
            check(mass(p,(1-lam)*s+lam*t)==(1-lam)*fs+lam*ft)
    check(mass(p,knots[0]-100)==table[0][1])
    check(mass(p,knots[-1]+100)==table[-1][1])
    check(min(v for t,v in table)==Q)
    check(max(v for t,v in table)==M-Q)
    left=sum(u-l for z,(l,u) in enumerate(I) if z<=p)
    right=sum(u-l for z,(l,u) in enumerate(I) if z>=p)
    check(left>Q);check(right>Q)

# All four selected actual caps, with strict full/empty statuses.
caps=[(1,F(1),F(-1),[1,0,-1,-1]),
      (1,F(-1),F(-93,100),[-1,0,-1,-1]),
      (2,F(1),F(2),[-1,-1,0,1]),
      (2,F(-1),F(2),[-1,-1,0,1])]
for p,u,a,statuses in caps:
    total=F(0)
    for z,((l,h),status) in enumerate(zip(I,statuses)):
        ends=[u*l+a*(z-p),u*h+a*(z-p)]
        if status==1:
            check(min(ends)>0);total+=h-l
        elif status==-1:
            check(max(ends)<0)
        else:
            check(min(ends)<0<max(ends))
            total+=(h if u>0 else -l)
    check(total==Q)

check(F(47,50)-F(93,100)==F(1,100))
check(F(1,2)==F(1,2)) # prescribed response weights / Gamma_1
for t in [F(-47,50)+F(k,2000) for k in range(41)]:
    check(mass(1,t)==M-Q)
    check(-t<=I[0][0])
for k in range(1,81):
    t=F(23,25)+F(k,20)
    check(mass(1,t)==Q)
    check(-t<I[0][0])

print(f"{checks} exact checks PASS")
