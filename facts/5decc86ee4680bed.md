---
fact_id: 5decc86ee4680bed
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w35-tilt-full-space-mean-balance
depends_on: ["0b2fbdaf8d3134a0", "5aeb5916857f97a9", "efc6257ea1f83bc1", "2fe966187abc0788", "d90ba05577427854", "20210aa9d661295a"]
verifier_run: 5c1aaa6e288c3745
target_match: null
---

## Source

- [137cd11c6631be8a](../candidates/137cd11c6631be8a.json), 137cd11c6631be8a:02 §§1–4, (1)–(10), unpenalized joint tilted mean balance.

## Statement

Let $P$ be a finite nonempty complete base in an affine lattice, with positive compact convex $d$-fibers $K_z$ ($d\ge1$) satisfying the anchored Minkowski inclusions $\sum_z\lambda_z K_z\subseteq K_p$ whenever $\lambda_z\ge0$, $\sum_z\lambda_z=1$, and $\sum_z\lambda_z z=p\in P$. Put $S=\bigcup_z\{z\}\times K_z$, $C=\operatorname{conv}S$, $dm=\sum_z\delta_z\otimes dX|_{K_z}$ and $M=m(S)$. All affine functions are relative to $\operatorname{aff}P\times\mathbb R^d$. Let $\varepsilon>0$, $N=d+1$, and $G(u)=(M^{-1}\sum_z\int_{K_z}[u\cdot(X-g_z)]^2\,dX)^{1/2}$, where $g_z$ are the fiber centroids. Use marked energy $E_K(y)=\inf_a\int_K[1+a\cdot(X-y)]^{-d-1}\,dX$ over denominators strictly positive throughout $K$, extended by zero on $\partial K$. For a parameter $L$ put $f(z,y)=[L(z,y)E_{K_z}(y)/M]^{1/N}$ and use the infimum $b_L(p,y)$ of mixed masses of the caps
$$
a\cdot(z-p)+u\cdot(X-y)\ge-\varepsilon G(u)f(p,y),\qquad u\ne0,
$$
and of closed pure-base caps containing $p$ (including the whole-base trace). Write $b_{\rm base}(p)$ for the latter minimum alone. Let $Q=\max_S b_L$, $I$ be the bases of maximizing marks, $J=\{p\in I:b_{\rm base}(p)>Q\}$, $A=I\setminus J$, and $k(T)$ count inherited lattice parities occupied by $T$, with $k(\varnothing)=0$. Assume $L$ is affine and strictly positive on $C$, with $M^{-1}\int_S L^{-r}\,dm=1$ for a fixed $r\ge d$.

If $(K,L)$ is a joint local minimizer of $Q/M$ over actual positive compatible families on the same base and their positive normalized full-affine parameters, and $0<Q/M<1/k(P)$, then $J$ is nonempty and
$$
\frac{\int_S wL(w)^{-r-1}\,dm}{\int_S L(w)^{-r-1}\,dm}
\in\operatorname{conv}\{(p,y)\in S:p\in J,\ b_L(p,y)=Q\}\cap\operatorname{relint}C .
$$

## Proof

The energy-root continuity and concavity of 0b2fbdaf8d3134a0 and 5aeb5916857f97a9 give a continuous concave extension of $f$ to the real hull, using the increasing concave weighted geometric mean of the energy root and $L$. To apply the closed-quantile superlevel argument of 0b2fbdaf8d3134a0, one can whiten the fixed positive pooled covariance, so that $G$-unit continuous normals are Euclidean-unit normals in the new coordinates. Equivalently each threshold is affine minus the concave $f$ times a fixed positive constant. Thus the $Q$-superlevel is convex and closed, and $I$ is lattice-complete. Own-boundary depth is zero by that fact's supporting-plane argument. On each sampled fiber the depth is continuous: for any unit continuous normal and any base tilt, varying the mark $y$ or $f$ moves the threshold by at most the displacement in $y$ plus $\varepsilon\max_{\|u\|=1}G(u)$ times the displacement in $f$. The sum of the maximal cross-section areas in the bounded fibers bounds the resulting mass change per unit threshold displacement, and the bound passes to the infimum. The same argument gives uniform fixed-family continuity under uniform changes in $f$.

First consider an all-atomic configuration. By efc6257ea1f83bc1, $I$ has a cover by $m\le k(I)\le k(P)$ closed pure-base caps of mass $Q$. The hypothesis $Q/M<1/k(P)$ gives $(Q/M)m<1$. Apply 2fe966187abc0788 to these actual caps. It provides compatible nested erosions, along which every covering cap has normalized mass strictly below $Q/M$. On the eroded hull, replace $L$ by $c_sL$, where $c_s=(M_s^{-1}\int_{S_s}L^{-r}\,dm_s)^{1/r}$. This is legal because the hull is nested, and $c_s\to1$ by boundedness of the old inverse power and volume convergence. By inclusion monotonicity of energy (d90ba05577427854), $f_s(w)\le f(w)(c_s M/M_s)^{1/N}$ at retained marks, and $G_s/G\to1$ uniformly on the unit sphere by convergence of moments. Comparing caps at retained marks with these old caps, their mass can only grow by a uniform $o(1)$ threshold slab, since the bodies are nested. This preserves the normalized gap on all the finitely many old nondeepest bases. The fixed pure-base cover bounds the old deepest bases independently of the parameter, so this is an arbitrarily small strict descent. Hence the original local minimum cannot have $J=\varnothing$.

Now write $g$ for the displayed tilted mean and $W_J$ for the displayed compact set of proper deepest marks. If $g\notin\operatorname{conv}W_J$, choose an affine $\psi$ with $\psi(g)=0$ and $\psi\le-\eta<0$ on $W_J$. Use the exact positive normalized family
$$
L_t=\left[M^{-1}\int_S (L+t\psi)^{-r}\,dm\right]^{1/r}(L+t\psi).
$$
Uniform positivity and $\int_S L^{-r-1}\psi\,dm=0$ give $L_t=L+t\psi+o(t)$ uniformly. There is a fixed neighborhood of $W_J$ on the union of its sampled fibers where $L_t<L$ for small positive $t$. At an old proper deepest mark, apply 20210aa9d661295a with $\delta=\varepsilon f(p,y)$ and $G$ to fix an attaining cap with proper own trace. A strict decrease in $L$ raises its threshold and removes positive own volume, so the new depth there is strictly below $Q$. At all other points in the neighborhood monotonicity gives new depth no greater than old depth, which is already strictly below $Q$. Outside the neighborhood at bases in $J$ and at every base outside $I$, the old compact gap and uniform slab estimate preserve depth strictly below $Q$. The new depth attains its maximum on each fiber by the continuity just proved. Each old atomic base remains bounded above by the unchanged pure-base value $Q$. Thus either $Q_t<Q$, or $Q_t=Q$ and all new maximizing bases are atomic. In the latter case apply the arbitrarily small erosion already constructed, now using $L_t$ as the starting affine parameter. The parameter step and the erosion both fit within any prescribed local-minimum neighborhood. This contradicts minimality in both cases.

Finally a nonconstant supporting affine functional of $C$ has a strictly positive gap on a set of positive sampled volume: an affine functional agreeing with its maximum on every sampled fiber would agree on their hull. The tilt has positive density throughout the sampled interiors, so $g$ lies in the relative interior.
