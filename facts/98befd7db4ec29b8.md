---
fact_id: 98befd7db4ec29b8
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: bulk-occurrence-common-chart-extraction
depends_on: []
verifier_run: c151ab44852a42fd
target_match: null
---

## Statement

Let \(H\) be a real Hilbert space, let \(N\geq2\), and let \(u_1,\ldots,u_N\in H\). Put
\[
 \bar u:=\frac1N\sum_{i=1}^N u_i,
 \qquad
 V:=\sum_{i=1}^N\|u_i-\bar u\|^2.
\tag{1}
\]
If \(N\) is even, let \(M\) be a uniformly random perfect matching of \(\{1,\ldots,N\}\). If \(N\) is odd, let \(M\) be a uniformly random near-perfect matching, meaning a matching of size \((N-1)/2\). Define
\[
 p_N:=
 \begin{cases}
  1/(N-1),&N\text{ even},\\
  1/N,&N\text{ odd}.
 \end{cases}
\tag{2}
\]
Then
\[
 \boxed{
 \mathbb E\sum_{\{i,j\}\in M}\|u_i-u_j\|^2
 =p_NN V
 =
 \begin{cases}
  \dfrac{N}{N-1}V,&N\text{ even},\\[4pt]
  V,&N\text{ odd}.
 \end{cases}}
\tag{3}
\]

Now give the items arbitrary weights \(\eta_1,\ldots,\eta_N>0\), and put
\[
 W:=\sum_{i=1}^N\eta_i,
 \qquad
 \eta_{\max}:=\max_i\eta_i,
 \qquad
 \bar u_\eta:=\frac1W\sum_{i=1}^N\eta_i u_i,
\tag{4}
\]
\[
 V_\eta:=\sum_{i=1}^N
 \eta_i\|u_i-\bar u_\eta\|^2,
 \qquad
 \mathcal E_\eta(M):=
 \sum_{\{i,j\}\in M}
 \min\{\eta_i,\eta_j\}\|u_i-u_j\|^2.
\tag{5}
\]
Then the exact expectation and its weighted-variance lower bound are
\[
 \boxed{
 \mathbb E\mathcal E_\eta(M)
 =p_N\sum_{1\leq i<j\leq N}
 \min\{\eta_i,\eta_j\}\|u_i-u_j\|^2
 \geq p_N\frac{W}{\eta_{\max}}V_\eta.}
\tag{6}
\]
In particular, at least one perfect or near-perfect matching satisfies the rightmost lower bound in (6).

If, moreover, the weights lie in one factor-\(K\) range,
\[
 0<\eta_{\min}:=\min_i\eta_i,
 \qquad
 \frac{\eta_{\max}}{\eta_{\min}}\leq K,
\tag{7}
\]
then there is such a matching with
\[
 \boxed{
 \mathcal E_\eta(M)
 \geq
 \begin{cases}
  \dfrac{N}{K(N-1)}V_\eta,&N\text{ even},\\[6pt]
  \dfrac1K V_\eta,&N\text{ odd}.
 \end{cases}}
\tag{8}
\]
For equal weights, the inequality in (6) is an equality. If, in addition, all pairwise distances \(\|u_i-u_j\|\) are equal, then every perfect or near-perfect matching has the same energy, and the corresponding existence bound in (8) with \(K=1\) is attained.

For the edgewise quotient form, let \(E\) be a fixed edge, let \(I_E\) be a finite set of at least two distinct whole labels assigned to \(E\), and let each \(\sigma\in I_E\) have weight \(\eta_\sigma>0\) and occurrence lift \(U_{\sigma,E}\in\mathbb R^d\). For any linear subspace \(L\subseteq\mathbb R^d\), apply (1)-(8) in the Hilbert quotient \(H:=\mathbb R^d/L\) to
\[
 u_\sigma:=[U_{\sigma,E}]\in H,
 \qquad
 \|[x]\|:=\operatorname{dist}(x,L).
\tag{9}
\]
The resulting matching pairs each assigned occurrence at most once and pairs each label at most once. If the assigned label sets \(I_E\) are disjoint for different edges, choosing one matching for each edge gives a globally whole-label-disjoint and occurrence-disjoint family, and the lower bounds (6) or (8) add over the edges.

## Proof

We first establish the pairwise variance identity. Expanding the squared distances gives
\[
 \begin{aligned}
 \sum_{i<j}\|u_i-u_j\|^2
 &=(N-1)\sum_i\|u_i\|^2
   -2\sum_{i<j}\langle u_i,u_j\rangle\\
 &=N\sum_i\|u_i\|^2
   -\left\|\sum_i u_i\right\|^2\\
 &=N\sum_i\|u_i-\bar u\|^2
 =NV.
 \end{aligned}
\tag{10}
\]

When \(N\) is even, a fixed unordered pair \(\{i,j\}\) belongs to a uniformly random perfect matching with probability \(1/(N-1)\): the partner of \(i\) is uniform among the other \(N-1\) indices. When \(N\) is odd, symmetry makes the unmatched index uniform. Conditional on \(i\) being matched, its partner is uniform among the other \(N-1\) indices, so
\[
 \mathbb P(\{i,j\}\in M)
 =\frac{N-1}{N}\frac1{N-1}
 =\frac1N.
\tag{11}
\]
Thus in both cases every fixed pair belongs to \(M\) with probability \(p_N\). Linearity of expectation and (10) prove (3). The same pair-probability calculation, now retaining the deterministic coefficient \(\min\{\eta_i,\eta_j\}\), proves the equality in (6).

The weighted pairwise variance identity is
\[
 \sum_{i<j}\eta_i\eta_j\|u_i-u_j\|^2
 =W\sum_i\eta_i\|u_i-\bar u_\eta\|^2
 =WV_\eta.
\tag{12}
\]
Indeed, expansion of the left side gives
\[
 W\sum_i\eta_i\|u_i\|^2
 -\left\|\sum_i\eta_i u_i\right\|^2,
\tag{13}
\]
which is exactly the expansion of the middle expression in (12). For every pair,
\[
 \min\{\eta_i,\eta_j\}
 \geq\frac{\eta_i\eta_j}{\eta_{\max}},
\tag{14}
\]
because \(\max\{\eta_i,\eta_j\}\leq\eta_{\max}\). Equations (12)-(14) imply
\[
 \begin{aligned}
 \mathbb E\mathcal E_\eta(M)
 &=p_N\sum_{i<j}
   \min\{\eta_i,\eta_j\}\|u_i-u_j\|^2\\
 &\geq\frac{p_N}{\eta_{\max}}
   \sum_{i<j}\eta_i\eta_j\|u_i-u_j\|^2\\
 &=p_N\frac{W}{\eta_{\max}}V_\eta,
 \end{aligned}
\tag{15}
\]
proving (6). Since the set of perfect or near-perfect matchings is finite, at least one realization has energy no smaller than its expectation.

Under (7),
\[
 W\geq N\eta_{\min}
 \geq\frac{N}{K}\eta_{\max}.
\tag{16}
\]
Substituting (16) and the two values of \(p_N\) from (2) into (6) proves (8). If all weights equal \(\eta\), then
\[
 \min\{\eta_i,\eta_j\}
 =\eta
 =\frac{\eta_i\eta_j}{\eta_{\max}},
\tag{17}
\]
so (14)-(16) are equalities, with \(K=1\), and the inequality in (6) is an equality.
If all pairwise distances are equal, every matching of the relevant cardinality has the same number of pairs of the same squared length. Its energy therefore equals the expectation, which proves the attainment assertion following (8).

Finally, a quotient of the finite-dimensional real Hilbert space \(\mathbb R^d\) by a linear subspace \(L\), equipped with the norm in (9), is again a real Hilbert space. Applying the proved statements to the distinct labels in \(I_E\) therefore gives the asserted edgewise matching. A matching uses each of its indices at most once. Hence it is occurrence-disjoint on \(E\) and whole-label-disjoint inside \(I_E\). Disjointness of the sets \(I_E\) across edges makes their union globally whole-label-disjoint, while summing the separate deterministic inequalities proves the final assertion.

## External sources

none
