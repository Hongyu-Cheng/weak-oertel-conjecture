import sys,time

import z3
x,y,z=z3.Reals('x y z');w=1-x-y-z;S=1;a=x*y;b=z*w;P=x+y;R=z+w
D=(x+z)*(x+w)*(y+z)*(y+w);Ds=[(x+z)*(x+w),(y+z)*(y+w),(x+z)*(y+z),(x+w)*(y+w)]
N=[x*(2*x+z+w-Ds[0]),y*(2*y+z+w-Ds[1]),z*(x+y+2*z-Ds[2]),w*(x+y+2*w-Ds[3])]
Centr=[b*(1+x)-x*x*y,b*(1+y)-x*y*y,a*(1+z)-z*z*w,a*(1+w)-z*w*w]
base=[x>0,y>0,z>0,w>0]+[g>=0 for g in Centr]
for name,j,k,ordering,upper in [('negative_pair_lower_unordered',2,3,[],False),('negative_middle_pair_upper',2,3,[y>=x,w>=z,N[2]*(x+w)>=N[0]*(y+z),N[1]*(x+w)>=N[3]*(y+z)],True)]:
 B=12*N[j]*N[k]-3*(Ds[j]*N[k]+Ds[k]*N[j]);FN=b*(P-a+b)
 expr=(37*D-64*FN)*B+192*(b*P-a*R)*N[j]*N[k] if upper else (64*FN-27*D)*B-192*(b*P-a*R)*N[j]*N[k]
 solver=z3.SolverFor('QF_NRA');solver.set(timeout=60000);solver.add(*(base+ordering+[B>0,expr<0]));start=time.time();result=solver.check();print(name,result,'elapsed',time.time()-start,flush=True)
 if result==z3.sat:
  model=solver.model();print('EXACT MODEL',model,flush=True);print('values',[model.eval(v,model_completion=True)for v in [x,y,z,w]],flush=True)
  open('./tetrahedral-central-correction-smt-candidate.txt','w').write(name+'\n'+str(model)+'\n'+str(solver.sexpr()))
 elif result==z3.unknown:print('reason',solver.reason_unknown(),flush=True)
