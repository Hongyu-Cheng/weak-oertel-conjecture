exec(open('./verify_fixed_endpoint_sector_polygon_replacement_slab_recovery.py').read().split('def verify(')[0])
rng=Random(581229)
for it in range(120):
 x,u,v=[F(rng.randint(1,20),rng.randint(1,10)) for _ in range(3)];d=F(0) if it%12==0 else F(rng.randint(1,20),rng.randint(1,10));L=x+2*v
 K=hull([(2*v,-v),(-x,x+u),(-x,-u),(-x-d,(x+d)/2)])
 check(len(K)==(3 if d==0 else 4));k=area(K);check(k==(L+d)*(x+2*u)/2)
 sig1=2*v*(x+2*u)/L;sig=(x+2*u)*(v/(x+u+v)+(x+d)/(x+d+2*u))
 Q1=v*sig1;Qc=L*(x+u)**2/(2*(x+u+v))+d*(x+2*u)/2-d*u*u/(x+d+2*u)
 for n,Q in zip([(1,0),(0,1),(-1,-1)],[Q1,Qc,Qc]):check(area(clip(K,n))==Q)
 pp=[ray_endpoint(K,e)[0] for e in rays]
 check(pp[1][1]-pp[4][1]==sig1);check(pp[0][0]-pp[3][0]==sig);check(pp[5][0]-pp[2][0]==sig)
 H2=2*Qc/sig;H=v+H2;D=d*u+2*d*v+d*x+2*u*v+u*x+2*v*x+x*x
 N=d*d*u+d*d*v+d*d*x+d*u*u+2*d*u*v+3*d*u*x+3*d*v*x+2*d*x*x+2*u*u*v+u*u*x+4*u*v*x+2*u*x*x+2*v*x*x+x**3
 check(H2==N/D)
 P=d*d*u+d*d*x+d*u*u+3*d*u*x+2*d*x*x+2*u*u*v+u*u*x+2*u*x*x+x**3
 deficit=2*H*H-(L+d/2)*H-2*k*H2/sig
 check(deficit==d*(d+2*v+x)*(u+v+x)*P/(2*D*D));check(deficit>=0);check(d==0 or deficit>0)
 check((L+d/2)**2-L*(L+d)==d*d/4)
print(checks,'exact actual-polygon and deficit checks PASS')
