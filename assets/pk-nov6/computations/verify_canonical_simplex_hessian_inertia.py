import sympy as S
from random import Random

rng=Random(394023)
t=S.symbols('t')
checks=0
for d in range(2,7):
    m=d+1
    for trial in range(4):
        A=S.Matrix(m,m,lambda i,j: 0 if i==j else rng.randrange(-3,4))
        c=S.Matrix([sum(A[i,j] for i in range(m)) for j in range(m)])
        rows=S.Matrix([sum(A[i,j] for j in range(m)) for i in range(m)])
        B=A-S.diag(*c)
        assert all(sum(B[i,j] for i in range(m))==0 for j in range(m))
        W=S.eye(m)+t*B
        # Numeric-matrix characteristic coefficients avoid enormous intermediate
        # rational expressions in a symbolic Gaussian elimination.
        coeffs=B.charpoly().all_coeffs()
        det=sum((-1)**k*coeffs[k]*t**k for k in range(m+1))
        h=S.Rational(d,m)
        cap_second=[]
        cap_first=[]
        for i in range(m):
            # Exact coefficient arithmetic in the rational physical cap formula.
            # Retain only degrees0,1,2; higher degrees cannot affect the Hessian.
            dc=[S.expand(det).coeff(t,k) for k in range(3)]
            v=B[i,i]/h
            power=[1,d*v,S.Rational(d*(d-1),2)*v*v]
            numerator=[sum(dc[k]*power[q-k] for k in range(q+1)) for q in range(3)]
            factors=[B[i,i]-B[i,j] for j in range(m) if j!=i]
            den1=sum(factors)
            den2=sum(factors[k]*factors[l] for k in range(d) for l in range(k+1,d))
            cap_first.append(numerator[1]-den1)
            cap_second.append(2*(numerator[2]-numerator[1]*den1+den1*den1-den2))
        assert S.diff(det,t).subs(t,0)==sum(cap_first)/m
        actual=S.diff(det,t,2).subs(t,0)-sum(cap_second)/m
        expected=(c.dot(c)/d-(rows.dot(rows)+sum(x*x for x in A))/m)
        assert S.simplify(actual-expected)==0
        checks+=1
    c0=S.Matrix([S.Integer(i) for i in range(d)]+[-S.Integer(d*(d-1)//2)])
    assert sum(c0)==0 and c0.dot(c0)>0
    lift=S.Matrix(m,m,lambda i,j: 0 if i==j else (m*c0[j]+c0[i])/S.Integer(d*m-1))
    row=S.Matrix([sum(lift[i,j] for j in range(m)) for i in range(m)])
    assert S.Matrix([sum(lift[i,j] for i in range(m)) for j in range(m)])==c0
    assert row == -c0/(d*m-1)
    J=row.dot(row)+sum(x*x for x in lift)
    assert S.simplify(J-m*c0.dot(c0)/(d*m-1))==0
    assert S.simplify(c0.dot(c0)/d-J/m-(d*d-1)*c0.dot(c0)/(d*(d*m-1)))==0
    # Verify the full exact inertia by rational symmetric pivots on each matrix.
    coords=[(i,j) for i in range(m) for j in range(m) if i!=j]
    n=len(coords)
    C=S.zeros(m,n); R=S.zeros(m,n)
    for k,(i,j) in enumerate(coords): C[j,k]=1; R[i,k]=1
    Q=C.T*C/d-(R.T*R+S.eye(n))/m
    assert Q.to_DM().rank()==d*m-1
    assert Q*S.ones(n,1) == S.zeros(n,1)
    checks+=1
print('PASS:',checks,'exact directional physical Hessians/lifts, full ranks, null modes, and positive-subspace coefficients in dimensions2 through6')
