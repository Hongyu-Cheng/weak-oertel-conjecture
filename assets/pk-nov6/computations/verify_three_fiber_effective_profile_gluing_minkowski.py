from fractions import Fraction as F

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


def tail(L, t):
    return min(2 * L, max(F(0), L - t))


def D(L, x, r):
    return tail(L, r - x) - tail(L, r + x)


def G(l, c, a, r):
    return (tail(l, r + c - a)
            + tail(l + 2 * c, r - c)
            + tail(l, r + c + a))


# Exact breakpoint checks for the piecewise-linear paired tails.
for l in [F(1, 2), F(1), F(3, 2)]:
    for j in range(13):
        c = l * F(j, 12)
        R, M, B = l + 2*c, 6*l + 4*c, 3*l + c
        for h in range(-32, 33):
            a = l * F(h, 8)
            centers = [(a-c, l), (c, R), (-a-c, l)]
            knots = {F(0), l+c}
            for x, L in centers:
                knots.update([abs(x-L), abs(x+L)])
            ordered = sorted(knots)
            probes = set(ordered)
            probes.update((x+y)/2 for x, y in zip(ordered, ordered[1:]))
            probes.add(ordered[-1]+l)
            for r in probes:
                value = G(l, c, a, r) + G(l, c, a, -r)
                delta = D(l, a+c, r) - D(l, a-c, r)
                check(value-M == D(R, c, r)-delta)
                check(0 <= delta <= 4*c)
                check(0 <= D(R, c, r) <= 2*c)
                if r <= l+c:
                    check(D(R, c, r) == 2*c)
                else:
                    check(delta <= 2*c)
                check(2*B <= value <= 2*(M-B))


def clip(poly, ax, ay, b):
    result = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp = ax*p[0] + ay*p[1] - b
        fq = ax*q[0] + ay*q[1] - b
        if fp >= 0:
            result.append(p)
        if (fp > 0 and fq < 0) or (fp < 0 and fq > 0):
            t = fp/(fp-fq)
            result.append((p[0]+t*(q[0]-p[0]), p[1]+t*(q[1]-p[1])))
    return result


def area(poly):
    if not poly:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p, q in zip(poly, poly[1:]+poly[:1])))/2


l, c, eps, A = F(1), F(9, 20), F(1, 2), F(2)
M, B = 6*l+4*c, 3*l+c
table = []
for z in [-1, 0, 1]:
    upper = l + 4*c*(1-abs(z))
    rectangle = [(-l, -F(1, 2)), (upper, -F(1, 2)),
                 (upper, F(1, 2)), (-l, F(1, 2))]
    row = [area(clip(rectangle, F(1), F(0), c)),
           area(clip(rectangle, F(-1), eps, -c-A*z)),
           area(clip(rectangle, F(-1), -eps, -c+A*z))]
    table.append(row)
    check(area(rectangle) < M/2)
check(table == [[F(11,20), F(0), F(2)],
                [F(47,20), F(29,20), F(29,20)],
                [F(11,20), F(2), F(0)]])
for i in range(3):
    check(sum(row[i] for row in table) == B)
check(B/M == F(23,52))
check(M-F(9,4)*B == F(3,80))
check(F(4,9)-B/M == F(1,468))
check((3*B-M)/B == F(17,23))
check(F(3,4)-F(17,23) == F(1,92))

# The coefficient vectors are for (z,x,w,constant).
margins = [(F(0), F(1), F(0), -c),
           (A, F(-1), eps, c),
           (-A, F(-1), -eps, c)]
check(all(2*margins[0][j]+margins[1][j]+margins[2][j] == 0
          for j in range(4)))
check(margins[0][1]*margins[1][2]-margins[0][2]*margins[1][1] != 0)
for point, only in [((F(0), F(1), F(0)), 0),
                    ((F(1), -F(1,2), F(0)), 1),
                    ((F(-1), -F(1,2), F(0)), 2)]:
    vals = [sum(m[j]*point[j] for j in range(3))+m[3] for m in margins]
    check(vals[only] > 0 and all(vals[j] < 0 for j in range(3) if j != only))

# Integrate arbitrary tilted cap tails over the symmetric product interval.
# All breakpoints are known exactly, so each trapezoid is an exact integral.
for a_num in range(-20, 21):
    a = F(a_num, 4)
    for v_num in range(-12, 13):
        v = F(v_num, 3)
        cuts = {-F(1,2), F(1,2)}
        if v:
            for center, radius in [(a-c,l), (c,l+2*c), (-a-c,l)]:
                for endpoint in [center-radius, center+radius]:
                    w = -endpoint/v
                    if -F(1,2) < w < F(1,2):
                        cuts.add(w)
        cuts = sorted(cuts)
        mass = sum((b-a_)*(G(l,c,a,-v*a_)+G(l,c,a,-v*b))/2
                   for a_,b in zip(cuts,cuts[1:]))
        check(B <= mass <= M-B)

print(f"PASS {checks} exact checks")
