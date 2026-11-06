from fractions import Fraction as F

def prob(ps,bs):
    v=[F(1)]*len(ps)
    for b in bs:
        for i in reversed(range(len(ps))):
            v[i]=(ps[i]*v[i]+(b*v[i+1] if i+1<len(ps) else 0))/(ps[i]+b)
    return v[0]

cases=[
    ([F(9,10),F(1),F(1,40),F(1,2),F(1,20)],
     [F(1),F(31,40),F(9,20),F(7,40),F(3,40)],
     [F(9,10),F(1),F(1,2),F(3,40)],
     F(44654803616666020420209277,90424914060963166702617600),
     F(15380294780653175263,31144717777833976680),
     F(45047868558815635573,219603362719481976277785600)),
    ([F(1),F(1),F(1),F(1,8),F(1,40)],
     [F(1),F(1,10),F(39,40),F(1,20),F(21,40),F(1,20),F(9,20)],
     [F(1),F(1),F(1),F(3,20)],
     F(2707328154118677286425321717654449,5529271691908209942614085489921600),
     F(1060866680607737867294402281,2166639116517141016477280400),
     F(314330359687274458483242667,221170867676328397704563419596864)),
]
for ps,bs,merged,before,after,gap in cases:
    assert sum(ps)==sum(bs)==sum(merged)
    assert F(1) in bs and all(0<x<=1 for x in ps+bs+merged)
    assert prob(ps,bs)==before
    assert prob(merged,bs)==after
    assert after-before==gap>0
print('PASS: two exact capped merging counterexamples')
