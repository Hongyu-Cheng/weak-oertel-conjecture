"""Exact algebra for a candidate finite-ear majorant; not a proof by itself."""
import sympy as S
from pathlib import Path
x,s,v,w,d,u=S.symbols('x s v w d u')
t=x*u
b=x+s;c=x+s+w;e=s+w;L=x+w+2*v;H=x+s+w+v;B=x+2*s+w
k=(L+d)*B/2
q1=(2*v+w)**2*B/(2*L);sig1=(2*v+w)*B/L
q2=L*b*b/(2*H)+d*(B-e*e/(e+t))/2
sig2=L*b/H+d*e/(e+t)
q3=L*c*c/(2*H)+d*(B-s*s/(b+d-t))/2
sig3=L*c/H+d*s/(b+d-t)
M=q1/sig1+q2/sig2+q3/sig3
cross=q2/sig2**2+q3/sig3**2+(c*q2/b+b*q3/c)/(sig2*sig3)
expr=2*M*M-(L+d/2)*M-k*cross
num,den=S.fraction(S.factor(expr))
print('factorization',S.factor_list(num)[0],[(str(f)[:100],p) for f,p in S.factor_list(num)[1]],flush=True)
Path('./finite_ear_majorant_num_root.txt').write_text(str(num))
P=S.Poly(S.expand(num),d,u,x,s,v,w)
print('degrees',P.degree_list(),'terms',len(P.terms()),'negative',sum(co<0 for _,co in P.terms()),flush=True)
du=P.degree(u)
bern=[]
for i in range(du+1):
    pol=S.expand(sum(P.as_expr().coeff(u,j)*S.binomial(i,j)/S.binomial(du,j) for j in range(i+1)))
    coeff=S.Poly(pol,d,x,s,v,w).coeffs()
    print('Bernstein',i,'terms',len(coeff),'negative',sum(z<0 for z in coeff),flush=True)
    bern.append(pol)
Path('./finite_ear_majorant_bernstein_root.txt').write_text('\n'.join(map(str,bern)))
