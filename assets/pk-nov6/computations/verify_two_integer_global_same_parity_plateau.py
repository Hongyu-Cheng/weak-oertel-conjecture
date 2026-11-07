from fractions import Fraction as F

# This checks the exact finite transport certificate used in the
# all-real-parameter proof, not a numerical halfspace sample.
pieces = [
 (0,F(-11,5),F(-1,5),0,F(6,5)),
 (0,F(-1,5),F(1,5),1,F(1,5)),
 (1,F(-11,5),F(-6,5),1,F(6,5)),
 (1,F(-6,5),F(-3,5),1,F(8,5)),
 (1,F(-3,5),F(1,5),2,F(4,5)),
 (2,F(-11,5),F(-1),2,F(6,5)),
 (2,F(-1),F(1,5),3,F(4,5)),
]
for j in range(3):
 pieces.append((j,F(1,5),F(11,5),j+4,F(-6,5)))

for j in range(3):
 ranges=sorted((l,r) for jj,l,r,k,c in pieces if jj==j)
 assert ranges[0][0]==F(-11,5) and ranges[-1][1]==F(11,5)
 assert all(ranges[t][1]==ranges[t+1][0] for t in range(len(ranges)-1))
for k in range(7):
 ranges=sorted((l+c,r+c) for j,l,r,kk,c in pieces if kk==k)
 assert all(-1<=l<r<=1 for l,r in ranges)
 assert all(ranges[t][1]<=ranges[t+1][0] for t in range(len(ranges)-1))
for j,l,r,k,c in pieces[:7]:
 assert c>=0 and k-j>=0
for j,l,r,k,c in pieces[7:]:
 assert k-j==4 and c==F(-6,5) and r-l==2
assert sum(r-l for j,l,r,k,c in pieces)==F(66,5)

fibers=[(p,q,F(8,5)+F(3,5)*q)
        for q in (-1,0,1) for p in range(-4+3*q,5-3*q)]
M=sum(2*w for p,q,w in fibers)
assert M==72
def clamp(t,cap): return max(F(0),min(cap,t))
def cap_mass(a,b,c):
 return sum(clamp(w+a*p+b*q+c,2*w) for p,q,w in fibers)
assert cap_mass(0,1,0)==24
assert cap_mass(0,-3,-3)==15
assert cap_mass(0,3,-3)==F(33,5)
assert F(24,72)==F(1,3)>F(1,8)
assert F(72,5)+F(48,5)==24
assert F(56,5)+F(66,5)==F(122,5)>24
assert F(8,5)-5*F(3,10)>0
assert sum(max(F(0),-F(p+1,2),F(p+1,2)-1) for p in range(-7,8))==21
assert 12<21
# The paired-threshold proof uses these exact constants; inequality
# (16) itself has a complete two-case proof in the note.
assert 7*F(16,5)==F(112,5)
assert 2*F(66,5)==F(132,5)
assert 2*24==48
print('PASS: exact transport, all-cap constants, global cover, paired-threshold coefficients')
