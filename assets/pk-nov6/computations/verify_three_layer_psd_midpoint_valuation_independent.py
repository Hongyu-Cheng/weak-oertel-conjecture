from fractions import Fraction as F
nu=[(F(1),F(0),F(3,8))]
eta=[(F(1,2),F(-1),F(0)),(F(1,4),F(1),F(1,2)),(F(1,4),F(1),F(1))]
mid=[(F(1,2),F(0),F(1,4)),(F(1,2),F(0),F(1,2))]
pairs=[(F(1,2),F(0),F(1,2)),(F(1,2),F(0),F(1))]
def moment(law,a,b):return sum(w*z**a*x**b for w,z,x in law)
def primitive_power(a,b,k):return (b**(k+1)-a**(k+1))/F(k+1)
def k_moment(k):
 l=F(1,4);m=F(3,8);r=F(1,2)
 return (primitive_power(l,m,k+1)-l*primitive_power(l,m,k)+r*primitive_power(m,r,k)-primitive_power(m,r,k+1))/2
assert k_moment(0)==F(1,128)
checks=0
for a in range(7):
 for b in range(9):
  lhs=moment(nu,a,b)-moment(eta,a,b)
  psd=-b*(b-1)*k_moment(b-2) if a==0 and b>=2 else F(0)
  jensen=sum(w*(F(0)**a*((l+r)/2)**b-(F(-1)**a*l**b+F(1)**a*r**b)/2) for w,l,r in pairs)
  assert lhs==psd+jensen,(a,b,lhs,psd,jensen)
  checks+=1
assert moment(eta,2,0)-moment(nu,2,0)==1
assert moment(mid,0,2)-moment(nu,0,2)==2*k_moment(0)==F(1,64)
assert sum(w*(r-l)**2/4 for w,l,r in pairs)==F(5,32)
assert moment(eta,0,2)-moment(nu,0,2)==F(11,64)
print(f'PASS: {checks} exact mixed polynomial distribution tests and all variance coefficients.')
