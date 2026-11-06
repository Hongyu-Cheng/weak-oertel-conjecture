"""Exact coefficient checks, with all volumes divided by pi."""
from fractions import Fraction as F

eps=F(1,10)
assert 1-eps*F(2,3)>0
assert F(1,2)-eps==F(2,5)
assert F(1,2)+eps==F(3,5)
for j in [0,1]:
    cap=3*(3-(F(j)+F(1,2)))
    assert cap==3*(F(5,2)-j)
assert F(1,8)+(eps*eps/2)*F(1,4)==F(101,800)

# Unknown vector is (v_i,w_i,m_i); the four homogeneous equations
# from the two t thresholds and two s thresholds have full rank.
rows=[[F(1,2),F(3,2),F(1)],
      [F(3,2),F(3,2),F(1)],
      [F(3,2),F(1,2),F(1)],
      [F(3,2),F(3,2),F(1)]]
rank=0
for col in range(3):
    pivot=next((i for i in range(rank,len(rows)) if rows[i][col]),None)
    if pivot is None:continue
    rows[rank],rows[pivot]=rows[pivot],rows[rank]
    scale=rows[rank][col]
    rows[rank]=[x/scale for x in rows[rank]]
    for i in range(len(rows)):
        if i!=rank:
            multiple=rows[i][col]
            rows[i]=[rows[i][k]-multiple*rows[rank][k] for k in range(3)]
    rank+=1
assert rank==3
assert F(1,4)+F(1,4)==F(1,2)
assert 8+4+8+2==22
print("Exact finite-cap uniqueness coefficients passed; 22 halfspaces plus total volume.")
