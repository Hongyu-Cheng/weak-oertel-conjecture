---
fact_id: dcca4b6d66d80dd4
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: zero-fresh-joint-diagonal-floor-packing
depends_on: ["10f1feebe06e22d0","39fdc9bb7abafc70","84560e8f5a46460c","e3666a74247dd6fd"]
verifier_run: 7bd6192c07bb43a9
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body of positive mixed volume, and write
\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
 \qquad
 a_z:=\operatorname{vol}_d(C_z).
\]
For \(0<t\leq a_z\), put
\[
 \mathsf M_t(C_z):=
 \left\{
 \frac1t\int_{C_z}x f(x)\,dx:
 0\leq f\leq1\ \text{a.e.},\quad
 \int_{C_z}f=t
 \right\},
 \qquad
 \mathcal K_z:=\mathsf M_{a_z/2}(C_z).
\tag{1}
\]
For every nonempty compact convex \(K\subseteq\mathbb R^d\), write
\[
 h_K(u):=\max_{x\in K}\langle u,x\rangle,
 \qquad
 F_K(u):=\{x\in K:\langle u,x\rangle=h_K(u)\}.
\]

Retain one common canonical zero-fresh hard system of accepted facts
`39fdc9bb7abafc70`, `84560e8f5a46460c`, and `e3666a74247dd6fd`.
Thus \(Q>0\), the label set \(I\) and circuit set \(\mathscr A\) are finite
and nonempty, and every \(j\in I\) has two distinct source fibers
\(z_j^-\), \(z_j^+\), an integral target
\[
 m_j:=\frac{z_j^-+z_j^+}{2},
\]
and a pair body
\[
 L_j:=\frac12(\mathcal K_{z_j^-}+\mathcal K_{z_j^+})
 \subseteq\mathsf M_{\vartheta_j}(C_{m_j})
 \quad\text{for some }\vartheta_j>0.
\tag{2}
\]
There are positive saturated loads \(q_j^{\mathrm{sat}}\), nonnegative
circuit loads \(q_j^\alpha\), and nonzero directions \(u_i\in\mathbb R^d\)
such that
\[
 \sum_{\alpha\in\mathscr A}q_j^\alpha=q_j^{\mathrm{sat}},
 \qquad
 \Omega_b:=\sum_jq_j^{\mathrm{sat}}>\frac{97}{100}Q,
\tag{3}
\]
\[
 \sum_{j:m_j=m}\frac{q_j^{\mathrm{sat}}}{\vartheta_j}\leq1
 \qquad(m\in\mathbb Z^n).
\tag{4}
\]
For \(\alpha\in\mathscr A\), put
\[
 \Omega_\alpha:=\sum_jq_j^\alpha>0,
 \qquad
 \pi_i^\alpha:=\frac{q_i^\alpha}{\Omega_\alpha},
\tag{5}
\]
Then
\[
 \sum_i\pi_i^\alpha=1,
 \qquad
 \sum_\alpha\Omega_\alpha=\Omega_b.
\]
For every source \(z\), define
\[
 \beta_z^\alpha:=\sum_jq_j^\alpha
 \bigl(\mathbf1_{\{z_j^-=z\}}+\mathbf1_{\{z_j^+=z\}}\bigr),
 \qquad
 \beta_z:=\sum_\alpha\beta_z^\alpha.
\tag{6}
\]
The simultaneous endpoint budget and exact total load are
\[
 \beta_z\leq\frac{a_z}{4},
 \qquad
 \sum_z\beta_z=2\Omega_b.
\tag{7}
\]

For every \(z\) with \(\beta_z>0\) and every \(i\in I\), retain the actual
half-cap \(A_z(u_i)\subseteq C_z\), of volume \(a_z/2\), and its barycenter
\[
 p_z(u_i):=\frac2{a_z}\int_{A_z(u_i)}x\,dx
 \in F_{\mathcal K_z}(u_i).
\tag{8}
\]
For \(\beta_z^\alpha>0\), define the weighted Minkowski body
\[
 \mathscr B_{\alpha,z}
 :=\sum_{i,k}\pi_i^\alpha\pi_k^\alpha
 [p_z(u_i),p_z(u_k)],
\tag{9}
\]
and, for \(\beta_z>0\), define
\[
 \mathscr B_z
 :=\frac1{\beta_z}
 \sum_{\alpha:\beta_z^\alpha>0}
 \beta_z^\alpha\mathscr B_{\alpha,z}.
\tag{10}
\]
Then every used source satisfies the exact inclusion
\[
 \boxed{\mathscr B_z\subseteq
 \mathsf M_{\beta_z/4}(C_z).}
\tag{11}
\]

There is a simultaneous compatible contact choice
\[
 p_{ij}:=\frac12
 \bigl(p_{z_j^-}(u_i)+p_{z_j^+}(u_i)\bigr)
 \in F_{L_j}(u_i),
 \qquad
 \ell_i:=p_{ii}.
\tag{12}
\]
For every family of synchronous parameters
\[
 \lambda_{\alpha,j,i,k}\in[0,1]
 \qquad(\alpha\in\mathscr A,\ j,i,k\in I),
\tag{13}
\]
define the two source points and their target midpoint by
\[
 x_{\alpha,j,i,k}^{\pm}
 :=(1-\lambda_{\alpha,j,i,k})p_{z_j^\pm}(u_i)
 +\lambda_{\alpha,j,i,k}p_{z_j^\pm}(u_k),
\tag{14}
\]
\[
 y_{\alpha,j,i,k}
 :=\frac{x_{\alpha,j,i,k}^-+x_{\alpha,j,i,k}^+}{2}
 =(1-\lambda_{\alpha,j,i,k})p_{ij}
 +\lambda_{\alpha,j,i,k}p_{kj}
 \in L_j.
\tag{15}
\]
Give each source occurrence in (14) weight
\[
 s_{\alpha,j,i,k}
 :=\frac{q_j^\alpha\pi_i^\alpha\pi_k^\alpha}{4}
\tag{16}
\]
and give the paired target point in (15) weight
\[
 w_{\alpha,j,i,k}:=2s_{\alpha,j,i,k}
 =\frac{q_j^\alpha\pi_i^\alpha\pi_k^\alpha}{2}.
\tag{17}
\]
These weights preserve every source occurrence exactly: for all
\(\alpha,z,i,k\),
\[
 \boxed{
 \sum_{\substack{j,\sigma\in\{-,+\}\\z_j^\sigma=z}}
 s_{\alpha,j,i,k}
 =\frac{\beta_z^\alpha\pi_i^\alpha\pi_k^\alpha}{4}.}
\tag{18}
\]

For every positive \(w_{\alpha,j,i,k}\), there is a density
\(g_{\alpha,j,i,k}\) supported on \(C_{m_j}\), of mass
\(w_{\alpha,j,i,k}\) and barycenter \(y_{\alpha,j,i,k}\), such that at
every physical target
\[
 \boxed{
 0\leq
 \sum_\alpha\sum_{j:m_j=m}\sum_{i,k}g_{\alpha,j,i,k}
 \leq
 \frac12\left(
 \sum_{j:m_j=m}\frac{q_j^{\mathrm{sat}}}{\vartheta_j}
 \right)\mathbf1_{C_m}
 \leq\frac12\mathbf1_{C_m}.}
\tag{19}
\]
Zero-weight terms use the zero density. Thus this is one atomwise joint
physical-target packing, not a collection of separately feasible target
families.

For a used target, put
\[
 \eta_m:=\sum_{j:m_j=m}q_j^{\mathrm{sat}},
 \qquad
 c_{\alpha j}:=\sum_i\pi_i^\alpha p_{ij},
\tag{20}
\]
\[
 c_m^{\mathrm{circ}}
 :=\frac1{\eta_m}
 \sum_\alpha\sum_{j:m_j=m}q_j^\alpha c_{\alpha j},
\tag{21}
\]
\[
 \widetilde g_{\alpha,i,k}^{(j,m)}
 :=\frac{q_j^\alpha}{2\eta_m}
 \pi_i^\alpha\pi_k^\alpha(p_{ij}-p_{kj}),
\tag{22}
\]
and
\[
 \widetilde{\mathcal Z}_m^{\mathrm{circ}}
 :=c_m^{\mathrm{circ}}
 +\sum_\alpha\sum_{j:m_j=m}\sum_{i,k}
 [-\widetilde g_{\alpha,i,k}^{(j,m)},
   \widetilde g_{\alpha,i,k}^{(j,m)}].
\tag{23}
\]
The joint density in (19) has mass \(\eta_m/2\), and its normalized
barycenter
\[
 x_m:=\frac2{\eta_m}
 \sum_\alpha\sum_{j:m_j=m}\sum_{i,k}
 w_{\alpha,j,i,k}y_{\alpha,j,i,k}
\tag{24}
\]
satisfies
\[
 \boxed{x_m\in\widetilde{\mathcal Z}_m^{\mathrm{circ}}
 \cap\mathsf M_{\eta_m/2}(C_m).}
\tag{25}
\]
The total mass of the source cloud and of its target transport is
\[
 2\sum_{\alpha,j,i,k}s_{\alpha,j,i,k}
 =
 \sum_{\alpha,j,i,k}w_{\alpha,j,i,k}
 =\frac{\Omega_b}{2}.
\tag{26}
\]

The diagonal terms are fixed under every synchronous choice:
\[
 x_{\alpha,j,i,i}^{\pm}=p_{z_j^\pm}(u_i),
 \qquad
 y_{\alpha,j,i,i}=p_{ij}.
\tag{27}
\]
Their total transported mass is exactly
\[
 \boxed{
 \sum_{\alpha,j,i}w_{\alpha,j,i,i}
 =\frac12\sum_\alpha\Omega_\alpha
   \sum_i(\pi_i^\alpha)^2
 =:F_{\mathrm{diag}}.}
\tag{28}
\]

Let \(G\) be the global complete metronoid-core capacity in accepted fact
`10f1feebe06e22d0`. For every affine map
\(a:\mathbb R^n\to\mathbb R^d\), define
\[
 A(a):=\{z:\beta_z>0,\ a(z)\in\mathscr B_z\},
 \qquad
 T(a):=\frac14\sum_{z\in A(a)}\beta_z.
\tag{29}
\]
Then
\[
 T(a)\geq\frac Q{100}
 \quad\Longrightarrow\quad
 G\geq T(a)\geq\frac Q{100}.
\tag{30}
\]

Assume now that no affine map has \(T(a)\geq Q/100\). Fix any affine
map \(a\), put \(A:=A(a)\), and define the labels with two non-hit
endpoints by
\[
 J_N:=\{j:z_j^-\notin A,\ z_j^+\notin A\},
 \qquad
 \Omega_N:=\sum_{j\in J_N}q_j^{\mathrm{sat}}.
\tag{31}
\]
Then, for every such affine map,
\[
 \boxed{\Omega_N>\frac{93}{100}Q,
 \qquad
 \frac{\Omega_N}{2}>\frac{93}{200}Q.}
\tag{32}
\]
The restriction of the densities in (19) to \(j\in J_N\) remains one
joint target packing and has total mass \(\Omega_N/2\). Its retained
diagonal mass is
\[
 F_{\mathrm{diag},N}
 :=\frac12\sum_\alpha\sum_{j\in J_N}q_j^\alpha
 \sum_i(\pi_i^\alpha)^2,
\tag{33}
\]
and it satisfies the strict loss bound
\[
 \boxed{0\leq
 F_{\mathrm{diag}}-F_{\mathrm{diag},N}<\frac Q{50}.}
\tag{34}
\]

## Proof

Fix a used source \(z\). For \(\beta_z^\alpha>0\), abbreviate
\(p_i:=p_z(u_i)\) and \(\pi_i:=\pi_i^\alpha\). Every point
\(b_{\alpha,z}\in\mathscr B_{\alpha,z}\) can be written as
\[
 b_{\alpha,z}
 =\sum_{i,k}\pi_i\pi_k
 \bigl((1-\lambda_{\alpha,z,i,k})p_i
 +\lambda_{\alpha,z,i,k}p_k\bigr)
\tag{35}
\]
for parameters \(\lambda_{\alpha,z,i,k}\in[0,1]\). Every
\(b_z\in\mathscr B_z\) is correspondingly
\[
 b_z=\frac1{\beta_z}
 \sum_\alpha\beta_z^\alpha b_{\alpha,z}.
\tag{36}
\]

Let \(R_{z,i}:=\mathbf1_{A_z(u_i)}\), and define
\[
 f_{\alpha,z,i}
 :=\frac{2\beta_z^\alpha}{a_z}\pi_iR_{z,i},
 \qquad
 F_{\alpha,z}:=\sum_i f_{\alpha,z,i}.
\tag{37}
\]
By (8), \(f_{\alpha,z,i}\) has mass
\(\beta_z^\alpha\pi_i\) and barycenter \(p_i\). Also
\[
 0\leq F_{\alpha,z}
 \leq\frac{2\beta_z^\alpha}{a_z}.
\tag{38}
\]
Put
\[
 h_{\alpha,z}:=\frac12\sum_{i,k}
 \left[
 (1-\lambda_{\alpha,z,i,k})\frac{\pi_k}{2}f_{\alpha,z,i}
 +\lambda_{\alpha,z,i,k}\frac{\pi_i}{2}f_{\alpha,z,k}
 \right].
\tag{39}
\]
Inside the outer factor \(1/2\), the coefficient of a fixed
\(f_{\alpha,z,i}\) is at most
\[
 \frac12\sum_k\pi_k+\frac12\sum_k\pi_k=1.
\]
Therefore \(0\leq h_{\alpha,z}\leq F_{\alpha,z}/2\). Direct summation of
masses and first moments gives
\[
 \int h_{\alpha,z}=\frac{\beta_z^\alpha}{4},
 \qquad
 \frac4{\beta_z^\alpha}
 \int xh_{\alpha,z}(x)\,dx=b_{\alpha,z}.
\tag{40}
\]
Equations (7) and (38) give the simultaneous pointwise bound
\[
 0\leq\sum_\alpha h_{\alpha,z}
 \leq\frac12\sum_\alpha F_{\alpha,z}
 \leq\frac{\beta_z}{a_z}
 \leq\frac14.
\tag{41}
\]
The density in (41) has mass \(\beta_z/4\) and barycenter \(b_z\) by
(36) and (40). This proves (11), including the full pooled circuit body
with one source density.

We next prove the synchronous transport and joint target packing. The two
points averaged in (12) maximize the same functional over their respective
half-metronoids. Hence their average maximizes that functional over the
Minkowski average \(L_j\), proving (12). Equations (14)-(15) follow by
direct expansion, and convexity of \(L_j\) gives
\(y_{\alpha,j,i,k}\in L_j\). At a fixed source \(z\), equation (6) gives
\[
 \begin{aligned}
 \sum_{\substack{j,\sigma\in\{-,+\}\\z_j^\sigma=z}}
 s_{\alpha,j,i,k}
 &=\frac{\pi_i^\alpha\pi_k^\alpha}{4}
 \sum_jq_j^\alpha
 \bigl(\mathbf1_{\{z_j^-=z\}}+
       \mathbf1_{\{z_j^+=z\}}\bigr)\\
 &=\frac{\beta_z^\alpha\pi_i^\alpha\pi_k^\alpha}{4},
 \end{aligned}
\]
which proves (18), including repeated physical sources and every ordered
pair. Whenever the right side of (18) is positive, normalizing the
corresponding sum of source Dirac masses gives one probability measure
supported on \([p_z(u_i),p_z(u_k)]\). Hence these occurrence atoms are
exactly one admissible disaggregation of every ordered segment block.

For a positive target weight \(w_{\alpha,j,i,k}\), membership (2) at the
point \(y_{\alpha,j,i,k}\) supplies a density
\(\rho_{\alpha,j,i,k}\) supported on \(C_{m_j}\), between zero and one,
of mass \(\vartheta_j\) and barycenter \(y_{\alpha,j,i,k}\). Define
\[
 g_{\alpha,j,i,k}
 :=\frac{w_{\alpha,j,i,k}}{\vartheta_j}
 \rho_{\alpha,j,i,k},
\tag{42}
\]
and set it to zero when the weight is zero. It has the required mass and
barycenter. Since every \(\rho_{\alpha,j,i,k}\leq\mathbf1_{C_m}\), at a
fixed target \(m\) one has
\[
 \begin{aligned}
 \sum_\alpha\sum_{j:m_j=m}\sum_{i,k}g_{\alpha,j,i,k}
 &\leq
 \sum_\alpha\sum_{j:m_j=m}\sum_{i,k}
 \frac{w_{\alpha,j,i,k}}{\vartheta_j}\mathbf1_{C_m}\\
 &=\frac12\sum_{j:m_j=m}\frac1{\vartheta_j}
 \sum_\alpha q_j^\alpha
 \sum_{i,k}\pi_i^\alpha\pi_k^\alpha\mathbf1_{C_m}\\
 &=\frac12\sum_{j:m_j=m}
 \frac{q_j^{\mathrm{sat}}}{\vartheta_j}\mathbf1_{C_m}
 \leq\frac12\mathbf1_{C_m}.
 \end{aligned}
\tag{43}
\]
This proves (19) with the original target budget and no target-witness
disjointness assumption.

Summing (17) over \(\alpha,j,i,k\) and using (3) and
\(\sum_{i,k}\pi_i^\alpha\pi_k^\alpha=1\) proves (26). The same
calculation restricted to one target gives mass \(\eta_m/2\), so the
barycenter in (24) belongs to \(\mathsf M_{\eta_m/2}(C_m)\) by (19).
For each block, one has
\[
 \begin{aligned}
 &\sum_{i,k}\pi_i^\alpha\pi_k^\alpha
 \bigl((1-\lambda_{\alpha,j,i,k})p_{ij}
 +\lambda_{\alpha,j,i,k}p_{kj}\bigr)\\
 &\quad=c_{\alpha j}
 +\sum_{i,k}\pi_i^\alpha\pi_k^\alpha
 (\lambda_{\alpha,j,i,k}-1/2)(p_{kj}-p_{ij}).
 \end{aligned}
\tag{44}
\]
Substitute (17) into (24), use (21), and put
\(\varepsilon_{\alpha,j,i,k}:=1-2\lambda_{\alpha,j,i,k}\in[-1,1]\).
Equations (22) and (44) then give
\[
 x_m=c_m^{\mathrm{circ}}
 +\sum_\alpha\sum_{j:m_j=m}\sum_{i,k}
 \varepsilon_{\alpha,j,i,k}
 \widetilde g_{\alpha,i,k}^{(j,m)},
\tag{45}
\]
which proves the switch-body membership in (25).

If \(i=k\), both segments in (14)-(15) are singletons, proving (27). By
(5), (17), and finite interchange,
\[
 \begin{aligned}
 \sum_{\alpha,j,i}w_{\alpha,j,i,i}
 &=\frac12\sum_\alpha\sum_jq_j^\alpha
   \sum_i(\pi_i^\alpha)^2\\
 &=\frac12\sum_\alpha\Omega_\alpha
   \sum_i(\pi_i^\alpha)^2,
 \end{aligned}
\]
which is (28). Thus the diagonal contribution is an actual subfamily of
the single joint packing (19), not a formal mass correction.

We finish with the affine-hit and non-hit arithmetic. If \(T(a)>0\), then
(11) gives
\[
 a(z)\in\mathsf M_{\beta_z/4}(C_z)
 \qquad(z\in A(a)).
\]
The affine-selector conclusion of accepted fact `10f1feebe06e22d0`, with
\(L=\mathbb R^n\), therefore gives \(G\geq T(a)\). This proves (30); the
case \(T(a)=0\) is irrelevant to its positive premise.

Under the final hypothesis, fix \(a\) and abbreviate \(A=A(a)\). Every
label outside \(J_N\) has at least one endpoint occurrence in \(A\).
Therefore (6) and exact occurrence counting give
\[
 \sum_{j\notin J_N}q_j^{\mathrm{sat}}
 \leq\sum_{z\in A}\beta_z
 =4T(a)<\frac Q{25}.
\tag{46}
\]
Using \(\Omega_b>97Q/100\) from (3),
\[
 \Omega_N
 =\Omega_b-\sum_{j\notin J_N}q_j^{\mathrm{sat}}
 >\frac{97}{100}Q-\frac1{25}Q
 =\frac{93}{100}Q,
\]
which proves both strict inequalities in (32). Restricting the already
joint family in (19) to \(j\in J_N\) preserves its pointwise bound, and
its mass is
\[
 \sum_\alpha\sum_{j\in J_N}\sum_{i,k}
 w_{\alpha,j,i,k}
 =\frac12\sum_{j\in J_N}q_j^{\mathrm{sat}}
 =\frac{\Omega_N}{2}.
\tag{47}
\]
Finally, (28), (33), \(\sum_i(\pi_i^\alpha)^2\leq1\), and (46) give
\[
 \begin{aligned}
 0\leq F_{\mathrm{diag}}-F_{\mathrm{diag},N}
 &=\frac12\sum_\alpha\sum_{j\notin J_N}q_j^\alpha
   \sum_i(\pi_i^\alpha)^2\\
 &\leq\frac12\sum_{j\notin J_N}\sum_\alpha q_j^\alpha
 =\frac12\sum_{j\notin J_N}q_j^{\mathrm{sat}}
 <\frac Q{50}.
 \end{aligned}
\]
This proves (34) and all stated source, target, multiplicity, and diagonal
claims. The argument supplies no upper bound on the residual rank of the
target barycenters and no closure beyond this joint packing theorem.

## External sources

none
