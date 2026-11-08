---
fact_id: a67fef996fdffc7c
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-two-sided-scalar-frontier-at-body-bm-equality
depends_on: []
verifier_run: 31028e35ed8de7f1
target_match: null
---

## Source

- [8426c7487ce19740](../candidates/8426c7487ce19740.json), 8426c7487ce19740:01 §§1–4, (1)–(5), four closed-section status cases and lattice realizations.

## Statement

Fix $d\ge1$, $N\ge2$, and $\theta_j>0$ with $\sum_j\theta_j=1$. In coordinates $(t,y)\in\mathbb R\times\mathbb R^{d-1}$ let $H_+=\{t\le0\}$ and $H_-=\{t\ge0\}$. For positive-volume compact convex bodies $A_j$, prescribe their volume roots $a_j=|A_j|^{1/d}>0$, fractions $p_j=|A_j\cap H_+|/|A_j|\in[0,1]$, and for each zero-volume closed section whether it is nonempty (tangent) or empty. Write
$$
s=\sum_j\theta_ja_j,\qquad c=\sum_j\theta_ja_jp_j^{1/d},
\qquad r=\sum_j\theta_ja_j(1-p_j)^{1/d},\qquad U=(s^d-r^d)^{1/d}.
$$
For a convex body $K\supseteq\sum_j\theta_jA_j$ with $|K|=s^d$, put $u=|K\cap H_+|^{1/d}$. Let $E_+$ and $E_-$ mean that at least one respective closed input section is empty. The possible $u$ are exactly

- $[c,U]$ if neither $E_+$ nor $E_-$ holds.
- $[0,U)$ if only $E_+$ holds and some $p_j>0$, and $\{0\}$ if all $p_j=0$ in that case.
- $(c,s]$ if only $E_-$ holds and some $p_j<1$, and $\{s\}$ if all $p_j=1$ in that case.
- $[0,s]$ if both hold.

Every value is realized by translated positive homothets of one body and $K$ equal to their weighted sum. In $d=1$ the first interval is a singleton. For two weights $1/2$ these are actual three integer fibers of the lift at bases $-1,1$ with the same ambient cut. More generally positive rational weights admit an integer source and affinely independent integer bases in the lift, with possible additional integer fibers unrestricted.

The strictness mechanism also holds without the volume equality: whenever all closed sections on one side are nonempty, some input has a positive support gap from the cutting plane on that side, and the target cut is proper, the corresponding side Brunn–Minkowski lower bound is strict.

## Proof

If every closed input section on $H_+$ is nonempty, their weighted Minkowski sum is contained in $K\cap H_+$. By Brunn–Minkowski for nonempty compact convex sets, including tangent sections by outer thickening and continuity, $u\ge c$. Similarly no empty section on $H_-$ implies $|K\cap H_-|^{1/d}\ge r$, hence $u\le U$. The interval is nonempty since the $\ell_d$ triangle inequality applied to the vectors $\theta_j a_j(p_j^{1/d},(1-p_j)^{1/d})$ gives $(c^d+r^d)^{1/d}\le s$.

Suppose only $E_+$ holds. An input with empty $H_+$ section has $\min_{A_i}t=\delta>0$. All $H_-$ input sections are nonempty, and their weighted sum is full dimensional because one of them is $A_i$. It lies in $\{t\ge\theta_i\delta\}$ and has volume at least $r^d$. A proper target cut has an interior point of $K$ on $t=0$, by a segment between interior points on opposite sides. A neighborhood of that point in $K$ provides positive volume in the residual strip $0<t<\theta_i\delta$, disjoint from the sum. Thus the side bound is strict whenever the target cut is proper, independently of the whole-volume equality. If some $p_j>0$ then $U>0$, and $r>0$ since $p_i=0$. So $u=U$ would be a proper target cut and contradict strictness. If all $p_j=0$, then $r=s$ forces $u=0$. Reflect $t$ for the symmetric case. If both types of emptiness occur, $0\le u\le s$ always.

For realization in $d\ge2$, choose a $(d-1)$-body $E$ containing zero with volume one. For $\tau\in[0,1]$ put $h_\tau(t)=(1-\tau)t+\tau(1-t)$ on $[0,1]$, $J_\tau=\int_0^1 h_\tau(t)^{d-1}\,dt$, and define the body $D_\tau$ by sections $J_\tau^{-1/(d-1)}h_\tau(t)E$. These sections give a convex body since the radius function is nonnegative affine. It has volume one, with prefix function $F_\tau(q)=J_\tau^{-1}\int_0^q h_\tau(t)^{d-1}\,dt$ for $q\in[0,1]$. The prefix is strictly increasing and jointly continuous in $\tau,q$. Its quantiles $q_j=F_\tau^{-1}(p_j)$ vary continuously in $\tau$ by compactness of $[0,1]$ and uniqueness of the inverse. Take
$$
A_j=a_j(D_\tau-q_j e_t),\qquad
K=s(D_\tau-\bar q e_t),\qquad
\bar q=s^{-1}\sum_j\theta_j a_j q_j .
$$
The identity $\sum_j b_j D_\tau=(\sum_jb_j)D_\tau$ for $b_j>0$ proves the exact sum and volume. The prescribed fractions are the prefixes, and $q_j=0,1$ gives tangent closed sections at zero-volume endpoints. The target root is $sF_\tau(\bar q)^{1/d}$. At $\tau=0$ the prefix is $q^d$, giving $u=c$. At $\tau=1$ it is $1-(1-q)^d$, giving opposite root $r$, hence $u=U$. Continuity attains every intermediate value. In $d=1$ take $D=[0,1]$ and $F(q)=q$ in the same construction, giving $c=U$.

Extend each prefix continuously by zero below $0$ and one above $1$. If only $E_+$ holds, use the $\tau=1$ shape (the interval for $d=1$), changing precisely the quantiles prescribed to be empty on $H_+$ from $0$ to $-\delta$, $\delta>0$. Their support gaps are strictly positive, their opposite sections stay nonempty, and all other endpoint statuses are unchanged. The target $\bar q$ decreases continuously and linearly from its tangent value, reaching nonpositive values for large $\delta$. The target root ranges over $[0,U)$ when $U>0$, since the tangent $\bar q$ is then in $(0,1)$, and is identically zero when $U=0$. If only $E_-$ holds, use the $\tau=0$ shape and change precisely the prescribed $1$ quantiles to $1+\delta$, giving the reflected conclusion. If both hold, use one fixed shape and set the empty-section quantiles to $-\delta$ on $H_+$ and $1+\eta$ on $H_-$, $\delta,\eta>0$. In $\bar q$ their coefficients have opposite signs and are nonzero, so $\bar q$ can be any real value and the extended prefix covers $[0,1]$.

For two equal weights take the hull of the lifts of $A_1,A_2$ at $-1,1$. By unique interpolation of the two bases its integer sections are exactly $A_1,K,A_2$, with the same cap trace on each from the ambient cut $t=0$. For rational weights write $\theta_j=m_j/\sum_i m_i$ with positive integers $m_i$. Use bases $z_j=m_N e_j$ for $j<N$ and $z_N=-\sum_{j<N}m_j e_j$ in $\mathbb Z^{N-1}$. They are affinely independent: an affine dependence with coefficients $c_j$ forces $m_N c_j=m_j c_N$ for $j<N$, and their sum zero forces all coefficients zero. They give barycenter zero under the prescribed weights, and hence the lifted hull has the stated section there. The construction does not constrain other integer sections.
