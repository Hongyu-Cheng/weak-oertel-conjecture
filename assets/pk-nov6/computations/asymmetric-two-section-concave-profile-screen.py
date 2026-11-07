import sys

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,vstack
import random,json
rng=random.Random(107733); gamma=27/64
def cross(a,b): return a[0]*b[1]-a[1]*b[0]

def clip(poly,axis):
 out=[]
 for A,B in zip(poly,poly[1:]+poly[:1]):
  x=A[0][axis]; y=B[0][axis]
  if x>=-1e-12:out.append(A)
  if (x>1e-12 and y< -1e-12) or (x< -1e-12 and y>1e-12):
   t=x/(x-y);out.append((A[0]+t*(B[0]-A[0]),A[1]+t*(B[1]-A[1])))
 return out

def integrate(poly,n):
 out=np.zeros(n)
 if len(poly)<3:return out
 for j in range(1,len(poly)-1):
  tri=[poly[0],poly[j],poly[j+1]]; area=abs(cross(tri[1][0]-tri[0][0],tri[2][0]-tri[0][0]))/2
  out+=area*sum((z[1] for z in tri))/3
 return out

def coefficients(vertices,res=5):
 coords=[];ind={}
 for i in range(res+1):
  for j in range(res+1-i):
   ind[i,j]=len(coords);coords.append((i*vertices[0]+j*vertices[1]+(res-i-j)*vertices[2])/res)
 coords=np.array(coords);n=len(coords);tris=[]
 for i in range(res):
  for j in range(res-i):
   tris.append([ind[i,j],ind[i+1,j],ind[i,j+1]])
   if i+j<res-1:tris.append([ind[i+1,j],ind[i+1,j+1],ind[i,j+1]])
 M=np.zeros(n);MX=M.copy();MY=M.copy();RX=M.copy();RY=M.copy();SX=M.copy();SY=M.copy();CX=M.copy();CY=M.copy();rows=[];cols=[];vals=[];row=0
 for tri in tris:
  vv=coords[tri];area=abs(cross(vv[1]-vv[0],vv[2]-vv[0]))/2
  inv=np.linalg.inv(np.column_stack([vv,np.ones(3)]).T)
  for j,z in enumerate(coords):
   if j in tri:continue
   lam=inv@np.r_[z,1.];rows.append(row);cols.append(j);vals.append(1.)
   for ii,l in zip(tri,lam):rows.append(row);cols.append(ii);vals.append(-l)
   row+=1
  poly=[]
  for k,i in enumerate(tri):
   basis=np.zeros(n);basis[i]=1;poly.append((vv[k],basis));M[i]+=area/3;MX[i]+=area*(sum(vv[:,0])+vv[k,0])/12;MY[i]+=area*(sum(vv[:,1])+vv[k,1])/12
  RX+=integrate(clip(poly,0),n);RY+=integrate(clip(poly,1),n)
  for ax,S,C in [(0,SX,CX),(1,SY,CY)]:
   intersections=[]
   for A,B in zip(poly,poly[1:]+poly[:1]):
    a=A[0][ax];b=B[0][ax]
    if abs(a)<1e-11:intersections.append(A)
    if a*b < -1e-22:
     t=a/(a-b);intersections.append((A[0]+t*(B[0]-A[0]),A[1]+t*(B[1]-A[1])))
   unique=[]
   for z in intersections:
    if not any(np.linalg.norm(z[0]-w[0])<1e-9 for w in unique):unique.append(z)
   if len(unique)==2:
    A,B=unique; aa=A[0][1-ax];bb=B[0][1-ax];length=abs(bb-aa)
    # If the line is a full shared edge, each adjacent triangle contributes half.
    zeros=sum(abs(z[0][ax])<1e-11 for z in poly);factor=.5 if zeros==2 else 1.
    S+=factor*length*(A[1]+B[1])/2
    C+=factor*length*((2*aa+bb)*A[1]+(aa+2*bb)*B[1])/6
 A=coo_matrix((vals,(rows,cols)),shape=(row,n)).tocsr()
 return coords,tris,A,[M,MX,MY,RX,RY,SX,SY,CX,CY]

best=-1e9; tested=0
for trial in range(1000):
 # Random rational triangle translated so zero is a rational interior point.
 verts=np.array([[rng.randint(-8,8),rng.randint(-8,8)] for _ in range(3)],float)
 det=cross(verts[1]-verts[0],verts[2]-verts[0])
 if abs(det)<2:continue
 weights=np.array([rng.randint(1,15) for _ in range(3)],float);weights/=sum(weights);verts-=weights@verts
 coords,tris,A,coefs=coefficients(verts,5);M,MX,MY,RX,RY,SX,SY,CX,CY=coefs;n=len(coords)
 AA=vstack([A,-MY,-MX]);bb=np.r_[np.zeros(A.shape[0]),-1e-5,-1e-5]
 for kk in [.25,.5,1,2,4]:
  for rr in [.1,.25,.5,1,2,4,10]:
   eq=np.array([M,SX-kk*SY,CX,CY,MX-(rr/kk)*MY]);rhs=np.array([1,0,0,0,0]);obj=RX-rr*RY
   result=linprog(-obj,A_ub=AA,b_ub=bb,A_eq=eq,b_eq=rhs,bounds=(0,None),method='highs')
   tested+=1
   if not result.success:continue
   value=obj@result.x;bound=1-gamma-rr*gamma;gap=value-bound
   if gap>best:
    best=gap
    print('best',trial,kk,rr,gap,'p',RX@result.x,RY@result.x,'mom',MX@result.x,MY@result.x,'sec',SX@result.x,SY@result.x,flush=True)
   if gap>1e-7:
    rec={'trial':trial,'vertices':verts.tolist(),'coords':coords.tolist(),'triangles':tris,'sectionratio':kk,'scalarratio':rr,'heights':result.x.tolist(),'value':value,'bound':bound,'gap':gap,'coefs':[x.tolist() for x in coefs]}
    open('./asymmetric-two-section-profile-numerical-candidate.json','w').write(json.dumps(rec,indent=2));print('NUMERICAL CANDIDATE ONLY; needs exact certification',flush=True);sys.exit()
 if trial%50==0:print('trial',trial,'LPs',tested,'best',best,flush=True)
print('finished','LPs',tested,'best',best,flush=True)
