"""Exact all-tilt countercertificate for a monotone concave triangle chain."""
from fractions import Fraction as Q
from verify_four_monotone_triangle_centroids import envelope, positive_cap, exact_tilt_minimum, G


def evaluate(radii, j, beta):
    q = radii[j]/3
    return sum((envelope(r,q-beta*(k-j)) for k,r in enumerate(radii)),Q(0))


def main():
    r = list(map(Q,[1,3,3]))
    expected = [Q(4,9),Q(4),Q(4)]
    betas = [Q(-3),Q(-1,2),Q(3)]
    for j in range(3):
        assert evaluate(r,j,betas[j]) == expected[j]
        assert exact_tilt_minimum(r,j) == expected[j]
    target = G*sum(x*x for x in r)/2
    assert target == Q(38,9)
    assert target-max(expected) == Q(2,9)
    assert max(expected)/target == Q(18,19)
    assert G*9+Q(1,2) == Q(9,2) > target
    profiles = 0
    for R in [Q(1,3),Q(1),Q(2),Q(3),Q(7,2)]:
        for k in range(1,25):
            a = R*Q(k,72)
            radii = [a,R,R]
            assert R-a >= 0
            values = [G*a*a,G*R*R,G*R*R]
            for j,beta in enumerate([-2*R,-R/6,2*R]):
                assert evaluate(radii,j,beta) == values[j]
                assert exact_tilt_minimum(radii,j) == values[j]
            target = G*(a*a+2*R*R)/2
            assert target-max(values) == G*a*a/2 > 0
            assert G*R*R+a*a/2-target == Q(5,18)*a*a > 0
            weights = [a*a,R*R,R*R]
            total = sum(weights)
            medians = [j for j in range(3)
                       if 2*sum(weights[:j]) <= total and 2*sum(weights[j+1:]) <= total]
            assert medians == [1]
            assert positive_cap(R,R/2,Q(1,2)) == 0
            assert positive_cap(R,R/3,Q(1,2)) == Q(5,9)*R*R > G*R*R
            profiles += 1
    print(f"PASS: exact three-anchor infima, {profiles} rational family profiles, "
          "unique median and actual source safety arithmetic.")


if __name__ == '__main__':
    main()
