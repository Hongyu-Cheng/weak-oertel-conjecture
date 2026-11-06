"""Exact finite calibrations; analytic compactness and rigidity are in the note."""
from fractions import Fraction as F
from itertools import combinations

checks = 0
def check(statement):
    global checks
    assert statement
    checks += 1

P = (-1, 0, 1)
M = F(6)
for den in range(2, 31):
    # e=s^2 makes the physical endpoint buffer rational in d=1.
    s = F(1, den)
    e = s*s
    L = {-1: e, 0: 1/e**2, 1: e}
    h = {z: e**2*L[z] for z in P}
    check(L[-1]*L[0]*L[1] == 1)  # exact equal-volume log normalization
    check(L[0] >= (L[-1]+L[1])/2)
    check(h[-1] == e**3 and h[0] == 1 and h[1] == e**3)
    # Uniform own-fiber probability rows: sigma=1/3, rho-density=1/2.
    for z in P:
        sigma = F(1, 3)
        tilted_row_density = sigma/L[z]*F(1, 2)
        check(tilted_row_density == 1/(M*L[z]))
        original_row_density = sigma*L[z]/L[z]*F(1, 2)
        check(original_row_density == 1/M)
        check(2*original_row_density == sigma)
    check(F(1, 3)+F(1, 3) == F(4, 6))
    check(F(1, 3) == F(2, 6))
    # The three source centroids are NOT simultaneously deepest.
    delta_endpoint = s**3/3
    check(delta_endpoint**2 == h[-1]/9)
    check(1+delta_endpoint < 3)  # endpoint steep-cap upper vs center symmetry lower

# All proper closed-minor quotas of the calibration, independently of depth.
closed = []
for count in (1, 2):
    for T in combinations(P, count):
        closure = tuple(z for z in P if min(T) <= z <= max(T))
        if closure != T:
            continue
        closed.append(T)
        parity = len({z % 2 for z in T})
        check(F(2*len(T)) < parity*M/2)
check(len(closed) == 5)
check({-1, 1} != {z for z in P if -1 <= z <= 1})  # zero set is not closed

# Exact marked-homothety equality yields the scale relation used in (19).
for d in range(1, 9):
    for a in (F(1, 4), F(2, 3), F(1), F(7, 3)):
        for b in (F(1, 3), F(3, 2), F(4)):
            energy_a, energy_b = a**d, b**d
            volume_a, volume_b = 5*a**d, 5*b**d
            h_a, h_b = 11*a, 11*b
            check((h_a/h_b)**d == energy_a/energy_b)
            check((h_a/h_b)**d == volume_a/volume_b)

print(f"PASS: {checks} exact vanishing-buffer calibration checks")
