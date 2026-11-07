"""Exact rational all-direction certificate for a globally critical cap-gluing counterexample.

See globally-critical-truncated-triangle-cap-gluing-counterexample-slab-recovery.md.
No floating-point calculation occurs. The finite strip partition is exhaustive,
and tensor Bernstein coefficients certify each rational polynomial inequality.
"""
import sympy as s
from fractions import Fraction as F
from math import comb
from collections import Counter
k,a,u,v=s.symbols('k a u v')
t=s.Rational(100,291);h=s.Rational(20,97);e=s.Rational(1,100)
delta=2*t*(1-2*t);M=(3+2*e**2-3*h**2)/2

def tail(r,c,sgn,km,am):
    val=s.expand(c).subs({k:km,a:am}); q=km*r
    if sgn>0:
        if val<=0:return r**2/2
        if val<q:return r**2/2-c**2/(2*k)
        if val<r:return (r-c)**2/(2*(1-k))
        return s.Integer(0)
    if val<q:return r**2/2
    if val<0:return r**2/2-(c-k*r)**2/(2*(-k)*(1-k))
    if val<r:return (r-c)**2/(2*(1-k))
    return s.Integer(0)

def bernstein(poly):
    po=s.Poly(poly,v,u);n=po.degree(v);m=po.degree(u)
    if po.is_zero:return [s.Integer(0)]
    cs={(i,j):c for (i,j),c in po.terms()}
    return [sum(cs.get((p,q),0)*s.Rational(comb(i,p),comb(n,p))*s.Rational(comb(j,q),comb(m,q)) for p in range(i+1) for q in range(j+1)) for i in range(n+1) for j in range(m+1)]

stats=Counter();bad=[];certs=[]; rows=[]; full=[]
for sign,lo,hi in [(1,s.Integer(0),s.Integer(1)),(-1,s.Integer(-1),s.Integer(0))]:
    lines={s.Integer(-2),s.Integer(2),-e,s.Integer(0),e}
    for z in [-1,1]:
        for r in [1+e*z,h]:
            for val in [0,k*r,r]:lines.add(s.expand((t*(1+k)-val)/z))
    lines=list(lines)
    assert all(-2 <= line.subs(k,q) <= 2 for line in lines for q in [lo,hi])
    points={lo,hi}
    if sign>0:points.add(3-1/t)
    for i,line in enumerate(lines):
        for ll in lines[:i]:
            dif=s.Poly(line-ll,k)
            if dif.degree()==1:
                rt=-dif.nth(0)/dif.nth(1)
                if lo<rt<hi:points.add(rt)
    for r in [s.Integer(1),h]:
        for val in [0,k*r,r]:
            dif=s.Poly(t*(1+k)-val,k)
            if dif.degree()==1:
                rt=-dif.nth(0)/dif.nth(1)
                if lo<rt<hi:points.add(rt)
    points=sorted(points)
    print('sign',sign,'kintervals',len(points)-1,'lines',len(lines),flush=True)
    for kl,kr in zip(points,points[1:]):
        km=(kl+kr)/2
        row_min={}
        order=sorted(lines,key=lambda x:x.subs(k,km))
        for al,ar in zip(order,order[1:]):
            if al.subs(k,km)<-2 or ar.subs(k,km)>2:continue
            if al.subs(k,km)==ar.subs(k,km):continue
            am=(al.subs(k,km)+ar.subs(k,km))/2
            cap=s.Integer(0)
            for z in [-1,0,1]:
                c=t*(1+k)-a*z
                cap+=tail(1+e*z,c,sign,km,am)-tail(h,c,sign,km,am)
            denominator=2*sign*k*(1-k)
            for label,expr in [('lower',cap-3*delta),('upper',M-3*delta-cap)]:
                poly=s.cancel(expr*denominator)
                assert s.denom(poly)==1
                poly=s.expand(poly)
                mapped=s.Poly(poly.subs(a,al+(ar-al)*u).subs(k,kl+(kr-kl)*v).expand(),v,u).as_expr()
                bs=bernstein(mapped)
                stats['total']+=1
                row_min[label]=min(row_min.get(label,min(bs)),min(bs))
                full.append({'sign':sign,'k_left':str(kl),'k_right':str(kr),'alpha_left':str(al),'alpha_right':str(ar),'bound':label,'numerator':str(poly),'bernstein':list(map(str,bs))})
                if min(bs)>=0:stats['pass']+=1
                else:
                    stats['bad']+=1
                    bad.append((sign,kl,kr,al,ar,label,poly,min(bs)))
                    if len(bad)<10:print('bad',bad[-1],flush=True)
        rows.append((sign,kl,kr,row_min['lower'],row_min['upper']))
    print(stats,flush=True)
print('FINAL',stats)
assert not bad
assert stats['total']==672 and stats['pass']==672
import json
with open('./truncated_triangle_exact_bernstein_certificate.json','w') as f:
    json.dump(full,f,indent=2)
with open('./truncated_triangle_strip_minima_table.md','w') as f:
    f.write('| sign | k left | k right | minimum lower coefficient | minimum upper coefficient |\n|---|---|---|---|---|\n')
    for row in rows:f.write('| '+' | '.join(map(str,row))+' |\n')
assert h*h==12*t*t-4*t
assert 0<h<2*t<1-e and 4*t-1-e>h and 1-2*t-e>0
volumes=[((1+e*z)**2-h*h)/2 for z in [-1,0,1]]
assert max(volumes)<3*delta and max(volumes)<sum(volumes)/2
assert volumes[0]+volumes[1]>3*delta
assert volumes[1]+volumes[2]>3*delta
assert s.expand(3*(1-t*(1+k))**2+2*(a+e)**2-6*(1-k)*delta-3*t*t*(k-(3-1/t))**2-2*(a+e)**2)==0
assert s.expand(3*(t*(1+k))**2+2*a*a-12*t*t*k-3*t*t*(1-k)**2-2*a*a)==0
print('PASS: 672 exact polynomial certificates and geometric, equality, and global-depth checks.')
