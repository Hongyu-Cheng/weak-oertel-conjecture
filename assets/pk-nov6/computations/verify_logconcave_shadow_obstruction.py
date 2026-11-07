from fractions import Fraction as Q

fibers={0:(Q(0),Q(2)),1:(Q(0),Q(101,40)),2:(Q(0),Q(61,20)),
        3:(Q(0),Q(61,40)),4:(Q(0),Q(0))}
M=sum(u-l for l,u in fibers.values())
assert M==Q(91,10)
assert [k for k,(l,u) in fibers.items() if u>l and
        sum(b-a for j,(a,b) in fibers.items() if j<k)<=M/2 and
        sum(b-a for j,(a,b) in fibers.items() if j>k)<=M/2]==[2]
assert Q(101,40)==(Q(2)+Q(61,20))/2
assert Q(61,40)==Q(61,20)/2

def above(s,t):
    return [max(Q(0),min(u-l,u-(s*k+t))) for k,(l,u) in fibers.items()]
def below(s,t):
    return [max(Q(0),min(u-l,s*k+t-l)) for k,(l,u) in fibers.items()]
right=above(Q(-1,2),Q(121,40))
left=below(Q(4),Q(-437,80))
assert right==[0,0,Q(41,40),0,0]
assert left==[0,0,Q(203,80),Q(61,40),0]
q=2*sum(right)/M
B=1-2*sum(left)/M
A=q-B
assert q==Q(41,182)
assert B==Q(39,364)
assert A==Q(43,364)

h=Q(41,80)
edges=[Q(-1,40)+j*h for j in range(7)]
assert edges[4]==Q(81,40)
assert edges[5]==Q(203,80)
assert edges[6]==Q(61,20)
bound=q+sum(A**j/B**(j-1) for j in range(2,6))
assert bound==Q(50046773,60149466)<1
assert 1-bound==Q(10102693,60149466)
assert q<Q(1,4) and A<Q(1,8) and A/B<Q(10,9)
assert Q(1,4)+Q(1,8)*sum(Q(10,9)**k for k in range(1,5))==Q(5939,6561)<1
print('Any-log-concave-shadow obstruction: all exact checks passed.')
