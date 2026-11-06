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

stats=Counter();bad=[];certs=[]
for sign,lo,hi in [(1,s.Integer(0),s.Integer(1)),(-1,s.Integer(-1),s.Integer(0))]:
    lines={s.Integer(-2),s.Integer(2),-e,s.Integer(0),e}
    for z in [-1,1]:
        for r in [1+e*z,h]:
            for val in [0,k*r,r]:lines.add(s.expand((t*(1+k)-val)/z))
    lines=list(lines)
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
                if min(bs)>=0:stats['pass']+=1
                else:
                    stats['bad']+=1
                    bad.append((sign,kl,kr,al,ar,label,poly,min(bs)))
                    if len(bad)<10:print('bad',bad[-1],flush=True)
    print(stats,flush=True)
print('FINAL',stats)
with open('./truncated_triangle_strip_bad.txt','w') as f:
    for bb in bad:f.write(repr(bb)+'\n')
