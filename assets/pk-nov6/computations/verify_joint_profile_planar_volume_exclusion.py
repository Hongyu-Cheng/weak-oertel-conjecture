from fractions import Fraction as F

checks = 0
def check(value, message):
    global checks
    assert value, message
    checks += 1

a,b,c = F(1,4),F(121,100),F(1)
gamma=F(4,9); M=a+b+c; target=gamma*M/2
x=F(302,675); s=a-target+x; t=1-x; Z=4*t+b-s
check(M==F(123,50), 'total')
check(target==F(41,75), 'target')
check(max(a,b,c)<M/2, 'strict noheavy')
check(F(1,2)+F(11,10)<=2, 'whole BM compatible roots')
check(target-a==F(89,300)<x, 'full endpoint exception')
check(s==F(407,2700)>0, 'positive residual s')
check(t==F(373,675)>0, 'positive middle residual t')
check(4*t-b==F(2701,2700)>0, 'first legal square')
check(Z==F(2207,675)>0, 'second legal square')
check(16*b*t-Z*Z==F(703,91125)>0, 'strict radical gap')
check(1+a/4==F(17,16), 'profile left')
check(F(9,16)*target+F(27,16)*x==1+a/4, 'profile equality')
check((1+a)/2>target, 'two-cap exclusion')

# The independently feasible remaining scalar menu is not asserted
# geometrically realizable or genuinely critical.
a,b,c=F(1,10),F(1),F(1)
Q=F(93,200); target=F(7,15)
q=[F(37,100),F(367,800),F(367,800)]
U=[F(19,200),F(1,160),F(1,160)]; V=[F(0)]*3
check(Q<target, 'remaining row below target')
check(gamma*(a+b+c)/2==target, 'remaining target')
check(max(a,b,c)<(a+b+c)/2, 'remaining strict noheavy')
check(a<1 and b==1, 'remaining whole BM roots: sqrt(a)+1<2')
check(sum(sorted(q,reverse=True)[:2])+sorted(q,reverse=True)[2]/4==F(101,100)>=1, 'remaining K profile')
check(sum(sorted(U,reverse=True)[:2])+sorted(U,reverse=True)[2]/4==F(329,3200)>=a, 'remaining A profile')
for j,(uj,qj,vj) in enumerate(zip(U,q,V)):
    check(uj+qj+vj==Q, f'row {j} budget')
    check(0<uj<a and vj==0 and 0<qj<1, f'row {j} statuses')
    check(uj+vj<=a, f'row {j} saturated tilt')
    check(Q<=3*qj, f'row {j} equalized tilt')
    r=a-uj; w=1-qj
    # sqrt(r)+1 <= 2 sqrt(w): equivalently
    # 4w-r-1 >= 2sqrt(r), after two legal squarings.
    z=4*w-r-1
    check(z>0 and z*z>=4*r, f'row {j} exact residual BM')
check(max(q)>=gamma, 'remaining middle centroid coverage mass')
check(max(U)>=gamma*a, 'remaining A centroid coverage mass')
print(f'{checks} exact rational checks passed.')
