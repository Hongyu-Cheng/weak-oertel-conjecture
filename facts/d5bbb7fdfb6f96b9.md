---
fact_id: d5bbb7fdfb6f96b9
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct22-fixed-budget-midpoint-cascade
depends_on: []
verifier_run: df48388577d24f94
target_match: null
---

## Statement

Let \(k\ge0\) and \(r\ge1\) be integers, set \(N=k+1\) and \(Q=2^k\), and define the integer quadratic budget on the integer lattice by
$$
\rho(x)=\sum_{a=1}^k\frac{x_a(x_a-1)}2\qquad(x\in\mathbb Z^k).
\tag{1}
$$
Let D be a finite nonempty subset of \(\mathbb Z^k\) satisfying
$$
D=\operatorname{conv}(D)\cap\mathbb Z^k,
\qquad \rho(x)\le r\quad(x\in D).
\tag{2}
$$
Put \(A=D\times\lbrace0\rbrace\subseteq\mathbb R^N\). For any \(\beta\in\mathbb R^k\), use the original affine probability law
$$
w_x=\exp(-\beta\cdot x),\qquad
Z=\sum_{x\in D}w_x,\qquad
p_{(x,0)}=p_x=\frac{w_x}{Z}.
\tag{3}
$$
An additive constant in the affine field cancels upon normalization, so (3) includes all real affine fields. Define exactly the original closed-halfspace and ordered-reflection quantities
$$
\begin{aligned}
\tau_p(z)&=\inf_{\substack{H\subseteq\mathbb R^N\text{ a closed affine halfspace}\\z\in H}}
\sum_{u\in A\cap H}p_u,
&M_3(p)&=\sum_{z\in A}p_z\tau_p(z)^3,\\
s_p(c)&=\sum_{\substack{x,y\in D\\x+y=2c}}\min(p_x,p_y),
&T(p)&=\sum_{c\in D}p_cs_p(c)^3.
\end{aligned}
\tag{4}
$$
The reflection sum is ordered and includes the diagonal once. The halfspaces may be required to have nonzero normals. Then, with
$$
c_r=2^{-40}3^{-5(r+1)}>0,
\tag{5}
$$
both original cubics satisfy
$$
M_3(p)\ge c_r8^{-N},\qquad T(p)\ge c_r8^{-N}.
\tag{6}
$$
In particular, (6) holds for every finite nonempty complete \(D\subseteq\lbrace0,1,2\rbrace^k\) with at most r coordinates equal to two at each point, because on this alphabet \(\rho(x)=\#\lbrace a:x_a=2\rbrace\). No Boolean point is assumed to belong to D, no affine-rank condition is imposed, and no relation between r and k is required.

## Proof

For every integer v, the number \(v(v-1)/2\) is a nonnegative integer, and it is zero exactly when \(v\in\lbrace0,1\rbrace\). Consequently, \(\rho\) is a nonnegative integer on \(\mathbb Z^k\), and its zero set is the Boolean cube \(\lbrace0,1\rbrace^k\), of cardinality Q.

Completeness in (2) implies that every integral midpoint \(c=(x+y)/2\) of two points of D belongs to D. The affine law (3) gives
$$
p_c^2=p_xp_y.
\tag{7}
$$
Moreover, the quadratic identity
$$
\rho\left(\frac{x+y}{2}\right)
=\frac{\rho(x)+\rho(y)}2-\frac{\lVert x-y\rVert^2}{8}
\tag{8}
$$
holds for all real x,y. Suppose x,y are distinct integer points with the same coordinatewise parity and with \(\rho(x),\rho(y)\le s\), where s is an integer. Their difference is a nonzero even integer vector, so \(\lVert x-y\rVert^2\ge4\). Their midpoint is integral, and (8) gives \(\rho(c)\le s-1/2\). Integrality of \(\rho(c)\) therefore implies
$$
\rho(c)\le s-1.
\tag{9}
$$
This is the budget drop that will bound the number of midpoint generations. It applies without a ternary-coordinate restriction.

We first establish the geometric bounds that will be used at each generation. For a fixed center c, distinct unordered reflected pairs \(\lbrace x,y\rbrace\), with \(x\ne y\) and \(x+y=2c\), have disjoint endpoints, because the partner of x is uniquely \(2c-x\). None of these endpoints equals c. Every closed affine halfspace containing \((c,0)\) contains an endpoint of each pair: if \(H=\lbrace u:v\cdot u\ge a\rbrace\) excluded both endpoints, it would also exclude their midpoint. The center itself belongs to H. Hence, if R(c) sums \(\min(p_x,p_y)\) over any collection of such distinct reflected pairs counted in both orders, then
$$
\tau_p((c,0))\ge p_c+\frac12R(c),\qquad s_p(c)\ge R(c).
\tag{10}
$$
This argument covers arbitrary affine rank and all containing closed halfspaces. It still applies when normals are required to be nonzero; such containing halfspaces exist, for instance \(\lbrace u:u_N\ge0\rbrace\).

In particular, the center mass and the reflection diagonal give
$$
M_3(p)\ge S_4,\qquad T(p)\ge S_4,
\qquad S_4=\sum_{x\in D}p_x^4.
\tag{11}
$$
If \(k=0\), D consists of the unique point of \(\mathbb Z^0\), its probability is one, and both moments in (4) equal one. This proves (6) in that case. The following argument also uses no requirement that \(r\le k\).

For t>0, use the entire original probability band and its two restricted moments:
$$
\begin{aligned}
\mathcal V_t&=\lbrace x\in D:t/2<p_x\le t\rbrace,\\
\mathcal M(t)&=\sum_{c\in\mathcal V_t}p_c\tau_p((c,0))^3,
&\mathcal T(t)&=\sum_{c\in\mathcal V_t}p_cs_p(c)^3.
\end{aligned}
\tag{12}
$$
For any actual subset \(W\subseteq\mathcal V_t\) of cardinality \(n\ge2Q\), let its deduplicated actual same-parity midpoint image be
$$
I(W)=\left\lbrace\frac{x+y}{2}:x,y\in W,\ x\ne y,\ x\equiv y\pmod2\right\rbrace,
\qquad b=|I(W)|.
\tag{13}
$$
There are Q parity classes. If \(n_e\) is the number of points of W in parity class e, the number v of ordered distinct same-parity endpoint pairs is
$$
v=\sum_e n_e(n_e-1)
\ge\frac{n^2}{Q}-n
\ge\frac{n^2}{2Q}>0.
\tag{14}
$$
The first inequality is Cauchy's inequality, and the second uses \(n\ge2Q\). In particular, \(b>0\). Every point of \(I(W)\) belongs to D by completeness and remains in the same original band by (7): the geometric mean of two numbers in \((t/2,t]\) is again in \((t/2,t]\). Thus
$$
I(W)\subseteq\mathcal V_t.
\tag{15}
$$

For \(c\in I(W)\), let \(a_c\) count the ordered distinct same-parity pairs in W whose midpoint is c. Let \(R_W(c)\) sum \(\min(p_x,p_y)\) over these pairs. Then
$$
\sum_{c\in I(W)}a_c=v,\qquad
R_W(c)\ge\frac t2a_c,\qquad
\sum_{c\in I(W)}a_c^3\ge\frac{v^3}{b^2}.
\tag{16}
$$
The last inequality is Hölder's inequality. Applying (10) at these centers inside the full band (12) yields the common estimate
$$
\begin{aligned}
\min(\mathcal M(t),\mathcal T(t))
&\ge\frac18\sum_{c\in I(W)}p_cR_W(c)^3\\
&\ge\frac{t^4}{128}\sum_{c\in I(W)}a_c^3
\ge\frac{t^4v^3}{128b^2}
\ge\frac{2^{-10}t^4n^6}{Q^3b^2}.
\end{aligned}
\tag{17}
$$
For the reflection moment the first inequality can omit the factor 1/8, so the stated common estimate is valid. This count has been proved under (2) directly, without using a theorem restricted to any particular budget.

We now deduce a local estimate for the full band whenever \(n_0=|\mathcal V_t|\ge2Q\). Start with \(W_0=\mathcal V_t\), and whenever \(n_i=|W_i|\ge2Q\), define \(W_{i+1}=I(W_i)\). Equations (14) and (15) imply that the next set is nonempty and stays in \(\mathcal V_t\). By (9), every defined \(W_i\) has budget at most r-i. If the construction has not stopped before generation r, then \(W_r\) consists of Boolean points, so \(n_r\le Q<2Q\). Thus the first stopping index
$$
L=\min\lbrace i\ge1:n_i<2Q\rbrace
\tag{18}
$$
exists and satisfies \(1\le L\le r\). Every \(n_i\) for \(0\le i\le L\) is positive, and \(n_i\ge2Q\) for i<L.

Put \(u_i=n_i/Q\), and take the largest generation ratio
$$
h=\max_{0\le i<L}\frac{u_i^6}{u_{i+1}^2}>0.
\tag{19}
$$
Applying (17) to each \(W_i\) gives a bound for the same two full-band restricted moments. Taking a maximum, rather than adding these bounds, gives
$$
\min(\mathcal M(t),\mathcal T(t))\ge2^{-10}t^4Qh.
\tag{20}
$$
In particular, overlap between any of the generation sets causes no multiple counting in (20). From (19),
$$
u_{i+1}\ge u_i^3h^{-1/2}.
\tag{21}
$$
Iterating this inequality gives
$$
u_L\ge u_0^{3^L}h^{-(3^L-1)/4}.
\tag{22}
$$
Indeed the exponent of h is \(-\tfrac12(1+3+\cdots+3^{L-1})=-(3^L-1)/4\). Since \(u_L<2\), rearranging (22) gives, with \(\epsilon_L=4/(3^L-1)\),
$$
h>2^{-\epsilon_L}u_0^{4+\epsilon_L}
=u_0^4(u_0/2)^{\epsilon_L}.
\tag{23}
$$
Define
$$
\epsilon_r=\frac4{3^r-1},\qquad \gamma=4+\epsilon_r.
\tag{24}
$$
Because \(L\le r\) and \(u_0\ge2\), the last expression in (23) is at least \(2^{-\epsilon_r}u_0^{4+\epsilon_r}\). Also \(0<\epsilon_r\le2\). Equation (20) therefore implies
$$
\min(\mathcal M(t),\mathcal T(t))
\ge2^{-12}t^4Q(n_0/Q)^{4+\epsilon_r}.
\tag{25}
$$
If \(m=\sum_{x\in\mathcal V_t}p_x\), then \(m\le tn_0\), so (25) gives the local full-band estimate
$$
\min(\mathcal M(t),\mathcal T(t))
\ge2^{-12}Q^{-3-\epsilon_r}m^{4+\epsilon_r}t^{-\epsilon_r}
\qquad(|\mathcal V_t|\ge2Q).
\tag{26}
$$

It remains to combine disjoint original probability bands. If \(S_4\ge2^{-40}Q^{-3}\), (11) and \(Q^{-3}=8\,8^{-N}\) give
$$
M_3(p),\ T(p)\ge2^{-37}8^{-N}\ge c_r8^{-N}.
\tag{27}
$$
Assume henceforth \(S_4<2^{-40}Q^{-3}\). Set
$$
\begin{aligned}
t_0&=2^{-10}/Q,&t_j&=t_02^{-j}\quad(j\ge0),\\
V_j&=\mathcal V_{t_j},&n_j&=|V_j|,&m_j&=\sum_{x\in V_j}p_x,\\
\mathcal J&=\lbrace j\ge0:n_j\ge2Q\rbrace.
\end{aligned}
\tag{28}
$$
These bands include all points of D at their indicated probabilities, regardless of budget. Their half-open convention makes them pairwise disjoint, including at dyadic boundaries. The total mass above \(t_0\) is bounded by
$$
\sum_{p_x>t_0}p_x
\le t_0^{-3}S_4<2^{-10}.
\tag{29}
$$
Every other point lies in exactly one \(V_j\). The total mass in bands having \(n_j<2Q\) is at most
$$
\sum_{j\ge0}2Qt_j=4Qt_0=2^{-8}.
\tag{30}
$$
It follows that
$$
\sum_{j\in\mathcal J}m_j
>1-2^{-10}-2^{-8}>\frac12.
\tag{31}
$$
Since D is finite and all probabilities are positive, only finitely many bands are nonempty. Thus \(\mathcal J\) is finite and nonempty in this case.

Apply (26) to each full band \(V_j\) with \(j\in\mathcal J\). Disjointness of these original bands gives, separately for each original moment,
$$
\begin{aligned}
M_3(p),\ T(p)
&\ge\sum_{j\in\mathcal J}\min(\mathcal M(t_j),\mathcal T(t_j))\\
&\ge2^{-12}Q^{-3-\epsilon_r}
\sum_{j\in\mathcal J}m_j^{\gamma}t_j^{-\epsilon_r}.
\end{aligned}
\tag{32}
$$
Set
$$
\alpha=\frac{\epsilon_r}{\gamma-1}
=\frac4{3^{r+1}+1}.
\tag{33}
$$
Hölder's inequality, applied to
\(m_j=(m_j^{\gamma}t_j^{-\epsilon_r})^{1/\gamma}t_j^{\epsilon_r/\gamma}\), gives
$$
\left(\sum_{j\in\mathcal J}m_j\right)^{\gamma}
\le
\left(\sum_{j\in\mathcal J}m_j^{\gamma}t_j^{-\epsilon_r}\right)
\left(\sum_{j\in\mathcal J}t_j^{\alpha}\right)^{\gamma-1}.
\tag{34}
$$
Here \(0<\alpha\le1\). Concavity of \(a\mapsto1-2^{-a}\) on [0,1], and its values zero and 1/2 at the endpoints, imply \(1-2^{-\alpha}\ge\alpha/2\). Consequently,
$$
\sum_{j\in\mathcal J}t_j^{\alpha}
\le\sum_{j\ge0}t_j^{\alpha}
=\frac{t_0^{\alpha}}{1-2^{-\alpha}}
\le\frac2\alpha t_0^{\alpha}.
\tag{35}
$$
Combining (31), (34), and (35), and using \(\alpha(\gamma-1)=\epsilon_r\), gives
$$
\sum_{j\in\mathcal J}m_j^{\gamma}t_j^{-\epsilon_r}
>2^{-\gamma}(\alpha/2)^{\gamma-1}t_0^{-\epsilon_r}
\ge2^{-6}(\alpha/2)^5t_0^{-\epsilon_r}.
\tag{36}
$$
For the last inequality, \(4<\gamma\le6\) and \(0<\alpha/2\le1\), so \(2^{-\gamma}\ge2^{-6}\) and \((\alpha/2)^{\gamma-1}\ge(\alpha/2)^5\).

Substituting (36) and \(t_0^{-\epsilon_r}=2^{10\epsilon_r}Q^{\epsilon_r}\) in (32) gives
$$
M_3(p),\ T(p)
>2^{-18}(\alpha/2)^5 2^{10\epsilon_r}Q^{-3}
\ge2^{-18}3^{-5(r+1)}Q^{-3}.
\tag{37}
$$
Indeed, \(2^{10\epsilon_r}\ge1\) and
\(\alpha/2=2/(3^{r+1}+1)\ge3^{-(r+1)}\). Finally \(Q^{-3}=8\,8^{-N}\), so (37) implies
$$
M_3(p),\ T(p)>2^{-15}3^{-5(r+1)}8^{-N}\ge c_r8^{-N}.
\tag{38}
$$
The atomic alternative (27) and the remaining alternative (38) prove (6). The ternary consequence follows from the budget identity in the statement. The argument makes no assumption of Boolean points at the start: a Boolean image arises only if the actual midpoint cascade reaches budget zero. Its stopping bound and its positive exponent \(\epsilon_r\) depend on a fixed finite r, and the resulting \(c_r\) in (5) decays to zero. Therefore no uniform-in-r or unrestricted-support lower bound is asserted.

## External sources

None. The proof establishes the midpoint, halfspace, parity-counting, and budget-drop claims directly and uses only elementary Cauchy and Hölder inequalities and concavity of a one-variable exponential function.
