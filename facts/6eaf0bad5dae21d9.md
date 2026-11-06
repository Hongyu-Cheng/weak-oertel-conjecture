---
fact_id: 6eaf0bad5dae21d9
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: weighted-planar-simplex-depth-quarter
depends_on: []
verifier_run: bc1f9a13999f46c2
target_match: null
---

## Statement

Take \(d=1\),
\[
K=[-2,2]^2,\qquad z_0=(0,0),
\]
and define
\[
\begin{split}
F(x,y):=\frac1{60}\min\{&
88-38x,\;
93-5x+38y,\;
40-10y,\\
&40+10x,\;
56+18x+8y
\}.
\end{split}
\tag{1}
\]
Then \(F\) is continuous and concave on \(K\), is strictly positive
there, and
\[
D=\{z\in K\cap\mathbb Z^2:F(z)>0\}
=[-2,2]^2\cap\mathbb Z^2.
\tag{2}
\]
Put \(M(z)=F(z)\).  Its complete lattice table, scaled by \(60\), is
\[
\begin{array}{c|rrrrr}
x\backslash y&-2&-1&0&1&2\\ \hline
-2&4&12&20&20&20\\
-1&22&30&30&30&20\\
0&17&40&40&30&20\\
1&12&50&40&30&20\\
2&7&12&12&12&12
\end{array}
\tag{3}
\]
and
\[
\Delta_M(0)=\frac{74}{15}.
\tag{4}
\]
For every \(q\in\{0,1,2\}\), every affinely independent
\(v_0,\ldots,v_q\in D\), and
\[
T=\operatorname{conv}\{v_0,\ldots,v_q\}\ni0,
\]
one has
\[
\min_{0\leq i\leq q}M(v_i)\,\kappa(T,0)\leq1.
\tag{5}
\]
Equality is attained.  Since
\[
1<\frac14\Delta_M(0)=\frac{37}{30},
\tag{6}
\]
no simplex required by the registered statement exists.

## Proof

Each expression inside the minimum in (1) is affine.  A finite pointwise
minimum of affine functions is concave and continuous.  Direct
substitution at the four vertices of \(K\) gives
\[
F(-2,-2)=\frac1{15},\qquad
F(-2,2)=\frac13,\qquad
F(2,-2)=\frac7{60},\qquad
F(2,2)=\frac15.
\]
Every point of the square is a convex combination of these four
vertices, so concavity gives \(F>0\) throughout \(K\).  This proves (2).
Substitution at the twenty-five lattice points gives (3).

Any proper closed halfspace containing \(0\) can be written as
\[
Q=\{p:n\mathbin{\cdot}p\geq\beta\},
\qquad n\neq0,\quad\beta\leq0.
\]
The boundary-through-zero halfspace
\(\{p:n\mathbin{\cdot}p\geq0\}\) is contained in \(Q\).  Since all
weights are positive, the minimum defining \(\Delta_M(0)\) may therefore
be taken over boundary-through-zero halfspaces.  The halfspace
\[
Q_*=\{(x,y):-3x+2y\geq0\}
\tag{7}
\]
has scaled mass
\[
60M(Q_*)=296,
\]
so its mass is \(74/15\).  The exact enumeration below checks every
directional chamber and proves that no boundary-through-zero halfspace
has smaller mass.  This proves (4), including all closed-boundary
contributions.

It remains to prove the simultaneous all-simplex upper bound.  Because
every eligible \(T\) is contained in \(K\),
\[
T\cap\mathbb Z^2=T\cap D.
\tag{8}
\]
The exact enumeration gives the following complete certificate:
\[
\begin{array}{c|r|c|c}
\kappa&
\#\{\text{eligible simplices with this }\kappa\}&
\max_T\min_{v\in\operatorname{vert}T}M(v)&
\max_T\min_vM(v)\,\kappa\\ \hline
1&273&2/3&2/3\\
2&540&1/2&1\\
3&212&1/3&1\\
4&16&1/5&4/5\\
5&20&1/5&1
\end{array}
\tag{9}
\]
Thus there are \(1061\) eligible simplices in all, no other value of
\(\kappa\) occurs, and (5) follows.

Here is the complete standard-library verifier.  It uses only integer
arithmetic and `Fraction`; there is no floating-point geometry and no
arbitrary normal cutoff.

```python
from collections import Counter
from fractions import Fraction
from functools import cmp_to_key
from itertools import combinations
from math import gcd

D = tuple((x, y) for x in range(-2, 3) for y in range(-2, 3))
z0 = (0, 0)

def F(p):
    x, y = p
    numerators = (
        88 - 38*x,
        93 - 5*x + 38*y,
        40 - 10*y,
        40 + 10*x,
        56 + 18*x + 8*y,
    )
    return Fraction(min(numerators), 60)

M = {p: F(p) for p in D}
assert min(M.values()) > 0

def primitive(v):
    a, b = v
    g = gcd(abs(a), abs(b))
    return (a // g, b // g)

def angle_half(v):
    x, y = v
    return 0 if y > 0 or (y == 0 and x > 0) else 1

def angle_cmp(u, v):
    hu, hv = angle_half(u), angle_half(v)
    if hu != hv:
        return -1 if hu < hv else 1
    cross = u[0]*v[1] - u[1]*v[0]
    return -1 if cross > 0 else (1 if cross < 0 else 0)

def complete_normals(P):
    events = set()
    for x, y in P:
        if (x, y) != z0:
            e = primitive((y, -x))
            events.add(e)
            events.add((-e[0], -e[1]))
    events = sorted(events, key=cmp_to_key(angle_cmp))
    chambers = []
    for i, u in enumerate(events):
        v = events[(i + 1) % len(events)]
        s = (u[0] + v[0], u[1] + v[1])
        assert s != (0, 0)
        chambers.append(primitive(s))
    return tuple(events + chambers)

def dot(n, p):
    return n[0]*p[0] + n[1]*p[1]

def det(a, b, c):
    return ((b[0]-a[0])*(c[1]-a[1])
            - (b[1]-a[1])*(c[0]-a[0]))

def on_segment(p, a, b):
    return (det(a, b, p) == 0
            and (p[0]-a[0])*(p[0]-b[0])
                + (p[1]-a[1])*(p[1]-b[1]) <= 0)

def in_triangle(p, t):
    a, b, c = t
    s = det(a, b, c)
    e = (det(a, b, p), det(b, c, p), det(c, a, p))
    return s != 0 and (all(q >= 0 for q in e) if s > 0
                       else all(q <= 0 for q in e))

def planar_kappa(P):
    return min(sum(dot(n, p) >= 0 for p in P)
               for n in complete_normals(P))

depth = min(sum(M[p] for p in D if dot(n, p) >= 0)
            for n in complete_normals(D))
assert depth == Fraction(74, 15)

records = [(1, M[z0])]
for a, b in combinations(D, 2):
    if on_segment(z0, a, b):
        P = tuple(p for p in D if on_segment(p, a, b))
        u = (b[0]-a[0], b[1]-a[1])
        kappa = min(
            sum(dot(u, p) >= 0 for p in P),
            sum(dot(u, p) <= 0 for p in P),
        )
        records.append((kappa, kappa * min(M[a], M[b])))

for t in combinations(D, 3):
    if in_triangle(z0, t):
        P = tuple(p for p in D if in_triangle(p, t))
        kappa = planar_kappa(P)
        records.append(
            (kappa, kappa * min(M[p] for p in t))
        )

assert len(records) == 1061
assert Counter(k for k, score in records) == {
    1: 273, 2: 540, 3: 212, 4: 16, 5: 20
}
max_min_level = {
    k: max(score / k for kk, score in records if kk == k)
    for k in range(1, 6)
}
assert max_min_level == {
    1: Fraction(2, 3),
    2: Fraction(1, 2),
    3: Fraction(1, 3),
    4: Fraction(1, 5),
    5: Fraction(1, 5),
}
assert max(score for k, score in records) == 1
assert 1 < depth / 4 == Fraction(37, 30)
```

For completeness of the directional enumeration, for a finite planar
set \(P\) the sign vector
\[
\bigl(\operatorname{sign}(n\mathbin{\cdot}p)\bigr)_{p\in P}
\]
is constant in every open angular chamber between consecutive event
normals \(n\perp p\).  `complete_normals` includes every primitive event
normal and, for each adjacent pair, their sum, which lies strictly in
that chamber.  The event set is centrally symmetric.  For a rank-two
set adjacent events cannot be opposite, so the asserted sum is nonzero.
Thus every open-chamber sign pattern and every closed-boundary event
pattern occurs in the finite list.  Rank-one simplices are handled
separately by their two closed rays.  This proves that (9) uses the
literal definition of \(\kappa\), counts every lattice point of \(T\),
and covers proper faces and closed boundary points.

GENUINE CONVEX-BODY REALIZATION
Define
\[
C:=\{(z,s)\in K\times\mathbb R:|s|\leq F(z)\}.
\tag{10}
\]
The two inequalities \(s\leq F(z)\) and \(-s\leq F(z)\) define convex
sets because \(F\) is concave.  Thus \(C\) is convex.  It is compact and
full-dimensional because \(K\) is compact and \(F>0\) on \(K\).  Its
one-dimensional fiber is
\[
C_z=[-F(z),F(z)].
\]
The maximal absolute halfspace depth of an interval
\([-F(z),F(z)]\) is attained at its midpoint and equals \(F(z)\).
Consequently the maximal absolute fiber-depth function of \(C\) is
exactly \(M(z)=F(z)\).  Hence the counterexample is not merely an
arbitrary lattice-weight profile.

## External sources

None.
