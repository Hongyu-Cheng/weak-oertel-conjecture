import sympy as s
E=[s.eye(4)[:,i] for i in range(4)]
def cap(c):
 pos=[i for i in range(4) if c[i]>0];neg=[i for i in range(4) if c[i]<0]
 assert len(pos)==len(neg)==2
 i,j=pos;k,l=neg
 def v(a,b):return (-c[b]*E[a]+c[a]*E[b])/(c[a]-c[b])
 A,B,C,D=v(i,k),v(i,l),v(j,l),v(j,k)
 ts=[[E[i],A,B,C],[E[i],A,C,D],[E[i],E[j],C,D]]
 prob=0;M=s.zeros(4);M2=s.zeros(4)
 for verts in ts:
  mat=s.Matrix.hstack(*verts);vol=abs(mat.det());sm=sum(verts,s.zeros(4,1))
  prob+=vol;M2+=vol*(sum((u*u.T for u in verts),s.zeros(4))+sm*sm.T)/20
 p,q=c[i],c[j];r,w=-c[k],-c[l]
 f=(p*q*(r+w)+r*w*(p+q))/((p+r)*(p+w)*(q+r)*(q+w))
 return prob,f,M2
raws=[s.Matrix([7,12,-28,-28]),s.Matrix([12,7,-28,-28]),s.Matrix([-19,-19,56,56])]
data=[cap(c) for c in raws];T=sum(P/f for P,f,M in data);W=sum((M/f for P,f,M in data),s.zeros(4))/T
uniform=(s.eye(4)+s.ones(4))/20
print('P/f/T',[(P,f) for P,f,M in data],T)
print('difference matrix',W-uniform)
for v in [s.Matrix([1,-1,0,0]),s.Matrix([0,0,1,-1]),s.Matrix([1,1,-1,-1])]:print('v',list(v),'gap',s.factor((v.T*(W-uniform)*v)[0]))
v=s.Matrix([1,-1,0,0])
assert T==s.Rational(3772,19)
assert (v.T*(W-uniform)*v)[0]==-s.Rational(24871,106087500)
y=s.symbols('y')
hinge=s.integrate((y-s.Rational(4,5))*6*y*(1-y),(y,s.Rational(4,5),1))
assert s.factor((200/T-1)*hinge)==s.Rational(63,1178750)
rows=[(P/f*s.ones(4,1)-c)/T for c,(P,f,M) in zip(raws,data)]
assert sum(rows,s.zeros(4,1))==s.ones(4,1)
assert all(v>0 for row in rows for v in row)
print('Exact moments, both convex-order obstructions, and positive stochastic reconstruction PASS')
