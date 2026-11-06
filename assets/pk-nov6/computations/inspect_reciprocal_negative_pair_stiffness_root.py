import sympy as s
p,q=s.symbols('p q',positive=True)
su=p+q;pr=p*q
N=su**2+4*su*pr+6*pr**2-pr-pr**3
R=3*(su+2*pr)*(1+su+pr)**2/(2*N)
H=s.hessian(R,(p,q))
for name,val in [('Hpp',H[0,0]),('det',H.det())]:
    fac=s.factor(val)
    num,den=fac.as_numer_denom()
    print(name,'factor',fac,flush=True)
    poly=s.Poly(num,p,q)
    # positive simplex parametrization p=u/(1+u+v), q=v/(1+u+v)
    u,v=s.symbols('u v',nonnegative=True); degree=poly.total_degree()
    out=s.Poly(s.expand(sum(c*u**i*v**j*(1+u+v)**(degree-i-j) for (i,j),c in poly.terms())),u,v)
    coeff=out.coeffs()
    print(name,'degree',degree,'terms',len(coeff),'signcounts',sum(1 for c in coeff if c>0),sum(1 for c in coeff if c<0),flush=True)
