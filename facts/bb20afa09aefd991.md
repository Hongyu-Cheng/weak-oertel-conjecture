---
fact_id: bb20afa09aefd991
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: intake18-balanced-floor-information-depth
depends_on: ["6d6fcf377e68c79c","9ee12600178ce4dd"]
verifier_run: b35ded4557f4469c
target_match: null
---

## Statement

Let
\[
C=\{(\mathbf x,\mathbf y):
\mathbf y\in T,\ -\ell_i^-(\mathbf y)\le x_i\le1+\ell_i^+(\mathbf y)\},
\quad S=C\cap(\mathbb Z^n\times\mathbb R^d),
\]
where \(T\) is a compact convex body and the roofs are nonnegative bounded upper-semicontinuous concave functions. Put
\[
a_i=\lfloor\ell_i^-\rfloor,\quad b_i=\lfloor\ell_i^+\rfloor,\quad
B=\prod_i(a_i+b_i+1),\quad M=\int_TB.
\]
Assume \(|a_i-b_i|\le1\) almost everywhere. Let
\(H_*=\max_{\mathbf p\in S}h_S(\mathbf p)\), using actual unnormalized mixed depth and closed halfspaces.

For every nonnegative integrable density \(\rho\) supported on \(T\), define
\[
\tau_\rho(\mathbf y)
:=
\inf_{\substack{L\subset\mathbb R^d\text{ a proper closed halfspace}\\
                  \mathbf y\in L}}
\int_{T\cap L}\rho(\mathbf z)\,d\mathbf z.
\]
In particular, define the maximum base depth
\[
\Delta_B:=\max_{\mathbf y\in T}\tau_B(\mathbf y).
\]

For \(\mathbf J\in\{0,1\}^n\), define
\[
R_{\mathbf J}(\mathbf y)
=\#\{\mathbf k:(\mathbf k,\mathbf y),(2\mathbf J-\mathbf k,\mathbf y)\in S\},
\quad Z_{\mathbf J}=\int_TR_{\mathbf J}.
\]
Then
\[
2^{-n}\sum_{\mathbf J}R_{\mathbf J}=B\quad\text{almost everywhere},
\qquad H_*\ge M/[2(d+1)].
\]
In particular, when \(d=1\), the nonatomic measure with density \(B\) has \(\Delta_B=M/2\), and hence
\[
H_*\ge M/4=\Delta_B/2.
\]

Define
\[
\mathbb P(\mathbf J=\mathbf j,\mathbf Y\in d\mathbf y)
=\frac{R_{\mathbf j}(\mathbf y)}{2^nM}\,d\mathbf y,
\]
and let \(\nu_B\) be its base marginal, with density \(B/M\) up to equality almost everywhere.
For every log-concave probability density reference \(\mu\) supported on \(T\), with \(D(\nu_B\|\mu)<\infty\),
\[
H_*\ge
\frac{M}{600[1+D(\nu_B\|\mu)+I(\mathbf J;\mathbf Y)]}. \tag{1}
\]

With
\[
\delta_i=\frac{|a_i-b_i|}{a_i+b_i+1},
\quad
\chi(t)=\tfrac12[(1+t)\log(1+t)+(1-t)\log(1-t)],
\]
and with \(\pi\) the marginal law of \(\mathbf J\), one has the exact identity
\[
I(\mathbf J;\mathbf Y)
=\mathbb E_{\nu_B}\sum_i\chi(\delta_i)-D(\pi\|U),
\]
where \(U\) is the uniform law on \(\{0,1\}^n\).

If \(B\) is constant and the floor-pattern vector \((a_1,b_1,\ldots,a_n,b_n)\) has at most \(K\) values almost everywhere, then
\(H_*\ge M/[600(1+\log K)]\).
If exactly \(k\) coordinates have three sites and all others have two sites almost everywhere, then
\[
H_*\ge\frac{M}{600(1+c_*k)},
\qquad c_*=\tfrac34\log3-\log2.
\]

For the final conditional assertion, a one-sided thin roof body means the following object. For arbitrary positive integers \(n,d\), a compact convex body \(T\subset\mathbb R^d\), and nonnegative upper-semicontinuous concave functions \(f_i:T\to[0,1]\), set
\[
C_f:=\{(\mathbf x,\mathbf y):\mathbf y\in T,\ 0\le x_i\le1+f_i(\mathbf y)\},
\qquad
S_f:=C_f\cap(\mathbb Z^n\times\mathbb R^d).
\]
For measurable \(A\subseteq\mathbb Z^n\times\mathbb R^d\), use the actual unnormalized mixed mass
\[
\mathcal H_d(A)
:=\sum_{\mathbf z\in\mathbb Z^n}
\mathcal H_d\bigl(A\cap(\{\mathbf z\}\times\mathbb R^d)\bigr),
\]
and, for \(\mathbf p\in S_f\), the actual closed-halfspace depth
\[
h_{S_f}(\mathbf p)
:=\inf_{\substack{H\subseteq\mathbb R^{n+d}\text{ a closed halfspace}\\
                   \mathbf p\in H}}
\mathcal H_d(S_f\cap H).
\]
Writing \(\mathbf{1}:=(1,\ldots,1)\in\mathbb Z^n\), the central reflection-pair mass of this body is
\[
Q_f
:=\int_T
\#\{\mathbf k\in\mathbb Z^n:(\mathbf k,\mathbf y),(2\mathbf{1}-\mathbf k,\mathbf y)\in S_f\}
\,d\mathbf y
=\int_T\prod_i(1+2\lfloor f_i\rfloor).
\]
Thus \(Q_f\), rather than the total mixed mass \(\mathcal H_d(S_f)=\int_T\prod_i(2+\lfloor f_i\rfloor)\), is the quantity on the right-hand side of the conditional premise.

If there is an absolute \(c>0\) such that every one-sided thin roof body just defined satisfies
\[
\max_{\mathbf p\in S_f}h_{S_f}(\mathbf p)\ge cQ_f
=c\int_T\prod_i(1+2\lfloor f_i\rfloor),
\]
then every thin asymmetric roof body with \(a_i,b_i\in\{0,1\}\) almost everywhere satisfies \(H_*\ge cM\). This final assertion is conditional; its one-sided premise is not asserted.

## Proof

For the scalar section \(\{-a,\ldots,b+1\}\),
\[
r_0=2\min(a,b+1)+1,\qquad
r_1=2\min(a+1,b)+1.
\]
When \(|a-b|\le1\), \((r_0+r_1)/2=a+b+1\). Since the balance hypothesis holds almost everywhere, multiplication proves
\[
2^{-n}\sum_{\mathbf J}R_{\mathbf J}=B
\quad\text{almost everywhere}.
\]
Integration therefore gives \(2^{-n}\sum_{\mathbf J}Z_{\mathbf J}=M\), so some \(\mathbf J\) has \(Z_{\mathbf J}\ge M\).

At every \(\mathbf y_0\), same-fiber reflection gives
\[
h_S((\mathbf J,\mathbf y_0))
\ge\tfrac12\tau_{R_{\mathbf J}}(\mathbf y_0).
\]
Apply accepted fact `6d6fcf377e68c79c` with zero integer dimension to the continuous density \(R_{\mathbf J}\). Its centerpoint has depth at least \(Z_{\mathbf J}/(d+1)\), proving the first bound. In dimension one use a median. Since \(B(\mathbf y)\,d\mathbf y\) is nonatomic and has mass \(M\), its maximum base depth is \(\Delta_B=M/2\).

Let \(\nu_{\mathbf J}=R_{\mathbf J}d\mathbf y/Z_{\mathbf J}\),
\(D_{\mathbf J}=D(\nu_{\mathbf J}\|\mu)\), and
\(\pi_{\mathbf J}=Z_{\mathbf J}/(2^nM)\).
All these relative entropies are finite: outside the null exceptional set, the conditional densities relative to \(\nu_B\) are bounded above and below by positive instance-dependent constants, and changing densities on that exceptional set changes none of the measures. The entropy chain rule gives
\[
\sum_{\mathbf J}\pi_{\mathbf J}D_{\mathbf J}
=D(\nu_B\|\mu)+I(\mathbf J;\mathbf Y). \tag{2}
\]

Accepted fact `9ee12600178ce4dd` implies that a density of mass \(Z\), with normalized relative entropy \(D\) from a log-concave reference, has maximum depth at least \(Z/[300(1+D)]\). To check this consequence, take
\(\theta=1/(1+D)\), \(\alpha=1/(1+\theta)\).
Jensen gives fractional moment at least \(Ze^{-\theta D}\), and the explicit constant satisfies
\(\kappa_{1/(1+\theta)}\ge\theta/100\).
This last scalar inequality follows by bounding
\(3^u-2^u\ge u\log(3/2)\), with \(u=\theta/(1+\theta)\); the stronger bound \(\theta/25\) follows by differentiation of
\(\theta^\theta[\log(3/2)/(1+\theta)]^{1+\theta}\).

Together with reflection,
\[
H_*\ge Z_{\mathbf J}/[600(1+D_{\mathbf J})]
\quad\text{for every }\mathbf J.
\]
Let \(L=\max_{\mathbf J}Z_{\mathbf J}/(1+D_{\mathbf J})\). Then
\[
M^2\le2^{-n}\sum_{\mathbf J}Z_{\mathbf J}^2
\le LM[1+D(\nu_B\|\mu)+I(\mathbf J;\mathbf Y)],
\]
by (2). This proves (1).

For \(\nu_B\)-almost every base point, the label bits are conditionally independent and have probabilities
\((1+\delta_i)/2,(1-\delta_i)/2\), in one order or the other. Their entropy relative to fair bits is \(\chi(\delta_i)\). Applying the entropy chain rule relative to the uniform label law gives the exact information identity; its expectation is unchanged by the exceptional null set.

If \(B\) is constant, use the uniform reference. Almost surely, the conditional label law depends only on the floor pattern, so its mutual information with the base is at most the pattern entropy, hence at most \(\log K\). In the almost-everywhere two-/three-site description, a three-site coordinate has \(\delta_i=1/2\) and every two-site coordinate has \(\delta_i=0\); \(\chi(1/2)=c_*\). This proves the stated consequences.

For the conditional thin-roof reduction, choose \(\mathbf J\) with \(Z_{\mathbf J}\ge M\). Define
\[
f_i(\mathbf y)
:=
\begin{cases}
\min\{\ell_i^-(\mathbf y),1\},&J_i=0,\\
\min\{\ell_i^+(\mathbf y),1\},&J_i=1.
\end{cases}
\]
These functions are nonnegative upper-semicontinuous concave and take values in \([0,1]\). Inside \(C\), retain the coordinate interval \([-f_i(\mathbf y),1]\) when \(J_i=0\), and retain \([0,1+f_i(\mathbf y)]\) when \(J_i=1\). Reflect each retained negative coordinate by \(x_i\mapsto1-x_i\). This lattice-preserving affine isometry maps the resulting convex subbody onto the one-sided body \(C_f\) and maps \((\mathbf J,\mathbf y)\) to \((\mathbf{1},\mathbf y)\).

At every base point where \(a_i,b_i\in\{0,1\}\) for all \(i\), one has
\[
1+2\lfloor f_i\rfloor
=
\begin{cases}
r_0,&J_i=0,\\
r_1,&J_i=1.
\end{cases}
\]
The thinness hypothesis gives this equality almost everywhere, so integration shows that the central reflection-pair mass \(Q_f\) is exactly \(Z_{\mathbf J}\). The assumed one-sided theorem supplies a point of the retained subbody with actual depth at least \(cZ_{\mathbf J}\). Every halfspace has at least as much mixed mass in \(S\) as in this subbody, so
\[
H_*\ge cZ_{\mathbf J}\ge cM.
\]

## External sources

None beyond the declared accepted predecessors.
