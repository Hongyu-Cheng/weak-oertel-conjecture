import sys

import sympy as sp,numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix
from math import comb
x,y,z,w=sp.symbols('x y z w');v=sp.symbols('X U Z V');S=x+y+z+w;a=x*y;b=z*w;P=x+y;R=z+w
D=(x+z)*(x+w)*(y+z)*(y+w)
Ds=[(x+z)*(x+w),(y+z)*(y+w),(x+z)*(y+z),(x+w)*(y+w)]
N=[x*(S*(2*x+z+w)-Ds[0]),y*(S*(2*y+z+w)-Ds[1]),z*(S*(x+y+2*z)-Ds[2]),w*(S*(x+y+2*w)-Ds[3])]
DC=12*N[2]*N[3]-3*S*(Ds[2]*N[3]+Ds[3]*N[2]);FN=b*(P*S-a+b)
Target=sp.expand((64*FN-27*D)*DC-192*S*(b*P-a*R)*N[2]*N[3])
G=[b*(S+y)-x*y*y,N[2]*(x+w)-N[0]*(y+z),N[1]*(x+w)-N[3]*(y+z)]
sub={x:v[0],y:v[0]+v[1],z:v[2],w:v[2]+v[3]}
Target=sp.Poly(Target.subs(sub,simultaneous=True),*v);G=[sp.Poly(g.subs(sub,simultaneous=True),*v)for g in G]

def monomials(deg):
 for i in range(deg+1):
  for j in range(deg-i+1):
   for k in range(deg-i-j+1):yield(i,j,k,deg-i-j-k)

for deg in [10,11,12,14]:
 T=Target*sp.Poly((2*v[0]+v[1]+2*v[2]+v[3])**(deg-10),*v);mons=list(monomials(deg));index={m:i for i,m in enumerate(mons)};rhs=np.array([float(T.coeff_monomial(m))for m in mons]);data=[];rows=[];cols=[];desc=[];norms=[]
 for i in range(deg//3+1):
  for j in range(deg//4+1):
   for k in range(deg//4+1):
    used=3*i+4*j+4*k
    if used>deg:continue
    poly=G[0]**i*G[1]**j*G[2]**k;terms=poly.terms()
    for m in monomials(deg-used):
     column=len(desc);desc.append((i,j,k,m));norm=max(abs(float(c))for _,c in terms);norms.append(norm)
     for expo,c in terms:
      total=tuple(expo[j]+m[j]for j in range(4));rows.append(index[total]);cols.append(column);data.append(float(c)/norm)
 A=csc_matrix((data,(rows,cols)),shape=(len(mons),len(desc)));scale=max(abs(rhs));rr=rhs/scale
 print('degree',deg,'shape',A.shape,'nnz',A.nnz,flush=True)
 result=linprog(np.ones(len(desc)),A_eq=A,b_eq=rr,bounds=(0,None),method='highs',options={'time_limit':120})
 print('result',result.status,result.message,'residual',np.max(abs(A@result.x-rr))if result.success else None,flush=True)
 if result.success:
  import json
  rec={'degree':deg,'scale':scale,'terms':[{'generator_powers':d[:3],'monomial':d[3],'coefficient':float(c*scale/n)}for d,c,n in zip(desc,result.x,norms)if c>1e-10]}
  open('./tetrahedral-central-correction-numerical-certificate.json','w').write(json.dumps(rec,indent=2));print('NUMERICAL multipliers only; exact rational check still required',len(rec['terms']),flush=True);break
