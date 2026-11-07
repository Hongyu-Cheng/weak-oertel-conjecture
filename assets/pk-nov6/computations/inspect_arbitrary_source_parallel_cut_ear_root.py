"""Exact coefficient probe; no positivity assertion unless explicitly checked."""
from pathlib import Path
import json
import sys
import sympy as s
from flint import fmpz_mpoly as F

a,b,t,u=s.symbols('a b t u')
L=a+b+1
branch=sys.argv[1] if len(sys.argv)>1 else 'double'
if branch=='double':
    X=(1+t)*u/(1+u)
    Y=(1+t)/(1+u)
    sig=[b+1+a*t/(a+X), a+1+b*t/(b+Y), a+b]
    q=[((b+1)**2+t*(L-a*a/(a+X)))/2,
       ((a+1)**2+t*(L-b*b/(b+Y)))/2,
       (a+b)**2/2]
else:
    X=-a*u/(1+u)
    Y=1+t-X
    sig=[(b+1)*(Y+b)/(b+1-X), a+1+b*t/(b+Y), a+b]
    q=[sig[0]*(b+1)/2,
       ((a+1)**2+t*(L-b*b/(b+Y)))/2,
       (a+b)**2/2]
k=L*(L+t)/2
M=s.cancel(sum(x/y for x,y in zip(q,sig)))
T=s.cancel(sum(x/y**2 for x,y in zip(q,sig)))
U=s.cancel(s.prod(x/y**2 for x,y in zip(q,sig)))
print('data simplified',flush=True)
E=s.cancel(M*M-k*T)
En,Ed=s.fraction(E)
print('E', len(s.Poly(En,a,b,t,u).terms()), flush=True)
Mn,Md=s.fraction(M); Un,Ud=s.fraction(U)
fg=F.gens(4)
def fp(expr):
    ans=F(0,4)
    for mon,coef in s.Poly(expr,a,b,t,u).terms():
        z=F(int(coef),4)
        for g,k0 in zip(fg,mon): z*=g**k0
        ans+=z
    return ans
RN=F(2,4)*fp(Mn)**2*fp(En)**2*fp(Ud)-fp(L*(L+t))**3*fp(Un)*fp(Md)**2*fp(Ed)**2
RD=F(2,4)*fp(Md)**2*fp(Ed)**2*fp(Ud)
print('uncancelled R',len(RN),'den',len(RD),flush=True)
common=RN.gcd(RD)
RN=RN//common;RD=RD//common
print('reduced R',len(RN),'den',len(RD),'common terms',len(common),flush=True)
for name,P0 in [('R_num',RN),('R_den',RD)]:
    neg=[(P0.exponent_tuple(j),str(P0.coefficient(j))) for j in range(len(P0)) if P0.coefficient(j)<0]
    print(name,'terms',len(P0),'negative',len(neg),'first',neg[:8],flush=True)
    Path(__file__).with_name('parallel_cut_ear_'+branch+'_'+name+'_root.txt').write_text(str(P0))
out={}
for name,f in [('E_num',En),('E_den',Ed)]:
    P=s.Poly(f,a,b,t,u)
    terms=P.terms()
    neg=[(m,str(c)) for m,c in terms if c<0]
    out[name]={'terms':len(terms),'degree':P.total_degree(),'negative_count':len(neg),'negative_first':neg[:20]}
    print(name,out[name],flush=True)
    Path(__file__).with_name('parallel_cut_ear_'+branch+'_'+name+'_root.txt').write_text(str(f))
Path(__file__).with_name('parallel_cut_ear_'+branch+'_coefficient_probe_root.json').write_text(json.dumps(out,indent=2))
