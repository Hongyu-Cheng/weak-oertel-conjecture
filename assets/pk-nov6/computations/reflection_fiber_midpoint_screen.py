import random,json
random.seed(90318)
best=1
for it in range(20000):
    n=random.randrange(3,20)
    lo=[0];up=[0];a=random.randrange(-10,1);b=random.randrange(0,11)
    for _ in range(n-1):
        a+=random.randrange(0,8);b-=random.randrange(0,8)
        lo.append(lo[-1]+a);up.append(up[-1]+b)
    shift=max(l-u for l,u in zip(lo,up))+random.randrange(1,10)
    Is=list(zip(lo,[u+shift for u in up]));M=sum(u-l for l,u in Is)
    def R(j,t):
        return sum(max(0,min(u,2*t-Is[2*j-i][0])-max(l,2*t-Is[2*j-i][1]))
          for i,(l,u) in enumerate(Is) if 0<=2*j-i<n)
    vals=[R(j,(l+u)/2) for j,(l,u) in enumerate(Is)]
    ratio=max(vals)/M
    if ratio<best:
        best=ratio
        if ratio<.52:print(it,n,ratio,Is,flush=True)
    if ratio<.5:
        print('MIDPOINT_FAIL',ratio,Is,vals,flush=True)
        with open('./reflection_midpoint_failure.json','w') as f:json.dump({'Is':Is,'vals':vals,'ratio':ratio},f)
        break
print('best',best)
