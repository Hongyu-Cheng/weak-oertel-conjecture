from fractions import Fraction as F

J=[(0,0),(1,0),(0,1),(1,1),(2,1),(1,2)]
roots=J[:4]
normals=[(1,0),(0,1),(-1,-1)]
a=[(F(-1,10),F(-1,10)),(F(1,10),F(-1,10)),
   (F(-1,10),F(1,10)),(F(1,10),F(1,10))]
beta=[F(0),F(1,10),F(1,10),F(1,5)]
dot=lambda x,y: sum(t*s for t,s in zip(x,y))
centers=lambda z:(11-4*z[0]-4*z[1],4*z[0]-5)
radii={z:F(1,10) if z in [(1,1),(2,1),(1,2)] else F(1,100) for z in J}
colors={z:0 for z in J}; colors[(2,1)]=1; colors[(1,2)]=2

for i,p in enumerate(roots):
    assert dot(a[i],p)==beta[i]
    for j in range(4):
        if j!=i:
            assert beta[j]-dot(a[j],p) in [F(1,10),F(1,5)]

# All expressions checked below are affine in epsilon, so checking the
# two endpoints certifies the whole closed parameter interval.
for e in [F(0),F(1,100)]:
    ell=lambda i,z:dot(a[i],z)-beta[i]+e
    contacts=[(5*e,5*e),(1-5*e,5*e),(5*e,1-5*e),(1-5*e,1-5*e)]
    for i,r in enumerate(contacts):
        assert ell(i,r)==0
        for j in range(4):
            if i!=j:
                assert ell(j,r) in [-F(1,10)+e,-F(1,5)+2*e]
                assert ell(j,r)<=-F(9,100)
    masses=[[F(0) for j in range(3)] for i in range(4)]
    for i in range(4):
        for z in J:
            assert -F(3,10)<=ell(i,z)<=F(11,100)
            for j,u in enumerate(normals):
                center=dot(u,centers(z))+ell(i,z)
                radius=radii[z]*sum(abs(v) for v in u)
                if j==colors[z]:
                    assert center-radius>0
                    masses[i][j]+=4*radii[z]**2
                else:
                    assert center+radius<0
        assert masses[i]==[F(103,2500),F(100,2500),F(100,2500)]

M=sum(4*radii[z]**2 for z in J)
defect=F(4,9)*F(3,25)-F(103,2500)
assert M==F(303,2500)
assert defect==F(91,7500)
assert defect/M==F(91,909)
widths=[F(1,5),F(1,5),F(2,5)]
new_weights=[w/sum(widths) for w in widths]
assert new_weights==[F(1,4),F(1,4),F(1,2)]
assert sum(l/w for l,w in zip(new_weights,widths))==F(15,4)
print('PASS: uniform cross contacts, fixed exact cap masses, vanishing witness gaps, and width normalization')
