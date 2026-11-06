---
fact_id: eced63cdad9e2b07
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: pooled-body-randomized-reflection-aggregation
depends_on: ["2d4c7439acb19da3","6d6fcf377e68c79c","c2ed1a4e6f4a7c4d"]
verifier_run: b5045d3f3b384a55
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let
\(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and put
\[
 \Lambda:=\mathbb Z^n\times\mathbb R^d,
 \qquad S:=C\cap\Lambda\ne\varnothing.
\]
Let \(\mu_C\) be its mixed-volume measure, and write
\[
 h_{\max}(C):=
 \sup_{y\in S}\inf\{\mu_C(H):H\text{ is a closed halfspace and }y\in H\}.
\tag{1}
\]
For finite Borel measures, write \(\sigma\preceq_{\mathrm{hs}}\mu_C\) when
\(\sigma(H)\leq\mu_C(H)\) for every closed halfspace \(H\).

Let \(I\) be a finite nonempty set.  For each \(i\in I\), let
\[
 m_i\in\mathbb Z^n,
 \qquad \varnothing\ne K_i\subseteq C_{m_i}
 \quad\text{be compact},
 \qquad c_i>0.
\]
Assume the all-selection domination property
\[
 \boxed{
 \sum_{i\in I}c_i\delta_{(m_i,x_i)}
 \preceq_{\mathrm{hs}}\mu_C
 \quad\text{for every simultaneous choice }x_i\in K_i.}
\tag{2}
\]
Choose arbitrary Borel probability measures \(\nu_i\) supported on \(K_i\),
let \(\iota_i(x):=(m_i,x)\), and define
\[
 \tau:=\sum_{i\in I}c_i(\iota_i)_\#\nu_i.
\tag{3}
\]
Fix an affine map \(s:\mathbb R^n\to\mathbb R^d\).  For
\(\xi\in(\mathbb Z/2\mathbb Z)^n\), let \(\tau_\xi\) be the part of
\(\tau\) on bases congruent to \(\xi\), and put
\[
 T_s(m,x):=x-s(m),
 \qquad \lambda_{\xi,s}:=(T_s)_\#\tau_\xi,
 \qquad \check\lambda_{\xi,s}(A):=\lambda_{\xi,s}(-A).
\tag{4}
\]
If \(\alpha,\beta\) are finite nonnegative measures, denote by
\(\alpha\wedge\beta\) their greatest common submeasure.  Set
\[
 \eta_{\xi,s}:=\lambda_{\xi,s}\wedge\check\lambda_{\xi,s},
 \qquad
 \mathfrak R_\tau(s):=\frac12\sum_\xi|\eta_{\xi,s}|.
\tag{5}
\]
Then there is a finite nonnegative Borel measure \(\rho_s\) supported on
\[
 C\cap\{(m,s(m)):m\in\mathbb Z^n\}
\]
such that
\[
 \boxed{\rho_s\preceq_{\mathrm{hs}}\mu_C,
 \qquad |\rho_s|=\mathfrak R_\tau(s).}
\tag{6}
\]
Consequently,
\[
 \boxed{h_{\max}(C)\geq2^{-n}\mathfrak R_\tau(s).}
\tag{7}
\]
This remains valid when \(\mathfrak R_\tau(s)=0\).

For a finite signed measure \(\sigma\), use the convention
\(\|\sigma\|_{\mathrm{var}}:=|\sigma|(\mathbb R^d)\), with no extra factor
of \(1/2\).  The exact overlap identity is
\[
 \boxed{
 \mathfrak R_\tau(s)
 =\frac{|\tau|}{2}
 -\frac14\sum_\xi
 \|\lambda_{\xi,s}-\check\lambda_{\xi,s}\|_{\mathrm{var}}.}
\tag{8}
\]

Now retain the complete canonical pooled switch-body system from accepted
fact `2d4c7439acb19da3`.  Thus
\[
 E_{\mathrm{sw}}=\{m:\eta_m>0\},
 \qquad
 \mathcal P_m^{\mathrm{sw}}
 =\frac1{\eta_m}\sum_{j\in I_m}q_j^{\mathrm{sat}}L_j,
 \qquad
 \Omega_b=\sum_{m\in E_{\mathrm{sw}}}\eta_m>\frac{97}{100}Q,
\tag{9}
\]
and, with
\[
 \gamma_d:=\left(\frac d{d+1}\right)^d,
 \qquad c_m:=\gamma_d\eta_m,
 \qquad D:=2^nh_{\max}(C),
\tag{10}
\]
every simultaneous selection \(x_m\in\mathcal P_m^{\mathrm{sw}}\) satisfies
\[
 \sum_{m\in E_{\mathrm{sw}}}c_m\delta_{(m,x_m)}
 \preceq_{\mathrm{hs}}\mu_C.
\tag{11}
\]
For arbitrary probability laws
\(\nu_m\in\mathcal P(\mathcal P_m^{\mathrm{sw}})\), use (3)-(5) with the
exact aliases
\[
 I=E_{\mathrm{sw}},
 \qquad K_m=\mathcal P_m^{\mathrm{sw}},
 \qquad c_m=\gamma_d\eta_m.
\tag{12}
\]
Then, for every affine \(s\),
\[
 \boxed{D\geq\mathfrak R_\tau(s)}
\tag{13}
\]
and (8) holds with \(|\tau|=\gamma_d\Omega_b\).

There is an exact finite matching form of (13).  Give
\(E_{\mathrm{sw}}\) any fixed total order.  For distinct \(m,m'\) of the
same parity, put an edge \(\{m,m'\}\) in \(G_s\) precisely when
\[
 s\left(\frac{m+m'}2\right)
 \in\frac{\mathcal P_m^{\mathrm{sw}}+
              \mathcal P_{m'}^{\mathrm{sw}}}{2}.
\tag{14}
\]
Put a loop at \(m\) precisely when
\[
 s(m)\in\mathcal P_m^{\mathrm{sw}}.
\tag{15}
\]
Define
\[
 \begin{aligned}
 \mathsf M_s:=\max\quad&
 \sum_{\substack{m<m'\\\{m,m'\}\in E(G_s)}}t_{mm'}
 +\sum_{\substack{m\\\{m,m\}\in E(G_s)}}t_{mm}\\
 \text{subject to}\quad&
 \sum_{\substack{m'\ne m\\\{m,m'\}\in E(G_s)}}t_{mm'}+2t_{mm}
 \leq c_m\quad(m\in E_{\mathrm{sw}}),\\
 &t_{mm'}\geq0,
 \end{aligned}
\tag{16}
\]
where an absent loop has \(t_{mm}:=0\).  Then
\[
 \boxed{
 \mathsf M_s
 =\sup_{\nu_m\in\mathcal P(\mathcal P_m^{\mathrm{sw}})}
 \mathfrak R_\tau(s)
 =\frac{\gamma_d\Omega_b}{2}
 -\frac14\inf_{\{\nu_m\}}
 \sum_\xi
 \|\lambda_{\xi,s}-\check\lambda_{\xi,s}\|_{\mathrm{var}},}
\tag{17}
\]
and both extrema over the laws are attained by finitely supported laws.
In particular,
\[
 \boxed{D\geq\mathsf M_s.}
\tag{18}
\]

The canonical hard ledger in `2d4c7439acb19da3` gives
\[
 D+R_{\mathrm{sel}}(C)<\frac Q{100}.
\tag{19}
\]
Hence, for every affine \(s\), there is a set
\(U_s\subseteq E_{\mathrm{sw}}\) such that
\[
 \boxed{
 \sum_{m\in U_s}c_m>\frac{91}{300}Q,}
\tag{20}
\]
\[
 \boxed{s(m)\notin\mathcal P_m^{\mathrm{sw}}
 \quad(m\in U_s),}
\tag{21}
\]
and, for all distinct same-parity \(m,m'\in U_s\),
\[
 \boxed{
 s\left(\frac{m+m'}2\right)
 \notin
 \frac{\mathcal P_m^{\mathrm{sw}}+
       \mathcal P_{m'}^{\mathrm{sw}}}{2}.}
\tag{22}
\]
Thus \(U_s\) is loopless and pairwise reflection-incompatible in \(G_s\).
Also, for every choice of the laws in (12),
\[
 \boxed{
 \sum_\xi
 \|\lambda_{\xi,s}-\check\lambda_{\xi,s}\|_{\mathrm{var}}
 >\frac{91}{150}Q.}
\tag{23}
\]

## Proof

First fix a closed halfspace \(H\).  Property (2) gives
\[
 \sum_i c_i\mathbf1_H(m_i,x_i)\leq\mu_C(H)
\]
for every point of \(\prod_iK_i\).  Integrating this inequality against the
finite product probability measure \(\bigotimes_i\nu_i\), and using Tonelli,
gives
\[
 \tau(H)=\sum_i c_i\int_{K_i}\mathbf1_H(m_i,x)\,d\nu_i(x)
 \leq\mu_C(H).
\tag{24}
\]
Therefore
\[
 \tau\preceq_{\mathrm{hs}}\mu_C.
\tag{25}
\]
This is the only passage from deterministic all-selection domination to a
randomized cloud.

We next construct the reflected endpoint coupling.  Fix a parity class
\(\xi\), abbreviate \(\lambda=\lambda_{\xi,s}\), and set
\(\eta=\lambda\wedge\check\lambda\).  Reflection exchanges the two
arguments of the common part, so
\[
 \check\eta=\check\lambda\wedge\lambda=\eta.
\tag{26}
\]
If \(|\eta|=0\), define \(\Pi_\xi:=0\).  Suppose \(|\eta|>0\).  Since
\(\eta\leq\lambda\), let
\[
 h_\xi:=\frac{d\eta}{d\lambda},
 \qquad 0\leq h_\xi\leq1,
\]
and define a submeasure of \(\tau_\xi\) by
\[
 d\bar\tau_\xi(p):=h_\xi(T_s(p))\,d\tau_\xi(p).
\tag{27}
\]
Then
\[
 \bar\tau_\xi\leq\tau_\xi,
 \qquad (T_s)_\#\bar\tau_\xi=\eta.
\tag{28}
\]

The endpoint space is a finite union of compact subsets of Euclidean space,
hence is standard Borel.  Disintegrate \(\bar\tau_\xi\) with respect to
\(T_s\).  There is an \(\eta\)-measurable probability kernel
\(u\mapsto\kappa_{\xi,u}\) such that
\[
 \bar\tau_\xi(B)
 =\int\kappa_{\xi,u}(B)\,d\eta(u),
 \qquad
 \kappa_{\xi,u}(T_s^{-1}\{u\})=1
 \quad\text{for \(\eta\)-almost every }u.
\tag{29}
\]
Modify the kernel arbitrarily on the null exceptional set.  By symmetry of
\(\eta\), both the fiber assertion at \(u\) and the one at \(-u\) then hold
for almost every integration parameter.  The map
\(u\mapsto\kappa_{\xi,u}\otimes\kappa_{\xi,-u}\) is a measurable probability
kernel on the product endpoint space.  Define
\[
 \Pi_\xi
 :=\frac12\int
 \kappa_{\xi,u}\otimes\kappa_{\xi,-u}\,d\eta(u).
\tag{30}
\]
For every bounded Borel \(f\), (29), the change of variable \(u\mapsto-u\),
and (26) give
\[
 \int f(p)\,d(\pi_1)_\#\Pi_\xi(p)
 =\frac12\int f\,d\bar\tau_\xi,
 \qquad
 \int f(q)\,d(\pi_2)_\#\Pi_\xi(q)
 =\frac12\int f\,d\bar\tau_\xi.
\tag{31}
\]
Consequently,
\[
 (\pi_1)_\#\Pi_\xi+(\pi_2)_\#\Pi_\xi
 =\bar\tau_\xi\leq\tau_\xi,
 \qquad
 |\Pi_\xi|=\frac12|\eta_{\xi,s}|.
\tag{32}
\]
At \(u=0\), (30) uses
\(\frac12\kappa_{\xi,0}\otimes\kappa_{\xi,0}\).  Thus zero-deviation
pairs, diagonal endpoint pairs, and coincident endpoints consume the two
endpoint marginals with total coefficient one, not two.  Formula (32) also
covers a parity class with zero overlap by the preceding definition.

Put \(M(p,q):=(p+q)/2\) and
\[
 \rho_s:=M_\#\left(\sum_\xi\Pi_\xi\right).
\tag{33}
\]
For almost every paired endpoint
\(p=(m,x)\), \(q=(m',x')\), the two bases have parity \(\xi\), and for some
\(u\),
\[
 x=s(m)+u,
 \qquad x'=s(m')-u.
\]
Hence
\[
 \frac{m+m'}2\in\mathbb Z^n,
 \qquad
 \frac{x+x'}2=s\left(\frac{m+m'}2\right).
\tag{34}
\]
Both endpoints belong to \(C\), so their midpoint belongs to \(C\) by
convexity.  This proves the support assertion in (6), including exact parity
integrality.  Also, pushforward preserves mass, so (5), (32), and (33) give
\[
 |\rho_s|=\sum_\xi|\Pi_\xi|=\mathfrak R_\tau(s).
\tag{35}
\]

The remaining midpoint and graph-centerpoint argument is the same mechanism
as in accepted fact `c2ed1a4e6f4a7c4d`; we record the hypotheses explicitly.
If a midpoint lies in a proper closed halfspace \(H=\{\ell\geq0\}\), then
\(\ell(p)+\ell(q)\geq0\), so at least one endpoint lies in \(H\).  The whole
space case is immediate.  Therefore (25) and (32) imply
\[
 \rho_s(H)
 \leq\sum_\xi\bigl((\pi_1)_\#\Pi_\xi(H)
                    +(\pi_2)_\#\Pi_\xi(H)\bigr)
 \leq\tau(H)\leq\mu_C(H).
\tag{36}
\]
This proves (6), with closed-halfspace boundary points retained.

If \(\mathfrak R_\tau(s)=0\), inequality (7) follows from
\(h_{\max}(C)\geq0\).  Suppose it is positive, and let
\(L_s(m):=(m,s(m))\) and
\(\zeta:=(\operatorname{pr}_{\mathbb R^n})_\#\rho_s\).  Then
\(\rho_s=(L_s)_\#\zeta\), and \(\zeta\) is a nonzero finite measure of mass
\(\mathfrak R_\tau(s)\) supported on \(\mathbb Z^n\).  Apply accepted fact
`6d6fcf377e68c79c` with continuous dimension zero.  It gives
\(m_0\in\mathbb Z^n\) such that every closed base halfspace \(J\ni m_0\)
satisfies
\[
 \zeta(J)\geq2^{-n}\mathfrak R_\tau(s).
\tag{37}
\]
If \(m_0\notin\operatorname{conv}(\operatorname{supp}\zeta)\), strict
separation supplies such a \(J\) disjoint from the support, contradicting
(37).  Hence
\[
 L_s(m_0)\in
 \operatorname{conv}(L_s(\operatorname{supp}\zeta))\subseteq C.
\]
It also has integral base, so it lies in \(S\).  Pulling any ambient closed
halfspace through \(L_s(m_0)\) back under \(L_s\), and using (36)-(37), proves
(7).

For completeness, let \(\theta:=\lambda+\check\lambda\), and write
\(f=d\lambda/d\theta\) and \(g=d\check\lambda/d\theta\).  Then
\(\lambda\wedge\check\lambda\) has density \(\min\{f,g\}\), while the
total variation of \(\lambda-\check\lambda\) has density \(|f-g|\).  Since
\(|\lambda|=|\check\lambda|\),
\[
 |\lambda\wedge\check\lambda|
 =|\lambda|-\frac12\|\lambda-\check\lambda\|_{\mathrm{var}}.
\tag{38}
\]
Summing (38) over the parity partition and multiplying by \(1/2\) proves
(8), including empty parity classes.

We now specialize.  Accepted fact `2d4c7439acb19da3`, equations (12)-(13)
and (29)-(30), proves exactly (11) for every independent simultaneous pooled
selection.  Thus (2) holds under the aliases (12).  Equations (7)-(8), after
multiplication by \(2^n\), prove (13) and its asserted normalization.

We prove the exact matching identity (17) in both directions.  First fix any
laws \(\{\nu_m\}\), and use the pair measures (30).  Partition each
\(\Pi_\xi\) according to the unordered pair of its two integral bases.  For
a distinct pair \(\{m,m'\}\), let \(t_{mm'}\) be the mass of both possible
base orders together, and for a repeated base let
\(t_{mm}:=\Pi_\xi(\{(p,q):\operatorname{base}(p)
=\operatorname{base}(q)=m\})\).  The marginal identity (32) gives
\[
 \sum_{m'\ne m}t_{mm'}+2t_{mm}
 \leq\tau(\{m\}\times\mathbb R^d)=c_m.
\tag{39}
\]
If \(t_{mm'}>0\) for \(m\ne m'\), the support of (30) supplies points
\(x\in\mathcal P_m^{\mathrm{sw}}\) and
\(y\in\mathcal P_{m'}^{\mathrm{sw}}\) with opposite deviations.  Affinity
of \(s\) gives (14), and the parity is already common.  If \(t_{mm}>0\),
the two paired points \(x,y\in\mathcal P_m^{\mathrm{sw}}\) have midpoint
\(s(m)\).  The pooled body is convex by its Minkowski definition in (9), so
\(s(m)\in\mathcal P_m^{\mathrm{sw}}\), which is the loop condition (15).
Thus \(t\) is feasible in (16), and its objective is
\[
 \sum_{m<m'}t_{mm'}+\sum_mt_{mm}
 =\sum_\xi|\Pi_\xi|=\mathfrak R_\tau(s).
\tag{40}
\]
It follows that every family of laws satisfies
\(\mathfrak R_\tau(s)\leq\mathsf M_s\).  This includes zero overlap and
loops without a separate convention beyond the coefficient two in (39).

Conversely, take any feasible matching \(t\).  For every nonloop edge
\(e=\{m,m'\}\), choose witnesses
\(x_{m,e}\in\mathcal P_m^{\mathrm{sw}}\) and
\(x_{m',e}\in\mathcal P_{m'}^{\mathrm{sw}}\) with opposite deviations, as
guaranteed by (14).  At vertex \(m\), put mass \(t_e/c_m\) at
\(x_{m,e}\) for every incident nonloop edge and, when there is a loop, put
mass \(2t_{mm}/c_m\) at \(s(m)\).  By (16) this is a subprobability measure;
complete it to a probability measure by placing the remaining mass at any
point of the nonempty pooled body.

For each parity class, the resulting deviation measure
\(\lambda_{\xi,s}\) contains the symmetric submeasure
\[
 \omega_\xi
 :=\sum_{\substack{e=\{m,m'\}\text{ nonloop}\\m\equiv m'\equiv\xi}}
 t_e(\delta_{u_e}+\delta_{-u_e})
 +\sum_{\substack{m\equiv\xi\\\{m,m\}\in E(G_s)}}
 2t_{mm}\delta_0,
\tag{41}
\]
where \(u_e=x_{m,e}-s(m)\) for either fixed orientation of \(e\).
Coincident witnesses and coincident deviations simply add their positive
atomic masses.  Since \(\omega_\xi=\check\omega_\xi\) and
\(\omega_\xi\leq\lambda_{\xi,s}\), it is also at most
\(\check\lambda_{\xi,s}\), and hence
\(\omega_\xi\leq\eta_{\xi,s}\).  Therefore
\[
 \mathfrak R_\tau(s)
 \geq\frac12\sum_\xi|\omega_\xi|
 =\sum_{m<m'}t_{mm'}+\sum_mt_{mm}.
\tag{42}
\]
The finite linear program (16) attains its optimum.  Choosing an optimal
\(t\) in this construction, and combining (40)-(42), proves the first
equality in (17), with finitely supported optimizing laws.  The second
equality follows from (8) because \(|\tau|=\sum_mc_m=\gamma_d\Omega_b\).
Finally, (13) and (17) prove (18).

It remains to derive the hard-branch consequences.  The dual of (16) is
\[
 \begin{aligned}
 \min\quad&\sum_mc_my_m\\
 \text{subject to}\quad&y_m+y_{m'}\geq1
 &&(\{m,m'\}\text{ a nonloop edge}),\\
 &2y_m\geq1&&(\{m,m\}\text{ a loop}),\\
 &y_m\geq0.
 \end{aligned}
\tag{43}
\]
By finite-dimensional linear-programming duality, (18)-(19), and
\(R_{\mathrm{sel}}(C)\geq0\), it has an optimal solution with
\[
 \sum_mc_my_m=\mathsf M_s\leq D<\frac Q{100}.
\tag{44}
\]
Define
\[
 U_s:=\{m:y_m<1/2\}.
\tag{45}
\]
The loop constraints in (43) exclude every loop from \(U_s\), and the edge
constraints exclude every nonloop edge with both ends in \(U_s\).  This
proves (21)-(22).  Moreover,
\[
 \sum_{m\notin U_s}c_m
 \leq2\sum_mc_my_m<\frac Q{50}.
\tag{46}
\]
The elementary binomial bound
\((1+1/d)^d<\sum_{k\geq0}1/k!<3\) gives \(\gamma_d>1/3\).  Hence (9)-(10)
give
\[
 \sum_mc_m=\gamma_d\Omega_b>\frac{97}{300}Q.
\tag{47}
\]
Subtracting (46) from (47) proves (20).

For arbitrary laws, (13) and (19) give
\(\mathfrak R_\tau(s)<Q/100\).  Solving (8) for the variation sum, then
using (9), \(\gamma_d>1/3\), and the strict overlap bound, gives
\[
 \begin{aligned}
 \sum_\xi
 \|\lambda_{\xi,s}-\check\lambda_{\xi,s}\|_{\mathrm{var}}
 &=2\gamma_d\Omega_b-4\mathfrak R_\tau(s)\\
 &>2\left(\frac13\right)\left(\frac{97}{100}Q\right)
   -\frac4{100}Q
 =\frac{91}{150}Q,
 \end{aligned}
\]
which proves (23).

The conclusion stops at the reflection-incompatible set \(U_s\).  Missing
loops and edges do not themselves construct a halfspace-dominated
off-graph selector, do not establish admissibility of any
\(M_{\mathrm{off}}\), and do not charge the mass in (20) to \(G\), \(D\),
\(R_{\mathrm{sel}}(C)\), or another terminal ledger.  No absorption or
branch closure follows from this packet.

## External sources

none
