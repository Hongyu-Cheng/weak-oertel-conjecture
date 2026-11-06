"""Independent parsing and exact verification of the dimension-uniform dual."""
from submission_text import read_submission
from pathlib import Path
from fractions import Fraction as F
import re, math
src=read_submission('660db01ed45063dd')
rows=[(int(d),int(r)) for d,r in re.findall(r'^\| (\d+) \| (\d+) \|$',src,re.M)]
assert len(rows)==13
checks=1
for d,R in rows:
 J=6*d**(d+1);B=3*(2*d+1)*d**d;N=B-4*(d+1)**d;Z=J+3*(d+1)*d**d+(d+1)**(d+1)
 assert N>0;checks+=1
 assert R==16*(Z*J**d-B**(d+1)-N**(d+1))-J**(d+1)>0;checks+=1
 A=F(d+1,d)**d;L=4*A/3-1
 de=2+F(d+1,d)*(1+A/3)-2*F(2*d+1,2*d)**(d+1)-2*(1-L/(2*d))**(d+1)
 assert de==F(1,8)+F(R,8*J**(d+1))>F(1,8);checks+=1
 assert F(B,J)==F(2*d+1,2*d);checks+=1
 assert F(N,J)==1-L/(2*d);checks+=1
 upper=F(d,d+1)*(F(d+1,d)**(d+1)+2*F(2*d+1,2*d)**(d+1)+2*F(N,J)**(d+1)-2)
 assert 1+4*A/3-upper==F(d,d+1)*de>0;checks+=1
assert 8*15**14>21*14**14;checks+=1
assert F(8,3)+F(1,24)*F(5,4)==F(87,32)<F(33,20)**2;checks+=1
assert sum(F(5,4)**i/math.factorial(i) for i in range(7))==F(2058029,589824)>F(80,23);checks+=1
assert F(15,8)-F(33,20)==F(9,40)>0;checks+=1
print(f'PASS: {checks} exact identities and certificates, including all 13 Appendix A integers')
