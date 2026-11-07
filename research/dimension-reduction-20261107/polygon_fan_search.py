"""Exploratory search over cyclic planar middle bodies (no proof claims)."""
import json,math,itertools
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import differential_evolution
from triangle_fan_search import clip,area

normals=np.array([[math.cos(a),math.sin(a)] for a in [0,2*math.pi/3,4*math.pi/3]])


def evaluate(x,detail=False):
    rad=np.r_[1.,np.exp(x[1:])]
    m=len(rad)
    angles=np.arange(3*m)*2*math.pi/(3*m)+x[0]
    points=np.column_stack([np.cos(angles),np.sin(angles)])*np.tile(rad,3)[:,None]
    hull=ConvexHull(points);B=points[hull.vertices]
    vol=area(B); beta=area(clip(B,-normals[0],0))/vol
    cone=clip(clip(B,normals[1],0),normals[2],0)
    best=0.; verts=None
    for a,b in itertools.combinations(cone,2):
        z=abs(a[0]*b[1]-a[1]*b[0])/2/vol
        if z>best: best=z;verts=[a.tolist(),b.tolist()]
    theta=best; gamma=1/math.e
    mass=(3*beta-1)/(3*gamma-1)
    if theta<=0 or mass<=1:return 1e9
    n=3*math.log1p((mass-1)/(3*theta))/math.log1p(theta/mass)
    if detail:return dict(ideal_n=n,theta=theta,beta=beta,m=mass,polygon=B.tolist(),source_vertices=verts,parameters=x.tolist())
    return n


if __name__=='__main__':
    res=differential_evolution(evaluate,[(0,2*math.pi/3)]+[(-1.8,1.8)]*5,popsize=14,maxiter=220,seed=119,tol=1e-8,polish=True)
    out=evaluate(res.x,True)
    print(json.dumps(out,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
