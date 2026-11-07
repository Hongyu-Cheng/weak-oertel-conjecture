"""Exact shared-normal identities and bounded algebraic degree (SymPy)."""
import random
import sympy as s

R, B = s.symbols('rho beta')


def cap(r, t, rho):
    if t <= 0:
        return r*r
    if t <= rho*r:
        return r*r-t*t/rho
    if t <= r:
        return (r-t)**2/(1-rho)
    return s.Rational(0)


def degree(poly, variable):
    return -1 if s.expand(poly) == 0 else s.degree(poly, variable)


def main():
    rng = random.Random(8127701)
    checked = 0
    for _ in range(80):
        count = rng.randrange(3, 10)
        # Concave, nondecreasing rational radius chain.
        slopes = sorted([s.Rational(rng.randrange(8),4) for _ in range(count-1)],reverse=True)
        radii = [s.Rational(rng.randrange(1,9),4)]
        for slope in slopes:
            radii.append(radii[-1]+slope)
        j = rng.randrange(count)
        q = radii[j]/3
        rho = s.Rational(rng.randrange(1,10),10)
        beta = s.Rational(rng.randrange(-15,16),8)
        full, low, high = [], [], []
        for k,r in enumerate(radii):
            t = (1+rho)*q-beta*(k-j)
            if t <= 0: full.append(k)
            elif t <= rho*r: low.append(k)
            elif t <= r: high.append(k)
        N = R*(1-R)*sum(radii[k]**2 for k in full+low)
        N -= (1-R)*sum(((1+R)*q-B*(k-j))**2 for k in low)
        N += R*sum((radii[k]-(1+R)*q+B*(k-j))**2 for k in high)
        N = s.expand(N)
        aa = N.coeff(B,2)
        bb = N.coeff(B,1)
        cc = N.coeff(B,0)
        l2 = sum((k-j)**2 for k in low)
        h2 = sum((k-j)**2 for k in high)
        l1 = sum(k-j for k in low)
        h1 = sum(k-j for k in high)
        hzr = sum((k-j)*radii[k] for k in high)
        assert s.expand(aa-(R*(l2+h2)-l2)) == 0
        assert s.expand(bb-(2*q*(1-R**2)*l1+2*R*hzr-2*q*R*(1+R)*h1)) == 0
        assert degree(aa,R) <= 1 and degree(bb,R) <= 2 and degree(cc,R) <= 3
        assert s.simplify(s.diff(N/(R*(1-R)),B,2)-2*aa/(R*(1-R))) == 0
        actual = sum(cap(r,(1+rho)*q-beta*(k-j),rho) for k,r in enumerate(radii))
        assert s.simplify(N.subs({R:rho,B:beta})/(rho*(1-rho))-actual) == 0
        tail = s.Rational(0)
        for k,r in enumerate(radii):
            t=(1+rho)*q-beta*(k-j)
            tail += max(r-t,0)**2/(1-rho)-max(rho*r-t,0)**2/(rho*(1-rho))+max(-t,0)**2/rho
        assert s.simplify(tail-actual) == 0
        U = s.expand(4*aa*cc-bb*bb)
        W = s.expand(4*aa*R*(1-R))
        assert degree(U,R) <= 4 and degree(W,R) <= 3
        assert degree(s.expand(s.diff(U,R)*W-U*s.diff(W,R)),R) <= 6
        for c0,c1 in [(s.Rational(1,7),s.Rational(-2,3)),(s.Rational(0),s.Rational(1))]:
            edge = s.expand(N.subs(B,c0+c1*R))
            assert degree(edge,R) <= 3
            den=R*(1-R)
            assert degree(s.expand(s.diff(edge,R)*den-edge*s.diff(den,R)),R) <= 4
        checked += 1
    f=(s.Rational(33,32)-s.Rational(5,4)*R+s.Rational(3,4)*R**2)/(1-R)
    rho_star=1-s.sqrt(102)/12
    assert s.simplify(s.diff(f,R).subs(R,rho_star)) == 0
    assert s.simplify(f.subs(R,rho_star)-(s.sqrt(102)-2)/8) == 0
    assert s.simplify(s.diff(f,R,2)-s.Rational(17,16)/(1-R)**3) == 0
    assert rho_star > 0 and rho_star < s.Rational(1,4)
    radii=[s.Rational(1,2),s.Rational(3,2),s.Rational(3,4)]
    for k,r in enumerate(radii):
        t=(1+rho_star)/2+s.Rational(1,8)*(k-1)
        assert t > rho_star*r and t < r
    assert (s.sqrt(102)-2)/8 < s.Rational(81,80)
    print(f"PASS: {checked} exact coupled trace-cell identities and degree bounds; "
          "all tail terms and the strict unequal-normal stationary branch.")


if __name__=='__main__':
    main()
