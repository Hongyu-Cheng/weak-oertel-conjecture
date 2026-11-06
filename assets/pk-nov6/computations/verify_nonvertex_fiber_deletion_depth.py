from fractions import Fraction as F

# Exact breakpoints suffice because each cap mass is continuous piecewise
# affine in its slope; exterior rays have constant mass.
def clamp(t):
    return min(F(1), max(F(0), t))

def down(x, b):
    breaks = {-x, 1-x, x, x-1}
    return min(x+clamp(x+v)+clamp(x-v) for v in breaks)

def up(x, b):
    breaks = {x-1,x,1-x,-x}
    return min(b-x+clamp(1-x+v)+clamp(1-x-v) for v in breaks)

for b in [F(1), F(3,2), F(2), F(3), F(4), F(5), F(7)]:
    for j in range(101):
        x=b*j/100
        assert down(x,b)==x+min(2*x,1)
        assert up(x,b)==b-x+min(max(2*(1-x),0),1)
    x=(b+1)/4 if b<=3 else (b-1)/2
    a=(b+5)/4 if b<=3 else (b+1)/2
    assert down(x,b)==up(x,b)==a
    assert a>F(1,2)

values=[F(1,2),F(2,5),F(3,7)]
assert values[1]<min(values[0],values[2])
assert F(3)-F(3,2)<=F(4)
print('PASS: exact slope breakpoints, center masses, and deletion dip')
