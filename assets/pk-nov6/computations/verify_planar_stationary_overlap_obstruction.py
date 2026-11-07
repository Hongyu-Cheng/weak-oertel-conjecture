from fractions import Fraction as F

T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
caps=[(-1,-1,F(3,5)),(3,-1,F(-3,5)),(-1,3,F(-3,5))]
def clip(P,H):
    a,b,c=H
    Q=[]
    for X,Y in zip(P,P[1:]+P[:1]):
        sx=a*X[0]+b*X[1]+c
        sy=a*Y[0]+b*Y[1]+c
        if sx>=0: Q.append(X)
        if (sx<0<sy) or (sy<0<sx):
            t=sx/(sx-sy)
            Q.append(tuple(X[k]+t*(Y[k]-X[k]) for k in (0,1)))
    return Q
def area(P):
    return abs(sum(X[0]*Y[1]-X[1]*Y[0]
                   for X,Y in zip(P,P[1:]+P[:1])))/2 if len(P)>2 else F(0)
vol=area(T)
p=[area(clip(T,H))/vol for H in caps]
assert p==[F(9,25),F(12,25),F(12,25)]
pairs=[area(clip(clip(T,caps[i]),caps[j]))/vol
       for i,j in ((0,1),(0,2),(1,2))]
assert pairs==[F(3,25),F(3,25),F(2,25)]
assert area(clip(clip(clip(T,caps[0]),caps[1]),caps[2]))==0
assert max(p)<F(1,2)
assert sum(p)-1==sum(pairs)==F(8,25)<F(1,3)
theta=[F(1,4),F(3,8),F(3,8)]
vectors=[(F(-3,5),F(-3,5)),(F(3,5),F(-1,5)),(F(-1,5),F(3,5))]
assert all(sum(theta[i]*vectors[i][k] for i in range(3))==0 for k in (0,1))
assert sum(theta[i]*p[i] for i in range(3))==F(9,20)
assert F(9,20)-F(4,9)==F(1,180)
assert F(1,3)-sum(pairs)==F(1,75)
print('PASS: exact stationary three-cap overlap obstruction and correct weights')
