---
fact_id: ae992b5eaace77ca
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-w31-triangle-outward-own-minimum
depends_on: []
verifier_run: 83bbecb350ef963a
target_match: null
---

## Source

- [2ab56d1c26a2c4f9](../candidates/2ab56d1c26a2c4f9.json), 2ab56d1c26a2c4f9:01 §3, (5)–(8).
- [b4250d3425f93191](../candidates/b4250d3425f93191.json), §2, (5)–(6), equivalent source occurrence of canonical claim 2ab56d1c26a2c4f9:01.

## Statement

Let $T$ be any nondegenerate centroid-zero triangle of area $V$, with barycentric coordinates $\lambda_i$ and covariance $\Sigma_T$ for its uniform area law. Smooth a through-centroid cap of continuous normal $u\ne0$ by averaging its ordinary areas over outward threshold displacements uniformly on $[0,h\sqrt{\kappa u^{\mathsf T}\Sigma_Tu}]$, for $\kappa>0$. Set $w=h\sqrt{\kappa/18}$. If $0<w\le 1/100$, the minimum over every continuous direction is $V(4/9+2w/3+w^2/3)$, attained exactly by positive multiples of the three normals $\nabla\lambda_i$.

## Proof

For a uniform point of a triangle the barycentric coordinates have second moments $1/6$ on the diagonal and $1/12$ off the diagonal, by integrating monomials on the standard two-simplex. Thus if the centered vertex values of $u\cdot x$ are $a_i$ with $\sum_i a_i=0$, its variance is $\sum_i a_i^2/12$. In particular $\operatorname{Var}(\lambda_i)=1/18$.

For a single positive vertex write the values $a,-a(1+s)/2,-a(1-s)/2$ with $a>0$ and $|s|\le1$. The cap at threshold zero is a vertex triangle of area fraction $4/(9-s^2)$ by multiplication of the two intercepted edge ratios. If $|s|\le1/2$, the width $H=h\sqrt{\kappa u^{\mathsf T}\Sigma_Tu}$ satisfies $H/a=\eta\sqrt{1+s^2/3}\le2w<1/4$, where $\eta=3w/2$. The next largest vertex value is at most $-a/4$. Therefore each displaced cut still isolates this vertex, and displacement $r$ multiplies its fraction by $(1+r/a)^2$. Averaging gives
$$
\frac{4}{9-s^2}\left(1+\eta\sqrt{1+s^2/3}+\frac{\eta^2}{3}(1+s^2/3)\right).
$$
This strictly increases in $s^2$. At zero it equals $4/9+2w/3+w^2/3$. For $|s|\ge1/2$ the ordinary fraction is already at least $16/35$ and smoothing cannot decrease it. If two vertex values are nonnegative, scale the values to $1,b,-1-b$ with $0\le b\le1$. The complementary vertex triangle has area fraction $(1+b)^2/((2+b)(1+2b))\le1/2$ because $2(1+b)^2\le(2+b)(1+2b)$. So this case gives at least $1/2$. The boundary case of a zero vertex value is included. Finally $4/9+1/150+1/30000<16/35$. The only minima thus have two equal negative vertex values, equivalently the three stated positive rays.
