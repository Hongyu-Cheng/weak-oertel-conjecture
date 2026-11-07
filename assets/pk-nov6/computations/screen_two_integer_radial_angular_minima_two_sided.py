"""Exploratory actual concave 2D-base arrays; complete tilt-cell minimization."""
import random
import json
import numpy as np


def cut_polygon(poly, normal, threshold, positive):
    result = []
    for a, b in zip(poly, poly[1:]+poly[:1]):
        da = float(np.dot(normal, a)-threshold)
        db = float(np.dot(normal, b)-threshold)
        if not positive:
            da, db = -da, -db
        if da >= -1e-9:
            result.append(a)
        if (da < -1e-9 and db > 1e-9) or (db < -1e-9 and da > 1e-9):
            result.append(a+da/(da-db)*(b-a))
    return result


def tilt_min(P, radii, source, theta):
    ds = P-source
    limit = 10*max(radii)+1
    cells = [[np.array([-limit,-limit]), np.array([limit,-limit]),
              np.array([limit,limit]), np.array([-limit,limit])]]
    lines = []
    seen = set()
    for z, r in zip(ds, radii):
        if np.dot(z, z) == 0:
            continue
        for threshold in [-(2-theta)*r, (1-2*theta)*r, (1+theta)*r]:
            vector = np.r_[z, threshold]
            if vector[np.flatnonzero(z)[0]] < 0:
                vector = -vector
            key = tuple(np.round(vector, 11))
            if key not in seen:
                lines.append((vector[:2], vector[2]))
                seen.add(key)
    for normal, threshold in lines:
        new = []
        for poly in cells:
            values = np.array([np.dot(normal, a)-threshold for a in poly])
            if min(values) >= -1e-9 or max(values) <= 1e-9:
                new.append(poly)
            else:
                for side in [True, False]:
                    piece = cut_polygon(poly, normal, threshold, side)
                    if len(piece) >= 3:
                        new.append(piece)
        cells = new
    best = (float('inf'), None)
    for poly in cells:
        center = sum(poly)/len(poly)
        margin = ds@center
        full = margin >= (1+theta)*radii
        empty = margin <= -(2-theta)*radii
        proper = ~(full | empty)
        high = proper & (margin <= (1-2*theta)*radii)
        low = proper & ~high
        A, B = np.zeros((2,2)), np.zeros(2)
        C = np.sum(4.5*radii[full]**2)
        if np.any(high):
            den=2*(1-theta)
            if den < 1e-10:
                continue
            A += ds[high].T@ds[high]/den
            B += 2*(2-theta)*ds[high].T@radii[high]/den
            C += np.sum(((2-theta)*radii[high])**2)/den
        if np.any(low):
            den=2*theta
            if den < 1e-10:
                continue
            A -= ds[low].T@ds[low]/den
            B += 2*(1+theta)*ds[low].T@radii[low]/den
            C += np.sum(4.5*radii[low]**2-((1+theta)*radii[low])**2/den)
        candidates = list(poly)
        for left, right in zip(poly, poly[1:]+poly[:1]):
            direction=right-left
            qa=direction@A@direction
            if qa>1e-10:
                parameter=-(2*left@A@direction+B@direction)/(2*qa)
                if 0<parameter<1:
                    candidates.append(left+parameter*direction)
        if np.min(np.linalg.eigvalsh(A))>1e-9:
            point=np.linalg.solve(2*A,-B)
            # Check every oriented edge of this convex polygon.
            crosses=[np.cross(q-p,point-p) for p,q in zip(poly,poly[1:]+poly[:1])]
            if min(crosses)>=-1e-8 or max(crosses)<=1e-8:
                candidates.append(point)
        for point in candidates:
            value=float(point@A@point+B@point+C)
            if value<best[0]:
                best=(value,point)
    return best


if __name__=='__main__':
    P=np.array([(i,j) for i in [-1,0,1] for j in [-1,0,1]],dtype=float)
    source=np.zeros(2)
    random.seed(4331)
    for trial in range(250):
        planes=[(random.randrange(-15,16),random.randrange(-15,16),
                 random.randrange(0,21)) for _ in range(random.randrange(2,8))]
        raw=np.array([min(a*x+b*y+c for a,b,c in planes) for x,y in P])
        offset=-min(raw)+random.randrange(1,21)
        radii=(raw+offset)/max(raw+offset)
        ca=min((tilt_min(P,radii,source,t)[0],t) for t in [0.,1.])
        best=(ca[0],ca[1],None)
        for theta in [.1,.2,.3,.4,.5,.6,.7,.8,.9]:
            value,alpha=tilt_min(P,radii,source,theta)
            if value<best[0]:
                best=(value,theta,alpha)
        if best[0]<ca[0]-1e-7:
            print(json.dumps({'trial':trial,'planes':planes,'offset':offset,
                              'radii_int':list(raw+offset),'canonical':ca,
                              'candidate':[best[0],best[1],best[2].tolist()]}),flush=True)
            break
        if trial%10==0:
            print('progress',trial,flush=True)
