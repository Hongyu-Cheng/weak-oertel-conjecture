from fractions import Fraction as F

P=(-1,0,1,2)
centers=((F(0),F(3,10)),(F(1),F(7,10)))

def L(i,z,x):
    s=x+z/F(5)-F(3,5)
    return s if i else -s

own=[L(i,*centers[i]) for i in range(2)]
assert own==[F(3,10),F(3,10)]
gap=[L(1-i,*centers[1-i])-L(i,*centers[1-i]) for i in range(2)]
assert gap==[F(3,5),F(3,5)]
cross=[L(i,*centers[1-i])-own[i] for i in range(2)]
assert cross==[-F(3,5),-F(3,5)]
assert sum(cross)==-sum(gap)

def cap_mass(u,a,z0,x0):
    out=[]
    for z in P:
        cut=x0-a*(z-z0)/u
        out.append(max(F(0),min(F(1),1-cut if u>0 else cut)))
    return out

dual0=cap_mass(-1,-F(1,5),*centers[0])
dual1=cap_mass(1,F(1,5),*centers[1])
assert dual0==[F(1,2),F(3,10),F(1,10),0]
assert dual1==[0,F(1,10),F(3,10),F(1,2)]
assert sum(dual0)==sum(dual1)==F(9,10)<1

assert cap_mass(-1,F(1,2),*centers[0])==[0,F(3,10),F(4,5),1]
assert cap_mass(1,-F(1,2),*centers[1])==[1,F(4,5),F(3,10),0]
assert -F(6,5)+F(7,5)==F(1,5)

masses=[]
for i,a in enumerate((F(1,2),-F(1,2))):
    for u in (1,-1):
        masses.append(sum(cap_mass(u,a,*centers[i])))
assert masses==[F(29,10),F(21,10),F(21,10),F(29,10)]
assert F(1,2)*(centers[1][0]-centers[0][0])-F(1,2)*(centers[0][0]-centers[1][0])==1
print('PASS: strict dual cycle gap, exact tilt correction, actual cap masses, and circuit flux.')
