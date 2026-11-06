exec(open('./tetrahedral-cross-pair-classification.py').read().split("print('F'")[0])
subs=s.subresultants(f,g,t)
for v in subs:
 print('degree',s.degree(v,t))
 if s.degree(v,t)==1:
  print('coef',s.factor(v.coeff(t,1)))
  print('constant',s.factor(v.subs(t,0)))
