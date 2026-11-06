from fractions import Fraction as F
import sympy as sp
b,d,L=F(16,25),F(29,50),F(3,4)
a,c=F(217,325),F(3823,5650)
alpha=[F(52,125),F(203,1000),F(381,1000)]
A,B=F(44051,93175),F(795184,835175)
l1,l2=F(169,217),F(12769,15292)
assert sum(alpha)==1 and min(alpha)>0
assert alpha[1]/A+alpha[2]/a==1
assert alpha[0]/B+alpha[2]/c==1
assert alpha[0]/b+alpha[1]/d==1
assert l1*a+L*b==1
assert l1*a*a+L*(2*b-b*b)==1
assert l2*c+L*d==1
assert l2*c*c+L*(2*d-d*d)==1
sig=l1*A+l2*B-1
m=(l1*A*A+l2*(2*B-B*B)-1)/(2*sig)
assert sig==F(20323200,124507889)>0
assert m==F(4993093096,227226897425)
assert 0<m<1-B<A<1
assert l1<1<1+sig
assert l1+l2+L>F(9,4)
assert l1*A*a+l2*B*c+L*b*d==1+sig*alpha[2]
M=sp.Matrix([[1,1-1/A,1-1/a],[1-1/B,1,1-1/c],[1-1/b,1-1/d,1]])
ker=M.T.nullspace()
assert len(ker)==1 and all(x>0 for x in ker[0])
assert alpha[0]/b==F(13,20)
# Cap3's relative midpoint displacement is 3/10; this exceeds 2-sqrt(3).
assert F(17,10)**2<3
print('PASS: complete central affine stress, positive cap circuit, exact profile loss')
