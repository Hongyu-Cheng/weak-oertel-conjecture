"""Exact certificates for maximum-depth increase under simplex compression."""
from fractions import Fraction as Q

def clip(value, width):
    return min(max(value, Q(0)), width)

def cap(fibers, index, height, slope):
    return sum((clip(upper-height-slope*(j-index), upper-lower)
                for j, (lower, upper) in fibers.items()), Q(0))

def breaks(fibers, index, height):
    return sorted({(endpoint-height)/(j-index)
                   for j, ends in fibers.items() if j != index
                   for endpoint in ends})

small = {-1: (Q(0), Q(1)), 0: (Q(0), Q(2)), 1: (Q(0), Q(1))}
small_breaks = breaks(small, 0, Q(3, 4))
assert small_breaks == [Q(-3,4),Q(-1,4),Q(1,4),Q(3,4)]
assert [cap(small, 0, Q(3,4), s) for s in small_breaks] == [Q(9,4),Q(7,4),Q(7,4),Q(9,4)]
assert cap(small,0,Q(3,4),Q(-100)) == cap(small,0,Q(3,4),Q(100)) == Q(9,4)
assert Q(7,16) < Q(1,2)

large = {j: (Q(0),Q(length)) for j,length in enumerate([2,6,10,3])}
large_breaks = breaks(large, 2, Q(4))
assert large_breaks == list(map(Q, [-4,-2,-1,1,2,4]))
assert [cap(large,2,Q(4),s) for s in large_breaks] == list(map(Q,[9,7,7,9,12,14]))
assert cap(large,2,Q(4),Q(-100)) == 9
assert cap(large,2,Q(4),Q(100)) == 14
assert sum(upper-lower for lower,upper in large.values()) == 21
assert max(upper-lower for lower,upper in large.values()) < Q(21,2)

compressed = {j: (-upper/2, upper/2) for j,(_,upper) in large.items()}
cbreaks = breaks(compressed,2,Q(0))
assert cbreaks == [Q(-3),Q(-3,2),Q(-1,2),Q(1,2),Q(3,2),Q(3)]
assert [cap(compressed,2,Q(0),s) for s in cbreaks] == [Q(8),Q(19,2),Q(19,2),Q(23,2),Q(23,2),Q(13)]
assert cap(compressed,2,Q(0),Q(-100)) == 8
assert cap(compressed,2,Q(0),Q(100)) == 13
# Each piece is affine; checking both endpoints proves the entire formula.
pieces = [(Q(0),Q(1,2),lambda b:Q(21,2)-2*b),
          (Q(1,2),Q(3,2),lambda b:Q(19,2)),
          (Q(3,2),Q(3),lambda b:11-b),
          (Q(3),Q(100),lambda b:Q(8))]
for left,right,formula in pieces:
    for b in [left,right]:
        assert cap(compressed,2,Q(0),-b) == formula(b)
        assert 8 <= formula(b) <= Q(21,2)

assert Q(7,21) < Q(8,21)
print("PASS: both exact maximum-depth simplex-compression counterexamples")
