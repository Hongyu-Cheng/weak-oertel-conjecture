from fractions import Fraction as Q

outer_edges=[Q(-5,4),Q(-3,4),Q(-1,4),Q(1),Q(5,4)]
outer_dens=[Q(2,7),Q(9,28),Q(67,140),Q(11,28)]
q_edges=[Q(0)]
for i,d in enumerate(outer_dens):
    q_edges.append(q_edges[-1]+d*(outer_edges[i+1]-outer_edges[i]))
assert q_edges==[Q(0),Q(1,7),Q(17,56),Q(101,112),Q(1)]
left_images=[2*t-(q-Q(1,2)) for t,q in zip(outer_edges,q_edges)]
assert left_images==[Q(-2),Q(-8,7),Q(-17,56),Q(179,112),Q(2)]
assert [2/d-1 for d in outer_dens]==[Q(6),Q(47,9),Q(213,67),Q(45,11)]
assert all(2/d-1>=1 for d in outer_dens)

# Source marginals of the two central pair maps.
w1,w2=Q(11,14),Q(3,14)
assert w1+w2==1
assert w2/6==Q(1,28)
assert w1/5+w2/6==Q(27,140)
assert w1/2==Q(11,28)
assert w2/Q(5,2)==Q(3,35)
assert (w1+w2)*Q(1,2)==Q(1,2)

# Central source usage is exactly Lebesgue measure on B.
assert Q(27,28)+Q(1,28)==1
assert Q(113,140)+Q(27,140)==1
singles_mass=Q(1,2)+Q(1,2)*Q(27,28)+Q(5,2)*Q(113,140)
assert singles_mass==3
central_pair_source_mass=1
assert singles_mass+central_pair_source_mass==4

# The five pieces sum to the same target density.
rows=[(Q(2,7),Q(1),Q(0)),
      (Q(9,28),Q(27,28),Q(0)),
      (Q(67,140),Q(113,140),Q(0)),
      (Q(11,28),Q(113,140),Q(3,35)),
      (Q(0),Q(113,140),Q(11,28)+Q(3,35))]
assert all(sum(row)==Q(9,7) for row in rows)
target_mass=Q(9,7)*(Q(9,4)-Q(-5,4))
assert target_mass==Q(9,2)==1+Q(1,2)+singles_mass
assert 9/target_mass==2
assert (Q(-5,4)+Q(9,4))/2==Q(1,2)
print('All rational three-fiber barycentric transport identities passed.')
