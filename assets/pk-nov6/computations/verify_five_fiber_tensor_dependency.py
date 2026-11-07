from fractions import Fraction as F
zs=list(map(F,[-2,-1,0,1,2]))
lam=list(map(F,[1,-4,6,-4,1]))
rows=[[F(1),4-z*z,z,4*z-z*z*z] for z in zs]
assert all(sum(lam[j]*rows[j][k] for j in range(5))==0 for k in range(4))
def rank(a):
    a=[r[:] for r in a]; piv=0
    for k in range(len(a[0])):
        q=next((q for q in range(piv,len(a)) if a[q][k]),None)
        if q is None: continue
        a[piv],a[q]=a[q],a[piv]
        c=a[piv][k];a[piv]=[v/c for v in a[piv]]
        for j in range(len(a)):
            if j!=piv:
                c=a[j][k];a[j]=[v-c*w for v,w in zip(a[j],a[piv])]
        piv+=1
        if piv==len(a):break
    return piv
assert rank(rows)==4
for j in range(5): assert rank(rows[:j]+rows[j+1:])==4
assert [sum(l*z**k for l,z in zip(lam,zs)) for k in range(5)]==[0,0,0,0,24]
print('Exact five-fiber rank/dependency certificate passed.')
