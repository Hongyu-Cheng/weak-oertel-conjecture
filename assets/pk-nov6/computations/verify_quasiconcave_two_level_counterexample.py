from fractions import Fraction as F
e=F(1,1000);a=F(1,3)-e/16;b=F(1,3)-41*e/125
assert 0<a<a+b<1 and b>F(8,25) and F(2,5)<F(5,4)*(a+b)<1
U=[(1-a)**2+e*(1-F(5,4)*a)**2,(1-b)**2,(a+b)**2+e*(1-F(5,3)*(1-F(5,4)*(a+b))**2)]
gaps=[F(3397759,163840000000),F(984871,140625000000),F(159342264433,13824000000000000)]
assert [F(1001,2250)-u for u in U]==gaps and min(gaps)>0
assert F(1,2)+F(16,125)/256==F(1001,2000)
print('PASS: exact nested-triangle measure, cap branches, and three strictly positive rational depth deficits.')
