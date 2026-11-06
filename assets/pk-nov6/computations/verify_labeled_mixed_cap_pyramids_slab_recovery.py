"""Exact calibrations for the all-status labeled cone proof."""
from fractions import Fraction as F
checks=0
def chk(x):
    global checks
    assert x
    checks+=1

def record(lo,hi,scale,tau,gamma=F(1)):
    # x1-cap, other d-1 side lengths one; section T includes 1/scale.
    t=tau/scale
    if t<lo: return hi-lo,F(0),'full'
    if t==lo: return hi-lo,gamma/scale,'inside'
    if lo<t<hi: return hi-t,1/scale,'proper'
    if t==hi: return F(0),gamma/scale,'outside'
    return F(0),F(0),'empty'

statuses=set()
for d in range(1,10):
  for scale in (F(1,3),F(1),F(7,2)):
    for a in (F(-2),F(-1,2),F(0),F(1,2),F(2)):
      for c in (F(-1),F(0),F(1)):
        for gamma in (F(0),F(1,3),F(1)):
          p=F(1,5); y=F(-2,7)
          Q=G=Hs=T=B=F(0)
          for z in (-1,0,1):
            lo=F(-1,2);hi=F(1,2);tau=c-a*z
            q,t,status=record(lo,hi,scale,tau,gamma)
            statuses.add(status)
            g=(scale*hi-tau)*t
            chk(g>=0);chk(d*q-g>=0)
            Q+=q;G+=g;Hs+=scale*hi*t;T+=t;B+=t*(z-p)
          delta=c-a*p-scale*y
          chk(G==Hs+a*B-delta*T-y*scale*T)
          chk(d*Q==G+sum(d*record(F(-1,2),F(1,2),scale,c-a*z,gamma)[0]-(scale/2-c+a*z)*record(F(-1,2),F(1,2),scale,c-a*z,gamma)[1] for z in (-1,0,1)))
chk(statuses=={'proper','inside','outside','full','empty'})
# Exact supporting family with actual opposite critical caps.
for d in range(1,21):
  for num in range(21):
    gamma=F(num,20)
    Q=G=T=B=X=F(0)
    for z in (-1,0,1):
      tau=-F(z,2)
      q,t,_=record(F(-1,2),F(1,2),F(1),tau,gamma)
      Q+=q;T+=t;B+=z*t;X+=tau*t;G+=(F(1,2)-tau)*t
    chk(Q==F(3,2));chk(T==1+2*gamma)
    chk(B==X==0);chk(G==F(1,2)+gamma)
    chk(d*Q-G==F(3*d,2)-F(1,2)-gamma)
# Compatible unequal cube widths; strict unfavorable support deficit.
for d in range(1,21):
  hs=[F(1,2),F(1),F(1,2)]
  Q=sum(hs);Ts=F(3);cone=sum(hs);own=Ts*hs[1]
  slack=own-cone;deficit=d*Q-cone
  chk(Q==2);chk(slack==1);chk(deficit==2*d-2)
  chk(d*Q==own-slack+deficit)
# Proper-to-supporting limiting record: all old sections are fully counted.
for m in range(3,101):
  a=F(1,2)-F(1,m)
  rows=[record(F(-1,2),F(1,2),F(1),-a*z) for z in (-1,0,1)]
  chk(all(status=='proper' for q,t,status in rows))
  chk(sum(q for q,t,status in rows)==F(3,2))
  chk(sum(t for q,t,status in rows)==3)
  chk(sum((F(1,2)+a*z)*rows[z+1][1] for z in (-1,0,1))==F(3,2))
# Pure-base exact mass is entirely remainder.
for d in range(1,21):
  vols=[F(1,3),F(5,2),F(7,4)]
  chk(d*sum(vols[1:])==sum(d*v for v in vols[1:]))
print(f'PASS: {checks} exact checks')
