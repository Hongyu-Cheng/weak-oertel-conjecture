"""Exact arithmetic calibration of the actual square-chain index obstruction.

The arbitrary-size statement and the constrained second-order alternative
are proved in the companion Markdown note, not inferred from these checks.
"""

from fractions import Fraction as F

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


normals = [(1, 2), (-2, 1), (1, -3)]
check(tuple(sum(v[i] for v in normals) for i in range(2)) == (0, 0))
check(normals[0][0] * normals[1][1] - normals[0][1] * normals[1][0] == 5)
check(all(abs(x) != abs(y) and x and y for x, y in normals))

for m in range(2, 13):
    indices = list(range(-m, m + 1))
    radius = {j: 1 - F(j*j, 4*m*m) for j in indices}
    mass = 4 * sum(r*r for r in radius.values())
    check(min(radius.values()) == F(3, 4))
    check(max(radius.values()) == 1)
    check(4 < mass / 2)
    check(2*m > 2)
    for j in range(-m + 1, m):
        check(radius[j-1] - 2*radius[j] + radius[j+1] == -F(1, 2*m*m))
    # In one integer dimension these strict pairwise barycentric conditions
    # certify every nontrivial compatible-support inequality.
    for left in indices:
        for right in indices:
            if right - left < 2:
                continue
            for j in range(left + 1, right):
                weight = F(right-j, right-left)
                check(radius[j] > weight*radius[left] + (1-weight)*radius[right])
    # A rational basis of the neutral radius space: e_j-r_j e_0.
    for j in indices:
        if j == 0:
            continue
        velocity = {k: F(0) for k in indices}
        velocity[j] = 1
        velocity[0] = -radius[j]
        check(sum(radius[k]*velocity[k] for k in indices) == 0)
        volume_hessian = 8*sum(a*a for a in velocity.values())
        check(volume_hessian == 8*(1+radius[j]**2) > 0)
        cap_hessian = volume_hessian/2
        check(volume_hessian-cap_hessian-cap_hessian == 0)

print(f"PASS {checks} exact rational checks")
