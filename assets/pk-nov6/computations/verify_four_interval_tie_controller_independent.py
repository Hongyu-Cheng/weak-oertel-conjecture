from fractions import Fraction as F

checks=0
def mass(lo,hi,p,x,t):
    return sum(min(H-L,max(F(0),H-x-t*(i-p)))
               for i,(L,H) in enumerate(zip(lo,hi)))

for j in range(21):
  for k in range(21):
    u=F(j,200);v=F(9*k,1000)
    lo=[F(47,50)+u/2,-F(11,10),-F(23,25),-F(9,100)+v/2]
    hi=[F(26,25)-u/2,F(1),F(23,25),F(9,100)-v/2]
    assert all(lo[i]-2*lo[i+1]+lo[i+2]>=0 for i in range(2))
    assert all(hi[i]-2*hi[i+1]+hi[i+2]<=0 for i in range(2))
    M=sum(H-L for L,H in zip(lo,hi));assert M==F(211,50)-u-v
    Q1=F(11,10)-u/2;Q2=F(11,10)-v
    table1=[(-F(26,25),F(151,50)+u/2-v),
      (-F(47,50)-u,F(78,25)-u/2-v),
      (-F(23,25)+u/2,F(78,25)-u/2-v),
      ((u+v)/4-F(9,200),F(449,200)-u/4-5*v/4),
      ((u-v)/4+F(9,200),F(79,40)-u/4+v/4),
      (F(23,25)+u/2,Q1)]
    table2=[(-F(1),Q2),(-F(13,25)+u/4,F(79,50)+u/4-v),
      (-F(47,100)-u/4,F(173,100)-5*u/4-v),
      (-F(9,100)+v/2,F(211,100)-u-v/2),
      (F(9,100)-v/2,F(211,100)-u-v/2),
      (F(11,10),F(78,25)-u)]
    for p,x,Q,table in [(1,-u/2,Q1,table1),(2,F(0),Q2,table2)]:
      assert [t for t,_ in table]==sorted(t for t,_ in table)
      knots=sorted(set((e-x)/F(i-p) for i in range(4) if i!=p
                       for e in [lo[i],hi[i]]))
      assert knots==sorted(set(t for t,_ in table))
      vals=[mass(lo,hi,p,x,t) for t in knots]
      assert min(vals)==Q and max(vals)==M-Q
      for t,value in table:
        assert mass(lo,hi,p,x,t)==value
        assert Q<=value<=M-Q
        checks+=1
      assert sum(hi[i]-lo[i] for i in range(p+1))>=Q
      assert sum(hi[i]-lo[i] for i in range(p,4))>=Q
      checks+=4
    beta=max(Q1,Q2)/M
    assert (beta<=F(55,211))==(101*u>=110*v and 156*v>=55*u)
    checks+=4

old=F(55,211)
for j in range(1,101):
  u=F(j,1000);v=u/2
  now=(F(11,10)-u/2)/(F(211,50)-3*u/2)
  assert now<old;old=now;checks+=1
assert old==F(105,407)
for j in range(1,101):
  t=F(j,1000)
  now=(F(11,10)-t/2)/(F(211,50)-2*t)
  assert now>F(55,211);checks+=1
print(f'PASS: {checks} exact knot, source-tie, compatibility, and rate-cone checks')
