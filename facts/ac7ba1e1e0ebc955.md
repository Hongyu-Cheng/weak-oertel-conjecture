---
fact_id: ac7ba1e1e0ebc955
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-hereditary-depth-distal-cap-trimming
depends_on: ["6769574fc1bd9f8d"]
verifier_run: f0a8bb97b4696466
target_match: null
---

## Source

- [cd833c78fb705a2e](../candidates/cd833c78fb705a2e.json), Abstract hereditary-depth formulation, displayed inequality and uniform-volume specialization; Ordinary convex-body theorem (1)–(2); Proof by convex distal trimming; The three-largest-cap consequence (3), dimension-one case, and simplex example.
- [eb88c1c4c388daab](../candidates/eb88c1c4c388daab.json), §3, ordinary cover bound (7) and its proof through the sentence citing §1 of 64b80eee72258d21; §4.2, coefficient definition and ordinary ordered-mass formula (12) through the sentence on tied cap volumes, restricted to m≥3.
- [64b80eee72258d21](../candidates/64b80eee72258d21.json), §1, ordinary positive-part cover bound (1) and its proof.

## Statement

Let $D\ge1$, let $\mu$ be a finite nonnegative Borel measure on $\mathbb{R}^D$ with convex support $K=\operatorname{supp}\mu$, and suppose every affine hyperplane has zero $\mu$-mass. Assume there is a fixed $g>0$ such that every closed convex subset $L\subseteq K$ of positive $\mu$-mass contains a point $y$ satisfying $\mu(L\cap H)\ge g\mu(L)$ for every closed halfspace $H$ containing $y$.

Let $H_1,\ldots,H_m$ be a finite cover of $K$ by closed halfspaces with nonzero normals, with $m\ge1$, and let $A_i=\mu(H_i)$. For every $\alpha\ge0$,
$$
\mu(K)\le\sum_{i=1}^m(A_i-\alpha)_+ + \frac{\alpha}{g},
\qquad x_+=\max\{x,0\}.
\tag{1}
$$

For ordinary volume on a convex body $K\subseteq\mathbb{R}^D$, write $V=\operatorname{vol}_D(K)$ and $\gamma_D=(D/(D+1))^D$. Then (1) holds with $g=\gamma_D$ and $A_i=\operatorname{vol}_D(K\cap H_i)$. In particular, for $a=\min_i A_i$,
$$
\sum_{i=1}^m A_i-V\ge(m-1/\gamma_D)a.
\tag{2}
$$
Arrange the cap masses in decreasing order and append zeros if $m<3$. For $D\ge2$,
$$
A_{(1)}+A_{(2)}+(1/\gamma_D-2)A_{(3)}\ge V,
\tag{3}
$$
where $0<1/\gamma_D-2<1$. For $D=1$, $A_{(1)}+A_{(2)}\ge V$.

## Proof

For $\alpha=0$, (1) is the cover union bound. Let $\alpha>0$. Write $H_i=\{x:u_i\cdot x\ge b_i\}$ with $u_i\ne0$. The function $t\mapsto\mu(\{x:u_i\cdot x\ge t\})$ is continuous by dominated convergence and the nullity of its boundary hyperplanes. It tends to zero as $t\to+\infty$ by finiteness of $\mu$. Thus for every $i$ with $A_i>\alpha$, there is a finite $t_i\ge b_i$ such that this function at $t_i$ equals $A_i-\alpha>0$.

Set $L=K\cap\bigcap_{i:A_i>\alpha}\{x:u_i\cdot x\le t_i\}$. This is closed and convex. Each removed region has mass $A_i-\alpha$, since the cutting hyperplane has zero mass. The union bound gives $\mu(L)\ge\mu(K)-\sum_i(A_i-\alpha)_+$. If the right-hand side is nonpositive, (1) follows. Otherwise $\mu(L)>0$. Every original $H_i$ has mass at most $\alpha$ within $L$. For an uncut cap this follows from $A_i\le\alpha$. For a cut cap, the full retained band $K\cap\{b_i\le u_i\cdot x\le t_i\}$ has mass $A_i-(A_i-\alpha)=\alpha$ and contains $L\cap H_i$. The depth point guaranteed for $L$ belongs to some $H_i$ because the halfspaces cover $K$. Hence $g\mu(L)\le\mu(L\cap H_i)\le\alpha$, which yields (1).

For ordinary volume, every closed convex $L\subseteq K$ of positive $D$-volume is compact and full-dimensional, hence is a convex body. Apply accepted fact `6769574fc1bd9f8d` to $L$ at metronoid mass $\operatorname{vol}_D(L)$. At full mass the only admissible density is $1$ almost everywhere, so the metronoid consists of the centroid of $L$, and the fact gives the hereditary premise with $g=\gamma_D$. For the centroid form in the primary source, see Theorem 2 and its proof in §3, pp. 1259–1260, in Branko Grünbaum’s [*Partitions of Mass-Distributions and of Convex Bodies by Hyperplanes*](https://msp.org/pjm/1960/10-4/pjm-v10-n4-p18-p.pdf).

Taking $\alpha=a$ in (1) gives (2) because each $A_i-a$ is nonnegative. Taking $\alpha=A_{(3)}$ gives (3) because the positive-part sum equals $A_{(1)}+A_{(2)}-2A_{(3)}$. The identity includes ties and zero padding. For $D\ge2$, the first two binomial terms and the strict exponential bound give $2<(1+1/D)^D<e<3$. For $D=1$, take $\alpha=A_{(2)}$ and use $1/\gamma_1=2$.

For a $D$-simplex, at least one barycentric coordinate is at least $1/(D+1)$ at every point. The cap at vertex $v_i$ defined by that threshold on $\lambda_i$ is the image of the simplex under homothety about $v_i$ by factor $D/(D+1)$. Each cap therefore has volume $\gamma_DV$. Substitution gives equality in (1) at $\alpha=\gamma_DV$, in (2) for this $m=D+1$, and in (3) for $D\ge2$ or the two-largest bound for $D=1$.
