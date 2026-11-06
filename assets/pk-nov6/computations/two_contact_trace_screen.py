import random

def interval_min(p,q,l1,l2,t):
    grid=sorted(set([0.,1.,p,1-q,t]))
    best=1e30
    for a in [0.]:
        for b in grid:
            if a<=t<=b and b>a+1e-12:
                val=(l1*max(0,min(b,1)-max(a,p))
                     +l2*max(0,min(b,1-q)-max(a,0)))/(b-a)
                best=min(best,val)
    return best

random.seed(935)
record=(1e99,None)
for _ in range(1000000):
    a=random.uniform(.0001,.9999)
    b=1-a
    c=max(a,b)+random.random()*4
    r=random.uniform(.0001,.9999)
    t=a*b*(1-r)
    delta=t-c*r
    s1=c-a;s2=c-b
    if abs(delta)>min(s1,s2):continue
    alpha=[b*(1-r),a*(1-r),r]
    lam=[a/(1-alpha[0]),b/(1-alpha[1]),c/(1-r)]
    ss=[s1,s2]
    G=[]
    for i in [0,1]:
        j=1-i;k=2
        contact=.5+delta/(2*ss[i])
        G.append(interval_min(alpha[j],alpha[k],lam[j],lam[k],contact))
    if max(G[i]+ss[i] for i in [0,1])>2:continue
    gap=max(G[i]+ss[i] for i in [0,1])-4/9*sum(lam)
    if gap<record[0]:
        record=(gap,(a,c,r,alpha,lam,ss,G))
print(record)
