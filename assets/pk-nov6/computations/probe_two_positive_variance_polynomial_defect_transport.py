from flint import fmpz_mpoly
from functools import reduce
import time
prod=lambda a:reduce(lambda x,y:x*y,a)
m=3;z,*us=fmpz_mpoly.gens(m+1);p=z+1
A=prod(u+1 for u in us);B=prod(p+u for u in us)
SA=reduce(lambda x,y:x+y,(u*(A//(u+1)) for u in us));SB=reduce(lambda x,y:x+y,(u*(B//(p+u)) for u in us))
G=(p**m*A-B)//z
Hp=(p**m*A*SB-G*B)//z
Hq=(p*G*A-B*SA)//z
Hs=[(p**(m+1)*A*(u+1)-B*(p+u))//z for u in us]
C=B+p*G;capvar=C*(A*B-C)
for tag,N in [('omit_p',B*Hq*prod(Hs)-G**(m+1)*capvar),('all',Hp*Hq*prod(Hs)-G**(m+2)*capvar),('omit_u',Hp*Hq*prod(Hs[1:])*(us[0]+1)*(p+us[0])-G**(m+1)*capvar)]:
 co=[int(N.coefficient(i)) for i in range(len(N))]
 print(tag,len(co),min(co),sum(c<0 for c in co),flush=True)
