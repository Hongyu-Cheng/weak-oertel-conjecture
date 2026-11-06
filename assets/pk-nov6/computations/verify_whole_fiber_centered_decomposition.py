from fractions import Fraction as F
vol=[F(1),F(3,2),F(1)]
mean=[F(1,2),F(3,4),F(1,2)]
M=sum(vol)
gx=sum(a*x for a,x in zip(vol,mean))/M
assert M==F(7,2) and gx==F(17,28)
assert sum(F(i)*a for i,a in enumerate(vol))/M==1
assert mean[0]-gx==F(-3,28)
assert mean[1]-gx==F(1,7)
assert -2*(mean[0]-gx)/(mean[1]-gx)==F(3,2)
assert M/max(vol)==F(7,3)>2
assert M*M/sum(a*a for a in vol)==F(49,17)>2
print('Whole-fiber centered decomposition obstruction verified exactly.')
