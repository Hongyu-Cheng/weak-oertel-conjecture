from fractions import Fraction as F

def tail(I,t):
    l,r=I
    return max(F(0),r-max(l,t))
def vol(I):return I[1]-I[0]
def disc(A,C):
    pts=sorted(set(A+C))
    T=vol(A)-vol(C)
    ds=[tail(A,t)-tail(C,t) for t in pts]
    return max([abs(v) for v in ds]+[abs(T-v) for v in ds]+[abs(T)])
def pair(A,C,y):
    pts=sorted(set(A+[2*y-t for t in C]))
    cs=[tail(A,t)+tail(C,2*y-t) for t in pts]
    return min(cs+[vol(A)+vol(C)-v for v in cs]+[vol(A),vol(C)])
count=0
for A in [[F(-1),F(1)],[F(0),F(1)],[F(-3,2),F(1,3)]]:
 for C in [[F(-2),F(2)],[F(-1),F(3)],[F(0),F(5,2)]]:
  assert vol(A)<=vol(C)
  for y in [F(k,4) for k in range(-12,13)]:
   CR=[2*y-C[1],2*y-C[0]]
   delta=disc(A,CR)
   exact=pair(A,C,y)
   assert exact==vol(C)-delta
   overlap=max(F(0),min(A[1],CR[1])-max(A[0],CR[0]))
   assert exact>=overlap
   if CR[0]<=A[0] and A[1]<=CR[1]:assert exact==vol(A)
   count+=1
print(f'PASS: {count} exact unequal-volume moving-center interval identities, overlap bounds and containment cases')
