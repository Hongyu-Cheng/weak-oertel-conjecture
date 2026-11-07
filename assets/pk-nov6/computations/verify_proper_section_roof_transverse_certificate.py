from fractions import Fraction as F

checks=0
def ck(v,msg):
    global checks
    assert v,msg
    checks+=1
W=F(6); alpha=F(5,4); L=F(3)
gmin=alpha-1; gmax=alpha+1
Q=W*alpha; M=L*W+Q
ck(gmin==F(1,4)>0,'positive roof')
ck(gmax==F(9,4)<=L,'reflection containment')
ck(Q==F(15,2),'cap area')
ck(M==F(51,2),'whole area')
ck(Q/M==F(5,17),'source exact normalized depth')
ck(F(3)/W==F(1,2),'section half ratio')
Qside=3*(alpha-F(1,2))
ck(Qside==F(9,4),'positive side exact integral')
ck(Qside/Q==F(3,10)<F(4,9),'failed Gamma2 transfer')
ck(3*L/(L*W)==F(1,2),'negative side half ratio')
ck(L*W/2==9>Q,'source not globally deepest')
hlo=(gmax-L)/2; hhi=gmin
ck(hlo==F(-3,8),'transverse lower endpoint')
ck(hhi==F(1,4),'transverse upper endpoint')
for numerator in range(-12,9):
    h=F(numerator,32)
    if not hlo<=h<=hhi:
        continue
    ck(2*h-gmax>=-L,'lower reflected roof containment')
    ck(2*alpha>=2*h,'paired roof nonempty')
    ck(-L<=h<=alpha,'actual source membership')
    ck(Q-h*W>0,'positive symmetric subset half mass')
ck(Q-hlo*W==F(39,4),'depth at transverse lower endpoint')
print(f'{checks} exact rational checks passed.')

# Universal nonsymmetric roof realization and unique section center.
W=F(5); R=F(19,10); m0_lower=F(121,1000)
G=F(31,10); L=F(50)
ck(F(11,10)*W==F(11,2),'section centroid first moment')
ck(R*R>F(221,100),'mixed support radius')
ck(F(1,5)>=m0_lower,'moment coefficient a')
ck(L*m0_lower/R==F(121,38)>G,'explicit universal roof height')
Q=2*(G-F(1,2))+(3*G-F(9,2))
ck(Q==10,'nonsymmetric roof cap area')
M=L*W+Q
ck(M==260 and Q/M==F(1,26),'nonsymmetric total and depth')
ck(F(150,2)>Q,'source is not globally deepest')
ck(F(2,5)>F(1,4),'section center exceeds section OC')
ck(F(1,20)<F(1,10),'improving cap remains proper above')
ck(F(-1,40)>-L,'improving cap remains proper below')
Qz=Q-(F(11,2)-W)/40
ck(Qz==F(799,80)<Q,'explicit section-center original-depth loss')
QG=2*(G-2)
ck(QG==F(11,5),'projected positive cap integral')
ck(QG/Q==F(11,50)<F(2,9),'failure of projected OC fraction transfer')
ck(2*L/(L*W)==F(2,5),'tracked opposite-side fraction')
print(f'{checks} total exact rational checks passed after nonsymmetric extension.')

# Strict-noheavy realization of section-center loss.
W=F(7,2); center=F(17,28); section_center=F(5,8)
Rbound=F(2); m0_lower=F(289,5488); L=F(40)
ck((1+F(9,8))/W==center,'strict-noheavy section centroid')
ck(L*m0_lower/Rbound==F(1445,1372)>1,'strict-noheavy global minimizing roof bound')
M=41*W; Q=W
ck(M==F(287,2),'strict-noheavy total')
ck(max(F(41),F(123,2))<M/2,'all fibers strictly nonheavy')
ck(section_center+1==F(13,8),'section center downward depth')
ck(F(7,2)-3*section_center==F(13,8),'section center upward depth')
ck(center+1==F(45,28)<F(13,8),'centroid section depth is smaller')
ck(section_center-F(3,2)==F(-7,8)>-L,'lifted cap lower proper threshold')
ck(section_center<1,'lifted cap upper proper threshold')
ck(W*(1-section_center+center)==F(55,16)<Q,'strict-noheavy lifted section center loses depth')
ck(F(30)>Q,'strict-noheavy source is not globally deepest')
print(f'{checks} total exact rational checks passed with strict-noheavy supplement.')
ck(41*(F(3,4)+F(5,4)+F(3,4))/2==F(451,8)>F(2,9)*M,'strict-noheavy body explicitly satisfies OC')
print(f'{checks} final exact rational checks passed.')
