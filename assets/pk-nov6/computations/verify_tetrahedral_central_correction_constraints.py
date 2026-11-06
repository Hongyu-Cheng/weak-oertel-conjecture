from fractions import Fraction as F

def check(ints):
 x,y,z,w=map(F,ints);S=x+y+z+w;P=x+y;R=z+w;a=x*y;b=z*w
 D=(x+z)*(x+w)*(y+z)*(y+w);FN=b*(P*S-a+b);sn=3*S*(b*P-a*R)
 Ds=[(x+z)*(x+w),(y+z)*(y+w),(x+z)*(y+z),(x+w)*(y+w)]
 Ns=[x*(S*(2*x+z+w)-Ds[0]),y*(S*(2*y+z+w)-Ds[1]),z*(S*(x+y+2*z)-Ds[2]),w*(S*(x+y+2*w)-Ds[3])]
 lam=[Ns[i]/(3*S*Ds[i])for i in range(4)]
 central=[b*(S+x)-x*x*y,b*(S+y)-x*y*y,a*(S+z)-z*z*w,a*(S+w)-z*w*w]
 assert all((S*Ds[i]-Ns[i])==central[i]for i in range(4))
 j,k=sorted(range(4),key=lambda i:lam[i])[1:3]
 B=12*Ns[j]*Ns[k]-3*S*(Ds[j]*Ns[k]+Ds[k]*Ns[j])
 if B==0:return
 c=4*Ns[j]*Ns[k]/B;corrected=FN/D-c*sn/(4*D)
 assert c==4/(12-1/lam[j]-1/lam[k])
 target=(64*FN-27*D)*B-192*S*(b*P-a*R)*Ns[j]*Ns[k]
 assert target/(64*D*B)==corrected-F(27,64)
 upper=(37*D-64*FN)*B+192*S*(b*P-a*R)*Ns[j]*Ns[k]
 assert upper/(64*D*B)==F(37,64)-corrected
 return lam,c,corrected
for ints in [(1,2,3,4),(1,1,1,1),(3,9,4,4),(12,7,3,3)]:check(ints)
lam,c,corr=check((16,29,5,8))
assert lam==[F(78,203),F(715,1887),F(3095,31059),F(1325,9657)]
assert c==F(378950,196347)
assert corr==F(172480645,247004526)>F(37,64)
print('PASS: exact rational reductions and the outside-central-domain obstruction; no central positivity theorem claimed.')
