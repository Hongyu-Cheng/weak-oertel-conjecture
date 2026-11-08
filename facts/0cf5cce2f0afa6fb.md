---
fact_id: 0cf5cce2f0afa6fb
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-genuine-critical-six-triangle-chain-empty-transit
depends_on: ["21cb697a8c0c4f03"]
verifier_run: aad3a1f926500ab4
target_match: null
---

## Source

- [b4ee4b06f66fa552](../candidates/b4ee4b06f66fa552.json), b4ee4b06f66fa552:02 §4, (7)–(10), genuine critical cover and failure of transit containment.
- [b4ee4b06f66fa552](../candidates/b4ee4b06f66fa552.json), b4ee4b06f66fa552:03 §5, (11)–(13), original row compensation.

## Statement

Let $T$ be an area-one triangle with centroid $g$ and barycentric functions $\lambda_i$, and let $[-2,3]\times T$ have its six integer fibers with summed area. Use caps $H_i=\{\lambda_i(x)-2z\ge1/3\}$ and $J_i=\{\lambda_i(x)+2(z-1)\ge1/3\}$ for $i=0,1,2$. They form an actual cover, and are globally critical at $(0,g)$ and $(1,g)$, respectively, capturing fraction $4/9$ of their own fiber. Put $c=\sqrt5/3$. The one-cap residual-root obstacle at a base is the minimum of the roots of residual areas over the six caps. The sampled convex-threshold program minimizing $\sum h_z^2$ above these obstacles has the unique optimum $h_z=c$. Its nearest-neighbor positive convexity multipliers have component $\{-1,0,1,2\}$, which includes base $-1$ even though the strict residual there for every $H_i$ is empty. Thus nonempty strict residuals at all positive-multiplier transit nodes are not automatic.

For the original normalized KKT terminal row from base $0$, the probabilities in base order are $(2,2,2,1,1,1)/9$. For the actual residual roots $f=(0,0,c,1,1,1)$ of any $H_i$, the signed difference $\sum_z\theta_z f_z-f_0=1/3-7\sqrt5/27<0$, although the empty transit node contributes a positive $2c/9$ to its second-difference representation.

## Proof

The cap $H_i$ is strictly full at $-2,-1$, gives the canonical upper barycentric cap at $0$, and is strictly empty at $1,2,3$. The cap $J_i$ is its reflection under $z\mapsto1-z$. The canonical cap has area $(2/3)^2=4/9$. At each of the two middle bases the three corresponding traces cover $T$ because one barycentric coordinate is at least $1/3$. The remaining bases are fully covered. The three continuous normals at either middle source sum to zero because $\sum_i\lambda_i=1$. Each row is regular since its own trace is proper and all other traces are strictly full or strictly empty. Each of the six caps has mass $22/9$, so the exact six-triangle depth theorem makes it genuinely critical at its stated mark. The minimum residual-root obstacles are therefore $(0,0,c,c,0,0)$.

Sampled convexity on these consecutive bases is equivalent to $\Delta h_j=h_{j-1}-2h_j+h_{j+1}\ge0$ at the interior bases: adjacent slopes are nondecreasing, so a supporting slope between the adjacent slopes at an interior base (one-sided at an endpoint) gives every nonlocal inequality by telescoping. Conversely the local support inequality gives both adjacent comparisons and hence $\Delta h_j\ge0$. The feasible constant $c$ gives attainment since objective sublevels are compact. Strict convexity makes the optimizer unique. Reflection then forces it to have the form $(a,b,v,v,b,a)$, with $v\ge c$. The two relevant second differences give $b\ge v$ and $a-b\ge b-v\ge0$. Hence its objective is at least $6c^2$, attained by the constant vector.

Write $s=2c$, let $\beta_j$ multiply $\Delta h_j\ge0$ with $\beta$ zero at both endpoints and outside, and let $\Lambda_j$ multiply $h_j\ge e_j$. Height stationarity is $\Lambda_j=s+2\beta_j-\beta_{j-1}-\beta_{j+1}$. Complementarity forces $\Lambda_j=0$ at the outer four bases since their obstacles are strictly slack. Stationarity at the extreme bases gives $\beta_{-1}=\beta_2=s$, and at the next pair gives $\beta_0=\beta_1=3s$. The middle equations give $\Lambda_0=\Lambda_1=3s$. All the multipliers are nonnegative. They are valid also for the original all-supporting-slopes system: use zero supporting slopes and equal outgoing edge multipliers $\beta_j$ to each immediate neighbor. Both edges are tight, the opposite increments cancel in slope stationarity, and the same height equations hold. This proves the exact nearest-neighbor realization and uniqueness of its multipliers. The positive component from $0$ contains $-1$, where $H_i$ strictly contains the entire fiber.

From base $j$ the original multiplier row continues to each immediate neighbor with probability $\beta_j/(s+2\beta_j)$ and stops with probability $s/(s+2\beta_j)$. Let $T_0$ denote the continuation matrix and $D_0$ the diagonal matrix of stopping probabilities. Every stopping probability is at least $1/7$, so the terminal transition matrix is $(I-T_0)^{-1}D_0$. For the row starting at $0$, let $W_j=((I-T_0)^{-1})_{0j}\beta_j/(s+2\beta_j)$ on the four transit nodes and zero elsewhere. Expanding $(I-T_0)^{-1}=I+(I-T_0)^{-1}T_0$ shows that these $W_j$ solve
$(2+s/\beta_j)W_j-W_{j-1}-W_{j+1}=\mathbf 1_{j=0}$ at each transit node. Its unique solution is $(2/9,2/3,1/3,1/9)$ in order $-1,0,1,2$, as is verified by substitution. At these nodes the terminal probabilities are $(s/\beta_j)W_j$. At the two stopping boundaries they are $W_{-1}$ and $W_2$, yielding the stated probability row with barycenter zero. Since $D_0+T_0-I$ acts on a vector $f$ by multiplying its second difference at $j$ by $\beta_j/(s+2\beta_j)$, the original signed row difference equals $\sum_jW_j\Delta f_j$.

The residual roots of any $H_i$ are exactly $(0,0,c,1,1,1)$ and the transit second differences are $(c,1-2c,c-1,0)$. The weighted sum is $(2/9)c+(2/3)(1-2c)+(1/3)(c-1)=1/3-7c/9<0$. The first term is the positive contribution at $-1$. The two negative terms from the middle bases compensate it using the original row with all boundary probabilities retained.
