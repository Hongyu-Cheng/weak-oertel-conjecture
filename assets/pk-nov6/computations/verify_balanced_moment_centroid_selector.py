"""Exact certificate checks; the full interval optimization is in the note."""
from fractions import Fraction as F

a,b,c=F(1,10),F(1),F(21,20)
I={-1:(-F(21,80),-F(13,80)),0:(-F(1,2),F(1,2)),1:(-F(59,80),F(5,16))}
assert tuple((I[-1][i]+I[1][i])/2 for i in (0,1))==(-F(1,2),F(3,40))
assert [I[z][1]-I[z][0] for z in (-1,0,1)]==[a,b,c]
M=a+b+c
assert M==F(43,20)
assert a<M/2 and c<M/2 and a+b>M/2
t=(a+b)/2
assert t==F(11,20)
A=t*(1-t)/2
ell_p=(2*t-F(17,20))/6
ell_m=F(1,10)
Fp=(2*t-F(17,20))*ell_p-3*ell_p**2
Fm=2*t*ell_m-3*ell_m**2
assert (A,ell_p,ell_m,Fp,Fm)==(F(99,800),F(1,24),F(1,10),F(1,192),F(2,25))
left,right=-(A+Fm)/t,(A+Fp)/t
assert (left,right)==(-F(163,440),F(619,2640))
y=(left+right)/2
assert y==-F(359,5280)
slope=-F(707,1056)
assert y+slope==I[1][0]
assert y-slope==F(397,660)>I[-1][1]
mass=a+y+F(1,2)
assert mass==F(2809,5280)
assert M/4-mass==F(29,5280)>0

def centroid(t):
    lo=max(F(0),(t-1)/2)
    hi=min(a,t/2)
    def opt(p):
        ell=max(lo,min(hi,p/6))
        return p*ell-3*ell*ell
    return (opt(2*t-F(17,20))-opt(2*t))/(2*t)

def formula(t):
    if t<=F(3,10): return -t/6
    if t<=F(17,40): return -F(1,10)+F(3,200)/t
    if t<=F(29,40): return t/6-F(29,120)+F(433,9600)/t
    return -F(17,400)/t

for j in range(1,241):
    tt=F(j,200)
    assert centroid(tt)==formula(tt)
    assert -F(17,80)<=centroid(tt)<=0
assert centroid(F(1,10))==-F(1,60)
assert F(3,5)+centroid(F(1,10))-M/4==F(11,240)
assert centroid(F(2,5))==-F(1,16)
# Exact third-branch discriminant and interval-root comparisons.
assert 1720**2-4*1600*433==120**2*13
assert 3**2<13<5**2 and 13<F(121,9)
print('PASS: exact moment body, unique base, prescribed cap gap, and t branches.')
