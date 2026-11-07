exec(open('./tetrahedral-centroid-symbolic.py').read().split("print('positive")[0])
subs={r:s.Integer(1),t:s.Integer(1),q:(1-p)/(1+3*p)}
for i,l in enumerate([l0,l1,l2,l3]):print('lambda',i,s.factor(l.subs(subs)))
vol=p*(a+b)+q*q/((q+t)*(q+r));mass=3*(a+b)
print('F',s.factor(vol.subs(subs)))
print('S',s.factor(mass.subs(subs)))
print('positivefactor r=s',s.factor((l0-l1).subs({r:1,t:1})))
