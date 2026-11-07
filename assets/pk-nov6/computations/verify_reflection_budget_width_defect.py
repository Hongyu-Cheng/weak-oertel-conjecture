from fractions import Fraction as F
import sympy as s
N,w,b=s.symbols('N w b', positive=True)
x=s.symbols('x', nonnegative=True)
# Integral of the clipped tent in the active-height regime b <= N*w.
area=2*s.integrate(2*N*x,(x,0,b/(2*N)))+b*(w-b/N)
assert s.expand(2*area-(N*w*w-(N*w-b)**2/N))==0
a,c,W=s.symbols('a c W')
assert s.expand(W*W-a*c-((W-(a+c)/2)*(W+(a+c)/2)+(a-c)**2/4))==0
widths=[F(2),F(6),F(10),F(3)]
counts=[];corr=[];defects=[]
for j,wj in enumerate(widths):
    indices=[i for i in range(4)if 0<=2*j-i<4]
    n=len(indices); C=sum(widths[i]*widths[2*j-i]for i in indices)
    counts.append(n);corr.append(C);defects.append(n*wj*wj-C)
    assert max(F(0),n*wj-10)**2<=n*(n*wj*wj-C)
assert counts==[1,3,3,1]
assert corr==[4,76,136,9]
assert defects==[0,32,164,0]
assert F(10)<sum(widths)/2
print('PASS: clipped-tent budget, exact width-defect decomposition, and below-half envelope limitation')
