from fractions import Fraction as F
checks = 0
def ck(p, msg):
    global checks
    assert p, msg
    checks += 1
r = [F(1+3*j,4) for j in range(6)]
v = [a*a for a in r]
G = F(4,9)
ck(sum(v)==F(591,16), 'complete total area')
ck(v==[F(i,16) for i in (1,16,49,100,169,256)], 'all actual fiber areas')
ck(max(v)==16 and 2*max(v)<sum(v), 'strict no-heavy')
ck((r[0]+r[2])/2==r[1]==1, 'actual affine root midpoint')
ck(G+v[0]==F(73,144), 'middle all-direction upper bound')
ck(G*v[0]==F(1,36) and G*v[2]==F(49,36), 'endpoint own-depth lower bounds')
ck(G*(v[0]+v[2])/2-(G+v[0])==F(3,16), 'uniform hidden-base gap')
ck((v[0]+v[2])/2-1==F(9,16), 'full-point hidden coefficient')
ck(F(9,16)*F(1,9)-F(1,16)==0, 'full-point threshold')
for lam in [F(i,8) for i in range(41)]:
    h0=F(1,36)+lam/6
    h1=F(73,144)+2*lam/3
    h2=F(49,36)+7*lam/6
    ck((h0+h2)/2-h1==F(3,16), 'lambda cancels in base gap')
    for b in [F(i,3) for i in range(-9,10)]:
        ck(max(h0,h2+2*b)>h1+b, 'base one not selected')
for f in [F(1,9)+F(i,90) for i in range(1,31)]:
    ck(F(9,16)*f-F(1,16)>0, 'strict deep-region gap')
for t in [F(i,32) for i in range(33)]:
    B0=F(7,5)
    ck(0<=t*(1-t)*B0<=B0/4, 'exact vector chord-gap bound')
print(f'{checks} exact rational checks passed.')
