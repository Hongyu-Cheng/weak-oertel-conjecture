# A smaller continuous dimension for the existing 1/e counterexample

The construction in accepted fact `df488edae05a1702` also works with

\[
 n=52,\qquad d=1\,350\,000\,000\,002\,747\,789.
\]

This reduces its continuous dimension by approximately 41.45%. It is a
parameter improvement within the same geometric family, and remains far
above the goal d<100. The conclusion is still the strict bound
\(\sup_{\mathbf y}\operatorname{depth}(\mathbf y)<1/(e2^{52})\).

## Parameters and geometric validity

Use the complete generalized geometric lemma in
[`facts/df488edae05a1702.md`](../../facts/df488edae05a1702.md), with

| Parameter | Exact value |
|---|---|
| N, n | 13, 52 |
| h | 2,747,786 |
| simplex padding dimension ell | 1,350,000,000,000,000,000 |
| s | 500000001/1000000000 |
| t | 999999997/1000000000 |
| eta | 399999999/400000000 |
| epsilon | 1/1000000000000 |
| q | 1000001/2000000 |

The total continuous dimension is 3+h+ell. The middle tetrahedron, its four
source boxes, the four blocks of 13 integer coordinates, the positive
Boolean fibers and all nonempty negative Boolean subsets in a single
block are unchanged in form. Here delta_q=2q-1=1/1000000, so
1-13 delta_q=999987/1000000>0. The other geometric parameters are those
of the accepted witness. All hypotheses of the generalized lemma are
checked exactly by `check_improved_n52.py`.

In particular the affine-facet origin argument still gives exactly the
prescribed middle fiber, every nonzero base is exposed, there are no
unlisted integer fibers, and all fibers are full-dimensional. The four
middle cuts still cover the middle fiber and each pays exactly one block
of negative fibers. No new geometric assertion is assumed from numerical
optimization.

## Exact scalar certificate

Let theta=3/32, beta=27/64, delta_t=1-t, and delta_q=2q-1. Put

\[
 m=\theta(2s)^3(2q)^h,\qquad
 E=4\theta\sum_{r=1}^{13}\binom{13}{r}(1-r\delta_t)^3(1-r\delta_q)^h.
\]

Integer outward-rounded binary exponentiation gives

\[
 \frac{1463251505373}{10^{12}}<m<\frac{1463251505374}{10^{12}},\qquad
 \frac{465699293757}{10^{12}}<E<\frac{465699293758}{10^{12}}.
\]

Write these bounds as mlo,mhi,Elo,Ehi. The same series bound as in the
accepted proof gives \(e<e_+=1359141/500000\). Exact fraction comparisons
then yield

\[
\begin{aligned}
 m_{\rm lo}/e_+-\beta-E_{\rm hi}/4
 &=\frac{37367344241}{129442000000000000}>0,\\
 1+E_{\rm lo}-m_{\rm hi}
 &=\frac{2447788383}{10^{12}}>0,\\
 1+E_{\rm lo}-m_{\rm hi}-\frac{2^{52}m_{\rm hi}}{2\ell-1}
 &=\frac{19129699748336272319166113}{2699999999999999999000000000000}>0.
\end{aligned}
\]

The last margin is approximately 7.0851e-6 and the middle-cut margin is
approximately 2.8868e-7; only the displayed exact inequalities are used.

## Uniform every-point conclusion

Before padding, let b be the middle-fiber volume. The total mass is
\(W=b[(2^{52}-1)m+1+E]\), and each middle cut has mass
\(b(\beta+E/4)<bm/e\). Since W>2^52 bm, these cuts are uniformly below
the desired normalized threshold.

For \(\Gamma_\ell=(\ell/(\ell+1))^\ell\), the elementary estimate
\(e\Gamma_\ell<1+1/(2\ell-1)\), proved in the accepted note, and the
last exact margin give
\(e\Gamma_\ell 2^{52}m<(2^{52}-1)m+1+E\). At every noncentral base,
isolate a containing simplex cap in the padding factor using the finite
exposing tilt. The normalized cap mass is at most \(\Gamma_\ell bm/W\),
also strictly below 1/(e2^52). The maximum of the two uniform bounds
therefore proves the strict supremum inequality for every actual point.

This retains the rational-polytope, full-dimensionality and
Hausdorff/fiber-measure conclusions of the original argument. It does not
refute the weaker conjecture for some smaller positive absolute constant.
It is an exact analytic and arithmetic result, not a Lean formalization.
