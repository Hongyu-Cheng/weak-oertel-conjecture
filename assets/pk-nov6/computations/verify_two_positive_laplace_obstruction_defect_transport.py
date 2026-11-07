from fractions import Fraction as Q
assert Q(707,500)**2<2<Q(71,50)**2
assert Q(1,2**30)<Q(1,1000)
assert Q(1,1024)<Q(1,1000)
assert Q(707,500)-Q(1,1000)>Q(141,100)
assert 2*(Q(71,50)+Q(1,1000)-1)==Q(421,500)
assert 2*sum(Q(1,(2*k+1)*3**(2*k+1)) for k in range(3))>Q(69,100)
assert Q(50,41)<Q(5,4)
assert Q(2,5)**4<Q(1,32)
assert Q(999,1000)*Q(2,5)>Q(399,1000)
assert (1-Q(69,100)/Q(421,500))/Q(399,1000)<Q(1,2)
assert Q(91,141)*Q(511,512)>Q(3,5)
print('11 exact rational certificates for arbitrary-Laplace obstruction PASS')
