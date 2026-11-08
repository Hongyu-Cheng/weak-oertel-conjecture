---
fact_id: 7de71b378ac4bfad
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w35-centers-ambient-mixed-sharpness
depends_on: []
verifier_run: 0ef3e706ad512264
target_match: null
---

## Source

- [c5c3a8a6a4fe43cd](../candidates/c5c3a8a6a4fe43cd.json), c5c3a8a6a4fe43cd:01 §§1–2, (1)–(2) and exact counterexample.

## Statement

Let $n,d\ge1$ with $N=n+d+1\le2^n$. Choose $N$ distinct binary bases $0,e_1,\ldots,e_n,v_1,\ldots,v_d$ in $\mathbb R^n$. Let $q_0=(0,0)$, $q_i=(e_i,0)$ for $1\le i\le n$, $q_{n+j}=(v_j,e_j)$ for $1\le j\le d$, and $C=\operatorname{conv}\{q_0,\ldots,q_{N-1}\}+(\{0\}^n\times[-\varepsilon,\varepsilon]^d)$, where
$$
0<\varepsilon<\min\{1/[Nd(n-1)],1/[2nd(N-1)]\}.
$$
The mixed $d$-volume measure has exactly $N$ equal positive cube fibers. Its maximal normalized depth over all ambient points is exactly $1/N$, attained at the mean of the $q_i$. For $n=4,d=8,\varepsilon=1/1000$ and additional bases the six weight-two binary vectors and $(1,1,1,0),(1,1,0,1)$, this maximal depth is $1/13$, below $\Gamma_8/5$ by exactly $2870203/2798036865$.

## Proof

Here $n\ge2$, and every extra binary vector $v_j$ has at least two ones. The edge matrix of $T=\operatorname{conv}\{q_0,\ldots,q_{N-1}\}$ from $q_0$ is block triangular with identity diagonal blocks, so $T$ is full dimensional. Its base projection lies in $[0,1]^n$. An integer base there is binary and a binary point can be a convex combination of binary vectors only if every positive-weight vector equals it, by checking each coordinate. Thus the integer fibers of $T$ are exactly the lifted vertices and the integer fibers of $C$ are exactly their translates by the common continuous cube. Each has volume $a=(2\varepsilon)^d$, their total mixed mass is $Na$, and their lifted convex hull equals $C$ by convexity of the common cube.

The affine barycentric functions on $T$ are
$$
\lambda_{n+j}(z,x)=x_j,\qquad
\lambda_i(z,x)=z_i-\sum_j(v_j)_i x_j,\qquad
\lambda_0(z,x)=1-\sum_i z_i+\sum_j(\|v_j\|_1-1)x_j.
$$
Adding a continuous cube displacement to any $q_\ell$ changes each coordinate by at most $d(n-1)\varepsilon<1/N$. In fact the three bounds are respectively $\varepsilon$, $d\varepsilon$, and $d(n-1)\varepsilon$. Hence the closed halfspace $\{\lambda_i\ge1/N\}$ contains its own whole cube and misses every other cube. These halfspaces cover the entire ambient space because the $\lambda_i$ sum to one. Every ambient mark therefore has normalized depth at most $1/N$.

Let $g=\sum_i q_i/N$. Translate the boundary of any halfspace containing $g$ until it passes through $g$, yielding a smaller cap defined by $L(z,x)=\alpha\cdot z+\beta\cdot x+b\ge0$ with nonzero normal and $L(g)=0$. Set $r_i=L(q_i)$ and $R=\max_i r_i$. The $r_i$ sum to zero and do not all vanish since the vertices affinely span, so $R>0$ and $|r_i|\le(N-1)R$. Evaluating at the vertices gives
$$
\beta_j=r_{n+j}-\sum_i(v_j)_i r_i+(\|v_j\|_1-1)r_0.
$$
The sum of the absolute coefficients here is $2\|v_j\|_1\le2n$, whence $\sum_j|\beta_j|\le2nd(N-1)R$. The entire cube at a vertex attaining $R$ therefore has $L\ge R-\varepsilon\sum_j|\beta_j|>0$. Every cap at $g$ contains at least this cube, proving exact depth $1/N$.

For the specified bases in dimension $(4,8)$ the two denominators in the constraint on $\varepsilon$ are $312$ and $768$. The construction applies and $\Gamma_8/5-1/13=(8/9)^8/5-1/13=2870203/2798036865$.
