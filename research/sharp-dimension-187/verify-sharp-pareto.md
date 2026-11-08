# Independent verification of the sharp-bound dimension tradeoffs

Date: 2026-11-07. Reviewed [sharp-triangle-join.md](sharp-triangle-join.md), including Section 6, its main and Pareto exact checkers and saved certificates, and the separate [geometric audit](alternative-join-audit.md) and [audit checker](alternative-join-audit-check.py).

Verdict: the same geometric proof legitimately covers all three pairs $(132,82)$, $(153,34)$, and $(129,104)$. Their strict sharp-bound counterexamples pass this independent mathematical and exact-arithmetic review. These particular examples provably do **not** refute the $1/(e2^n)$ bound; a proof appears below. This is an LLM review with exact arithmetic, not formal verification or an accepted graph entry.

## Parameter substitutions and proof coverage

The Section 6 parameters agree exactly with the checker. In particular, the $(132,82)$ value $791357067/20000000000$ equals the program's $39567853350/10^{12}$. Every row uses $a=159/250>1/2$ and $\epsilon=10^{-13}$, with $D=d+1$, $N=n/3$, and its own cutoff. They are respectively:

| $(n,d)$ | $N$ | Cutoff |
| --- | --- | --- |
| $(132,82)$ | 44 | 25 |
| $(153,34)$ | 51 | 10 |
| $(129,104)$ | 43 | 32 |

The construction's source vertices, volume ratios, and center identities are formulas in $a,D$, rather than special identities at $d=99$ or $a=63/100$. The triangular determinant formulas remain valid under all three substitutions. There are exactly $D=d+1$ vertices in each positive joined simplex, and their determinant is nonzero. The weights expressing the shifted center are strictly positive, sum to one, and reconstruct the stated barycentric center exactly.

The source polygons are determined by the same five planar boundary lines. Joining with the free face introduces no new inequality or volume factor: the remaining vertex columns form an identity block, including for the cap determinant. The normalization by the sum of the first three barycentric coordinates handles the positive-sum portion, and the zero-sum case is exactly the free face.

The truncated negative-subset census does not depend on the numerical cutoff. An integer convex combination of negative Boolean generators from one block must use identical generators at every coordinate. Therefore it cannot introduce an unlisted larger subset. The exposing functionals work for every cutoff at most $N$.

The positive-fiber affine-facet residual is identically $(k-1)\delta(1/D-a\epsilon/Q)$, and this is nonnegative for every $k=1,\ldots,n$. The negative scaling $1-rDv$ is positive up to the chosen cutoff, giving the exact origin-fiber envelope in every case. The paid and unpaid cut inequalities remain strict. All nonzero actual fibers are exposed, all positive fibers are full-dimensional simplices, and the negative masses decrease with their subset cardinality.

The same every-point argument therefore applies: cover the origin fiber by the three prescribed cuts, isolate a simplex cap on each positive fiber, and isolate an entire negative fiber by an integer-only closed halfspace. The last kind of halfspace can contain the whole fiber on its boundary; its positive mass is correctly included. The proof does not assume that every ambient halfspace boundary has zero mixed-integer volume.

## Exact checks performed

Both certificate producers passed and reproduced their saved JSON byte for byte. To avoid rewriting repository certificates, I executed their source with `__file__` directed into disposable temporary directories and compared the resulting files with the saved versions.

I also ran the separate geometric audit checker three times with only its initial parameter assignments replaced by the three rows above. For each row it independently checked:

* all vertices of the planar source by intersecting pairs of boundary lines;
* the positive-source, negative-source, and cap determinants;
* the center weights, reconstruction, and three continuous row scores;
* the affine facet identity and strict positive-fiber cut gaps for every $k=1,\ldots,n$;
* positive negative-fiber scales, monotonicity of negative volumes, and all three exact mass margins.

All checks passed using rational arithmetic. The following decimals are only orientation; the signs were established exactly.

| $(n,d)$ | $1+E-m$ | $\Gamma_dm-\beta-E/3$ | $\Gamma_dm-\alpha_1$ |
| --- | --- | --- | --- |
| $(132,82)$ | $5.8230046671\cdot10^{-5}$ | $2.0333537060\cdot10^{-5}$ | $1.1476513014$ |
| $(153,34)$ | $3.9409933944\cdot10^{-5}$ | $1.3818118480\cdot10^{-5}$ | $1.0670853063$ |
| $(129,104)$ | $4.2567937992\cdot10^{-7}$ | $1.5101148175\cdot10^{-7}$ | $1.1606112700$ |

No parameterization error or mathematical gap was found.

## Exact depth and why these examples satisfy the weaker bound

Write $W$ for total mixed-integer volume and $M=mb$ for a positive fiber's volume. The proved every-point estimate is $\operatorname{depth}_S(y)\le\Gamma_dM/W$ for all $y\in S$. At the centroid of a positive simplex fiber, every containing ambient halfspace retains at least $\Gamma_dM$ from that fiber by the ordinary centroid Grünbaum inequality. A zero continuous normal retains the entire fiber. An isolated simplex vertex cap realizes the matching upper bound. Therefore the maximum depth is exactly

$$
\max_{y\in S}\operatorname{depth}_S(y)=\frac{\Gamma_dM}{W},
$$

and it is attained at every positive-fiber centroid. The ordinary centroid statement used here is proved in Section 3 of [Grünbaum's original paper](https://msp.org/pjm/1960/10-4/pjm-v10-n4-p18-p.pdf), pp. 1259–1260.

There is an especially simple proof that this maximum is strictly greater than $1/(e2^n)$, using only the support count. If $L$ is the number of nonempty fibers, a largest fiber has volume at least $W/L$, so its centroid has normalized ambient depth at least $\Gamma_d/L$.

Here $n=3N$, $N\ge43$, $d\le104$, and

$$
\begin{aligned}
L&=2^{3N}+3\sum_{r=1}^{\mathrm{cutoff}}\binom Nr
<2^{3N}\left(1+\frac{3}{2^{2N}}\right)
\le2^n\left(1+\frac{3}{2^{86}}\right),\\
e\Gamma_d-1
&>\log(e\Gamma_d)
=\int_0^1\frac{t}{d+t}\,dt
>\frac1{2(d+1)}\ge\frac1{210}
>\frac3{2^{86}}.
\end{aligned}
$$

Thus $L<e\Gamma_d2^n$, and the largest-fiber centroid has depth strictly greater than $1/(e2^n)$. Together with the exact maximum above and the sharp counterexample proof, this yields

$$
\frac1{e2^n}
<\max_{y\in S}\operatorname{depth}_S(y)
=\frac{\Gamma_dM}{W}
<\frac{\Gamma_d}{2^n}.
$$

The same argument also covers the main worked pair $(132,99)$. The distinction is therefore established mathematically: these are sharp-bound counterexamples that satisfy the weaker $1/e$ bound, rather than examples for which the weaker comparison is merely unknown.

Only this review file was created. No construction, certificate, accepted fact, or graph record was changed.
