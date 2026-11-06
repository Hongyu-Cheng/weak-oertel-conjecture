---
fact_id: ae8bb1ec375ace78
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: intrinsic-rank-residual-selector-depth
depends_on: ["107b9182522633f9","6769574fc1bd9f8d","6d6fcf377e68c79c","c49b4366d3d2977f"]
verifier_run: 8b89df5afca14e66
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and write
\[
C_z:=\{y\in\mathbb R^d:(z,y)\in C\},
\qquad
S:=C\cap(\mathbb Z^n\times\mathbb R^d).
\]
For \((z,y)\in C\), define its absolute fiber depth by
\[
\delta_C(z,y):=
\inf\left\{
\operatorname{vol}_d(C_z\cap L):
L\subseteq\mathbb R^d\text{ is a proper closed halfspace and }y\in L
\right\}.
\tag{1}
\]
For \(p\in S\), define
\[
h_S(p):=
\inf\left\{
\sum_{z\in\mathbb Z^n}\operatorname{vol}_d(C_z\cap H_z):
H\subseteq\mathbb R^{n+d}\text{ is a closed halfspace and }p\in H
\right\},
\tag{2}
\]
where \(H_z:=\{y:(z,y)\in H\}\), and put
\[
h_{\max}(C):=\sup_{p\in S}h_S(p),
\qquad
W:=\sum_{z\in\mathbb Z^n}\operatorname{vol}_d(C_z).
\tag{3}
\]

Let \(I\subseteq\mathbb Z^n\) be finite and nonempty. For every \(z\in I\), choose \(q_z\in C_z\) and a weight \(w_z\geq0\) such that
\[
\delta_C(z,q_z)\geq w_z.
\tag{4}
\]
Put
\[
J:=\{z\in I:w_z>0\},
\qquad
T:=\sum_{z\in I}w_z.
\tag{5}
\]
If \(T=0\), then the conclusions below reduce to the automatic bound \(h_{\max}(C)\geq0\). Suppose henceforth that \(T>0\), so that \(J\ne\varnothing\), and define
\[
A:=\operatorname{aff}(J),
\qquad
\rho:=\dim A.
\tag{6}
\]
For every affine map \(s:A\to\mathbb R^d\), put
\[
V_s:=\operatorname{span}\{q_z-s(z):z\in J\},
\qquad
r_s:=\dim V_s.
\tag{7}
\]
Then there exists a point \(p_s\in S\) such that every closed halfspace \(H\subseteq\mathbb R^{n+d}\) containing \(p_s\) satisfies
\[
\sum_{z\in\mathbb Z^n}\operatorname{vol}_d(C_z\cap H_z)
\geq
\frac{T}{2^\rho(r_s+1)}.
\tag{8}
\]
Consequently, with
\[
r_q(J):=
\min_{s:A\to\mathbb R^d\text{ affine}}
\dim\operatorname{span}\{q_z-s(z):z\in J\},
\tag{9}
\]
one has
\[
\boxed{
h_{\max}(C)\geq\frac{T}{2^\rho(r_q(J)+1)}.
}
\tag{10}
\]
The minimum in (9) is attained, including when \(\rho=0\) or \(r_q(J)=0\).

There is an exact coordinate-free residual-rank identity. Let \(N:=|J|\), choose any affine coordinate isomorphism \(\xi:A\to\mathbb R^\rho\), let \(X\) be the \(N\times(\rho+1)\) matrix whose row indexed by \(z\) is \((1,\xi(z)^{\mathsf T})\), and let \(Q\) be the \(N\times d\) matrix whose row indexed by \(z\) is \(q_z^{\mathsf T}\). Then
\[
\boxed{
r_q(J)
=\operatorname{rank}[X\ Q]-\operatorname{rank}X
=\dim\operatorname{aff}\{(z,q_z):z\in J\}-\rho.
}
\tag{11}
\]
In particular,
\[
0\leq r_q(J)\leq\min\{d,N-\rho-1\}.
\tag{12}
\]

For the centroid specialization, put
\[
D_+:=\{z\in\mathbb Z^n:a_z:=\operatorname{vol}_d(C_z)>0\},
\qquad
c_z:=\frac1{a_z}\int_{C_z}y\,dy,
\qquad
\gamma_d:=\left(\frac d{d+1}\right)^d.
\tag{13}
\]
For every nonempty \(E\subseteq D_+\), write
\[
W_E:=\sum_{z\in E}a_z,
\qquad
\rho_E:=\dim\operatorname{aff}(E),
\tag{14}
\]
and define the intrinsic centroid residual rank
\[
r_{\mathrm{aff}}(E):=
\min_{s:\operatorname{aff}(E)\to\mathbb R^d\text{ affine}}
\dim\operatorname{span}\{c_z-s(z):z\in E\}.
\tag{15}
\]
Then
\[
r_{\mathrm{aff}}(E)
=\dim\operatorname{aff}\{(z,c_z):z\in E\}-\rho_E
\leq\min\{d,|E|-\rho_E-1\},
\tag{16}
\]
and
\[
\boxed{
h_{\max}(C)
\geq
\frac{\gamma_d}{2^{\rho_E}(r_{\mathrm{aff}}(E)+1)}W_E.
}
\tag{17}
\]
Thus an affine-independent \(E\) satisfies
\[
h_{\max}(C)\geq\gamma_d2^{-\rho_E}W_E,
\tag{18}
\]
and, if \(N_+:=|D_+|\) and \(\rho_+:=\dim\operatorname{aff}(D_+)\), then
\[
h_{\max}(C)
\geq
\frac{\gamma_d W}
{2^{\rho_+}\bigl(1+\min\{d,N_+-\rho_+-1\}\bigr)}
\qquad(W>0).
\tag{19}
\]

The corresponding enemy constraints retain all strictness. Let \(c>0\), assume \(W>0\), and put \(\varphi_E:=W_E/W\). If
\[
h_{\max}(C)<c\,2^{-n}W,
\tag{20}
\]
then every nonempty \(E\subseteq D_+\) satisfies
\[
r_{\mathrm{aff}}(E)+1
>
\frac{\gamma_d}{c}\,2^{n-\rho_E}\varphi_E.
\tag{21}
\]
If the hypothesis in (20) is replaced by \(h_{\max}(C)\leq c\,2^{-n}W\), then the conclusion is the non-strict inequality
\[
r_{\mathrm{aff}}(E)+1
\geq
\frac{\gamma_d}{c}\,2^{n-\rho_E}\varphi_E.
\tag{22}
\]
In (21), respectively (22), the left side can be replaced by either upper bound \(d+1\) or \(|E|-\rho_E\), preserving the same strict, respectively non-strict, comparison. More generally, the arbitrary selector data (4)-(9) imply
\[
h_{\max}(C)<c\,2^{-n}W
\Longrightarrow
r_q(J)+1>\frac{2^{n-\rho}T}{cW},
\tag{23}
\]
and \(<,>\) become \(\leq,\geq\) simultaneously.

There are two covariance-adjusted consequences. For \(z\in D_+\), let
\[
\Sigma_z:=\frac1{a_z}\int_{C_z}(y-c_z)(y-c_z)^{\mathsf T}\,dy
\tag{24}
\]
and
\[
\mathcal E_z:=
\left\{
\eta\in\mathbb R^d:
\max_{y\in C_z}
\left|\left\langle\Sigma_z^{-1}\eta,y-c_z\right\rangle\right|
\leq1
\right\}.
\tag{25}
\]
For a nonempty \(E\subseteq D_+\), choose \(\eta_z\in\mathcal E_z\) and define
\[
r_{\mathrm{cov}}(E;\eta):=
\min_{s:\operatorname{aff}(E)\to\mathbb R^d\text{ affine}}
\dim\operatorname{span}\{c_z+\eta_z-s(z):z\in E\}.
\tag{26}
\]
Then
\[
\boxed{
h_{\max}(C)
\geq
\frac{\gamma_d}{2}
\frac{W_E}{2^{\rho_E}(r_{\mathrm{cov}}(E;\eta)+1)}.
}
\tag{27}
\]

For the asymmetric version, let \(\eta_z\in\mathbb R^d\), and put
\[
p_z:=\max_{y\in C_z}
\left\langle\Sigma_z^{-1}\eta_z,y-c_z\right\rangle,
\qquad
q_z^-:=\max_{y\in C_z}
\left(-\left\langle\Sigma_z^{-1}\eta_z,y-c_z\right\rangle\right).
\tag{28}
\]
If \(q_z^-\leq1\) for every \(z\in E\), then \(p_z\geq0\), and, with
\[
r_+(E;\eta):=
\min_{s:\operatorname{aff}(E)\to\mathbb R^d\text{ affine}}
\dim\operatorname{span}\{c_z+\eta_z-s(z):z\in E\},
\tag{29}
\]
one has
\[
\boxed{
h_{\max}(C)
\geq
\frac{\gamma_d}{2^{\rho_E}(r_+(E;\eta)+1)}
\sum_{z\in E}\frac{a_z}{1+p_z}.
}
\tag{30}
\]
In particular, if \(0\leq\lambda\leq1\) and there is an affine map \(s:\operatorname{aff}(E)\to\mathbb R^d\) satisfying
\[
s(z)-c_z\in\lambda\mathcal E_z
\qquad(z\in E),
\tag{31}
\]
then
\[
\boxed{
h_{\max}(C)
\geq
\frac{\gamma_d}{1+\lambda}\,2^{-\rho_E}W_E.
}
\tag{32}
\]
Thus \(\lambda=0\) recovers exact affine centroids, while \(\lambda=1\) gives the covariance-tolerant affine criterion with intrinsic factor \(2^{-\rho_E}\).

Finally, assume \(S\ne\varnothing\) and consider the prismatic class of accepted fact `c49b4366d3d2977f`: let \(d\geq2\), let \(P\subseteq\mathbb R^n\) be compact and convex, let \(\ell:P\to\mathbb R\) be convex, let \(u:P\to\mathbb R\) be concave, let \(U\subseteq\mathbb R^{d-1}\) be a full-dimensional convex body, and let
\[
C=\{(y,t,v):y\in P,\ \ell(y)\leq t\leq u(y),\ v\in U\}
\tag{33}
\]
be full-dimensional. Put
\[
D:=\{z\in P\cap\mathbb Z^n:u(z)>\ell(z)\},
\qquad
\rho_D:=\dim\operatorname{aff}(D),
\tag{34}
\]
when \(D\ne\varnothing\). Then every such body satisfies
\[
\boxed{
h_{\max}(C)
\geq
\frac{\gamma_d}{2}\,2^{-\rho_D}W
\geq
\frac{\gamma_d}{2}\,2^{-n}W
>
\frac1{2e}\,2^{-n}W.
}
\tag{35}
\]
When \(D=\varnothing\), one has \(W=0\), and the assumed nonempty set \(S\) contains a witness for the automatic zero lower bound. Hence the entire prismatic class within the locked problem's hypothesis satisfies the weak Oertel bound with the absolute constant \(1/(2e)\), for arbitrary support rank and arbitrary endpoint data.

This also fixes the logical status of the finite prismatic assertion (FE) in accepted fact `c49b4366d3d2977f`. If (FE) fails for every positive constant, then there is a sequence of full-dimensional \(d=2\) prismatic bodies \(C_j\), with masses \(W_j>0\), such that
\[
\frac{\mathfrak C_{\mathrm{core}}(C_j)}{W_j}\longrightarrow0,
\qquad
\frac{2^{n_j}M_{\mathrm{vol}}(C_j)}{W_j}\longrightarrow0,
\tag{36}
\]
where \(\mathfrak C_{\mathrm{core}}\) is the complete metronoid-core capacity and \(M_{\mathrm{vol}}\) is the largest positive fiber volume defined there, but nevertheless
\[
\frac{2^{n_j}h_{\max}(C_j)}{W_j}\geq\frac13
\qquad(j\geq1).
\tag{37}
\]
Thus failure of (FE) would be a separation of the complete-core-plus-heavy-fiber certificate system from true mixed depth, not a counterexample to the weak Oertel conjecture. No assertion is made here that (FE) fails, and none of the conclusions above proves the locked conjecture for general convex bodies.

## Proof

Assume first that \(T>0\), fix an affine map \(s:A\to\mathbb R^d\), and abbreviate \(V:=V_s\), \(r:=r_s\). Choose \(z_0\in J\), and let
\[
L_0:=A-z_0,
\qquad
L:=L_0\cap\mathbb Z^n.
\tag{38}
\]
The real vector space \(L_0\) is spanned by the integer vectors \(z-z_0\), \(z\in J\), so it is rational. Hence \(L\) is a free abelian group of rank \(\rho\) whose real span is \(L_0\). Choose a \(\mathbb Z\)-basis \(b_1,\ldots,b_\rho\) of \(L\), with the empty basis when \(\rho=0\), and define
\[
F:\mathbb R^\rho\to A,
\qquad
F(t):=z_0+\sum_{i=1}^\rho t_ib_i.
\tag{39}
\]
Then \(F\) is an affine isomorphism and, crucially,
\[
F(\mathbb Z^\rho)=A\cap\mathbb Z^n.
\tag{40}
\]
Thus this is a chart by the complete affine lattice, not merely by the sublattice generated by \(J-z_0\); there is no lattice-index or covolume factor.

Choose a linear isomorphism \(\vartheta:V\to\mathbb R^r\), using the unique map \(\{0\}\to\mathbb R^0\) when \(r=0\). For \(z\in J\), let \(u_z:=F^{-1}(z)\in\mathbb Z^\rho\), and form the finite atomic measure
\[
\nu:=
\sum_{z\in J}w_z
\delta_{(u_z,\vartheta(q_z-s(z)))}
\tag{41}
\]
on \(\mathbb Z^\rho\times\mathbb R^r\). Its total mass is \(T>0\). Accepted fact `6d6fcf377e68c79c`, applied with integer dimension \(\rho\) and continuous dimension \(r\), supplies
\[
\bar p=(u^\star,v^\star)\in\mathbb Z^\rho\times\mathbb R^r
\tag{42}
\]
such that every closed halfspace in \(\mathbb R^{\rho+r}\) containing \(\bar p\) has \(\nu\)-mass at least
\[
\Delta:=\frac{T}{2^\rho(r+1)}>0.
\tag{43}
\]
This use includes \(\rho=0\), \(r=0\), and \((\rho,r)=(0,0)\).

The point \(\bar p\) lies in the convex hull of the atoms in (41). Otherwise strict separation from their compact convex hull would give a proper closed halfspace containing \(\bar p\), disjoint from every atom, and hence of \(\nu\)-mass zero, contradicting (43).

Define the affine embedding
\[
\Psi:\mathbb R^\rho\times\mathbb R^r\to\mathbb R^n\times\mathbb R^d,
\qquad
\Psi(u,v):=
\bigl(F(u),s(F(u))+\vartheta^{-1}(v)\bigr).
\tag{44}
\]
It sends the atom indexed by \(z\) to \((z,q_z)\). Therefore
\[
p_s:=\Psi(\bar p)
\in\operatorname{conv}\{(z,q_z):z\in J\}
\subseteq C.
\tag{45}
\]
Its base coordinate is \(F(u^\star)\in A\cap\mathbb Z^n\) by (40), so \(p_s\in S\).

Let \(H\) be a proper closed ambient halfspace containing \(p_s\). Its pullback \(\Psi^{-1}(H)\) is the sublevel or superlevel set of an affine functional on \(\mathbb R^{\rho+r}\). If this functional is nonconstant, the pullback is a proper closed halfspace containing \(\bar p\). If it is constant, containment of \(\bar p\) forces the pullback to be all of \(\mathbb R^{\rho+r}\), rather than the empty set. Thus (43) gives
\[
\sum_{\substack{z\in J\\(z,q_z)\in H}}w_z
\geq\Delta.
\tag{46}
\]

Write
\[
H=\{(z,y):\alpha\cdot z+\beta\cdot y\geq t\}
\tag{47}
\]
with \((\alpha,\beta)\ne(0,0)\). For every index counted in (46), the fiber section \(H_z\) contains \(q_z\). If \(\beta\ne0\), then \(H_z\) is a proper closed halfspace, so (4) gives
\[
\operatorname{vol}_d(C_z\cap H_z)\geq w_z.
\tag{48}
\]
If \(\beta=0\), membership of \((z,q_z)\) in \(H\) forces \(H_z=\mathbb R^d\), and (48) again holds because
\[
w_z\leq\delta_C(z,q_z)\leq\operatorname{vol}_d(C_z).
\tag{49}
\]
Summing (48) over the indices counted in (46), and discarding every other nonnegative fiber contribution, proves
\[
\sum_{z\in\mathbb Z^n}\operatorname{vol}_d(C_z\cap H_z)
\geq\Delta.
\tag{50}
\]
If the whole ambient space is admitted as an improper halfspace, its mixed volume is at least \(\sum_{z\in J}\operatorname{vol}_d(C_z)\geq T\geq\Delta\). An empty halfspace cannot contain \(p_s\). This proves (8) for every allowed containing halfspace. Minimizing \(r_s\) proves (10), once attainment in (9) is established below. If \(T=0\), all weights vanish and the asserted lower bound is zero, so no affine hull of an empty positive support is needed.

We prove the exact rank identity. The matrix \(X\) has rank \(\rho+1\). An affine map \(s:A\to\mathbb R^d\) has, in the coordinates \(\xi\), a coefficient matrix \(B\) such that the matrix of residual row vectors is
\[
R_B:=Q-XB.
\tag{51}
\]
Its row rank is exactly \(\dim\operatorname{span}\{q_z-s(z):z\in J\}\). Let \(\mathcal X:=\operatorname{col}(X)\subseteq\mathbb R^N\), and project columns to \(\mathbb R^N/\mathcal X\). For every \(B\), the quotient images of the columns of \(R_B\) equal those of \(Q\). Hence
\[
\operatorname{rank}R_B
\geq
\dim\operatorname{span}\bigl\{[Q_1],\ldots,[Q_d]\bigr\}
=\operatorname{rank}[X\ Q]-\operatorname{rank}X.
\tag{52}
\]
Conversely, choose a linear complement \(\mathcal U\) to \(\mathcal X\) inside \(\mathcal X+\operatorname{col}(Q)\), and decompose every column of \(Q\) as a column in \(\mathcal X\) plus a column in \(\mathcal U\). Choosing the columns of \(B\) to subtract the \(\mathcal X\)-parts makes \(\operatorname{col}(R_B)\subseteq\mathcal U\), where its dimension is exactly the quotient dimension in (52). This proves attainment and the first equality in (11). Since
\[
\operatorname{rank}X=\rho+1,
\qquad
\operatorname{rank}[X\ Q]
=1+\dim\operatorname{aff}\{(z,q_z):z\in J\},
\tag{53}
\]
the second equality follows. Finally,
\[
\operatorname{rank}[X\ Q]
\leq\min\{N,\rho+1+d\}
\tag{54}
\]
gives (12).

For the centroid specialization, fix \(z\in D_+\). The full-mass metronoid of \(C_z\) is represented by the density \(1\) and has barycenter \(c_z\). Accepted fact `6769574fc1bd9f8d`, applied with mass \(a_z\), says that every proper closed halfspace in the fiber containing \(c_z\) has volume at least \(\gamma_da_z\). Apply (10) with
\[
q_z=c_z,
\qquad
w_z=\gamma_da_z
\qquad(z\in E).
\tag{55}
\]
Equations (11)-(12) give (16), and (10) gives (17). If \(E\) is affine independent, then \(|E|=\rho_E+1\), so (12) forces \(r_{\mathrm{aff}}(E)=0\), proving (18). Applying (12) to \(E=D_+\) in (17) proves (19).

Divide (17) by \(2^{-n}W\). If (20) holds, its right side must be strictly less than \(c\), which rearranges to (21). Under the non-strict depth hypothesis the same rearrangement gives (22). Equation (12) gives
\[
r_{\mathrm{aff}}(E)+1
\leq\min\{d+1,|E|-\rho_E\},
\tag{56}
\]
so the stated consequences for these upper bounds preserve the respective inequality signs. The same rearrangement of (10) proves (23), including its non-strict version.

We next prove the covariance corollaries. Accepted fact `107b9182522633f9` proves that every \(\Sigma_z\) in (24) is positive definite, every \(\mathcal E_z\) in (25) is a compact origin-symmetric convex body, and
\[
c_z+\mathcal E_z
\subseteq\mathsf M_{a_z/2}(C_z).
\tag{57}
\]
Accepted fact `6769574fc1bd9f8d` then gives
\[
\delta_C(z,c_z+\eta_z)\geq\frac{\gamma_da_z}{2}
\qquad(\eta_z\in\mathcal E_z).
\tag{58}
\]
Apply (10) to the selected points \(c_z+\eta_z\) and weights \(\gamma_da_z/2\). This proves (27).

For arbitrary \(\eta_z\), accepted fact `107b9182522633f9` proves \(p_z,q_z^-\geq0\) and, under \(q_z^-\leq1\),
\[
c_z+\eta_z
\in
\mathsf M_{a_z/(1+p_z)}(C_z).
\tag{59}
\]
The metronoid sandwich in accepted fact `6769574fc1bd9f8d` therefore yields
\[
\delta_C(z,c_z+\eta_z)
\geq
\frac{\gamma_da_z}{1+p_z}.
\tag{60}
\]
Using these values as the weights in (10) proves (30). If (31) holds, choose \(\eta_z=s(z)-c_z\). Then
\[
p_z\leq\lambda,
\qquad
q_z^-\leq\lambda\leq1,
\qquad
r_+(E;\eta)=0.
\tag{61}
\]
Consequently
\[
\sum_{z\in E}\frac{a_z}{1+p_z}
\geq\frac{W_E}{1+\lambda},
\tag{62}
\]
and (30) gives (32).

For the prismatic conclusion, accepted fact `c49b4366d3d2977f` gives the positive fibers
\[
C_z=[\ell(z),u(z)]\times U
\qquad(z\in D)
\tag{63}
\]
and their total volume \(W\). Their centroids are
\[
c_z=
\left(\frac{\ell(z)+u(z)}2,\operatorname{cg}(U)\right).
\tag{64}
\]
The constant affine map
\[
s(z):=(0,\operatorname{cg}(U))
\tag{65}
\]
has all residuals in the one-dimensional scalar-coordinate subspace. Thus
\[
r_{\mathrm{aff}}(D)\leq1.
\tag{66}
\]
Equation (17) with \(E=D\) proves the first inequality in (35), and \(\rho_D\leq n\) proves the second. The standard strict inequality \(\gamma_d>1/e\) for every finite positive integer \(d\) proves the last. The zero-mass case was already separated in the statement.

Finally, failure of every positive constant in (FE) permits a sequence of finite data for which the normalized maximum in that assertion tends to zero. The exact finite-to-geometric realization and capacity identity in accepted fact `c49b4366d3d2977f` turn those data into full-dimensional \(d=2\) prismatic bodies satisfying (36), with no rank, support, mass, or representation discrepancy. This conclusion concerns precisely the complete-core-plus-heavy-fiber assertion (PMC). Independently, accepted fact `6d6fcf377e68c79c`, applied to each realized mixed-volume measure with continuous dimension \(2\), gives
\[
h_{\max}(C_j)
\geq\frac{W_j}{2^{n_j}(2+1)},
\tag{67}
\]
which is (37). Hence such a sequence separates the stated certificate system from true depth and cannot disprove the locked conjecture. This completes every asserted consequence.

## External sources

none
