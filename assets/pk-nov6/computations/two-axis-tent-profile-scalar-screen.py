from fractions import Fraction as F
from random import Random
rng=Random(945284);gam=F(27,64)
for trial in range(300000):
 pars=[];deltas=[];mx=[];my=[]
 for sx,sy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
  a=F(rng.randint(1,20),20);b=F(rng.randint(1,20),20)
  if a+b<=1:dd=F(0);xb=yb=F(0)
  else:dd=(a+b-1)**2/(6*a*b);xb=(2+(1-b)/a)/4;yb=(2+(1-a)/b)/4
  pars.append((sx,sy,a,b));deltas.append(dd);mx.append(sx*dd*xb);my.append(sy*dd*yb)
 M=F(4,3)-sum(deltas);X=-sum(mx);Y=-sum(my);px=(F(2,3)-deltas[0]-deltas[1])/M;py=(F(2,3)-deltas[0]-deltas[2])/M;sx=X/(M*M);sy=Y/(M*M)
 caps=[('x+',px,sx),('x-',1-px,-sx),('y+',py,sy),('y-',1-py,-sy)]
 lo=max([(F(0),'none')]+[((gam-p)/(-s),name) for name,p,s in caps if s<0],key=lambda z:z[0]);up=min([((p-gam)/s,name) for name,p,s in caps if s>0],default=(F(10**20),'none'),key=lambda z:z[0])
 if lo[0]>up[0]:
  rec=(pars,deltas,M,X,Y,caps,lo,up);print('EXACT TWO AXIS TENT FAILURE',trial,rec,flush=True);open('./two-axis-tent-profile-scalar-counter.txt','w').write(repr(rec));break
 if trial%20000==0:print(trial,'no exact two-axis tent obstruction',flush=True)
else:print('300000 exact two-axis tent samples no scalar obstruction',flush=True)
