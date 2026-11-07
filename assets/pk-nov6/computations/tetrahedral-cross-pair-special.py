exec(open('./tetrahedral-cross-pair-classification.py').read().split("print('F'")[0])
for pv in [s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]:
 res=((3*p**4+18*p**3+26*p**2+2*p-1)*q*q+2*p*(p-1)*(3*p*p+4*p+5)*q+2*p*p*(p-1)**2).subs(p,pv)
 for qv in s.nroots(res):
  if abs(s.im(qv))>1e-10 or s.re(qv)<=0:continue
  for tv in s.nroots(f.subs({p:pv,q:qv})):
   if abs(s.im(tv))>1e-10 or s.re(tv)<=0:continue
   if abs(complex(g.subs({p:pv,q:qv,t:tv})))>1e-5:continue
   vals=[float(v.subs({p:pv,q:qv,r:1,t:tv})) for v in [l0,l1,l2,l3]]
   print('case',pv,float(qv),float(tv),vals)
