---
fact_id: d1d2a1ae4e4d0bd6
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3cq-actual-discrete-depth-logconcavity-closure-test
depends_on: ["01a4100542206b94","c16327a288b708bd"]
verifier_run: c085cc4410814248
target_match: null
---

## Statement

Let \(N=2\), let \(P=\operatorname{conv}\{(0,0),(4,1),(1,4)\}\), and let \(D=P\cap\mathbb Z^2\). This support is complete and has eleven points. Give it the original root law \(p_{\mathbf z}=1/11\) for \(\mathbf z\in D\), with \(p_{\mathbf z}=0\) elsewhere. This is the log-affine law with parameter \(\boldsymbol\theta=\mathbf0\); both exponential coordinate parameters are the rational number one.

Use the actual closed-halfspace depth and original-law moment
\[
\tau_p(\mathbf z)
=\inf_{\substack{H\subset\mathbb R^2\text{ a closed halfspace}\\\mathbf z\in H}}
\sum_{\mathbf u\in D\cap H}p_{\mathbf u},
\qquad
M_3(p)=\sum_{\mathbf z\in D}p_{\mathbf z}\tau_p(\mathbf z)^3.
\]
The actual minima satisfy
\[
\bigl(\tau_p((0,0)),\tau_p((1,1)),\tau_p((2,2))\bigr)
=\frac1{11}(1,2,5).
\]
Consequently the table equal to \(\tau_p\) on \(D\) and zero on \(\mathbb Z^2\setminus D\) has no finite-valued globally log-concave extension to \(\mathbb R^2\), even if agreement at zero lattice values is dropped.

Moreover, the table \(\mathbf z\mapsto p_{\mathbf z}\tau_p(\mathbf z)^3\) and its normalized law \(\widetilde p_{\mathbf z}=p_{\mathbf z}\tau_p(\mathbf z)^3/M_3(p)\), zero off \(D\), have no such extension. Here \(M_3(p)\) and every occurrence of \(\tau_p\) retain the original uniform root law \(p\); no depth is recomputed for \(\widetilde p\). All cap cardinalities below are unnormalized masses, and division by eleven gives their masses under \(p\).

In contrast, every nonzero erosion table \(r_s(\mathbf z)=\min\{p_{\mathbf z},(\tau_p(\mathbf z)-s)_+\}\), extended by zero, has a globally log-concave extension by accepted fact `01a4100542206b94`. Thus the counterexample distinguishes actual depth from erosion rather than contradicting that predecessor.

## Proof

The triangle has the exact description \(P=\{(u,v):u\le4v,\ v\le4u,\ u+v\le5\}\). The first two inequalities imply \(u,v\ge0\), and the three boundary intersections are exactly the stated vertices. For integer \(v\), its horizontal census is

| \(v\) | All integer \(u\) in \(P\) |
| --- | --- |
| \(0\) | \(0\) |
| \(1\) | \(1,2,3,4\) |
| \(2\) | \(1,2,3\) |
| \(3\) | \(1,2\) |
| \(4\) | \(1\) |

Number these points as follows; the numbering is only an index for the finite trace certificates.

| \(i\) | \(\mathbf z_i\) |
| --- | --- |
| \(1\) | \((0,0)\) |
| \(2\) | \((1,1)\) |
| \(3\) | \((1,2)\) |
| \(4\) | \((1,3)\) |
| \(5\) | \((1,4)\) |
| \(6\) | \((2,1)\) |
| \(7\) | \((2,2)\) |
| \(8\) | \((2,3)\) |
| \(9\) | \((3,1)\) |
| \(10\) | \((3,2)\) |
| \(11\) | \((4,1)\) |

Since the three vertices belong to \(D\), one has \(\operatorname{conv}(D)=P\) and hence \(D=\operatorname{conv}(D)\cap\mathbb Z^2\). The function \(\mathbf1_P/11\) is globally log-concave and matches the original law at every lattice point, including its zeros. This checks the extension hypothesis for the application of `01a4100542206b94` in the statement.

For a center \(\mathbf z_j\) and nonzero normal \(\mathbf a\), write \(H_{\mathbf z_j,\mathbf a}=\{\mathbf u:\mathbf a\cdot(\mathbf u-\mathbf z_j)\ge0\}\). Accepted fact `c16327a288b708bd`, part 1, applies to this finite positive law: the actual minimum is attained by such a cap with no other point on its boundary. It therefore suffices to check all generic normal chambers through each of \(\mathbf z_1,\mathbf z_2,\mathbf z_7\). This is a reduction of the actual infimum over all closed halfspaces, not a restriction to one chosen direction.

A normal is nongeneric precisely when it is perpendicular to some nonzero difference \(\mathbf z_i-\mathbf z_j\). Taking both primitive integer perpendicular directions for each such difference gives the following lists. In each row, the listed vectors followed by their negatives in the same order form the complete counterclockwise cyclic list of critical rays.

| Center index \(j\) | First half of the cyclic critical-ray list |
| --- | --- |
| \(1\) | \((-1,4),(-1,3),(-1,2),(-2,3),(-1,1),(-3,2),(-2,1),(-3,1),(-4,1)\) |
| \(2\) | \((1,0),(0,1),(-1,2),(-1,1),(-2,1)\) |
| \(7\) | \((1,0),(2,1),(1,1),(1,2),(0,1),(-1,1)\) |

Every consecutive pair in each full cyclic list has positive determinant, so its angular gap is strictly less than \(\pi\). The sum of the two adjacent rays lies inside the corresponding open chamber. The table below uses these sums for the first half of the chambers. Their negatives represent every remaining chamber. Within a chamber, all noncentral dot-product signs are constant. The displayed traces follow by the integer dot products \(\mathbf a\cdot(\mathbf z_i-\mathbf z_j)\); none vanishes for \(i\ne j\).

For every displayed generic cap, its opposite-normal cap has trace \((\{1,\ldots,11\}\setminus\{i:\mathbf z_i\in H_{\mathbf z_j,\mathbf a}\})\cup\{j\}\). Its cardinality is therefore twelve minus the displayed cardinality. Thus the trace column and this complement rule specify every generic trace, not merely its size.

| Center \(j\) | Normal \(\mathbf a\) | All indices in \(D\cap H_{\mathbf z_j,\mathbf a}\) | Cardinality | Opposite-normal cardinality |
| --- | --- | --- | --- | --- |
| \(1\) | \((-2,7)\) | \(1,2,3,4,5,6,7,8,9,10\) | \(10\) | \(2\) |
| \(1\) | \((-2,5)\) | \(1,2,3,4,5,6,7,8,10\) | \(9\) | \(3\) |
| \(1\) | \((-3,5)\) | \(1,2,3,4,5,7,8,10\) | \(8\) | \(4\) |
| \(1\) | \((-3,4)\) | \(1,2,3,4,5,7,8\) | \(7\) | \(5\) |
| \(1\) | \((-4,3)\) | \(1,3,4,5,8\) | \(5\) | \(7\) |
| \(1\) | \((-5,3)\) | \(1,3,4,5\) | \(4\) | \(8\) |
| \(1\) | \((-5,2)\) | \(1,4,5\) | \(3\) | \(9\) |
| \(1\) | \((-7,2)\) | \(1,5\) | \(2\) | \(10\) |
| \(1\) | \((-3,-3)\) | \(1\) | \(1\) | \(11\) |
| \(2\) | \((1,1)\) | \(2,3,4,5,6,7,8,9,10,11\) | \(10\) | \(2\) |
| \(2\) | \((-1,3)\) | \(2,3,4,5,7,8,10\) | \(7\) | \(5\) |
| \(2\) | \((-2,3)\) | \(2,3,4,5,7,8\) | \(6\) | \(6\) |
| \(2\) | \((-3,2)\) | \(1,2,3,4,5,8\) | \(6\) | \(6\) |
| \(2\) | \((-3,1)\) | \(1,2,3,4,5\) | \(5\) | \(7\) |
| \(7\) | \((3,1)\) | \(7,8,9,10,11\) | \(5\) | \(7\) |
| \(7\) | \((3,2)\) | \(5,7,8,9,10,11\) | \(6\) | \(6\) |
| \(7\) | \((2,3)\) | \(4,5,7,8,10,11\) | \(6\) | \(6\) |
| \(7\) | \((1,3)\) | \(4,5,7,8,10\) | \(5\) | \(7\) |
| \(7\) | \((-1,2)\) | \(3,4,5,7,8\) | \(5\) | \(7\) |
| \(7\) | \((-2,1)\) | \(1,2,3,4,5,7,8\) | \(7\) | \(5\) |

The exhaustive minima in the two cardinality columns are respectively one, two, and five. They are attained, for example, by normals \((-3,-3)\) at \(\mathbf z_1\), \((-1,-1)\) at \(\mathbf z_2\), and \((3,1)\) at \(\mathbf z_7\). Dividing by eleven proves all three asserted actual cap minima. In particular the value at \(\mathbf z_7\) is a lower bound against every admissible cap as well as an attained upper bound.

The same finite certificate admits the following independent exact audit. SageMath version 10.8 was used; the command below exited zero and printed `ALL_EXACT_CHECKS_PASSED`. Its inputs are integer coordinates and rational polyhedral data. It recomputes the complete critical-ray sets and all generic cap sizes, without floating-point angles or optimization statuses.

```sh
sage --nodotsage --python - <<'PY'
from sage.all import Polyhedron, QQ
from math import gcd
D=((0,0),(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1))
P=Polyhedron(vertices=[(0,0),(4,1),(1,4)],base_ring=QQ)
assert set(D)==set(tuple(map(int,z)) for z in P.integral_points())
rays={1:[(-1,4),(-1,3),(-1,2),(-2,3),(-1,1),(-3,2),(-2,1),(-3,1),(-4,1)],
      2:[(1,0),(0,1),(-1,2),(-1,1),(-2,1)],
      7:[(1,0),(2,1),(1,1),(1,2),(0,1),(-1,1)]}
for j in rays:
    z=D[j-1]
    full=rays[j]+[(-a,-b) for a,b in rays[j]]
    actual=set()
    for w in D:
        if w==z: continue
        a,b=w[0]-z[0],w[1]-z[1]
        g=gcd(abs(a),abs(b))
        actual.update([(-b//g,a//g),(b//g,-a//g)])
    assert actual==set(full)
    sizes=[]
    for u,v in zip(full,full[1:]+full[:1]):
        assert u[0]*v[1]-u[1]*v[0]>0
        normal=(u[0]+v[0],u[1]+v[1])
        dots=[normal[0]*(w[0]-z[0])+normal[1]*(w[1]-z[1]) for w in D]
        assert all(t!=0 for k,t in enumerate(dots,1) if k!=j)
        sizes.append(sum(t>=0 for t in dots))
    assert min(sizes)=={1:1,2:2,7:5}[j]
assert (QQ(2)/11)**2 < (QQ(1)/11)*(QQ(5)/11)
print('ALL_EXACT_CHECKS_PASSED')
PY
```

Finally, \(\mathbf z_2=(\mathbf z_1+\mathbf z_7)/2\), and \(\mathbf z_1,\mathbf z_7\) have the same coordinatewise parity. Any global log-concave extension agreeing at these three sites would require
\[
\tau_p(\mathbf z_2)^2\ge\tau_p(\mathbf z_1)\tau_p(\mathbf z_7),
\qquad\text{whereas}\qquad
\frac4{121}<\frac5{121}.
\]
This is a violation for the actual depth table itself.

Since \(\tau_p(\mathbf z)\ge p_{\mathbf z}>0\) on \(D\), the original-law moment \(M_3(p)\) is positive. For the normalized depth-weighted law the three values are \((\widetilde p_{\mathbf z_1},\widetilde p_{\mathbf z_2},\widetilde p_{\mathbf z_7})=(1,8,125)/(11^4M_3(p))\). Its required midpoint inequality would give \(8^2\ge1\cdot125\), contradicted by \(64<125\). The common positive normalization cancels, so the unnormalized depth-weighted table fails as well. Neither calculation is a midpoint-operator marginal or a fixed-normal cumulative-cap table.

## External sources

none
