# A quantitative centroid certificate at a nonvertex high core

Status: pending auxiliary lemma. This is a direct calculation from ordinary Grünbaum and Brunn–Minkowski. It is related to the strict nonvertex improvement in pending `24ea9b953da308e9` and its parity consequences in `5904b09673c3b836`, but uses no conclusion from either. Its role is to justify a restricted structural consequence of failed sharp depth, not a global extremal classification.

Let (C\subset\mathbb R^n\times\mathbb R^d\) be convex and compact, with (d\ge1\). Write (K_z\) for its fibers. Suppose distinct bases (z_1,\ldots,z_k\), all different from an integer base (w\), have positive-volume fibers (V_i=|K_{z_i}|\), and
\[
 \lambda_i>0,\qquad \sum_i\lambda_i=1,\qquad
 \sum_i\lambda_i z_i=w.
\]
The bases (z_i\) are integral when their cap masses are charged to the mixed source. Let (g_i\) be their actual centroids and put (y=\sum_i\lambda_i g_i\). Then (y\in K_w\), and
\[
 h_S((w,y))\ge\Gamma_d\left[
 \left(\sum_i\lambda_i V_i^{1/d}\right)^d+\min_i V_i
 \right]. \tag{1}
\]

To prove this, consider a through-point halfspace
\[
 a\cdot(z-w)+u\cdot(x-y)\ge0.
\]
If (u\ne0\), the own-fiber cap contains the Minkowski combination of the continuous centroid caps (K_{z_i}\cap\{x:u\cdot(x-g_i)\ge0\}\). Convexity supplies containment, and each summand has volume at least (\Gamma_d V_i\). Brunn–Minkowski therefore gives the first term of (1). Meanwhile
\[
 \sum_i\lambda_i[a\cdot(z_i-w)+u\cdot(g_i-y)]=0.
\]
At least one actual endpoint centroid lies in the ambient halfspace. That endpoint's cap has volume at least (\Gamma_d V_i\ge\Gamma_d\min_i V_i\). Its base differs from (w\), so it is an additional disjoint contribution. This proves (1). If (u=0\), the own fiber is wholly contained, and the same weighted base-score identity includes an entire endpoint fiber. Convexity and Brunn–Minkowski give (V_w\ge(\sum_i\lambda_i V_i^{1/d})^d\); the resulting lower bound is stronger than (1). Every containing halfspace contains its parallel through-point halfspace. All centers and charged fibers are actual, and no boundary mass is removed.

## A high-core consequence under a failure hypothesis

Use the parity-core notation (P,L,V,E,W\) of the local-deficit note. Suppose (F_r\le\varepsilon V\) for every parity, put
\[
 G=\{w\in P:V_w\ge(1-\eta)V\},
\]
and assume
\[
 0<\eta<1,\quad 0\le\varepsilon<1-\eta,\quad
 2(1-\eta)>1+\varepsilon.
\]
If no actual point has depth at least (\Gamma_d W/L\), then

1. (G=\operatorname{conv}(G)\cap\mathbb Z^n\).
2. Every member of (G\) is a vertex of (\operatorname{conv}(G)\).
3. If (B=P\setminus G\), then (|B|\eta V<\Delta<E\le L\varepsilon V\) when (B\ne\varnothing\), where (\Delta=\sum_{w\in P}(V-V_w)\).

For the first assertion, any integer point in the convex hull of the high bases has fiber volume at least ((1-\eta)V\), by convexity and Brunn–Minkowski. It cannot be an outside fiber because every such fiber has volume at most (\varepsilon V<(1-\eta)V\). It must therefore be in the core and high. For the second assertion, a nonvertex (w\in G\) is a convex combination of other members of (G\). Equation (1) gives a point of depth at least (2\Gamma_d(1-\eta)V\). But (W/L\le V+E/L\le(1+\varepsilon)V\), contradicting the displayed strict inequality and the failure hypothesis. For the third, the largest-core centroid already has depth at least (\Gamma_d V\); failure implies (V<W/L\), or (\Delta<E\). Each bad core contributes more than (\eta V\) to (\Delta\), and summing the parity bounds gives the last inequality.

Thus a putative failure in this regime has an almost complete parity set of high fibers whose convex hull contains no lattice points other than its vertices. This implication alone does not control outside incidence: the exact slab-obstruction note supplies empty cores with one low target and many incident partners. The cap-depth hypothesis, or a new geometric repair, remains essential.
