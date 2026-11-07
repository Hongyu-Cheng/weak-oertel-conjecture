"""Exact checks of the explicit center in the proved three-fiber theorem."""
from fractions import Fraction as F

count=0
for a0 in range(1,15):
    for a2 in range(1,15):
        s=F(a0+a2)
        m=min(a0,a2)
        for dl in range(9):
            for du in range(dl,9):
                L=s/2+F(dl,3)
                U=s/2+F(du,3)
                a1=(L+U)/2
                T=(s+a1)/2
                if max(a0,a1,a2)>=T:
                    continue
                x=max(F(0),T-m-L)
                up=min(a1,U-x)+min(m,max(F(0),s-2*x))
                down=min(a1,L+x)+min(m,max(F(0),s+2*x))
                assert -L<=x<=U
                assert up>=T and down>=T
                assert a1+m>=T
                count+=1
print(f"Explicit three-fiber capacity center verified on {count} exact rational instances.")
