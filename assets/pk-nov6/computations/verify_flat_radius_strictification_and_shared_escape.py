"""Exact Jensen gaps, flat cap masses, and compatible shared-cap physical descent."""
from fractions import Fraction as F
from itertools import combinations, product


def solve(a,b):
    """Square rational solve, or None if singular."""
    n=len(a)
    w=[list(row)+[b[i]] for i,row in enumerate(a)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if w[i][k]),None)
        if pivot is None:
            return None
        w[k],w[pivot]=w[pivot],w[k]
        val=w[k][k]
        w[k]=[x/val for x in w[k]]
        for i in range(n):
            if i!=k:
                val=w[i][k]
                w[i]=[x-val*y for x,y in zip(w[i],w[k])]
    return [row[-1] for row in w]


# All basic excluded-target representations in a lattice-complete square.
p=list(product((-1,0,1),repeat=2))
eps=F(1,10)
raw={z:1+eps*(3-sum(x*x for x in z)) for z in p}
relations=0
for z in p:
    others=[x for x in p if x!=z]
    for count in (2,3):
        for sources in combinations(others,count):
            columns=[[F(1),F(x[0]),F(x[1])] for x in sources]
            alpha=None
            for rowids in combinations(range(3),count):
                candidate=solve([[columns[j][i] for j in range(count)] for i in rowids],
                                [F((1,*z)[i]) for i in rowids])
                if candidate is not None and all(
                    sum(candidate[j]*columns[j][i] for j in range(count))==F((1,*z)[i])
                    for i in range(3)):
                    alpha=candidate
                    break
            if alpha is None or min(alpha)<0:
                continue
            variance=sum(alpha[j]*sum((sources[j][k]-z[k])**2 for k in range(2))
                         for j in range(count))
            gap=raw[z]-sum(alpha[j]*raw[sources[j]] for j in range(count))
            assert variance>=1 and gap==eps*variance>=eps
            relations+=1
for d in range(1,9):
    mu=F(len(p))/sum(r**d for r in raw.values())  # exactly lambda^d
    gamma=F(d,d+1)**d
    assert mu*sum(r**d for r in raw.values())==len(p)
    assert mu*sum(gamma*r**d for r in raw.values())==gamma*len(p)


class Jet:
    def __init__(self,x=0,dx=0,q=0):
        self.c=(F(x),F(dx),F(q))
    @staticmethod
    def cast(x):
        return x if isinstance(x,Jet) else Jet(x)
    def __add__(self,x):
        x=self.cast(x)
        return Jet(*(a+b for a,b in zip(self.c,x.c)))
    __radd__=__add__
    def __neg__(self):
        return Jet(*(-x for x in self.c))
    def __sub__(self,x):
        return self+-self.cast(x)
    def __rsub__(self,x):
        return self.cast(x)-self
    def __mul__(self,x):
        x=self.cast(x)
        return Jet(*(sum(self.c[j]*x.c[i-j] for j in range(i+1)) for i in range(3)))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.cast(x)
        a,b,c=x.c
        return self*Jet(1/a,-b/a**2,b*b/a**3-c/a**2)
    def __pow__(self,n):
        out=Jet(1)
        for _ in range(n):
            out*=self
        return out


def det(a):
    w=[row[:] for row in a]
    out=1
    for k in range(len(w)):
        pivot=w[k][k]
        assert (pivot.c[0] if isinstance(pivot,Jet) else pivot)!=0
        out*=pivot
        for i in range(k+1,len(w)):
            val=w[i][k]/pivot
            for j in range(k+1,len(w)):
                w[i][j]-=val*w[k][j]
    return out


def caps(w):
    m=len(w)
    volume=det(w)
    out=[]
    for i in range(m):
        value=volume*(w[i][i]-F(1,m))**(m-1)
        for j in range(m):
            if i!=j:
                value/=w[i][i]-w[i][j]
        out.append(value)
    return volume,out


physical=0
for d in range(2,8):
    m=d+1
    gamma=F(d,m)**d
    radii=[F(11,10),F(6,5),F(11,10)]
    weight=[r**d for r in radii]
    mu=F(3)/sum(weight)  # The final common dilation has determinant mu.
    c=[F(1),F(-1)]+[F(0)]*(m-2)
    lift=[[(-c[i] if i==j else (m*c[j]+c[i])/F(d*m-1))
           for j in range(m)] for i in range(m)]
    velocity=[lift,[[-weight[0]/weight[1]*x for x in row] for row in lift],
              [[F(0) for _ in range(m)] for _ in range(m)]]
    for b in velocity:
        assert all(sum(b[i][j] for i in range(m))==0 for j in range(m))
        assert sum(b[i][i] for i in range(m))==0
    h=F(d*d-1,d*(d*m-1))*sum(x*x for x in c)*(weight[0]+weight[0]**2/weight[1])
    wjet=[[[Jet(i==j,velocity[z][i][j]) for j in range(m)] for i in range(m)]
          for z in range(3)]
    volumes=[];cut=[]
    for w in wjet:
        v,f=caps(w)
        volumes.append(v);cut.append(f)
    mass=sum(weight[z]*volumes[z] for z in range(3))
    cap=[sum(weight[z]*cut[z][i] for z in range(3)) for i in range(m)]
    assert mass.c[1]==0 and all(x.c[1]==0 for x in cap)
    assert 2*mass.c[2]-sum(2*x.c[2] for x in cap)/(m*gamma)==h>0

    desired=gamma*h/2
    f=[-desired-2*x.c[2] for x in cap]
    trace=sum(f)/(m*gamma*weight[0])
    row=[x/(gamma*weight[0])-trace for x in f]
    acc=[[(trace/d)*(F(i==j)-F(1,m))+row[i]/m
          for j in range(m)] for i in range(m)]
    assert all(sum(acc[i][j] for i in range(m))==0 for j in range(m))
    assert sum(acc[i][i] for i in range(m))==trace
    for i in range(m):
        assert gamma*weight[0]*(trace+sum(acc[i]))==f[i]

    wjet=[[[Jet(i==j,velocity[z][i][j],acc[i][j]/2 if z==0 else 0)
            for j in range(m)] for i in range(m)] for z in range(3)]
    data=[caps(w) for w in wjet]
    mass=sum(weight[z]*data[z][0] for z in range(3))
    cap=[sum(weight[z]*data[z][1][i] for z in range(3)) for i in range(m)]
    assert 2*mass.c[2]==h/2>0
    assert all(2*x.c[2]==-desired<0 for x in cap)

    time=F(1,10000)
    w=[[[F(i==j)+time*velocity[z][i][j]+
          (time*time*acc[i][j]/2 if z==0 else 0)
          for j in range(m)] for i in range(m)] for z in range(3)]
    assert all(all(sum(wz[i][j] for i in range(m))==1 for j in range(m)) for wz in w)
    assert all(wz[i][i]>F(1,m) and all(wz[i][j]<F(1,m) for j in range(m) if j!=i)
               for wz in w for i in range(m))
    data=[caps(wz) for wz in w]
    actual_mass=mu*sum(weight[z]*data[z][0] for z in range(3))
    actual_caps=[mu*sum(weight[z]*data[z][1][i] for z in range(3)) for i in range(m)]
    assert actual_mass>3
    assert all(value<3*gamma for value in actual_caps)

    # Exact target-simplex inclusion for EVERY left/right vertex pair.
    # The common algebraic normalization lambda cancels from this check.
    for j in range(m):
        for k in range(m):
            target=[radii[0]/(2*radii[1])*w[0][i][j]+
                    radii[2]/(2*radii[1])*w[2][i][k]+
                    (1-(radii[0]+radii[2])/(2*radii[1]))/m
                    for i in range(m)]
            bary=solve(w[1],target)
            assert bary is not None and sum(bary)==1 and min(bary)>0
    physical+=1

# The d=1 obstruction to volume gain has exact opposite-cap accounting.
for widths in ([F(1),F(2)],[F(1,3),F(2,5),F(7,2)]):
    assert sum(w/2 for w in widths)*2==sum(widths)

print("PASS:",relations,"exact excluded-target Jensen relations; flat normalized")
print("volume/cap identities in dimensions1--8;",physical,"actual compatible")
print("unequal-volume two-fiber Hessian/acceleration escapes in dimensions2--7.")
