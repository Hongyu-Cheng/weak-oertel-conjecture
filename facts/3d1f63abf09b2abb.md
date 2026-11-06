---
fact_id: 3d1f63abf09b2abb
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: global-core-one-sided-augmentation
depends_on: ["6769574fc1bd9f8d","ae0161dd5d4ea672","fbeb0a501b268d12"]
verifier_run: 981bb182063e4324
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body with \(C\cap(\mathbb Z^n\times\mathbb R^d)\ne\varnothing\), and put
\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
 \qquad
 a_z:=\operatorname{vol}_d(C_z),
 \qquad
 I_+:=\{z\in\mathbb Z^n:a_z>0\},
 \qquad
 W:=\sum_{z\in\mathbb Z^n}a_z.
\tag{1}
\]
The set \(I_+\) is finite. For \((z,x)\in C\), define its absolute fiber depth by
\[
 \delta_C(z,x)
 :=
 \inf\left\{
 \operatorname{vol}_d(C_z\cap H):
 H\subseteq\mathbb R^d\text{ is a proper closed halfspace and }x\in H
 \right\}.
\tag{2}
\]
Let \(S_C:=C\cap(\mathbb Z^n\times\mathbb R^d)\), and define
\[
 h_{\max}(C)
 :=
 \sup_{p\in S_C}
 \inf_{\substack{H\subseteq\mathbb R^{n+d}\text{ closed halfspace}\\p\in H}}
 \sum_{z\in\mathbb Z^n}\operatorname{vol}_d(C_z\cap H_z),
 \qquad
 H_z:=\{x:(z,x)\in H\}.
\tag{3}
\]
For a \(d\)-dimensional convex body \(K\) and \(0<t\leq\operatorname{vol}_d(K)\), write
\[
 \mathsf M_t(K)
 :=
 \left\{
 \frac1t\int_Kx f(x)\,dx:
 f\in L^\infty(K),\ 0\leq f\leq1\text{ a.e.},\ \int_Kf\,dx=t
 \right\},
 \qquad
 \gamma_d:=\left(\frac d{d+1}\right)^d.
\tag{4}
\]
For a finite nonempty \(E\subseteq\mathbb Z^n\) and \(m\in\mathbb Z^n\cap\operatorname{conv}E\), let
\[
 \Lambda_m(E)
 :=
 \left\{
 \lambda\in\mathbb R_+^E:
 \sum_{z\in E}\lambda_z=1,
 \quad
 \sum_{z\in E}\lambda_zz=m
 \right\}.
\tag{5}
\]
For nonempty convex sets \(Q_z\subseteq\mathbb R^d\), set
\[
 \mathcal K_m(Q)
 :=
 \bigcap_{\lambda\in\Lambda_m(E)}
 \sum_{z\in E}\lambda_zQ_z.
\tag{6}
\]
The global complete metronoid-core capacity is
\[
 G:=\mathfrak C_{\mathrm{core}}(C)
 :=
 \sup\left\{
 \sum_{z\in E}t_z:
 \begin{array}{l}
 \varnothing\ne E\subseteq I_+,\quad 0<t_z\leq a_z,\\
 \text{there is }m\in\mathbb Z^n\cap\operatorname{conv}E
 \text{ with }\mathcal K_m(\mathsf M_t)\ne\varnothing,\\
 \displaystyle
 \sum_{z\in E\cap J}t_z
 \geq2^{-n}\sum_{z\in E}t_z
 \text{ for every proper closed halfspace }J\subseteq\mathbb R^n
 \text{ containing }m
 \end{array}
 \right\},
\tag{7}
\]
where the supremum of the empty family is zero.

Let \(A\subsetneq\mathbb R^n\) be a proper affine subspace containing an integer point, and put \(r:=\dim A\). A proper relative closed halfspace of \(A\) means one defined by a nonconstant affine functional on \(A\); when \(r=0\), there are no such halfspaces. Let \(E_0\subseteq A\cap\mathbb Z^n\) be finite and nonempty, and let
\[
 m\in A\cap\mathbb Z^n\cap\operatorname{conv}E_0.
\tag{8}
\]
For each \(z\in E_0\), let \(D_z\subseteq C_z\) be nonempty, compact, and convex, and let \(w_z\geq0\) satisfy
\[
 \delta_C(z,x)\geq w_z
 \qquad(x\in D_z).
\tag{9}
\]
Assume
\[
 T:=\sum_{z\in E_0}w_z>0,
 \qquad
 \mathcal K_m(D)\ne\varnothing,
\tag{10}
\]
and assume that for some \(\beta\in[2^{-n},1]\), every proper relative closed halfspace \(J_A\subseteq A\) containing \(m\) satisfies
\[
 \sum_{z\in E_0\cap J_A}w_z\geq\beta T.
\tag{11}
\]
There is an affine functional \(\varphi:\mathbb R^n\to\mathbb R\) such that
\[
 \varphi=0\text{ on }A,
 \qquad
 \varphi(z)\ne0\quad(z\in I_+\setminus A).
\tag{12}
\]
For \(\sigma\in\{+1,-1\}\), define
\[
 I_\sigma:=\{z\in I_+:\sigma\varphi(z)>0\},
 \qquad
 H_\sigma:=\sum_{z\in I_\sigma}a_z,
 \qquad
 H_*:=\max\{H_+,H_-\},
 \qquad
 W_A:=\sum_{z\in I_+\cap A}a_z.
\tag{13}
\]
Then, for each \(\sigma\),
\[
 \boxed{
 h_{\max}(C)
 \geq
 2^{-n}\min\{T+\gamma_dH_\sigma,\ 2^n\beta T\}.
 }
\tag{14}
\]
Consequently, the exact heavier-side bound and its support-free corollary are
\[
 h_{\max}(C)
 \geq
 2^{-n}\min\{T+\gamma_dH_*,\ 2^n\beta T\}
 \geq
 2^{-n}\min\left\{T+\frac{\gamma_d}{2}(W-W_A),\ 2^n\beta T\right\}.
\tag{15}
\]
If \(A\) is the affine hull of an exposed face of \(\operatorname{conv}I_+\), \(\varphi\) may be chosen with all of \(I_+\setminus A\) on one strict side, and (15) improves to
\[
 \boxed{
 h_{\max}(C)
 \geq
 2^{-n}\min\{T+\gamma_d(W-W_A),\ 2^n\beta T\}.
 }
\tag{16}
\]

Independently of (8)-(11), here is the complete metronoid-capacity form. Let \(E_0\subseteq I_+\cap A\) be finite and nonempty, let
\[
 m\in A\cap\mathbb Z^n\cap\operatorname{conv}E_0,
\]
and suppose that
\[
 0<t_z\leq a_z\quad(z\in E_0),
 \qquad
 \tau:=\sum_{z\in E_0}t_z>0,
 \qquad
 \mathcal K_m(\mathsf M_t)\ne\varnothing,
\tag{17}
\]
and that every proper relative closed halfspace \(J_A\subseteq A\) containing \(m\) satisfies
\[
 \sum_{z\in E_0\cap J_A}t_z\geq\beta\tau
\tag{18}
\]
for some \(\beta\in[2^{-n},1]\). Then, for each \(\sigma\),
\[
 \boxed{
 G\geq\min\{\tau+H_\sigma,\ 2^n\beta\tau\},
 \qquad
 h_{\max}(C)\geq
 \gamma_d2^{-n}\min\{\tau+H_\sigma,\ 2^n\beta\tau\}.
 }
\tag{19}
\]
Thus
\[
 G\geq\min\{\tau+H_*,\ 2^n\beta\tau\}
 \geq
 \min\left\{\tau+\frac{W-W_A}{2},\ 2^n\beta\tau\right\}.
\tag{20}
\]
In the exposed-face case, \(H_*\) in (20) can be replaced by \(W-W_A\).

Define the relative complete metronoid-core capacity on \(A\) by
\[
 G_A^{\mathrm{rel}}
 :=
 \sup\left\{
 \sum_{z\in E}t_z:
 \begin{array}{l}
 \varnothing\ne E\subseteq I_+\cap A,\quad 0<t_z\leq a_z,\\
 \text{there is }m'\in A\cap\mathbb Z^n\cap\operatorname{conv}E
 \text{ with }\mathcal K_{m'}(\mathsf M_t)\ne\varnothing,\\
 \displaystyle
 \sum_{z\in E\cap J_A}t_z
 \geq2^{-r}\sum_{z\in E}t_z
 \text{ for every proper relative closed halfspace }J_A\subseteq A
 \text{ containing }m'
 \end{array}
 \right\},
\tag{21}
\]
again with empty supremum zero. Then
\[
 \boxed{
 G
 \geq
 \min\{G_A^{\mathrm{rel}}+H_*,\ 2^{n-r}G_A^{\mathrm{rel}}\}
 \geq
 \min\left\{G_A^{\mathrm{rel}}+\frac{W-W_A}{2},\ 2^{n-r}G_A^{\mathrm{rel}}\right\}.
 }
\tag{22}
\]
If \(A\) is the affine hull of an exposed face, the first entry in both minima in (22) improves to \(G_A^{\mathrm{rel}}+W-W_A\).

Finally, assume the exact hard-branch hypotheses
\[
 W_L<2^{\dim L-n}W
 \quad\text{for every proper primitive affine lattice subspace }L\subsetneq\mathbb R^n,
 \qquad
 G<\frac W4.
\tag{23}
\]
Here primitive means that \(L=b+V\) for some \(b\in\mathbb Z^n\) and \(V\cap\mathbb Z^n\) is a saturated lattice of rank \(\dim V\). Then every such \(L\), with \(q:=\dim L<n\), satisfies the ambient-normalized lower-rank domination
\[
 \boxed{2^{n-q}G_L^{\mathrm{rel}}\leq G.}
\tag{24}
\]

For completeness, an admissible one-factor lattice-simplex packet consists of an integer \(1\leq q\leq n\), a full-dimensional lattice simplex
\[
 \Delta=\operatorname{conv}\{v_0,\ldots,v_q\}\subseteq\mathbb R^q,
 \qquad
 D:=\Delta\cap\mathbb Z^q,
\]
an injective integral affine map
\[
 \Phi(u)=b+Uu,
 \qquad
 b\in\mathbb Z^n,
 \quad
 U\in\mathbb Z^{n\times q},
 \quad
 \operatorname{rank}U=q,
\]
points \(x_j\in C_{\Phi(v_j)}\), and numbers \(c_j\geq0\) such that
\[
 \delta_C(\Phi(v_j),x_j)^{1/d}\geq c_j
 \qquad(0\leq j\leq q).
\tag{25}
\]
If \(\lambda_j\) are the barycentric coordinates on \(\Delta\), put
\[
 g(u):=\sum_{j=0}^q\lambda_j(u)c_j,
 \qquad
 \mathcal E(\Pi):=\sum_{u\in D}g(u)^d,
 \qquad
 \operatorname{Sc}_n(\Pi):=2^{n-q}\mathcal E(\Pi).
\tag{26}
\]
Under (23), every such packet, of every rank \(1\leq q\leq n\), satisfies
\[
 \boxed{\operatorname{Sc}_n(\Pi)\leq G.}
\tag{27}
\]
For \(q=n\), (27) holds without (23). Outside (23), no ambient-normalized domination by \(G\) is asserted here for \(q<n\), and no such domination is asserted here for a packet having at least two nonzero-rank factors.

## Proof

Compactness of the base projection of \(C\) implies that only finitely many integer fibers are nonempty, hence \(I_+\) is finite. Consider the nonzero finite-dimensional vector space of affine functionals that vanish on \(A\). For each \(z\notin A\), evaluation at \(z\) is a nonzero linear functional on that vector space, so its zero set is a proper linear hyperplane. Avoiding the finitely many such hyperplanes for \(z\in I_+\setminus A\) gives \(\varphi\) satisfying (12).

We first prove the depth-region form. Fix \(\sigma\in\{+1,-1\}\), and put
\[
 R:=\min\{\gamma_dH_\sigma,\ (2^n\beta-1)T\}\geq0.
\tag{28}
\]
If \(R=0\), take \(F=\varnothing\). If \(R>0\), the positive capacities \(\gamma_da_z\), \(z\in I_\sigma\), have total \(\gamma_dH_\sigma\geq R\). Taking full capacities successively and, if necessary, a final partial capacity gives a finite nonempty \(F\subseteq I_\sigma\) and numbers
\[
 0<r_z\leq\gamma_da_z\quad(z\in F),
 \qquad
 \sum_{z\in F}r_z=R.
\tag{29}
\]
For \(z\in F\), define
\[
 \widetilde D_z:=\mathsf M_{r_z/\gamma_d}(C_z),
 \qquad
 \widetilde w_z:=r_z,
\tag{30}
\]
and for \(z\in E_0\), define \(\widetilde D_z:=D_z\) and \(\widetilde w_z:=w_z\). No set or weight is added when \(F=\varnothing\). Since \(0<r_z/\gamma_d\leq a_z\), accepted fact `6769574fc1bd9f8d` shows that every set in (30) is nonempty, compact, and convex, is contained in \(C_z\), and satisfies
\[
 \delta_C(z,x)\geq r_z=\widetilde w_z
 \qquad(x\in\widetilde D_z).
\tag{31}
\]
Thus no zero-mass metronoid is introduced.

Set \(E':=E_0\cup F\). The two sets are disjoint because \(E_0\subseteq A\), while \(\sigma\varphi>0\) on \(F\). For \(\lambda\in\Lambda_m(E_0)\), define its zero-extension \(\operatorname{ext}_F\lambda\in\mathbb R^{E'}\) by
\[
 (\operatorname{ext}_F\lambda)_z
 :=
 \begin{cases}
 \lambda_z,&z\in E_0,\\
 0,&z\in F.
 \end{cases}
\tag{32}
\]
Then the exact identity of representation polytopes is
\[
 \boxed{
 \Lambda_m(E')
 =\{\operatorname{ext}_F\lambda:\lambda\in\Lambda_m(E_0)\}.
 }
\tag{33}
\]
Indeed, zero-extension plainly preserves total coefficient one and barycenter \(m\). Conversely, if \(\mu\in\Lambda_m(E')\), then
\[
 0=\sigma\varphi(m)
 =\sum_{z\in E'}\mu_z\sigma\varphi(z)
 =\sum_{z\in F}\mu_z\sigma\varphi(z).
\tag{34}
\]
Every summand in the last expression is nonnegative, and \(\sigma\varphi(z)>0\) on \(F\), so \(\mu_z=0\) for every \(z\in F\). Its restriction to \(E_0\) therefore lies in \(\Lambda_m(E_0)\), proving (33).

Using the standard convention \(0Q=\{0\}\) for a nonempty set \(Q\), equations (32)-(33) give the exact complete-core equality
\[
 \boxed{
 \mathcal K_m(\widetilde D)
 =
 \bigcap_{\mu\in\Lambda_m(E')}
 \sum_{z\in E'}\mu_z\widetilde D_z
 =
 \bigcap_{\lambda\in\Lambda_m(E_0)}
 \sum_{z\in E_0}\lambda_zD_z
 =\mathcal K_m(D)\ne\varnothing.
 }
\tag{35}
\]
This equality concerns every barycentric representation, not a selected one.

Let \(J\subseteq\mathbb R^n\) be a proper closed halfspace containing \(m\). The trace \(J\cap A\) is either all of \(A\), or a proper relative closed halfspace of \(A\) containing \(m\). In the first case all old weights lie in \(J\); in the second case (11) applies. Since all weights are nonnegative, in either case
\[
 \sum_{z\in E'\cap J}\widetilde w_z
 \geq\beta T.
\tag{36}
\]
Equation (28) gives \(T+R\leq2^n\beta T\), hence
\[
 \beta T\geq2^{-n}(T+R)
 =2^{-n}\sum_{z\in E'}\widetilde w_z.
\tag{37}
\]
Apply the barycentric Minkowski-core depth theorem in accepted fact `ae0161dd5d4ea672` to the sets and weights on \(E'\). By (35)-(37), any point of the nonempty enlarged core gives
\[
 h_{\max}(C)
 \geq2^{-n}(T+R)
 =2^{-n}\min\{T+\gamma_dH_\sigma,\ 2^n\beta T\},
\]
which is (14).

Because (12) makes \(I_+\setminus A\) the disjoint union of \(I_+\) on the two strict sides,
\[
 H_++H_-=W-W_A,
 \qquad
 H_*\geq\frac12(W-W_A).
\tag{38}
\]
Choosing the heavier side in (14) proves (15). If \(A\) is the affine hull of an exposed face \(\mathcal F\) of \(\operatorname{conv}I_+\), choose a supporting affine functional equal to zero on \(A\) and strictly positive on every point of \(I_+\setminus A\), after changing sign. Such strictness follows from \(\operatorname{conv}I_+\) meeting its supporting hyperplane exactly in \(\mathcal F\). Then \(H_*=W-W_A\), proving (16). If \(I_+\setminus A=\varnothing\), the same conclusion is vacuous and both sides equal zero.

We next prove the metronoid-capacity form. Fix \(\sigma\), and put
\[
 U_\sigma:=\min\{H_\sigma,\ (2^n\beta-1)\tau\}\geq0.
\tag{39}
\]
If \(U_\sigma=0\), take \(F=\varnothing\). If \(U_\sigma>0\), choose \(F\subseteq I_\sigma\) and masses
\[
 0<u_z\leq a_z\quad(z\in F),
 \qquad
 \sum_{z\in F}u_z=U_\sigma,
\tag{40}
\]
by the same finite-capacity argument as above. On \(E':=E_0\cup F\), retain the masses \(t_z\) for \(z\in E_0\) and use \(u_z\) for \(z\in F\). Accepted fact `6769574fc1bd9f8d` makes all added positive-mass metronoids nonempty compact convex subsets of their fibers. Equations (32)-(35), with \(D_z=\mathsf M_{t_z}(C_z)\) on \(E_0\) and \(\widetilde D_z=\mathsf M_{u_z}(C_z)\) on \(F\), show that the enlarged complete core is exactly the old nonempty core. Equations (18), (39), and nonnegativity give, for every proper ambient closed halfspace \(J\ni m\),
\[
 \sum_{z\in E'\cap J}\widetilde t_z
 \geq\beta\tau
 \geq2^{-n}(\tau+U_\sigma).
\tag{41}
\]
The enlarged tuple is therefore admissible in (7), and
\[
 G\geq\tau+U_\sigma
 =\min\{\tau+H_\sigma,\ 2^n\beta\tau\}.
\tag{42}
\]
The metronoid-core master bound in accepted fact `ae0161dd5d4ea672` gives the corresponding depth bound in (19). Equations (20) and the exposed-face improvement now follow from (38) exactly as before.

Apply (42) to every tuple in (21), with \(\beta=2^{-r}\), and choose the heavier side. The function
\[
 s\longmapsto\min\{s+H_*,\ 2^{n-r}s\}
\]
is continuous and nondecreasing on \([0,\infty)\). Taking a sequence of admissible tuple masses tending to the supremum \(G_A^{\mathrm{rel}}\) proves the first inequality in (22) whenever the defining family is nonempty. When it is empty, \(G_A^{\mathrm{rel}}=0\) and that inequality is trivial. The second inequality follows from (38), and the exposed-face statement follows from \(H_*=W-W_A\).

Assume now (23), and let \(L\) be a proper primitive affine lattice subspace of dimension \(q<n\). The second inequality in (22), applied to \(L\), says
\[
 G\geq
 \min\left\{
 G_L^{\mathrm{rel}}+\frac{W-W_L}{2},
 \ 2^{n-q}G_L^{\mathrm{rel}}
 \right\}.
\tag{43}
\]
Writing \(c:=n-q\geq1\), strict no-rank-drop gives
\[
 G_L^{\mathrm{rel}}+\frac{W-W_L}{2}
 >\frac{1-2^{-c}}2W
 \geq\frac W4
 >G.
\tag{44}
\]
Since (43) implies that its displayed minimum is at most \(G\), the other entry must be at most \(G\). This proves (24).

It remains to prove the packet conclusion. Accepted fact `fbeb0a501b268d12` proves directly that every one-factor packet has
\[
 \mathcal E(\Pi)\leq G.
\tag{45}
\]
Thus if \(q=n\), then \(\operatorname{Sc}_n(\Pi)=\mathcal E(\Pi)\leq G\), without (23). Suppose \(q<n\). If \(\mathcal E(\Pi)=0\), (27) is immediate, so assume it is positive. The one-factor construction in the proof of accepted fact `fbeb0a501b268d12` uses
\[
 D_+:=\{u\in\Delta\cap\mathbb Z^q:g(u)>0\},
 \qquad
 t_u:=g(u)^d,
\tag{46}
\]
and produces an intrinsic integer center \(c\in\mathbb Z^q\cap\operatorname{conv}D_+\) with relative halfspace balance \(2^{-q}\mathcal E(\Pi)\). With
\[
 L:=b+\operatorname{im}_{\mathbb R}U,
 \qquad
 m_*:=\Phi(c),
 \qquad
 E_*:=\Phi(D_+),
 \qquad
 t_{\Phi(u)}:=t_u,
\tag{47}
\]
that proof also establishes \(0<t_z\leq a_z\), and its affine selector \(x(u)\) satisfies
\[
 x(c)\in
 \bigcap_{\alpha\in\Lambda_{m_*}(E_*)}
 \sum_{z\in E_*}\alpha_z\mathsf M_{t_z}(C_z).
\tag{48}
\]
The rank assumption makes \(\Phi:\mathbb R^q\to L\) an affine isomorphism. Therefore every proper relative closed halfspace of \(L\) pulls back to a proper closed halfspace of \(\mathbb R^q\), so the tuple (47)-(48) is relatively \(2^{-q}\)-balanced. Also, as proved in `fbeb0a501b268d12`, \(L\) is a proper primitive affine lattice subspace even when \(U\mathbb Z^q\) is nonsaturated. Consequently
\[
 G_L^{\mathrm{rel}}\geq\mathcal E(\Pi).
\tag{49}
\]
Combining (24) and (49) gives
\[
 \operatorname{Sc}_n(\Pi)
 =2^{n-q}\mathcal E(\Pi)
 \leq2^{n-q}G_L^{\mathrm{rel}}
 \leq G,
\]
proving (27). The argument has separately covered zero energy, zero individual factor values, full rank, proper rank, and nonsaturated embeddings. It uses no statement about multifactor packets, so the final scope limitation is exact.

## External sources

none
