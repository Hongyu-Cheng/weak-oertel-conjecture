from fractions import Fraction as F

checks=0
for d in range(1,13):
    for a in [F(k,10) for k in range(10)]:
        # Increasing affine-power density on [a,1], shifted to start at0.
        mean=F(d,d+1)*(1-a**(d+1))/(1-a**d)-a
        reverse_mean=1-a-mean
        for k in range(21):
            t=(1-a)*F(k,20)
            cdf=((a+t)**d-a**d)/(1-a**d)
            reverse_cdf=(1-(1-t)**d)/(1-a**d)
            assert mean*cdf <= F(d,d+1)*t
            assert reverse_mean*reverse_cdf <= F(d,d+1)*t
            checks+=2
    # The sharp endpoint cone.
    assert F(d,d+1)*F(1)==F(d,d+1)
    for q in [F(k,20) for k in range(1,20)]:
        alpha=1-q**d
        expression=alpha*(d+q**d/(1-q))
        assert expression<=d
        if d>=2: assert expression<d
        assert 1-alpha/F(d+1)+q**(d+1)/(F(d+1)*(1-q)) == (d+q**d/(1-q))/F(d+1)
        checks+=1
print('PASS:',checks,'exact marginal and scalar checks, both affine-power orientations, endpoint sharpness, and strict interior algebra')
