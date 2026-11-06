---
fact_id: 71c2efa2f9be09aa
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3aa-heterogeneous-ternary-potential-balanced-packing
depends_on: ["488f0a583886b5fc","793210f8a4be3647"]
verifier_run: 5c965538fa2d4e9b
target_match: null
---

## Statement

Let \(N\ge1\) be an integer, let \(T_1,\ldots,T_N\) be finite nonnegative real numbers, and let \(D=\{0,1,2\}^N\). For \(\mathbf I\in D\), set \(\epsilon_i=e^{-T_i}\), \(\phi_{\mathbf I}=\sum_{i=1}^N T_i(I_i-1)_+\), and \(w_{\mathbf I}=e^{-\phi_{\mathbf I}}\), where \(x_+=\max\{x,0\}\). Set \(w_{\mathbf I}=0\) at every lattice point outside \(D\), and let \(W=\sum_{\mathbf I\in D}w_{\mathbf I}=\prod_{i=1}^N(2+\epsilon_i)\).

Use the canonical logarithmic packing score of accepted fact `488f0a583886b5fc`, with its integer dimension \(n=N\) and no change of weight normalization. The assignment's \(B_{\log}(w)\) denotes exactly that fact's \(\mathcal B_{\log}(w)\). Explicitly, for \(\mathbf J\in D\), let \(\mathcal E_{\mathbf J}\) consist of all nonempty affinely independent \(E\subseteq D\) with \(\mathbf J\in\operatorname{relint}\operatorname{conv}E\), and let \(\lambda_{E,\mathbf I}>0\) be their unique barycentric coefficients. Define \(G_E=\sum_{\mathbf I\in E}\lambda_{E,\mathbf I}\phi_{\mathbf I}-\phi_{\mathbf J}\), and, for \(L\ge0\), define

\[
\begin{aligned}
P_{\log}(\mathbf J,L;w)
&=\max\left\{\sum_{\substack{E\in\mathcal E_{\mathbf J}\\G_E\le L}}x_E:
x_E\ge0,\quad
\sum_{\substack{E\in\mathcal E_{\mathbf J}\\G_E\le L,\ \mathbf I\in E}}x_E\le w_{\mathbf I}
\quad(\mathbf I\in D)\right\},\\
\mathcal B_{\log}(w)
&=\max_{\mathbf J\in D,\ L\ge0}\frac{P_{\log}(\mathbf J,L;w)}{1+L}.
\end{aligned}
\]

These are the full-occurrence capacity conventions of accepted fact `793210f8a4be3647`: a source occurring in a component is charged its full component mass, not its barycentric coefficient times that mass. The singleton \(\{\mathbf J\}\) is included.

The table has complete positive support \(D\), is globally extendable, and has normalized convex-admissible potential \(\phi\). At the particular center \(\mathbf J=(1,\ldots,1)\), there exists \(L\ge0\) such that

\[
\frac{P_{\log}(\mathbf J,L;w)}{1+L}
\ge \frac{e^{-2880}}2\,2^{-N}W.
\]

Consequently \(\mathcal B_{\log}(w)\ge c\,2^{-N}W\) for the absolute constant \(c=e^{-2880}/2>0\).

## Proof

First check the complete table and all convexity requirements. Finiteness of every \(T_i\) gives \(w_{\mathbf I}>0\) at every \(\mathbf I\in D\); the definition makes every other lattice weight zero. Since \(\operatorname{conv}D=[0,2]^N\), its lattice points are exactly \(D\). The function \(\Phi(x)=\sum_iT_i(x_i-1)_+\) is convex on \(\mathbb R^N\): for any nonnegative coefficients of sum one, the positive part of their weighted average is at most the weighted average of their positive parts, because that latter quantity is both nonnegative and at least the weighted average before taking positive parts. Multiplying these inequalities by \(T_i\ge0\) and adding proves convexity, including every finite barycentric inequality. In particular, if \(\mathbf J'\in D\) is any barycenter of points of \(D\), then \(\phi_{\mathbf J'}\le\sum\lambda_{\mathbf I}\phi_{\mathbf I}\).

All potentials are nonnegative and vanish on \(\{0,1\}^N\). Thus \(w_{\max}=1\), \(\min_D\phi=0\), and \(\phi_{\mathbf I}=\log(w_{\max}/w_{\mathbf I})\), exactly as in `488f0a583886b5fc`. Define \(f=e^{-\Phi}\) on \([0,2]^N\) and \(f=0\) outside that cube. It is finite valued, agrees with the entire lattice table, and is log-concave. When both endpoints lie in the cube this follows from convexity of \(\Phi\) and of the cube; otherwise the right side of the required log-concavity inequality is zero. This supplies the global extension directly. Finally, summing the product weights gives \(W=\prod_i(2+\epsilon_i)\), so \(2^{-N}W=\prod_i(1+\epsilon_i/2)\).

For each integer \(j\ge0\), let \(\mathcal I_j=\{i:j\le T_i<j+1\}\), \(m_j=|\mathcal I_j|\), and \(t_j=j+1\). These bins partition all coordinates, and only finitely many are nonempty. Declare a bin active precisely when \(m_j\ge128t_j^2e^{j/2}\), and write \(\mathcal A\) for the set of active bin indices. We will use the finite cutoff \(L=\frac12\sum_{j\in\mathcal A}t_jm_j\).

The inactive stock has an absolute bound. For an inactive bin, \(m_j<128t_j^2e^{j/2}\) and \(\epsilon_i\le e^{-j}\) for \(i\in\mathcal I_j\). Hence

\[
\sum_{j\notin\mathcal A}\sum_{i\in\mathcal I_j}\epsilon_i
\le128\sum_{j=0}^{\infty}(j+1)^2e^{-j/2}
\le128\sum_{j=0}^{\infty}(j+1)^2(2/3)^j
=5760.
\]

Here \(e^{1/2}\ge1+1/2=3/2\), which follows by integrating the inequality \(e^x\ge1\) for \(x\ge0\). The identity \(\sum_{j\ge0}(j+1)^2s^j=(1+s)/(1-s)^3\) for \(0\le s<1\) follows by differentiating the geometric series twice, and gives the value \(45\) at \(s=2/3\). The differentiations are valid inside its radius of convergence. Since \(\log(1+x)\le x\) for \(x\ge0\), by integration of \(1/(1+x)\le1\), it follows that

\[
\prod_{j\notin\mathcal A}\prod_{i\in\mathcal I_j}(1+\epsilon_i/2)\le e^{2880}.
\tag{1}
\]

Next establish the budget for each active bin. Put \(a_j=e^{-t_j/2}\) and let \(Z_j\) be the coefficient of \(\xi^0\) in the Laurent polynomial \((1+a_j(\xi+\xi^{-1}))^{m_j}\). Thus \(a_j\) means \(\exp(-(j+1)/2)\), and \(a_j^{2r}=e^{-t_jr}\). Expanding the polynomial gives

\[
Z_j=\sum_{r=0}^{\lfloor m_j/2\rfloor}
\frac{m_j!}{r!^2(m_j-2r)!}\,e^{-t_jr}.
\tag{2}
\]

The central coefficient is a largest coefficient. To prove this rather than assume it, fix \(0\le a\le1\) and write \(b_k^{(m)}\) for the coefficient of \(\xi^k\) in \((1+a(\xi+\xi^{-1}))^m\), extended by zero outside its support. The coefficients for \(m=0\) are symmetric and nonincreasing for \(k\ge0\). If this holds for \(m\), the recurrence can be written

\[
\begin{aligned}
b_k^{(m+1)}
&=(1-a)b_k^{(m)}+a(b_{k-1}^{(m)}+b_k^{(m)}+b_{k+1}^{(m)}),\\
b_k^{(m+1)}-b_{k+1}^{(m+1)}
&=(1-a)(b_k^{(m)}-b_{k+1}^{(m)})
+a(b_{k-1}^{(m)}-b_{k+2}^{(m)}).
\end{aligned}
\]

For \(k\ge1\), both differences in the second line are nonnegative. For \(k=0\), symmetry gives \(b_{-1}^{(m)}=b_1^{(m)}\ge b_2^{(m)}\), so the same is true. Symmetry is also preserved by the recurrence. This proves the assertion by induction. Apply it to \(a=a_j\le1\); the \(2m_j+1\) coefficients sum to \((1+2a_j)^{m_j}\). Therefore

\[
Z_j\ge\frac{(1+2e^{-t_j/2})^{m_j}}{2m_j+1}.
\tag{3}
\]

We claim that every active bin satisfies the stronger budget

\[
Z_j\ge\left(1+\frac{t_jm_j}{2}\right)
\prod_{i\in\mathcal I_j}(1+\epsilon_i/2).
\tag{4}
\]

For this claim put \(u_j=e^{-j/2}\in(0,1]\) and \(z_j=m_ju_j\). The active threshold gives \(z_j\ge128t_j^2\ge128\). Since \(\log2=\int_1^2 ds/s\ge1/2\), we have \(e^{-1/2}\ge1/2\). Consequently

\[
\begin{aligned}
\frac{1+2e^{-t_j/2}}{1+e^{-j}/2}
&\ge\frac{1+u_j}{1+u_j/2}
=1+\frac{u_j}{2+u_j}\ge1+\frac{u_j}{3},\\
\log\frac{1+2e^{-t_j/2}}{1+e^{-j}/2}
&\ge\frac{u_j}{3+u_j}\ge\frac{u_j}{4}.
\end{aligned}
\tag{5}
\]

The first line also uses \(u_j^2\le u_j\). The second uses \(\log(1+x)\ge x/(1+x)\) for \(x\ge0\), obtained by integrating \(1/(1+s)\ge1/(1+x)\) over \(0\le s\le x\).

We now prove that the exponential surplus in (5) pays both polynomial factors. Since \(m_j\ge1\) and \(t_jm_j\ge1\),

\[
(2m_j+1)\left(1+\frac{t_jm_j}{2}\right)
\le\frac92t_jm_j^2
=\frac92t_jz_j^2e^j.
\tag{6}
\]

For \(z\ge128\), \(\log z\le z/16\). Indeed, \(z/16-\log z\) is increasing for \(z\ge128\), since its derivative is \(1/16-1/z>0\), and its value at \(128\) is \(8-7\log2>0\), using \(\log2<1\). Thus \(2\log z_j\le z_j/8\). Also \(\log t_j\le t_j-1=j\), by integrating \(1/s\le1\) from \(1\) to \(t_j\), and \(\log(9/2)<2\), since \(e^2\ge1+2+2=5>9/2\). The latter lower bound follows from the first three terms of the exponential power series. It follows that

\[
\log\bigl((9/2)t_jz_j^2e^j\bigr)
\le \frac{z_j}{8}+2t_j
\le\frac{z_j}{4},
\tag{7}
\]

where the last step uses \(z_j/8\ge16t_j^2\ge2t_j\). Combining (5)-(7) gives

\[
\left(\frac{1+2e^{-t_j/2}}{1+e^{-j}/2}\right)^{m_j}
\ge e^{z_j/4}
\ge(2m_j+1)\left(1+\frac{t_jm_j}{2}\right).
\]

Apply (3), and then use \(\epsilon_i\le e^{-j}\) on the bin. This yields
\(Z_j\ge(1+t_jm_j/2)(1+e^{-j}/2)^{m_j}\ge(1+t_jm_j/2)\prod_{i\in\mathcal I_j}(1+\epsilon_i/2)\), proving (4).

It remains to construct the globally feasible packing without multiplying component arities or undercharging any source. Let \(\mathcal V\subseteq\{-1,0,1\}^N\) consist of the displacements that are zero on all inactive-bin coordinates and have equally many \(+1\) and \(-1\) coordinates within each active bin. For \(\mathbf v\in\mathcal V\), let \(r_j(\mathbf v)\) be this common sign count in bin \(j\in\mathcal A\). The set \(\mathcal V\) contains zero and is closed under \(\mathbf v\mapsto-\mathbf v\). Formula (2) and independent choices across bins give the exact finite identity

\[
\sum_{\mathbf v\in\mathcal V}
\exp\left(-\sum_{j\in\mathcal A}t_jr_j(\mathbf v)\right)
=\prod_{j\in\mathcal A}Z_j.
\tag{8}
\]

The empty product is one, so this remains valid when there is no active bin.

For each nonzero \(\mathbf v\in\mathcal V\) whose first nonzero coordinate is \(+1\), use the support \(E_{\mathbf v}=\{\mathbf J+\mathbf v,\mathbf J-\mathbf v\}\) with coefficients \(1/2,1/2\), and assign it mass
\(x_{E_{\mathbf v}}=\exp(-\sum_{j\in\mathcal A}t_jr_j(\mathbf v))\).
Also assign \(x_{\{\mathbf J\}}=1\), and assign zero to every other support. Each nonzero reflected support is affinely independent and has \(\mathbf J\) in its relative interior, so it belongs to \(\mathcal E_{\mathbf J}\). Both endpoints lie in the complete support \(D\). Their exact weights and their logarithmic gap are

\[
\begin{aligned}
w_{\mathbf J+\mathbf v}
&=\exp\left(-\sum_{i:v_i=1}T_i\right),
&w_{\mathbf J-\mathbf v}
&=\exp\left(-\sum_{i:v_i=-1}T_i\right),\\
G_{E_{\mathbf v}}
&=\frac12\sum_iT_i|v_i|
\le\sum_{j\in\mathcal A}t_jr_j(\mathbf v)
\le L.
\end{aligned}
\tag{9}
\]

Indeed, each sign has \(r_j(\mathbf v)\) coordinates in bin \(j\), and every such \(T_i<t_j\). It follows that each endpoint weight is at least \(x_{E_{\mathbf v}}\). Distinct chosen supports are disjoint: an equality between two endpoints forces their displacement vectors to be equal or opposite, and the representative rule selects just one of these two orientations. None of these endpoints is \(\mathbf J\). Therefore each endpoint is charged the full \(x_{E_{\mathbf v}}\) exactly once; \(\mathbf J\) is charged its singleton mass \(1=w_{\mathbf J}\); every other original source is charged zero. This proves all shared capacity inequalities under the full-occurrence conventions of `793210f8a4be3647`. The singleton has gap zero, and (9) verifies the cutoff for every other positive variable. We have constructed a feasible packing for the canonical program of `488f0a583886b5fc`, not a packing on a renormalized subtable.

Write \(M\) for its total component mass, consistently with `793210f8a4be3647`. The summand in (8) is invariant under changing orientation, and its value at zero is one. Hence

\[
M=\frac{1+\prod_{j\in\mathcal A}Z_j}{2}
\ge\frac12\prod_{j\in\mathcal A}Z_j.
\tag{10}
\]

For finitely many nonnegative numbers, expanding their product shows \(\prod_j(1+b_j)\ge1+\sum_jb_j\). Apply this with \(b_j=t_jm_j/2\) and use (4). Together with (10), this proves

\[
\begin{aligned}
P_{\log}(\mathbf J,L;w)
&\ge M
\ge\frac{1+L}{2}
\prod_{j\in\mathcal A}\prod_{i\in\mathcal I_j}(1+\epsilon_i/2),\\
\frac{P_{\log}(\mathbf J,L;w)}{1+L}
&\ge\frac12
\prod_{j\in\mathcal A}\prod_{i\in\mathcal I_j}(1+\epsilon_i/2)
\ge\frac{e^{-2880}}2\prod_{i=1}^N(1+\epsilon_i/2)
=\frac{e^{-2880}}2\,2^{-N}W.
\end{aligned}
\]

The second inequality in the last line is exactly the inactive-stock estimate (1). Empty active sets and zero penalties have already been included throughout. The maximum defining \(\mathcal B_{\log}(w)\) is at least the value at this one center and cutoff, completing the proof.

## External sources

None. All bin estimates, coefficient bounds, complete-support and convex-admissibility checks, and full-capacity packing assertions are proved above. The two declared accepted predecessors are used only for the canonical score definitions and capacity conventions.
