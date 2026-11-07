from fractions import Fraction as F
w=tuple(map(F,(2,42,82,122,21))); z=range(5); M=sum(w)
assert M==269
assert all(w[i+1]-w[i]>=w[i+2]-w[i+1] for i in range(3))
rows={
 1:((2,21,2,0,0),(2,21,2,0,0),(-21,19,59),F(601)),
 2:((2,42,42,26,10),(2,38,40,42,0),(-42,16,38),F(5444)),
 3:((0,0,21,F(183,4),21),(0,0,F(23,4),F(305,4),F(23,4)),(F(-183,4),F(-99,4),F(-61,2)),F(43737,8))}
for j,(pp,qq,du,score) in rows.items():
 p=tuple(map(F,pp));q=tuple(map(F,qq));la,nu,om=map(F,du)
 assert sum(p)==sum(q)>0
 assert sum((i-j)*p[i] for i in z)==sum((i-j)*q[i] for i in z)==0
 assert all(0<=p[i]<=w[i] and 0<=q[i]<=w[i] for i in z)
 for v,grad,mul in [(p,tuple(-a for a in p),tuple(la+nu*(i-j) for i in z)),(q,tuple(w[i]-q[i] for i in z),tuple(-la+om*(i-j) for i in z))]:
  for i in z:
   r=grad[i]-mul[i]
   assert r==0 or (r>0 and v[i]==w[i]) or (r<0 and v[i]==0)
 A=-sum(a*a for a in p)/2;B=sum(w[i]*q[i]-q[i]*q[i]/2 for i in z)
 assert A+B==score
 if j==3:
  assert A==F(-47601,32) and B==F(222549,32) and sum(p)==F(351,4)
  assert -p[j]==-w[j]+q[j]==F(-183,4)
assert F(43737,8)>5444>601>F(441,4)>1
assert [j for j in z if sum(w[:j+1])>=M/2 and sum(w[j:])>=M/2]==[3]
def upper_lengths(a,b):
 return tuple(max(F(0),min(w[i],-(b-a*(i-3)))) for i in z)
def lower_lengths(a,b):
 return tuple(max(F(0),min(w[i],a*(i-3)-b+w[i])) for i in z)
assert upper_lengths(F(99,4),F(-183,4))==tuple(map(F,rows[3][0]))
assert lower_lengths(F(61,2),F(183,4))==tuple(map(F,rows[3][1]))
assert sum(upper_lengths(F(1000),F(-183,4)))==F(267,4)
assert M/4-F(267,4)==F(1,2)
assert sum(upper_lengths(F(1000),F(-101,2)))==F(143,2)
assert F(143,2)/M==F(143,538)>F(1,4)
print('PASS: unique global free-width maximum, unique median, source duals and bad common boundary')
