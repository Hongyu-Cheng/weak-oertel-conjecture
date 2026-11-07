# Exact actual polygon clipping, not a numerical PSD certificate.
exec(open('./verify_fixed_endpoint_sector_polygon_replacement_slab_recovery.py').read().split('def verify(')[0])
h=F(7,10); A=F(100,89); s=F(1077,890)
K=[(F(0),F(1)),(F(-1),F(1)),(-s,-h),(s+h,-h)]
check(h==F(7,10));check(A==(s+h)/(1+h));check(s+h==F(170,89))
for i in range(4):
 check(cross(sub(K[i],K[i-1]),sub(K[(i+1)%4],K[i]))>0)
 check(cross(K[i],K[(i+1)%4])>0)
k=area(K);check(k==F(62339,17800))
q=[area(clip(K,n)) for n in [(1,0),(0,1),(-1,-1)]]
for x in q:check(x/k==F(1700,3667))
W=[area(sector(K,rays[i],rays[(i+1)%6])) for i in range(6)]
check(W[1]==F(1,2));check(W[0]==A/2);check(W[2]==A/2);check(W[4]==h*h/2)
expected=[(A,F(0)),(F(0),F(1)),(F(-1),F(1)),(-A,F(0)),(F(0),-h),(h,-h)]
for d,p in zip(rays,expected):check(ray_endpoint(K,d)[0]==p)
c=q[0]/k
check(12-(c+3)**2==F(47267,13446889));check(c>F(128,279));check(c-F(128,279)==F(4924,1023093))
check(sum(q)-F(3,4)*max(q)-k==k*F(158,3667))
print(checks,'exact checks PASS')
