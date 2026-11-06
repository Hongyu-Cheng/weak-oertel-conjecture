from fractions import Fraction as Q
A=Q(115,243);B=Q(128,243);L=Q(256,243);tau=Q(6,25)
assert A+B==1 and L/2==B
assert A<2*tau and A>tau
assert B*Q(27,40)**2==tau
assert tau<Q(1,4)
# All caps assigned to one fiber exclude the other fiber strictly.
assert 1>tau and L-2<A-tau
assert 0<Q(53,40) and A/L<Q(93,40) and 1<Q(93,40)
# Equal triangle caps cover strictly, and their standard interior witnesses
# are exclusive because 4/5>13/40>1/10.
assert 3*Q(13,40)<1 and Q(4,5)>Q(13,40)>Q(1,10)
T=B*Q(1,40)**2
E0=2*A-2*tau;E1=2*B-3*tau+T;E=E0+E1
assert T==Q(2,6075)
assert E0==Q(2834,6075) and E1==Q(2028,6075)
assert E==Q(4862,6075)
assert E-3*tau==Q(488,6075)>0
print('Exact five-cap counterexample verified.')
