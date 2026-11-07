from fractions import Fraction as F

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def nonnegative_affine_length(slope, intercept):
    # Length of {0<=x<=1:slope*x+intercept>=0}; closed endpoints
    # have the same ordinary length and are retained in the conditions.
    if slope == 0:
        return F(1) if intercept >= 0 else F(0)
    root = -intercept/slope
    if slope > 0:
        return max(F(0),F(1)-max(F(0),root))
    return max(F(0),min(F(1),root))

# Convex affine-power examples, using exact powered comparisons.
for d in range(1,21):
    gamma = F(d,d+1)**d
    check(F(1,3) < gamma <= F(1,2))
    for p in range(1,21):
        # On a d-simplex, f=(sum x)^p has mean d/(d+p), and
        # sublevel-at-mean volume (d/(d+p))^(d/p).
        check(F(d,d+p)**d >= gamma**p)

# A convex function with a genuine minimum atom.
for j in range(21):
    c = F(j,20)
    mean = (1-c)**2/2
    mass = min(F(1),c+mean)
    check(mass >= F(1,2))
    check(mass == F(1,2)+c*c/2)

# The mean interval and ALL tested actual projected affine cuts.
for eps in (F(1,100),F(1,10),F(1,4),F(2,5)):
    low_mean,high_mean = F(1,4)-eps,F(3,4)+eps
    check(high_mean-low_mean == F(1,2)+2*eps)
    for r in range(11):
        t0 = low_mean+(high_mean-low_mean)*F(r,10)
        check(F(1,4)-eps <= t0 <= F(3,4)+eps)
        for alpha in range(-7,8):
            for u in range(-7,8):
                if alpha == u == 0:
                    continue
                if alpha > 0:
                    # alpha*(b(x)-t0)+u*(x-1/2)>=0.
                    slope = -F(alpha,2)+u
                    intercept = alpha*(1+eps-t0)-F(u,2)
                elif alpha < 0:
                    # The maximum is at the lower endpoint a(x).
                    slope = F(alpha,2)+u
                    intercept = alpha*(-eps-t0)-F(u,2)
                else:
                    slope,intercept = F(u),-F(u,2)
                check(nonnegative_affine_length(slope,intercept) >= F(1,2))

# Exact original and extruded fibers for the relocation certificate.
eps = F(1,100)
def fiber_length(t,k):
    # a(x)-k<=t<=b(x)+k gives x<=2(t+k+eps)
    # and x<=2(1+eps+k-t), in [0,1].
    return max(F(0),min(F(1),2*(t+k+eps),2*(1+eps+k-t)))

old = [fiber_length(t,0) for t in range(-2,4)]
new = [fiber_length(t,1) for t in range(-2,4)]
check(old == [0,0,2*eps,2*eps,0,0])
check(new == [0,2*eps,1,1,2*eps,0])
check(sum(old) == 4*eps)
check(sum(new) == sum(old)+2)
check(sum(new) == F(51,25))
cap_mass = sum(min(length,2*eps) for length in new)
check(cap_mass == 8*eps == F(2,25))
check(cap_mass/sum(new) == F(2,51))
new_raw = F(1,2)+2*eps
check(new_raw == F(13,25))
check(new_raw/sum(new) == F(13,51))
check(F(2,51) < F(1,6))
check(F(13,51) > F(1,4))
for d in range(1,101):
    gamma = F(d,d+1)**d
    for n in range(1,11):
        check(F(2,51*2**(n-1)) < gamma/2**n)
        check(F(13,51*2**(n-1)) > gamma/2**n)

# The raw finite-extrusion target deficit is exactly unchanged.
for k in range(11):
    for d in range(1,11):
        gamma = F(d,d+1)**d
        for Q in (F(0),F(1,100),F(1,5)):
            M,A = F(7,5),F(9,7)
            check(Q+k*gamma*A-gamma*(M+2*k*A)/2 == Q-gamma*M/2)

# Mixed-quotient mean-sublevel obstruction, including closed threshold.
for N in range(1,50):
    values = [F(0)]*(N+1)+[F(-1)]
    mean = sum(values)/len(values)
    check(mean == -F(1,N+2))
    check(sum(v <= mean for v in values) == 1)

print(f'PASS: {checks} exact mean-sublevel, endpoint-shadow and center-relocation checks')
