"""Exact constructive checks for selected critical star covers, including the cubic path."""
from fractions import Fraction as F
from itertools import product


class Series:
    """Truncated exact series through degree three."""
    def __init__(self, *c):
        self.c = tuple(F(c[i]) if i < len(c) else F(0) for i in range(4))
    @staticmethod
    def cast(x):
        return x if isinstance(x, Series) else Series(x)
    def __add__(self, x):
        x = self.cast(x)
        return Series(*(a+b for a,b in zip(self.c,x.c)))
    __radd__ = __add__
    def __neg__(self):
        return Series(*(-a for a in self.c))
    def __sub__(self, x):
        return self+-self.cast(x)
    def __rsub__(self, x):
        return self.cast(x)-self
    def __mul__(self, x):
        x = self.cast(x)
        return Series(*(sum(self.c[j]*x.c[i-j] for j in range(i+1)) for i in range(4)))
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = self.cast(x)
        out = [1/x.c[0]]
        for i in range(1,4):
            out.append(-sum(x.c[j]*out[i-j] for j in range(1,i+1))/x.c[0])
        return self*Series(*out)
    def __rtruediv__(self,x):
        return self.cast(x)/self
    def __pow__(self,n):
        out = Series(1)
        for _ in range(n):
            out *= self
        return out


def det(matrix):
    a = [row[:] for row in matrix]
    ans = 1
    for j in range(len(a)):
        pivot = a[j][j]
        assert (pivot.c[0] if isinstance(pivot, Series) else pivot) != 0
        ans *= pivot
        for i in range(j+1,len(a)):
            factor = a[i][j]/pivot
            for k in range(j+1,len(a)):
                a[i][k] -= factor*a[j][k]
    return ans


def cap_formula(w,a):
    m,d = len(a),len(a)-1
    vol = det(w)
    caps = []
    for i in range(m):
        value = vol*(w[i][i]-a[i])**d
        for j in range(m):
            if i != j:
                value /= w[i][i]-w[i][j]
        caps.append(value)
    return vol,caps


def derivative(b,a):
    m,d = len(a),len(a)-1
    trace = sum(b[i][i] for i in range(m))
    f = []
    for i in range(m):
        row = sum(b[i][j] for j in range(m) if i != j)
        f.append((1-a[i])**d*(trace+row+d*(1/(1-a[i])-1)*b[i][i]))
    return trace,f


def inverse(f,a):
    m,d = len(a),len(a)-1
    z = [f[i]/(d*(1-a[i])**(d-1)) for i in range(m)]
    total = sum(z)
    return [[z[i] if i==j else z[i]-total/d for j in range(m)] for i in range(m)]


def improve(a,i,j,sign=1):
    m,d = len(a),len(a)-1
    e = [[F(0) for _ in range(m)] for _ in range(m)]
    e[i][j],e[j][j] = F(sign),F(-sign)
    f = derivative(e,a)[1]
    neutral = inverse(f,a)
    big_h = sum(1/(d*(1-x)**(d-1)) for x in a)
    jvalue = sign*(a[j]+(a[i]-1)/d)
    eps = jvalue/(2*big_h)
    correction = inverse([-eps]*m,a)
    b = [[e[i][j]-neutral[i][j]+correction[i][j]
          for j in range(m)] for i in range(m)]
    return b,jvalue,eps


def actual_checks(w,a):
    m,d = len(a),len(a)-1
    assert all(sum(w[i][j] for i in range(m)) == 1 for j in range(m))
    assert all(sum(abs(w[i][j]-F(i==j)) for i in range(m)) < 2 for j in range(m))
    for j in range(m):
        for k in range(m):
            assert sum(max(F(0),(w[i][j]-F(i==k))/2) for i in range(m)) < 1
    assert all(w[i][i]>a[i] and all(w[i][j]<a[i] for j in range(m) if i!=j)
               for i in range(m))
    vol,caps = cap_formula(w,a)
    assert vol > 1
    assert all(value < (1-threshold)**d for value,threshold in zip(caps,a))
    return vol,caps


checks = 0
for d in range(2,9):
    m = d+1
    # A nonuniform proper selected group; choose a pair with nonzero J.
    a = [F(2,m+1)]+[F(1,m+1)]*d
    candidates = [(a[j]+(a[i]-1)/d,i,j)
                  for i in range(m) for j in range(m) if i!=j]
    value,i,j = max(candidates,key=lambda p:abs(p[0]))
    sign = 1 if value>0 else -1
    b,jvalue,eps = improve(a,i,j,sign)
    assert jvalue>0 and eps>0
    assert derivative(b,a)==(jvalue/2,[-eps]*m)
    tau = F(1,10000)
    w = [[F(i==j)+tau*b[i][j] for j in range(m)] for i in range(m)]
    actual_checks(w,a)
    checks += 1

    # Exact formal cubic coefficients of the analytic canonical escape.
    time = Series(0,1)
    aa = [Series(F(1,m)) for i in range(m)]
    aa[0] -= time
    aa[1] += time
    bb,jj,ee = improve(aa,0,1)
    assert jj.c == (F(0),F(d-1,d),F(0),F(0))
    ww = [[Series(i==j)+time*time*bb[i][j] for j in range(m)] for i in range(m)]
    volume,cut = cap_formula(ww,aa)
    gamma = F(d,m)**d
    assert volume.c == (F(1),F(0),F(0),F(d-1,2*d))
    for i in range(m):
        delta = cut[i]-(1-aa[i])**d
        assert delta.c == (F(0),F(0),F(0),-gamma*F(d-1,2*d))
    checks += 1

    # Concrete rational time on that same canonical path.
    t = F(1,1000)
    a = [F(1,m)]*m
    a[0] -= t
    a[1] += t
    b,jvalue,eps = improve(a,0,1)
    w = [[F(i==j)+t*t*b[i][j] for j in range(m)] for i in range(m)]
    actual_checks(w,a)
    checks += 1
    if d==2:
        planar_w,planar_a = w,a


def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]
                   -poly[i][1]*poly[(i+1)%len(poly)][0]
                   for i in range(len(poly))))/2 if poly else F(0)


def clip(poly,u,k):
    out=[]
    def margin(p):
        return sum(x*y for x,y in zip(u,p))+k
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        a,b=margin(p),margin(q)
        if a>=0:
            out.append(p)
        if a<0<b or b<0<a:
            t=a/(a-b)
            out.append(tuple(p[j]+t*(q[j]-p[j]) for j in range(2)))
    return out


third = F(1,3)
kbody=[(-third,-third),(1-third,-third),(-third,1-third)]
reflected=[(-x,-y) for x,y in kbody]
middle=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(1)),
        (F(-1),F(0)),(F(0),F(-1)),(F(1),F(-1))]
moving=[(planar_w[1][j]-third,planar_w[2][j]-third) for j in range(3)]
normals=[(-F(1),-F(1)),(F(1),F(0)),(F(0),F(1))]
assert area(kbody)==F(1,2) and area(middle)==3
assert area(moving)>area(kbody)
for i,u in enumerate(normals):
    beta=planar_a[i]-third
    old_own=area(clip(kbody,u,-beta))
    own=area(clip(moving,u,-beta))
    cap=own+area(clip(middle,u,F(0)))+area(clip(reflected,u,beta))
    assert cap==2+own-old_own<2
checks += 1

# Binary embedding, using actual planar fibers and finite isolation coefficient 10.
regular=[(3*x,3*y) for x,y in kbody]  # Area 9/2, canonical cap area D=2.
assert area(regular)==F(9,2)
binary_caps=0
for n in range(2,6):
    zero=(0,)*(n-1)
    bases=[(z,*v) for v in product((0,1),repeat=n-1)
           for z in ((-1,0,1) if v==zero else (0,1))]
    fibers={}
    for p in bases:
        if p[1:]==zero:
            fibers[p]={-1:moving,0:middle,1:reflected}[p[0]]
        else:
            fibers[p]=regular
    assert len(bases)==2**n+1
    for i,u in enumerate(normals):
        total=F(0)
        for p,poly in fibers.items():
            z,w=p[0],p[1:]
            constant=(planar_a[i]-third)*z-10*sum(w)
            value=area(clip(poly,u,constant))
            if w!=zero:
                assert value==0
                assert all(sum(x*y for x,y in zip(u,q))+constant<0 for q in poly)
            total+=value
        assert total<2
        binary_caps+=1
    for q in bases:
        if q[1:]==zero:
            continue
        def expose(p):
            z,w=p[0],p[1:]
            return 3*sum(x if bit else -x for x,bit in zip(w,q[1:]))+(2*q[0]-1)*z
        assert all(expose(q)-expose(p)>=1 for p in bases if p!=q)
        for u in normals:
            total=F(0)
            for p,poly in fibers.items():
                constant=10*(expose(p)-expose(q))
                value=area(clip(poly,u,constant))
                if p!=q:
                    assert value==0
                    assert all(sum(x*y for x,y in zip(u,x))+constant<0 for x in poly)
                total+=value
            assert total==2
            binary_caps+=1

print("PASS:",checks,"exact all-d first-order/cubic identities and actual compatible paths;")
print(binary_caps,"actual planar isolated global cap budgets in binary embeddings.")
print("Planar canonical-path absolute volume gain:",area(moving)-F(1,2))
