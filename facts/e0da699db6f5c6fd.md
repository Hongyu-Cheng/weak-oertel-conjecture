---
fact_id: e0da699db6f5c6fd
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-forced-split-positive-volume-crease-fibers
depends_on: []
verifier_run: f84202ae5f5160ae
target_match: null
---

## Source

- [3b257d8ddacb6167](../candidates/3b257d8ddacb6167.json), 3b257d8ddacb6167:07 §7, (19)–(20), explicit two-row crease-fiber obstruction.
- [f1e67b1b6817e2f9](../candidates/f1e67b1b6817e2f9.json), f1e67b1b6817e2f9:03 §6, (12)–(18), rational roof, rows and exact quota enumeration.

## Statement

Let $P=\{-1,0,1,2\}\times\{-1,0,1\}$, $q(z)=2z_1+z_2-1$, and $\ell(z)=5-|q(z)|$. Take centered interval fibers $K_z=[-V_z/2,V_z/2]$ with lengths in lexicographic order
$$
(V_z)_z=(2,2,2,136,203,270,270,203,136,2,2,2)/1230 .
$$
Their hull is compatible and canonical, has mixed mass $M=1$, and every nonempty proper closed minor $T=P\cap\operatorname{conv}T$ has $\sum_{z\in T}V_z<k(T)/4$, where $k(T)$ counts its occupied parities. For the two marks $Y_0=((0,0),0)$ and $Y_1=((1,0),0)$ there is a full-space contact martingale from $(\delta_{Y_0}+\delta_{Y_1})/8$ to $dm/\ell$, with $\ell$-integral $1/2$ in each row. In every such contact martingale both rows take positive mass from each of the complete crease fibers at $(0,1)$ and $(1,-1)$, of length $9/41$ each. The first row takes fractions $151/162$ and $11/162$ of their respective target masses. In particular no partition assigning each whole sampled fiber to one contacting row can realize the martingale. The continuous allocations can be nonunique. Geometrically normalizing $\ell$ rescales both tilted marginals by the same factor and preserves the fractions and original-volume weights.

## Proof

The concave length roof on the base rectangle is
$$
V(z)=\min(270+67q(z),270-67q(z),270+268z_1,538-268z_1)/1230.
$$
Its four affine pieces from left to right are the triangles with vertex lists
$$
((-1,-1),(-1,1),(0,1)),\quad ((-1,-1),(0,1),(1,-1)),\quad
((0,1),(1,-1),(2,1)),\quad ((1,-1),(2,-1),(2,1)).
$$
They tile the rectangle. At their vertices the corresponding planes are respectively the third, first, second and fourth listed planes and equal the minimum. Affine inequalities then give the same equality throughout each triangle. This also verifies the listed heights at sampled sites by substitution. The roof interpolates centered intervals by Minkowski sums on the triangles, and its positive minimum on the rectangle is at least $2/1230$ since each affine term is at least that large. Thus the entire real-base family is the canonical hull of the sampled intervals. The lengths sum to one.

For reproducibility, the finite quota enumeration uses the following exact predicate. A point $q$ of the sampled base belongs to the hull of a nonempty subset $T$ iff it belongs to $T$, lies between two points of $T$ on their line, or lies in one nondegenerate triangle with vertices in $T$, by planar Carathéodory. For the segment test require $\det(b-a,q-a)=0$ and $(q-a)\cdot(q-b)\le0$. For the triangle test orient the three vertices counterclockwise by the sign of $\det(b-a,c-a)$ and require all three oriented edge determinants with $q$ to be nonnegative. The enumeration is the following integer loop.
```text
for each mask from 1 through (1 << |P|) - 2:
    T = the points of P selected by the mask
    if any q in P outside T passes the segment or triangle test for T:
        continue
    k = number of distinct (z_1 mod 2, z_2 mod 2) for z in T
    count[k] += 1
    minimum[k] = min(minimum[k], integer quota slack of T)
```

Here the integer slack is $1230k-4\sum_{z\in T}1230V_z$. The loop retains 704 masks, and the minima by $k=1,2,3,4$ are $(150,24,166,8)$. These are all positive. The integer loop and those values are also implemented in the source calibration verifier.

On the ordered targets $(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1)$ put first-row masses
$$
(24,12,8,544,609,604,44)/14760.
$$
Use the reflection $z\mapsto(1-z_1,-z_2)$ for the second row. Spread each listed mass uniformly on its corresponding interval. The first row has mass $1845/14760=1/8$, zero base first moments by the list, and zero continuous first moment by centering. Reflection gives the second barycenter. On each strict side the listed mass equals $V_z/\ell(z)$. At each crease their two masses sum to $648/14760=(9/41)/5$. Thus their sum is $dm/\ell$. The contacting planes are $5+q$ and $5-q$ respectively, so affine Jensen gives each row $\ell$-integral $(1/8)4=1/2$.

For any coupling with these source and target marginals and the martingale property, the $\ell$-integrals of the two marginals are both one. Concave Jensen is therefore an equality row by row, so a row is supported on the contact of its source plane. The strict-side fibers are forced to the corresponding rows. The first row has strict-side base moments $-44/14760$ and $-560/14760$. If its remaining two masses on $(0,1),(1,-1)$ are $a,b$, the two moment equations are $b=44/14760$ and $a-b=560/14760$. Dividing by $648/14760$ gives the stated positive fractions, each less than one. Allocating to that row a centered subinterval of the prescribed length fraction and to the other its symmetric complement also preserves both row masses and continuous means. It differs from uniform splitting. Multiplication by a common positive constant preserves the plane contacts and rescales the inverse-density marginals inversely. This gives the asserted normalization rule.
