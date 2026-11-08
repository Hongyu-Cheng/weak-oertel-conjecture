---
fact_id: d835962fccfaca7e
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-fixed-uniform-near-facet-endpoint-credits
depends_on: ["67ecf7db6692fe65", "724e9b2e1a3ec0bf"]
verifier_run: f812ce3356caf999
target_match: null
---

## Source

- [6b774d09877ca348](../candidates/6b774d09877ca348.json), 6b774d09877ca348:03 §3 (6)–(7), (9)–(11); §4 (12)–(13).
- [6b774d09877ca348](../candidates/6b774d09877ca348.json), 6b774d09877ca348:01 Opening (1)–(2), §§1–2, (3)–(5).
- [986ab1688d049a3b](../candidates/986ab1688d049a3b.json), 986ab1688d049a3b:02 §1, two-row stochastic calculation.
- [986ab1688d049a3b](../candidates/986ab1688d049a3b.json), 986ab1688d049a3b:03 §1, (3)–(3a), optional larger margin.

## Statement

Let $d\ge1$, $N=d+1$, $J=\lceil N/2\rceil$, $b=1/N$, $q=N-J+1$, and let $B,C$ be $d$-simplices of equal volume $V>0$. Let $A$ be a convex body of volume $a>0$ with $(A+C)/2\subset B$. Affinely normalize $B$ to the standard simplex and shear $(z,x)\mapsto(z,x+zp_0)$ on the three bases $-1,0,1$, where $p_0$ is any point of the normalized $A$. Use $A,B,C,a,V$ for the resulting data, write $\lambda_i$ for the barycentric functions of $B$, and put $R=2\sqrt d$ and $r=(a/V)^{1/d}$. Then $0\in A$, $C\subset2B$, $A\subset2(B-B)$ and $r\le1$.

For $N=2$ choose $\delta=1/4$. For $N\ge3$ one may use either $\delta=N^{-N/(2q)}-b$ or $\delta=\max\{N^{-N/(2q)},4^{-(N-1)/q}\}-b$. For each $p\in A$, at least $J$ indices satisfy $\lambda_i(p)+\max_C\lambda_i\ge2b+2\delta$. Define the fixed sets and credits
$$A_i=\{p\in A:\lambda_i(p)+\max_C\lambda_i\ge2b+\delta\},\qquad c_i=|A_i|.$$
Then $0\le c_i\le a$ and $\sum_i c_i\ge Ja$.

If $y\in B$ satisfies $\max_i(\lambda_i(y)-b)_+\le\sigma$, and $f_i(x)=\lambda_i(x)+v\cdot x$ is nonconstant with $\lVert v\rVert\le\varepsilon$, then the condition $2\sigma+2r+6R\varepsilon<\delta$ ensures, for every real $\beta$,
$$|A\cap\{f_i\ge f_i(y)+\beta\}|+|C\cap\{f_i\ge f_i(y)-\beta\}|\ge c_i.$$
In particular $r,\sigma\le\delta/8$ and $\varepsilon\le\delta/(24R)$ suffice. For unit normals this includes the oriented neighborhoods $\lVert u-u_i\rVert\le\delta/(24R\sqrt d)$ of $u_i=\nabla\lambda_i/\lVert\nabla\lambda_i\rVert$.

For $\Gamma=(d/(d+1))^d$ and $\bar c=N^{-1}\sum_i c_i$, the point with $\lambda_i(y)=b+(c_i-\bar c)/(N\Gamma V)$ satisfies these center conditions whenever
$$a/V\le(\delta/8)^d,\qquad a/V\le N\Gamma\delta/8,\qquad a/V<\Gamma.$$

## Proof

Affine normalization changes all masses by the same Jacobian. The shear translates $A,C$ oppositely, preserving their average and shifting the tilt by a fixed number for each continuous normal. It gives $0\in A$, so $C\subset2B$. Fixing $p\in C$ then gives $A+p\subset2B$ and $p\in2B$, hence $A\subset2(B-B)$. All three bodies lie in the radius-$R$ ball since $B\subset[0,1]^d$. Brunn–Minkowski and the midpoint inclusion imply $a\le V$.

For each $p\in A$, the simplex $(p+C)/2$ lies in $B$, with barycentric vertex matrix nonnegative column-stochastic and of absolute determinant $2^{-d}$. Each row maximum is $(\lambda_i(p)+\max_C\lambda_i)/2$. For $N\ge3$ apply accepted 724e9b2e1a3ec0bf at its volume parameter one. For the larger optional margin, if row maxima are $m_i$ and row sums are $s_i$, then Hadamard gives $|\det|^2\le\prod_i m_i s_i\le\prod_i m_i$, using $\sum_i s_i=N$. Since all $m_i\le1$, this product is bounded above by the $q$-th power of the $J$-th largest maximum. For $N=2$, a stochastic two-column matrix with first entries $x_1,x_2$ has row maxima summing to $1+|x_1-x_2|=3/2$, so one is at least $3/4$. This proves the pointwise count for the chosen margins. Integrating the count for the larger sets $A_i$ proves $\sum_i c_i\ge Ja$.

For any $p\in A_i$, write $h=\max_C f_i$, $w=\max_C f_i-\min_C f_i$, and $\rho=R\varepsilon$. The support bounds give $f_i(p)+h\ge2b+\delta-2\rho$ and $f_i(y)\le b+\sigma+\rho$. Since $C\subset2B$, its width for each affine $\lambda_i$ is at most two, including the coordinate $1-\sum_jx_j$. Thus $w\le2+2\rho$ and
$$f_i(p)+h-2f_i(y)-wr\ge\delta-2\sigma-2r-4\rho-2\rho r\ge\delta-2\sigma-2r-6\rho>0.$$
Apply accepted 67ecf7db6692fe65 with $s=f_i(y)$ and $|C|=V$. Its comparison cap contains $A_i$, proving the bound for each real tilt and each allowed center and direction simultaneously. Any closed containing cap contains its parallel through-point cap. The stated closed parameter bounds give a slack of at least $\delta/4$. They make $f_i$ nonconstant because $\lVert\nabla\lambda_i\rVert\ge1$ and $\varepsilon<1$. For the unit normal claim, multiply $u$ by $\lVert\nabla\lambda_i\rVert\le\sqrt d$, yielding a perturbation of norm at most $\varepsilon$ with unrestricted rescaled tilt.

The proposed mark has coordinates summing to one and absolute deviations from $b$ at most $a/(N\Gamma V)$. Thus the strict bound $a/V<\Gamma$ places it in the interior. The other two inequalities ensure $r,\sigma\le\delta/8$, as claimed.
