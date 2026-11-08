"""Replay the finite combinatorics and exact arithmetic in the accompanying fact.

The geometric argument for the actual fibers and all-point caps is in
the accompanying fact. This script does not enumerate the lifted polytope or its caps.
Run with Python 3 and no third-party packages.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial


BLOCKS = 19
D = 1178
K = 2048
N = K - 1
Q = 220
U = N - Q
SLOTS = range(BLOCKS)
POOLS = range(55, 71)
FORMS = ((2, 2, -3),) * 4 + ((-2, -2, 3),) * 3 + ((-2, -2, 5),)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def rows(z):
    u = sum(z[:8])
    return tuple(u - v for v in z[8:]) + (u,)


def verify_local_block():
    selectors = tuple(product((0, 1), repeat=3))
    masks = tuple(product((0, 1), repeat=8))
    reps = set()
    for s in selectors:
        values = tuple(dot(form, s) for form in FORMS)
        assert not any(s) or all(values)
        signs = tuple(1 if value >= 0 else -1 for value in values)
        for bits in masks:
            z = tuple(sign * bit for sign, bit in zip(signs, bits)) + s
            if sum(rows(z)) < 0:
                z = tuple(-x for x in z)
            reps.add(z)

    assert len(reps) == len({tuple(x % 2 for x in z) for z in reps}) == K
    eligible = {}
    for z in reps:
        a = rows(z)
        assert min(a) >= 0 and (sum(a) > 0) == any(z)
        if sum(a) == 1:
            eligible[z] = a.index(1)

    # Saturated coordinates and the sign forms give the local exposure faces.
    local = reps | {tuple(-x for x in z) for z in eligible}
    assert len(local) == K + 280
    assert all(tuple((1 if i < 8 else -1) if j == i else 0 for j in range(11))
               in reps for i in range(11))
    strata = {z[8:] for z in local}
    for s in strata:
        if not any(s):
            continue
        saturated = [t for t in strata if all(not u or t[i] == u for i, u in enumerate(s))]
        sign = next(u for u in s if u)
        assert all(sign * u >= 0 for t in saturated for u in t)
        assert [t for t in saturated if sum(map(abs, t)) == sum(map(abs, s))] == [s]
        signs = tuple(1 if dot(form, s) > 0 else -1 for form in FORMS)
        assert all(dot(form, s) for form in FORMS)
        assert all(all(y in (0, sign) for y, sign in zip(z[:8], signs))
                   for z in local if z[8:] == s)
    assert {z[:8] for z in local if not any(z[8:])} == set(masks)
    for i, form in enumerate(FORMS):
        assert all(z[i] * dot(form, z[8:]) > 0
                   for z in local if z[i] and any(z[8:]))

    # The linear extensions use the owner row to add the coding offset.
    owner_selectors = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1))
    offsets = [tuple(int(dot(form, s) > 0) if owner < 3 else int(dot(form, s) < 0)
                     for form in FORMS)
               for owner, s in enumerate(owner_selectors)]
    pools = [set() for _ in offsets]
    bands, tails = [], []
    for i in SLOTS:
        weights = (100 * 3**(BLOCKS - 1 - i),) * 2 + (1, 2, 4, 8, 16, 32)
        high_scores, tail_scores = [], {}
        for z, owner in eligible.items():
            assert z[8:] == tuple((-1 if owner < 3 else 1) * x
                                  for x in owner_selectors[owner])
            mask = tuple(y + offset for y, offset in zip(z[:8], offsets[owner]))
            assert all(bit in (0, 1) for bit in mask) and sum(mask) == 4
            if i == 0:
                pools[owner].add(mask)
            priority = 20 * (dot(weights, z[:8]) +
                             dot(tuple(dot(weights, off) for off in offsets), rows(z)))
            priority += (BLOCKS - i) * sum(rows(z))
            assert priority == 20 * dot(weights, mask) + BLOCKS - i
            if mask[0] or mask[1]:
                high_scores.append(priority)
            else:
                tail_scores[mask] = priority
        assert len(high_scores) == Q and len(tail_scores) == 15
        bands.append(high_scores)
        tails.append(tail_scores)

    weight_four = {mask for mask in masks if sum(mask) == 4}
    assert len(eligible) == 280 and all(pool == weight_four for pool in pools)
    assert all(min(a) > max(b) for a, b in zip(bands, bands[1:]))
    tail_masks = sorted(tails[0], key=tails[0].get, reverse=True)
    assert len({tails[0][mask] for mask in tail_masks}) == 15
    tail_order = [row[mask] for mask in tail_masks for row in tails]
    assert min(bands[-1]) > tail_order[0]
    assert all(a > b for a, b in zip(tail_order, tail_order[1:]))


def high_winner(slots, sentinel):
    first, second, third = slots[:3]
    if sentinel == first:
        return None
    return third if sentinel == second else first


def verify_directions():
    # Only the first three indices and the sentinel matter, so these
    # representatives include every possible high-arrow pattern.
    for first, second, third in combinations(SLOTS, 3):
        triple = (first, second, third)
        for slots in (triple, *(triple + (j,) for j in range(third + 1, BLOCKS))):
            rank = {first: 0, third: 1, second: 2}
            for sentinel in slots:
                winner = high_winner(slots, sentinel)
                if winner is None:
                    assert sentinel == first
                    continue
                assert winner != sentinel and rank[winner] < rank.get(sentinel, 2)
                assert any(i < sentinel for i in slots if i != winner)
                assert high_winner(slots, winner) != sentinel

    for r, j, i in product(SLOTS, repeat=3):
        if len({r, j, i}) == 3:
            arrow = high_winner(sorted((r, j, i)), j) == i
            assert arrow == (r < j and (i < r or i > j))


def verify_three_zero_priorities():
    for zeros in combinations(SLOTS, 3):
        outsiders = [i for i in SLOTS if i not in zeros]
        # Keeping only the two least fixed highs preserves both the
        # winner and whether a tail can win.
        fixed_sets = ((), *((i,) for i in outsiders), *combinations(outsiders, 2))
        for fixed in fixed_sets:
            edges = set()
            interleaved = set()
            for j in zeros:
                i, k = (slot for slot in zeros if slot != j)
                for high_i, high_k in product((False, True), repeat=2):
                    sites = {i: high_i, k: high_k}
                    highs = sorted([slot for slot, high in sites.items() if high] + list(fixed))
                    winner = None
                    if len(highs) >= 2:
                        winner = high_winner(sorted([j, *highs]), j)
                    elif len(highs) == 1 and highs[0] < j:
                        r = highs[0]
                        candidates = [slot for slot in sites if not sites[slot] and (slot < r or slot > j)]
                        if len(candidates) == 2:
                            interleaved.add(frozenset(candidates))
                        elif candidates:
                            winner = candidates[0]
                    if winner in sites:
                        other = k if winner == i else i
                        edges.add(((winner, sites[winner]), (other, sites[other])))

            if not fixed:
                a, b, c = zeros
                order = {c: 2, a: 1, b: 0}
                assert not interleaved and all(order[i] > order[j] for (i, _), (j, _) in edges)
                continue
            assert len(interleaved) <= 1
            assert not any(not high_i and high_j for (_, high_i), (_, high_j) in edges)
            group = next(iter(interleaved), set())
            for high in (False, True):
                representatives = {i: min(group) if not high and i in group else i for i in zeros}
                arcs = {(representatives[i], representatives[j])
                        for (i, high_i), (j, high_j) in edges if high_i == high_j == high}
                while arcs:
                    incoming = {j for _, j in arcs}
                    remaining = {(i, j) for i, j in arcs if i in incoming}
                    assert len(remaining) < len(arcs)
                    arcs = remaining


def count_pools():
    ordinary = {55: (N**BLOCKS - U**BLOCKS) // Q, 71: 0}
    assert ordinary[55] == sum(U**i * N**(BLOCKS - 1 - i) for i in SLOTS)
    extra = {
        55: sum((t - 1) * comb(BLOCKS, t) * Q**(t - 2) * U**(BLOCKS - t)
                for t in range(3, BLOCKS + 1)),
        71: 0,
    }
    high_lights = sum((N**j - U**j) * N**(BLOCKS - 1 - j) -
                      j * Q * U**(BLOCKS - 2) for j in SLOTS)
    assert high_lights == Q * extra[55]

    candidate_sets = [[i for i in SLOTS if i < r or i > j]
                      for j in SLOTS for r in range(j)]
    assert Counter(map(len, candidate_sets)) == {m: m + 1 for m in range(BLOCKS - 1)}
    for k in range(56, 71):
        left, right = N - 4 * k, N - 4 * (k - 1)
        ordinary[k] = (right**BLOCKS - left**BLOCKS) // 4
        assert ordinary[k] == sum(left**i * right**(BLOCKS - 1 - i) for i in SLOTS)

        left, right = U - 4 * (k - 55), U - 4 * (k - 56)
        extra[k] = sum((m + 1) * Q * U**(BLOCKS - 2 - m) * (right**m - left**m) // 4
                       for m in range(1, BLOCKS - 1))
        # Fix the sole high and sentinel, then count the competitors
        # before and after each candidate in the current tail rank.
        assert extra[k] == sum(
            Q * U**(BLOCKS - 2 - len(axes)) * left**i * right**(len(axes) - 1 - i)
            for axes in candidate_sets for i in range(len(axes))
        )

    tail_lights = sum(Q * U**(BLOCKS - 2 - len(axes)) *
                      (U**len(axes) - (U - 60)**len(axes)) for axes in candidate_sets)
    assert tail_lights == 4 * sum(extra[k] for k in range(56, 71))
    assert all(ordinary[k] >= ordinary[k + 1] and extra[k] >= extra[k + 1] for k in POOLS)
    centers = {k: ordinary[k] - ordinary[k + 1] + extra[k] - extra[k + 1] for k in POOLS}
    assert sum(centers.values()) == ordinary[55] + extra[55]
    lights = sum(4 * k * centers[k] for k in POOLS)
    assert lights == N**BLOCKS - (N - 280)**BLOCKS + high_lights + tail_lights

    reset = BLOCKS * N**(BLOCKS - 1) - ordinary[55]
    assert reset == sum(N**(BLOCKS - 1) - U**j * N**(BLOCKS - 1 - j) for j in SLOTS)
    inactive = K**BLOCKS - N**BLOCKS - reset - sum(centers.values())
    assert reset > 0 and inactive > 0
    return centers, reset, inactive, lights


def verify_arithmetic(centers, reset, inactive):
    tau = 1 - 3 * Fraction(3, 4)**3 + 3 * Fraction(1, 2)**3 - Fraction(1, 4)**3
    beta = Fraction(3, 4)**3
    assert (tau, beta) == (Fraction(3, 32), Fraction(27, 64))
    f = D - 3
    gamma = Fraction(D, D + 1)**D
    cap = tau * Fraction(f, f + 1)**f
    mass_grid = 10**16
    inactive_mass = Fraction((mass_grid * cap / gamma) // 1 - 1, mass_grid)
    assert tau < inactive_mass and gamma * inactive_mass < cap
    volume = (N**BLOCKS + reset) * tau + inactive * inactive_mass

    grid = 10**14
    den = (f + 1)**f
    rhs = 6 * f**f * grid**D
    radii = {}
    for k in POOLS:
        lo, hi = grid // 2, grid
        assert 27 * lo**D * den <= rhs < (27 + 6 * k) * hi**D * den
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if (27 * mid**D + 6 * k * (2 * mid - grid)**D) * den <= rhs:
                lo = mid
            else:
                hi = mid
        radii[k] = lo - 1
        r = Fraction(radii[k], grid)
        assert Fraction(1, 2) < r < 1
        center, light = r**D, tau * (2 * r - 1)**D
        assert center < tau and light < cap and beta * center + k * light < cap
        volume += centers[k] * (center + 4 * k * light)

    # Ratios between successive omitted Taylor terms are at most 1/33.
    e_upper = sum(Fraction(1, factorial(j)) for j in range(33))
    e_upper += Fraction(1, 32 * factorial(32))
    target = volume / (e_upper * K**BLOCKS)
    assert gamma * inactive_mass < target
    assert target - cap > Fraction(15, 10**11)
    assert cap * K**BLOCKS / volume < Fraction(36787944, 10**8) < 1 / e_upper
    return radii, inactive_mass


def main():
    if not __debug__:
        raise SystemExit("Run without -O so the exact checks execute.")
    assert 11 * BLOCKS == 209 and 11 * BLOCKS + D == 1387
    assert K**BLOCKS == 2**209
    verify_local_block()
    verify_directions()
    verify_three_zero_priorities()
    centers, reset, inactive, lights = count_pools()
    verify_arithmetic(centers, reset, inactive)
    print(f"PASS: dimensions (209, {D}), total 1387")
    print(f"Baseline sites: {K**BLOCKS}; added light sites: {lights}")
    print("Strict raw cap margin > 1.5e-10; normalized depth < 0.36787944 / 2^209")


if __name__ == "__main__":
    main()
