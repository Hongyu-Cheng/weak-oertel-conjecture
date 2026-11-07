import random

def interval_min(a,b,l1,l2,t):
    grid=sorted(set([0.,1.,a,1-b,t]))
    best=1e30
    for x in grid:
        for y in grid:
            if x<=t<=y and y>x+1e-12:
                val=(l1*max(0,min(y,a)-max(x,0))
                     +l2*max(0,min(y,1)-max(x,1-b)))/(y-x)
                best=min(best,val)
    return best

random.seed(1797)
record=(-1e99,None)
for _ in range(1000000):
    L=random.uniform(.05,3)
    b=random.uniform(.05,.95)
    d=random.uniform(.05,.95)
    if abs(1-L*b)<1e-8 or abs(1-L*d)<1e-8:continue
    a=(1-2*L*b+L*b*b)/(1-L*b)
    c=(1-2*L*d+L*d*d)/(1-L*d)
    if not (0<a<1 and 0<c<1 and a+b>1 and c+d>1):continue
    l1=(1-L*b)/a;l2=(1-L*d)/c
    if min(l1,l2)<=0:continue
    s=random.random()
    al1=b*s;al2=d*(1-s);al3=1-al1-al2
    if al3>=min(a,c):continue
    aa=al2/(1-al3/a);bb=al1/(1-al3/c)
    if not (0<aa<1 and 0<bb<1):continue
    if max(abs(2*s-1),abs(2*al2/aa-1),abs(2*al1/bb-1))>2-3**.5:continue
    sig=l1*aa+l2*bb-1
    if sig<=1e-8:continue
    m=(l1*aa*aa+l2*(2*bb-bb*bb)-1)/(2*sig)
    if not 0<m<1:continue
    G=interval_min(aa,bb,l1,l2,m)
    if G+sig>2:continue
    excess=4/9*(l1+l2+L)+min(1.,2-G-sig)-2
    if excess>record[0]:
        record=(excess,(L,b,d,a,c,s,al1,al2,al3,aa,bb,l1,l2,sig,m,G))
print(record)
