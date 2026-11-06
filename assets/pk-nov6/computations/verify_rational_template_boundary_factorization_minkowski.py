"""Exact finite calibrations of the marked factorization; not its proof."""

from fractions import Fraction as F
from itertools import combinations
from math import lcm

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


def independent_solution(columns, target):
    """Solve an overdetermined independent-column system over Q."""
    count = len(columns)
    rows = [[F(column[i]) for column in columns] + [F(target[i])]
            for i in range(len(target))]
    pivot_rows = []
    start = 0
    for col in range(count):
        pivot = next((i for i in range(start, len(rows)) if rows[i][col]), None)
        if pivot is None:
            return None
        rows[start], rows[pivot] = rows[pivot], rows[start]
        scale = rows[start][col]
        rows[start] = [entry / scale for entry in rows[start]]
        for i in range(len(rows)):
            if i != start and rows[i][col]:
                scale = rows[i][col]
                rows[i] = [entry - scale * value
                           for entry, value in zip(rows[i], rows[start])]
        pivot_rows.append(start)
        start += 1
    if any(all(entry == 0 for entry in row[:-1]) and row[-1] for row in rows):
        return None
    return tuple(rows[i][-1] for i in pivot_rows)


def anchored_vertices(points, source):
    size = len(points)
    output = set()
    for count in range(1, min(size, len(source) + 1) + 1):
        for support in combinations(range(size), count):
            coefficients = independent_solution(
                [(1,) + points[i] for i in support], (1,) + source)
            if coefficients is None or not all(value > 0 for value in coefficients):
                continue
            vertex = [F(0)] * size
            for i, value in zip(support, coefficients):
                vertex[i] = value
            output.add(tuple(vertex))
    return sorted(output)


def choose_decomposition(vertices, weights):
    for count in range(1, min(len(vertices), len(weights)) + 1):
        for support in combinations(range(len(vertices)), count):
            coefficients = independent_solution([vertices[r] for r in support], weights)
            if coefficients is None or not all(value >= 0 for value in coefficients):
                continue
            theta = [F(0)] * len(vertices)
            for r, value in zip(support, coefficients):
                theta[r] = value
            return theta
    raise AssertionError("No independent affine sublist found")


families = [
    [(0,)],
    [(0,), (1,), (2,)],
    [(0,), (1,), (2,), (3,), (4,)],
    [(0, 0), (2, 0), (0, 2), (2, 2), (1, 1)],
    [(0, 0), (3, 0), (0, 3), (1, 1)],
]

for points in families:
    size = len(points)
    for source in points:
        vertices = anchored_vertices(points, source)
        check(bool(vertices))
        denominator = lcm(*(a.denominator for vertex in vertices for a in vertex))
        for vertex in vertices:
            check(sum(vertex) == 1)
            check(all((denominator * a).denominator == 1 for a in vertex))
            for coordinate in range(len(source)):
                check(sum(vertex[i] * points[i][coordinate] for i in range(size))
                      == source[coordinate])
        mixtures = [tuple(F(r + 1, len(vertices) * (len(vertices) + 1) // 2)
                          for r in range(len(vertices)))]
        for r in range(len(vertices)):
            theta = [F(0)] * len(vertices)
            theta[r] = 1
            mixtures.append(tuple(theta))
        for r, t in combinations(range(len(vertices)), 2):
            for fraction in (F(1, 2), F(1, 3), F(2, 5)):
                theta = [F(0)] * len(vertices)
                theta[r], theta[t] = fraction, 1 - fraction
                mixtures.append(tuple(theta))
        for mixture in mixtures:
            weights = [sum(mixture[r] * vertices[r][i] for r in range(len(vertices)))
                       for i in range(size)]
            theta = choose_decomposition(vertices, weights)
            check(sum(theta) == 1)
            check(all(sum(theta[r] * vertices[r][i] for r in range(len(vertices))) == weights[i]
                      for i in range(size)))
            # All fibers are [-1,1]^2, all normals (0,1). Each q conditional
            # law has two atoms, with probabilities 1/3 and 2/3.
            atoms = [(F(2 * i - size + 1, size + 1), F(size - 2 * i, size + 1))
                     for i in range(size)]
            means = [(a + 2 * b) / 3 for a, b in atoms]
            original_x = sum(weights[i] * means[i] for i in range(size))
            intermediate = [sum(vertex[i] * means[i] for i in range(size))
                            for vertex in vertices]
            check(sum(theta[r] * intermediate[r] for r in range(len(vertices))) == original_x)
            for r, vertex in enumerate(vertices):
                if not theta[r]:
                    continue
                check(-1 <= intermediate[r] <= 1)
                second_mass = F(0)
                second_moment = F(0)
                for i in range(size):
                    split = F(0) if not weights[i] else theta[r] * vertex[i] / weights[i]
                    check(0 <= split <= 1)
                    for atom, conditional_mass in zip(atoms[i], (F(1, 3), F(2, 3))):
                        new_mass = split * weights[i] * conditional_mass
                        second_mass += new_mass
                        second_moment += new_mass * atom
                check(second_mass == theta[r])
                check(second_moment == theta[r] * intermediate[r])
            for i in range(size):
                for conditional_mass in (F(1, 3), F(2, 3)):
                    reconstructed = sum(
                        (F(0) if not weights[i] else theta[r] * vertices[r][i] / weights[i])
                        * weights[i] * conditional_mass
                        for r in range(len(vertices)))
                    check(reconstructed == weights[i] * conditional_mass)

# The exact flat-face obstruction and its unavoidable two intermediate points.
vertices = anchored_vertices([(0,), (1,), (2,)], (1,))
check(set(vertices) == {(F(0), F(1), F(0)), (F(1, 2), F(0), F(1, 2))})
theta = choose_decomposition(vertices, (F(1, 4), F(1, 2), F(1, 4)))
check(theta == [F(1, 2), F(1, 2)])
means = (-1, 1, -1)
check(sorted(sum(vertex[i] * means[i] for i in range(3)) for vertex in vertices) == [-1, 1])
check(sum(a * b for a, b in zip((F(1, 4), F(1, 2), F(1, 4)), means)) == 0)

print(f"PASS: {checks} exact rational checks")
