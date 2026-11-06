---
fact_id: ebaad3e56b09e26c
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: mean-rounded-convex-downset-corner
depends_on: []
verifier_run: 17d30b0b138048df
target_match: null
---

## Statement

Define the rational polytope
\[
P=\{q\in\mathbb R_{\ge0}^{5}:q_1+5q_i\le10\text{ for }i=2,3,4,5\}
\]
and the actual convex body \(C=P\times[0,1]\), with integer dimension \(n=5\) and continuous dimension \(d=1\). Retain the actual-volume definitions \(C_z=\{y:(z,y)\in C\}\), \(w_z=\operatorname{vol}_1(C_z)\), \(D=\{z\in\mathbb Z^5:w_z>0\}\), \(W=\sum_z w_z\), and \(T=2^{-5}W\). In this construction, \(D=P\cap\mathbb Z^5\), \(w_z=1\) on \(D\), and \(w_z=0\) everywhere else.

For the auxiliary uniform mean and the prescribed center rule, put \(\bar z=|D|^{-1}\sum_{z\in D}z\), \(x=(3/4)\bar z\), and
\[
\begin{aligned}
J(D)&=D\cap\prod_{i=1}^{5}[\lfloor x_i\rfloor,\lceil x_i\rceil],\\
A_j&=\{u\in\mathbb Z^5:0\le u\le j,\ j+u\in D\}\qquad(j\in D).
\end{aligned}
\]
The intersection defining \(J(D)\) consists of integer points because \(D\subset\mathbb Z^5\). Every coordinate inequality is componentwise. Then
\[
|D|=166,\qquad J(D)=\{1,2\}\times\{0,1\}^{4},\qquad
\max_{j\in J(D)}|A_j-A_j|=5<\frac{83}{16}=2^{-5}|D|.
\]
Each difference set counts every distinct integer difference once, including both orientations and zero.

For every integer \(r\ge1\), the actual body \(C^{(r)}=P^r\times[0,1]\) has integer dimension \(5r\) and continuous dimension one. A superscript \((r)\) below means that the same definitions are applied to this body; it changes no weight or normalization. Its positive support is \(D^{(r)}=D^r\), and its full integer table is uniformly one there and zero elsewhere. Form its own uniform mean, three-quarter-mean vector, and rounding rectangle by the preceding definitions in dimension \(5r\). With \(A_j^{(r)}=\{u\in\mathbb Z^{5r}:0\le u\le j,\ j+u\in D^{(r)}\}\), one has
\[
\frac{\max_{j\in J(D^{(r)})}|A_j^{(r)}-A_j^{(r)}|}
{2^{-5r}|D^{(r)}|}
=\left(\frac{80}{83}\right)^r\longrightarrow0.
\]
Thus even an arbitrary absolute positive constant cannot repair the inequality while retaining this prescribed rectangle.

For these actual uniform tables, the original threshold set
\(F_j^{(r)}(t)=\{u\in\mathbb Z^{5r}:0\le u\le j,\ w_{j+u}^{(r)}\ge e^{-t}w_j^{(r)}\}\)
equals \(A_j^{(r)}\) for every positive center and every finite \(t\ge0\). Consequently the same ratio holds for the actual threshold corner score restricted to \(j\in J(D^{(r)})\), with its original normalization \(T^{(r)}=2^{-5r}W^{(r)}\) and its original factor \(e^{-t}/(1+2t)\).

## Proof

All inequalities defining \(P\) have rational coefficients. They describe a closed convex set. Nonnegativity and any one of the four displayed upper bounds imply \(q_1\le10\), and they imply \(q_i\le2\) for \(i=2,3,4,5\). Thus \(P\) is compact. The point \((1,1,1,1,1)\) satisfies every nonnegativity constraint strictly and every other constraint strictly, since \(1+5=6<10\). Hence \(P\) has nonempty interior in \(\mathbb R^5\). Its upper constraints have nonnegative coefficients, so \(0\le q'\le q\in P\) implies \(q'\in P\). It is a real coordinatewise downset. The product \(C=P\times[0,1]\) is therefore a full-dimensional compact convex body in \(\mathbb R^6\).

For every integer \(z\), its actual fiber is exactly \([0,1]\) if \(z\in P\), and is empty otherwise. This verifies the entire claimed actual weight table, including every zero and every boundary fiber.

Here is the complete integer census. Write \(z=(a,b_2,b_3,b_4,b_5)\). The constraints force the integer \(a\) into \(\{0,1,\ldots,10\}\), and each other coordinate is an independent integer in \([0,(10-a)/5]\). Therefore
\[
D=
\bigl(\{0\}\times\{0,1,2\}^{4}\bigr)
\mathbin{\dot\cup}
\bigl(\{1,2,3,4,5\}\times\{0,1\}^{4}\bigr)
\mathbin{\dot\cup}
\bigl(\{6,7,8,9,10\}\times\{0\}^{4}\bigr).
\]
The three terms have distinct first coordinates, so the union is disjoint. This gives \(|D|=3^4+5\cdot2^4+5=81+80+5=166\), with no omitted integer sites.

The sum of first coordinates is \(16(1+2+3+4+5)+(6+7+8+9+10)=240+40=280\). For each fixed \(i\in\{2,3,4,5\}\), the first block contributes \((0+1+2)3^3=81\) to the sum of the \(i\)-th coordinates. Each of the five slices in the second block contributes \((0+1)2^3=8\), and the last block contributes zero. The other four coordinate sums therefore all equal \(81+5\cdot8=121\). It follows exactly that
\[
\bar z=\left(\frac{140}{83},\frac{121}{166},\frac{121}{166},\frac{121}{166},\frac{121}{166}\right),
\qquad
x=\left(\frac{105}{83},\frac{363}{664},\frac{363}{664},\frac{363}{664},\frac{363}{664}\right).
\]
Since \(1<105/83<2\) and \(0<363/664<1\), the integer points in the entire rounding rectangle are exactly \(\{1,2\}\times\{0,1\}^4\). Every one belongs to \(D\), either by the census or because \(j_1+5j_i\le2+5=7\le10\). This proves the stated complete description of \(J(D)\) and its cardinality \(2\cdot2^4=32\).

Fix any allowed center \(j\). If \(u\in A_j\) and \(j_i=0\) for some \(i\ge2\), then \(0\le u_i\le j_i\) gives \(u_i=0\). If instead \(j_i=1\), a positive integer \(u_i\le j_i\) would equal one. In that event \(j_i+u_i=2\) and \(j_1+u_1\ge j_1\ge1\), so the corresponding defining constraint at the forward point would fail:
\((j_1+u_1)+5(j_i+u_i)\ge1+10>10\).
Thus every \(u\in A_j\) has all coordinates except its first equal to zero.

Conversely, take any integer \(a\) with \(0\le a\le j_1\) and put \(u=(a,0,0,0,0)\). This satisfies \(0\le u\le j\). The first coordinate of \(j+u\) is between one and four, and every other coordinate is zero or one. Hence \(j+u\in D\) by the complete census. We have proved the exact identities
\[
A_j=\{(a,0,0,0,0):a\in\mathbb Z,\ 0\le a\le j_1\},
\qquad
A_j-A_j=\{(a,0,0,0,0):a\in\mathbb Z,\ -j_1\le a\le j_1\}.
\]
The second set contains each displayed vector once; different representations of a difference do not affect this count. The 16 allowed centers with \(j_1=1\) have exactly three distinct differences each, and the 16 with \(j_1=2\) have exactly five each. These two cases exhaust all allowed centers. Their maximum is five, whereas \(2^{-5}|D|=166/32=83/16>5\). The seed's normalized ratio is \(2^5\cdot5/166=80/83<1\).

Now fix \(r\ge1\). Products preserve compactness, convexity, rationality of the displayed description, full dimension, and the downset property, so \(C^{(r)}\) is an actual body with all the stated properties. Integer membership separates across its five-coordinate blocks, proving \(D^{(r)}=D^r\), \(|D^{(r)}|=166^r\), and \(W^{(r)}=166^r\). In a uniform Cartesian product, the sum of any coordinate is its seed sum multiplied by \(166^{r-1}\). Dividing by \(166^r\) shows that its mean, and therefore its three-quarter-mean vector, is the concatenation of \(r\) copies of the seed vector. Its rounding rectangle and positive support both separate into blocks. Thus \(J(D^{(r)})=J(D)^r\).

Write a center in that product as \(j=(j^{(1)},\ldots,j^{(r)})\). The coordinate inequalities and forward membership likewise separate, giving \(A_j^{(r)}=\prod_{k=1}^r A_{j^{(k)}}\). For any Cartesian product of nonempty sets, its difference with itself is exactly the Cartesian product of the individual difference sets: projection proves one inclusion, and choosing one representing pair in each block proves the reverse inclusion. Thus distinct-difference cardinalities multiply. The complete seed calculation implies
\[
\max_{j\in J(D^{(r)})}|A_j^{(r)}-A_j^{(r)}|=5^r,
\qquad
\frac{5^r}{166^r/2^{5r}}=\left(\frac{80}{83}\right)^r.
\]
The equality in the maximum is attained by choosing first coordinate two in every block. Since \(0<80/83<1\), the ratio tends to zero.

Every positive actual weight in this family is one. At a finite threshold \(t\ge0\), the number \(e^{-t}w_j^{(r)}=e^{-t}\) is strictly positive and at most one. A forward weight meets it exactly when it equals one; all original zero weights fail it. This proves \(F_j^{(r)}(t)=A_j^{(r)}\). Moreover \(e^{-t}/(1+2t)\le1\), with equality at \(t=0\), so optimization over all finite thresholds at a prescribed center leaves precisely its distinct-difference count. The preceding normalized ratio is therefore also the ratio of the original threshold score restricted to the mean rectangle to \(T^{(r)}=166^r/2^{5r}\).

Finally, the scope can be checked directly. The positive seed center \(j_0=(0,1,1,1,1)\) is outside \(J(D)\), since its first coordinate is zero. Its forward set is exactly \(\{0\}\times\{0,1\}^{4}\), because the first coordinate of every forward point remains zero and all other coordinates are at most two. Its difference set is \(\{0\}\times\{-1,0,1\}^{4}\), which has \(3^4=81\) distinct vectors. The product of these centers therefore gives an unrestricted actual corner count \(81^r\), whose ratio to \(T^{(r)}\) is \((1296/83)^r>1\). This explicit witness prevents interpreting the restricted-rule failure as a failure of the optimized corner inequality or of the locked mixed-integer depth conjecture.

## External sources

None. The support census, mean, complete allowed-center count, distinct differences, actual-body realization, and product amplification are proved directly with integer and rational arithmetic.
