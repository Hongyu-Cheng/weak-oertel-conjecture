---
fact_id: fc66ae9d2bedbb55
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: intake14-rounded-roof-laplace
depends_on: []
verifier_run: b01cf03f32d8430c
target_match: null
---

## Statement

All logarithms are natural. Let \(n,d\in\mathbb Z_{>0}\), let \(T\subseteq\mathbb R^d\) be a convex body, and, for \(1\le i\le n\), let

\[
\ell_i^-,\ell_i^+:T\longrightarrow[0,\infty)
\]

be bounded upper-semicontinuous concave functions. Define the closed-endpoint roof body

\[
C:=\left\{(\mathbf x,\mathbf y)\in\mathbb R^n\times\mathbb R^d:
\mathbf y\in T,\quad
-\ell_i^-(\mathbf y)\le x_i\le 1+\ell_i^+(\mathbf y)
\text{ for every }i\right\},
\]

put

\[
\Lambda:=\mathbb Z^n\times\mathbb R^d,
\qquad
S:=C\cap\Lambda,
\]

and define the actual integer fibers and original mixed-integer mass by

\[
C_{\mathbf I}:=\{\mathbf y\in\mathbb R^d:(\mathbf I,\mathbf y)\in C\},
\qquad
W:=\mathcal H_d(S)
=\sum_{\mathbf I\in\mathbb Z^n}\mathcal H_d(C_{\mathbf I}).
\]

For each \(\mathbf y\in T\), define the scalar floor counts

\[
a_i(\mathbf y):=\lfloor\ell_i^-(\mathbf y)\rfloor,
\qquad
b_i(\mathbf y):=\lfloor\ell_i^+(\mathbf y)\rfloor,
\qquad
N_i(\mathbf y):=a_i(\mathbf y)+b_i(\mathbf y)+2.
\tag{1}
\]

Thus, including every integer at a closed endpoint, the integer section over \(\mathbf y\) is

\[
D(\mathbf y):=\{\mathbf I\in\mathbb Z^n:(\mathbf I,\mathbf y)\in C\}
=\prod_{i=1}^n\{-a_i(\mathbf y),-a_i(\mathbf y)+1,\ldots,b_i(\mathbf y)+1\},
\tag{2}
\]

and

\[
W=\int_T\prod_{i=1}^nN_i(\mathbf y)\,d\mathcal H_d(\mathbf y)>0.
\tag{3}
\]

Let

\[
\mu:=W^{-1}\mathcal H_d\vert_S
\]

and let \((\mathbf K,\mathbf Y)\) have law \(\mu\). Equivalently, \(\mathbf Y\) has density \(W^{-1}\prod_iN_i(\mathbf y)\) on \(T\), and, conditional on \(\mathbf Y=\mathbf y\), \(\mathbf K\) is uniform on \(D(\mathbf y)\). Hence the coordinates \(K_i\) are independent conditional on \(\mathbf Y=\mathbf y\); no independence among the roof values, the widths \(N_i(\mathbf Y)\), or the coordinates of \(\mathbf Y\) is assumed.

Now define the mixed mean, its coordinatewise nearest-integer rounding, the rounding displacement, and the selected mixed point, in that order, by

\[
\mathbf m:=\mathbb E_\mu\mathbf K,
\qquad
\mathbf y^\star:=\mathbb E_\mu\mathbf Y,
\qquad
J_i\in\operatorname*{argmin}_{j\in\mathbb Z}|m_i-j|,
\qquad
\boldsymbol\delta:=\mathbf m-\mathbf J,
\qquad
\mathbf p^\star:=(\mathbf J,\mathbf y^\star).
\tag{4}
\]

At a half-integer either nearest integer may be chosen. In every case \(|\delta_i|\le1/2\). Then \(\mathbf p^\star\in S\).

For an integer \(N\ge2\), define

\[
M_N(t):=\frac1N\sum_{r=0}^{N-1}
\exp\!\left(t\left(r-\frac{N-1}{2}\right)\right)
=
\begin{cases}
\dfrac{\sinh(Nt/2)}{N\sinh(t/2)},&t\ne0,\\[6pt]
1,&t=0.
\end{cases}
\tag{5}
\]

For every \(\mathbf u\in\mathbb R^n\) and \(\mathbf v\in\mathbb R^d\), the following width-sensitive chain holds:

\[
\begin{aligned}
\log\mathbb E_\mu\exp\!\left(
\mathbf u\cdot(\mathbf K-\mathbf J)
+\mathbf v\cdot(\mathbf Y-\mathbf y^\star)
\right)
&\ge
\sum_{i=1}^n\left[
u_i\delta_i+
\mathbb E_\mu\log M_{N_i(\mathbf Y)}(u_i)
\right]\\
&\ge
\sum_{i=1}^n\left[
u_i\delta_i+\log\cosh(u_i/2)
\right]\\
&\ge-n\log2.
\end{aligned}
\tag{6}
\]

In particular,

\[
\boxed{
\mathbb E_\mu\exp\!\left(
\mathbf u\cdot(\mathbf K-\mathbf J)
+\mathbf v\cdot(\mathbf Y-\mathbf y^\star)
\right)\ge2^{-n}
}
\tag{7}
\]

for every \(\mathbf u,\mathbf v\).

For \(\mathbf p\in\mathbb R^{n+d}\), define its Laplace capacity by

\[
\operatorname{Cap}_\mu(\mathbf p)
:=\inf_{\boldsymbol\theta\in\mathbb R^{n+d}}
\mathbb E_\mu\exp\!\left(
\boldsymbol\theta\cdot((\mathbf K,\mathbf Y)-\mathbf p)
\right).
\tag{8}
\]

Let

\[
h_{\mathrm{bin}}(q):=-q\log q-(1-q)\log(1-q),
\qquad 0\le q\le1,
\tag{9}
\]

where \(0\log0:=0\). Then the binary-entropy refinement is

\[
\boxed{
\operatorname{Cap}_\mu(\mathbf p^\star)
\ge
\exp\!\left(
\sum_{i=1}^n h_{\mathrm{bin}}(1/2+\delta_i)-n\log2
\right)
\ge2^{-n}.
}
\tag{10}
\]

Equivalently, if

\[
\Psi(\boldsymbol\theta)
:=\log\mathbb E_\mu e^{\boldsymbol\theta\cdot(\mathbf K,\mathbf Y)},
\qquad
\Psi^*(\mathbf p)
:=\sup_{\boldsymbol\theta}
\bigl(\boldsymbol\theta\cdot\mathbf p-\Psi(\boldsymbol\theta)\bigr),
\]

then

\[
\Psi^*(\mathbf p^\star)
\le\sum_{i=1}^n
\bigl[\log2-h_{\mathrm{bin}}(1/2+\delta_i)\bigr].
\tag{11}
\]

The uniform constant \(2^{-n}\) in (7) and (10) is sharp for every \(n\): for the admissible body \(C=[0,1]^n\times T\), every permitted nearest-integer choice \(\mathbf J\) satisfies

\[
\operatorname{Cap}_\mu(\mathbf p^\star)=2^{-n}.
\tag{12}
\]

Finally, for \(\mathbf p\in S\), let

\[
h_S(\mathbf p):=
\inf\{\mathcal H_d(S\cap H):
H\subseteq\mathbb R^{n+d}\text{ is a closed halfspace and }\mathbf p\in H\}.
\]

Then

\[
\frac{h_S(\mathbf p)}W\le\operatorname{Cap}_\mu(\mathbf p).
\tag{13}
\]

This is only an upper bound on normalized actual depth by capacity. In particular, (10) does not imply a lower bound on \(h_S(\mathbf p^\star)\), and no reverse comparison or actual-depth conclusion is asserted.

## Proof

Because each \(-\ell_i^-\) is lower-semicontinuous and convex and each \(1+\ell_i^+\) is upper-semicontinuous and concave, the defining inequalities make \(C\) closed and convex. Boundedness of \(T\) and of the roofs makes \(C\) bounded, while \([0,1]^n\times T\subseteq C\) gives nonempty interior. Thus \(C\) is a convex body.

For a fixed \(\mathbf y\in T\), the closed inequalities in the definition of \(C\) give exactly (2). In particular, if either roof value is an integer, the corresponding endpoint is retained. The number of integer points in the section is therefore \(\prod_iN_i(\mathbf y)\). Only finitely many integer vectors can occur because all roofs are bounded. Tonelli's theorem applied to these nonnegative section indicators gives

\[
\begin{aligned}
\sum_{\mathbf I\in\mathbb Z^n}\mathcal H_d(C_{\mathbf I})
&=\sum_{\mathbf I\in\mathbb Z^n}
\int_T\mathbf1_{\{\mathbf I\in D(\mathbf y)\}}\,d\mathcal H_d(\mathbf y)\\
&=\int_T\#D(\mathbf y)\,d\mathcal H_d(\mathbf y)
=\int_T\prod_{i=1}^nN_i(\mathbf y)\,d\mathcal H_d(\mathbf y).
\end{aligned}
\tag{14}
\]

Since every \(N_i\ge2\) and \(T\) has positive \(d\)-dimensional volume, \(W>0\). Moreover, for every measurable \(B\subseteq T\),

\[
\mu(\{\mathbf K=\mathbf I,\ \mathbf Y\in B\})
=\frac1W\int_B\mathbf1_{\{\mathbf I\in D(\mathbf y)\}}\,d\mathcal H_d(\mathbf y).
\tag{15}
\]

Summing (15) over \(\mathbf I\) proves the asserted marginal density of \(\mathbf Y\); dividing (15) by that density proves the asserted conditional uniform law. Because \(D(\mathbf y)\) is a Cartesian product, this conditional law is a product law. This establishes precisely the conditional independence used below.

For feasibility, define the midpoint of the \(i\)-th conditional integer interval by

\[
c_i(\mathbf y):=
\frac{b_i(\mathbf y)+1-a_i(\mathbf y)}2.
\tag{16}
\]

It is the conditional mean of \(K_i\). Also,

\[
[c_i(\mathbf y)-1/2,c_i(\mathbf y)+1/2]
\subseteq[-a_i(\mathbf y),b_i(\mathbf y)+1]
\subseteq[-\ell_i^-(\mathbf y),1+\ell_i^+(\mathbf y)].
\tag{17}
\]

The first inclusion follows because \(a_i+b_i\ge0\), and the second follows from the definitions of the floors. Thus

\[
c_i(\mathbf y)-\frac12\ge-\ell_i^-(\mathbf y),
\qquad
c_i(\mathbf y)+\frac12\le1+\ell_i^+(\mathbf y).
\tag{18}
\]

The barycenter \(\mathbf y^\star=\mathbb E\mathbf Y\) lies in the closed convex set \(T\). Jensen's inequality for the concave roofs gives

\[
\mathbb E\ell_i^\pm(\mathbf Y)
\le\ell_i^\pm(\mathbb E\mathbf Y)
=\ell_i^\pm(\mathbf y^\star).
\tag{19}
\]

For completeness, (19) remains valid with the stated upper-semicontinuous boundary behavior: the hypograph of each roof is a closed convex set, the barycenter of the random vector \((\mathbf Y,\ell_i^\pm(\mathbf Y))\) belongs to that hypograph, and this is exactly (19). Taking expectations in (18), and using \(m_i=\mathbb E c_i(\mathbf Y)\), gives

\[
m_i-\frac12\ge-\ell_i^-(\mathbf y^\star),
\qquad
m_i+\frac12\le1+\ell_i^+(\mathbf y^\star).
\tag{20}
\]

Hence

\[
\bigl(\mathbf m+[-1/2,1/2]^n\bigr)\times\{\mathbf y^\star\}
\subseteq C.
\tag{21}
\]

Since \(\mathbf J-\mathbf m=-\boldsymbol\delta\in[-1/2,1/2]^n\), (21) proves \(\mathbf p^\star=(\mathbf J,\mathbf y^\star)\in C\cap\Lambda=S\).

We next prove (6). Given \(\mathbf Y=\mathbf y\), write \(K_i=-a_i(\mathbf y)+R_i\), where \(R_i\) is uniform on \(\{0,\ldots,N_i(\mathbf y)-1\}\). Equation (16) is also

\[
c_i(\mathbf y)=-a_i(\mathbf y)+\frac{N_i(\mathbf y)-1}{2}.
\]

The conditional product law and (5) therefore give

\[
\begin{aligned}
&\mathbb E_\mu\!\left[
\exp\!\left(
\mathbf u\cdot(\mathbf K-\mathbf J)
+\mathbf v\cdot(\mathbf Y-\mathbf y^\star)
\right)\middle|\mathbf Y\right]\\
&\quad=\exp\!\left(
\mathbf u\cdot(\mathbf c(\mathbf Y)-\mathbf J)
+\mathbf v\cdot(\mathbf Y-\mathbf y^\star)
+\sum_{i=1}^n\log M_{N_i(\mathbf Y)}(u_i)
\right).
\end{aligned}
\tag{22}
\]

Applying Jensen's inequality to the exponential on the right side of (22), then taking logarithms, yields

\[
\begin{aligned}
\log\mathbb E_\mu e^{\mathbf u\cdot(\mathbf K-\mathbf J)
+\mathbf v\cdot(\mathbf Y-\mathbf y^\star)}
&\ge\mathbf u\cdot(\mathbb E\mathbf c(\mathbf Y)-\mathbf J)
+\mathbf v\cdot(\mathbb E\mathbf Y-\mathbf y^\star)\\
&\quad+\sum_{i=1}^n\mathbb E\log M_{N_i(\mathbf Y)}(u_i)\\
&=\sum_{i=1}^n\left[
u_i\delta_i+\mathbb E\log M_{N_i(\mathbf Y)}(u_i)
\right].
\end{aligned}
\tag{23}
\]

This proves the first inequality in (6) while retaining the actual random section widths.

For \(N\ge2\) and \(t\ne0\), put \(s=|t|/2>0\). The function

\[
f_s(x):=\frac{\sinh(xs)}x
\]

is nondecreasing for \(x>0\), because the numerator of its derivative is

\[
xs\cosh(xs)-\sinh(xs),
\]

whose derivative as a function of \(xs\ge0\) is \(xs\sinh(xs)\ge0\) and whose value at zero is zero. Therefore

\[
M_N(t)=\frac{\sinh(Ns)}{N\sinh s}
\ge\frac{\sinh(2s)}{2\sinh s}
=\cosh s=\cosh(t/2).
\tag{24}
\]

The same inequality is equality at \(t=0\). It holds pointwise for every value of \(N_i(\mathbf Y)\), proving the second inequality in (6). Finally, \(|\delta_i|\le1/2\) and

\[
u_i\delta_i+\log\cosh(u_i/2)
\ge-\frac{|u_i|}{2}
+\log\left(\frac{e^{|u_i|/2}}2\right)
=-\log2.
\tag{25}
\]

Summing (25) proves the last inequality in (6), and exponentiating proves (7).

To prove sharpness, set every roof equal to zero, so \(C=[0,1]^n\times T\). Then \(\mathbf K\) is uniform on \(\{0,1\}^n\), independently of \(\mathbf Y\), and \(\mathbf m=\tfrac12\mathbf1\). Every allowed \(\mathbf J\) is a Boolean corner. For \(t>0\), set

\[
u_i(t):=t(2J_i-1),
\qquad
\mathbf v:=\mathbf0.
\]

For each coordinate, \(u_i(t)(K_i-J_i)\) is zero when \(K_i=J_i\) and is \(-t\) otherwise. Consequently,

\[
\mathbb E_\mu e^{\mathbf u(t)\cdot(\mathbf K-\mathbf J)}
=\left(\frac{1+e^{-t}}2\right)^n
\longrightarrow2^{-n}.
\tag{26}
\]

Equation (7) gives the reverse inequality for every transform parameter, so (26) proves (12) and sharpness.

We now prove the entropy refinement. For \(|\delta|\le1/2\), put \(q=1/2+\delta\in[0,1]\). Then

\[
e^{s\delta}\cosh(s/2)
=\frac12\left(e^{sq}+e^{-s(1-q)}\right).
\tag{27}
\]

If \(0<q<1\), differentiation shows that the unique minimum occurs at

\[
e^s=\frac{1-q}{q},
\]

and substitution gives

\[
\inf_{s\in\mathbb R}e^{s\delta}\cosh(s/2)
=\frac1{2q^q(1-q)^{1-q}}
=\exp\bigl(h_{\mathrm{bin}}(q)-\log2\bigr).
\tag{28}
\]

For \(q=0\) or \(q=1\), the same formula follows by sending \(s\) to the appropriate infinite endpoint and using \(0\log0=0\). The second inequality in (6), followed by (28) coordinate by coordinate, gives

\[
\begin{aligned}
\log\operatorname{Cap}_\mu(\mathbf p^\star)
&=\inf_{\mathbf u,\mathbf v}
\log\mathbb E_\mu
e^{\mathbf u\cdot(\mathbf K-\mathbf J)
+\mathbf v\cdot(\mathbf Y-\mathbf y^\star)}\\
&\ge\sum_{i=1}^n
\inf_{s\in\mathbb R}\bigl[s\delta_i+\log\cosh(s/2)\bigr]\\
&=\sum_{i=1}^n h_{\mathrm{bin}}(1/2+\delta_i)-n\log2.
\end{aligned}
\tag{29}
\]

This proves the first inequality in (10); the second follows from nonnegativity of binary entropy. Also,

\[
\log\operatorname{Cap}_\mu(\mathbf p^\star)
=\inf_{\boldsymbol\theta}
\bigl[\Psi(\boldsymbol\theta)-\boldsymbol\theta\cdot\mathbf p^\star\bigr]
=-\Psi^*(\mathbf p^\star),
\tag{30}
\]

so (11) is exactly the equivalent form of (10). The \(i\)-th cost in (11) is zero when \(m_i\in\mathbb Z\), because then \(\delta_i=0\), and is maximal at \(\delta_i=\pm1/2\), where it equals \(\log2\).

It remains to establish the direction of the depth comparison. Fix \(\mathbf p\in S\). For every nonzero \(\boldsymbol\theta\in\mathbb R^{n+d}\), the closed halfspace

\[
H_{\boldsymbol\theta}:=
\{\mathbf x\in\mathbb R^{n+d}:
\boldsymbol\theta\cdot(\mathbf x-\mathbf p)\ge0\}
\]

contains \(\mathbf p\), and pointwise on \(S\),

\[
\mathbf1_{H_{\boldsymbol\theta}}(\mathbf x)
\le e^{\boldsymbol\theta\cdot(\mathbf x-\mathbf p)}.
\tag{31}
\]

Therefore

\[
\frac{h_S(\mathbf p)}W
\le\mu(H_{\boldsymbol\theta})
\le\mathbb E_\mu
e^{\boldsymbol\theta\cdot((\mathbf K,\mathbf Y)-\mathbf p)}.
\tag{32}
\]

The last expectation is continuous in \(\boldsymbol\theta\), because \(C\) is compact, so its infimum over nonzero \(\boldsymbol\theta\) equals its infimum over all \(\boldsymbol\theta\): parameters tending to zero recover the value one at zero. Taking the infimum in (32) proves (13). Its direction shows why the capacity lower bounds (7) and (10) cannot be used as actual-depth lower bounds.

## External sources

None.
