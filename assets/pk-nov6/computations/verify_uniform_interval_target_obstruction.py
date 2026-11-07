from fractions import Fraction as Q

fibers={0:(Q(0),Q(2)),1:(Q(0),Q(3)),2:(Q(0),Q(4)),3:(Q(0),Q(2))}
M=sum(u-l for l,u in fibers.values())
assert M==11
medians=[k for k in fibers if sum(u-l for j,(l,u) in fibers.items() if j<k)<=M/2
         and sum(u-l for j,(l,u) in fibers.items() if j>k)<=M/2]
assert medians==[2]
def below(s,t):
    return [max(Q(0),min(u-l,s*k+t-l)) for k,(l,u) in fibers.items()]
def above(s,t):
    return [max(Q(0),min(u-l,u-s*k-t)) for k,(l,u) in fibers.items()]
right=above(Q(-1,2),Q(7,2))
left=below(Q(4),Q(-23,5))
assert right==[0,0,Q(3,2),0]
assert left==[0,0,Q(17,5),2]
assert 1-2*sum(right)/M==Q(8,11)
assert 2*sum(left)/M==Q(54,55)
assert Q(8,11)/Q(5,2)==Q(16,55)
assert (Q(54,55)-Q(8,11))/(Q(17,5)-Q(5,2))==Q(28,99)
assert Q(16,55)-Q(28,99)==Q(4,495)>0
print('Uniform interval target obstruction: all exact checks passed.')
