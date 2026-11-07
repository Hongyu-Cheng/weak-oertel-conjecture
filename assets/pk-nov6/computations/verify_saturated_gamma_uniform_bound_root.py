"""Exact certificate for the finite part of an all-k gamma-tail bound."""
from math import factorial
from fractions import Fraction as F

certificate=[45977,45659,45718,45852,45999,46140,46270,46389,46497,46595,
46684,46766,46841,46909,46973,47031,47085,47135,47182,47225,
47266,47304,47339,47373,47404,47433,47461,47487,47512,47535,
47557,47577,47597,47616,47633,47650,47665,47680,47694,47708,
47720,47732,47744,47755,47765,47774,47784,47792,47800,47808,
47815,47822,47829,47835,47841,47846,47851,47856,47861,47865,
47869,47872,47876,47879,47882,47884,47887,47889,47891,47893,
47894,47896,47897,47898]
assert len(certificate)==74
for m,r in enumerate(certificate,1):
    z_direct=sum((2**(m+1)-2**j)*(factorial(m)//factorial(j))*m**j for j in range(m+1))
    current=m**m
    z_recursive=0
    for j in range(m,-1,-1):
        z_recursive+=(2**(m+1)-2**j)*current
        if j:
            assert (j*current)%m==0
            current=j*current//m
    assert z_recursive==z_direct
    numerator=100000*z_direct*32**m
    denominator=2**(m+1)*factorial(m)*87**m
    assert r*denominator<=numerator<(r+1)*denominator
    assert r>45000
assert F(87,32)-(F(163,60)+F(7,4320))==F(1,2160)
assert F(3,16*75)==F(1,20)**2
print('PASS: all74 integer certificates, two exact constructions, exponential-series bound, and analytic cutoff')
