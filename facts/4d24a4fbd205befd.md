---
fact_id: 4d24a4fbd205befd
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-integer-mean-closed-tail
depends_on: ["108bf10461a9c6ff"]
verifier_run: 743e3c9f45064c3e
target_match: null
---

## Source

- [821242aee5d2f3e1](../candidates/821242aee5d2f3e1.json), §§7–8.
- [b1b0de9a36eb803f](../candidates/b1b0de9a36eb803f.json), Closed tails at an integer mean, exact d=1 example.

## Statement

Let $d\ge1$ be real and let $(a_i)_{i=\ell}^r$ be positive probability masses on consecutive integers with concave $d$th roots. Suppose $\mu=\sum_{i=\ell}^r i a_i$ is an integer. Both closed tails satisfy
$$
\sum_{i\ge\mu}a_i>\left(\frac{d+1}{d+2}\right)^{d+1},
\qquad
\sum_{i\le\mu}a_i>\left(\frac{d+1}{d+2}\right)^{d+1}.
$$
At every fixed $d$ this constant is the infimum of either tail among profiles with exactly integer mean.

For the geometric consequence, let $d$ be a positive integer and $C\subseteq\mathbb R\times\mathbb R^d$ a convex body with positive mixed $d$-volume $W$. If the base coordinate of its mixed-volume centroid is an integer, every closed vertical halfspace containing the centroid has mixed $d$-volume strictly greater than $W((d+1)/(d+2))^{d+1}$. This normalized bound is also sharp as an infimum.

## Proof

Put $p=1/(d+1)$ and $F_i=\sum_{j=i}^r a_j$. For a singleton both tails are one. Otherwise $\ell<\mu<r$ because all masses are positive. The piecewise linear interpolation of $(F_i^p)_{\ell\le i\le r}$ is concave by concave-root-tail-concavity with the given $d$ and masses. Jensen's inequality on $[\ell,r]$ gives
$$
F_\mu^p\ge\sum_{i=\ell}^r a_i F_i^p
=\sum_{i=\ell}^r(F_i-F_{i+1})F_i^p
>\int_0^1 t^p\,dt
=\frac{1}{p+1}.
$$
The strict inequality is the upper-endpoint sum for a strictly increasing function on the partition $1=F_\ell>\cdots>F_r>F_{r+1}=0$. The terminal zero is used only in this partition. Raising to $1/p$ gives the upper-tail bound. The probability law with masses $a_{-i}$ on $[-r,-\ell]\cap\mathbb Z$ has the same root concavity and mean $-\mu$, so its upper tail gives the lower-tail bound for the original law.

For exact integer centering in the limiting example, use weights $w_j(L)=(L-j)_+^d$ for integers $j\ge0$ and real $L>1$. Their roots are affine on the positive support $0\le j<L$. Write $\mu(L)=\sum_j j w_j(L)/\sum_j w_j(L)$. This is continuous because the sums are locally finite with continuous summands and $w_0(L)>0$. On each interval between consecutive integers let $P_j=w_j(L)/\sum_i w_i(L)$ for the positive terms. Differentiation on that interval gives
$$
\mu'(L)=d\sum_{i<j<L}P_iP_j(j-i)\left(\frac1{L-j}-\frac1{L-i}\right)>0,
$$
where $0\le i<j$ are integers. The formula follows by differentiating the quotient and pairing the two terms for each pair of indices. Strictness follows from the positive terms at $0,1$. Continuity then gives strict increase on all of $(1,\infty)$, and $\mu(L)\to0$ as $L\downarrow1$. The Riemann sums with mesh $1/L$ give
$$
\frac{\mu(L)}{L}
=\frac{L^{-1}\sum_{0\le j<L}(j/L)(1-j/L)^d}
       {L^{-1}\sum_{0\le j<L}(1-j/L)^d}
\longrightarrow\frac{\int_0^1 t(1-t)^d\,dt}{\int_0^1(1-t)^d\,dt}
=\frac1{d+2}.
$$
In particular $\mu(L)\to\infty$, so for every integer $k\ge1$ there is a unique $L_k>1$ with $\mu(L_k)=k$. The support gives $L_k>k$, hence $L_k\to\infty$ and $k/L_k\to1/(d+2)$. In the following tail Riemann sum the moving lower cutoff can be replaced by the limiting cutoff $1/(d+2)$ with error at most $|k/L_k-1/(d+2)|+2/L_k$ after multiplication by the mesh, since the summands $(1-j/L_k)^d$ are in $[0,1]$. Therefore
$$
\frac{\sum_{j\ge k}w_j(L_k)}{\sum_{j\ge0}w_j(L_k)}
\longrightarrow
\frac{\int_{1/(d+2)}^1(1-t)^d\,dt}{\int_0^1(1-t)^d\,dt}
=\left(\frac{d+1}{d+2}\right)^{d+1}.
$$
Reflection gives the corresponding infimum for the lower tail. At $d=1$ the exact choice $L_k=3k+1$ follows from $\sum_{j=0}^{L-1}j(L-j)/\sum_{j=0}^{L-1}(L-j)=(L-1)/3$ for integral $L$. The upper-tail fraction is then $(2k+1)(2k+2)/((3k+1)(3k+2))$, as in the separate square-root note.

For the geometric statement write $C_x=\{y:(x,y)\in C\}$ for real $x$ and put $v_i=\operatorname{vol}_d(C_i)$ at integer $i$. If two real fibers have positive volume, their Minkowski convex combination is contained in the fiber at the interpolated base. The Brunn–Minkowski inequality gives positivity there and concavity of the $d$th root of the fiber volume between the two bases. Thus the positive integer fibers have finite consecutive support and their normalized volumes $a_i=v_i/W$ satisfy the scalar hypotheses. Their mean is the base coordinate of the mixed centroid. A closed vertical halfspace containing that centroid contains either all fibers with $i\ge\mu$ or all fibers with $i\le\mu$, including the entire fiber at $\mu$. Zero-volume fibers contribute zero. This proves the bound, which exceeds $W/e$ since $\log(1+1/(d+1))<1/(d+1)$. For each $L=L_k$, the convex body given by $0\le x\le L$ and $\lVert y\rVert_2\le L-x$ has fiber volumes $\operatorname{vol}_d(B_2^d) w_j(L)$ exactly on its positive integer support $0\le j<L$. Its base mean is exactly $k$, so the same limiting example gives sharpness for the closed vertical caps.
