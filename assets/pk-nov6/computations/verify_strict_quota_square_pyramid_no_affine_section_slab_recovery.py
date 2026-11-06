from fractions import Fraction as F
from itertools import product

P=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,0),(0,0,1),(0,0,2)]
checks=0
actual=[]
for x,y,z in product(range(-1,2),range(-1,2),range(3)):
    if abs(x)+abs(y)<=1-F(z,2): actual.append((x,y,z))
assert set(actual)==set(P);checks+=1
assert len({tuple(v%2 for v in p) for p in P})==4;checks+=1
D=F(203,220); side=F(11,20)
assert D-side==F(41,110)>0;checks+=1
assert (1+F(1,10))/2==side;checks+=1
width=D+side
assert width==F(81,55);checks+=1
Vo=width*side
assert Vo==F(81,100);checks+=1
assert (1+F(4,5))/2==F(9,10);checks+=1
w=[F(1),F(1,100),F(1),F(1,100),Vo,Vo*F(9,10)**2,Vo*F(4,5)**2]
assert w[5:]==[F(6561,10000),F(324,625)];checks+=1
M=sum(w)
assert M==F(8009,2000);checks+=1
rules=[((1<<0)|(1<<1),4),((1<<2)|(1<<3),4),((1<<4)|(1<<6),5)]
closed=[]; gaps=[]
for mask in range(1,(1<<7)-1):
    if any((mask&support)==support and not(mask>>target&1) for support,target in rules):continue
    ids=[i for i in range(7) if mask>>i&1]
    k=len({tuple(v%2 for v in P[i]) for i in ids})
    gap=F(k)*M/4-sum(w[i] for i in ids)
    assert gap>0,(ids,k,gap)
    closed.append(mask);gaps.append(gap);checks+=1
assert len(closed)==82;checks+=1
assert min(gaps)==F(9,8000);checks+=1
assert sum(1 for gap in gaps if gap==F(9,8000))==2;checks+=1
# The three independent representation identities determine arbitrary affine data.
for ho,A,B,C in product([F(-2,3),F(0),F(5,7)],repeat=4):
    h=[ho+A*x+B*y+C*z for x,y,z in P]
    assert h[0]+h[1]==2*h[4] and h[2]+h[3]==2*h[4] and h[6]+h[4]==2*h[5]
    checks+=1
print(f'PASS {checks} exact checks; 82 proper closed minors; minimum quota slack 9/8000; affine-selection gap 41/110')
