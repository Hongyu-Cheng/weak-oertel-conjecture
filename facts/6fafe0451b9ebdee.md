---
fact_id: 6fafe0451b9ebdee
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w34-simplex-integrated-endpoint-credit
depends_on: ["724e9b2e1a3ec0bf", "67ecf7db6692fe65"]
verifier_run: 72c25ec3c3174119
target_match: null
---

## Source

- [986ab1688d049a3b](../candidates/986ab1688d049a3b.json), 986ab1688d049a3b:07 §4, (9)–(10), including stronger (3a) option.

## Statement

Let $B,C\subset\mathbb R^d$, $d\ge1$, be simplices of equal volume $V>0$. Let $A$ be a convex body of volume $a>0$ with $(A+C)/2\subset B$. Put $N=d+1$, $J=\lceil N/2\rceil$, $b=1/N$ and $R=\lfloor N/2\rfloor+1$. For $N=2$ use $\delta=\tfrac14$; for $N\ge3$ take either
$$
 \delta=N^{-N/(2R)}-b
 \qquad\text{or}\qquad
 \delta=\max\{N^{-N/(2R)},4^{-(N-1)/R}\}-b .
$$
Let $\lambda_i$ be the barycentric coordinates of $B$. For arbitrary real $b_i$, define the actual endpoint costs
$$
 e_i=\min_{\beta\in\mathbb R}\bigl(|A\cap\{\lambda_i\ge b_i+\beta\}|+|C\cap\{\lambda_i\ge b_i-\beta\}|\bigr).
$$
If $(a/V)^{1/d}+\max_i(b_i-b)_+<\delta$, then $\sum_i e_i\ge Ja$. In particular, at $b_i=b$ it suffices that $a/V<\delta^d$. For $d\ge2$ this lower bound is strictly greater than $N(d/(d+1))^d a$.

## Proof

Set $r=(a/V)^{1/d}$; Brunn–Minkowski and the midpoint inclusion give $r\le1$. For any $p\in A$, the simplex $(p+C)/2$ lies in $B$ and has volume $2^{-d}V$. Its barycentric vertex matrix has nonnegative entries and unit column sums. For $N\ge3$, 724e9b2e1a3ec0bf gives absolute determinant $2^{-d}$ from this volume ratio. Write $h_i=\max_C\lambda_i$, and let $W_i$ be the width of $\lambda_i$ on $C$. The matrix row maximum is $(\lambda_i(p)+h_i)/2$, and $W_i\le2$ since the width on $(p+C)/2$ is $W_i/2\le1$.

The centered row bound of 724e9b2e1a3ec0bf applied with determinant parameter one gives at least $J$ row maxima at least $N^{-N/(2R)}$ when $N\ge3$. For the other bound, if row maxima are $m_i$ and row sums $s_i$, Hadamard gives $|\det|^2\le\prod_i(m_i s_i)\le\prod_i m_i$, since $\sum_i s_i=N$. All maxima are at most one, so the product is at most the $R$th power of the $J$th largest maximum. This gives the second threshold $4^{-(N-1)/R}$ for the same row order statistic. When $N=2$, write the two columns as $(x,1-x)$ and $(y,1-y)$; one barycentric coordinate is an affine interval coordinate on $B$, so $|x-y|=|(p+C)/2|/|B|=1/2$. Hence the row maxima sum to $1+|x-y|=3/2$. Thus in every case, at least $J$ indices at each $p$ satisfy $\lambda_i(p)+h_i\ge2(b+\delta)$.

Apply 67ecf7db6692fe65 with $f=\lambda_i$ and $s=b_i$. Its hypotheses hold since the coordinate is nonconstant and $a\le V=|C|$. The lemma bounds $e_i$ below by the volume of $\{p\in A:\lambda_i(p)\ge2b_i-h_i+W_i r\}$. Each of the $J$ indices just obtained belongs to this comparison at $p$, since
$$
 \lambda_i(p)+h_i\ge2(b+\delta)>2b_i+2r\ge2b_i+W_i r.
$$
Summing the indicators and integrating over $A$ gives the bound even though the indices may vary with $p$. A minimum exists since the cap volumes are continuous in $\beta$ by null affine boundaries, and outside some finite interval the endpoint costs are constant at $a$ or $V$. They are actual closed cap volumes on bases $-1,1$ for the halfspace $\lambda_i(x)+\beta z\ge b_i$; the convex hull with the middle fiber $B$ has exactly the displayed fibers by the midpoint inclusion. Finally $(1+1/d)^d>2$ for $d\ge2$ by the binomial theorem, so $J/N\ge1/2>(d/(d+1))^d$.
