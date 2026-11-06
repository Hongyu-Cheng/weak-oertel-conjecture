"""Exact rational diagnostic for the finite path; the Markdown supplies proof."""
from fractions import Fraction as F

checks = 0

def tail(length, threshold):
    return min(length, max(F(0), length / 2 - threshold))

def pair(a, b, x):
    # The clipped pair sum is piecewise affine in its first threshold.
    cuts = [-a / 2, a / 2, 2*x-b/2, 2*x+b/2]
    return min(tail(a, t) + tail(b, 2*x-t) for t in cuts)

def direct_beta(a, b, U, s):
    # Breakpoints of the two continuous, piecewise affine middle bounds,
    # together with their exact crossing on every affine subinterval.
    lo, hi = s-U/2, s+U/2
    cuts = sorted({lo, hi, *[v for v in
        [(b-a)/4, (a+b)/4, -(b-a)/4, -(a+b)/4]
        if lo <= v <= hi]})
    def values(x):
        return U/2+s-x+pair(a,b,x), U/2-s+x+pair(a,b,-x)
    candidates = set(cuts)
    for l, r in zip(cuts, cuts[1:]):
        pl, ql = values(l)
        pr, qr = values(r)
        dl, dr = pl-ql, pr-qr
        if dl != dr and dl*dr <= 0:
            candidates.add(l+(r-l)*dl/(dl-dr))
    middle = max(min(values(x)) for x in candidates)
    return max(a/2, b/2, middle)/(a+b+U)

def path(a, b, U, s):
    # Continuous-coordinate reflection was performed before calling.
    nodes = [(a,U,s), (a,U,U/2-(a+b)/4)]
    def fw(a,U):
        if U <= b: return U/2+a
        if U <= b+2*a: return (U+b)/4+a
        return (U+a)/2
    if fw(a,U) <= b/2:
        U=b-2*a
        nodes.append((a,U,U/2-(a+b)/4))
    else:
        a=max(F(0),(b-U)/2)
        nodes.append((a,U,U/2-(a+b)/4))
    if a>0:
        a,U=F(0),b
        nodes.append((a,U,b/4))
    elif U>b:
        U=b
        nodes.append((F(0),U,b/4))
    return nodes

for b in [F(1),F(3,2),F(2)]:
  for j in range(1,11):
    a=b*j/10
    for k in range(13):
      U=(a+b)/2+b*k/6
      maxs=U/2-(a+b)/4
      for j_s in range(5):
        s=maxs*j_s/4
        nodes=path(a,b,U,s)
        prev=direct_beta(a,b,U,s)
        for left,right in zip(nodes,nodes[1:]):
          for j_t in range(1,9):
            t=F(j_t,8)
            aa,UU,ss=[(1-t)*l+t*r for l,r in zip(left,right)]
            assert aa>=0 and UU>0
            assert abs(ss)<=UU/2-(aa+b)/4
            now=direct_beta(aa,b,UU,ss)
            assert now<=prev, (left,right,t,now,prev)
            prev=now
            checks+=1
        assert nodes[-1][0]==0 and nodes[-1][1]==b
        assert prev==F(1,4)
        checks+=1

print(f"PASS: {checks} exact rational path and terminal checks")
