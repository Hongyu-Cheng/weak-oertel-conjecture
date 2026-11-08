---
fact_id: f670cd39b5fbf1fd
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-mixed-inverse-power-energy-blocked-entropy-selector
depends_on: ["9ea9bc3d72c92743", "0487ae7e836ac430"]
verifier_run: ec7481ea0b0358ed
target_match: null
---

## Source

- [baefc769abdb40f1](../candidates/baefc769abdb40f1.json), baefc769abdb40f1:03 Opening argument, (2), exactly the blocked entropy maximizing marks.
- [baefc769abdb40f1](../candidates/baefc769abdb40f1.json), baefc769abdb40f1:04 Final triangle example after (2), failed global-energy selector.
- [f3dc7a372eeb1eae](../candidates/f3dc7a372eeb1eae.json), f3dc7a372eeb1eae:03 §3, exact triangle and cap.

## Statement

Use the finite positive-volume fiber model, raw mixed measure and energy of mixed-inverse-power-energy-face-minimizer. Assume the sampled fibers are actual, i.e. $C\cap(\{z\}\times\mathbb R^d)=\{z\}\times K_z$ for $z\in P$. At an occupied base $b$ let $B(b)$ be the finite-base energy of 9ea9bc3d72c92743 with exponent $N=d+1$ and masses $m_z=|K_z|$. Write $\pi_z$ for its maximizing escort probabilities and $g_z$ for the ordinary centroids. Then
$$
\max_{x\in K_b}E(b,x)=B(b),
$$
uniquely at $x_b=\sum_z\pi_z g_z\in\operatorname{int}K_b$. Hence the maximizing points over $S$ are exactly the marks $(b,x_b)$ whose bases maximize $B$ over $P$.

## Proof

Take the minimal base face $F$ for $b$. The finite-base theorem 9ea9bc3d72c92743 with $N=d+1$ gives its unique positive relative denominator $L_z=1+\alpha\cdot(z-b)$, and escort masses $e_z=m_zL_z^{-d-2}$ on the face, zero outside it, with total $B(b)$ and mean $b$. Actual convex compatibility gives $\sum_z\pi_z K_z\subseteq K_b$ for $\pi_z=e_z/B(b)$, so $x_b=\sum_z\pi_z g_z$ is in the interior by the same fact. Regard $L_z$ as an affine denominator on the face hull, constant along each fiber. It is positive there and equals one at every candidate $(b,x)$. Its energy is exactly $B(b)$, giving the upper bound for every $x$ by face restriction.

At $x_b$, the full first derivative of the face objective at this denominator is zero. In the base components this is $\sum_z e_z(z-b)=0$, and in the continuous components it is $\sum_z e_z(g_z-x_b)=0$. The face parameter domain is convex, so a stationary point of the convex objective minimizes it. The derivative is valid throughout that domain by compactness and strict positivity. Thus equality holds at $x_b$. At any other $x\in K_b$ the continuous derivative is nonzero, and a sufficiently small displacement of the continuous parameter in a decreasing direction keeps the denominator positive on the compact face hull. The face objective then strictly decreases from $B(b)$. By the equality of the face and full infima this proves strictness even at boundary marks of $K_b$. The maximizing-base conclusion follows by taking the maximum over the nonempty finite set $P$.

**Actual triangle specialization.** Take $n=1$, $d=2$, $T=\operatorname{conv}\{(2,-1),(-1,2),(-1,-1)\}$ and $V=|T|$, with fibers $T,3T,4T$ at $-1,0,1$ respectively. The lifted hull has exactly these three integer fibers: the middle trace from the endpoint-only hull is $(T+4T)/2=(5/2)T\subset3T$, and any other hull point at base zero is a combination of a point of that trace and one of $3T$. The total mixed mass is $26V$. At the endpoints $B$ equals $V$ and $16V$. At base zero the denominator row $(2/3,1,4/3)$ gives escort masses $(81/16,9,81/16)V$ and thus base balance. By strict convexity and the finite-base identities it is the minimizer and $B(0)=153V/8$. All centroids are zero, so the unique global energy maximizer is $(0,0)$. The containing closed halfspace $x_1-8z\ge0$ takes all of $T$, fraction $(2/3)^2=4/9$ of $3T$ by vertex homothety, and only a volume-null supporting face of $4T$. It has mixed mass $5V$, which is less than $(\gamma_2/2)26V=52V/9$.
