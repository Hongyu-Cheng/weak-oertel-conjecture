from fractions import Fraction as F

def overlap(Is,j,t):
    total=F(0)
    for z,(lo,hi) in Is.items():
        zz=2*j-z
        if zz in Is:
            l,r=Is[zz]
            total+=max(F(0),min(hi,2*t-l)-max(lo,2*t-r))
    return total

def maxoverlap(Is):
    vals=[]
    for j,(lo,hi) in Is.items():
        bp={lo,hi}
        for z,I in Is.items():
            zz=2*j-z
            if zz in Is:
                for a in I:
                    for b in Is[zz]:
                        t=(a+b)/2
                        if lo<=t<=hi:bp.add(t)
        vals += [overlap(Is,j,t) for t in bp]
    return max(vals)

for ep in [F(1,1000),F(1,100),F(1,7),F(1,2),F(9,10)]:
    Is={-1:(F(0),F(1)),0:(F(0),F(1)),1:(F(0),ep)}
    assert maxoverlap(Is)==1+2*ep
    assert 1<(2+ep)/2
    assert (1+2*ep)/(2+ep)>F(1,2)
print('PASS: exact breakpoint maxima and nonheavy sharpness family')
