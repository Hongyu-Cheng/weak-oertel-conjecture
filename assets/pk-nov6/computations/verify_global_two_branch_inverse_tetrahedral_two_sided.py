"""Exact polynomial identities for the globally convex inverse-section description."""
import sympy as s
A,B,G,k,n=s.symbols('A B G k n')
D=1+A+B-G;U=A+B;V=A*B;W=G*D;delta=W-V
Q=3*k*k-2*U*k+V;R=k*Q/(delta-2*k);N=k*k+R
x=k+R/(k-A);y=k+R/(k-B)
z=-k+(k+R)/(G-k);w=-k+(k+R)/(D-k)
F=3*k**5+(-8*U-3*V+3*W-4)*k**4+(4*U*U+2*U*V-2*U*W+4*U+6*V+4*W)*k**3+(-4*U*V-4*U*W+V*V-4*V-W*W)*k**2+(-U*V*V+U*W*W-V*V+4*V*W)*k+V*V*W-V*W*W
checks=0
def zero(e):
 global checks
 assert s.cancel(e)==0
 checks+=1
E1=n*n-(V+k*k)*n+k*k*(V+U-k)-V*k
E2=n*n+(-W-k*k+2*k)*n+k*k*(W-U)
zero(E1-E2+(2*k-delta)*n+k*(k*k+(delta-2*U)*k+V))
zero(x-(A*k-N)/(A-k));zero(y-(B*k-N)/(B-k))
zero(z-(N+(1-G)*k)/(G-k));zero(w-(N+(1-D)*k)/(D-k))
zero(x+y+z+w-1-F/((k-A)*(k-B)*(G-k)*(D-k)*(delta-2*k)))
zero(E2.subs(n,N)-k*F/(delta-2*k)**2)
zero((E1-E2).subs(n,N))
zero(z*w-N-k*F/((G-k)*(D-k)*(delta-2*k)**2))
zero(Q.subs(k,A)-A*(A-B))
f=k*Q
zero(s.diff(f,k).subs(k,A)-A*(5*A-3*B))
zero(s.diff(f,k,2)-(18*k-4*U))
J=k*Q/(k-B)
zero(J-(3*k*k+(B-2*A)*k+B*(B-A)+B*B*(B-A)/(k-B)))
zero(J.subs(k,A)-A*A)
zero(s.diff(J,k).subs(k,A)-(4*A+A*B/(A-B)))
zero(s.diff(J,k,2)-(6-2*B*B*(A-B)/(k-B)**3))
k0=delta/2;ca=A*Q.subs(k,A)/(delta-2*A);c0=k0*Q.subs(k,k0)/(k0-A)
dd=s.symbols("delta_independent")
rr=k*Q/(dd-2*k);kk0=dd/2
caa=A*Q.subs(k,A)/(dd-2*A);cc0=kk0*Q.subs(k,kk0)/(kk0-A)
affine=s.cancel(rr/(k-A)-caa/(k-A)-cc0/(dd-2*k))
zero(s.diff(affine,k,2))
zero(s.diff(z,k)-(-1+(1+s.diff(R,k))/(G-k)+(k+R)/(G-k)**2))
zero(s.diff(w,k)-(-1+(1+s.diff(R,k))/(D-k)+(k+R)/(D-k)**2))
Z=k*k+(delta-2*U)*k+V
J0=4*k**3+(delta-5*U)*k*k+(2*U*U-delta*U)*k+V*(delta-U)
zero((delta-2*k)*(k-A)*(k-B)+Q*(2*k-U)-J0)
zero(N*(x+y-k)/((x-k)*(y-k))-Z*J0/Q**2)
# Four direct normalized reciprocal-coordinate centroid identities.
xx,yy,zz=s.symbols('x y z');ww=1-xx-yy-zz;kk=xx*yy-zz*ww;nn=zz*ww
for old,new in [
(xx/(xx+zz)+xx/(xx+ww)-xx-1,(kk*xx-nn)/(xx-kk)),
(yy/(yy+zz)+yy/(yy+ww)-yy-1,(kk*yy-nn)/(yy-kk)),
(1-zz/(zz+xx)-zz/(zz+yy)+zz,(kk*zz+nn+kk)/(zz+kk)),
(1-ww/(ww+xx)-ww/(ww+yy)+ww,(kk*ww+nn+kk)/(ww+kk))]:zero(old-new)
bs=[s.Rational(56,165),s.Rational(47,225),s.Rational(559,2475),s.Rational(559,2475)]
vals={A:3*bs[0]-1,B:3*bs[1]-1,G:1-3*bs[2]}
poly=13476375*k*k+5322240*k-131908
zero(F.subs(vals)-(625*k-16)*(825*k-266)**2*poly/s.Integer(1910907861328125))
zero((delta/2).subs(vals)-s.Rational(37688,680625))
zero(poly.subs(k,s.Rational(1,55))+30685)
zero(poly.subs(k,s.Rational(16,625))-s.Rational(41166316,3125))
assert s.Rational(1,55)<s.Rational(16,625)<s.Rational(37688,680625)<s.Rational(266,825)
checks+=1
# Rational interior tests supplement, not replace, the strict convexity proof.
forms=[(s.cancel(fn),s.cancel(s.diff(fn,k,2))) for fn in (x,y,z,w)]
for av in [s.Rational(1,100),s.Rational(1,50),s.Rational(1,25)]:
 for bv in [s.Rational(-1,2),s.Rational(-1,5),s.Rational(-1,20),s.Integer(0)]:
  for gv in [s.Rational(1,5),s.Rational(2,5),s.Rational(3,5)]:
   dv=1+av+bv-gv
   if not 0<dv<1:continue
   top=min(gv,dv,(gv*dv-av*bv)/2)
   if top<=av:continue
   kv=(av+top)/2;vv={A:av,B:bv,G:gv,k:kv}
   for fn,second in forms:
    assert fn.subs(vv)>0
    assert second.subs(vv)>0
    checks+=2
print('PASS:',checks,'exact identities, interval checks, and rational convexity calibrations')
