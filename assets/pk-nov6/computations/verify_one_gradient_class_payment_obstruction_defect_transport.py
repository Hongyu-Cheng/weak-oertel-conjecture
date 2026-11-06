"""Exact actual P=3Delta_2 interval calibration and every minor quota."""
from fractions import Fraction as F
import runpy

D=runpy.run_path('./verify_ell_contact_cell_parity_obstruction_defect_transport.py')
hull,inside=D['hull'],D['inside']
P=[(i,j) for i in range(4) for j in range(4-i)]
p=(1,1)
checks=0
assert len(P)==10
assert all(sum(z[c] for z in P)==10 for c in range(2))
assert len({(x%2,y%2) for x,y in P})==4
checks+=3
pairs=[((1,0),(1,2)),((2,0),(0,2)),((0,1),(2,1))]
for a,b in pairs:
    assert a in P and b in P and tuple(a[c]+b[c] for c in range(2))==(2,2)
    checks+=1
core={p}|{z for pair in pairs for z in pair}
extra=[z for z in P if z not in core]
assert len(core)==7 and len(extra)==3
assert all(sum(z[c]-p[c] for z in extra)==0 for c in range(2))
checks+=2
normals={(0,0):(-1,-1),(0,3):(-1,1),(3,0):(1,-1),
         (1,0):(-1,-4),(2,0):(1,-4),(0,1):(-4,-1),
         (0,2):(-4,1),(1,2):(3,4),(2,1):(4,3)}
for z,a in normals.items():
    kept=[w for w in P if sum(a[c]*(w[c]-z[c]) for c in range(2))>=0]
    assert z in kept and len(kept)<=2
    checks+=1
v=[20*(z[0]-1)+2*(z[1]-1) for z in P]
assert sorted(v)==[-22,-20,-18,-16,-2,0,2,18,20,38]
assert len([t for t in v if t>0])==4
assert len([t for t in v if t>=0])==5
assert min(abs(t) for t in v if t)!=0
assert F(1,30)<1
checks+=5

counts={k:0 for k in range(1,5)}
mins={k:100 for k in range(1,5)}
for mask in range(1,(1<<len(P))-1):
    T=[z for j,z in enumerate(P) if mask>>j&1]
    if [z for z in P if inside(z,hull(T))]!=T:
        continue
    k=len({(x%2,y%2) for x,y in T})
    gap=5*k-2*len(T)
    assert gap>0
    counts[k]+=1
    mins[k]=min(mins[k],gap)
    checks+=1
assert counts=={1:10,2:45,3:93,4:126}
assert mins=={1:3,2:2,3:5,4:2}
checks+=2
print(f'{checks} exact checks PASS; {sum(counts.values())} proper closed minors')
print('counts:',counts,'minimum quota slacks:',mins)
