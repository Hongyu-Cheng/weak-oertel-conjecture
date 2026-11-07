from fractions import Fraction as F
z=(-1,0,1,2)
m=tuple(F(i,5) for i in range(1,5))
assert sum(m)==2 and sum(i*a for i,a in zip(z,m))==2
assert sum(a-a*a/2 for a in m)==F(7,5)
assert sum(a*a/2 for a in m)==F(3,5)
# The pointwise affine-margin exchange in the note certifies both global optima.
def upper_mass(a,b):
    return sum(max(F(0),min(F(1),1-(b-a*i))) for i in z)
assert upper_mass(F(3,10),F(1))==F(9,10)
assert F(7,10)+F(3,10)==1
assert F(9,10)/4==F(9,40)<F(1,4)
assert upper_mass(F(1,2),F(1))==F(3,2)
assert F(3,2)/4==F(3,8)>F(1,4)
# Reflections preserve the actual fiber set and generate all four candidates.
p=(1,F(7,10))
points={(p[0],p[1]),(p[0],1-p[1]),(1-p[0],p[1]),(1-p[0],1-p[1])}
assert points=={(1,F(7,10)),(0,F(3,10)),(1,F(3,10)),(0,F(7,10))}
assert set(1-i for i in z)==set(z)
print('PASS: exact exposed sources and four failed adjacent-partition centroids')
