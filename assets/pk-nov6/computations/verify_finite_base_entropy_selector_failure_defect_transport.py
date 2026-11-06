from fractions import Fraction as F

checks=0
def check(q):
    global checks
    assert q
    checks+=1

def clip(poly,a,b,c):
    ans=[]
    for P,Q in zip(poly,poly[1:]+poly[:1]):
        p=a*P[0]+b*P[1]-c
        q=a*Q[0]+b*Q[1]-c
        if p>=0: ans.append(P)
        if (p<0<q) or (q<0<p):
            t=p/(p-q)
            ans.append((P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1])))
    return ans

def area(poly):
    if len(poly)<3: return F(0)
    return abs(sum(P[0]*Q[1]-P[1]*Q[0] for P,Q in zip(poly,poly[1:]+poly[:1])))/2

T=[(F(2),F(-1)),(F(-1),F(2)),(F(-1),F(-1))]
V=area(T)
check(V==F(9,2))
vols=[]
caps=[]
for z,r in [(-1,1),(0,3),(1,4)]:
    poly=[(r*x,r*y) for x,y in T]
    vols.append(area(poly))
    caps.append(area(clip(poly,F(1),F(0),F(8*z))))
check(vols==[V,9*V,16*V])
check(caps==[V,4*V,F(0)])
check(sum(vols)==26*V)
check(sum(caps)==5*V)
check(sum(caps)<F(2,9)*sum(vols))
alpha=F(1,3)
weights=[vols[0]/(1-alpha)**4,vols[1],vols[2]/(1+alpha)**4]
E=sum(weights)
check(weights[0]==weights[2]==F(81,16)*V)
check(E==F(153,8)*V)
check(sum(v/L**3 for v,L in zip(vols,[1-alpha,F(1),1+alpha]))==E)
check(E>vols[2]>vols[0])
check([v/E for v in weights]==[F(9,34),F(8,17),F(9,34)])
check(-weights[0]+weights[2]==0)
check(F(4,9)*vols[2]>F(2,9)*sum(vols))
# Direct discrete entropy KKT scale checks for a grid of perfect fourth powers.
for aa in range(1,5):
    for bb in range(1,5):
        al=F(bb-aa,bb+aa)
        ww=F(aa+bb,2)**4
        check(F(aa**4)/(1-al)**4==ww)
        check(F(bb**4)/(1+al)**4==ww)
        check(F(aa**4)/(1-al)**3+F(bb**4)/(1+al)**3==2*ww)
print(f'{checks} exact checks PASS')
