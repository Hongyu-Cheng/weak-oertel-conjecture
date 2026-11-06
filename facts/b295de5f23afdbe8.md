---
fact_id: b295de5f23afdbe8
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3ej-planar-weighted-radius-slab-or-core
depends_on: []
verifier_run: 540a08950bfd478a
target_match: null
---

## Statement

Let \(d\ge1\) be an integer, let \(P\subset\mathbb R^2\) be nonempty, compact, and convex, and let \(r:P\to[0,\infty)\) be a finite-valued concave function. Assume
\(W:=\sum_{z\in P\cap\mathbb Z^2}r(z)^d>0\), and define
\(R:=\max_{z\in P\cap\mathbb Z^2}r(z)>0\) and
\(\delta:=1/(10000d)\). Set
\(\eta:=1/2\), \(c:=1/(3\cdot10^9)\), and \(\omega:=2^{27}\).
Then at least one of the following holds:

1. There are a primitive \(u\in\mathbb Z^2\setminus\{0\}\) and an integer \(m\) such that
\(\sum_{z\in P\cap\mathbb Z^2:\ m\le u\cdot z\le m+\omega}r(z)^d\ge\eta W\).
2. The original top-radius core satisfies
\(\sum_{z\in P\cap\mathbb Z^2:\ r(z)\ge(1-\delta)R}r(z)^d\ge cW\).

The slabs in the first conclusion have integer endpoints in a primitive integer coordinate. Every lattice point on every displayed boundary is included.

## Proof

For any bounded nonempty set \(Q\subset\mathbb R^2\), write
\(\operatorname{width}_u(Q):=\sup_{x\in Q}u\cdot x-\inf_{x\in Q}u\cdot x\) and
\(\operatorname{lw}(Q):=\inf_{u\in\mathbb Z^2\text{ primitive}}\operatorname{width}_u(Q)\).
Taking the closure preserves these widths. A bounded set contained in a line has lattice width zero: a rational line has a primitive integer normal, and for an irrational line the pigeonhole principle applied to fractional parts of multiples of its slope gives integer normals whose scalar product with its direction tends to zero. Dividing such normals by their greatest common divisors only decreases the width. Thus \(\operatorname{lw}(Q)\ge64\) for a convex \(Q\) implies that its closure is full dimensional.

We first prove the exact counting estimate
\[
\#(aQ\cap\mathbb Z^2)\le6a^2\#(Q\cap\mathbb Z^2)
\qquad(a\ge1)
\tag{1}
\]
for every bounded convex \(Q\) with \(\operatorname{lw}(Q)\ge64\); \(Q\) need not be closed. Here \(aQ=\{ax:x\in Q\}\).

Let \(K=\overline Q\), \(A=\operatorname{area}(K)\), and \(w=\operatorname{lw}(K)\ge64\). The minimum defining \(w\) is attained: a Euclidean ball of positive radius contained in \(K\) gives a lower bound proportional to \(\|u\|\) for \(\operatorname{width}_u(K)\), so only finitely many integer vectors can compete with any fixed vector. Complete a primitive minimizing vector to a unimodular integer coordinate system \((x,y)\) in which its coordinate is \(y\). Lattice points and area are preserved. Let the \(y\)-range of \(K\) be \([\alpha,\beta]\), so \(\beta-\alpha=w\), and let \(\ell(y)\) be the length of the horizontal section. Convexity makes \(\ell\) nonnegative and concave on this interval. Put \(L=\max\ell\).

Choose points of \(K\) on its bottom and top supporting lines. The segment joining them has an equation \(x=b+sy\). For any point \((x,y)\in K\), the point \((b+sy,y)\) is also in \(K\), whence \(|x-b-sy|\le\ell(y)\le L\). Choose an integer \(k\) with \(|s-k|\le1/2\). The primitive integer coordinate \(x-ky\) has width at most \(2L+w/2\). Its width is at least \(w\) by minimality. Hence \(L\ge w/4\). Concavity of the sections gives \(A\ge Lw/2\), by integrating the two line segments from a point where \(\ell=L\) to the endpoints with endpoint value zero. Consequently
\[
L\le\frac{2A}{w},\qquad A\ge\frac{w^2}{8}.
\tag{2}
\]

Extend \(\ell\) by zero off \([\alpha,\beta]\). This nonnegative function is unimodal and has total variation at most \(2L\). On each unit interval its integral is at most its value at the left integer endpoint plus its variation on that interval. Summing gives
\(\sum_{j\in\mathbb Z}\ell(j)\ge A-2L\).
Deleting the at most two integer rows equal to \(\alpha\) or \(\beta\) loses at most another \(2L\). On each remaining integer row, the open horizontal section lies in \(\operatorname{int}K\), and an open interval of length \(\ell(j)\) contains at least \(\ell(j)-1\) integers. Also \(\operatorname{int}K\subset Q\): for any point of this interior, approximate vertices of a small surrounding triangle by points of \(Q\), and use convexity. There are at most \(w+1\) relevant integer rows. Therefore (2) implies
\[
\#(Q\cap\mathbb Z^2)
\ge A-4L-(w+1)
\ge A\left(1-\frac{16}{w}-\frac8{w^2}\right)
\ge\frac A2.
\tag{3}
\]
This lower bound used interior points only, so it is valid even when \(Q\) omits some or all of its boundary.

For completeness, every compact convex \(B\) of lattice width at least one satisfies
\(\#(B\cap\mathbb Z^2)\le2\operatorname{area}(B)+2\).
If its \(N\) lattice points are not collinear, triangulate their convex hull using all of them. There are at least \(N-2\) nondegenerate triangles, each of area at least \(1/2\), since its vertex determinant is a nonzero integer. The triangle count follows by starting with a triangulation of the extreme vertices and inserting the other boundary and interior points: each insertion increases the triangle count by at least one. If the lattice points are collinear and \(N\ge2\), their extreme difference is \(hv\), where \(v\) is primitive and the integer \(h\ge N-1\). The two triangles formed with the extreme points of \(B\) in the primitive normal coordinate \((-v_2,v_1)\) lie on opposite sides of the lattice-point line and have total area \(h\operatorname{width}_{(-v_2,v_1)}(B)/2\ge(N-1)/2\). The cases \(N\le1\) are immediate. This proves the stated upper estimate without a volume-to-count assumption.

Apply it to \(aK\). Its width is at least \(64a\), and (2) gives \(A\ge512\). Together with (3),
\(\#(aQ\cap\mathbb Z^2)\le\#(aK\cap\mathbb Z^2)\le2a^2A+2\le3a^2A\le6a^2\#(Q\cap\mathbb Z^2)\), proving (1).

Choose an integer maximizer \(z_0\) of \(r\). For the remainder define \(P'=P-z_0\) and \(f(x)=r(z_0+x)/R\) on \(P'\). Thus \(f(0)=1\), and \(0\le f(x)\le1\) at every integer point of \(P'\), although no such upper bound is required away from integer points. Define the actual convex superlevels
\(Q_t:=\{x\in P':f(x)\ge1-t\}\) and their actual counts \(N_t:=\#(Q_t\cap\mathbb Z^2)\), for \(0\le t\le1\). In particular \(Q_1=P'\) and \(0\in Q_t\). Concavity at the integer peak gives the containment
\[
Q_t\subseteq(t/s)Q_s\qquad(0<s\le t\le1),
\tag{4}
\]
because for \(x\in Q_t\),
\(f((s/t)x)\ge(1-s/t)f(0)+(s/t)f(x)\ge1-s\).
This argument works at all boundary points without a continuity assumption.

The finite original weighted sum has the exact layer-cake formula
\[
\frac W{R^d}
=d\int_0^1(1-t)^{d-1}N_t\,dt.
\tag{5}
\]
Indeed, the contribution of an integer point with radius \(f(x)\) is the integral from \(1-f(x)\) to \(1\). Non-strict superlevels change no integral endpoint and retain every original boundary point.

Suppose first that \(\operatorname{lw}(Q_\delta)\ge64\). For \(t\le\delta\) we have \(N_t\le N_\delta\). For \(t\ge\delta\), (4) and (1) give \(N_t\le6(t/\delta)^2N_\delta\). Since
\(d\int_0^1t^2(1-t)^{d-1}\,dt=2/((d+1)(d+2))\), (5) yields
\[
\frac W{R^d}
\le N_\delta\left(1+\frac{12}{\delta^2(d+1)(d+2)}\right)
\le1200000001N_\delta.
\tag{6}
\]
The original top-radius-core weight divided by \(R^d\) is at least
\((1-\delta)^dN_\delta\ge(1-d\delta)N_\delta\ge N_\delta/2\), by Bernoulli's inequality. Its fraction of \(W\) is therefore at least \(1/2400000002>c\). This proves conclusion 2 in this case.

It remains to treat \(\operatorname{lw}(Q_\delta)<64\). Consider the finite dyadic levels \(t_j=\min\{2^j\delta,1\}\), stopping when the value first reaches one. If none of their superlevels has lattice width at least 64, then \(P'=Q_1\) has a primitive integer direction of width less than 64, and the whole original lattice support is contained in a slab of width \(\omega\). This proves conclusion 1.

Otherwise let \(\tau\) be the first dyadic level whose superlevel has lattice width at least 64, and let \(s\) be the preceding level. We have \(\tau>\delta\), \(\tau/s\le2\), and some primitive \(u\) with \(\operatorname{width}_u(Q_s)<64\). By (4),
\(\operatorname{width}_u(Q_\tau)<128\).
Fix this single direction \(u\), and put \(a=2^{20}\).
If \(a\tau\ge1\), (4) gives \(\operatorname{width}_u(P')\le\operatorname{width}_u(Q_\tau)/\tau<128a=\omega\), so again the whole original lattice support is captured.

Suppose \(T:=a\tau<1\). The superlevel \(Q_T\) has width less than \(128a=\omega\) in the same fixed direction. We prove that its original weight is at least \(W/2\). For \(t\ge\tau\), (4) and (1) give
\(N_t\le6(t/\tau)^2N_\tau\).
Writing \(W_{\rm out}:=R^d\sum_{x\in(P'\cap\mathbb Z^2)\setminus Q_T}f(x)^d\), the same pointwise integration as in (5), now restricted to \([T,1]\), gives
\[
\frac{W_{\rm out}}{R^d}
\le\frac{6N_\tau}{\tau^2}\,d\int_T^1t^2(1-t)^{d-1}\,dt,
\qquad
\frac W{R^d}\ge(1-\tau)^dN_\tau.
\tag{7}
\]
The integral also counts contributions from points inside \(Q_T\), which only enlarges this upper bound; hence (7) does not discard any outside point.

Put \(\rho=d\tau\ge d\delta=1/10000\). From \(a\tau<1\) and \(a/(10000d)\le a\tau\), we obtain \(d>a/10000>2\). Also \(\tau<1/a<1/2\), so \((1-\tau)^d\ge e^{-2\rho}\), while \((1-t)^{d-1}\le e^{-dt/2}\) for \(0\le t\le1\). Substituting \(v=dt\) in (7) and evaluating the elementary exponential integral yields
\[
\frac{W_{\rm out}}W
\le\frac{6e^{2\rho}}{\rho^2}\int_{a\rho}^{\infty}v^2e^{-v/2}\,dv
=6e^{-(a/2-2)\rho}\left(2a^2+\frac{8a}{\rho}+\frac{16}{\rho^2}\right).
\tag{8}
\]
For \(a=2^{20}\) and \(\rho\ge1/10000\),
\((a/2-2)\rho\ge(2^{19}-2)/10000>50\), and
\(2a^2+8a/\rho+16/\rho^2\le2a^2+80000a+1600000000<3a^2\).
Using \(e\ge2\), (8) is at most
\(18a^2e^{-50}\le18\cdot2^{40}/2^{50}=18/1024<1/2\).
Thus the original mass in \(Q_T\) is greater than \(W/2\).

Finally, in every slab case the relevant finite nonempty integer set has \(u\)-coordinate range less than the integer \(\omega\). Taking its minimum coordinate as the integer slab endpoint captures it in a closed width-\(\omega\) slab. Translating back by \(z_0\) adds the integer \(u\cdot z_0\) to that endpoint and preserves primitivity, width, all original weights, and all boundary inclusions. This proves conclusion 1 with \(\eta=1/2\), completing the alternative.

## External sources

None. The planar lattice-count estimates and the weighted tail estimate are proved above.
