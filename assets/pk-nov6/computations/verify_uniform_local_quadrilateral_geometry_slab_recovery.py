"""Exact enclosing-triangle identity, including concentrating endpoint ears."""
exec(open('./verify_fixed_endpoint_sector_polygon_replacement_slab_recovery.py').read().split('def verify(')[0])
rng=Random(715832)
normals=[(1,0),(0,1),(-1,-1)]
def sections(K):
    pp=[ray_endpoint(K,e)[0]for e in rays]
    return [pp[1][1]-pp[4][1],pp[0][0]-pp[3][0],pp[5][0]-pp[2][0]]
for it in range(120):
    X,SS,V=[F(rng.randint(1,10),rng.randint(1,8))for _ in range(3)]
    W=F(rng.randint(0,10),rng.randint(1,8))
    pts=[(2*V+W,-V-W),(-X,X+SS),(-X,-SS-W)]
    # Small generic vertex perturbations preserve strict incidence.
    scale=min(X,SS,V)/(10000*(1+X+SS+V+W))
    pts=[add(P,(scale*rng.randint(-1,1),scale*rng.randint(-1,1)))for P in pts]
    T=hull(pts);kk=area(T)
    for idx,P in enumerate(pts):check(all((dot(n,P)>0)==(j==idx)for j,n in enumerate(normals)))
    eta=min(X,SS,V)/(1000*(1+X+SS+V+W))
    theta=eta**(it%3+1)  # Includes eta~theta and either relative order of small scales.
    if it%4==0:theta=2*eta
    for first in range(3):
        for nxt in range(3):
            if first==nxt:continue
            last=3-first-nxt;A,B,C=pts[first],pts[nxt],pts[last]
            Q0=add(mul(1-theta,A),mul(theta,B))
            Q=sub(mul(1+eta,Q0),mul(eta,C))
            aa=eta/(1-(1+eta)*theta);bb=(1+eta)*theta
            R=sub(mul(1+aa,A),mul(aa,C))
            K=hull(pts+[Q]);outer=hull([R,B,C]);corner=hull([R,A,Q])
            check(len(K)==4);check(Q==add(mul(1-bb,R),mul(bb,B)))
            check(area(K)==kk*(1+eta));check(area(outer)==kk*(1+aa))
            loss=kk*eta*(1+eta)*theta/(1-(1+eta)*theta)
            check(area(corner)==loss);check(area(outer)-area(K)==loss)
            for P in (R,A,Q):check(all((dot(n,P)>0)==(j==first)for j,n in enumerate(normals)))
            edge=sub(Q,A);nn=(-edge[1],edge[0]);cut=dot(nn,A)
            if dot(nn,B)<cut:nn=mul(-1,nn);cut=-cut
            check(hull(clip(outer,nn,cut))==K)
            check(sections(outer)==sections(K))
            for j,n in enumerate(normals):check(area(clip(outer,n))-area(clip(K,n))==(loss if j==first else 0))
            # General two-status cap and section formulas, without using corner containment.
            sT=sections(T);sK=sections(K)
            for ind in (first,nxt):
                pos=pts[ind];neg=pts[nxt if ind==first else first]
                p=dot(normals[ind],pos);q=-dot(normals[ind],neg);z=dot(normals[ind],Q)
                frac=1-q*q/((p+q)*(q+z)) if z>=0 else p*p/((p+q)*(p-z))
                co=2*q/((p+q)*(q+z)) if z>=0 else 2*p/((p+q)*(p-z))
                check(area(clip(K,normals[ind]))-area(clip(T,normals[ind]))==eta*kk*frac)
                check(sK[ind]-sT[ind]==eta*kk*co)
print(f'PASS: {checks:,} exact enclosing-triangle, clipping, and section checks')
