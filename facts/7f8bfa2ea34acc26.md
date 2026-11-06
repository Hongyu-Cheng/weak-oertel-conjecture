---
fact_id: 7f8bfa2ea34acc26
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: ternary-affine-majorant-curvature-combined-no-go
depends_on: ["0bcc51d8cd216cf3","604889294a17d7df","6d6fcf377e68c79c"]
verifier_run: aef20b5ee3fe49ff
target_match: null
---

## Statement

For integers \(n,d\ge1\) and a convex body \(C\subseteq\mathbb R^n\times\mathbb R^d\), let \(w_{\mathbf z}=\operatorname{vol}_d\{\mathbf y:(\mathbf z,\mathbf y)\in C\}\), \(D_+=\{\mathbf z\in\mathbb Z^n:w_{\mathbf z}>0\}\), \(W=\sum_{\mathbf z\in D_+}w_{\mathbf z}>0\), and \(M(w)=\max_{\mathbf z\in\mathbb Z^n}w_{\mathbf z}\). The integer table is zero outside \(D_+\). We use the following canonical quantities, with exactly the normalization recorded in accepted fact 604889294a17d7df:

\[
\begin{aligned}
S_{\mathbf j}(w)&=\sum_{\mathbf v\in\mathbb Z^n}\min\{w_{\mathbf j+\mathbf v},w_{\mathbf j-\mathbf v}\},
&S_*(w)&=\max_{\mathbf j\in\mathbb Z^n}S_{\mathbf j}(w),\\
\alpha(\mathbf v)&=\min\{w_{\mathbf j+\mathbf v},w_{\mathbf j-\mathbf v}\},
&\mathcal U_{\mathbf j}&=\{\mathbf v:\alpha(\mathbf v)>0\},\\
\Delta_{\mathbf j}(\mathbf v)&=\log\frac{w_{\mathbf j}^2}{w_{\mathbf j+\mathbf v}w_{\mathbf j-\mathbf v}},
&B_{\mathbf j}^{\Delta}(R)&=\sum_{\substack{\mathbf v\in\mathcal U_{\mathbf j}\\\Delta_{\mathbf j}(\mathbf v)\le R}}\alpha(\mathbf v),\\
K(w)&=\max_{\substack{\mathbf j\in D_+\\R\ge0}}\frac{B_{\mathbf j}^{\Delta}(R)}{1+R}.
\end{aligned}
\]

Here \(\alpha,\mathcal U_{\mathbf j},\Delta_{\mathbf j}\) are defined at a fixed positive center \(\mathbf j\), and \(\Delta_{\mathbf j}\) is defined only on \(\mathcal U_{\mathbf j}\). All logarithms are natural. The displacement sums are oriented: both nonzero displacements \(\mathbf v\) and \(-\mathbf v\) are counted, and zero is counted exactly once. The cutoff \(R\) is the parameter called \(L\) in accepted fact 604889294a17d7df. Its integer dimension \(N\) is the dimension called \(n\) in these general definitions. In particular, \(M(w)\) is the maximum fiber volume.

Set \(\gamma_d=(d/(d+1))^d\), \(\theta_d=1-\gamma_d\), and \((t)_+=\max\{t,0\}\). For every affine \(L:\mathbb R^n\to\mathbb R\) satisfying \(L(\mathbf z)\ge w_{\mathbf z}^{1/d}\) on \(D_+\), define

\[
Q_L=\sum_{\mathbf z\in D_+}\bigl(w_{\mathbf z}-\theta_d L(\mathbf z)^d\bigr)_+,
\qquad
\mathcal A_d(w)=\sup_{\substack{L\text{ affine}\\L(\mathbf z)\ge w_{\mathbf z}^{1/d}\ (\mathbf z\in D_+)}}Q_L.
\]

The class is nonempty because it contains a sufficiently large positive constant. Each admissible \(L\) is positive on \(\operatorname{conv}(D_+)\). Under the exact substitution \(\varphi=L|_{\operatorname{conv}(D_+)}\), its \(Q_L\) is the \(Q_\varphi\) of accepted fact 0bcc51d8cd216cf3. The source's \(\mathcal A_d\) is precisely this affine-subclass supremum. The accepted consumer gives \(h_{\max}(C)\ge2^{-n}\mathcal A_d(w)\), where \(h_{\max}(C)\) is the supremum of the locked halfspace depth over \(C\cap(\mathbb Z^n\times\mathbb R^d)\). Only this affine subclass is used below. The displayed definition of \(\mathcal A_d\) also makes sense for any finite nonempty positive table and integer exponent \(d\ge1\), without an actual-body hypothesis.

Fix any integer \(m\ge2\). Define

\[
\begin{aligned}
r_m(\mathbf x)&=1-\frac{3}{4m}\sum_{i=1}^m|x_i|
\qquad(\mathbf x\in[-1,1]^m),\\
B_m&=\left\{(\mathbf x,\mathbf y)\in\mathbb R^m\times\mathbb R^m:
\mathbf x\in[-1,1]^m,\quad |y_i|\le\frac{r_m(\mathbf x)}2\ (1\le i\le m)\right\}.
\end{aligned}
\]

This is a full-dimensional rational compact convex polytope with exact positive integer-fiber support \(\{-1,0,1\}^m\). If \(s\) coordinates of \(\mathbf x\) are nonzero, its fiber volume is \(u_{\mathbf x}=u_s=(1-3s/(4m))^m\). Put \(W_B=\sum_{s=0}^m\binom ms2^s u_s\). Then \(\max u_{\mathbf x}=1\) and \(W_B\ge(3/4)^m\).

For every integer \(r\ge0\), every finite nonempty \(E\subseteq\mathbb Z^r\), every positive table \((a_{\mathbf z})_{\mathbf z\in E}\), and every integer \(D\ge m\), put \(W_A=\sum_{\mathbf z\in E}a_{\mathbf z}\). Define \(a\otimes u\) by \((a\otimes u)_{(\mathbf z,\mathbf x)}=a_{\mathbf z}u_{\mathbf x}\) on \(E\times\{-1,0,1\}^m\), and zero elsewhere. Then

\[
\mathcal A_D(a\otimes u)\le\left(\frac{28}{29}\right)^m W_AW_B.
\tag{1}
\]

In particular, (1) applies to the actual fiber table of a product of \(B_m\) with any other convex body having positive mixed volume, with \(D\) equal to the product's continuous dimension.

For the combined construction, set \(k=2^{128\cdot16^m}\) and take the exact body \(A_m=C_{k,k^3}\) of accepted fact 604889294a17d7df. More explicitly, compute its entrance counts and dimensions from the exact rational profile as follows:

\[
\begin{aligned}
\rho_t&=(1-t/k^3)^{k^3}\qquad(0\le t\le k),\\
b_\ell&=0\quad(1\le\ell<8),
&b_\ell&=\left\lfloor\frac1{8\ell\rho_\ell}\right\rfloor\quad(8\le\ell\le k),\\
Q_0&=0,
&Q_\ell&=\sum_{j=1}^{\ell}b_j,\qquad Q=Q_k,\\
\lambda_0&=0,
&\lambda_s&=\ell\quad\text{when }Q_{\ell-1}<s\le Q_\ell,\\
\mathfrak m&=2(Q+1)^4,
&n_A&=1+\sum_{j=1}^Q\mathfrak m^j.
\end{aligned}
\]

Here \(\lambda_s\) is exactly the entrance height denoted \(a_s\) in accepted fact 604889294a17d7df; \(\mathfrak m\) is its tree branching parameter denoted \(m\), and its integer dimension \(N\) is \(n_A\). Use the precise tree objects \(\mathcal T_{\mathfrak m,Q},A_{\mathfrak m,Q},P_{\mathfrak m,Q}\) specified there, at these newly computed parameters. Write \(\mathbf x_A\in\mathbb R^{n_A-1}\) for a real tree vector, \(\mathbf z_A\) for a lattice tree point, \(\operatorname{level}(\mathbf z_A)\) for its number of coordinates equal to two, and \(|u|\) for the depth of tree node \(u\). The exact base polytope and lattice support are

\[
\begin{aligned}
\widehat P&=\left\{(\mathbf x_A,t):\mathbf x_A\in P_{\mathfrak m,Q},\quad
0\le t\le k,\quad t\ge\lambda_{|u|}((\mathbf x_A)_u-1)\ (u\in\mathcal T_{\mathfrak m,Q})\right\},\\
\widehat A&=\widehat P\cap\mathbb Z^{n_A}
=\left\{(\mathbf z_A,t):\mathbf z_A\in A_{\mathfrak m,Q},\quad
\lambda_{\operatorname{level}(\mathbf z_A)}\le t\le k,\quad t\in\mathbb Z\right\}.
\end{aligned}
\]

The actual body \(A_m\) has base \(\widehat P\) and continuous fibers \([-(1-t/k^3)/2,(1-t/k^3)/2]^{k^3}\). Consequently its actual table is \(a_{(\mathbf z_A,t)}=\rho_t\) on \(\widehat A\), zero elsewhere, and its continuous dimension is \(k^3\).

Let \(C_m=A_m\times B_m\), with the coordinates permuted to put all integer coordinates first. Its integer and continuous dimensions are \(N_m=n_A+m\) and \(D_m=k^3+m\). It is a full-dimensional rational compact convex polytope. Its complete integer-fiber support is \(\widehat A\times\{-1,0,1\}^m\), its actual table is \(w^{(m)}=a\otimes u\), and its total mixed volume is \(W_m=W_AW_B\). These actual tables satisfy

\[
\begin{aligned}
\frac{M(w^{(m)})}{2^{-N_m}W_m}&<6^{-m},\\
\frac{K(w^{(m)})}{2^{-N_m}W_m}&<2^{-m},\\
\frac{\mathcal A_{D_m}(w^{(m)})}{W_m}&\le\left(\frac{28}{29}\right)^m.
\end{aligned}
\tag{2}
\]

Writing \(\mathcal S_m=C_m\cap(\mathbb Z^{N_m}\times\mathbb R^{D_m})\), there is one point \(\mathbf p_m\in\mathcal S_m\), selected before the containing halfspace, such that \(h_{\mathcal S_m}(\mathbf p_m)\ge2^{-N_m-1}W_m\), with the locked problem's depth definition. Hence, for every fixed \(c_M,c_K,c_A\ge0\),

\[
\frac{c_M M(w^{(m)})+c_K K(w^{(m)})+c_A2^{-N_m}\mathcal A_{D_m}(w^{(m)})}{2^{-N_m}W_m}
\longrightarrow0
\qquad(m\to\infty),
\tag{3}
\]

although the actual depth at \(\mathbf p_m\), divided by \(2^{-N_m}W_m\), is at least \(1/2\).

## Proof

On \([-1,1]^m\), the function \(r_m\) is concave and satisfies \(1/4\le r_m\le1\). The defining conditions of \(B_m\) are equivalent to the cube inequalities and the finite rational linear inequalities \(2\epsilon y_i+(3/(4m))\boldsymbol\sigma^{\mathsf T}\mathbf x\le1\), for every \(1\le i\le m\), \(\epsilon\in\{-1,1\}\), and \(\boldsymbol\sigma\in\{-1,1\}^m\). Thus \(B_m\) is a rational compact convex polytope. It contains \([-1,1]^m\times[-1/8,1/8]^m\), so it is full-dimensional. Its projection is exactly \([-1,1]^m\), and every base point there has a positive-volume cube fiber. Its complete integer support and the formula for \(u_s\) follow. Each of its \(3^m\) integer fibers has volume at least \(4^{-m}\), proving \(W_B\ge(3/4)^m\). The central fiber has volume one, the maximum.

We prove (1) for the stated arbitrary finite table. Fix an admissible affine majorant and write \(L(\mathbf z,\mathbf x)=L(\mathbf z,\mathbf0)+\sum_{i=1}^m\beta_i x_i\). For coordinate \(i\), designate the sign \(\epsilon_i=1\) if \(\beta_i\ge0\), and \(\epsilon_i=-1\) if \(\beta_i<0\). Suppose \(x_i=\epsilon_i\), and let \(\mathbf x'\) be obtained by replacing that coordinate by zero. If \(\mathbf x\) has \(s\ge1\) nonzero coordinates, then \(\mathbf x'\) has \(s-1\), and both points belong to the full ternary support. Affinity gives \(L(\mathbf z,\mathbf x)-L(\mathbf z,\mathbf x')=|\beta_i|\ge0\). Because both affine values are positive and \(L\) majorizes the product roots, \(L(\mathbf z,\mathbf x)^D\ge a_{\mathbf z}u_{s-1}\).

The two binomial estimates needed for uniform constants are

\[
\begin{aligned}
(1+1/D)^D&\ge2+\frac{D-1}{2D}\ge\frac94
\qquad(D\ge2),\\
\left(1+\frac3{4m}\right)^m
&\ge1+\frac34+\frac{9(m-1)}{32m}\ge\frac{121}{64}
\qquad(m\ge2).
\end{aligned}
\]

Thus \(\theta_D\ge5/9\). Also, for \(1\le s\le m\),

\[
\frac{u_{s-1}}{u_s}
=\left(1+\frac3{4m-3s}\right)^m
\ge\left(1+\frac3{4m}\right)^m
\ge\frac{121}{64},
\qquad
\frac{\theta_Du_{s-1}}{u_s}\ge\frac{605}{576}>1.
\]

It follows that \((a_{\mathbf z}u_{\mathbf x}-\theta_D L(\mathbf z,\mathbf x)^D)_+=0\) whenever \(x_i=\epsilon_i\) for at least one coordinate. This includes \(\beta_i=0\), for which our designated sign remains valid. Therefore all positive excess is confined to \(\mathbf x\in\prod_{i=1}^m\{0,-\epsilon_i\}\).

Give \(\{-1,0,1\}^m\) probability mass \(u_{\mathbf x}/W_B\), and denote its random vector by \(X\). If every coordinate other than \(i\) is fixed and \(s\) of them are nonzero, the conditional probability of \(X_i=\epsilon_i\) is \(u_{s+1}/(u_s+2u_{s+1})\). Here \(0\le s\le m-1\), and

\[
\frac{u_{s+1}}{u_s}
=\left(1-\frac3{4m-3s}\right)^m
\ge\left(\frac m{m+3}\right)^m
>e^{-3}>\frac1{27}.
\]

The first strict inequality follows from \(\log(1+3/m)<3/m\). The second uses \(e<3\), obtained directly from the exponential series and \(j!\ge2^{j-1}\) for \(j\ge2\), with strict inequality for \(j\ge3\). Since \(t\mapsto t/(1+2t)\) is increasing for \(t>0\), every one of these conditional probabilities exceeds \(1/29\).

For each \(i\), the event \(X_j\ne\epsilon_j\) for \(j<i\) depends only on coordinates other than \(i\). Averaging the preceding conditional bound over those other coordinates proves that \(X_i=\epsilon_i\) still has conditional probability greater than \(1/29\) given that event. Every such conditioning event has positive probability because all ternary weights are positive. Successive conditioning consequently gives

\[
\mathbb P(X_i\ne\epsilon_i\text{ for every }i)
=\prod_{i=1}^m\mathbb P(X_i\ne\epsilon_i\mid X_j\ne\epsilon_j\text{ for }j<i)
\le\left(\frac{28}{29}\right)^m.
\]

Each excess summand is at most its original weight. Summing only over the possible positive-excess support therefore gives \(Q_L\le W_AW_B\,\mathbb P(X_i\ne\epsilon_i\text{ for every }i)\). This bound is uniform over all affine majorants, so taking their supremum proves (1). No property of the first table beyond its finite positive support has been used.

We next verify the actual combined construction and (2). Our \(k\) is an integer at least eight, and \(k^3\ge2k\). The rational specialization of accepted fact 604889294a17d7df therefore applies with its continuous dimension \(d=k^3\). In particular, after computing its entrance counts from \(\rho_t=(1-t/k^3)^{k^3}\), it supplies precisely the rational body, dimensions, and complete lattice support stated above. All these fibers are the actual cubes, with their stated positive rational volumes. That accepted fact gives, at these same rebuilt parameters,

\[
M(a)=S_*(a)=1,
\qquad
T_A:=\frac{W_A}{2^{n_A}}\ge\frac3{64}(H_k-H_7),
\qquad H_k=\sum_{j=1}^k\frac1j.
\]

For the strict size estimate, \(H_k>\log k\), \(\log2>1/2\), and \(H_7<3\). The logarithm bound follows by integrating \(1/x>1/2\) on the interior of \([1,2]\); the harmonic comparison follows by integrating the decreasing function \(1/x\). Hence \(T_A>(3/64)(64\cdot16^m-3)=3\cdot16^m-9/64>16^m\).

The product, followed by the coordinate permutation, preserves rationality, compactness, convexity, and full dimension. Its projection is \(\widehat P\times[-1,1]^m\), so the previously proved exact supports show that every integer point in this projection has exactly the product of the stated positive cube fibers, and no other integer index has a nonempty fiber. Product Lebesgue volume gives \(w^{(m)}=a\otimes u\) and \(W_m=W_AW_B\). The equality \(M(w^{(m)})=M(a)\max u=1\) is attained. Also,

\[
2^{-N_m}W_m
=\frac{T_AW_B}{2^m}
>16^m\left(\frac38\right)^m
=6^m.
\tag{4}
\]

This proves the first inequality in (2).

The table \(a\) has the globally log-concave extension supplied in accepted fact 604889294a17d7df. The function \(r_m^m\) is positive and log-concave on its cube: concavity and positivity of \(r_m\), followed by the weighted arithmetic-geometric mean inequality, give its log-concavity. Extending it by zero off the cube preserves log-concavity. The product of these two functions on the product support is therefore a globally log-concave extension of the actual table \(w^{(m)}\). In particular every positive reflected pair at a positive center has the finite nonnegative curvature used in the canonical definition of \(K\), and the zero displacement has curvature zero.

Fix any product integer center \((\mathbf j,\boldsymbol\xi)\). The retained oriented displacements in the second factor belong to \(V_{\boldsymbol\xi}=\{\boldsymbol\eta\in\mathbb Z^m:\boldsymbol\xi+\boldsymbol\eta,\boldsymbol\xi-\boldsymbol\eta\in\{-1,0,1\}^m\}\). The map \(\boldsymbol\eta\mapsto\boldsymbol\xi+\boldsymbol\eta\) is injective, so \(|V_{\boldsymbol\xi}|\le3^m\). Each second-factor endpoint volume is at most one. With \(a\) extended by zero as stipulated, we obtain

\[
\begin{aligned}
S_{(\mathbf j,\boldsymbol\xi)}(w^{(m)})
&=\sum_{\boldsymbol\eta\in V_{\boldsymbol\xi}}\sum_{\mathbf v\in\mathbb Z^{n_A}}
\min\{a_{\mathbf j+\mathbf v}u_{\boldsymbol\xi+\boldsymbol\eta},
a_{\mathbf j-\mathbf v}u_{\boldsymbol\xi-\boldsymbol\eta}\}\\
&\le|V_{\boldsymbol\xi}|\sum_{\mathbf v\in\mathbb Z^{n_A}}\min\{a_{\mathbf j+\mathbf v},a_{\mathbf j-\mathbf v}\}
\le3^m.
\end{aligned}
\]

This counts both nonzero orientations and zero exactly as in \(S_{\mathbf j}(a)\); no unordered-pair factor is introduced. For every positive center and every cutoff \(R\ge0\), the cutoff sum is at most \(S_{\mathbf j}(w^{(m)})\), and \(1+R\ge1\). Thus \(K(w^{(m)})\le S_*(w^{(m)})\le3^m\). Together with (4), this gives \(K(w^{(m)})/(2^{-N_m}W_m)<3^m/6^m=2^{-m}\), proving the second inequality in (2). Applying (1) with \(E=\widehat A\), \(r=n_A\), and \(D=D_m=k^3+m\) proves its third inequality.

It remains to verify the actual depth at a single point. Apply accepted fact 6d6fcf377e68c79c to the finite measure \(\nu=\sum_{\mathbf I}w^{(m)}_{\mathbf I}\delta_{\mathbf I}\) on the integer base. Its parameters in that theorem are \(n=N_m\) and \(d=0\), and its total mass is \(W_m\). It supplies one \(\mathbf j_m\in\mathbb Z^{N_m}\) such that every closed base halfspace containing \(\mathbf j_m\) has \(\nu\)-mass at least \(2^{-N_m}W_m\). The point belongs to \(\widehat P\times[-1,1]^m\): otherwise strict separation from that compact convex set would give a closed halfspace containing \(\mathbf j_m\) with zero \(\nu\)-mass. By the exact integer support, its actual fiber is positive. Every actual fiber is centrally symmetric about \(\mathbf0\), so fix \(\mathbf p_m=(\mathbf j_m,\mathbf0)\in\mathcal S_m\) now.

For an arbitrary proper closed ambient halfspace whose boundary passes through \(\mathbf p_m\), write its inequality as \(\mathbf a_H^{\mathsf T}(\mathbf I-\mathbf j_m)+\mathbf b_H^{\mathsf T}\mathbf y\ge0\), with \((\mathbf a_H,\mathbf b_H)\ne(\mathbf0,\mathbf0)\). If \(\mathbf a_H\ne\mathbf0\), let \(G=\{\mathbf I:\mathbf a_H^{\mathsf T}(\mathbf I-\mathbf j_m)\ge0\}\). If \(\mathbf a_H=\mathbf0\), let \(G=\mathbb R^{N_m}\). In both cases \(\nu(G)\ge2^{-N_m}W_m\). At each positive index in \(G\), the ambient halfspace contains the portion of that fiber satisfying \(\mathbf b_H^{\mathsf T}\mathbf y\ge0\). Central symmetry gives at least half its volume; when \(\mathbf b_H=\mathbf0\), the entire fiber is included, including fibers on the vertical boundary. Summing the actual fiber volumes gives mixed mass at least \(\nu(G)/2\ge2^{-N_m-1}W_m\).

Every proper closed halfspace containing \(\mathbf p_m\) contains the parallel halfspace with boundary through \(\mathbf p_m\). Monotonicity gives the same bound for it, and the whole-space case is immediate if included in the convention. The point \(\mathbf p_m\) was chosen before any of these halfspaces, so this proves the asserted locked depth bound with the required quantifier order.

Finally (2) bounds the nonnegative expression in (3) by \(c_M6^{-m}+c_K2^{-m}+c_A(28/29)^m\), which tends to zero. In particular, no positive absolute lower bound at scale \(2^{-n}W\) holds uniformly for \(M(w)+K(w)+2^{-n}\mathcal A_d(w)\) or \(\max\{M(w),K(w),2^{-n}\mathcal A_d(w)\}\), even on this family of actual rational bodies. Their depth lower bound simultaneously remains at least one half of that scale. The identification with accepted fact 0bcc51d8cd216cf3 was the restriction \(\varphi=L\); the proof does not bound its larger class of all positive convex majorants. The construction therefore refutes the stated scalar coverage principle and supplies no disproof of the locked weak Oertel conjecture.

## External sources

None beyond the declared accepted predecessors. Accepted fact 604889294a17d7df supplies the exact rebuilt rational tree bodies and their mass and reflected-minimum bounds; 6d6fcf377e68c79c supplies the weighted lattice centerpoint; and 0bcc51d8cd216cf3 supplies the exact affine-subclass majorant consumer. The unverified starting passage was `.math-prover/source_archives/2026-09-07/parity-comparison.txt`, lines 570-930. Every new factor, product estimate, and depth calibration used here is proved above.
