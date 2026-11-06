from fractions import Fraction as F
checks=0
def ck(p,msg):
 global checks
 assert p,msg
 checks+=1
ck(F(1,18)>F(1,25),'standard triangle inner radius squared')
ck(F(32,9)<4,'shifted square outer radius squared')
ck(16*F(1,2**20)==F(1,2**16),'thin support ratio to angular bound')
ck(F(720,7*65536)<F(2,5),'exact A cap cover radius bound')
ck(F(259200,49*65536)==F(2025,25088),'planar strip constant')
ck(F(2025,25088)<F(1,9),'strict planar contradiction')
ck(F(9,2)-F(17,4)==F(1,4),'critical mass forces E>=Q/4')
ck(F(1,4)*F(4,9)==F(1,9),'B comparison forces E>=b/9')
ck(F(9,4)*F(4,7)==F(9,7),'planar bad target bounds middle volume')
for d in range(2,31):
 g=F(d,d+1)**d
 ck(F(1,3)<g<F(1,2),'positive angular loss coefficient')
 ck(F(1,1)/g-2>0,'mass comparison sign')
 # Treat positive r and omega as rational placeholders; all cancellations
 # are algebraic and independent of their actual geometric values.
 r=F(1,d+2);omega=F(d+1,3);b=F(2)**d;k=3*b
 L=F(d)*2**d*k/(omega*r**(d-1))
 Cd=F(3*d)*2**d/(omega*r**(d-1))
 ck(L==Cd*b,'all-d compatible radius after k<=3b')
 cone_distance=F(d)*2**(d-1)*k/(omega*r**(d-1))
 ck(cone_distance==L/2,'exact cone factor')
 eps=min(r/(Cd*2**d),(1-2*g)/(2*omega*Cd**d*2**(d*(d-1))))
 ck(eps>0,'explicit dimension-only threshold positive')
 ck(eps*L<=r<2*r,'normalized A pair cover condition')
 ck(omega*eps*L**d/b<=F(1,2)*(1-2*g)<1-2*g,'normalized strict strip condition')
print(f'{checks} exact rational checks passed.')
