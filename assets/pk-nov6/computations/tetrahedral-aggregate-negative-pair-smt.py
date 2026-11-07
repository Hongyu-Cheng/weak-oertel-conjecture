import sys,time
import z3
P,a,b=z3.Reals('P a b');R=1-P;k=a-b;D=k*k+a*R+b*P
sumneg=R*(a+k*k)+2*k*(a+b);prodneg=a*a+a*k*R+k*k*b
N=D-sumneg+prodneg;B=2*D-3*sumneg+4*prodneg
Fnum=b*(P-a+b);diff=b*P-a*R
Target=64*(Fnum*B-N*diff)-27*D*B
constraints=[P>0,P<1,a>0,b>0,4*a<=P*P,4*b<=R*R,2*b-k*P>=0,b*b-b*k*P+k*k*a>=0,2*a+k*R>=0,a*a+a*k*R+k*k*b>=0,B>0,Target<0]
s=z3.SolverFor('QF_NRA');s.set(timeout=120000);s.add(*constraints);t=time.time();r=s.check();print('aggregate negative-pair lower',r,'seconds',time.time()-t,flush=True)
if r==z3.sat:
 print(s.model(),flush=True);open('./tetrahedral-aggregate-smt-candidate.txt','w').write(str(s.model())+'\n'+s.sexpr())
elif r==z3.unknown:print(s.reason_unknown(),flush=True)
