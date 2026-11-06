"""Independent exact checks of the fixed concave-roof comparison."""
from fractions import Fraction as F


def clip(P,u,c):
    result=[]
    for p,q in zip(P,P[1:]+P[:1]):
        a=u[0]*p[0]+u[1]*p[1]+c
        b=u[0]*q[0]+u[1]*q[1]+c
        if a>=0:
            result.append(p)
        if a*b<0:
            t=a/(a-b)
            result.append(tuple(p[i]+t*(q[i]-p[i]) for i in range(2)))
    return result


def area(P):
    if len(P)<3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(P,P[1:]+P[:1])))/2


checks=0
for endpoint0,endpoint1 in [(0,0),(0,1),(1,0),(1,1),(2,1)]:
    for k in [F(1,10),F(1,4),F(1,2),F(4,5),F(9,10)]:
        for height in [F(0),F(1,3),F(2)]:
            if not endpoint0 and not endpoint1 and not height:
                continue
            def psi(s):
                return endpoint0+(endpoint1-endpoint0)*s+height*min(s/k,(1-s)/(1-k))
            b=3*(psi(F(2,3))-psi(F(1,3)))
            a=psi(F(1,3))-b/3
            assert a>=0 and a+b>=0
            def ell(s):
                return a+b*s
            points=sorted(set([F(0),k,F(1,3),F(2,3),F(1)]))
            def integrate(f,left,right):
                knots=[x for x in points if left<=x<=right]
                return sum((q-p)*(f(p)+f(q))/2 for p,q in zip(knots,knots[1:]))
            Z=integrate(psi,F(0),F(1))
            A=integrate(lambda s:psi(s)-ell(s),F(1,3),F(2,3))
            B=(integrate(lambda s:ell(s)-psi(s),F(0),F(1,3))
               +integrate(lambda s:ell(s)-psi(s),F(2,3),F(1)))
            E=integrate(psi,F(1,3),F(2,3))-Z/3
            assert A>=0 and B>=0 and E==(2*A+B)/3
            assert A+B<=3*E
            assert (E==0)==(height==0)
            if E:
                assert E/(3*max(A,B))>=F(1,9)
            # Exact first-order coefficient from the canonical facet law.
            I=integrate(psi,F(1,3),F(2,3))
            V=F(1,2)
            assert ((Z+I)/3-F(4,9)*Z)/V==E/(3*V)
            for epsilon in [F(1,100),F(1,200),F(1,500)]:
                assert 1-epsilon*b>0
                top=(1+epsilon*a)/(1-epsilon*b)
                assert top>=1
                K=[(F(0),F(-1)),(F(1),F(0))]
                K += [(s,epsilon*psi(s)) for s in reversed(points)]
                L=[(F(0),F(-1)),(top,top-1),(F(0),epsilon*a)]
                KL=clip(K,(epsilon*b,F(-1)),epsilon*a)
                J=epsilon**2*(a+b)**2/(2*(1-epsilon*b))
                assert area(K)==V+epsilon*Z
                assert area(L)==(1+epsilon*a)**2/(2*(1-epsilon*b))
                assert area(K)-area(KL)==epsilon*A
                assert area(L)-area(KL)==epsilon*B+J
                TV=1-area(KL)/max(area(K),area(L))
                assert TV==max(epsilon*A,epsilon*B+J)/max(area(K),area(L))
                if not E:
                    tau=(epsilon*(a+b)/(1+epsilon*a))**2
                    assert J/area(L)==tau
                    assert TV==tau
                    deleted=clip(L,(F(1),F(0)),F(-1))
                    assert area(deleted)==J
                checks+=1

# Taylor algebra used by the exact planar one-corner formula:
# sqrt(1+3t)=1+3t/2-9t^2/8+O(t^3).
sqrt_coeff=[F(1),F(3,2),F(-9,8)]
assert sum(sqrt_coeff[i]*sqrt_coeff[2-i] for i in range(3))==0
absolute=[F(4,9),F(-1,3),F(-1,4)]
assert absolute[1]+absolute[0]==F(1,9)
assert sum(absolute)==F(-5,36)
print(f'PASS: {checks} exact roof-area, deficit, TV, and affine-corner cases; '
      'first-variation and one-corner expansion coefficients.')
