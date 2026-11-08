---
fact_id: d6c7be6baab5ec89
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-hadamard-deepest-circuit-quantile-inverse
depends_on: ["0a03438ff4e94ff8", "1fa8cb387c27b040"]
verifier_run: cd50e7c685a49b5f
target_match: null
---

## Source

- [a0fdd477aa859374](../candidates/a0fdd477aa859374.json), a0fdd477aa859374:04 §4, (5)–(7), Hadamard inverse and necessary condition.

## Statement

In the anchored quantile and touching deepest-circuit comparison, assume each selected cap mass $F_j$ has a continuous joint Hadamard directional derivative $D_j(\delta,s)$ at $(p_0,b_j)$, with feasible body directions $\delta$ and real threshold directions $s$. For every such $\delta$ and every real mass direction $a$ there is a unique $q_j(\delta,a)\in\mathbb R$ with $D_j(\delta,q_j)=a$. This is the joint Hadamard directional derivative of $Q_j$ in $(\delta,a)$; it is continuous, positively homogeneous and strictly decreasing in $a$. The directional derivative of the common raw circuit root is the unique $a_c(\delta)$ solving

$\sum_j\rho_j q_j(\delta,a_c(\delta))=0.$

It is continuous and positively homogeneous. If $M$ has a Hadamard directional derivative and the original family is a local minimum of actual maximal normalized depth $\beta$, then every feasible direction and every choice of such a circuit at each old deepest base satisfy
$$
\max_{z\in Z}\big[a_{c_z}(\delta)-\beta M'(\delta)\big]\ge0.
$$

## Proof

For a fixed feasible $\delta$, apply the uniform slab slope bounds to the two thresholds $b_j+t s_1,b_j+t s_2$ with $s_1<s_2$, at the same nearby feasible body parameter. Divide by $t>0$ and pass to the joint directional limit:

$c(s_2-s_1)\le D_j(\delta,s_1)-D_j(\delta,s_2)\le C(s_2-s_1).$

The lower bound and continuity show that $D_j(\delta,\cdot)$ decreases bijectively onto $\mathbb R$. Its inverse has reciprocal positive lower and upper decrease rates. In particular it is continuous jointly in $(\delta,a)$, by comparing to the inverse equation at any given pair and using the lower slope and continuity of $D_j$. Positive homogeneity follows by uniqueness and homogeneity of the directional derivative.

To prove the inverse derivative, let $t\downarrow0$ and let $(\delta_t,a_t)\to(\delta,a)$ with $p_t=p_0+t\delta_t$ feasible. The difference quotients

$\frac{Q_j(p_t,\tau_0+t a_t)-b_j}{t}$

are bounded by joint Lipschitz continuity. Along any convergent subsequence with limit $s$, the joint Hadamard expansion and the inverse equation imply $D_j(\delta,s)=a$. By uniqueness every subsequential limit is $q_j(\delta,a)$, establishing the joint Hadamard limit for arbitrary convergent directions.

The weighted sum of the $q_j$ is likewise continuous and strictly decreasing onto $\mathbb R$ as a function of $a$, with a uniform lower decrease rate. Its zero is therefore continuous in $\delta$ and positively homogeneous. The quotients $(\tau_c(p_t)-\tau_0)/t$ are bounded by local Lipschitz continuity. For every convergent subsequence, use the just-proved Hadamard expansions of the quantiles in the exact weighted threshold equation. The resulting limit solves the weighted inverse equation and thus equals $a_c(\delta)$. This proves the Hadamard derivative of the circuit root. Finally apply the touching global bound at the local minimum and take the right directional limit of the finite maximum after subtracting $\beta M(p_t)$. This yields the necessary inequality, without requiring linearity of any directional response.
