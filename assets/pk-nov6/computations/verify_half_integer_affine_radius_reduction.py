"""Independent exact checks of the deficit-monotone affine replacement.

The proof is the companion markdown file, not these finite checks.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement


def tail(a,r,u):
    if u <= 0:
        return r*r
    if u >= a*r:
        return Q(0)
    if a == Q(1,2):
        return r*r-4*u*u
    if a == 1:
        return (r-u)**2
    if u <= (1-a)*r:
        return r*r-u*u/(a*(1-a))
    return (a*r-u)**2/(a*(2*a-1))


gamma=Q(4,9)
t=Q(1,3)
checks=0
normals=[Q(1,2),Q(3,5),Q(2,3),Q(3,4),Q(1)]
tilts=[Q(0),Q(1,78),Q(1,12),Q(1,5),Q(1,3),Q(1)]
for m in range(1,8):
    for drops in combinations_with_replacement([Q(j,12) for j in range(5)],m):
        if sum(drops)>1:
            continue
        radii=[Q(1)]
        for drop in drops:
            radii.append(radii[-1]-drop)
        for a in normals:
            da=(a+4)/9
            for beta in tilts:
                rho=[min(max(t-beta*h,0)/da,(2*t+beta)/(a+da))
                     for h in range(m+1)]
                p=[None]+[(1-radii[h])/h for h in range(1,m+1)]
                q=[None]+[(1-rho[h])/h for h in range(1,m+1)]
                assert all(p[h]<=p[h+1] for h in range(1,m))
                assert all(q[h]>q[h+1] for h in range(1,m))
                k=0
                for h in range(1,m+1):
                    if p[h]<=q[h]:
                        assert k==h-1
                        k=h
                if k==m:
                    slope=p[m]
                elif k==0:
                    slope=q[1]
                else:
                    lower=max(p[k],q[k+1])
                    upper=min(q[k],p[k+1])
                    assert lower<=upper
                    slope=(lower+upper)/2
                assert 0<=slope<=Q(1,m)
                for h in range(m+1):
                    old=radii[h]
                    new=1-slope*h
                    center=rho[h]
                    assert min(old,center)<=new<=max(old,center) or h==0
                    def objective(r):
                        return tail(a,r,t-beta*h)+tail(a,r,t+beta*(h+1))-gamma*r*r
                    assert objective(new)<=objective(old)
                    # Direct minimizer check, including every knot range.
                    for r in [Q(0),old,new,Q(1),center/Q(2),center+Q(1,7)]:
                        assert objective(center)<=objective(r)
                    checks+=1
print(f"PASS: {checks} exact pair-minimizer and deficit-monotone replacement checks")
