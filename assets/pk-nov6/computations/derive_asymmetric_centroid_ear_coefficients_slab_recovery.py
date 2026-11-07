import sympy as s
r,z,w=s.symbols('r z w')
X=(r+1)*z/(1+z); Y=(r+1)/(1+z)
k=s.Rational(3,2)*(r+3)
S=[2+r/(X+1),2+r/(Y+1),s.Integer(2)]
Q=[(3*r+6-S[0])/2,(3*r+6-S[1])/2,s.Integer(2)]
M=s.factor(sum(q/v for q,v in zip(Q,S)))
T=sum(q/v**2 for q,v in zip(Q,S));U=s.prod(q/v**2 for q,v in zip(Q,S))
E=s.factor(M*M-k*T);R=s.factor(M*M*E*E-4*k**3*U)
D1=r*z+3*r+2*z+4; D2=3*r*z+r+4*z+2
EP=s.cancel(E*4*D1**2*D2**2/3)
RP=s.cancel(R*64*D1**6*D2**6/(27*r))
def compress(poly,halfdeg):
    # symmetric z polynomial /z^halfdeg expressed in w=z+z^-1-2.
    P=s.Poly(poly,z); out=P.nth(halfdeg)
    C0=s.Integer(2); C1=w+2
    Cs=[C0,C1]
    for j in range(2,halfdeg+1):Cs.append(s.expand((w+2)*Cs[-1]-Cs[-2]))
    for j in range(1,halfdeg+1):
        assert s.expand(P.nth(halfdeg+j)-P.nth(halfdeg-j))==0
        out+=P.nth(halfdeg+j)*Cs[j]
    out=s.expand(out)
    assert s.cancel(z**halfdeg*out.subs(w,(z-1)**2/z)-poly)==0
    return out
for name,poly,n in [('E',EP,2),('R',RP,6)]:
    cp=compress(poly,n);p=s.Poly(cp,r,w)
    print(name,'compressed degrees',p.degree(r),p.degree(w),'terms',len(p.terms()),'negative',sum(1 for m,c in p.terms() if c<0))
    for j in range(p.degree(r)+1):
        row=[p.coeff_monomial(r**j*w**l) for l in range(p.degree(w)+1)]
        print(j, row)
    print()
