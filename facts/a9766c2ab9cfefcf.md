---
fact_id: a9766c2ab9cfefcf
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: optimized-marginal-depth-lifting-obstruction
depends_on: ["bb2b5f9519ae23e8","f049539ffd9c9b1d"]
verifier_run: 971b45586ce443fb
target_match: null
---

## Statement

For every integer \(d\geq1\), set
\(\varepsilon:=1/[2(d+1)]\), \(m:=[2(d+1)]^d\), and
\(n:=(d+1)m\). Let \(\mathbf e_1,\ldots,\mathbf e_n\) be the standard
basis of \(\mathbb R^n\). In \(\mathbb R^d\), let
\(\mathbf v_0:=\mathbf0\) and let \(\mathbf v_1,\ldots,\mathbf v_d\)
be the standard basis. Define the standard simplex
\(\Delta_d:=\operatorname{conv}\{\mathbf v_0,\ldots,\mathbf v_d\}\),
its centroid \(\mathbf x_*:=\mathfrak c(\Delta_d)
=(d+1)^{-1}\sum_{r=0}^d\mathbf v_r\), its volume
\(V:=\operatorname{vol}_d(\Delta_d)=1/d!\), and the canonical constant
\(\gamma_d:=(d/(d+1))^d\). Partition \(\{1,\ldots,n\}\) into
\(I_0,\ldots,I_d\), each of cardinality \(m\), and put
\(K_r:=(1-\varepsilon)\mathbf v_r+\varepsilon\Delta_d\). Consider
\[
C:=\operatorname{conv}\left(
 (\{\mathbf0\}\times\Delta_d)
 \ \cup\!
 \bigcup_{r=0}^d\ \bigcup_{i\in I_r}
 (\{\mathbf e_i,-\mathbf e_i\}\times K_r)
\right)\subseteq\mathbb R^{n+d}.
\]
This is a full-dimensional rational convex polytope, hence a convex body.
Use the locked problem's \(\Lambda:=\mathbb Z^n\times\mathbb R^d\),
\(S:=C\cap\Lambda\), and \(h_S\). For \(\mathbf z\in\mathbb Z^n\),
use the canonical fiber notation
\(C_{\mathbf z}:=\{\mathbf x:(\mathbf z,\mathbf x)\in C\}\),
\(w_{\mathbf z}:=\operatorname{vol}_d(C_{\mathbf z})\), with empty fibers
having volume zero, and \(W:=\sum_{\mathbf z}w_{\mathbf z}\). Define the
ambient finite Borel measure \(\mu_C(A):=\mathcal H_d(S\cap A)\) and the
weighted marginal depth, for \(\mathbf z_0\in\mathbb R^n\), by
\[
\tau(\mathbf z_0):=
\inf_{\substack{Q\subseteq\mathbb R^n\text{ a closed halfspace}\\
                 \mathbf z_0\in Q}}
\sum_{\mathbf z\in Q\cap\mathbb Z^n}w_{\mathbf z}.
\]
Thus the archived construction's \(h_C\) is \(h_S\) here, its base
variable \(\mathbf x\) is our \(\mathbf z\), its continuous variable
\(\mathbf y\) is our \(\mathbf x\), and its centroid \(\mathbf c\) is
our \(\mathbf x_*\). The symbols \(w_{\mathbf z},W,\gamma_d\) have the
same meanings as in accepted fact `bb2b5f9519ae23e8`.

The integer fibers and their total mass are exactly
\[
\begin{aligned}
C_{\mathbf0}&=\Delta_d, & w_{\mathbf0}&=V,\\
C_{\pm\mathbf e_i}&=K_r\quad(i\in I_r), &
w_{\pm\mathbf e_i}&=\varepsilon^dV,\\
C_{\mathbf z}&=\varnothing
\quad\bigl(\mathbf z\notin\{\mathbf0,\pm\mathbf e_1,\ldots,
\pm\mathbf e_n\}\bigr), & W&=(2d+3)V.
\end{aligned}
\]
The origin uniquely maximizes \(\tau\) over \(\mathbb R^n\), in particular
over all feasible integer bases, and
\(\tau(\mathbf0)=(d+2)V\), whereas
\(\tau(\pm\mathbf e_i)=\varepsilon^dV\).

The exact global optimal mixed-integer halfspace depth is
\[
\max_{\mathbf p\in S}h_S(\mathbf p)
=\max_{\mathbf x\in\Delta_d}h_S((\mathbf0,\mathbf x))
=h_S((\mathbf0,\mathbf x_*))
=(1+\gamma_d)V.
\]
Consequently the optimized lifting ratio and the weak Oertel ratio satisfy
\[
\begin{aligned}
\frac{\displaystyle\max_{\mathbf x\in C_{\mathbf0}}
                    h_S((\mathbf0,\mathbf x))}{\tau(\mathbf0)}
&=\frac{1+\gamma_d}{d+2}\longrightarrow0,\\
\frac{\displaystyle\max_{\mathbf p\in S}h_S(\mathbf p)}{2^{-n}W}
&=\frac{2^n(1+\gamma_d)}{2d+3}\longrightarrow\infty
\qquad(d\longrightarrow\infty).
\end{aligned}
\]
The latter ratio is greater than \(1\) for every \(d\geq1\). Therefore this
family satisfies the locked weak Oertel inequality for every permitted fixed
\(c_0\in(0,1/e)\).

## Proof

The simplex volume formula gives \(V=1/d!>0\). To check its stated
centroid, each permutation of its vertices defines an affine automorphism of
\(\Delta_d\). Such an automorphism preserves its uniform probability
measure: its constant absolute Jacobian is \(1\), since it maps the
simplex onto itself. The integrals of its \(d+1\) barycentric-coordinate
functions are therefore equal, and their sum is \(V\). Each mean
barycentric coordinate is \(1/(d+1)\), proving the formula for
\(\mathbf x_*\). The defining formulas also give
\(0<\varepsilon<1\), \(m\varepsilon^d=1\),
\(K_r\subseteq\Delta_d\), and
\(\operatorname{vol}_d(K_r)=\varepsilon^dV\).

Every set used to generate \(C\) is a polytope with rational vertices,
and there are finitely many such sets. Their convex hull is therefore a
compact rational convex polytope. Its base projection is
\(\operatorname{conv}\{\mathbf0,\pm\mathbf e_1,\ldots,
\pm\mathbf e_n\}=\{\mathbf z:\|\mathbf z\|_1\leq1\}\).
An integer vector in this projection is either \(\mathbf0\) or one of
\(\pm\mathbf e_i\), since the sum of its absolute integer coordinates is
at most \(1\).

All generating continuous coordinates lie in \(\Delta_d\), so
\(C\subseteq\mathbb R^n\times\Delta_d\). The inclusion
\(\{\mathbf0\}\times\Delta_d\subseteq C\) now proves
\(C_{\mathbf0}=\Delta_d\). Fix \(i\in I_r\) and a sign
\(\sigma\in\{1,-1\}\). The base functional
\(\mathbf z\mapsto\sigma z_i\) has maximum \(1\) on the projection
and attains it only at \(\sigma\mathbf e_i\). A convex combination of
generating points with base \(\sigma\mathbf e_i\) must consequently use
only points whose base is \(\sigma\mathbf e_i\). Their continuous
coordinates range over exactly the convex set \(K_r\), so
\(C_{\sigma\mathbf e_i}=K_r\). This proves all the asserted integer
fiber identities.

For completeness, \(C\) has full ambient dimension. It contains
\((\mathbf0,\mathbf v_0),\ldots,(\mathbf0,\mathbf v_d)\), and for
each \(i\in I_r\) it contains
\((\mathbf e_i,(1-\varepsilon)\mathbf v_r
                    +\varepsilon\mathbf v_0)\).
The \(n+d\) differences of the other points from
\((\mathbf0,\mathbf v_0)\) are linearly independent: their base
projections first force every coefficient of a point over
\(\mathbf e_i\) to vanish, after which the \(d\) standard vertical
basis vectors force the remaining coefficients to vanish. Thus \(C\)
has dimension \(n+d\) and nonempty interior. Its integer fibers give
\(W=V+2n\varepsilon^dV=(2d+3)V\).

Consider any proper base halfspace containing the origin, written
\(Q=\{\mathbf z:\mathbf a^\top\mathbf z\geq t\}\) with
\(\mathbf a\ne\mathbf0\) and \(t\leq0\). It contains the origin
and at least one point of every pair
\(\{\mathbf e_i,-\mathbf e_i\}\), because one of \(a_i,-a_i\)
is nonnegative. Hence its marginal mass is at least
\(V+n\varepsilon^dV=(d+2)V\). The particular halfspace
\(\{\mathbf z:\sum_{i=1}^n z_i\geq0\}\) contains the origin and
exactly one point of each pair, so it attains this bound. A convention
allowing the whole space as a halfspace does not change the infimum.
This proves \(\tau(\mathbf0)=(d+2)V\).

Every base halfspace containing \(\sigma\mathbf e_i\) has marginal
mass at least \(w_{\sigma\mathbf e_i}\), and the halfspace
\(\{\mathbf z:\sigma z_i\geq1\}\) contains exactly that one point
of the integer projection. Therefore
\(\tau(\sigma\mathbf e_i)=\varepsilon^dV\). More generally, for any
real \(\mathbf z_0\ne\mathbf0\), the halfspace
\(\{\mathbf z:\mathbf z_0^\top\mathbf z\geq
\|\mathbf z_0\|_2^2\}\) contains \(\mathbf z_0\), excludes the
origin, and contains at most one point of each antipodal pair. Thus
\(\tau(\mathbf z_0)\leq n\varepsilon^dV=(d+1)V
<(d+2)V=\tau(\mathbf0)\). This also proves the asserted uniqueness
over all real base points.

We next give an upper halfspace for every point of the central fiber. Let
\(\lambda_0(\mathbf x):=1-\sum_{j=1}^d x_j\) and
\(\lambda_r(\mathbf x):=x_r\) for \(1\leq r\leq d\); these are the
barycentric-coordinate functions of \(\Delta_d\). Given
\(\mathbf x\in\Delta_d\), choose \(\ell\) for which
\(s:=\lambda_\ell(\mathbf x)\geq1/(d+1)\). In particular
\(\varepsilon<s\leq1\). Define \(a_i:=2\) for \(i\in I_\ell\)
and \(a_i:=0\) for the other indices, and take the proper closed
ambient halfspace
\[
H_{\mathbf x}:=
\{(\mathbf z,\mathbf x'):
  \mathbf a^\top\mathbf z+\lambda_\ell(\mathbf x')\geq s\}.
\]
Its boundary contains \((\mathbf0,\mathbf x)\). For
\(\mathbf x'=(1-\varepsilon)\mathbf v_r
+\varepsilon\mathbf u\in K_r\) with \(\mathbf u\in\Delta_d\),
affineness of the barycentric functions gives
\(\lambda_\ell(\mathbf x')=(1-\varepsilon)\delta_{\ell r}
+\varepsilon\lambda_\ell(\mathbf u)\).
If \(r\ne\ell\), this is at most \(\varepsilon<s\), and the base
term is zero on both fibers with index in \(I_r\). All such fibers
are excluded. If \(i\in I_\ell\), the value on its positive fiber is
\(2+\lambda_\ell(\mathbf x')\geq2>s\), whereas the value on its
negative fiber is \(-2+\lambda_\ell(\mathbf x')\leq-1<s\).
Thus exactly the \(m\) positive fibers in this cluster contribute,
with total mass \(m\varepsilon^dV=V\).

The section in the central fiber is the simplex cap
\(\{\mathbf x'\in\Delta_d:\lambda_\ell(\mathbf x')\geq s\}
=s\mathbf v_\ell+(1-s)\Delta_d\). This identity follows by
subtracting \(s\) from the \(\ell\)-th barycentric coordinate and
dividing all the resulting coordinates by \(1-s\) when \(s<1\);
when \(s=1\), both sides are the single vertex \(\mathbf v_\ell\).
Its volume is \((1-s)^dV\). Consequently
\[
\mu_C(H_{\mathbf x})
=V+(1-s)^dV
\leq\left[1+\left(\frac d{d+1}\right)^d\right]V
=(1+\gamma_d)V.
\]
For any point of a noncentral integer fiber at
\(\sigma\mathbf e_i\), the ambient vertical halfspace
\(\{(\mathbf z,\mathbf x'):\sigma z_i\geq1\}\) contains that
point and has mixed mass \(\varepsilon^dV<(1+\gamma_d)V\).
These halfspaces establish the claimed upper bound at every point of
\(S\).

For the matching lower bound, set
\(\mathbf p_*:=(\mathbf0,\mathbf x_*)\), and let \(H\) be any
proper closed halfspace containing \(\mathbf p_*\). Write
\(H=\{(\mathbf z,\mathbf x):\mathbf a^\top\mathbf z
+\mathbf u^\top\mathbf x\geq t\}\), with
\((\mathbf a,\mathbf u)\ne(\mathbf0,\mathbf0)\).
Since \(t\leq\mathbf u^\top\mathbf x_*\), the halfspace
\[
H_0:=\{(\mathbf z,\mathbf x):
  \mathbf a^\top\mathbf z
  +\mathbf u^\top(\mathbf x-\mathbf x_*)\geq0\}
\]
has boundary through \(\mathbf p_*\) and is contained in \(H\).
It therefore suffices to lower-bound \(\mu_C(H_0)\). If
\(\mathbf u=\mathbf0\), then \(\mathbf a\ne\mathbf0\), and the
marginal-depth calculation gives
\(\mu_C(H_0)\geq(d+2)V\geq(1+\gamma_d)V\), since
\(0<\gamma_d\leq1\).

Suppose that \(\mathbf u\ne\mathbf0\), and define
\(t_r:=\mathbf u^\top(\mathbf v_r-\mathbf x_*)\) for
\(0\leq r\leq d\). Their sum is zero. They are not all zero,
because the differences \(\mathbf v_r-\mathbf v_0\) span
\(\mathbb R^d\). Choose \(\ell\) with
\(t_\ell=\max_r t_r>0\). For every \(r\), the equality
\(t_r=-\sum_{q\ne r}t_q\) implies \(t_r\geq-dt_\ell\).
Every \(\mathbf x\in K_\ell\) consequently satisfies
\[
\begin{aligned}
\mathbf u^\top(\mathbf x-\mathbf x_*)
&\geq(1-\varepsilon)t_\ell+\varepsilon\min_r t_r\\
&\geq[1-(d+1)\varepsilon]t_\ell
=\tfrac12t_\ell>0.
\end{aligned}
\]
For each \(i\in I_\ell\), choose a sign \(\sigma_i\) such that
\(\sigma_i a_i\geq0\). The whole fiber
\(\{\sigma_i\mathbf e_i\}\times K_\ell\) then lies strictly
inside \(H_0\). These \(m\) distinct fibers contribute at least
\(m\varepsilon^dV=V\).

The central section of \(H_0\) is the closed halfspace
\(\{\mathbf x:\mathbf u^\top(\mathbf x-\mathbf x_*)\geq0\}\)
through the centroid of the full-dimensional convex body \(\Delta_d\).
The Grünbaum inequality recorded and used in accepted fact
`bb2b5f9519ae23e8` states precisely that such a halfspace contains at
least \(\gamma_d\operatorname{vol}_d(\Delta_d)=\gamma_dV\) of its
volume. This is the only part of that predecessor consumed here; no affine
selector is being asserted for the present fibers. Summing the central
contribution and the \(m\) noncentral contributions proves
\(\mu_C(H_0)\geq(1+\gamma_d)V\), and hence the same bound for
\(H\). If the whole space is allowed as a halfspace, its mass is
\(W=(2d+3)V\), so that case also satisfies the bound.

At \(\mathbf x=\mathbf x_*\), every barycentric coordinate is
\(1/(d+1)\), so each of the upper halfspaces just constructed has
exact mass \((1+\gamma_d)V\). Together with the lower bound, this
proves \(h_S(\mathbf p_*)=(1+\gamma_d)V\) and the two claimed
maxima. All halfspaces used are closed. The noncentral inclusions and
exclusions in the upper construction are strict, and the central cap
formula is valid as a closed-set identity, including \(s=1\).

Dividing the exact maximum by \(\tau(\mathbf0)\) gives the first
stated ratio. Its value is positive and at most \(2/(d+2)\), which
tends to zero. Thus, for every proposed absolute \(\eta>0\), choose
an integer \(d\) with \(2/(d+2)<\eta\). For the constructed
\(n\) and \(C\), every point over the unique deepest marginal base
has depth strictly smaller than \(\eta\tau(\mathbf0)\). The global
upper bound proves that allowing a different integer base cannot achieve
\(\eta\max_{\mathbf z_0}\tau(\mathbf z_0)\) either.

To make the relationship with accepted fact `f049539ffd9c9b1d` precise,
its depth consequence is a lower bound \(\alpha M/e\) for a lift over
a base point whose closed marginal halfspaces all have mass at least
\(\alpha M\), under its log-concavity hypothesis on the ambient
measure. The attempted specialization here would be
\(\rho=\mu_C\), \(M=W\), \(P(\mathbf z,\mathbf x)=\mathbf z\),
\(\pi=P_\#\mu_C\), \(z_0=\mathbf0\), and
\(\alpha=\tau(\mathbf0)/W=(d+2)/(2d+3)\). These are the exact
normalization and alias maps to that predecessor. Its marginal hypothesis
holds, and dropping its log-concavity hypothesis would require a lift of
depth at least \(\tau(\mathbf0)/e\). The computed ratio tending to
zero disproves that extension. If the full selection conclusion were
retained, its selected barycenter would lie in \(C\), because its
measure is dominated by \(\mu_C\) and \(C\) is compact and convex;
the required base coordinate \(\mathbf0\) would put it in the
central integer fiber. Thus the same contradiction would apply.

There is no contradiction with the accepted theorem itself. In fact
\(\mu_C\) is not log-concave: choose any \(i\in I_r\), and take
\(A:=\{\mathbf0\}\times\Delta_d\) and
\(B:=\{\mathbf e_i\}\times K_r\). Then
\(\mu_C(A)=V>0\) and \(\mu_C(B)=\varepsilon^dV>0\), whereas
\((A+B)/2\) has the noninteger base coordinate
\(\mathbf e_i/2\) and therefore has \(\mu_C\)-mass zero. This
violates the midpoint inequality required for a log-concave measure.

Finally, division by \(2^{-n}W\) gives the stated weak Oertel ratio.
Since \(m\geq2\), one has \(n\geq d+2\), and
\(2^{d+2}\geq2d+4>2d+3\). The ratio is thus greater than \(1\)
for every \(d\). Also \(n\geq d+1\) gives the lower bound
\(2^{d+1}/(2d+3)\), which tends to infinity: for example,
\(2^{d+1}\geq\binom{d+1}{2}=d(d+1)/2\).
In particular the explicit point \(\mathbf p_*\) satisfies
\(h_S(\mathbf p_*)\geq c_0 2^{-n}W\) for every
\(c_0\in(0,1/e)\). The obstruction concerns a fixed fraction of
maximum marginal depth, and leaves the locked conjecture unresolved.

## External sources

None beyond the declared accepted predecessors. Every property of the
constructed body and every new comparison is proved above.
