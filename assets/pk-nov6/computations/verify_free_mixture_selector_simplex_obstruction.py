"""Exact rational checks for the five-dimensional auxiliary obstruction."""
from fractions import Fraction as F

d=5
R=F(9,2); r=F(497,3000); ell=F(11,12)-R*r
T=1-r-ell
assert T==F(3979,6000)
p=[F(0),F(11,12),F(0),F(0),F(0)]
base=[r,ell,F(0),F(0),F(0)]
vertices=[p,base]
for coordinate in range(1,5):
    v=base.copy();v[coordinate]+=T;vertices.append(v)
for v in vertices:
    assert min(v)>=0 and sum(v)<=1
    assert v[0]<=r
    assert R*v[0]+v[1]>=F(11,12)

matrix=[[vertices[j+1][i]-p[i] for j in range(5)] for i in range(5)]
det=F(1)
for i in range(5):
    j=next(j for j in range(i,5) if matrix[j][i])
    if i!=j:
        matrix[i],matrix[j]=matrix[j],matrix[i];det=-det
    pivot=matrix[i][i];det*=pivot
    for j in range(i+1,5):
        t=matrix[j][i]/pivot
        for k in range(i,5):matrix[j][k]-=t*matrix[i][k]
m=abs(det)
assert m==r*T**4==F(124581095445185057,3888000000000000000)
assert m-F(1,32)==F(3081095445185057,3888000000000000000)>0
assert F(11,20)**5-m==F(71095869554814943,3888000000000000000)>0
# The preceding bounds give 0<a=(2*m**(1/5)-1)**5<10^-5 exactly.
a_bound=(2*F(11,20)-1)**5
assert a_bound==F(1,100000)<F(1,100)
alpha=F(2,25);beta=F(17,50)
assert alpha*a_bound<F(1,1000)
assert R*alpha>beta
assert F(1,6)+beta*a_bound<2
gamma=F(5,6)**5
first=F(12,25)*(1+F(12,125)*F(1,100))**4
assert first==F(1148810043113472,2384185791015625)<F(1,2)
linear=gamma*(F(1,2)+F(51,25))-1
assert linear==F(323,15552)>0
quadratic=gamma*10*F(51,125)**2*F(1,100)
assert quadratic<linear
print('PASS: simplex geometry, rational root bounds, wedge coverage, and both strict cap budgets')
print('relative midpoint simplex volume:',m)
print('second-cap linear slack minus maximal quadratic remainder:',linear-quadratic)
