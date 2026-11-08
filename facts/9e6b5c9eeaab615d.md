---
fact_id: 9e6b5c9eeaab615d
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-ordinary-maximal-depth-minkowski-rigidity
depends_on: ["4e868f774de77608", "755cb08c379113cc", "1269c554ca9a41b8"]
verifier_run: 142b305adb8ad3be
target_match: null
---

## Source

- [6c56e9569b9982d7](../candidates/6c56e9569b9982d7.json), Opening, (1)–(2), §3, (7)–(11), and §6, (13).
- [4202609a15fa8f99](../candidates/4202609a15fa8f99.json), §1, (2)–(4) and final paragraph.

## Statement

Let $K,L,N\subset\mathbb R^d$, $d\ge1$, be compact convex bodies with nonempty interiors, and suppose $N\supseteq sK+tL$ for $s,t>0$. Write $A(B)$ for the maximum raw ordinary closed-halfspace depth in $B$. Then
$$
A(N)^{1/d}\ge sA(K)^{1/d}+tA(L)^{1/d}.
$$
Equality holds exactly when $N=sK+tL$ and $K,L$ are positively homothetic. If equality holds, let $g_K,g_L,g_N$ be their unique deepest points. Then $g_N=sg_K+tg_L$ and
$L=r(K-g_K)+g_L$ for $r=(A(L)/A(K))^{1/d}$.
For every active direction at $g_N$, the entire captured cap of $N$ is the weighted Minkowski sum of the caps of $K,L$ through $g_K,g_L$ in the same direction.

Equivalently, under this containment, equality in the maximal-depth-root inequality is the same as $|N|^{1/d}=s|K|^{1/d}+t|L|^{1/d}$. The statement applies in parallel $d$-dimensional affine planes, with intrinsic volumes and the same Minkowski containment. In particular, $s=t=1/2$ gives rigidity at an actual compatible midpoint.

## Proof

For any positive body, compactness and continuity of the through-cap minimum give a deepest mark. Boundary marks have depth zero by support and any own interior mark has positive depth by an inball. For any positive ordinary fiber, a minimizing through-cap at an interior mark has that mark as its section centroid. Apply the one-fiber calculation of 1269c554ca9a41b8 §2 with fixed base coefficient and $(u',b')=(w,w\cdot y)$ for a cap through $y$. The trace is proper, so the two-sided derivative is its positive coarea times $w$ dotted with the section centroid minus $y$. Since the variation always contains $y$, the derivative vanishes at a minimizing direction for every $w$. A minimum cap at the midpoint of two distinct deepest marks would either have different thresholds at the two marks, or be a minimizing cap through both. In the first case the larger endpoint threshold cuts off a strictly smaller cap, since the open slab contains an interior point of their segment. In the second case the same section would have two distinct centroids. Both contradict maximality.

Put $g=sg_K+tg_L$, which is interior to $N$ because the sum of inballs around the endpoint marks contains a ball about $g$. The pointwise root inequality in 4e868f774de77608 gives $D_N(g)^{1/d}\ge sA(K)^{1/d}+tA(L)^{1/d}$, where $D_N$ denotes raw ordinary depth. To apply the fact, take the full-dimensional real-base hull of $\{0\}\times K$ and $\{1\}\times L$, use its fiber at $t/(s+t)$, dilate by $s+t$ and use the containment in $N$. In particular this proves the asserted inequality for $A(N)$. If that inequality is tight, then $g$ attains $A(N)$ and equals $g_N$.

For each unit $u$ let $K_u,L_u,N_u$ denote the caps in direction $u$ through $g_K,g_L,g$, respectively. Addition of the cap inequalities gives $sK_u+tL_u\subseteq N_u$. Classical Brunn–Minkowski gives
$$
|N_u|^{1/d}\ge |sK_u+tL_u|^{1/d}\ge s|K_u|^{1/d}+t|L_u|^{1/d}
  \ge sA(K)^{1/d}+tA(L)^{1/d}.
$$
At equality in the root inequality, for any active direction at $g$ the chain is an equality throughout. Positivity of the coefficients makes both endpoint cap volumes equal to the corresponding own maxima. All three caps have positive volume. Equal volumes and inclusion give $N_u=sK_u+tL_u$, since a proper inclusion of compact convex bodies of positive volume increases volume. The Brunn–Minkowski equality case gives $L_u=r K_u+b_u$, with the same $r=(A(L)/A(K))^{1/d}$ for each active $u$. For the classical equality case used here, see Theorem 4.1 and the ensuing equality discussion in [Gardner, The Brunn–Minkowski Inequality](https://doi.org/10.1090/S0273-0979-02-00941-2).

The face minimizing $u\cdot x$ in each endpoint cap is the section by the through-mark cutting hyperplane. The positive homothety maps one such face to the other. The proper-trace variation above makes their centroids $g_K,g_L$, so $b_u=g_L-rg_K$ for every active $u$.

Apply 755cb08c379113cc to the compatible one-base family $\{0\}\times N$. Its anchored capacities are the ordinary cap volumes on $N$. We obtain a positively balanced finite collection of active directions. Their through-mark closed halfspaces cover $\mathbb R^d$ at any mark, since a point outside all of them would have a negative weighted sum of margins. Taking unions at $g_K$ and $g_L$ gives $L=r(K-g_K)+g_L$ from the same identity on each cap. Taking the union of the corresponding $N_u=sK_u+tL_u$ at $g$ shows $N\subseteq sK+tL$. The reverse containment was assumed.

Conversely, if $L=rK+b$ for $r>0$ and $N=sK+tL$, then $N=(s+tr)K+tb$. Translation invariance and $d$-homogeneity of raw depth give equality. The volume-root equivalence follows from ordinary Brunn–Minkowski and strict volume increase under proper inclusion, which give exactly the same equality conditions. For parallel planes choose origins for $K$ and $L$ and take the $s,t$ weighted sum of those origins for $N$. This puts all three bodies in the same vector space and preserves the containment and every cap measure.
