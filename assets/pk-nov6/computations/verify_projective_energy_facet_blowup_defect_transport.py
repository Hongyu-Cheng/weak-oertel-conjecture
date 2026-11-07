from fractions import Fraction as F
import sympy as s
n=0
def ck(q):
    global n
    assert q
    n+=1
b,d=s.symbols('b d',positive=True)
# Log derivative of the scalar prism denominator.
ck(s.simplify(1/b-d/(1-b)-(1-(d+1)*b)/(b*(1-b)))==0)
for dim in range(1,31):
    bs=F(1,dim+1)
    C=F(dim+1,dim)**(dim+1)
    ck(1/(dim*bs*(1-bs)**dim)==C)
    ck((dim+1)*bs==1)
    ck((dim+1)*(1-bs)==dim)
    ck((1-bs)**(-dim-1)/((dim+1)*bs*C)==1)
    ck((1-bs)/(dim*bs)==1)
    # Simplex facet formula, with arbitrary exact positive facet coordinates.
    bary=[F(2*j,dim*(dim+1)) for j in range(1,dim+1)]
    facprod=s.prod(bary)
    EF=dim**dim*facprod
    limit=F((dim+1)**(dim+1),dim)*facprod
    ck(limit==C*EF)
    for z in [F(1,5),F(1,2),F(4,5)]:
        if z==bs: continue
        ck(z*(1-z)**dim<bs*(1-bs)**dim)
H,delta=s.symbols('H delta',positive=True)
E=4*delta*(H-delta)/H
ck(s.limit(E/delta,delta,0,dir='+')==4)
ck(s.limit(s.diff(E,delta),delta,0,dir='+')==4)
print(f'{n} exact checks PASS')
