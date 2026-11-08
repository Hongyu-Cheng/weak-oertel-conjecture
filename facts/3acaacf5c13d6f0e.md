---
fact_id: 3acaacf5c13d6f0e
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-zero-endpoint-facet-moment-and-descent
depends_on: ["6769574fc1bd9f8d", "b319e7dcda1486e9"]
verifier_run: 52b5ffbf7c45fd32
target_match: null
---

## Source

- [6ac02348e3ceb9a9](../candidates/6ac02348e3ceb9a9.json), 6ac02348e3ceb9a9:02 Proof §3, (7)–(13).
- [6ac02348e3ceb9a9](../candidates/6ac02348e3ceb9a9.json), 6ac02348e3ceb9a9:04 Proof §5, nearest-point separation and captured-volume derivative.
- [568f7cf028ec23b6](../candidates/568f7cf028ec23b6.json), 568f7cf028ec23b6:02 §1, (1), one-sided supporting-plane derivative.

## Statement

Let $d\ge2$, with positive compact convex fibers $A,K,B$ at $-1,0,1$ and $(A+B)/2\subseteq K$. For a cap $u\cdot(x-y)+\alpha z\ge0$ through $y\in\operatorname{int}K$, $u\ne0$, suppose the $A,K$ cuts are proper with areas $t,s>0$ and centroids $c_A,c_K$, and the $B$ cut is at an outside supporting facet $F$ of area $M>0$. Use intrinsic surface measure $dS=d\mathcal H^{d-1}|_F$. Let $\mathsf M_t(F)$ be the set of means of densities $0\le\theta\le1$ on $F$ of mass $t$, defined for $0<t\le M$. Put $b_*=(2t+s)y-tc_A-sc_K$. The inequalities
$$
t[w\cdot(c_A-y)-\beta]+s\,w\cdot(c_K-y)+\int_F[w\cdot(x-y)+\beta]_+\,dS\ge0
\qquad(w\in\mathbb R^d,\ \beta\in\mathbb R)
$$
are equivalent to $t\le M$ and $b_*\in t\mathsf M_t(F)$. The equivalent selector equation is
$$
t(c_A-y)+s(c_K-y)+\int_F\theta(x)(x-y)\,dS=0,\qquad \int_F\theta\,dS=t.
$$
For $t<M$, any admissible prescribed mean is attained by a convex combination of at most $d$ indicators of actual intrinsic volume-$t$ caps of $F$. At a relative boundary mean every selector is the same such indicator almost everywhere. For $t=M$ the selector is the full facet, and if also $s=t$ then $E_A,F$ are translates, $E_K=(E_A+F)/2$, and $y=c_K$.

For $0<t\le M$ and $b_*\notin t\mathsf M_t(F)$, let $p$ be its nearest point in that set and put $w=b_*-p$. With $\delta$ any minimizer of $\int_F[w\cdot x+\delta]_+\,dS-t\delta$, choose $\beta=\delta+w\cdot y$. This perturbation at the fixed mark has right capture derivative $-\|b_*-p\|^2/\|u\|$. Its continuous-normal increment $w$ is tangent to the facet, and the perturbed cap has strictly smaller mass for all sufficiently small positive sizes.

## Proof

In the inequalities take $w=0,\beta=1$, obtaining $t\le M$. On the $(d-1)$-dimensional affine hull of $F$, use the compact convex moment body and the top-cap support formula (1) of 6769574fc1bd9f8d, transported by an affine isometry with intrinsic volume. The dual formula for its unnormalized support is
$$
h_{t\mathsf M_t(F)}(w)=\min_\delta\left(\int_F[w\cdot x+\delta]_+\,dS-t\delta\right).
$$
Indeed every mass-$t$ selector gives a linear moment bounded by this hinge objective for every $\delta$. For a nonflat direction and $t<M$ take minus the upper volume-$t$ quantile for $\delta$ and use that cap indicator to attain equality. For a constant value $w\cdot x=c$ use $\delta=-c$; at full mass any $\delta\ge-\min_F w\cdot x$ works. In the proper nonflat case the bathtub integrand $(\mathbf 1_{\rm cap}-\theta)(w\cdot x+\delta)$ is strictly positive wherever a selector differs from the cap indicator off the null cutting plane, so every maximizing selector equals that indicator a.e.

Substitute $\delta=\beta-w\cdot y$. The entire family of inequalities reads $\int_F[w\cdot x+\delta]_+\,dS-t\delta\ge w\cdot b_*$ for all $w,\delta$. The dual formula and separation of the compact convex body give exactly membership and the stated selector equation. The equation automatically respects the correct affine plane: $u\cdot c_A=u\cdot y+\alpha$, $u\cdot c_K=u\cdot y$, hence $u\cdot b_*=t(u\cdot y-\alpha)$.

For $0<t<M$ the set of intrinsic volume-$t$ cap centroids is compact. In a converging sequence of unit tangential normals the levels are bounded; every convergent level subsequence tends to the unique volume-$t$ level by dominated convergence, since each cutting plane is null and the tail is strictly decreasing between the two support levels. Dominated convergence then gives centroid continuity. Its convex hull is compact by intrinsic Carathéodory, and it has the same support function as the moment body by the top-cap formula. Thus it equals the body, with at most $d$ cap indicators needed. This body has full relative dimension because its constant-selector mean has strictly lower support value than a top cap in every nonflat direction. The strict gap is uniform on the unit tangent sphere by continuity and compactness, and separation gives a relative ball around that mean. Every relative boundary point has a nonflat supporting direction, so the uniqueness of the selector follows from the bathtub integrand above.

At $t=M$ mass forces $\theta=1$ a.e. If also $s=t$, the midpoint inclusion and Brunn–Minkowski in dimension $d-1$ give equality of areas throughout. A proper inclusion of full-dimensional compact convex sets in the same section plane would strictly increase area. Hence $E_K=(E_A+F)/2$. The positive-volume Brunn–Minkowski equality case gives homothety, with equal areas making it translation; for intervals this follows from equal length directly. Then $c_K=(c_A+c_F)/2$ and the selector equation gives $y=c_K$.

For the descent assertion, projection on the compact convex moment set gives $w\cdot(z-p)\le0$ for every point $z$ there by differentiating squared distance along the segment from $p$ to $z$. Thus $h(w)-w\cdot b_*=-\|b_*-p\|^2$. At the stated minimizing hinge threshold the left side of the all-direction inequality equals that negative value. By the proper and outside-supporting fixed-body slice calculation in b319e7dcda1486e9, with normalized margin and perturbation divided by $\|u\|$, its value divided by $\|u\|$ is the actual capture derivative. The affine plane identity puts $w$ in $u^\perp$. The negative derivative gives the strict decrease.
