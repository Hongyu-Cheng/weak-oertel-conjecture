import sympy as s
p,q,r,t=s.symbols('p q r t',positive=True)
v=[p,q,r,t]; signs=[1,1,-1,-1]
P=s.cancel((p**3/((p+r)*(p+t))-q**3/((q+r)*(q+t)))/(p-q))
g=s.Matrix([s.diff(P,z)*sg for z,sg in zip(v,signs)])
H=s.Matrix(4,4,lambda i,j:s.diff(P,v[i],v[j])*signs[i]*signs[j])
sub=dict(zip(v,[1,5,5,8])); P0=P.subs(sub); g0=g.subs(sub); H0=H.subs(sub)
f=sum(g0)/3; b=g0/(3*f); scale=P0/f
u=s.Matrix([g0[1],-g0[0],0,0]); w=s.Matrix([0,0,g0[3],-g0[2]])
Q=s.Matrix([[s.factor(u.dot(H0*u)),s.factor(u.dot(H0*w))],[s.factor(w.dot(H0*u)),s.factor(w.dot(H0*w))]])
print('P',P0,'f',f,'P/f',scale,'b',list(b),'xraw',list(scale*s.ones(4,1)-s.Matrix([1,5,-5,-8])))
print('Q',Q,'det',s.factor(Q.det()))
print('b0-1/3',b[0]-s.Rational(1,3),'1/3-b1',s.Rational(1,3)-b[1])
# More legible tangent pair vectors rescaled independently.
u=s.Matrix([s.factor(b[1]/b[0]),-1,0,0]); w=s.Matrix([0,0,s.factor(b[3]/b[2]),-1]);
Q=s.simplify(s.Matrix([[u.dot(H0*u),u.dot(H0*w)],[w.dot(H0*u),w.dot(H0*w)]]))
print('v1',list(u),'v2',list(w),'Qscaled',Q,'det_scaled',s.factor(Q.det()))
assert scale>5 and b[0]>s.Rational(1,3) and max(b[1:])<s.Rational(1,3)
assert Q[0,0]>0 and Q.det()>0
