import sys

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from fractions import Fraction as F
import json
N=9;half=N//2;coords=np.array([(i/half,j/half) for i in range(-half,half+1) for j in range(-half,half+1)]);count=N*N
tris=[]
for i in range(N-1):
 for j in range(N-1):
  a=i*N+j;b=(i+1)*N+j;c=i*N+j+1;d=(i+1)*N+j+1
  tris.extend([(a,b,d),(a,d,c)])
M=np.zeros(count);MX=M.copy();MY=M.copy();RX=M.copy();RY=M.copy();SX=M.copy();SY=M.copy();CX=M.copy();CY=M.copy()
rows=[];cols=[];vals=[];nrow=0
for tri in tris:
 vv=coords[list(tri)];area=abs(np.linalg.det(np.array([vv[1]-vv[0],vv[2]-vv[0]])))/2
 inv=np.linalg.inv(np.column_stack([vv,np.ones(3)]).T)
 for j,z in enumerate(coords):
  if j in tri:continue
  lam=inv@np.r_[z,1.]
  rows.append(nrow);cols.append(j);vals.append(1.)
  for ii,l in zip(tri,lam):rows.append(nrow);cols.append(ii);vals.append(-l)
  nrow+=1
 for k,i in enumerate(tri):
  M[i]+=area/3;MX[i]+=area*(sum(vv[:,0])+vv[k,0])/12;MY[i]+=area*(sum(vv[:,1])+vv[k,1])/12
  if sum(vv[:,0])>=0:RX[i]+=area/3
  if sum(vv[:,1])>=0:RY[i]+=area/3
for j in range(N-1):
 i0=half*N+j;i1=i0+1;v0=coords[i0,1];v1=coords[i1,1];length=v1-v0
 SX[i0]+=length/2;SX[i1]+=length/2;CX[i0]+=length*(2*v0+v1)/6;CX[i1]+=length*(v0+2*v1)/6
for i in range(N-1):
 i0=i*N+half;i1=i0+N;v0=coords[i0,0];v1=coords[i1,0];length=v1-v0
 SY[i0]+=length/2;SY[i1]+=length/2;CY[i0]+=length*(2*v0+v1)/6;CY[i1]+=length*(v0+2*v1)/6
A=coo_matrix((vals,(rows,cols)),shape=(nrow,count)).tocsr()
from scipy.sparse import vstack
A=vstack([A,-MY]);bb=np.r_[np.zeros(nrow),-1e-5];gamma=27/64
for ratio in [F(1,20),F(1,10),F(1,5),F(1,3),F(1,2),F(2,3),F(1),F(3,2),F(2),F(3),F(5),F(10),F(20)]:
 rr=float(ratio);eq=np.array([M,SX-SY,CX,CY,MX-rr*MY]);rhs=np.array([1,0,0,0,0]);obj=RX-rr*RY
 result=linprog(-obj,A_ub=A,b_ub=bb,A_eq=eq,b_eq=rhs,bounds=(0,None),method='highs')
 if not result.success:print('ratio',ratio,'infeasible',result.message,flush=True);continue
 value=obj@result.x;bound=1-gamma-rr*gamma;gap=value-bound
 print('ratio',ratio,'value',value,'bound',bound,'gap',gap,'moments',MX@result.x,MY@result.x,'sections',SX@result.x,SY@result.x,flush=True)
 if gap>1e-7:
  rec={'N':N,'ratio':str(ratio),'heights':result.x.tolist(),'value':value,'bound':bound,'moments':[MX@result.x,MY@result.x]};open('./two-section-concave-grid-numerical-candidate.json','w').write(json.dumps(rec,indent=2));print('NUMERICAL CANDIDATE ONLY; rational certification required',flush=True);break
