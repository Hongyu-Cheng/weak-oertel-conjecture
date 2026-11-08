---
fact_id: effc7ae9d169ce7b
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w35-density-minorant-retention
depends_on: ["281951e60a80792a", "d6a3cbae1da72277", "00a936d98cf18703"]
verifier_run: e8b040aafd046bec
target_match: null
---

## Source

- [046d33287d7b1ff0](../candidates/046d33287d7b1ff0.json), 046d33287d7b1ff0:05 §4 (4)–(5), retained-mass obstruction.
- [046d33287d7b1ff0](../candidates/046d33287d7b1ff0.json), 046d33287d7b1ff0:01 §1 (1), actual median target and domination.

## Statement

Let $T=\operatorname{conv}\{(0,0),(1,0),(0,1)\}$, $A=\operatorname{conv}\{(0,0),(4/5,0),(0,8/25)\}$, and $s=3/128+2^{-20}$. Let $M$ be the mixed area of the hull with fibers $(2-s)A,T,sA$ at bases $-1,0,1$. For any coupling $\pi$ of the uniform probabilities of $X$ in $(2-s)A$ and $Y$ in $sA$, put $\eta_\pi=\mathbf1_T\,dx+|sA|\operatorname{Law}_\pi((X+Y)/2)$, of mass $W=M/2+1/4096000$.

If a finite nonzero measure $\xi\le\eta_\pi$ has a point at which every containing closed halfspace has $\xi$-mass at least $(4/9)\xi(\mathbb R^2)$, then
$$
\xi(\mathbb R^2)<M/2-27/40000000,\qquad
W-\xi(\mathbb R^2)>1/4096000+27/40000000.
$$
This applies to compactly supported inverse-cube-root convex densities and to log-concave measures on any affine support.

## Proof

The exact fibers and the bound $\sup_y\inf_{H\ni y}\eta_\pi(H)<2M/9-3/10^7$ over closed planar halfspaces follow from 281951e60a80792a, with exactly these endpoint laws and transported mass $b=|sA|$. Its area identities give $b=ce$ and $M=c(2+2e-\delta)$, with $c=1/2$, $e=32s^2/125$, and $\delta=1/1024000$. Thus $W=c+b=M/2+c\delta/2=M/2+1/4096000$.

At the depth point of $\xi$, each containing cap has at least as much $\eta_\pi$-mass by measure domination. Thus $(4/9)\xi(\mathbb R^2)$ is bounded by the maximum raw depth of $\eta_\pi$. The strict gap gives the first inequality after division by $4/9$. Subtraction from $W$ gives the second.

For a density minorant with convex inverse cube-root, its positive domain is full dimensional by positive mass, and its support is contained in the compact $T$. The bounded representative lemma and d6a3cbae1da72277 give the required point. A full-dimensional log-concave measure has a log-concave density representative by Borell's affine-support characterization of log-concave Radon measures (Convex measures on locally convex spaces, Theorem 1.1 with $s=0$). Its inverse cube-root is convex by convexity and monotonicity of the exponential applied to $-(\log f)/3$, with extension by infinity at zeros. On a line a median has depth at least half the mass in ambient closed halfspaces, and on a singleton the point has full mass.
