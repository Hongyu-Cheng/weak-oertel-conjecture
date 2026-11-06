---
fact_id: ac87fdfe8d02a7ee
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: intake14-capacity-obstructions
depends_on: ["02a48d28569660b9","bf1ff94487296374","ce8cccfdbee6f1cc"]
verifier_run: 430e2996fc4a4c9d
target_match: null
---

## Statement

For a compactly supported probability law \(p\) on \(\mathbb R^N\), and a point \(\mathbf z\) in its support, write
\[
\tau_p(\mathbf z)
:=\inf_{\substack{H\subseteq\mathbb R^N\text{ a proper closed halfspace}\\
                   \mathbf z\in H}}p(H),
\qquad
\mathsf C_p(\mathbf z)
:=\inf_{\mathbf a\in\mathbb R^N}
\int e^{\mathbf a\cdot(\mathbf x-\mathbf z)}\,dp(\mathbf x).
\tag{1}
\]
For finite laws, \(\mathsf C_p\) is the canonical entropy capacity of accepted fact \(\mathrm{bf1ff94487296374}\). It is exactly the quantity denoted \(\mathcal C_p\) in the unverified source; thus
\[
\boxed{\mathcal C_p^{\rm source}=\mathsf C_p^{\rm canonical}.}
\tag{2}
\]
For \(q>0\), put
\[
M_q(p):=\sum_{\mathbf z}p_{\mathbf z}\tau_p(\mathbf z)^q
\tag{3}
\]
when \(p\) is finite.

(A) There are, for integers \(N\to\infty\), full-dimensional complete lattice supports
\[
L_N=\operatorname{conv}(L_N)\cap\mathbb Z^N,
\]
uniform probability laws \(p_N\) on \(L_N\), and \(\mathbf z_N\in L_N\) such that
\[
\boxed{
\mathsf C_{p_N}(\mathbf z_N)=(1+o(1))2^{-N},
\qquad
\tau_{p_N}(\mathbf z_N)
=\left(\sqrt{\frac7{6\pi}}+o(1)\right)
\frac{2^{-N}}{\sqrt N}.}
\tag{4}
\]
Consequently no absolute \(c>0\) can satisfy
\(\tau_p(\mathbf z)\ge c\mathsf C_p(\mathbf z)\) for all uniform laws on full-dimensional complete lattice supports, even when \(\mathsf C_p(\mathbf z)/2^{-N}\to1\). Nevertheless these laws obey, for every fixed \(q\ge1\),
\[
M_q(p_N)\ge2^{-q(N+1)}.
\tag{5}
\]

(B) For every \(N\ge1\), let
\[
Q_N=\operatorname{conv}\{\mathbf e_1,\ldots,\mathbf e_N,-\mathbf1\},
\qquad
D_N=Q_N\cap\mathbb Z^N
=\{\mathbf0,\mathbf e_1,\ldots,\mathbf e_N,-\mathbf1\},
\tag{6}
\]
and let \(\pi_N\) be uniform on \(D_N\). Then
\[
\tau_{\pi_N}(\mathbf0)=\frac2{N+2},
\qquad
\tau_{\pi_N}(\mathbf v)=\frac1{N+2}
\quad(\mathbf v\in D_N\setminus\{\mathbf0\}),
\tag{7}
\]
and, for every \(q>0\),
\[
\boxed{M_q(\pi_N)=\frac{N+1+2^q}{(N+2)^{q+1}}.}
\tag{8}
\]
Moreover,
\[
\mathsf C_{\pi_N}(\mathbf0)=1,
\qquad
\mathsf C_{\pi_N}(\mathbf v)=\frac1{N+2}
\quad(\mathbf v\in D_N\setminus\{\mathbf0\}),
\tag{9}
\]
so for every \(s>1\),
\[
\boxed{
\sum_{\mathbf z\in D_N}\pi_{N,\mathbf z}
       \mathsf C_{\pi_N}(\mathbf z)^s
=\frac{1+(N+1)(N+2)^{-s}}{N+2}.}
\tag{10}
\]
Thus, for every fixed \(s>1\) and \(q>0\),
\[
\boxed{
\frac{\left(\sum_{\mathbf z}\pi_{N,\mathbf z}
             \mathsf C_{\pi_N}(\mathbf z)^s\right)^{1/s}}
     {M_q(\pi_N)^{1/q}}
\sim N^{1-1/s}\longrightarrow\infty.}
\tag{11}
\]
In particular, there is no dimension-independent finite constant \(A_{s,q}\) for which the numerator in (11) is at most \(A_{s,q}M_q(p)^{1/q}\) for every complete lattice law \(p\).

Accepted fact \(\mathrm{ce8cccfdbee6f1cc}\) already rules out unrestricted universal conversions from the capacity second moment to the depth second moment on other complete log-affine families. Accepted fact \(\mathrm{02a48d28569660b9}\) already establishes the simplex census in (6), its zero mean under the uniform law, and a related mixed-integer cylinder obstruction to a maximum-capacity argument. Assertions (4) and (11) are the new critical-window and all-exponent refinements. They do not refute Hq or the locked target: (5) gives the relevant lower calibration for (A), while in (B), \(2^{qN}M_q(\pi_N)\to\infty\) for every fixed \(q>0\); moreover \(\mathrm{02a48d28569660b9}\) proves that the corresponding one-continuous-dimensional cylinder satisfies the locked conclusion.

## Proof

1. Continuous ball formulas and the minimizing tilt.

Let \(\nu_N\) be normalized Lebesgue measure on the Euclidean unit ball \(B_2^N\), and let \(0<r<1\). The first coordinate has density
\[
f_N(t)=\gamma_N(1-t^2)^{(N-1)/2}\mathbf1_{[-1,1]}(t),
\qquad
\gamma_N=\frac{\Gamma(N/2+1)}
{\sqrt\pi\,\Gamma((N+1)/2)}.
\tag{12}
\]
Any halfspace containing \(r\mathbf e_1\) contains its parallel translate whose boundary passes through that point. After choosing a unit normal, such a translated halfspace has the form
\(\{\mathbf x:\mathbf u\cdot\mathbf x\ge r u_1\}\). Rotational invariance makes its measure the upper tail of the first coordinate at \(ru_1\). This tail is decreasing, and \(u_1\le1\), so the minimum occurs at \(\mathbf u=\mathbf e_1\). Hence
\[
\tau_{\nu_N}(r\mathbf e_1)
=\gamma_N\int_r^1(1-t^2)^{(N-1)/2}\,dt.
\tag{13}
\]

Fix a compact interval \(K\Subset(0,1)\), put \(m=N-1\), and let \(r\in K\). Stirling's formula gives
\[
\gamma_N=(1+O(N^{-1}))\sqrt{\frac{N}{2\pi}}.
\tag{14}
\]
For \(\psi(t)=\tfrac12\log(1-t^2)\), the derivative
\(\psi'(r)=-r/(1-r^2)\) is uniformly bounded away from zero on \(K\). Splitting the integral at a fixed small distance from \(r\), Taylor expanding on the first part, and substituting \(y=m(t-r)\) gives the uniform endpoint estimate
\[
\int_r^1e^{m\psi(t)}\,dt
=(1+o(1))\frac{1-r^2}{mr}(1-r^2)^{m/2}.
\tag{15}
\]
Indeed, the domination after substitution follows from
\(\psi(t)-\psi(r)\le-c_K(t-r)\) near \(r\); the remaining part is
\(O(e^{-c_Km})e^{m\psi(r)}\). Thus (14)-(15) imply, uniformly for \(r\in K\),
\[
\tau_{\nu_N}(r\mathbf e_1)
=(1+o(1))
\frac{\sqrt{1-r^2}}{r\sqrt{2\pi N}}
(1-r^2)^{N/2}.
\tag{16}
\]

Rotational invariance also shows that the vector tilt minimizing (1) is parallel to \(\mathbf e_1\) with nonnegative coefficient: at fixed norm this orientation maximizes its scalar product with \(r\mathbf e_1\), while the moment generating function depends only on the norm. Therefore
\[
\mathsf C_{\nu_N}(r\mathbf e_1)
=\inf_{a\ge0}e^{-ar}\gamma_N
\int_{-1}^1e^{at}(1-t^2)^{m/2}\,dt.
\tag{17}
\]
The objective is coercive as \(a\to\infty\): an interval contained in \((r,1)\) gives a positive fixed mass on which \(e^{a(t-r)}\) grows exponentially. Its logarithm is strictly convex, and its derivative at zero is \(-r<0\); hence it has a unique minimizer \(a_N(r)>0\), characterized by the tilted mean being \(r\).

We now locate that minimizer. Set
\[
\lambda(r)=\frac r{1-r^2},
\qquad
A(r)=\frac{1+r^2}{(1-r^2)^2}.
\tag{18}
\]
For \(\alpha\) in a compact subinterval of \((0,\infty)\), the phase
\[
\phi_\alpha(t)=\alpha t+\frac12\log(1-t^2)
\tag{19}
\]
has a unique maximizer \(t(\alpha)\in(0,1)\), determined by
\(\alpha=t(\alpha)/(1-t(\alpha)^2)\), and its second derivative there is negative and bounded away from zero. Taylor expansion on
\(\lvert t-t(\alpha)\rvert\le m^{-2/5}\), followed by
\(y=\sqrt m(t-t(\alpha))\), gives
\[
\int_{-1}^1e^{(m\alpha+b)t}(1-t^2)^{m/2}\,dt
=e^{m\phi_\alpha(t(\alpha))+bt(\alpha)}
\sqrt{\frac{2\pi}{m\lvert\phi_\alpha''(t(\alpha))\rvert}}
(1+O(m^{-1}))
\tag{20}
\]
uniformly when \(\alpha\) ranges over such a compact interval and \(b\) is bounded. On the complement, strict concavity near the maximizer and a fixed phase gap away from it give an exponentially smaller contribution. The same calculation with one or two factors of \(t-t(\alpha)\) shows that the tilted mean is \(t(\alpha)+O(m^{-1})\) and its variance is bounded above and below by positive constant multiples of \(m^{-1}\), uniformly in the same range.

Choose fixed \(\alpha_-<\lambda(r)<\alpha_+\), uniformly for \(r\in K\), so that
\(t(\alpha_-)<r<t(\alpha_+)\). The tilted-mean estimate and its monotonicity place \(a_N(r)/m\) between \(\alpha_-\) and \(\alpha_+\) for all large \(N\). At the minimizer the tilted mean equals \(r\), so
\(t(a_N(r)/m)=r+O(m^{-1})\). The inverse relation in (18), whose derivative is bounded on \(K\), yields
\[
a_N(r)=m\frac r{1-r^2}+O_K(1).
\tag{21}
\]
This also proves boundedness of \(b=a_N(r)-m\lambda(r)\) in (20).

At \(\alpha=\lambda(r)\), the maximizer in (19) is \(r\), and
\[
\phi_{\lambda(r)}''(r)=-A(r).
\tag{22}
\]
Substituting (20)-(22) into (17), the factor \(e^{a_N(r)r}\) from the integral cancels \(e^{-a_N(r)r}\). Using (14) gives, uniformly for \(r\in K\),
\[
\mathsf C_{\nu_N}(r\mathbf e_1)
=(1+o(1))\frac1{\sqrt{A(r)}}(1-r^2)^{m/2}
=(1+o(1))
\sqrt{\frac{1-r^2}{1+r^2}}
(1-r^2)^{N/2}.
\tag{23}
\]

2. The critical radius and the sharp ratio.

For fixed \(N\), the capacity in (17) is continuous and strictly decreasing in
\(r\in(0,1)\). Indeed, using the positive optimizer at a smaller radius gives a strict upper bound at a larger radius. Its value at zero is one. For every fixed \(a>0\), taking \(r\uparrow1\) in the corresponding value in (17), and then taking \(a\to\infty\), gives zero by dominated convergence applied to
\(e^{-a(1-X_1)}\), since \(X_1<1\) almost surely. Thus there is a unique
\(r_N\in(0,1)\) such that
\[
\mathsf C_{\nu_N}(r_N\mathbf e_1)=2^{-N}.
\tag{24}
\]
Formula (23), first at two fixed radii with \(1-r^2\) respectively larger and smaller than \(1/4\), shows that \(r_N\) stays in a compact subinterval of \((0,1)\) and that \(1-r_N^2\to1/4\). Taking logarithms in (23)-(24) gives
\[
0=\frac N2\log\bigl(4(1-r_N^2)\bigr)
+\frac12\log\frac{1-r_N^2}{1+r_N^2}+o(1).
\tag{25}
\]
Writing \(1-r_N^2=1/4+\delta_N\), (25) first gives
\(\delta_N=O(N^{-1})\), and expansion of both logarithms then gives
\[
2N\delta_N-\frac12\log7+o(1)=0.
\]
Therefore
\[
r_N^2=\frac34-\frac{\log7}{4N}+o(N^{-1}).
\tag{26}
\]
Dividing (16) by (23) and using (24) and (26), we obtain
\[
\begin{aligned}
\tau_{\nu_N}(r_N\mathbf e_1)
&=(1+o(1))
\sqrt{\frac{1+r_N^2}{2\pi r_N^2N}}
\mathsf C_{\nu_N}(r_N\mathbf e_1)\\
&=\left(\sqrt{\frac7{6\pi}}+o(1)\right)
\frac{2^{-N}}{\sqrt N}.
\end{aligned}
\tag{27}
\]

3. Uniform halfspace convergence and diagonal lattice discretization.

Fix \(N\) temporarily. For integers \(R\ge1\), let
\[
L_{N,R}=RB_2^N\cap\mathbb Z^N,
\qquad
\mu_{N,R}=\frac1{\lvert L_{N,R}\rvert}
\sum_{\mathbf x\in L_{N,R}}\delta_{\mathbf x/R}.
\tag{28}
\]
Ordinary Riemann sums, with the sphere and all hyperplanes having Lebesgue measure zero, show that \(\mu_{N,R}\Rightarrow\nu_N\). In fact the convergence is uniform over all closed halfspaces:
\[
\sup_H\lvert\mu_{N,R}(H)-\nu_N(H)\rvert\longrightarrow0.
\tag{29}
\]
To prove (29), if it failed, choose
\(H_R=\{\mathbf x:\mathbf u_R\cdot\mathbf x\ge t_R\}\) with a fixed positive discrepancy. Halfspaces missing or containing the unit ball cause no difficulty, so after clipping \(t_R\) we may take
\((\mathbf u_R,t_R)\in S^{N-1}\times[-1,1]\). Pass to a subsequence converging to \((\mathbf u,t)\). For every \(\varepsilon>0\), eventually
\[
\{\mathbf u\cdot\mathbf x\ge t+\varepsilon\}
\subseteq H_R
\subseteq
\{\mathbf u\cdot\mathbf x\ge t-\varepsilon\}
\quad(\mathbf x\in B_2^N).
\tag{30}
\]
Weak convergence applies to the two fixed bounding halfspaces, and the
\(\nu_N\)-mass of the intervening slab tends to zero with \(\varepsilon\), because the limiting hyperplane has zero mass. The same inclusions control
\(\nu_N(H_R)\), contradicting the chosen discrepancy.

Choose \(\mathbf z_{N,R}\in L_{N,R}\) with
\(\mathbf z_{N,R}/R\to r_N\mathbf e_1\), for example
\(\mathbf z_{N,R}=\lfloor Rr_N\rfloor\mathbf e_1\). Translating every containing halfspace until its boundary passes through the target shows
\[
\tau_\mu(\mathbf z)
=\inf_{\mathbf u\in S^{N-1}}
\mu\{\mathbf x:\mathbf u\cdot(\mathbf x-\mathbf z)\ge0\}.
\tag{31}
\]
Equations (29)-(31), together with the uniformly vanishing
\(\nu_N\)-mass of slabs whose widths tend to zero, imply
\[
\tau_{\mu_{N,R}}(\mathbf z_{N,R}/R)
\longrightarrow\tau_{\nu_N}(r_N\mathbf e_1).
\tag{32}
\]

Capacity converges as well. Put \(\mathbf z=r_N\mathbf e_1\) and choose
\(\rho>0\) so small that
\(\overline B(\mathbf z+3\rho\mathbf u,\rho)\subset B_2^N\) for every unit
\(\mathbf u\). For all large \(R\), (29) implies, uniformly in
\(\mathbf u\),
\[
\mu_{N,R}\{\mathbf x:\mathbf u\cdot
(\mathbf x-\mathbf z_{N,R}/R)\ge\rho\}\ge c_N>0,
\tag{33}
\]
because the displayed halfspace contains the indicated radius-\(\rho\) ball after decreasing \(\rho\) if necessary. Hence, for \(a\ge0\),
\[
\int e^{a\mathbf u\cdot(\mathbf x-\mathbf z_{N,R}/R)}
\,d\mu_{N,R}(\mathbf x)
\ge c_Ne^{a\rho}.
\tag{34}
\]
Since the value at zero tilt is one, every minimizing tilt lies in one fixed ball, independent of large \(R\). On that ball the exponential integrals converge locally uniformly to the corresponding integral for \(\nu_N\): weak convergence gives pointwise convergence, while bounded support gives a common Lipschitz bound in the tilt and hence convergence on a finite net. Taking infima yields
\[
\mathsf C_{\mu_{N,R}}(\mathbf z_{N,R}/R)
\longrightarrow\mathsf C_{\nu_N}(r_N\mathbf e_1)=2^{-N}.
\tag{35}
\]

Depth and capacity are invariant under the invertible scaling
\(\mathbf x\mapsto\mathbf x/R\); in the capacity formula set the rescaled tilt equal to \(R\) times the original tilt. For each \(N\), choose an integer \(R_N\) so large that the relative errors in both (32) and (35) are at most \(1/N\), and set
\[
L_N=L_{N,R_N},\qquad
p_N=\operatorname{Unif}(L_N),\qquad
\mathbf z_N=\mathbf z_{N,R_N}.
\tag{36}
\]
This diagonal choice, (24), and (27) prove (4). Each \(L_N\) is complete because
\(\operatorname{conv}(L_N)\subseteq R_NB_2^N\), whence
\(\operatorname{conv}(L_N)\cap\mathbb Z^N\subseteq L_N\), and the reverse inclusion is automatic. Taking \(R_N\ge1\) makes it full-dimensional because it contains \(\mathbf0,\mathbf e_1,\ldots,\mathbf e_N\).

4. Why the lattice balls do not violate the averaged target scale.

Let \(D=\operatorname{conv}(D)\cap\mathbb Z^N\) be any finite complete support, let \(p\) be uniform on \(D\), and define
\[
R_{\mathbf z}=\#\{\mathbf x\in D:2\mathbf z-\mathbf x\in D\}.
\tag{37}
\]
Every halfspace whose boundary passes through \(\mathbf z\) contains at least one point from each reflected pair, so
\(\tau_p(\mathbf z)\ge R_{\mathbf z}/(2\lvert D\rvert)\). Completeness makes midpoint formation a bijection between the reflected triples counted on the left and ordered same-parity pairs, giving
\[
\sum_{\mathbf z\in D}R_{\mathbf z}
=\sum_{\boldsymbol\varepsilon\in\{0,1\}^N}
\lvert D\cap(2\mathbb Z^N+\boldsymbol\varepsilon)\rvert^2
\ge\frac{\lvert D\rvert^2}{2^N}.
\tag{38}
\]
Thus \(M_1(p)\ge2^{-(N+1)}\), and Jensen's inequality gives
\(M_q(p)\ge M_1(p)^q\) for \(q\ge1\). Applying this to (36) proves (5).

5. The simplex identities and all-exponent separation.

The full dimensionality and exact complete support (6) were established in accepted fact \(\mathrm{02a48d28569660b9}\). Its barycentric census can also be seen directly: if
\(\mathbf z=-\lambda_0\mathbf1+\sum_i\lambda_i\mathbf e_i\), with all coefficients nonnegative and summing to one, then
\(z_i=\lambda_i-\lambda_0\). An integer coordinate equal to \(-1\) forces
\(\lambda_0=1\) and gives \(\mathbf z=-\mathbf1\). Otherwise every coordinate is zero or one and
\(\sum_i z_i=1-(N+1)\lambda_0\le1\), giving only \(\mathbf0\) and the standard basis vectors. Thus no lattice points are missing from (6).

Every nonzero point in \(D_N\) is a vertex of the simplex \(Q_N\), so an exposing halfspace isolates it. Since every containing halfspace includes the atom at its center,
\[
\tau_{\pi_N}(\mathbf v)=\pi_{N,\mathbf v}=\frac1{N+2}
\quad(\mathbf v\ne\mathbf0).
\tag{39}
\]
The \(N+1\) simplex vertices have sum zero. Translating any halfspace containing the origin until its boundary passes through the origin only decreases its mass; for the translated halfspace, the vertex scores sum to zero, so at least one vertex lies in it. Therefore every containing halfspace contains the origin and at least one simplex vertex. The halfspace
\(\{\mathbf x:\mathbf1\cdot\mathbf x\le0\}\) contains exactly
\(\mathbf0\) and \(-\mathbf1\) from \(D_N\). This proves
\(\tau_{\pi_N}(\mathbf0)=2/(N+2)\), hence (7) and (8).

The uniform law on \(D_N\) has mean zero, as also recorded in
\(\mathrm{02a48d28569660b9}\). Thus for every tilt \(\mathbf a\), Jensen's inequality gives
\[
\sum_{\mathbf x\in D_N}\pi_{N,\mathbf x}e^{\mathbf a\cdot\mathbf x}
\ge e^{\mathbf a\cdot\mathbb E\mathbf X}=1,
\tag{40}
\]
with equality at \(\mathbf a=\mathbf0\). Hence
\(\mathsf C_{\pi_N}(\mathbf0)=1\). At any nonzero vertex \(\mathbf v\), the center term gives
\(\mathsf C_{\pi_N}(\mathbf v)\ge \pi_{N,\mathbf v}\). If \(\ell\) uniquely exposes \(\mathbf v\), substitute the tilt \(t\ell\) after normalizing so that
\(\ell(\mathbf x-\mathbf v)<0\) for every other support point, and let
\(t\to\infty\). All other terms vanish, proving
\(\mathsf C_{\pi_N}(\mathbf v)=\pi_{N,\mathbf v}=1/(N+2)\). This is consistent with the canonical boundary-capacity formula in
\(\mathrm{bf1ff94487296374}\) and proves (9). Summing the \(s\)-th powers gives (10).

For fixed \(s>1\), (10) gives
\[
\left(\sum \pi_{N,\mathbf z}\mathsf C_{\pi_N}(\mathbf z)^s\right)^{1/s}
\sim N^{-1/s},
\tag{41}
\]
because \((N+1)(N+2)^{-s}\to0\). For every fixed \(q>0\), (8) gives
\[
M_q(\pi_N)^{1/q}\sim N^{-1}.
\tag{42}
\]
Dividing (41) by (42) proves (11). Finally, (8) also gives
\(2^{qN}M_q(\pi_N)\to\infty\), so this averaged-capacity obstruction is not an Hq counterexample. Together with (5) and the locked-target calibration in
\(\mathrm{02a48d28569660b9}\), this confirms the limited route-obstruction interpretation stated above.

## External sources

none
