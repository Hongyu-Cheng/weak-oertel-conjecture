"""Exact arithmetic check of the proved trapezoid lemma's algebra."""
from fractions import Fraction as F

def affine_integral(slope,intercept,a,b):
    return slope*(b*b-a*a)/2+intercept*(b-a)

count=0
for denominator in range(2,24):
    for numerator in range(denominator):
        c=F(numerator,denominator);B=1-c
        for md in range(1,13):
            for mn in range(1,40):
                m=F(mn,md);L=B/(m+1);t=c+L;r=t+L/B
                val=-m*L*L
                if r<=1:
                    val+=affine_integral(m+3,-m*c-3,t,r)
                    val+=affine_integral(2,-1,r,F(1))
                    formula=(2*c*B*m-1)/(2*(m+1))
                else:
                    val+=affine_integral(m+3,-m*c-3,t,F(1))
                    formula=B*B*m*(m-2)/(2*(m+1))
                assert val==formula
                V=m*c*c/2 if m*c<=1 else c-1/(2*m)
                assert V>=max(0,val)
                if m>=1/B:
                    if m*c<=1:
                        assert 2*(m+1)*(V-val)==(m*c-1)**2+3*m*c*c
                    else:
                        assert 2*m*(m+1)*(V-val)==2*(m*c)**2+2*m*c-1
                count+=1
print('PASS:',count,'exact rational parameter checks; proof is in the companion note.')
