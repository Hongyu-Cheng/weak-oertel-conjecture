from fractions import Fraction as F


def clamp(v, w):
    return min(w, max(F(0), v))


def exact_midpoint_depth(widths, j):
    slopes = {F(0)}
    for k, w in enumerate(widths):
        if k != j:
            slopes.add(w / (2*(k-j)))
            slopes.add(-w / (2*(k-j)))
    return min(sum(
        clamp(w/2+beta*(k-j), w) for k, w in enumerate(widths)
    ) for beta in slopes)


def tail_formula(N, q, j):
    widths = [q+k for k in range(N)]
    values = [sum(widths[:j])+widths[j]/2,
              sum(widths[j+1:])+widths[j]/2]
    for k in range(N):
        if k > j:
            values.append(sum(min(q+i, (k-i)*(q+j)/(2*(k-j))) for i in range(k)))
        elif k < j:
            values.append(sum(min(q+i, (i-k)*(q+j)/(2*(j-k))) for i in range(k+1,N)))
    return min(values)


checks = 0
for N in range(1, 13):
    for q in [F(1,20), F(1,3), F(1), F(7,3), F(9), F(100)]:
        widths = [q+k for k in range(N)]
        for j in range(N):
            assert exact_midpoint_depth(widths, j) == tail_formula(N,q,j)
            checks += 1

for qi in range(1, 121):
    q = F(qi, 20)
    widths = [q,q+2,q+4]
    depths = [exact_midpoint_depth(widths,j) for j in range(3)]
    assert depths == [q/2,(3*q+2)/2,(q+4)/2]
    beta = max(depths)/sum(widths)
    assert beta == max(q+4,3*q+2)/(6*q+12)
    assert beta >= F(5,18)
    assert (beta == F(5,18)) == (q == 1)
    checks += 1

for widths, target in [([1,3],F(3,8)), ([1,3,5],F(5,18)), ([1,3,5,7],F(13,32))]:
    widths = list(map(F,widths))
    depths = [exact_midpoint_depth(widths,j) for j in range(len(widths))]
    assert max(depths)/sum(widths) == target

widths = list(map(F,[1,3,5,7]))
assert [exact_midpoint_depth(widths,j) for j in range(4)] == list(map(F,[F(1,2),F(5,2),F(13,2),F(7,2)]))
for j,beta in enumerate([F(-7,2),F(-5,2),F(-7,2),F(7,2)]):
    cap = sum(clamp(w/2+beta*(k-j),w) for k,w in enumerate(widths))
    assert cap <= F(13,2)

for s in [F(10,11),F(1),F(6,5),F(14,11)]:
    t = (s-1)/2
    assert s-2*t == 1
    lower,upper = t-s/4,t+9*s/4
    assert -1 < lower < 0
    assert 2 <= upper <= 3
    assert [1+2*(k-t)/s for k in range(3)] == [F(k)/s for k in [1,3,5]]
    if s == F(10,11):
        assert upper == 2 and t == F(-1,22)
    if s == F(14,11):
        assert upper == 3 and t == F(3,22)

assert F(3,8) > F(5,18) and F(13,32) > F(5,18)
print(f'PASS: {checks} exact affine-profile/midpoint checks; three-fiber formula; scale-phase ridge and both positive-mass jumps; four-fiber cover.')
