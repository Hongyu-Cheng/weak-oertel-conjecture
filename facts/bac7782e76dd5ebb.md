---
fact_id: bac7782e76dd5ebb
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3ed-integer-box-central-slab-countertest
depends_on: []
verifier_run: 911d74ff694b4e2a
target_match: null
---

## Statement

Let \(n,k\ge1\), let \(j_i\) be nonnegative integers with at least one positive \(j_i\), let \(V_i\) be independent and uniform on \(\{-j_i,\ldots,j_i\}\), and let \(a_{ri}>0\) for \(1\le r\le k\), \(1\le i\le n\). Use the subgoal's normalization \(\sigma_r^2=\sum_i a_{ri}^2j_i(j_i+1)/3\), which is positive under these hypotheses. Fix an integer \(m\ge1\), a real number \(\beta\ge0\), and an integer \(L\ge2\). Suppose that for each row \(r\) there exists \(H_r\subseteq\{1,\ldots,n\}\), with \(|H_r|\le m\), such that \(\sum_{i\notin H_r}a_{ri}j_i\le\beta\sigma_r\). Then

\[
\Pr\left\{\left|\sum_i a_{ri}V_i\right|\le\left(\beta+\frac{\sqrt{3m}}{L}\right)\sigma_r\text{ for every }r\right\}
\ge(2L-1)^{-mk}
\ge(k+1)^{-C_{m,L}k},
\qquad C_{m,L}=\frac{m\log(2L-1)}{\log2}.
\]

In particular, assume that for each row its positive effective coefficients \(a_{ri}j_i\), put in nonincreasing order, form a sequence \(w_{r,1},\ldots,w_{r,N_r}\) satisfying \(w_{r,s+1}\le w_{r,s}/q\) for some fixed \(q\ge2\). The row orders and leading coordinates may differ. Then the absolute choices \(B=3\), \(C=2\) satisfy

\[
\Pr\left\{\left|\sum_i a_{ri}V_i\right|\le3\sigma_r\text{ for every }r\right\}
\ge3^{-k}\ge(k+1)^{-2k}.
\]

More basically, for arbitrary rows and ranges as above, every point of the integer box supported on at most one coordinate belongs to every slab of width \(B\sigma_r\) whenever \(B\ge\sqrt3\). Thus a literal origin-only construction is impossible at such widths, although this last observation alone gives no adequate probability bound when \(n\) grows.

## Proof

Put \(H=\bigcup_{r=1}^k H_r\), so \(|H|\le mk\), and consider the event \(E=\{|V_i|\le\lfloor j_i/L\rfloor\text{ for every }i\in H\}\). Coordinates outside \(H\) are unrestricted. On \(E\), the triangle inequality, the hypothesis on the row tail, and Cauchy--Schwarz give, for every \(r\),

\[
\begin{aligned}
\left|\sum_i a_{ri}V_i\right|
&\le\sum_{i\in H_r}a_{ri}\frac{j_i}{L}+\sum_{i\notin H_r}a_{ri}j_i\\
&\le\frac{\sqrt{|H_r|}}{L}\left(\sum_{i\in H_r}a_{ri}^2j_i^2\right)^{1/2}+\beta\sigma_r\\
&\le\left(\frac{\sqrt{3m}}{L}+\beta\right)\sigma_r.
\end{aligned}
\]

The last inequality uses \(j_i^2\le j_i(j_i+1)\). Hence \(E\) is contained in all the asserted slabs.

For every nonnegative integer \(j\), write \(j=Lt+s\), where \(t\ge0\) and \(0\le s\le L-1\). The exact central-interval probability obeys

\[
\frac{2\lfloor j/L\rfloor+1}{2j+1}
=\frac{2t+1}{2Lt+2s+1}
\ge\frac{2t+1}{2Lt+2L-1}
\ge\frac1{2L-1}.
\]

Indeed, the final inequality is equivalent to \((2L-2)t\ge0\). Independence therefore yields \(\Pr(E)\ge(2L-1)^{-|H|}\ge(2L-1)^{-mk}\). Since \(k+1\ge2\), the displayed definition of \(C_{m,L}\) implies \((k+1)^{C_{m,L}k}\ge(2L-1)^{mk}\), proving the first assertion. When every \(j_i=0\), omitted from the positive-variance statement, all \(V_i=0\) and the simultaneous event instead has probability one.

For the geometric specialization, take \(H_r\) to be the leading coordinate in row \(r\), and take \(m=1\), \(L=2\). Summing the geometric majorant gives \(\sum_{s=2}^{N_r}w_{r,s}\le w_{r,1}/(q-1)\). The variance formula gives \(\sigma_r\ge w_{r,1}/\sqrt3\). Thus the hypothesis holds with \(\beta=\sqrt3/(q-1)\le\sqrt3\). The first assertion supplies simultaneous slabs of width at most \(\bigl(\sqrt3+\sqrt3/2\bigr)\sigma_r=(3\sqrt3/2)\sigma_r<3\sigma_r\), with probability at least \(3^{-k}\). Finally \(k+1\ge2\) implies \((k+1)^2\ge4>3\), proving the stated \(C=2\) bound. No independence between the rows is needed; the only independent events concern the coordinates in \(H\).

For the axis assertion, a point supported on coordinate \(i\) satisfies \(|\sum_h a_{rh}V_h|\le a_{ri}j_i\) in row \(r\). If \(j_i>0\), then \(a_{ri}j_i\le\sqrt{3j_i/(j_i+1)}\,\sigma_r<\sqrt3\,\sigma_r\); if \(j_i=0\), the point is zero. This proves the final assertion exactly.

The first assertion also identifies a necessary escape from the tested mechanism. Any class with fixed \(m\) and a uniformly bounded quantity \(\max_r\min_{|H_r|\le m}\sigma_r^{-1}\sum_{i\notin H_r}a_{ri}j_i\) has fixed constants of the required form, independent of \(n,k\), all ranges, and all coefficient values. Consequently an all-fixed-constants counterfamily cannot stay in any such class. This is only a restriction on possible counterfamilies: no estimate is proved here when those trimmed support ratios are unbounded.

## External sources

None. All estimates are elementary and proved above.
