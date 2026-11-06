---
fact_id: 5cbf8fde2004faef
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: ternary-block-profile-original-average
depends_on: ["d18d590c47b229bf"]
verifier_run: 13168f5025bf4971
target_match: null
---

## Statement

Let \(n,q\) be positive integers, and partition \([n]=\{1,\ldots,n\}\) into nonempty blocks \(\mathcal B_1,\ldots,\mathcal B_q\) of sizes \(n_j=|\mathcal B_j|\). Here \(\mathcal B_j\) denotes the block called \(B_j\) in the registered subgoal, leaving the predecessor's scalar \(B_1\) distinct. Let \(\Omega\) be any nonempty subset of \(\prod_{j=1}^q\{0,\ldots,2n_j\}\), with no convexity hypothesis. For arbitrary \(\beta\in\mathbb R^n\), define the original objects

\[
\begin{aligned}
D&=\left\{I\in\{0,1,2\}^n:
 \left(\sum_{i\in\mathcal B_j}I_i\right)_{j=1}^q\in\Omega\right\},&
w_I&=e^{-\beta\cdot I},\\
W&=\sum_{I\in D}w_I,&
p_I&=\frac{w_I}{W},\\
\tau_w(J)&=\inf_{\substack{H\text{ closed halfspace of }\mathbb R^n\\J\in H}}
 \sum_{I\in D\cap H}w_I,&
A&=\sum_{J\in D}w_J\tau_w(J).
\end{aligned}
\]

Then

\[
\begin{aligned}
\frac{A}{W^2}
&\ge
\frac{1}{4}\,
\frac{(11/20)^n}{|\Omega|\prod_{j=1}^q(2n_j+1)^3}\\
&\ge
\frac{1}{4}\,
\frac{(11/20)^n}{\prod_{j=1}^q(2n_j+1)^4}\\
&\ge
\frac{2^{-n}}{4(240q)^{4q}}.
\end{aligned}
\tag{1}
\]

The same normalized inequalities hold if every original weight is multiplied by the same positive constant, so an additive constant in its affine logarithm is allowed.

For \(q=1\), this applies to every nonempty union of the layers \(\{I:\sum_i I_i=K\}\), and therefore to every nonempty ternary unit-budget cut \(\{I\in\{0,1,2\}^n:\sum_i I_i\le t\}\). More generally, if a budget coefficient vector \(c\in\mathbb R^n\) is constant with value \(\gamma_j\in\mathbb R\) on each block \(\mathcal B_j\), any nonempty support specified by conditions on the block totals is covered. For example, for any set \(T\subseteq\mathbb R\), the support
\(\{I\in\{0,1,2\}^n:\sum_i c_iI_i\in T\}\), where \(c_i=\gamma_j\) for \(i\in\mathcal B_j\), is obtained by taking
\(\Omega=\{\mathbf k\in\prod_j\{0,\ldots,2n_j\}:\sum_j\gamma_jk_j\in T\}\).
Thus a budget vector with a fixed number \(q\) of distinct coefficient values gives the dimension-independent coefficient \(1/[4(240q)^{4q}]\) in (1), uniformly over those coefficient values and \(\beta\). The coefficient depends on \(q\).

## Proof

For \(I\in\{0,1,2\}^n\), write \(I^{(j)}=(I_i)_{i\in\mathcal B_j}\), using increasing coordinate order inside each block. For each profile \(\mathbf k=(k_1,\ldots,k_q)\in\Omega\), define

\[
\begin{aligned}
F_{j,k_j}
&=\left\{L\in\{0,1,2\}^{\mathcal B_j}:
               \sum_{i\in\mathcal B_j}L_i=k_j\right\},\\
D_{\mathbf k}
&=\{I\in D:I^{(j)}\in F_{j,k_j}\text{ for every }j\},\\
w^{(j)}_L&=\exp\left(-\sum_{i\in\mathcal B_j}\beta_iL_i\right),&
W_{j,k_j}&=\sum_{L\in F_{j,k_j}}w^{(j)}_L,&
p^{(j,k_j)}_L&=\frac{w^{(j)}_L}{W_{j,k_j}},\\
W_{\mathbf k}&=\sum_{I\in D_{\mathbf k}}w_I,&
p^{\mathbf k}_I&=\frac{w_I}{W_{\mathbf k}}\quad(I\in D_{\mathbf k}),&
P_{\mathbf k}&=\frac{W_{\mathbf k}}{W}.
\end{aligned}
\tag{2}
\]

Every \(F_{j,k_j}\) is nonempty: write \(k_j=2a+b\) with \(b\in\{0,1\}\), and choose \(a\) coordinates equal to two, \(b\) coordinates equal to one, and the rest zero. The inequality \(k_j\le2n_j\) ensures \(a+b\le n_j\). Hence every \(D_{\mathbf k}\) is nonempty and all normalizers in (2) are positive. The cells form a disjoint partition of \(D\), and coordinate restriction identifies \(D_{\mathbf k}\) exactly with \(\prod_{j=1}^qF_{j,k_j}\). Consequently

\[
\begin{aligned}
w_I&=\prod_{j=1}^qw^{(j)}_{I^{(j)}},&
W_{\mathbf k}&=\prod_{j=1}^qW_{j,k_j},&
p^{\mathbf k}_I&=\prod_{j=1}^qp^{(j,k_j)}_{I^{(j)}},\\
p_I&=P_{\mathbf k}p^{\mathbf k}_I\quad(I\in D_{\mathbf k}),&
\sum_{\mathbf k\in\Omega}P_{\mathbf k}&=1.
\end{aligned}
\tag{3}
\]

These identities use the original weights, without changing their tilt or discarding any source mass.

Apply accepted fact \(\texttt{d18d590c47b229bf}\) separately to every block layer. Its dimension \(n\), budget \(K\), tilt \(\beta\), and support \(F\) are here, respectively, \(n_j\), \(k_j\), \((\beta_i)_{i\in\mathcal B_j}\), and \(F_{j,k_j}\). Its \(w,W,p\) are exactly \(w^{(j)},W_{j,k_j},p^{(j,k_j)}\) from (2). Denote its entropy law, reciprocal second moment, and original average by \(\nu^{(j,k_j)}_{J^{(j)}}\), \(R_1^{(j,k_j)}(J^{(j)})\), and \(B_1^{(j,k_j)}\), so that the predecessor's \(R_1,B_1\) have the explicit aliases

\[
\begin{aligned}
R_1^{(j,k_j)}(J^{(j)})
&=\left(\sum_{L\in F_{j,k_j}}
 \frac{\nu^{(j,k_j)}_{J^{(j)}}(L)^2}{p^{(j,k_j)}_L}\right)^{-1},\\
B_1^{(j,k_j)}
&=\sum_{J^{(j)}\in F_{j,k_j}}
       p^{(j,k_j)}_{J^{(j)}}R_1^{(j,k_j)}(J^{(j)})
\ge\frac{(11/20)^{n_j}}{(2n_j+1)^3}.
\end{aligned}
\tag{4}
\]

We also use the uniform-law characterization proved in \(\texttt{d18d590c47b229bf}\). For every \(J^{(j)}\in F_{j,k_j}\), its prescribed law is uniform on

\[
\mathcal M_{j,J^{(j)}}=
\left\{L\in F_{j,k_j}:
 L_i=J_i\text{ whenever }J_i\in\{0,2\}\right\}.
\tag{5}
\]

In (5), \(J_i\) means the corresponding coordinate of \(J^{(j)}\). To see the symmetry directly, the map \(L\mapsto2J^{(j)}-L\) fixes the endpoint coordinates, maps each other coordinate \(L_i\in\{0,1,2\}\) to \(2-L_i\), and preserves the total because both \(L\) and \(J^{(j)}\) have total \(k_j\). It is thus an involution of \(\mathcal M_{j,J^{(j)}}\). Its uniform law has barycenter \(J^{(j)}\). Moreover, any law with that barycenter must fix endpoint coordinates, so it is supported on (5); the uniform law maximizes entropy on this finite set. This also verifies directly the identification with the predecessor's entropy law. The set contains \(J^{(j)}\), including when it is a singleton.

For a full original center \(J\in D_{\mathbf k}\), form the product law
\(\nu_{\mathbf k,J}(I)=\prod_{j=1}^q
\nu^{(j,k_j)}_{J^{(j)}}(I^{(j)})\) on \(D_{\mathbf k}\). Define its cell reciprocal second moment and cell average by

\[
\begin{aligned}
R_{1,\mathbf k}(J)
&=\left(\sum_{I\in D_{\mathbf k}}
       \frac{\nu_{\mathbf k,J}(I)^2}{p^{\mathbf k}_I}\right)^{-1},\\
B_{1,\mathbf k}
&=\sum_{J\in D_{\mathbf k}}p^{\mathbf k}_JR_{1,\mathbf k}(J).
\end{aligned}
\tag{6}
\]

The cell product structure and (3) give the exact factorizations

\[
\begin{aligned}
\sum_{I\in D_{\mathbf k}}\frac{\nu_{\mathbf k,J}(I)^2}{p^{\mathbf k}_I}
&=\prod_{j=1}^q
 \left(\sum_{L\in F_{j,k_j}}
 \frac{\nu^{(j,k_j)}_{J^{(j)}}(L)^2}{p^{(j,k_j)}_L}\right),\\
R_{1,\mathbf k}(J)&=\prod_{j=1}^qR_1^{(j,k_j)}(J^{(j)}),\\
B_{1,\mathbf k}&=\prod_{j=1}^qB_1^{(j,k_j)}
\ge\frac{(11/20)^n}{\prod_{j=1}^q(2n_j+1)^3}.
\end{aligned}
\tag{7}
\]

In the last equality, the sum over original centers factors with their original conditional probabilities \(p^{\mathbf k}_J\); no alternate distribution on centers is introduced.

The product law \(\nu_{\mathbf k,J}\) is invariant under \(I\mapsto2J-I\), because each factor has the symmetry just proved. This map preserves its support. Let \(H=\{x\in\mathbb R^n:a\cdot x\ge b\}\) be any closed halfspace containing \(J\). For every point \(I\) in the law's support, at least one of \(I,2J-I\) belongs to \(H\): if both had scalar product less than \(b\), their midpoint \(J\) would also have scalar product less than \(b\). It follows that \(\mathbf 1_H(I)+\mathbf 1_H(2J-I)\ge1\). Integrating and using symmetry gives \(\nu_{\mathbf k,J}(H)\ge1/2\).

Apply Cauchy-Schwarz with the positive conditional probabilities \(p^{\mathbf k}_I\). For every such \(H\),

\[
\begin{aligned}
\frac12
&\le\sum_{I\in D_{\mathbf k}\cap H}\nu_{\mathbf k,J}(I)\\
&\le
\left(\sum_{I\in D_{\mathbf k}\cap H}p^{\mathbf k}_I\right)^{1/2}
\left(\sum_{I\in D_{\mathbf k}\cap H}
       \frac{\nu_{\mathbf k,J}(I)^2}{p^{\mathbf k}_I}\right)^{1/2}\\
&\le
\left(\sum_{I\in D_{\mathbf k}\cap H}p^{\mathbf k}_I\right)^{1/2}
R_{1,\mathbf k}(J)^{-1/2}.
\end{aligned}
\tag{8}
\]

Therefore \(\sum_{I\in D_{\mathbf k}\cap H}p^{\mathbf k}_I
\ge R_{1,\mathbf k}(J)/4\). Since the full halfspace mass includes all cell mass, (8) gives

\[
\sum_{I\in D\cap H}w_I
\ge\sum_{I\in D_{\mathbf k}\cap H}w_I
=W_{\mathbf k}\sum_{I\in D_{\mathbf k}\cap H}p^{\mathbf k}_I
\ge\frac{W_{\mathbf k}}4R_{1,\mathbf k}(J).
\tag{9}
\]

Taking the infimum over all containing closed ambient halfspaces proves
\(\tau_w(J)\ge W_{\mathbf k}R_{1,\mathbf k}(J)/4\). Multiplying by the original weight of each original center and summing over the disjoint cells yields

\[
\begin{aligned}
\frac{A}{W^2}
&=\frac1{W^2}\sum_{\mathbf k\in\Omega}
                    \sum_{J\in D_{\mathbf k}}w_J\tau_w(J)\\
&\ge\frac1{4W^2}\sum_{\mathbf k\in\Omega}
            W_{\mathbf k}\sum_{J\in D_{\mathbf k}}w_JR_{1,\mathbf k}(J)\\
&=\frac14\sum_{\mathbf k\in\Omega}P_{\mathbf k}^2B_{1,\mathbf k}\\
&\ge
\frac{(11/20)^n}{4\prod_{j=1}^q(2n_j+1)^3}
\sum_{\mathbf k\in\Omega}P_{\mathbf k}^2.
\end{aligned}
\tag{10}
\]

Cauchy-Schwarz gives
\(1=(\sum_{\mathbf k\in\Omega}P_{\mathbf k})^2
\le|\Omega|\sum_{\mathbf k\in\Omega}P_{\mathbf k}^2\).
Together with \(|\Omega|\le\prod_j(2n_j+1)\), this proves the first two inequalities of (1).

For the last inequality, it remains to show
\((11/10)^n/\prod_j(2n_j+1)^4\ge(240q)^{-4q}\).
Because \(n_j\le n\), the left side is at least
\((11/10)^n/(2n+1)^{4q}\).
If \(n\ge8q\), the binomial theorem and the \(4q\) factors \(n,n-1,\ldots,n-4q+1\), each at least \(n/2\), imply

\[
\begin{aligned}
\frac{(11/10)^n}{(2n+1)^{4q}}
&\ge
\frac{\binom n{4q}\,10^{-4q}}{(3n)^{4q}}\\
&\ge
\frac{(n/2)^{4q}\,10^{-4q}}{(4q)!\,(3n)^{4q}}
=\frac1{60^{4q}(4q)!}
\ge\frac1{(240q)^{4q}}.
\end{aligned}
\tag{11}
\]

Here \(2n+1\le3n\) and \((4q)!\le(4q)^{4q}\). If \(1\le n<8q\), then \((11/10)^n\ge1\) and \(2n+1\le16q+1\le240q\), so
\((11/10)^n/(2n+1)^{4q}\ge(240q)^{-4q}\) as well. This proves (1) for all permitted dimensions.

All arguments allow \(n_j=1\), endpoint budgets, singleton block layers, singleton product laws, and arbitrary ambient orientations of the halfspace. The pairing argument retains boundary points because the halfspaces are closed. Multiplying all \(w_I\) by a positive constant multiplies \(W\) and \(\tau_w\) by that constant and \(A\) by its square, proving the affine-intercept assertion without altering (1). The stated budget applications follow from the displayed definition of their allowed profile set \(\Omega\).

## External sources

None.
