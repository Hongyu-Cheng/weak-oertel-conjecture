"""Fraction certificates for the exact fine/coarse scale obstruction."""
from fractions import Fraction as F

def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def area(vertices):
    return abs(cross(sub(vertices[1],vertices[0]),sub(vertices[2],vertices[0])))/2

for L in range(6,121,3):
    h=F(1,L); eps=h*h
    Q0=[(F(-1),F(0)),(F(1),-eps),(F(1),eps)]
    Q1=[(-h,F(-1)),(h,F(1)),(F(0),2*h)]
    assert area(Q0)==area(Q1)==2*eps
    assert all((u/h).denominator==1 for u,x in Q0+Q1)
    m0=F(0); ca=cb=cc=F(0)
    for i in range(-L,L+1):
        u=i*h; low=-eps*(1+u)/2; high=-low
        m0+=h*(high-low)
        ca+=h*(high-low)*(u<=F(1,3))
        xb=eps*((1+u)/2-F(2,3))
        cb+=h*max(F(0),min(high,xb)-low)
        xc=-xb
        cc+=h*max(F(0),high-max(low,xc))
    assert m0==eps*(2+h)
    assert ca==cb==cc==eps*(F(8,9)+2*h/3)<=eps
    m1=2*h*h
    assert m1==2*eps
    assert m0+m1==eps*(4+h)
    assert eps/(m0+m1)==1/(4+h)>F(1,8)
    assert m1/(m0+m1)==2/(4+h)
    assert (h/2)/(4*eps)==1/(8*h)
    assert (2*h)/(64*eps)==1/(32*h)
    # Exact strict exclusions for the five ambient caps, at all vertices.
    for u,x in Q1:
        lambdas=[(1-u)/2,(1+u)/4-x/(2*eps),(1+u)/4+x/(2*eps)]
        assert all(v-F(1,3)-2/eps<0 for v in lambdas)
    for u,x in Q0:
        t=x-u/h
        assert t-h-(2/h+2)<0
        assert h-t-(2/h+2)<0
    # Fixed x>=0 cap in Q1: negative-vertex edge-product fraction.
    negative=F(1,2)/(1+2*h)
    coarse=(1-negative)/2
    assert coarse==(1+4*h)/(4*(1+2*h))
    # Determinant-normalized component images and persistent fine spacing.
    image=[(u/(2*h),(x-u/h)/(2*h)) for u,x in Q1]
    assert image==[(F(-1,2),F(0)),(F(1,2),F(0)),(F(0),F(1))]
    assert area(image)==F(1,2)
    assert h/(2*h)==F(1,2)

print('PASS: exact hull vertices, areas, fine sums, cap cover, depth, and mesh obstruction.')
