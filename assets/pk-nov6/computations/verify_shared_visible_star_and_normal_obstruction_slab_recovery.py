"""Exact actual-polygon checks for the shared visible-star measure.

These check sampled integer fibers and oblique/closed cap derivatives,
including the vertical-seam double-counting example. They are not a proof
of the arbitrary-dimensional geometric lemma.
"""
from fractions import Fraction as F

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    points = sorted(set(points))
    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def fiber(poly, z):
    values=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        if a[0] == b[0]:
            if z == a[0]: values.extend([a[1],b[1]])
        elif min(a[0],b[0]) <= z <= max(a[0],b[0]):
            t=(z-a[0])/(b[0]-a[0])
            values.append(a[1]+t*(b[1]-a[1]))
    return (min(values),max(values)) if values else None

def cap_mass(poly, bases, cap):
    az, ux, b = cap
    total=F(0)
    for z in bases:
        section=fiber(poly,z)
        if section is None: continue
        lo,hi=section
        if ux > 0: lo=max(lo,(b-az*z)/ux)
        elif ux < 0: hi=min(hi,(b-az*z)/ux)
        elif az*z < b: continue
        total+=max(F(0),hi-lo)
    return total

def star_atoms(poly, bases, w0, v, deduplicate=True):
    atoms=[]
    for z in bases:
        seen=set()
        for a,b in zip(poly,poly[1:]+poly[:1]):
            dz,dx=b[0]-a[0],b[1]-a[1]
            if dz == 0: continue  # vertical ambient facet
            u=-dz/abs(dz)
            normal_z=dx/abs(dz)
            level=normal_z*a[0]+u*a[1]
            if normal_z*w0[0]+u*w0[1] != level or u*v <= 0:
                continue
            if not min(a[0],b[0]) <= z <= max(a[0],b[0]):
                continue
            r=(z-a[0])/dz
            r0=(w0[0]-a[0])/dz
            bounds=[F(1)]
            if r0 > 0: bounds.append(r/r0)
            if r0 < 1: bounds.append((1-r)/(1-r0))
            roof=min(bounds)
            x=(level-normal_z*z)/u
            key=(u,level-normal_z*z)
            if deduplicate and key in seen: continue
            seen.add(key)
            atoms.append((z,x,u*v*roof))
    return atoms

cases=[
    ([(-1,-1),(1,-1),(1,0),(0,1),(-1,0)],(0,1),1),
    ([(-2,-1),(2,-1),(2,1),(-2,1)],(0,1),1),
    ([(-2,-1),(2,-1),(2,1),(-2,1)],(2,1),1),
    ([(-2,-2),(2,-2),(2,2),(-2,1)],(0,-2),-1),
]
for points,w0,v in cases:
    poly=hull([tuple(map(F,p)) for p in points])
    w0=tuple(map(F,w0)); v=F(v)
    bases=list(map(F,range(int(min(p[0] for p in poly)),
                           int(max(p[0] for p in poly))+1)))
    atoms=star_atoms(poly,bases,w0,v)
    caps=[(F(a),F(u),F(b)) for a in (-2,-1,0,1,2)
          for u in (-2,-1,0,1,2) if a or u
          for b in (-3,-1,0,1,3)]
    # Include every supporting cut in both orientations and tangent cuts.
    for z,x,mass in atoms:
        for a in (-1,0,1):
            for u in (-1,1):
                caps.append((F(a),F(u),a*z+u*x))
    for epsilon in (F(1,1000),F(1,10000)):
        grown=hull(poly+[(w0[0],w0[1]+epsilon*v)])
        before=sum(fiber(poly,z)[1]-fiber(poly,z)[0] for z in bases)
        after=sum(fiber(grown,z)[1]-fiber(grown,z)[0] for z in bases)
        check(after-before == epsilon*sum(t[2] for t in atoms))
        for cap in caps:
            az,ux,b=cap
            expected=sum(mass for z,x,mass in atoms
                         if az*z+ux*x > b or
                         (az*z+ux*x == b and ux*v >= 0))
            check(cap_mass(grown,bases,cap)-cap_mass(poly,bases,cap)
                  == epsilon*expected)

poly=hull([tuple(map(F,p)) for p in cases[0][0]])
bases=list(map(F,[-1,0,1])); w0=(F(0),F(1))
check(sum(a[2] for a in star_atoms(poly,bases,w0,F(1))) == 1)
check(sum(a[2] for a in star_atoms(poly,bases,w0,F(1),False)) == 2)

# Exact constants of the positive-volume, strict-no-heavy obstruction.
gamma=F(4,9); L=F(8); delta=F(1,800)
M=9*(F(1,2)+3*F(1,100))
check(L*delta == F(1,100))
check(M == F(477,100))
check(F(1,2) < M/8)
check(9*F(1,2)*gamma == 2)
check(F(9,200) < 2)
check(gamma/(1+L+delta) < gamma/(1+L))
check(gamma/(1+L) == F(4,81))
check(F(4,81) < gamma/8)
check((F(9,2)/M) == F(50,53))
check(F(50,53) > F(2,8))
print(f"PASS: {checks} exact checks")
