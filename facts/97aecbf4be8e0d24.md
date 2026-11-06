---
fact_id: 97aecbf4be8e0d24
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: original-mean-half-temperature-cap-comparison
depends_on: ["9f39e2160c59af72"]
verifier_run: e5f8da4017864919
target_match: null
---

## Statement

Use the seed notation \(Q,F,Z_1,Z_2\) of accepted fact `9f39e2160c59af72`. Explicitly, put

\[
\begin{aligned}
Q&=[-9,9]\times[-54,54]\times[-54,54]\subset\mathbb R^3,\\
m(y)&=\max\{6|y_1|,|y_2|,|y_3|\},\\
F(y)&=\log(5/4)m(y),\\
Z_1&=\sum_{y\in Q\cap\mathbb Z^3}e^{-F(y)},&
Z_2&=\sum_{y\in Q\cap\mathbb Z^3}e^{-2F(y)}.
\end{aligned}
\]

For each integer \(k\ge1\), set \(r=3k\), \(P=Q^k\), and \(D=P\cap\mathbb Z^r\). Write \(\mathbf I=(y^{(1)},\ldots,y^{(k)})\) in its three-coordinate blocks and define the original potential and weights by

\[
\psi_{\mathbf I}=2\sum_{i=1}^k F(y^{(i)}),\qquad
w_{\mathbf I}=e^{-\psi_{\mathbf I}}
=\left(\frac{16}{25}\right)^{\sum_{i=1}^k m(y^{(i)})}
\quad(\mathbf I\in D).
\]

Thus the potential \(\psi\) here is twice the product potential of the accepted seed. Define the quantities in the registered comparison by

\[
\begin{aligned}
W&=\sum_{\mathbf I\in D}w_{\mathbf I},\\
C_\psi(\beta)&=\inf_{\boldsymbol\theta\in\mathbb R^r}
\sum_{\mathbf I\in D}e^{-\beta\psi_{\mathbf I}+\boldsymbol\theta\cdot\mathbf I}
\qquad(\beta>0),\\
\tau_0&=\min_{\mathbf b\in\mathbb R^r\setminus\{0\}}
\sum_{\substack{\mathbf I\in D\\\mathbf b\cdot\mathbf I\ge0}}w_{\mathbf I}.
\end{aligned}
\]

For every \(k\), the support is finite and complete, \(P=\operatorname{conv}D\) has rank \(r\), \(0\in\operatorname{int}P\), the potential is the restriction of a finite convex function on \(\mathbb R^r\), and \(\psi_0=0\). The original law is exactly centered: \(\sum_{\mathbf I\in D}w_{\mathbf I}\mathbf I=0\). The following formulas and strict lower bound hold:

\[
\begin{aligned}
W&=Z_2^k,& C_\psi(1/2)&=Z_1^k,&
\tau_0&=\frac{Z_2^k+1}{2},\\
\frac{C_\psi(1/2)}{2^r\tau_0}
&=\frac{2Z_1^k}{8^k(Z_2^k+1)}
>\left(1+\frac1{2880}\right)^k.
\end{aligned}
\]

In particular, for every finite \(K>0\), every integer \(k>2880K\) gives an allowed finite original table with \(C_\psi(1/2)>K2^r\tau_0\).

## Proof

The seed inequality from accepted fact `9f39e2160c59af72` is \(Z_1/(8Z_2)>2881/2880\). We first reproduce its exact finite verification, then check the original stationarity, the capacity infimum, and every closed-cap boundary required for the present application.

The seed support is exactly
\(Q\cap\mathbb Z^3=\{-9,\ldots,9\}\times\{-54,\ldots,54\}^2\), with \(19\cdot109^2=225739\) sites. For an integer \(0\le j\le54\), the inequalities \(m(y)\le j\) are exactly \(|y_1|\le\lfloor j/6\rfloor\), \(|y_2|\le j\), and \(|y_3|\le j\). Consequently the cumulative counts and shell counts are

\[
\begin{aligned}
N_j&=(2\lfloor j/6\rfloor+1)(2j+1)^2
\qquad(0\le j\le54),\\
c_0&=1,&c_j&=N_j-N_{j-1}\qquad(1\le j\le54),\\
Z_1&=\sum_{j=0}^{54}c_j(4/5)^j,&
Z_2&=\sum_{j=0}^{54}c_j(16/25)^j.
\end{aligned}
\tag{1}
\]

These counts retain every shell, including \(j=54\), and every point of the box boundary. The exact integer identities

\[
\begin{aligned}
4\sum_{j=0}^{54}c_j4^j5^{54-j}-2881\cdot5^{54}
&=17774801494955064467736902999977976859>0,\\
90\cdot5^{108}-\sum_{j=0}^{54}c_j16^j25^{54-j}
&=6938264773648001915237683573203503262633545083165524435581609083121261609>0
\end{aligned}
\tag{2}
\]

prove \(Z_1>2881/4\) and \(Z_2<90\), respectively. The origin term gives \(Z_2\ge1\). Dividing by the positive denominators therefore yields
\(Z_1/(8Z_2)>(2881/4)/(8\cdot90)=2881/2880\).
The finite identities (2) can also be checked directly by the following integer arithmetic using precisely the coefficients in (1):

~~~python
N = [(2 * (j // 6) + 1) * (2 * j + 1)**2 for j in range(55)]
c = [1] + [N[j] - N[j - 1] for j in range(1, 55)]
A = sum(c[j] * 4**j * 5**(54 - j) for j in range(55))
B = sum(c[j] * 16**j * 25**(54 - j) for j in range(55))
assert 4*A - 2881*5**54 == 17774801494955064467736902999977976859
assert 90*5**108 - B == 6938264773648001915237683573203503262633545083165524435581609083121261609
~~~

The function \(m\) is the maximum of the six linear functions \(6y_1,-6y_1,y_2,-y_2,y_3,-y_3\). Therefore \(F\) is finite, convex, even, nonnegative, and zero at the origin. The same properties hold for the function \(2\sum_iF(y^{(i)})\) on all of \(\mathbb R^{3k}\). Its restriction \(\psi\) is convex-admissible for every barycentric relation among sites of \(D\), including relations with boundary sites, and \(\psi_0=0\).

The product \(P=Q^k\) is a full-dimensional box whose vertices are integral and lie in \(D\). Hence \(P=\operatorname{conv}D\), and its lattice support is exactly \(D=(Q\cap\mathbb Z^3)^k\). All \(225739^k\) sites have the positive weights stated above. Every coordinate interval contains zero in its interior, so \(0\in\operatorname{int}P\). If a global log-concave extension of the complete table is desired, use \(e^{-2\sum_iF(y^{(i)})}\) on \(P\) and zero outside \(P\); convexity of the potential and of \(P\) verifies log-concavity when both endpoints belong to \(P\), while the right side is zero if an endpoint does not. This extension agrees with all positive and zero lattice values.

The set \(D\) is symmetric under \(\mathbf I\mapsto-\mathbf I\), and \(\psi_{-\mathbf I}=\psi_{\mathbf I}\). Each nonzero pair has equal original weights and contributes \(w_{\mathbf I}\mathbf I+w_{-\mathbf I}(-\mathbf I)=0\) to the original first moment. The origin contributes zero. Thus \(\sum_Dw_{\mathbf I}\mathbf I=0\) exactly. No change of measure or tilt is used to obtain this original stationarity. Finite product factorization gives \(W=Z_2^k\).

To determine the capacity infimum, choose one representative from every nonzero pair \(\{\mathbf I,-\mathbf I\}\). For every \(\beta>0\) and every \(\boldsymbol\theta\in\mathbb R^r\),

\[
\begin{aligned}
\sum_{\mathbf I\in D}e^{-\beta\psi_{\mathbf I}+\boldsymbol\theta\cdot\mathbf I}
&=1+\sum_{\{\mathbf I,-\mathbf I\}}
e^{-\beta\psi_{\mathbf I}}
\left(e^{\boldsymbol\theta\cdot\mathbf I}+e^{-\boldsymbol\theta\cdot\mathbf I}\right)\\
&\ge1+2\sum_{\{\mathbf I,-\mathbf I\}}e^{-\beta\psi_{\mathbf I}}
=\sum_{\mathbf I\in D}e^{-\beta\psi_{\mathbf I}}.
\end{aligned}
\tag{3}
\]

The inequality uses \(e^a+e^{-a}\ge2\), and equality holds at \(\boldsymbol\theta=0\). Thus (3) is a lower bound valid for every tilt, and the zero tilt attains it. In particular the capacity is exactly the un-tilted sum at every temperature, and finite product factorization at \(\beta=1/2\) gives \(C_\psi(1/2)=Z_1^k\).

It remains to compute the minimum original closed-cap mass. Every closed halfspace through zero contains zero, whose weight is one. For each nonzero symmetric pair, it contains at least one point, and their weights are equal. If its boundary contains that pair, it includes both points. Therefore every nonzero normal gives cap mass at least \(1+(W-1)/2=(W+1)/2\).

This lower bound is attained by an explicit normal. Write \(\mathbf I=(I_1,\ldots,I_r)\) and set \(\mathbf b=(1,109,109^2,\ldots,109^{r-1})\). All coordinates of sites of \(D\) have absolute value at most \(54\). For a nonzero \(\mathbf I\), let \(\ell\) be its highest nonzero coordinate index. Since \(|I_\ell|\ge1\),

\[
|\mathbf b\cdot\mathbf I|
\ge109^{\ell-1}-54\sum_{j=0}^{\ell-2}109^j
=\frac{109^{\ell-1}+1}{2}>0,
\tag{4}
\]

where the empty sum for \(\ell=1\) is zero. Hence this normal has no equality atom except zero. Its closed cap contains precisely one point from each nonzero pair, together with zero, so its mass is \((W+1)/2\). This proves \(\tau_0=(Z_2^k+1)/2\) with the closed-boundary convention. If one also allows closed halfspaces merely containing zero, moving their threshold to zero gives a contained closed halfspace through zero, so the same minimum results.

Finally, \(Z_2^k\ge1\) and the strict seed inequality give

\[
\begin{aligned}
\frac{C_\psi(1/2)}{2^r\tau_0}
&=\left(\frac{Z_1}{8Z_2}\right)^k
\frac{2Z_2^k}{Z_2^k+1}\\
&\ge\left(\frac{Z_1}{8Z_2}\right)^k
>\left(1+\frac1{2880}\right)^k
\ge1+\frac{k}{2880}.
\end{aligned}
\]

The last inequality is the binomial theorem. This tends to infinity and is greater than any prescribed finite \(K>0\) when \(k>2880K\). Every member is a finite complete table satisfying the original stationarity and all the registered hypotheses. The conclusion is exactly the failure of the proposed universal temperature-to-original-cap comparison.

## External sources

None. Accepted fact `9f39e2160c59af72` supplies the exact symmetric shell seed. Its finite sum certificates are reproduced above; the original-mean condition, capacity minimization, exact closed-cap mass, and quantified implication for the registered comparison are proved directly.
