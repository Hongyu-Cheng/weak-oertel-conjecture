"""Exact all-normal certificate; standard-library rational arithmetic only.

Run with --regenerate to write the independently inspectable triangle
certificate. A normal run reconstructs the partition and checks the
saved certificate exactly. The companion source proves why these finite
identities include every ambient halfspace.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import sys

checks = 0
def ck(condition):
    global checks
    assert condition
    checks += 1

z = [-2, -1, 0, 1, 2]
r = [F(1), F(51, 50), F(51, 50), F(203, 200), F(101, 100)]
H = [F(4001, 4000), F(8091, 8000), F(403, 400),
     F(8029, 8000), F(3999, 4000)]
delta = F(1, 4000)
Q = F(8130713, 1600000)
M = F(8140687, 800000)
ck(M == 2*sum(a*b for a, b in zip(r, H)))
ck(Q == 2*r[0]*H[0]+sum(r[i]*(H[i]-F(z[i], 2)+delta)
                       for i in [1, 2, 3]))
ck(all(r[i+1]-r[i] >= r[i+2]-r[i+1] for i in range(3)))
ck(all(H[i+1]-H[i] >= H[i+2]-H[i+1] for i in range(3)))
for lo in range(5):
    for hi in range(lo, 5):
        if lo == 0 and hi == 4:
            continue
        k = len({v % 2 for v in z[lo:hi+1]})
        ck(2*sum(r[i]*H[i] for i in range(lo, hi+1)) < k*M/2)

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def clip(poly, normal):
    out = []
    for a, b in zip(poly, poly[1:]+poly[:1]):
        va, vb = dot(normal, a), dot(normal, b)
        if va >= 0:
            out.append(a)
        if va < 0 < vb or vb < 0 < va:
            out.append(tuple((vb*x-va*y)/(vb-va) for x, y in zip(a, b)))
    ans = []
    for p in out:
        if not ans or p != ans[-1]:
            ans.append(p)
    if len(ans) > 1 and ans[0] == ans[-1]:
        ans.pop()
    return ans

def twice_area(poly):
    return abs(sum(a[0]*b[1]-a[1]*b[0]
                   for a, b in zip(poly, poly[1:]+poly[:1])))

def bilinear(matrix, a, b):
    return sum(a[i]*matrix[i][j]*b[j]
               for i in range(3) for j in range(3))

triangles = []
cell_counts = []
for base_sign in [-1, 1]:
    terms = []
    for base, width, height in zip(z, r, H):
        terms.extend([
            (1, (width/2, height+delta, base_sign*base)),
            (-1, (-width/2, height+delta, base_sign*base)),
            (-1, (width/2, -height+delta, base_sign*base)),
            (1, (-width/2, -height+delta, base_sign*base))])
    simplex = [(F(1), F(0), F(0)), (F(0), F(1), F(0)),
               (F(0), F(0), F(1))]
    matrix = [[F(0) for _ in range(3)] for _ in range(3)]
    matrix[0][1] = matrix[1][0] = -Q
    cells = [(simplex, matrix)]
    for factor, normal in terms:
        next_cells = []
        for poly, matrix in cells:
            positive = clip(poly, normal)
            negative = clip(poly, tuple(-x for x in normal))
            if len(positive) >= 3 and twice_area(positive):
                changed = [[matrix[i][j]+factor*normal[i]*normal[j]
                            for j in range(3)] for i in range(3)]
                next_cells.append((positive, changed))
            if len(negative) >= 3 and twice_area(negative):
                next_cells.append((negative, matrix))
        cells = next_cells
    cell_counts.append(len(cells))
    ck(sum(twice_area(poly) for poly, _ in cells) == 1)
    total_triangle_area = F(0)
    for cell_index, (poly, matrix) in enumerate(cells):
        for j in range(1, len(poly)-1):
            tri = [poly[0], poly[j], poly[j+1]]
            if not twice_area(tri):
                continue
            total_triangle_area += twice_area(tri)
            center = tuple(sum(v[k] for v in tri)/3 for k in range(3))
            direct = [[F(0) for _ in range(3)] for _ in range(3)]
            direct[0][1] = direct[1][0] = -Q
            for factor, normal in terms:
                if dot(normal, center) > 0:
                    for ii in range(3):
                        for jj in range(3):
                            direct[ii][jj] += factor*normal[ii]*normal[jj]
            # A term identically zero on a nondegenerate triangle has
            # zero coefficient vector; the matrix is therefore exact.
            ck(direct == matrix)
            coef = [[bilinear(matrix, a, b) for b in tri] for a in tri]
            for ii in range(3):
                for jj in range(ii, 3):
                    ck(coef[ii][jj] >= 0)
            # Every zero Bernstein face is confined to t=0 or u=0.
            # This proves strict positivity whenever t,u are positive.
            for count in [1, 2, 3]:
                for subset in combinations(range(3), count):
                    if all(coef[ii][jj] == 0 for ii in subset for jj in subset):
                        ck(all(tri[ii][0] == 0 for ii in subset)
                           or all(tri[ii][1] == 0 for ii in subset))
            triangles.append({
                'base_sign': base_sign, 'cell': cell_index,
                'vertices': [[str(x) for x in v] for v in tri],
                'matrix': [[str(x) for x in row] for row in matrix],
                'bernstein': [str(coef[ii][jj]) for ii in range(3)
                              for jj in range(ii, 3)]})
    ck(total_triangle_area == 1)
ck(cell_counts == [54, 56])
ck(len(triangles) == 193)

def clipped(value, upper):
    return max(F(0), min(upper, value))

def axis_mass(a, horizontal):
    if horizontal:
        return sum(2*hh*clipped(rr/2+a*base, rr)
                   for base, rr, hh in zip(z, r, H))
    return sum(rr*clipped(hh+a*base+delta, 2*hh)
               for base, rr, hh in zip(z, r, H))

axis_tables = []
for horizontal in [False, True]:
    knots = {F(0)}
    for base, width, height in zip(z, r, H):
        if base:
            knots.update([(-width/2)/base, (width/2)/base] if horizontal
                         else [(-height-delta)/base, (height-delta)/base])
    knots = sorted(knots)
    values = [axis_mass(a, horizontal) for a in knots]
    expected = Q+F(13, 20000) if horizontal else Q
    ck(min(values) == expected)
    if not horizontal:
        ck([a for a, value in zip(knots, values) if value == Q] == [-F(1, 2)])
        ck(values[0] > Q and values[-1] > Q)
    else:
        ck(all(value > Q for value in values))
    for a, b, fa, fb in zip(knots, knots[1:], values, values[1:]):
        for numerator in [1, 2, 3]:
            lam = F(numerator, 4)
            ck(axis_mass((1-lam)*a+lam*b, horizontal) == (1-lam)*fa+lam*fb)
    # The two unbounded intervals are constant: all nonzero-base
    # intervals are saturated, while the own interval is independent of a.
    ck(axis_mass(knots[0]-1, horizontal) == values[0])
    ck(axis_mass(knots[-1]+1, horizontal) == values[-1])
    axis_tables.append({'horizontal': horizontal,
                        'knots': [str(a) for a in knots],
                        'masses': [str(v) for v in values]})

# All other bases are excluded by actual closed pure-base caps.
other_bounds = [2*r[0]*H[0], 2*sum(r[i]*H[i] for i in [0, 1]),
                2*sum(r[i]*H[i] for i in [3, 4]), 2*r[4]*H[4]]
ck(all(v < Q for v in other_bounds))
ck(2*sum(r[i]*H[i] for i in [0, 1, 2]) > Q)
ck(2*sum(r[i]*H[i] for i in [2, 3, 4]) > Q)
ck(H[0] == 1+delta and H[4] == 1-delta)
ck(delta < H[2])
for h in [F(1, 100000), F(1, 1000000)]:
    ck((axis_mass(-F(1, 2)+h, False)-Q)/h == F(3, 200))
    ck((axis_mass(-F(1, 2)-h, False)-Q)/h == F(1, 200))

payload = {'widths': list(map(str, r)), 'halfheights': list(map(str, H)),
           'delta': str(delta), 'Q': str(Q), 'M': str(M),
           'cell_counts': cell_counts, 'triangles': triangles,
           'axis_tables': axis_tables}
path = Path(__file__).with_name('globally_deepest_rectangle_inside_facets_certificate_two_sided.json')
if '--regenerate' in sys.argv:
    path.write_text(json.dumps(payload, indent=2)+'\n')
ck(json.loads(path.read_text()) == payload)
print(f'PASS: {checks} exact checks; {sum(cell_counts)} cells, '
      f'{len(triangles)} triangles, all Bernstein coefficients nonnegative')
