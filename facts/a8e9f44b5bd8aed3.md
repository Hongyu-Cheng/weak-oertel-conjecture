---
fact_id: a8e9f44b5bd8aed3
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-w33-sampled-peak-sharp-variation
depends_on: []
verifier_run: 361f3208cb079f2c
target_match: null
---

## Source

- [d46094c158197e98](../candidates/d46094c158197e98.json), d46094c158197e98:01 §§1–2, (1)–(7), sampled peak and sharp variation refinement.

## Statement

Let $s\ge1$ be an integer, $Q\subset\mathbb R\times\mathbb R^s$ be compact convex, and sample on a grid of spacing $h>0$. Enumerate the $N$ nonempty sampled fibers, including null ones, at consecutive grid sites. Write $w_j$ for their $s$-volumes, $T=\sum_j w_j$, $W=\max_jw_j$, and $A=\operatorname{vol}_{s+1}(Q)$, setting $T=W=0$ for an empty sample set. Then
$$
A\ge h\sum_{j=0}^{N-2}\Phi_s(w_j^{1/s},w_{j+1}^{1/s})
 \ge h\left(T-W+\frac{\operatorname{TV}(w)}{s+1}\right)\ge h(T-W),
$$
where $\Phi_s(a,b)=\sum_{k=0}^s a^kb^{s-k}/(s+1)$ and $\operatorname{TV}(w)=\sum_{j=0}^{N-2}|w_{j+1}-w_j|$. When $N\ge1$ the variation bound is equivalently
$$
A/h\ge T-\frac{s-1}{s+1}W-\frac{w_0+w_{N-1}}{s+1}.
$$
The coefficient $1/(s+1)$ is sharp.

## Proof

The projection of $Q$ is an interval when it is nonempty, so the nonempty sampled sites are consecutive. Convexity and Brunn–Minkowski, also for nonempty zero-volume endpoint sections, give on each consecutive sampled interval the volume lower bound $[(1-t)w_j^{1/s}+t w_{j+1}^{1/s}]^s$ at relative position $t\in[0,1]$. The sampled roots are concave by the same interpolation and the sampled weights are unimodal. Integrating and ignoring any unsampled outer volume gives the first bound. The integral $\int_0^1[(1-t)a+tb]^s\,dt$ is $\Phi_s(a,b)$ by the difference of powers when $a\ne b$, and by continuity when they agree. For $a\ge b$ the mixed monomials are at least $b^s$, so this integral is at least $b^s+(a^s-b^s)/(s+1)$, and reflection exchanges $a,b$.

Choose any maximizing index. In $\sum_j\min(w_j,w_{j+1})$ the indices before the peak contribute the left term and those from the peak onwards contribute the right term. This is exactly $T-W$. Summing the adjacent differences in absolute value telescopes on each side of the same peak, giving $2W-w_0-w_{N-1}$ for $N\ge1$. Empty sums and the single-fiber case give the stated conventions. A cone over an $s$-body of volume $W$ at the first sampled site to a point at the next has exactly two nonempty sampled fibers of weights $W,0$ and volume $hW/(s+1)$. Thus $T-W=0$ and $\operatorname{TV}=W$, showing sharpness. A product between two sampled sites gives equality in the basic bound as well.
