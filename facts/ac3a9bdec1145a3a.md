---
fact_id: ac3a9bdec1145a3a
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: signed-consecutive-coefficient-knapsack-reflection
depends_on: ["280b299bc1e87c14","9272a9ce484e5757","a3507c471fff4ad1"]
verifier_run: e8da546b5db1431f
target_match: null
---

## Statement

Let \(n\ge2\) and \(B\ge1\) be integers, let \(R\ge0\) be real, and let \(a=(a_1,\ldots,a_n)\in\mathbb R^n\) be arbitrary. Put \(b=(B,B+1,\ldots,B+1)\) and

\[
\begin{aligned}
D&:=\{z\in\mathbb Z_{\ge0}^n:b\cdot z\le R\},\\
\widetilde w_z&:=
\begin{cases}
e^{-a\cdot z},&z\in D,\\
0,&z\notin D,
\end{cases}\\
\widetilde W&:=\sum_{z\in\mathbb Z^n}\widetilde w_z,\qquad
\widetilde S_j:=\sum_{v\in\mathbb Z^n}
\min\{\widetilde w_{j+v},\widetilde w_{j-v}\}.
\end{aligned}
\tag{1}
\]

The reflection sums are oriented and include zero. There exists \(j\in D\) such that

\[
\widetilde S_j\ge \frac{e^{-500}}2\,2^{-n}\widetilde W.
\tag{2}
\]

For the actual mixed-volume consequence, let \(d\ge1\) be an integer and let \(C\subset\mathbb R^n\times\mathbb R^d\) be a convex body. Define \(C_z:=\{y\in\mathbb R^d:(z,y)\in C\}\) and \(w_z:=\operatorname{vol}_d(C_z)\), with zero volume for empty or lower-dimensional fibers. Suppose that

\[
\{z\in\mathbb Z^n:w_z>0\}=D,\qquad
\frac K M e^{-a\cdot z}\le w_z\le KM e^{-a\cdot z}
\quad(z\in D)
\tag{3}
\]

for some \(K>0\) and \(M\ge1\). Put \(W:=\sum_{z\in\mathbb Z^n}w_z\), \(S:=C\cap(\mathbb Z^n\times\mathbb R^d)\), and \(h_S(p):=\inf_{H\ni p}\mathcal H_d(S\cap H)\), with the infimum over closed ambient halfspaces. These actual objects have exactly their meanings in accepted fact 280b299bc1e87c14, with the same integer dimension \(n\) and continuous dimension \(d\); the tilded quantities in (1) are separate scalar objects.

The same center \(j\) can be chosen to have a point \(y^\star\in C_j\) such that \(p^\star:=(j,y^\star)\in S\) satisfies

\[
h_S(p^\star)\ge c(M)\,2^{-n}W,\qquad
c(M):=\frac{-\log(1-e^{-1})\,e^{-500}}
{32M^2(1+4\log M)}>0.
\tag{4}
\]

For each fixed \(M\), this constant is independent of \(n,d,B,R,a,K\) and all fiber shapes. The point is selected before the halfspace, and the same point satisfies the bound for every closed ambient halfspace containing it. No divisibility condition on the budget and no sign condition on \(a\) is imposed. All logarithms are natural.

## Proof

Because \(b\) has positive integer entries, \(D\) is finite and contains zero, so \(0<\widetilde W<\infty\). Let \(H:=\lfloor R\rfloor\) and write its Euclidean division by \(B+1\) as \(H=(B+1)q+r\), where \(q,r\) are integers with \(q\ge0\) and \(0\le r\le B\). Here \(H\) is the integer budget, distinct from a halfspace in the definition of depth. Since \(b\cdot z\) is integral for every lattice point, replacing \(R\) by \(H\) leaves the complete support \(D\) unchanged.

For every \(z\in\mathbb Z^n\), define \(p:=\sum_{i=1}^n z_i-q\), \(\sigma:=H-b\cdot z\), and \(k_i:=z_i\) for \(2\le i\le n-1\). The vector \(k\) is empty when \(n=2\), and its sums are then zero. The identity \(b\cdot z=(B+1)\sum_i z_i-z_1\) gives the inverse formulas

\[
\begin{aligned}
z_1&=(B+1)p+\sigma-r,\\
z_i&=k_i\quad(2\le i\le n-1),\\
z_n&=q-Bp-\sigma+r-\sum_{i=2}^{n-1}k_i.
\end{aligned}
\tag{5}
\]

These formulas invert \(z\mapsto(p,\sigma,k)\) on the whole lattice, not just on \(D\): their coordinate sum is \(q+p\), and substituting them into \(H-b\cdot z\) gives \(\sigma\). Both this map and its inverse are affine with integer coefficients. Their linear parts are therefore inverse integer matrices, so their determinants have absolute value one.

Partition \(D\) into \(D_+:=\{z\in D:p\ge1\}\) and \(D_-:=\{z\in D:p\le0\}\). Since \(p\) is an integer, these pieces are disjoint and cover \(D\). Define the restricted original profiles \(\widetilde w_z^\pm:=\widetilde w_z\mathbf 1_{\{z\in D_\pm\}}\), their masses \(\widetilde W_\pm:=\sum_z\widetilde w_z^\pm\), and their reflection sums \(\widetilde S_j^\pm:=\sum_v\min\{\widetilde w_{j+v}^\pm,\widetilde w_{j-v}^\pm\}\). Thus

\[
\widetilde W=\widetilde W_++\widetilde W_-,
\qquad
\widetilde S_j\ge\widetilde S_j^\pm\quad(j\in\mathbb Z^n).
\tag{6}
\]

We will use affine unimodular changes of coordinates only on these scalar profiles. If \(T(z)=Uz+c\), with \(U\) an invertible integer matrix whose inverse is integral and \(c\in\mathbb Z^n\), then \(T(j\pm v)=T(j)\pm Uv\). The map \(v\mapsto Uv\) is a bijection of \(\mathbb Z^n\). Transporting each weight unchanged under \(T\) consequently preserves the total mass and the reflection sum at corresponding centers. This reindexing preserves both orientations and zero. Multiplying every weight by a positive constant also multiplies both sums by that constant.

For the upper piece, put \(Q:=q+r-B\), \(t:=p-1\), and \(x=(x_1,\ldots,x_{n-1}):=(\sigma,k_2,\ldots,k_{n-1})\). Formula (5) becomes

\[
\begin{aligned}
z_1&=(B+1)(t+1)+x_1-r,\\
z_i&=x_i\quad(2\le i\le n-1),\\
z_n&=Q-Bt-\sum_{i=1}^{n-1}x_i.
\end{aligned}
\tag{7}
\]

The affine map \(z\mapsto(x,t)\) is a permutation and an integer translation after the unimodular map in (5), and (7) is its integer affine inverse. It takes \(D_+\) exactly onto

\[
E_+:=\left\{(x,t)\in\mathbb Z_{\ge0}^{n-1}\times\mathbb Z_{\ge0}:
Bt+\sum_{i=1}^{n-1}x_i\le Q\right\}.
\tag{8}
\]

Indeed, \(z\in D_+\) gives \(t,x\ge0\), and \(z_n\ge0\) is precisely the inequality in (8). Conversely, for a point of (8), formula (7) gives \(z_n\ge0\), all the middle coordinates nonnegative, and \(z_1\ge B+1-r\ge1\). Formula (5) then gives \(p=t+1\ge1\) and original slack \(\sigma=x_1\ge0\), so \(z\in D_+\). This proves both directions, including equality in the budget.

If \(Q<0\), (8) is empty, so \(D_+\) is empty. If \(Q=0\), (8) consists only of \((x,t)=(0,0)\), since \(B>0\). In this case \(D_+\) is the single original point \((B+1-r,0,\ldots,0)\), and its restricted reflection sum at that point equals \(\widetilde W_+\). It therefore satisfies \(\widetilde S_j^+\ge e^{-500}2^{-n}\widetilde W_+\). It remains to treat \(Q>0\).

Substitution of (7) into the original exponent gives

\[
\begin{aligned}
a\cdot z&=V_+(t)+\sum_{i=1}^{n-1}\gamma_i x_i,\\
\gamma_i&:=a_i-a_n\quad(1\le i\le n-1),\\
V_+(t)&:=a_1(B+1-r)+a_nQ+
\bigl((B+1)a_1-Ba_n\bigr)t.
\end{aligned}
\tag{9}
\]

In particular, \(V_+\) is finite and affine, with no sign restriction on its slope. If every \(\gamma_i\ge0\), leave the coordinates and (9) unchanged. Otherwise choose \(i_0\) with \(\gamma_{i_0}=\min_i\gamma_i<0\), and set

\[
t'=t,\qquad
x_i'=x_i\ (i\ne i_0),\qquad
x_{i_0}'=Q-Bt-\sum_{i=1}^{n-1}x_i.
\tag{10}
\]

This is an integer affine involution on the whole lattice: applying the same formula again restores \(x_{i_0}\), while all other coordinates and \(t\) stay fixed. Its linear part has determinant \(-1\), as it changes only one coordinate row and that row has coefficient \(-1\) in column \(i_0\). On (8), the new coordinate \(x_{i_0}'\) is the nonnegative slack and the new slack is \(x_{i_0}\). Thus (10) maps the complete set \(E_+\) onto itself.

In the new coordinates, the exponent in (9) is exactly

\[
\begin{aligned}
a\cdot z
&=V_+(t)+\gamma_{i_0}(Q-Bt)
-\gamma_{i_0}x_{i_0}'
+\sum_{i\ne i_0}(\gamma_i-\gamma_{i_0})x_i'.
\end{aligned}
\tag{11}
\]

The new horizontal coefficients are \(-\gamma_{i_0}>0\) in coordinate \(i_0\) and \(\gamma_i-\gamma_{i_0}\ge0\) in every other coordinate. The new height potential \(V_+(t)+\gamma_{i_0}(Q-Bt)\) remains finite and affine. This proves that after either the identity or (10), the transported original profile on \(E_+\) has the form \(e^{-V(t)-\widehat a\cdot x}\), with every \(\widehat a_i\ge0\) and \(V\) affine. Here \(x\) denotes the resulting horizontal coordinate vector, \(V\) is the resulting potential just computed, and \(\widehat a\) is the resulting list of horizontal coefficients.

Apply the scalar clause of accepted fact 9272a9ce484e5757 with its total integer dimension \(N=n\), its horizontal dimension \(N-1=n-1\), its interval \([A,B]\) replaced by the present interval \([0,Q/B]\), and its two resource vectors both equal to \((1,\ldots,1)\). In this substitution the predecessor's upper-endpoint symbol \(B\) means the real number \(Q/B\); the \(B\) in that quotient and in (8) remains the original positive integer coefficient. The predecessor's two budget functions are both the present function \(t\mapsto Q-Bt\), and its nonnegative horizontal tilt and convex potential are the present \(\widehat a\) and \(V\). Its continuous dimension is immaterial to this scalar clause and may be taken as \(1\).

These substitutions meet every scalar hypothesis: \(0<Q/B\), both budget functions are continuous, nonnegative and concave on \([0,Q/B]\), positive on its interior, and the potential is finite, continuous and convex. The predecessor's complete support is precisely (8), including its zero-budget endpoint whenever that endpoint is integral. Its scalar profile is the transported original restricted profile, with no change of weights.

The predecessor's curvature \(\widetilde\Delta_J(\xi)\) is zero on every supported reflected pair, because its height potential is affine and its horizontal exponent is linear. Its cutoff parameter with \(N=n\) is \(\Theta_n:=2+(2n-2+2\log3)/(4\sqrt n)>0\). Consequently its cutoff sum \(\widetilde B_J^{\widetilde\Delta}(\Theta_n)\) equals the full reflection sum of this transported profile. Its scalar conclusion gives a center with reflection at least \((1+\Theta_n)e^{-500}2^{-n}\widetilde W_+\), and hence at least \(e^{-500}2^{-n}\widetilde W_+\). By the affine reindexing already proved, this center pulls back to one \(j\in D_+\) with

\[
\widetilde S_j^+\ge e^{-500}2^{-n}\widetilde W_+.
\tag{12}
\]

Here the predecessor's \(\widetilde W\) is the present \(\widetilde W_+\), its \(J\) is the transported center, and its cutoff sum is the transported version of \(\widetilde S_j^+\); it is not the full original profile of (1). The singleton argument proves (12) also for \(Q=0\). The case \(Q<0\) contributes zero mass and needs no center.

For the lower piece, put \(h:=-p\) and \(\sigma':=\sigma-r-(B+1)h\). Formula (5) gives \(\sigma'=z_1\) and the exact inverse

\[
z_1=\sigma',\qquad
z_i=k_i\ (2\le i\le n-1),\qquad
z_n=q-h-\sigma'-\sum_{i=2}^{n-1}k_i.
\tag{13}
\]

The map \(z\mapsto(h,\sigma',k)\) is an integer affine map on the whole lattice with inverse (13). Its forward formulas are \(h=q-\sum_i z_i\), \(\sigma'=z_1\), and \(k_i=z_i\), so the inverse and forward linear parts are integer matrices and its determinant has absolute value one. It maps \(D_-\) exactly onto

\[
E_-:=\left\{(h,\sigma',k)\in\mathbb Z_{\ge0}^n:
h+\sigma'+\sum_{i=2}^{n-1}k_i\le q\right\}.
\tag{14}
\]

For \(z\in D_-\), \(h\ge0\), \(\sigma'=z_1\ge0\) and \(k\ge0\), and \(z_n\ge0\) gives (14). Conversely, (14) and (13) give all original coordinates nonnegative, \(p=-h\le0\), and original slack \(\sigma=r+(B+1)h+\sigma'\ge0\). Thus the reconstructed point belongs to \(D_-\). In particular, this chart has no additional residue or facet restriction. When \(q=0\), (14) is a singleton and (13) sends it to the original point zero.

Write the \(n\) coordinates in (14) as \(y=(h,\sigma',k_2,\ldots,k_{n-1})\). Then

\[
a\cdot z=a_nq+\beta\cdot y,\qquad
\beta=(-a_n,a_1-a_n,a_2-a_n,\ldots,a_{n-1}-a_n).
\tag{15}
\]

If all \(\beta_i\ge0\), no further change is necessary. If a coefficient is negative, choose \(i_0\) minimizing \(\beta_i\) and replace \(y_{i_0}\) by \(y_{i_0}'=q-\sum_{i=1}^n y_i\), leaving the other coordinates fixed. As in (10), this is an integer affine involution of determinant \(-1\) that exchanges that coordinate with the slack and maps the complete unit simplex (14) onto itself. The exponent becomes

\[
a_nq+\beta_{i_0}q
-\beta_{i_0}y_{i_0}'
+\sum_{i\ne i_0}(\beta_i-\beta_{i_0})y_i',
\tag{16}
\]

whose coordinate coefficients are all nonnegative. This calculation also holds for \(q=0\).

After this possible involution, the transported restricted profile is a positive constant times an exponential profile with nonnegative tilt on the full unit simplex with budget \(q\). Apply the scalar clause of accepted fact a3507c471fff4ad1. Its dimension is the present \(n\), its support \(A\) is the simplex \(E_-\) in the resulting coordinates, its resource coefficients \(b_i\) are all \(1\), its budget \(R\) is the integer \(q\), and its tilt coefficients are the nonnegative coefficients in (15) or (16). The constant factor in the transported weights is \(e^{-a_nq}\) in the first case and \(e^{-q(a_n+\beta_{i_0})}\) in the second case. Multiplying the predecessor's scalar total and scalar reflection by this same factor gives exactly the transported restricted total \(\widetilde W_-\) and restricted reflection. Its conclusion and affine reindexing therefore supply an original \(j\in D_-\) such that

\[
\widetilde S_j^-\ge e^{-50}2^{-n}\widetilde W_-
\ge e^{-500}2^{-n}\widetilde W_-.
\tag{17}
\]

This accepted scalar clause allows budget zero; directly, when \(q=0\) the single point has reflection equal to its mass. Thus no degenerate lower piece is omitted.

At least one of the two masses in (6) is at least \(\widetilde W/2>0\). Choose that piece and the center furnished by (12) or (17), using the singleton case when needed. The chosen piece is nonempty. Its original restricted reflection is at most the full original reflection by (6), so (2) follows. This uses complete original mass from both pieces; no residue class or low-height column has been deleted.

We now prove (4) for this same original center \(j\). Retain all actual objects from (3), and use the notation of accepted fact 280b299bc1e87c14:

\[
\begin{aligned}
\alpha(v)&:=\min\{w_{j+v},w_{j-v}\},\\
\mathcal U_j&:=\{v\in\mathbb Z^n:\alpha(v)>0\},\\
\Delta_j(v)&:=\log\frac{w_j^2}{w_{j+v}w_{j-v}}
\quad(v\in\mathcal U_j).
\end{aligned}
\tag{18}
\]

Its center \(j\), oriented displacement \(v\), pair minimum \(\alpha(v)\), pair support \(\mathcal U_j\), and actual curvature \(\Delta_j(v)\) are exactly those in (18). The full-support hypothesis in (3) gives \(\mathcal U_j=\{v:j+v,j-v\in D\}\). Since \(j\in D\), \(w_j>0\) and \(0\in\mathcal U_j\). The actual body is convex, so the predecessor's nonnegativity conclusion gives \(\Delta_j(v)\ge0\).

For every \(v\in\mathcal U_j\), the full original scalar exponent is affine and hence
\(\widetilde w_j^2=\widetilde w_{j+v}\widetilde w_{j-v}\). This concerns all positive original pairs, including pairs whose endpoints belong to different pieces. Applying (3) at the original center and these original endpoints gives

\[
\begin{aligned}
\alpha(v)&\ge \frac K M
\min\{\widetilde w_{j+v},\widetilde w_{j-v}\}
\quad(v\in\mathbb Z^n),\\
0\le\Delta_j(v)&\le
\log\frac{(KM\widetilde w_j)^2}
{(K/M)^2\widetilde w_{j+v}\widetilde w_{j-v}}
=4\log M
\quad(v\in\mathcal U_j),\\
W&\le KM\widetilde W.
\end{aligned}
\tag{19}
\]

In the first inequality, displacements outside the common pair support have both minima zero, so the all-displacement formulation is valid. Combining (19) and (2) yields

\[
\sum_v\alpha(v)
\ge\frac K M\widetilde S_j
\ge\frac{e^{-500}}{2M^2}\,2^{-n}W.
\tag{20}
\]

Use the fixed-center even-thinning assertion of accepted fact 280b299bc1e87c14 with its indexed weights \(q_v:=\alpha(v)\). These indexed weights have their predecessor meaning and are distinct from the integer quotient \(q\) used earlier. They are even, have finite support, satisfy \(0\le q_v\le\alpha(v)\), and have positive mass because \(q_0=w_j>0\). The predecessor's mass \(M_q=\sum_v\alpha(v)\) is distinct from the comparison factor \(M\); its mean curvature \(\overline\Delta_{j,q}\) is at most \(4\log M\) by (19). Its other actual geometric objects and integer and continuous dimensions retain exactly the meanings already specified.

All hypotheses of that lifting assertion hold: \(n,d\ge1\), \(C\) is a convex body, \(w_j>0\), and \(0<W<\infty\). With \(\ell:=-\log(1-e^{-1})\), it therefore supplies one \(y^\star\in C_j\), selected after this original \(j\) and thinning and before every halfspace, such that

\[
\begin{aligned}
h_S((j,y^\star))
&\ge\frac{\ell M_q}{16(\overline\Delta_{j,q}+\log2)}\\
&\ge\frac{\ell}{16(1+4\log M)}\sum_v\alpha(v)\\
&\ge\frac{\ell e^{-500}}{32M^2(1+4\log M)}\,2^{-n}W.
\end{aligned}
\tag{21}
\]

The second inequality uses \(\log2<1\), and the last is (20). This is (4). The accepted lifting assertion includes every closed ambient halfspace containing the selected point, including a vertical halfspace whose boundary contains its central fiber. Zero-volume integer fibers outside \(D\) remain in the mixed set \(S\) and contribute zero to \(W=\mathcal H_d(S)\). The bound uses no restriction on their geometry. Finally, \(M\ge1\) and \(0<\ell<1\), so \(c(M)>0\) and \(c(M)<1/e\). This proves the actual mixed-volume consequence with the stated quantifier order.

## External sources

None. The scalar convex-height conclusion is used from accepted fact 9272a9ce484e5757, the scalar nonnegative-knapsack conclusion from accepted fact a3507c471fff4ad1, and the fixed-center reflected-volume lift from accepted fact 280b299bc1e87c14, with all substitutions and profile normalizations specified above. The two-chart decomposition, both slack involutions, transformed affine weights, all boundary cases, and mass selection are proved directly here.
