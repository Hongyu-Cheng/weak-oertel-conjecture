from fractions import Fraction as F
I={-1:(-F(347,400),F(337,400)),0:(-F(1,2),F(1,2)),1:(-F(53,400),F(43,400))}
a,b,c=F(171,100),F(1),F(6,25);e=-F(1,80)
assert [(I[i][1]-I[i][0]) for i in [-1,0,1]]==[a,b,c]
assert (I[-1][0]+I[1][0])/2==I[0][0]
assert (I[-1][1]+I[1][1])/2==F(19,40)<=I[0][1]
assert (I[-1][0]+I[-1][1])/2==(I[1][0]+I[1][1])/2==e
M=a+b+c;t=M/2
assert (M,t)==(F(59,20),F(59,40))
lo=max(F(0),(t-b)/2);hi=min(a,c,t/2)
assert (lo,hi)==(F(19,80),F(6,25))
du=2*I[0][1]-I[-1][1]-I[1][1];dl=I[-1][0]+I[1][0]-2*I[0][0]
assert (du,dl)==(F(1,20),F(0))
assert (2*t-du-6*hi,2*t-dl-6*hi)==(F(73,50),F(151,100))
q=t-2*c;assert q==F(199,200)
y=2*c*e/t;length=(c*(a-c)+q*(1-q))/t
assert (y,length)==(-F(6,1475),F(14311,59000))
assert (y-length/2,y+length/2)==(-F(14791,118000),F(13831,118000))
assert (I[-1][0]+t/2,I[-1][1]-t/2)==(-F(13,100),F(21,200))
assert length-(a-t)==F(223,29500)>0
assert c<t<a
assert y-1<I[-1][0] and y+1>I[1][1]
cap=c+F(1,2)+y
assert cap==F(2171,2950)
assert M/4-cap==F(37,23600)>0
assert min(a+b,b+c)==F(31,25)<t
print('PASS: actual fibers, all-source endpoint optimization, unique longest base, and strict closed-cap failure.')
