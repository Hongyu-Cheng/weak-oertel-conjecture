"""Exact checks for private-cap meeting motion and shared-original constraints."""
from fractions import Fraction as Q


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def rank(matrix):
    a = [list(map(Q, row)) for row in matrix]
    if not a:
        return 0
    row = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        value = a[row][column]
        a[row] = [x/value for x in a[row]]
        for i in range(len(a)):
            if i != row:
                value = a[i][column]
                a[i] = [x-value*y for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def solve(matrix, rhs):
    n = len(rhs)
    a = [list(map(Q, row))+[Q(value)] for row, value in zip(matrix, rhs)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        pivot_value = a[j][j]
        a[j] = [x/pivot_value for x in a[j]]
        for i in range(n):
            if i != j:
                pivot_value = a[i][j]
                a[i] = [x-pivot_value*y for x, y in zip(a[i], a[j])]
    return [a[i][-1] for i in range(n)]


# Original coefficient order is (x,y,z,constant).
margins = [
    (1, 0, 0, 0),
    (0, 1, -1, 0),
    (-1, -1, -2, 0),
    (0, -1, 1, -1),
    (-1, 1, 2, -2),
]
groups = [[0, 1, 2], [0, 3, 4]]
f = [(Q(-1), Q(0)), (Q(1), Q(-1))]
sections = [
    [[Q(-1), Q(0)], [Q(0), Q(0)]],
    [[Q(1), Q(-1)], [Q(0), Q(0)]],
]
for group, fg, section in zip(groups, f, sections):
    normals = [margins[i][:2] for i in group]
    assert tuple(sum(u[k] for u in normals) for k in range(2)) == (0, 0)
    assert rank(normals) == 2
    assert rank([list(u)+[-1] for u in normals]) == 3
    for i in group:
        u = margins[i][:2]
        c = tuple(fg[k]-sum(u[j]*section[j][k] for j in range(2))
                  for k in range(2))
        assert c == margins[i][2:]

eps = Q(1, 20)
witnesses = [
    (0, eps, -eps/2),
    (0, -eps, 2*eps),
    (0, -eps, -eps),
    (1, -eps, -2*eps),
    (1, -eps, eps),
]
for own, (z, x, y) in enumerate(witnesses):
    assert z in (0, 1) and abs(x) < Q(1, 4) and abs(y) < Q(1, 4)
    values = [dot(row, (x, y, z, 1)) for row in margins]
    assert values[own] > 0
    assert all(value < 0 for i, value in enumerate(values) if i != own)

# Exact shared-normal inconsistency, including arbitrarily small rational times.
M = [[Q(-2), Q(0)], [Q(1), Q(0)]]
assert rank(M) == 1
assert rank([M[0]+[Q(0)], M[1]+[Q(-1)]]) == 2
for t in [Q(1, k) for k in range(2, 102)]:
    for displacement in (t, -t, t*t):
        new_m = [[Q(-2), Q(0)], [Q(1)+displacement, Q(0)]]
        rhs = [Q(-2), Q(1)]
        assert rank(new_m) == 1
        assert rank([row+[v] for row, v in zip(new_m, rhs)]) == 2

# A changing margin realizes the section motion exactly; adverse sign loses
# the integer-boundary fiber, and one common offset repairs the finite source.
for t in [Q(-1, k) for k in range(10, 60)]:
    moved = list(margins)
    moved[1] = (0, 1, -1, t)
    moved[2] = (-1, -1, -2, 2*t)
    values = [dot(row, (t, 0, 0, 1)) for row in moved]
    assert all(value < 0 for value in values)
    kappa = -t
    for z in (0, 1):
        fa, fb = -z+t+kappa, z-1+kappa
        assert max(fa, fb) >= 0

# Difference rows of any t shared normals in a full circuit have rank t-1.
private_checks = 0
for d in range(1, 9):
    normals = [[Q(int(i == j)) for j in range(d)] for i in range(d)]
    normals += [[Q(-1)]*d]
    assert rank([u+[-1] for u in normals]) == d+1
    for t in range(1, d+2):
        selected = normals[:t]
        differences = [[x-y for x, y in zip(u, selected[0])]
                       for u in selected[1:]]
        assert rank(differences) == t-1
        assert d-rank(differences) == d+1-t
        private_checks += 1

# Full-row-rank shared systems admit arbitrary small right-side and section
# changes. Reconstruct one shared original, not two separate copies.
full_rank_checks = 0
for d in range(1, 7):
    for rows in range(1, d+1):
        for denom in (100, 1000, 10000):
            t = Q(1, denom)
            matrix = [[Q(int(i == j))+t*Q(i+j+1)
                       for j in range(rows)] for i in range(rows)]
            rhs = [Q(int(i == 0))+t*Q(i+2) for i in range(rows)]
            u = solve(matrix, rhs)+[Q(0)]*(d-rows)
            extended = [row+[Q(0)]*(d-rows) for row in matrix]
            assert rank(extended) == rows
            assert [dot(row, u) for row in extended] == rhs
            # g0 has Q=f=0, hence c_shared=0. The other group has
            # Q^T=M and f=rhs, giving the exact same shared coefficient.
            assert all(value-dot(row, u) == 0 for row, value in zip(extended, rhs))
            full_rank_checks += 1

print("PASS: five strict actual witnesses; 300 exact shared-motion obstructions; "
      "50 finite-source offset repairs; "
      f"{private_checks} private-dimension and {full_rank_checks} full-rank checks.")
