from fractions import Fraction as F
from math import comb, log, exp
from scipy.optimize import minimize_scalar

def Tval(d,N,j):
    torque=0; mass=0
    for z in range(1,N+1):
        w=z**d
        if torque+(z-j)*w>0:
            return F(mass)-F(torque,z-j),z
        torque+=(z-j)*w; mass+=w
    return F(mass),N

for d in range(2,17,2):
    N=d+1;j=d//2+1
    T,k=Tval(d,N,j)
    ls=[comb(d,z-1)/2**d for z in range(1,N+1)]
    dual=sum(l*(d*log(z)-log(l)) for z,l in zip(range(1,N+1),ls))
    res=minimize_scalar(lambda a: sum(exp(d*log(z)+a*(z-j)) for z in range(1,N+1)),bounds=(-10,0),method='bounded')
    print(d,N,j,k,'T',T,'dual/T',exp(dual)/float(T),'E/T',res.fun/float(T))
