"""Exact finite calibrations of the general face/join/parity proof."""
from itertools import combinations, product

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) < 2:
        return points
    lower = []
    for p in points:
        while len(lower) > 1 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) > 1 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


grid = list(product(range(-1, 3), repeat=2))
seen = set()
cases = 0
overlap_cases = 0
for size in (1, 2, 3, 4):
    for generators in combinations(grid, size):
        vertices = tuple(hull(generators))
        key = frozenset(vertices)
        if key in seen:
            continue
        seen.add(key)
        if len(vertices) == 1:
            P = set(vertices)
            faces = [frozenset(P)]
        elif len(vertices) == 2:
            a, b = vertices
            P = {
                p for p in grid
                if cross(a, b, p) == 0
                and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
                and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
            }
            faces = [frozenset([a]), frozenset([b]), frozenset(P)]
        else:
            edges = list(zip(vertices, vertices[1:]+vertices[:1]))
            P = {p for p in grid if all(cross(a, b, p) >= 0 for a, b in edges)}
            faces = [frozenset([v]) for v in vertices]
            faces += [frozenset(p for p in P if cross(a, b, p) == 0) for a, b in edges]
            faces.append(frozenset(P))
        faces = set(faces)
        minimal = {
            p: frozenset.intersection(*(face for face in faces if p in face))
            for p in P
        }
        check(all(minimal[p] in faces for p in P))
        candidates = set(minimal.values())
        maximal = {face for face in candidates if not any(face < other for other in candidates)}
        check(set().union(*maximal) == P)
        witnesses = [min(p for p in P if minimal[p] == face) for face in maximal]
        parity = lambda p: (p[0] % 2, p[1] % 2)
        check(len(set(map(parity, witnesses))) == len(witnesses))
        check(len(witnesses) <= len(set(map(parity, P))) <= 4)
        for p, q in product(P, repeat=2):
            if parity(p) == parity(q):
                m = ((p[0]+q[0])//2, (p[1]+q[1])//2)
                check(m in P)
                join = frozenset.intersection(*(face for face in faces if p in face and q in face))
                check(minimal[m] == join)
        # Every supporting face through a witness contains its fixed face.
        for p in witnesses:
            for face in faces:
                if p in face:
                    check(minimal[p] <= face)
        if any(a & b for a, b in combinations(maximal, 2)):
            overlap_cases += 1
        cases += 1

# Sharp count and an overlapping three-face cover.
cube = set(product((0, 1), repeat=2))
check(len(cube) == len(set((x % 2, y % 2) for x, y in cube)) == 4)
triangle = {(x, y) for x in range(3) for y in range(3) if x+y <= 2}
edge_faces = [{p for p in triangle if p[0] == 0},
              {p for p in triangle if p[1] == 0},
              {p for p in triangle if p[0]+p[1] == 2}]
check(set().union(*edge_faces) == triangle)
check(all(a & b for a, b in combinations(edge_faces, 2)))
check({(0, 1), (1, 0), (1, 1)} <= triangle)

# Four exact protecting quadrants: the overlap-free-interior angular
# calibration has zero in every vertex-selection convex hull.
menus = [[(1, 0), (0, 1)], [(-1, 0), (0, 1)],
         [(-1, 0), (0, -1)], [(1, 0), (0, -1)]]
for selection in product(*menus):
    vectors = set(selection)
    # For these four menus every selection has an opposite pair.
    check(any((-x, -y) in vectors for x, y in vectors))
for v in product(range(-3, 4), repeat=2):
    protecting = [all(g[0]*v[0]+g[1]*v[1] >= 0 for g in menu) for menu in menus]
    check(any(protecting))

print("PASS", checks, "exact checks on", cases, "complete lattice hulls;",
      overlap_cases, "cases have overlapping maximal measured faces")
