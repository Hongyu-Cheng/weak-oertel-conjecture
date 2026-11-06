---
fact_id: 5967de7b4fedb5fd
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: balanced-cap-bounded-stopping-no-go
depends_on: ["51ff186e1aaeaa85"]
verifier_run: 4b0b098f94ff4d46
target_match: null
---

## Statement

For a compact full-dimensional convex body \(K\subseteq\mathbb R\times\mathbb R\), write

\[
K_z:=\{x\in\mathbb R:(z,x)\in K\},
\qquad
a_z(K):=\operatorname{vol}_1(K_z).
\]

Call \(B\) a legal balanced-cap descendant of \(K\) if the following conditions hold. The positive-volume lattice support \(E(K):=\{z\in\mathbb Z:a_z(K)>0\}\) has a length-weighted \(2^{-1}\)-centerpoint \(m\in\mathbb Z\cap\operatorname{conv}E(K)\), its half-mass complete core

\[
\bigcap_{\lambda\in\Lambda_m(E(K))}
\sum_{z\in E(K)}\lambda_z
\mathsf M_{a_z(K)/2}(K_z)
\]

is empty, one chooses any support-minimal negative balanced family, any positive balancing weights, and any exact affine linear-programming minorants allowed in accepted fact \(51ff186e1aaeaa85\), and \(B\subseteq K\) is the same-base weighted Minkowski descendant constructed in equations (5)--(7) of that fact. Choices at different iterations may depend arbitrarily on the entire preceding chain. Between iterations one may apply any invertible fiber-preserving affine normalization

\[
(t,x)\longmapsto(t,sx+ct+b),
\qquad s\ne0,
\]

and may also interchange the two outer base points \(t=-1\) and \(t=1\).

For every integer \(L\ge1\), put

\[
r_L:=8^{-(L+2)}
\]

and define

\[
C_L:=
\left\{(t,x):-1\le t\le1,
\quad 0\le x\le1-(1-r_L)|t|\right\}.
\tag{1}
\]

Then \(C_L\) is a compact full-dimensional convex body whose positive-volume lattice fibers are

\[
(C_L)_0=[0,1],
\qquad
(C_L)_{-1}=(C_L)_1=[0,r_L].
\tag{2}
\]

Starting from \(K^{(0)}=C_L\), consider any adaptive chain in which \(K^{(j+1)}\) is any legal balanced-cap descendant of \(K^{(j)}\), followed if desired by any of the affine normalizations above. For every \(0\le j\le L\):

1. \(E(K^{(j)})=\{-1,0,1\}\), and \(0\) is its unique length-weighted \(2^{-1}\)-centerpoint;
2. the half-mass complete core of \(K^{(j)}\) at \(0\) is empty;
3. there is a fiber-preserving affine coordinate in which

\[
K^{(j)}_0=[0,1],
\qquad
K^{(j)}_{\pm1}\subseteq[-\varepsilon_j,\varepsilon_j],
\qquad
\varepsilon_j\le8^j r_L<\frac18.
\tag{3}
\]

Consequently, no finite integer \(N\), independent of the body and of the adaptive choices, can guarantee that \(N\) iterations of the support-minimal balanced-cap descendant operation reach the nonempty half-mass-core branch.

This is only a no-go theorem for cap descent alone. In the original body \(C_L\), the point \((0,1/2)\) has mixed halfspace depth at least \(1/2\), while

\[
W(C_L)=1+2r_L.
\tag{4}
\]

Thus

\[
h_{\max}(C_L)\ge\frac12
=\frac{1}{1+2r_L}\,2^{-1}W(C_L),
\tag{5}
\]

so the family is rescued by its heavy center fiber and does not disprove weak Oertel.

## Proof

We first record affine equivariance, which is what makes the quantifier over normalizations harmless. Let

\[
F(t,x)=(t,sx+ct+b),\qquad s\ne0.
\]

Lebesgue measure in every fiber is multiplied by the same factor \(|s|\), so the weighted-centerpoint condition is unchanged. Pushforward of admissible half-mass densities gives

\[
\mathsf M_{a_z(FK)/2}((FK)_z)
=F_z\bigl(\mathsf M_{a_z(K)/2}(K_z)\bigr),
\qquad F_z(x)=sx+cz+b.
\tag{6}
\]

Hence emptiness of the complete core is invariant. A cap inequality

\[
vx\ge\ell(t)
\]

is carried to

\[
\frac{v}{s}y\ge
\ell(t)+\frac{v}{s}(ct+b).
\tag{7}
\]

The new right side is affine in \(t\). The transformation in (7) is a bijection between exact affine minorants before and after applying \(F\). It preserves positive balance because every continuous normal is multiplied by \(1/s\), and the added affine terms cancel after summing with balanced weights. It also preserves negativity of the balanced certificate and support-minimality. Finally, since the balance weights sum to one,

\[
F_z\left(\sum_i\theta_i x_i\right)
=\sum_i\theta_iF_z(x_i).
\tag{8}
\]

Thus the descendant construction in accepted fact \(51ff186e1aaeaa85\) commutes with \(F\). It is therefore enough at each iteration to prove the claimed invariant in one convenient affine fiber coordinate. Any normalization made by the chain can be conjugated away, and interchanging the two outer base points changes nothing.

We prove a one-step invariant. Suppose \(K\) is a full-dimensional convex body with

\[
E(K)=\{-1,0,1\},
\qquad
K_0=[0,1],
\qquad
K_{\pm1}\subseteq[-\varepsilon,\varepsilon],
\qquad
0<\varepsilon<\frac18.
\tag{9}
\]

The two outer fibers have positive lengths at most \(2\varepsilon\), whereas the center fiber has length one. The point \(0\) is a weighted \(1/2\)-centerpoint: every closed halfline containing \(0\) contains the whole center fiber and hence mass at least one, while the total mass is at most \(1+4\varepsilon<3/2\). It is the unique lattice centerpoint in the convex hull of the support. Indeed, the halfline \((-\infty,-1]\) shows that \(-1\) is not a centerpoint, because it contains mass at most \(2\varepsilon<1/2\le W(K)/2\); the symmetric halfline excludes \(1\).

Put

\[
D_z:=\mathsf M_{a_z(K)/2}(K_z).
\]

For the center interval,

\[
D_0=\left[\frac14,\frac34\right].
\tag{10}
\]

This follows directly by filling the leftmost or rightmost half of \([0,1]\); the standard rearrangement inequality shows that these are the minimum and maximum possible centroids of a density bounded by one and having mass \(1/2\). Also \(D_{\pm1}\subseteq K_{\pm1}\subseteq[-\varepsilon,\varepsilon]\). The barycentric representation of \(0\) that assigns weight \(1/2\) to each outer base point gives

\[
\frac12D_{-1}+\frac12D_1
\subseteq[-\varepsilon,\varepsilon].
\]

This set is disjoint from \(D_0\), so the half-mass complete core is empty.

We next analyze every legal cap choice. In the order \((-1,0,1)\),

\[
\Lambda_0(E(K))
=\{(q,1-2q,q):0\le q\le1/2\}.
\tag{11}
\]

For a direction \(v\in\mathbb R\), let \(h_z(v)=\max_{x\in D_z}vx\) and let

\[
\phi(v)=\min_{\lambda\in\Lambda_0(E(K))}
\sum_z\lambda_zh_z(v).
\]

The objective is affine in \(q\), so its minimum occurs at an endpoint of (11). From (10) and \(D_{\pm1}\subseteq[-\varepsilon,\varepsilon]\),

\[
\phi(1)
=\frac{h_{-1}(1)+h_1(1)}2
\in[-\varepsilon,\varepsilon],
\qquad
\phi(-1)=-\frac14.
\tag{12}
\]

For the first equality, the outer average is at most \(\varepsilon<3/4=h_0(1)\). For the second, the outer average is at least \(-\varepsilon>-1/4=h_0(-1)\).

Because the continuous dimension is one, every support-minimal balanced family supplied by accepted fact \(51ff186e1aaeaa85\) has exactly two nonzero normals. Positive balance forces them to have opposite signs. Relabel and write

\[
v_+=u>0,
\qquad
v_-=-w<0,
\qquad
\theta v_++(1-\theta)v_-=0,
\quad 0<\theta<1.
\tag{13}
\]

Positive homogeneity gives \(\phi(u)=u\phi(1)\) and \(\phi(-w)=w\phi(-1)\). Every legal exact affine minorant satisfies \(\ell_+(0)=\phi(u)\) and \(\ell_-(0)=\phi(-w)\), regardless of its slope. Consequently its two cap sections in the center fiber are forced to be

\[
A_{+,0}=[a,1],
\qquad
A_{-,0}=\left[0,\frac14\right],
\qquad
a:=\max\{0,\phi(1)\}\in[0,\varepsilon].
\tag{14}
\]

No choice of the two normal magnitudes, the balancing weight \(\theta\), or the affine-minorant slopes changes (14).

Let \(B\) be the descendant. Its center fiber is the interval

\[
B_0
=\theta[a,1]+(1-\theta)\left[0,\frac14\right]
=[\alpha,\beta],
\tag{15}
\]

where

\[
0\le\alpha=\theta a\le\varepsilon,
\qquad
\beta-\alpha
=\theta(1-a)+\frac{1-\theta}{4}
\ge\frac14.
\tag{16}
\]

For \(z=\pm1\), every cap section \(A_{i,z}\) is a subset of the convex interval \(K_z\). Therefore

\[
B_z=\theta A_{+,z}+(1-\theta)A_{-,z}
\subseteq K_z
\subseteq[-\varepsilon,\varepsilon].
\tag{17}
\]

Accepted fact \(51ff186e1aaeaa85\) also guarantees that \(B\) is full-dimensional and that all three of these lattice fibers retain positive volume, so its positive lattice support is still \(\{-1,0,1\}\).

Normalize the continuous coordinate by

\[
y=\frac{x-\alpha}{\beta-\alpha}.
\tag{18}
\]

Then the center fiber becomes \([0,1]\). For \(x\in B_{\pm1}\), equations (16)--(17) give

\[
|y|
\le\frac{|x|+|\alpha|}{\beta-\alpha}
\le\frac{2\varepsilon}{1/4}
=8\varepsilon.
\tag{19}
\]

Thus every legal descendant of a body satisfying (9), after an affine fiber identification, satisfies the same invariant with

\[
\varepsilon_{\mathrm{new}}\le8\varepsilon.
\tag{20}
\]

This proof used only exactness of the minorants at \(0\), not their slopes, and treated every \(u,w>0\) and every \(0<\theta<1\). Together with affine equivariance, (20) has all the asserted adaptive and normalization quantifiers.

The body in (1) is compact, convex, and full-dimensional because its upper profile \(1-(1-r_L)|t|\) is positive and concave on \([-1,1]\). Its lattice fibers are exactly (2), so it satisfies (9) with \(\varepsilon_0=r_L\). Inductively applying (20) gives

\[
\varepsilon_j\le8^jr_L
=8^{j-L-2}
\le8^{-2}
<\frac18
\qquad(0\le j\le L).
\tag{21}
\]

At every stage, the argument preceding (10) proves that \(0\) is the unique weighted lattice centerpoint and that its half-mass core is empty. This closes the induction and proves (3). Since \(L\) was arbitrary, a universal finite stopping time is impossible.

Finally, let \(p=(0,1/2)\in C_L\). The section at base \(0\) of any closed ambient halfspace containing \(p\) is either all of \(\mathbb R\) or a closed halfline containing \(1/2\). Its intersection with \([0,1]\) has length at least \(1/2\). All other fiber contributions are nonnegative, so \(h_S(p)\ge1/2\). Equation (2) gives \(W(C_L)=1+2r_L\), proving (4)--(5). Hence the obstruction concerns finite stopping of the cap descent mechanism, not the locked conjecture.

## External sources

none
