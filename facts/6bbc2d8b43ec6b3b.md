---
fact_id: 6bbc2d8b43ec6b3b
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: stopped-rank-double-divergence
depends_on: ["0e3ca60ae9b0dbad","7ec63df101c30343","9468b734966ba646","d06d919de3083960"]
verifier_run: f665701e44bb49ea
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
\]
and, for \(p\in S\),
\[
 h_S(p):=\inf\{\mathcal H_d(S\cap H):
 H\subseteq\mathbb R^{n+d}\text{ is a closed halfspace and }p\in H\},
 \qquad
 h_{\max}(C):=\sup_{p\in S}h_S(p).
\]
Let \(Q>0\) be the canonical half-strength product-reservoir mass, let
\(R,G,R_{\mathrm{sel}}(C),M_{\mathrm{off}}(C),R_{\mathrm{cloud}}(C)\)
be the canonical nonnegative capacities, and put
\[
 D:=2^nh_{\max}(C),
 \qquad
 \mathcal A(C):=
 R+G+R_{\mathrm{sel}}(C)+M_{\mathrm{off}}(C)
 +R_{\mathrm{cloud}}(C)+D.
\tag{1}
\]
Assume the canonical hard inequality
\[
 \mathcal A(C)<\frac Q{100}.
\tag{2}
\]
The hard ledger of accepted fact 7ec63df101c30343 then gives
\[
 Q\leq\frac W8,
 \qquad
 W<\frac{803}{75}Q.
\tag{3}
\]

Fix the stopped set of accepted fact d06d919de3083960, and use the stopped-fiber normalization retained in accepted fact 0e3ca60ae9b0dbad. Namely,
\[
 \varnothing\ne A_\star\subseteq\mathbb Z^n,
 \qquad
 w_y>0\quad(y\in A_\star),
 \qquad
 4w_y\leq a_y,
\]
\[
 W_\star:=\sum_{y\in A_\star}w_y,
 \qquad
 q:=\dim\operatorname{aff}(A_\star)\geq1,
\tag{4}
\]
and
\[
 r_\star^c:=
 \min_{s:\operatorname{aff}(A_\star)\to\mathbb R^d\ \operatorname{affine}}
 \dim\operatorname{span}\{c_y-s(y):y\in A_\star\},
\tag{5}
\]
where \(c_y\) is the centroid of \(C_y\). The stopped mass and selector estimates are
\[
 2^{n-q}W_\star>\frac{11}{320}Q,
\tag{6}
\]
\[
 R_{\mathrm{sel}}(C)
 \geq
 4\gamma_d\,2^{n-q}\frac{W_\star}{r_\star^c+1}.
\tag{7}
\]

For each integer \(R_0\geq0\), define the positive constant from accepted fact 9468b734966ba646 by
\[
 c_{R_0}:=
 \begin{cases}
 \dfrac1{2e},&R_0=0,\\[4pt]
 \dfrac1e-\left(1-\dfrac1e\right)\log\dfrac e{e-1},&R_0=1,\\[7pt]
 \dfrac1{64e},&R_0=2,\\[7pt]
 \displaystyle
 \max\left\{
 \dfrac1{eR_0 2^{R_0}(R_0+1)^{R_0}},
 \dfrac1{e2^{R_0+1}(R_0+2)^{R_0}}
 \right\},&R_0\geq3.
 \end{cases}
\tag{8}
\]
Then, for every \(R_0\geq0\),
\[
 q\leq R_0
 \quad\Longrightarrow\quad
 h_{\max}(C)
 >\frac{11c_{R_0}}{80}\,2^{-n}Q
 >\frac{15c_{R_0}}{1168}\,2^{-n}W
 >\frac{33c_{R_0}}{5120}\,2^{-n}W.
\tag{9}
\]
For \(R_0=0\), the implication is vacuous because \(q\geq1\).

Now let \((C_j)_{j\geq1}\) be a sequence for which, for every \(j\), all the preceding canonical hard-branch data are defined, \(W_j,Q_j>0\), (1)-(7) hold with subscript \(j\), and a stopped set \(A_{\star,j}\) has been chosen as above. Define
\[
 \varepsilon_j:=\frac{\mathcal A(C_j)}{Q_j},
 \qquad
 \delta_j:=\frac{2^{n_j}h_{\max}(C_j)}{W_j},
 \qquad
 q_j:=\dim\operatorname{aff}(A_{\star,j}),
 \qquad
 r_j:=r_{\star,j}^c.
\tag{10}
\]
If
\[
 \varepsilon_j\longrightarrow0,
\tag{11}
\]
then \(\delta_j\to0\), so this is in particular a normalized depth-vanishing counterexample sequence, and both stopped ranks diverge with the exact quantifier statements
\[
 (\forall R_0\in\mathbb Z_{\geq0})
 (\exists J_{R_0}\in\mathbb Z_{>0})
 (\forall j\geq J_{R_0})
 \quad q_j>R_0,
\tag{12}
\]
\[
 r_j+1>\frac1{20\varepsilon_j}
 \quad(j\geq1),
\tag{13}
\]
and consequently
\[
 (\forall T>0)(\exists J_T\in\mathbb Z_{>0})(\forall j\geq J_T)
 \quad r_j>T.
\tag{14}
\]
No assertion is made that the simultaneous branch \(q_j,r_j\to\infty\) is terminal or has high-rank closure.

## Proof

We first prove the fixed-rank bound without using the separate rank-one or rank-two conclusions of accepted fact 0e3ca60ae9b0dbad. We use only its stopped-body construction, saturated intrinsic chart, and ambient depth transfer.

Put
\[
 B:=\operatorname{aff}(A_\star).
\]
For each \(y\in A_\star\), define
\[
 \lambda_y:=\left(\frac{4w_y}{a_y}\right)^{1/d}\in(0,1],
 \qquad
 K_y:=c_y+\lambda_y(C_y-c_y).
\tag{15}
\]
Convexity gives \(K_y\subseteq C_y\), and homogeneity gives
\[
 \operatorname{vol}_d(K_y)=4w_y.
\tag{16}
\]
Define the genuine relative convex body
\[
 \widetilde C_\star
 :=\operatorname{conv}\bigcup_{y\in A_\star}(\{y\}\times K_y)
 \subseteq C\cap(B\times\mathbb R^d).
\tag{17}
\]

Choose \(y_0\in A_\star\) and put
\[
 \Gamma:=(B-y_0)\cap\mathbb Z^n.
\tag{18}
\]
The integer differences of an affine basis of \(A_\star\) give \(q\) real-linearly independent elements of \(\Gamma\), while discreteness in the \(q\)-dimensional space \(B-y_0\) gives \(\operatorname{rank}\Gamma=q\). The lattice is saturated: if \(u\in\mathbb Z^n\), \(k\in\mathbb Z\setminus\{0\}\), and \(ku\in\Gamma\), then the real vector subspace \(B-y_0\) contains \(u\), so \(u\in\Gamma\). In particular,
\[
 B\cap\mathbb Z^n=y_0+\Gamma.
\tag{19}
\]
Choose a \(\mathbb Z\)-basis \(g_1,\ldots,g_q\) of \(\Gamma\), set
\[
 Uu:=\sum_{i=1}^qu_i g_i,
 \qquad
 \Phi(u,x):=(y_0+Uu,x),
\tag{20}
\]
and define
\[
 C_\star':=\Phi^{-1}(\widetilde C_\star)
 \subseteq\mathbb R^q\times\mathbb R^d,
 \qquad
 S_\star':=C_\star'\cap(\mathbb Z^q\times\mathbb R^d).
\tag{21}
\]
Equations (19)-(20) give the exact lattice identity
\[
 \Phi(\mathbb Z^q\times\mathbb R^d)
 =(B\cap\mathbb Z^n)\times\mathbb R^d.
\tag{22}
\]
The map is the identity in every continuous fiber. Hence there is neither a lattice-index factor nor a continuous Jacobian factor in mixed volume. Accepted fact 0e3ca60ae9b0dbad verifies that \(C_\star'\) is a convex body in \(\mathbb R^{q+d}\). Its positive-volume integer-fiber support has affine rank exactly \(q\), since it is contained in \(\mathbb R^q\) and contains the images of all points of \(A_\star\).

Put
\[
 W_\star':=\mathcal H_d(S_\star').
\]
Every \(K_y\) is contained in the corresponding fiber of \(\widetilde C_\star\), and distinct \(y\)'s have distinct intrinsic integer bases. Thus (16) and (22) give
\[
 W_\star'\geq4W_\star.
\tag{23}
\]
The same accepted chart construction gives the ambient depth transfer
\[
 h_S(\Phi(p'))\geq h_{S_\star'}(p')
 \qquad(p'\in S_\star').
\tag{24}
\]
Indeed, the pullback to \(\mathbb R^q\times\mathbb R^d\) of the intersection of any ambient closed halfspace with \(B\times\mathbb R^d\) is a closed halfspace or the whole space, contains \(p'\), and preserves every continuous-fiber volume; contributions from \(C\setminus\widetilde C_\star\) are nonnegative.

Fix \(R_0\geq0\) and suppose \(q\leq R_0\). Since \(q\geq1\), only \(R_0\geq1\) occurs. Apply the uniform rank-cap conclusion of accepted fact 9468b734966ba646 to \(C_\star'\), whose integer dimension is \(q\), total mixed volume is \(W_\star'\), and intrinsic positive-support rank is \(q\leq R_0\). It supplies \(p'\in S_\star'\) with
\[
 h_{S_\star'}(p')\geq c_{R_0}2^{-q}W_\star'.
\tag{25}
\]
Using (23)-(25) and then the strict stopped mass estimate (6),
\[
 \begin{aligned}
 h_{\max}(C)
 &\geq h_S(\Phi(p'))
 \geq c_{R_0}2^{-q}W_\star'\\
 &\geq4c_{R_0}2^{-q}W_\star
 >\frac{11c_{R_0}}{80}\,2^{-n}Q.
 \end{aligned}
\tag{26}
\]
Equation (3) gives \(Q>75W/803\). Since \(803=11\cdot73\), equation (26) yields
\[
 h_{\max}(C)
 >\frac{11c_{R_0}}{80}\frac{75}{803}\,2^{-n}W
 =\frac{15c_{R_0}}{1168}\,2^{-n}W.
\tag{27}
\]
Finally, \(15/1168>33/5120\), proving every inequality in (9). This argument uses one theorem uniformly for all fixed rank caps and imports no separate rank-one or rank-two statement.

We turn to the sequence. Since \(D_j\) is a nonnegative summand of \(\mathcal A(C_j)\) and \(Q_j\leq W_j/8\),
\[
 0\leq\delta_j
 =\frac{D_j}{W_j}
 \leq\frac{\mathcal A(C_j)}{Q_j}\frac{Q_j}{W_j}
 \leq\frac{\varepsilon_j}{8}.
\tag{28}
\]
Thus (11) implies \(\delta_j\to0\), which justifies the normalized depth-vanishing terminology.

Fix \(R_0\geq1\). If \(q_j\leq R_0\), equation (26) gives
\[
 \frac{D_j}{Q_j}
 =\frac{2^{n_j}h_{\max}(C_j)}{Q_j}
 >\frac{11c_{R_0}}{80}.
\tag{29}
\]
Because \(D_j\leq\mathcal A(C_j)\), this would imply
\[
 \varepsilon_j>\frac{11c_{R_0}}{80}.
\tag{30}
\]
By (11), there is \(J_{R_0}\) such that \(\varepsilon_j<11c_{R_0}/80\) for every \(j\geq J_{R_0}\). Equations (29)-(30) then exclude \(q_j\leq R_0\) on that tail. For \(R_0=0\), take \(J_0=1\) and use \(q_j\geq1\). This proves (12).

It remains to prove residual-rank divergence. Combining (6)-(7) gives
\[
 R_{\mathrm{sel}}(C)
 >\frac{11\gamma_d}{80}\frac{Q}{r_\star^c+1}.
\tag{31}
\]
Accepted fact d06d919de3083960 records \(\gamma_d>4/11\), so
\[
 R_{\mathrm{sel}}(C)
 >\frac{Q}{20(r_\star^c+1)}.
\tag{32}
\]
In particular, every denominator in the following chain is positive. Rearranging (32), and using that \(R_{\mathrm{sel}}(C)\) is a nonnegative summand of \(\mathcal A(C)\), gives
\[
 r_\star^c+1
 >\frac{Q}{20R_{\mathrm{sel}}(C)}
 \geq\frac{Q}{20\mathcal A(C)}.
\tag{33}
\]
Applying (33) to the \(j\)-th instance gives exactly
\[
 r_j+1>\frac1{20\varepsilon_j},
\]
which is (13). For any \(T>0\), equation (11) supplies \(J_T\) such that
\[
 \varepsilon_j<\frac1{20(T+1)}
 \qquad(j\geq J_T).
\]
Then (13) gives \(r_j+1>T+1\), hence \(r_j>T\), proving (14). The two divergence conclusions leave the simultaneous unbounded-rank branch untouched, as stated.

## External sources

none
