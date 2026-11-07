import sympy as s
p,t,m=s.symbols('p t m',positive=True)
for k in [2,3,4]:
 S=sum(s.prod(m+ell for ell in range(2,j+2))*2**j/s.factorial(j)*(t-p)**j*(1-p)**(k-1-j) for j in range(k))
 G=((k-1)+(m+1)*p-(k+m)*t)*S
 C=[s.expand(G).coeff(t,j) for j in range(k+1)]
 Q=lambda v:sum(C[j]*v**j/(m+j) for j in range(k+1))
 T=((m+1)*p+k-1)/(m+k+p-1)
 QT=s.factor(Q(T));print('k',k,'upper',QT,flush=True)
 neg=((m+1)*(k-1)+(m*k+1)*p)/(m*2**k*(1+p)**2)
 low=s.factor(neg-(m+1)*Q(p)/(2**k*(1-p)**(k+1)))
 print('lower',low,flush=True)
