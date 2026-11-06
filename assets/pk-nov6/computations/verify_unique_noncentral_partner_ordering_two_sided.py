from fractions import Fraction as F
c=(F(1,10),F(2),F(-1),F(-1))
x,y,z,w=(1/abs(t) for t in c)
l=x+y+z+w
b=((x/(x+z)+x/(x+w)-x/l)/3,
   (y/(y+z)+y/(y+w)-y/l)/3,
   (z/(z+x)+z/(z+y)-z/l)/3,
   (w/(w+x)+w/(w+y)-w/l)/3)
assert b==(F(56,165),F(47,225),F(559,2475),F(559,2475))
assert sum(b)==1
assert sum(ci*bi for ci,bi in zip(c,b))==0
assert b[0]-F(1,3)==F(1,165)
assert F(1,3)-b[1]==F(28,225)
assert F(1,3)-b[2]==F(266,2475)
assert F(1,3)-b[3]==F(266,2475)
assert b[2]-b[1]==F(14,825)
assert b[3]-b[1]==F(14,825)
assert all(t!=0 for t in c)
print('10 exact checks PASS')
