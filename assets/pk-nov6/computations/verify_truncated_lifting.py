from fractions import Fraction as Q

r=Q(1,10)
eps=r**4
gamma=Q(4,5)**4
beta=(1+eps)/(1+2*eps)
beta_padded=beta/2
volume_T=Q(1,24)
mass=2*(1+2*eps)*volume_T
tau=gamma*(1+eps)
assert beta==Q(10001,10002)
assert beta_padded==Q(10001,20004)<Q(1,2)
assert gamma*beta_padded*mass==tau*volume_T
assert tau==Q(160016,390625)
assert tau<(1-r)**4
assert tau>2*eps
a=Q(8000199,10**7)
b=Q(7999223,10**7)
assert tau-a**4==Q(2032792963819263760799,10**28)>0
assert tau-2*eps-b**4==Q(664183074753367294559,10**28)>0
assert 4*a+b-4==Q(19,10**7)>0
assert gamma*beta_padded>gamma/4
print('Binary-padding truncated-lifting counterexample: exact arithmetic passed.')
