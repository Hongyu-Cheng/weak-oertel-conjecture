import sympy as s
p,q,U,V=s.symbols('p q U V',positive=True)
D=p+q-2*p*q
F=p*(1-q)/D;G=q*(1-p)/D
fi=4*p*F;fj=4*q*G
P=8*p*q*(1-p)*(1-q)/D;C=8+P;Ei=2*fi+P;Ej=2*fj+P
Ai=C+Ei*fi/(4*(p*U)**2)-C*fi/(2*p*U)
Aj=C+Ej*fj/(4*(q*V)**2)-C*fj/(2*q*V)
B=Ai+Aj-C;a=1-V;b=U
wb=F*(C-Ei/(p*U));wa=G*(C-Ej/(q*V))
checks=0
for expr in [Ai*a+B*(b-a)+Aj*(1-b)+wa+wb,
             Ai*a*a/2+B*(b*b-a*a)/2+Aj*(1-b*b)/2+a*wa+b*wb,
             C-8*(p+q-p*q)*(1-p*q)/D,
             Ei/C-p*(1-q)/(1-p*q),
             Ej/C-q*(1-p)/(1-p*q)]:
 assert s.factor(expr)==0;checks+=1
f,u,v=s.symbols('f u v',real=True);l=u+v-1
A=((u-f)**2+f*(1-f))/u**2
BB=((v-1+f)**2+f*(1-f))/v**2
Z=(1-v)**2*A+(1-u)**2*BB-l*l*(A+BB-1)
assert s.factor(Z*Z-4*(1-u)**2*(1-v)**2*A*BB+4*f*(1-f)*(1-u)**2*(1-v)**2*l*l/(u*u*v*v))==0
checks+=1
print(f'PASS: {checks} independent symbolic section-atom, moment, and disk identities.')
