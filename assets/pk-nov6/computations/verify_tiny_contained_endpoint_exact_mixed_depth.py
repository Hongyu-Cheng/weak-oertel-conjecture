"""Exact checks for the proved all-direction small-endpoint theorem."""
from fractions import Fraction as F
from itertools import permutations,product


def clip(P,u,c):
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        a=sum(x*y for x,y in zip(u,p))+c
        b=sum(x*y for x,y in zip(u,q))+c
        if a>=0:
            out.append(p)
        if a*b<0:
            t=a/(a-b)
            out.append(tuple(p[i]+t*(q[i]-p[i]) for i in range(2)))
    return out


def area(P):
    if len(P)<3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(P,P[1:]+P[:1])))/2


T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
V=F(1,2);Gamma=F(4,9)
As=[]
for r in [F(1,20),F(1,10),F(3,20)]:
    for shift in [(0,0),(1-r,0),(0,1-r),((1-r)/3,(1-r)/3)]:
        As.append([(F(shift[0])+r*x,F(shift[1])+r*y) for x,y in T])
As.append([(F(0),F(0)),(F(3,20),F(0)),(F(1,50),F(1,5))])
for A in As:
    alpha=area(A)/V
    # rho2 is the positive root of 81 rho^2+108 rho-4=0.
    assert alpha>0 and 81*alpha*alpha+108*alpha-4<0
    assert all(x>=0 and y>=0 and x+y<=1 for x,y in A)

profile_checks=0
for r in [F(i,100) for i in range(101)]:
    mean=(1+r)/3
    if r<=F(1,2):
        f=(2-r)**2/(9*(1-r))
        q=(1-2*r)**2/(9*(1-r))
        value=(5*r*r-4*r+1)/(9*(1-r))
        v=1-r
        assert value==(5*v+2/v-6)/9
        assert (9*value+6)**2-40==(5*v-2/v)**2
    else:
        f=1-(1+r)**2/(9*r)
        q=0
        value=(3-r-1/r)/9
        assert value>=F(1,18)
    assert f+q-Gamma==value>0
    profile_checks+=1

cap_checks=0
normals=set()
for r in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
    normals.update(permutations([F(0),r,F(1)]))
for A in As:
    a=area(A)
    for values in normals:
        u=(values[1]-values[0],values[2]-values[0])
        const=values[0];mean=sum(values)/3
        own=area(clip(T,u,const-mean))
        for beta in [F(i,4) for i in range(-8,9)]:
            left=area(clip(A,u,const-mean-beta))
            right=area(clip(T,u,const-mean+beta))
            assert own+left+right>=Gamma*V+a
            # Distinguished threshold 2mean-min values has min=0.
            qcap=area(clip(T,u,const-2*mean))
            assert left+right>=min(a,qcap)
            cap_checks+=1
    # The finite canonical cover uses the same coefficient 2.
    for u,const in [((-1,-1),1),((1,0),0),((0,1),0)]:
        Pmasses=[area(clip(K,u,F(const)-2*z-F(1,3)))
                 for z,K in [(-1,A),(0,T),(1,T)]]
        Qmasses=[area(clip(K,u,F(const)+2*(z-1)-F(1,3)))
                 for z,K in [(-1,A),(0,T),(1,T)]]
        assert Pmasses==[a,Gamma*V,0]
        assert Qmasses==[0,0,Gamma*V]

base_checks=0
for n in range(1,6):
    cube=list(product([0,1],repeat=n));zero=(0,)*n
    for mask in cube:
        I=[i for i,x in enumerate(mask) if x]
        k=len(I)
        if not k:
            continue
        p=tuple(-x for x in mask)
        assert sum(p)==-k
        assert sum(p[i] for i in I)+k==0
        assert all(sum(w[i] for i in I)+k>=1 for w in cube)
        for w in cube:
            if w==zero:
                continue
            def delta(z):
                return ((k+1)*sum(1-z[i] for i in range(n) if w[i])
                        +sum(z[i] for i in range(n) if not w[i]))
            assert delta(w)==0 and delta(p)>=1
            j=sum(w[i] for i in I)
            s=sum(w[i] for i in range(n) if i not in I)
            assert delta(p)==(2*k+3)*j+(k+1)*s-k
            for v in cube:
                if v!=w:
                    assert delta(v)>=1
                    base_checks+=1

for d in range(2,12):
    assert F(d-1,d+1)**d>0

print(f'PASS: {profile_checks} exact planar-profile checks, {cap_checks} '
      f'actual coupled planar cap checks, finite canonical upper budgets, '
      f'and {base_checks} binary isolation inequalities. '
      'The note proves all dimensions, normals, and sufficiently small masses.')
