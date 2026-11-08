from fractions import Fraction as Q
from math import comb
import json

# Direct transcription of the proof. No imports from submitted checkers.
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
p=(Q(334371,10**6),Q(332129,10**6))
u=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(0),Q(1))]
n=[tuple(Q(x,10**6) for x in row) for row in [(-599637,-800272),(971233,238130),(-310548,950558)]]
w=[Q(1),Q(58465186893,71226006661),Q(317229508283,498582046627)]
f=[tuple(wi*x for x in ni) for wi,ni in zip(w,n)]
assert all(sum(row[i] for row in f)==0 for i in range(2))
q=[(Q(403842028213,971233000000),Q(0)),(Q(52763454809,90079000000),Q(37315545191,90079000000)),(Q(0),Q(93258952483,160054400000))]
delta=[Q(325903,10**7),Q(6517257,200000000),Q(50753,1562500)]
eps=Q(1,10**20); m=Q(660847,200000); gamma=Q(99,100)**99
origin=[Q(3,100)*(1-sum(p)),Q(3,100)*p[0],Q(3,100)*p[1]]+[Q(1,100)]*97
assert sum(origin)==1 and min(origin)>Q(99,10000)
E=[]; beta=[]; all_gaps=[]
for a,N in enumerate([56,56,55]):
    b,c=[j for j in range(3) if j!=a]
    vals=[dot(f[a],sub(v,p)) for v in u]
    assert vals[a]>0 and vals[b]<0 and vals[c]<0
    assert dot(f[(a+1)%3],sub(q[a],p))==0
    theta_max=abs(det(sub(u[a],p),sub(q[a],p)))
    theta=m/(1+delta[a])**99
    contraction=theta/theta_max
    assert 0<contraction<1
    contracted=tuple(p[i]+contraction*(q[a][i]-p[i]) for i in range(2))
    verts=[p,u[a],contracted]
    assert abs(det(sub(verts[1],p),sub(verts[2],p)))==theta
    for j in range(3):
        scores=[dot(f[j],sub(v,p)) for v in verts]
        assert min(scores)==0 if j==a else max(scores)==0
    # Cramer's rule directly reconstructs d_a from the first two row equations.
    rhs=[Q(2 if j==a else -1) for j in range(3)]
    dxy=((rhs[0]*f[1][1]-f[0][1]*rhs[1])/det(*f[:2]),(f[0][0]*rhs[1]-rhs[0]*f[1][0])/det(*f[:2]))
    assert [dot(row,dxy) for row in f]==rhs
    assert max(abs(x) for x in (-sum(dxy),*dxy))<3
    v0,v1=sub(u[a],p),sub(contracted,p)
    U,V=det(dxy,v1)/det(v0,v1),det(v0,dxy)/det(v0,v1)
    assert min(U,V)>0 and U+V<6
    dp=delta[a]+Q(1,10**12)
    gaps=[(dp-delta[a])*o-10*(2-delta[a]-dp)*eps for o in origin]
    assert min(gaps)>0
    all_gaps.extend(gaps)
    assert 1-30*dp>0>1-31*dp
    E.append(theta*sum(comb(N,r)*(1-r*dp)**99 for r in range(1,31)))
    beta.append(vals[a]**2/((vals[a]-vals[b])*(vals[a]-vals[c])))
surplus=1+sum(E)-m
margins=[gamma*m-b-e for b,e in zip(beta,E)]
assert min(surplus,*margins)>Q(8,100000)
W=(2**167-1)*m+1+sum(E)
assert gamma*m/W<gamma/Q(2**167)
assert Q(2**167)*gamma*m/W>Q(24,65)
print(json.dumps({'status':'PASS_DIRECT_TRANSCRIPTION_INDEPENDENT_CHECK','surplus':float(surplus),'middle_margins':list(map(float,margins)),'minimum_origin_facet_gap':float(min(all_gaps)),'relative_sharp_deficit':float(surplus/W)},indent=2))
