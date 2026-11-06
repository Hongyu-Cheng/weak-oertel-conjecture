---
fact_id: 6ca311257acdfbcb
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: parity-compressed-row-fractional-capacity
depends_on: ["488f0a583886b5fc","5d0f9e78ced711d6"]
verifier_run: 7e794ef0f7f44957
target_match: null
---

## Statement

Retain the canonical notation and full-occurrence convention of accepted fact `488f0a583886b5fc`. For an actual convex body \(C\subset\mathbb R^n\times\mathbb R^d\), write \(C_{\mathbf I}=\{\mathbf y:(\mathbf I,\mathbf y)\in C\}\), \(w_{\mathbf I}=\mathcal L^d(C_{\mathbf I})\), \(D=\{\mathbf I\in\mathbb Z^n:w_{\mathbf I}>0\}\), \(W=\sum_Dw_{\mathbf I}>0\), and \(T=W/2^n\). Put \(w_{\max}=\max_Dw_{\mathbf I}\) and \(\phi_{\mathbf I}=\log(w_{\max}/w_{\mathbf I})\). A finite positive barycentric component with target \(\mathbf J\), support \(E\), and coefficients \(\lambda_{\mathbf I}\) has logarithmic cost

\[
G=\sum_{\mathbf I\in E}\lambda_{\mathbf I}\phi_{\mathbf I}-\phi_{\mathbf J},
\qquad
\sum_{\mathbf I\in E}\lambda_{\mathbf I}=1,
\qquad
\sum_{\mathbf I\in E}\lambda_{\mathbf I}\mathbf I=\mathbf J.
\tag{1}
\]

Let \(p=w/W\), and use exactly the arrays of accepted fact `5d0f9e78ced711d6`: \(r_{\mathbf J,\mathbf I}\ge0\), with both indices in \(D\), column sums \(p_{\mathbf I}\), and row identities \(\sum_{\mathbf I}r_{\mathbf J,\mathbf I}(\mathbf I-\mathbf J)=\mathbf0\). Write \(q_{\mathbf J}=\sum_{\mathbf I}r_{\mathbf J,\mathbf I}\). Minimize \(\sum_{\mathbf J}q_{\mathbf J}\|\mathbf J\|^2\) over these arrays.

For comparison with the full score \(\mathcal B_{\log}(w)\), define \(\mathcal R_{\log}(r;w)\) as follows. Choose a positive row \(\mathbf J\), a cutoff \(L\ge0\), and any finite collection of components (1) at \(\mathbf J\), with masses \(x_k\ge0\) and costs at most \(L\) whenever \(x_k>0\). Require the full occurrence constraints

\[
\sum_{k:\mathbf I\in E_k}x_k\le W r_{\mathbf J,\mathbf I}
\quad(\mathbf I\in D).
\tag{2}
\]

The score \(\mathcal R_{\log}(r;w)\) is the supremum of \(\sum_kx_k/(1+L)\) over these choices. Supports and coefficients are unrestricted, and the singleton at \(\mathbf J\) is included. Thus (2) replaces the original capacity \(w_{\mathbf I}\) by the amount assigned to this particular row; it does not discount any occurrence by its barycentric coefficient. The costs in (1) continue to use the original actual table \(w\).

For each integer \(n\ge4\), let \(s_n>e\) be the unique solution of \(s_n(\log s_n-1)=n-2\). There are an integer \(d\ge1\), an actual compact convex body \(C\subset\mathbb R^n\times\mathbb R^d\), and an explicit minimizing array \(r\) such that

\[
\begin{aligned}
\{\mathbf J:q_{\mathbf J}>0\}&=\{0,1\}^n,\\
n+2\le T&\le n+s_n+3,\\
\mathcal R_{\log}(r;w)&\le s_n+3,\\
\frac{\mathcal R_{\log}(r;w)}{T}
&\le\frac{s_n+3}{n+2}\longrightarrow0,\\
\frac{\mathcal B_{\log}(w)}{T}
&\ge\frac{n+1}{n+s_n+3}\longrightarrow1.
\end{aligned}
\tag{3}
\]

The final line asserts a lower bound whose right side tends to one; it does not assert convergence of the full score itself. More precisely, the total mass obtainable at a positive row using (2), when no cost restriction is imposed, is exactly \(2+\zeta_{\mathbf J}\), where the explicit nonnegative excesses below satisfy \(0\le\zeta_{\mathbf J}\le s_n+1\). That row's assigned total source mass is \(Wq_{\mathbf J}=n+2+\zeta_{\mathbf J}\). Every minimum-second-moment array for this table has its positive rows contained in \(\{0,1\}^n\); the upper bound for \(\mathcal R_{\log}\) is proved for the explicit array, not for every allocation on those possible row targets.

## Proof

We construct the complete support first. Use the simplex and its associated set with exactly the meanings of \(P_r,A_r\) in accepted fact `5d0f9e78ced711d6`, here with \(r=n\):

\[
P_n=\operatorname{conv}\{\mathbf e_1,\ldots,\mathbf e_n,-\mathbf1\},
\qquad
A_n=\{\mathbf0,\mathbf e_1,\ldots,\mathbf e_n,-\mathbf1\}.
\]

Let \(\mathcal Q=\{0,1\}^n\), let \(P=P_n+[0,1]^n\), and set \(D=A_n+\mathcal Q\). Here the sum defining \(D\) is a set of distinct physical lattice sites, and multiplicities will be recorded separately. The notation \(P\) agrees with \(\operatorname{conv}D\) in accepted fact `488f0a583886b5fc`.

We verify \(P\cap\mathbb Z^n=D\) without omitting any lattice points. Every coordinate of a point of \(P\) lies between \(-1\) and \(2\). If an integer point \(\mathbf I=\mathbf x+\mathbf y\), with \(\mathbf x\in P_n\) and \(\mathbf y\in[0,1]^n\), has \(I_i=-1\), then \(x_i=-1\). The only vertex of \(P_n\) attaining that coordinate minimum is \(-\mathbf1\), so \(\mathbf x=-\mathbf1\). Thus \(\mathbf I\in\{-1,0\}^n\). If it has \(I_i=2\), then \(x_i=1\), whose unique maximizing vertex is \(\mathbf e_i\). Consequently this is its only coordinate equal to two, and all the other coordinates belong to \(\{0,1\}\). If neither event occurs, the point belongs to \(\mathcal Q\). Conversely all the following sites are in \(A_n+\mathcal Q\), and hence in \(P\):

\[
\begin{aligned}
&\mathcal Q,\\
&\{-1,0\}^n\setminus\{\mathbf0\},\\
&\{\mathbf I:I_i=2\text{ for exactly one }i,
\ I_j\in\{0,1\}\text{ for }j\ne i\}.
\end{aligned}
\tag{4}
\]

These are disjoint and exhaust the lattice intersection. The cube and the simplex are convex hulls of their vertices, so distributing convex combinations also proves \(P=\operatorname{conv}(A_n+\mathcal Q)=\operatorname{conv}D\).

For each \(\mathbf I\in D\), define the positive integer multiplicity
\(m_{\mathbf I}=|\{\mathbf J\in\mathcal Q:\mathbf I\in\mathbf J+A_n\}|\).
Direct counting gives

\[
m_{\mathbf I}=
\begin{cases}
2,&\mathbf I=\mathbf0,\\
k+1,&\mathbf I\in\mathcal Q,\quad k=\sum_i I_i\ge1,\\
1,&\mathbf I\in D\setminus\mathcal Q.
\end{cases}
\qquad
\sum_{\mathbf I\in D}m_{\mathbf I}=(n+2)2^n.
\tag{5}
\]

Indeed, a nonzero binary site is obtained from the central element of \(A_n\), or by subtracting \(\mathbf e_i\) from it at one of its coordinates equal to one. At zero there are the central representation and \(\mathbf0=\mathbf1-\mathbf1\). Every site in the second or third line of (4) has exactly one representation. The total in (5) also follows by counting the \(n+2\) distinct sources in each of the \(2^n\) translated sets \(\mathbf J+A_n\).

The table \(m\) itself is not asserted to be convex-admissible. We repair it explicitly before constructing the actual body. Put \(b_n=\log(n+1)\), and on \(P\) define the auxiliary concave roof

\[
\psi(\mathbf x)=
\max\left\{
\sum_{\mathbf I\in D}\lambda_{\mathbf I}\log m_{\mathbf I}:
\lambda_{\mathbf I}\ge0,\quad
\sum_{\mathbf I}\lambda_{\mathbf I}=1,\quad
\sum_{\mathbf I}\lambda_{\mathbf I}\mathbf I=\mathbf x
\right\}.
\tag{6}
\]

The feasible set is nonempty and compact, so the maximum exists. Combining coefficient vectors proves concavity. Also \(0\le\psi\le b_n\), and \(\psi(\mathbf I)\ge\log m_{\mathbf I}\). Upper semicontinuity follows directly: along a convergent sequence of base points, take maximizing coefficient vectors and a convergent subsequence of them. Their limit represents the limiting base point and bounds the upper limit of the objectives by (6). No numerical linear-programming assertion is used.

At every \(\mathbf I\in D\setminus\mathcal Q\), one has \(\psi(\mathbf I)=0\). Such a point either has a coordinate \(-1\) or a coordinate \(2\). In any barycentric representation of that point from \(D\), all sources with positive coefficient have the same extreme coordinate. By (4)-(5) all those sources have multiplicity one, so every objective in (6) is zero. At \(\mathbf1\), one has \(\psi(\mathbf1)=b_n\), since \(m_{\mathbf1}=n+1\) and this is the largest multiplicity.

We need a bound on how much this repair can increase a binary site. For \(\mathbf J\in\mathcal Q\), put \(k=\sum_iJ_i\). We claim

\[
e^{\psi(\mathbf J)}\le\max\{k+2,s_n\},
\qquad
0\le e^{\psi(\mathbf J)}-m_{\mathbf J}\le s_n.
\tag{7}
\]

Consider any coefficient vector in (6) at \(\mathbf J\). Let \(t\) be its total coefficient on \(\mathcal Q\), and let \(a\) be its total coefficient on \(\{-1,0\}^n\setminus\{\mathbf0\}\). The other sources have nonnegative coordinate sum. Taking coordinate sums in its barycentric identity therefore gives

\[
\sum_{\mathbf I\in\mathcal Q}\lambda_{\mathbf I}\sum_i I_i
\le k+na\le k+n(1-t).
\tag{8}
\]

The objective receives zero contribution from sites outside \(\mathcal Q\). On \(\mathcal Q\), (5) gives \(m_{\mathbf I}\le\sum_i I_i+2\). If \(t>0\), concavity of the logarithm and (8) consequently bound the objective by

\[
H_k(t)=t\log\left(\frac{n+k}{t}-n+2\right),
\qquad 0<t\le1.
\tag{9}
\]

If \(t=0\), the objective is zero, so it cannot violate (7). To maximize (9), put \(u=(n+k)/t-n+2\), so \(u\ge k+2\), and write
\(H_k(t)=(n+k)\log u/(u+n-2)\).
The derivative of \(\log u/(u+n-2)\) has the sign of \(1+(n-2)/u-\log u\). This expression is strictly decreasing for \(u>0\) and vanishes at \(u=s_n\). If \(k+2\ge s_n\), the maximum on \(u\ge k+2\) occurs at \(k+2\), giving \(H_k(t)\le\log(k+2)\). If \(k+2<s_n\), its maximum occurs at \(s_n\), where

\[
H_k(t)\le
\frac{(n+k)\log s_n}{s_n+n-2}
=\frac{n+k}{s_n}
\le\frac{n+s_n-2}{s_n}
=\log s_n.
\tag{10}
\]

Here both equalities use \(s_n(\log s_n-1)=n-2\). This proves the first part of (7). Its second part follows from (5), the lower bound \(\psi(\mathbf J)\ge\log m_{\mathbf J}\), and \(s_n>e>2\): at a nonzero binary site the possible increase is at most \(\max\{1,s_n-(k+1)\}\le s_n\), and at zero it is at most \(s_n-2\).

Choose any integer \(d>b_n+(n+1)b_n^2\), and define an actual body in the original integer dimension by

\[
C=\left\{(\mathbf x,\mathbf y):
\mathbf x\in P,\quad
0\le y_i\le1+\frac{\psi(\mathbf x)}{d-b_n}
\quad(1\le i\le d)\right\}.
\tag{11}
\]

Its upper fiber side length is positive and concave. Thus \(C\) is convex. It is bounded, and upper semicontinuity of \(\psi\) makes it closed, so it is compact. The set \(P\) has nonempty interior, and \(\operatorname{int}(P)\times(0,1)^d\subset C\), proving full dimension. Every fiber above \(P\) has positive volume, and every fiber outside \(P\) is empty. Consequently (4) is its complete positive integer support, and its actual weights are exactly

\[
w_{\mathbf I}=\left(1+\frac{\psi(\mathbf I)}{d-b_n}\right)^d
\quad(\mathbf I\in D),
\qquad
w_{\mathbf I}=0\quad(\mathbf I\notin D).
\tag{12}
\]

In particular \(w_{\mathbf I}=1\) on \(D\setminus\mathcal Q\). This is a direct construction of actual volume weights, not an assertion that the multiplicity table was already admissible. The auxiliary roof \(\psi\) is not the negative of the final canonical potential. Their exact relation is

\[
\phi_{\mathbf I}
=d\log\frac d{d-b_n}
-d\log\left(1+\frac{\psi(\mathbf I)}{d-b_n}\right).
\tag{13}
\]

This potential is fully convex-admissible. Indeed, concavity of the side length in (11), followed by the weighted arithmetic-geometric mean inequality, gives \(\log w_{\mathbf J}\ge\sum_{\mathbf I}\lambda_{\mathbf I}\log w_{\mathbf I}\) for every finite positive barycentric representation. Thus every cost (1) is nonnegative, and all hypotheses of the original logarithmic score in accepted fact `488f0a583886b5fc` hold on the complete support.

The passage to actual volumes increases \(e^{\psi}\) by at most one at every site. For \(0\le h\le b_n\), differentiation gives

\[
\begin{aligned}
0\le d\log\left(1+\frac h{d-b_n}\right)-h
&\le\varepsilon,\\
\varepsilon=d\log\frac d{d-b_n}-b_n
&=\int_0^{b_n}\frac{s}{d-s}\,ds
\le\frac{b_n^2}{2(d-b_n)}
<\frac1{2(n+1)}.
\end{aligned}
\tag{14}
\]

For the first line, the left expression is zero at \(h=0\), its derivative is \((b_n-h)/(d-b_n+h)\ge0\), and its endpoint value at \(b_n\) is \(\varepsilon\). The elementary bound \(e^x\le1/(1-x)\) for \(0\le x<1\) implies \(e^{\varepsilon}-1<1/(n+1)\). Since \(e^{\psi}\le n+1\), (12)-(14) give

\[
e^{\psi(\mathbf I)}\le w_{\mathbf I}\le e^{\psi(\mathbf I)}+1,
\qquad
n+1\le w_{\max}=w_{\mathbf1}\le n+2.
\tag{15}
\]

Define \(\zeta_{\mathbf J}=w_{\mathbf J}-m_{\mathbf J}\) for \(\mathbf J\in\mathcal Q\). Equations (7) and (15) prove
\(0\le\zeta_{\mathbf J}\le s_n+1\).
There is no excess outside \(\mathcal Q\). Thus

\[
W=(n+2)2^n+\sum_{\mathbf J\in\mathcal Q}\zeta_{\mathbf J},
\qquad
n+2\le T\le n+s_n+3.
\tag{16}
\]

We now give the whole row array. For \(\mathbf J\in\mathcal Q\) and \(\mathbf I\in D\), set

\[
W r_{\mathbf J,\mathbf I}
=\mathbf1_{\{\mathbf I\in\mathbf J+A_n\}}
+\zeta_{\mathbf J}\mathbf1_{\{\mathbf I=\mathbf J\}},
\tag{17}
\]

and set all rows indexed by \(D\setminus\mathcal Q\) to zero. Formula (5), together with the exact excess definition, proves that the column sum of (17) is \(w_{\mathbf I}\), so the normalized column sums are precisely \(p\). The elements of \(A_n\) sum to zero. Therefore every row has mean \(\mathbf J\), and
\(Wq_{\mathbf J}=n+2+\zeta_{\mathbf J}>0\)
for every \(\mathbf J\in\mathcal Q\). This verifies all constraints of the accepted minimum-second-moment problem simultaneously.

It is a global minimizer, not merely an array with different row parities. For every integer vector \(\mathbf J\), coordinatewise integrality gives
\(\|\mathbf J\|^2\ge\sum_i J_i\), with equality exactly on \(\mathcal Q\), because \(j^2-j=j(j-1)\ge0\) for every integer \(j\). Every feasible array has the same mean, by its column sums and row identities. Consequently its objective satisfies

\[
\sum_{\mathbf J}q_{\mathbf J}\|\mathbf J\|^2
\ge\sum_{\mathbf J}q_{\mathbf J}\sum_iJ_i
=\sum_{\mathbf I}p_{\mathbf I}\sum_iI_i.
\tag{18}
\]

The array (17) attains equality because all its positive rows lie in \(\mathcal Q\). Moreover, equality in (18) for any minimizer forces every positive row to lie in \(\mathcal Q\). This last observation restricts possible row targets only; it does not force the allocation (17).

Fix any one of the \(2^n\) positive rows of (17). Its assigned capacities are one at each of the \(n+1\) noncentral sites \(\mathbf J+\mathbf e_i\), \(\mathbf J-\mathbf1\), are \(1+\zeta_{\mathbf J}\) at \(\mathbf J\), and are zero elsewhere. A positive-mass component satisfying (2) must therefore use a subset of these sites. Translate its barycentric identity by \(-\mathbf J\). If \(a_i\) is its coefficient at \(\mathbf e_i\) and \(a_-\) its coefficient at \(-\mathbf1\), with missing coefficients set to zero, the coordinate equations give \(a_i=a_-\) for all \(i\). Thus a component is either the central singleton or contains all \(n+1\) noncentral sites. It may also contain the central site, and no restriction on its original arity or coefficients has been imposed.

Every component of the second kind charges each of those noncentral sources its entire mass. The capacity one at, for example, \(\mathbf J+\mathbf e_1\) therefore bounds the combined mass of all second-kind components by one. The combined mass of central-singleton components is at most \(1+\zeta_{\mathbf J}\). This remains a valid upper bound if other components also use the central source. Hence every finite scheme at this row, even without a cost restriction, has

\[
\sum_kx_k\le2+\zeta_{\mathbf J}\le s_n+3.
\tag{19}
\]

The unrestricted mass bound is attained: take the central singleton with mass \(1+\zeta_{\mathbf J}\), and one component on all \(n+1\) noncentral vertices with mass one and coefficients \(1/(n+1)\). They have disjoint supports and the required barycenters, and they use exactly all the assigned capacities. Both logarithmic costs are finite and nonnegative. In particular some finite cutoff admits this scheme. Since \(1+L\ge1\), (19) bounds every row and every cutoff in the definition of \(\mathcal R_{\log}\), proving its bound in (3).

Finally, return to the original full capacities \(w_{\mathbf I}\). At the allowed target \(\mathbf1\), the central singleton of mass \(w_{\mathbf1}=w_{\max}\) has cost zero. It is feasible for the full logarithmic program of accepted fact `488f0a583886b5fc`. Thus \(\mathcal B_{\log}(w)\ge w_{\max}\ge n+1\), and (16) proves its lower comparison in (3). This explicitly checks the unrestricted target scale rather than inferring a failure of the full score from (19).

The scalar \(s_n\) is well defined because \(s\mapsto s(\log s-1)\) increases continuously from zero to infinity on \((e,\infty)\). It satisfies \(s_n\to\infty\) and
\(s_n/n=(1-2/n)/(\log s_n-1)\to0\).
This proves both limiting right sides in (3). In particular, for every proposed absolute \(c>0\), all sufficiently large members of this exact family satisfy \(\mathcal R_{\log}(r;w)<cW/2^n\), simultaneously across the complete collection of positive rows in (17). The construction makes no claim about \(\sup_r\mathcal R_{\log}(r;w)\) over alternative minimizing arrays. Recovering even the displayed singleton from the row allocations requires using its capacity portions assigned to different rows, which (2) deliberately excludes.

## External sources

None. Accepted fact `488f0a583886b5fc` supplies the canonical full logarithmic program and its unrestricted-support convention. Accepted fact `5d0f9e78ced711d6` supplies the exact row minimization problem and the meanings of \(P_n,A_n\). The complete support, repaired potential, actual body, minimizing array, every assigned source capacity, every packing upper bound, and both target-scale comparisons are proved directly above. No computer-assisted premise, solver certificate, integral-cover rounding, or tensor-capacity inference is used.
