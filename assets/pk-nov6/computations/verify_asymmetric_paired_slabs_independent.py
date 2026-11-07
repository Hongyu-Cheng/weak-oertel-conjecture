from fractions import Fraction as F

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


Z = tuple(range(-2, 4))
LO = (F(-1),) * 6
HI = tuple(map(F, ('-9/10', '1/20', '1', '1', '1/20', '-9/10')))
M = sum(h-l for l, h in zip(LO, HI))
y = F(-1, 40)
Q = F(17, 8)


def traces(p, mark, slope, upward=True):
    v = tuple(max(F(0), min(h-l, h-mark-slope*(z-p)))
              for z, l, h in zip(Z, LO, HI))
    return v if upward else tuple(h-l-a for l, h, a in zip(LO, HI, v))


slopes = tuple(HI[i+1]-HI[i] for i in range(5))
check(slopes == tuple(map(F, ('19/20', '19/20', '0', '-19/20', '-19/20'))))
check(all(slopes[i] >= slopes[i+1] for i in range(4)))
check(M == F(63, 10))
check(HI == HI[::-1])

knots = sorted(set((endpoint-y)/z for z, l, h in zip(Z, LO, HI)
                   if z for endpoint in (l, h)))
expected = [('-39/40', '167/40'), ('-39/80', '59/16'), ('-13/40', '16/5'),
            ('-7/24', '3'), ('-3/40', '47/20'), ('3/80', '17/8'),
            ('7/16', '17/8'), ('39/80', '89/40'), ('39/40', '89/40'),
            ('41/40', '87/40')]
check(knots == [F(t) for t, _ in expected])
for t, v in expected:
    mass = sum(traces(0, y, F(t)))
    check(mass == F(v))
    check(Q <= mass <= M-Q)
    # Verify affine interpolation on both neighboring subsegments.
for a, b in zip(knots[:-1], knots[1:]):
    for theta in (F(1, 3), F(1, 2), F(2, 3)):
        t = (1-theta)*a+theta*b
        check(sum(traces(0, y, t)) ==
              (1-theta)*sum(traces(0, y, a))+theta*sum(traces(0, y, b)))
for t in (knots[0]-1, knots[0]-100):
    check(sum(traces(0, y, t)) == F(167, 40))
for t in (knots[-1]+1, knots[-1]+100):
    check(sum(traces(0, y, t)) == F(87, 40))

up = traces(0, y, F(1, 4))
down = traces(0, y, F(-2), upward=False)
check(up == tuple(map(F, ('0', '13/40', '41/40', '31/40', '0', '0'))))
check(down == tuple(map(F, ('1/10', '21/20', '39/40', '0', '0', '0'))))
check(sum(up) == sum(down) == Q)
check(sum(traces(1, y, F(-1, 4))) == Q)
check(sum(traces(1, y, F(2), upward=False)) == Q)
# Margins in (z,x,constant) coordinates; addition removes x globally.
left_margins = ((F(-1, 4), F(1), -y), (F(-2), F(-1), y))
right_margins = ((F(1, 4), F(1), -y-F(1, 4)), (F(2), F(-1), y-F(2)))
check(tuple(sum(v[k] for v in left_margins) for k in range(3)) ==
      (F(-9, 4), F(0), F(0)))
check(tuple(sum(v[k] for v in right_margins) for k in range(3)) ==
      (F(9, 4), F(0), F(-9, 4)))

check(sum(h-l for z, l, h in zip(Z, LO, HI) if z <= 0) == F(63, 20))
check(sum(h-l for z, l, h in zip(Z, LO, HI) if z >= 0) == F(103, 20))
check(sum(traces(0, F(0), F(2, 5))) == F(41, 20))
target = F(1, 2)*2+F(21, 20)+F(1, 10)
check(target == F(43, 20))
check(target-Q == F(1, 40))
check(Q/M == F(85, 252) > F(1, 4))

print(f'{checks} exact checks PASS')
