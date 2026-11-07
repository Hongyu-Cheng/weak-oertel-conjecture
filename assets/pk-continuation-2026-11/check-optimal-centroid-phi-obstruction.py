"""Exact arithmetic certificate; no floating point or external packages."""
from fractions import Fraction as F

d = 50
s = F(3, 5)
gamma = F(50, 51) ** 50
q = 1 - gamma
p2 = 1 - 2 * gamma + F(49, 51) ** 50
p3 = 1 - 3 * F(2452, 2499) ** 50 + 3 * F(2405, 2499) ** 50 - F(2358, 2499) ** 50
certificates = [
    (275 * 50**50 - 102 * 51**50, 4068043986047429985602706053949018164846014812458565621403549431200916045583537369898),
    (2 * 51**50 - 5 * 50**50, 3403287057921129734944673741972200624218705591912577144678361775858805567733656130002),
    (76 * 51**50 - 250 * 50**50 + 125 * 49**50, 727420084022539442635372648876975077461212355756106614514663906596044028494940440201),
    (4 * 2499**50 - 15 * 2452**50 + 15 * 2405**50 - 5 * 2358**50, 9787215075048633955976402806724642126219384023004732660407207393224944221178287780859324176777815665169962716026084743921308916718526931957767094815401368817365986111899),
]
assert all(value == displayed and value > 0 for value, displayed in certificates)
assert F(102, 275) < gamma < F(2, 5)
assert p2 > F(49, 125)
assert p3 > F(1, 5)
phi = lambda t: 1 - t + max(F(0), s - t)
target = F(11, 10) * gamma
assert q > s
assert phi(q) == gamma < target
assert phi(p2) / 2 < phi(F(49, 125)) / 2 == F(51, 125) < target
assert phi(p3) / 3 < phi(F(1, 5)) / 3 == F(2, 5) < target
assert (1 + s) / 4 == F(2, 5) < target
assert s * gamma < target and s / 2 == F(3, 10) < target
print('PASS: all exact integer identities and universal-k consumer bounds verified.')
