"""Exact ordinary calibration and paired-roof loss checks.

The audited clipping utilities are reused; its original buffered
certificate is checked first by the import. This script then reconstructs
the different zero-buffer arrangement directly from its actual heights.
"""
from fractions import Fraction as F
from itertools import combinations
import verify_globally_deepest_rectangle_inside_facets_two_sided as old

checks = 0
def ck(condition):
    global checks
    assert condition
    checks += 1

z = [-2, -1, 0, 1, 2]
r = [F(1), F(51, 50), F(51, 50), F(203, 200), F(101, 100)]
h = [F(0), F(3), F(2), F(1), F(0)]
a = F(3, 800)
H = [1+a*v for v in h]
Q = F(812869, 160000)
M = F(814069, 80000)
ck(2*sum(x*y for x, y in zip(r, H)) == M)
ck(2*r[0]*H[0]+sum(r[i]*(H[i]-F(z[i], 2)) for i in [1, 2, 3]) == Q)
ck(M-2*Q == F(3, 200))
count = 0
cells_per_sign = []
for sign in [-1, 1]:
    terms = []
    for base, width, height in zip(z, r, H):
        terms += [(1, (width/2, height, sign*base)),
                  (-1, (-width/2, height, sign*base)),
                  (-1, (width/2, -height, sign*base)),
                  (1, (-width/2, -height, sign*base))]
    poly = [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))]
    matrix = [[F(0) for _ in range(3)] for _ in range(3)]
    matrix[0][1] = matrix[1][0] = -Q
    cells = [(poly, matrix)]
    for factor, normal in terms:
        new = []
        for poly, matrix in cells:
            for direction in [1, -1]:
                clipped = old.clip(poly, tuple(direction*v for v in normal))
                if len(clipped) < 3 or not old.twice_area(clipped):
                    continue
                changed = matrix
                if direction == 1:
                    changed = [[matrix[i][j]+factor*normal[i]*normal[j]
                                for j in range(3)] for i in range(3)]
                new.append((clipped, changed))
        cells = new
    cells_per_sign.append(len(cells))
    ck(sum(old.twice_area(poly) for poly, _ in cells) == 1)
    for poly, matrix in cells:
        for j in range(1, len(poly)-1):
            tri = [poly[0], poly[j], poly[j+1]]
            if not old.twice_area(tri):
                continue
            count += 1
            coefficients = [[old.bilinear(matrix, v, w) for w in tri] for v in tri]
            for ii in range(3):
                for jj in range(ii, 3):
                    ck(coefficients[ii][jj] >= 0)
            for n in [1, 2, 3]:
                for subset in combinations(range(3), n):
                    if all(coefficients[ii][jj] == 0 for ii in subset for jj in subset):
                        ck(all(tri[ii][0] == 0 for ii in subset)
                           or all(tri[ii][1] == 0 for ii in subset))
ck(cells_per_sign == [43, 43])
ck(count == 138)

def mass(tilt, heights=H, horizontal=False):
    if horizontal:
        return sum(2*height*old.clipped(width/2+tilt*base, width)
                   for base, width, height in zip(z, r, heights))
    return sum(width*old.clipped(height+tilt*base, 2*height)
               for base, width, height in zip(z, r, heights))

for horizontal in [False, True]:
    knots = {F(0)}
    for base, width, height in zip(z, r, H):
        if base:
            value = width/2 if horizontal else height
            knots.update([value/base, -value/base])
    knots = sorted(knots)
    vals = [mass(v, horizontal=horizontal) for v in knots]
    if horizontal:
        ck(min(vals) > Q)
    else:
        ck(min(vals) == Q)
        ck([v for v, fv in zip(knots, vals) if fv == Q] == [-F(1, 2)])
    ck(vals[0] > Q and vals[-1] > Q)
    ck(mass(knots[0]-1, horizontal=horizontal) == vals[0])
    ck(mass(knots[-1]+1, horizontal=horizontal) == vals[-1])

A = sum(width*speed for width, speed in zip(r, h))
ck(A == F(1223, 200))
for den in range(1000, 10001, 137):
    t = F(1, den)
    newH = [height-t*speed for height, speed in zip(H, h)]
    ck(all(newH[i+1]-newH[i] >= newH[i+2]-newH[i+1] for i in range(3)))
    newM = 2*sum(width*height for width, height in zip(r, newH))
    newQ = mass(-F(1, 2), newH)
    ck(newM == M-2*A*t)
    ck(newQ == Q-A*t)
    ck(newQ/newM < Q/M)
    ck(newQ/newM-Q/M == A*t*(2*Q-M)/(M*(M-2*A*t)))
    volume = [2*width*height for width, height in zip(r, newH)]
    ck(all(v < newQ for v in [volume[0], sum(volume[:2]), sum(volume[3:]), volume[4]]))
    for i in [1, 2, 3]:
        ck(abs(F(z[i], 2)) < newH[i])
    # Both actual cap masses lose exactly half the total removed mass.
    ck(Q-newQ == (M-newM)/2)

print(f'PASS: {checks} paired-roof checks; 86 cells, 138 triangles')
