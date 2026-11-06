from fractions import Fraction as F
checks=0
def ck(q):
    global checks
    assert q
    checks+=1

for d,a,root in [(1,F(1,8),F(1,2)),(2,F(1,81),F(1,3))]:
    D=d+2
    ck(root**D==a)
    k=(3-a)/4
    alo,ahi=k-a/2,k+a/2
    blo,bhi=k-F(1,2),k+F(1,2)
    ck(ahi-alo==a)
    ck(bhi-blo==1)
    ck((alo+blo)/2==(1-a)/2)
    ck((ahi+bhi)/2==1)
    M=2+a
    ck(a<M/2 and 1<M/2)
    ck(min(a+1,F(2))>M/2)
    w=((root+1)/2)**D
    alpha=(1-root)/(1+root)
    ck(a/(1-alpha)**D==w)
    ck(1/(1+alpha)**D==w)
    E=1+2*w
    ck(a/(1-alpha)**(D-1)+1+1/(1+alpha)**(D-1)==E)
    y=(F(1,2)+2*w*k)/E
    ck(F(1,2)<y<k)
    ck(y-1<alo)
    ck(y+1>bhi)
    cap=a+1-y
    gamma=F(d,d+1)**d
    ck(cap<gamma*M/2)
    ck((1+2*a)/(2*M)>F(1,4)>=gamma/2)
    ck((1-a)/4==blo)
    ck((1+3*a)/4<=bhi)
    if d==1:
        ck((alo,ahi,blo,bhi)==(F(21,32),F(25,32),F(7,32),F(39,32)))
        ck(y==F(1133,1888) and w==F(27,64) and E==F(59,32))
        ck(cap==F(991,1888))
        ck(gamma/2-cap/M==F(3,1003))
        ck((1+2*a)/(2*M)==F(5,17))
    else:
        ck((alo,ahi,blo,bhi)==(F(20,27),F(61,81),F(20,81),F(101,81)))
        ck(y==F(10433,18306) and w==F(16,81) and E==F(113,81))
        ck(cap==F(8099,18306))
        ck(gamma/2-cap/M==F(785,331542))
        ck((1+2*a)/(2*M)==F(83,326))
print(f'{checks} exact checks PASS')
