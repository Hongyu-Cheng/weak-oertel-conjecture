from fractions import Fraction as F

widths=[F(1),F(2),F(3)]
assert sum(widths)==6
assert sum(i*w for i,w in enumerate(widths))==8
mD,mE=F(4),F(2)
assert mD+mE==6 and mD+2*mE==8
cases=[[(F(0),F(1)),(F(0),F(2)),(F(0),F(1))],
       [(F(0),F(1)),(F(0),F(2)),(F(2),F(3))]]
for k,intervals in enumerate(cases):
    assert sum(b-a for a,b in intervals)==mD
    assert sum(i*(b-a) for i,(a,b) in enumerate(intervals))==mD
    mean=sum((b*b-a*a)/2 for a,b in intervals)/mD
    assert mean==[F(3,4),F(5,4)][k]
    lengths=[]
    for z,(a,b) in enumerate(intervals):
        if k==0:
            threshold=mean-4*(z-1)
            lengths.append(max(F(0),min(b,threshold)-a))
        else:
            threshold=mean+4*(z-1)
            lengths.append(max(F(0),b-max(a,threshold)))
    assert lengths==[F(1),F(3,4),F(0)]
    assert sum(lengths)==F(7,4)<mD/2
assert F(7,4)/4==F(7,16)<F(1,2)
assert F(3,2)<F(7,4)<F(2)
assert F(2,6)==F(1,3)>F(1,4)
print('PASS: forced partition moments, exact bad caps, and original-depth constants')
