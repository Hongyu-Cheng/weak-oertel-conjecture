---
fact_id: 0e3ca60ae9b0dbad
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: stopped-intrinsic-rank-two-closure
depends_on: ["7ec63df101c30343","8aac56c49321466c","d06d919de3083960","daef2580cdfec07b"]
verifier_run: 78597585ce704ebd
target_match: null
---

## Statement

Retain the canonical hard-branch objects and normalizations of accepted facts 7ec63df101c30343 and d06d919de3083960. Thus \(n,d\in\mathbb Z_{>0}\), \(C\subseteq\mathbb R^n\times\mathbb R^d\) is a convex body,
\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
 \qquad
 a_z:=\operatorname{vol}_d(C_z),
 \qquad
 W:=\sum_{z\in\mathbb Z^n}a_z>0,
\]
\[
 S:=C\cap(\mathbb Z^n\times\mathbb R^d),
 \qquad
 \gamma_d:=\left(\frac d{d+1}\right)^d,
 \qquad
 D:=2^nh_{\max}(C),
\]
and \(G:=\mathfrak C_{\mathrm{core}}(C)\) and \(Q>0\) are the canonical complete-core capacity and half-strength product-reservoir mass. In particular,
\[
 D<\frac Q{100},
 \qquad
 G<\frac Q{100},
 \qquad
 Q\leq\frac W8,
 \qquad
 Q\geq\frac3{32}(W-4G).
\tag{1}
\]

Fix the stopped set supplied by accepted fact d06d919de3083960, and use its notation
\[
 \varnothing\ne A_\star\subseteq\mathbb Z^n,
 \qquad
 w_y>0\quad(y\in A_\star),
 \qquad
 W_\star:=\sum_{y\in A_\star}w_y,
 \qquad
 q:=\dim\operatorname{aff}(A_\star).
\tag{2}
\]
The retained stopped-fiber normalization and the conclusions of that accepted fact are
\[
 4w_y\leq a_y\quad(y\in A_\star),
 \qquad
 q\geq1,
 \qquad
 2^{n-q}W_\star>\frac{11}{320}Q.
\tag{3}
\]
Then the following hold.

1. The case \(q=0\) is impossible by (3), and the case \(q=1\) contradicts the hard inequality \(D<Q/100\).

2. If \(q=2\), there is a point \(p\in S\) such that
\[
 h_S(p)
 >\frac{11\gamma_d}{5120}\,2^{-n}Q
 >\frac{33\gamma_d}{327680}\,2^{-n}W
 >\frac{33}{327680e}\,2^{-n}W.
\tag{4}
\]
Thus this rank-two branch satisfies the locked weak-Oertel conclusion with the absolute constant
\[
 c_\star:=\frac{33}{327680e}\in(0,1/e).
\tag{5}
\]

Consequently, in the canonical stopped branch, any configuration not already ruled out by contradiction and not discharged by the explicit certificate (4) must satisfy \(q\geq3\).

## Proof

We first build one genuine intrinsic convex body from the stopped fibers. Put
\[
 B:=\operatorname{aff}(A_\star).
\]
For \(y\in A_\star\), let \(c_y\) be the centroid of \(C_y\), and define
\[
 \lambda_y:=\left(\frac{4w_y}{a_y}\right)^{1/d}\in(0,1],
 \qquad
 K_y:=c_y+\lambda_y(C_y-c_y).
\tag{6}
\]
Because \(C_y\) is convex and \(c_y\in C_y\), one has \(K_y\subseteq C_y\). Homogeneity of \(d\)-dimensional volume and (3) give
\[
 \operatorname{vol}_d(K_y)=\lambda_y^da_y=4w_y.
\tag{7}
\]
Define the relative convex hull
\[
 \widetilde C_\star
 :=\operatorname{conv}\bigcup_{y\in A_\star}(\{y\}\times K_y)
 \subseteq C\cap(B\times\mathbb R^d).
\tag{8}
\]
This is an actual convex subset of \(C\), not a formal collection of independently shrunken fibers.

We next audit its intrinsic lattice. Choose \(y_0\in A_\star\) and put
\[
 \Gamma:=(B-y_0)\cap\mathbb Z^n.
\tag{9}
\]
The integer differences of an affine basis of \(A_\star\) give \(q\) real-linearly independent elements of \(\Gamma\). Since \(\Gamma\) is a discrete subgroup of the \(q\)-dimensional space \(B-y_0\), it has rank exactly \(q\). It is saturated in \(\mathbb Z^n\): if \(ku\in\Gamma\) for \(u\in\mathbb Z^n\) and \(0\ne k\in\mathbb Z\), then \(ku\in B-y_0\), hence \(u\in B-y_0\), and therefore \(u\in\Gamma\). In particular,
\[
 B\cap\mathbb Z^n=y_0+\Gamma.
\tag{10}
\]

Choose a \(\mathbb Z\)-basis \(g_1,\ldots,g_q\) of \(\Gamma\), set
\[
 Uu:=\sum_{i=1}^qu_i g_i,
 \qquad
 \Phi(u,x):=(y_0+Uu,x),
\tag{11}
\]
and put
\[
 C_\star':=\Phi^{-1}(\widetilde C_\star)
 \subseteq\mathbb R^q\times\mathbb R^d.
\tag{12}
\]
Then \(\Phi\) is an affine bijection from \(\mathbb R^q\times\mathbb R^d\) onto \(B\times\mathbb R^d\), and (10) gives the exact lattice identity
\[
 \Phi(\mathbb Z^q\times\mathbb R^d)
 =(B\cap\mathbb Z^n)\times\mathbb R^d.
\tag{13}
\]
There is no lattice-index factor. There is also no continuous Jacobian factor in mixed volume, because \(\Phi\) is the identity on every \(d\)-dimensional continuous fiber.

The set \(C_\star'\) is a convex body in \(\mathbb R^{q+d}\). Compactness and convexity follow from (8) and (12). For full dimensionality, choose affinely independent \(y_0,\ldots,y_q\in A_\star\). Each \(K_{y_i}\) has positive \(d\)-volume by (7). Choose an interior point in every \(K_{y_i}\), and choose \(d\) sufficiently small independent vertical perturbations of the point over \(y_0\). In intrinsic coordinates, the \(q\) differences to the other selected fibers have linearly independent base components, and the \(d\) vertical differences are independent. Hence their \(q+d\) differences are linearly independent.

Write
\[
 W_\star':=
 \sum_{u\in\mathbb Z^q}
 \operatorname{vol}_d((C_\star')_u).
\tag{14}
\]
For every \(y\in A_\star\), equation (13) gives a distinct \(u_y\in\mathbb Z^q\) with \(y=y_0+Uu_y\), and (8) gives \(K_y\subseteq(\widetilde C_\star)_y\). Therefore (7) implies
\[
 W_\star'
 \geq\sum_{y\in A_\star}\operatorname{vol}_d(K_y)
 =4W_\star.
\tag{15}
\]
The positive integer-fiber support of \(C_\star'\) contains all \(u_y\), so its affine hull is all of \(\mathbb R^q\).

We record the ambient-transfer inequality once. If \(p'\in C_\star'\cap(\mathbb Z^q\times\mathbb R^d)\) and \(p:=\Phi(p')\), then \(p\in S\). For every ambient closed halfspace \(H\subseteq\mathbb R^{n+d}\) containing \(p\), the pullback
\[
 J:=\Phi^{-1}\bigl(H\cap(B\times\mathbb R^d)\bigr)
\tag{16}
\]
is a proper closed halfspace in \(\mathbb R^{q+d}\) or the whole space, and it contains \(p'\). Fiberwise volume preservation, (8), and (13) give
\[
 \mathcal H_d(S\cap H)
 \geq
 \sum_{u\in\mathbb Z^q}
 \operatorname{vol}_d((C_\star')_u\cap J_u).
\tag{17}
\]
If \(J\) is the whole space, the last member is \(W_\star'\); otherwise it is the mixed volume of the proper halfspace section. Thus
\[
 h_S(\Phi(p'))\geq h_{S_\star'}(p'),
 \qquad
 S_\star':=C_\star'\cap(\mathbb Z^q\times\mathbb R^d),
\tag{18}
\]
and, after taking suprema,
\[
 h_{\max}(C)\geq h_{\max}(C_\star').
\tag{19}
\]
This transfer keeps closed-halfspace boundary mass and discards only nonnegative contributions from \(C\setminus\widetilde C_\star\).

Suppose \(q=1\). Apply accepted fact 8aac56c49321466c to the convex body \(C_\star'\subseteq\mathbb R\times\mathbb R^d\), with its affine slice equal to all of \(\mathbb R\). The affine hull assertion after (15) identifies its slice rank with one and its slice mass with \(W_\star'\). Equations (11) and (18) of that accepted fact give
\[
 \mathfrak C_{\mathrm{core}}(C_\star')
 \geq\frac14W_\star',
 \qquad
 h_{\max}(C_\star')
 \geq\frac{\gamma_d}{2}
 \mathfrak C_{\mathrm{core}}(C_\star')
 \geq\frac{\gamma_d}{8}W_\star'.
\tag{20}
\]
Combining (15), (19), and (20),
\[
 h_{\max}(C)\geq\frac{\gamma_d}{2}W_\star.
\tag{21}
\]
The stopped-mass inequality (3), now with \(q=1\), yields
\[
 D=2^nh_{\max}(C)
 \geq\gamma_d2^{n-1}W_\star
 >\frac{11\gamma_d}{320}Q.
\tag{22}
\]
Accepted fact d06d919de3083960 records \(\gamma_d>4/11\) in this canonical normalization. Hence
\[
 D>\frac{Q}{80}>\frac{Q}{100},
\tag{23}
\]
contradicting (1). This proves the rank-one exclusion. The rank-zero exclusion is already the assertion \(q\geq1\) in (3).

Suppose \(q=2\). Apply the first assertion of accepted fact daef2580cdfec07b to \(C_\star'\subseteq\mathbb R^2\times\mathbb R^d\). It supplies \(p'\in S_\star'\) such that
\[
 h_{S_\star'}(p')
 \geq\frac{\gamma_d}{256}W_\star'
 \geq\frac{\gamma_d}{64}W_\star,
\tag{24}
\]
where the second inequality is (15). Put \(p:=\Phi(p')\). Equations (18), (24), and the stopped-mass inequality (3) with \(q=2\) give
\[
 h_S(p)
 \geq\frac{\gamma_d}{64}W_\star
 >\frac{11\gamma_d}{5120}\,2^{-n}Q.
\tag{25}
\]

It remains to convert the reservoir mass to the total physical mass without changing its normalization. Accepted fact 7ec63df101c30343 gives all four inequalities in (1) for this same \(C,W,G,Q\). In particular,
\[
 G<\frac Q{100}\leq\frac W{800}<\frac W8.
\tag{26}
\]
Together with the last inequality in (1), this gives
\[
 Q\geq\frac3{32}(W-4G)>\frac3{64}W.
\tag{27}
\]
Substitution into (25) proves the first two strict inequalities in (4). Accepted fact daef2580cdfec07b also proves \(\gamma_d>1/e\), so the last strict inequality in (4) follows. Since \(0<33/327680<1\), equation (5) indeed defines an absolute constant in \((0,1/e)\).

Thus \(q=0\) is excluded by the stopped theorem, \(q=1\) is incompatible with the canonical hard branch, and \(q=2\) already has the explicit terminal depth certificate (4). Only \(q\geq3\) remains in the nonterminal stopped branch.

## External sources

none
