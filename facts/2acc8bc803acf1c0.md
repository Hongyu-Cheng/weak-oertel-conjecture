---
fact_id: 2acc8bc803acf1c0
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: exposed-fiber-isolation-sharpness
depends_on: ["6769574fc1bd9f8d","6d6fcf377e68c79c"]
verifier_run: 36be78cedc144be4
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and write
\[
C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
\qquad
D_+(C):=\{z\in\mathbb Z^n:\operatorname{vol}_d(C_z)>0\}.
\tag{1}
\]
Assume \(D_+(C)\ne\varnothing\).
For a Borel set \(A\subseteq\mathbb R^{n+d}\), define
\[
\mu_C(A):=
\sum_{w\in\mathbb Z^n}
\operatorname{vol}_d\bigl(C_w\cap A_w\bigr),
\qquad
A_w:=\{y\in\mathbb R^d:(w,y)\in A\}.
\tag{2}
\]
For \(p\in C\cap(\mathbb Z^n\times\mathbb R^d)\), put
\[
h_C(p):=
\inf\{\mu_C(H):H\subseteq\mathbb R^{n+d}
\text{ is a closed halfspace and }p\in H\},
\tag{3}
\]
and put
\[
h_{\max}(C):=
\max_{p\in C\cap(\mathbb Z^n\times\mathbb R^d)}h_C(p).
\tag{4}
\]
For a positive-volume fiber \(C_z\) and \(x\in C_z\), define its intrinsic absolute depth by
\[
\delta_{C_z}(x):=
\inf\left\{
\operatorname{vol}_d(C_z\cap L):
L\subseteq\mathbb R^d\text{ is a proper closed halfspace and }x\in L
\right\}.
\tag{5}
\]

Suppose \(z\in D_+(C)\) is strictly exposed in \(D_+(C)\): there is a linear functional \(\ell:\mathbb R^n\to\mathbb R\) such that
\[
\ell(z)>\ell(w)
\qquad
\text{for every }w\in D_+(C)\setminus\{z\}.
\tag{6}
\]
Then the mixed depth on that fiber is exactly its intrinsic depth, pointwise:
\[
\boxed{h_C(z,x)=\delta_{C_z}(x)}
\qquad(x\in C_z).
\tag{7}
\]

Consequently, for every \(d\)-dimensional convex body \(K\subseteq\mathbb R^d\) of volume \(v>0\), the product body
\[
C^{\square}_{n,K}:=[0,1]^n\times K
\tag{8}
\]
satisfies the exact identities
\[
\mu_{C^{\square}_{n,K}}(\mathbb R^{n+d})=2^n v,
\qquad
h_{C^{\square}_{n,K}}(z,x)=\delta_K(x)
\quad
(z\in\{0,1\}^n,\ x\in K),
\tag{9}
\]
and hence
\[
\boxed{
h_{\max}(C^{\square}_{n,K})=
\max_{x\in K}\delta_K(x).
}
\tag{10}
\]

Let
\[
\gamma_d:=\left(\frac d{d+1}\right)^d.
\tag{11}
\]
If \(\Delta_d\subseteq\mathbb R^d\) is a \(d\)-simplex of volume \(v>0\), then
\[
\boxed{
\max_{x\in\Delta_d}\delta_{\Delta_d}(x)=\gamma_d v.
}
\tag{12}
\]
Therefore
\[
h_{\max}([0,1]^n\times\Delta_d)=\gamma_d v,
\qquad
\frac{h_{\max}([0,1]^n\times\Delta_d)}
{\mu_{[0,1]^n\times\Delta_d}(\mathbb R^{n+d})}
=\gamma_d2^{-n}.
\tag{13}
\]

Finally, define
\[
\Theta_{n,d}:=
\inf_C
\frac{h_{\max}(C)}{\mu_C(\mathbb R^{n+d})},
\tag{14}
\]
where the infimum is over all convex bodies \(C\subseteq\mathbb R^n\times\mathbb R^d\) of positive mixed mass. Then
\[
\boxed{\Theta_{n,d}\leq\gamma_d2^{-n}}
\qquad(n,d\geq1),
\tag{15}
\]
while in continuous dimension one,
\[
\boxed{\Theta_{n,1}=2^{-(n+1)}}.
\tag{16}
\]
It follows that
\[
\Theta_{n,d}\geq2\gamma_d\Theta_{n,1}
\tag{17}
\]
holds if and only if
\[
\Theta_{n,d}=\gamma_d2^{-n}.
\tag{18}
\]

## Proof

The projection of \(C\) onto \(\mathbb R^n\) is compact, so only finitely many lattice vectors index nonempty fibers. Thus the sum in (2) is finite, \(D_+(C)\) is finite, and \(\mu_C\) is a finite Borel measure. We first record why the maximum notation in (4) is legitimate. If \(p\in C\cap(\mathbb Z^n\times\mathbb R^d)\), moving the boundary of any proper closed halfspace containing \(p\) parallel toward \(p\) can only decrease its \(\mu_C\)-mass. Hence
\[
h_C(p)=
\inf_{a\in\mathbb S^{n+d-1}}
\mu_C\bigl(\{q:\langle a,q\rangle\geq\langle a,p\rangle\}\bigr).
\tag{19}
\]
If the whole ambient space is admitted as an improper closed halfspace, its mass is the total mixed mass and it does not change this infimum.
For fixed \(a\), the function of \(p\) on the right of (19) is upper semicontinuous. Indeed, if \(p_j\to p\), then for every \(\eta>0\), eventually
\[
\langle a,p_j\rangle\geq\langle a,p\rangle-\eta,
\]
so
\[
\limsup_{j\to\infty}
\mu_C\bigl(\{q:\langle a,q\rangle\geq\langle a,p_j\rangle\}\bigr)
\leq
\mu_C\bigl(\{q:\langle a,q\rangle\geq\langle a,p\rangle-\eta\}\bigr).
\]
Letting \(\eta\downarrow0\) and using continuity from above of the finite measure gives the value at \(p\). The infimum of upper-semicontinuous functions is upper semicontinuous. Since \(C\cap(\mathbb Z^n\times\mathbb R^d)\) is compact, \(h_C\) attains its maximum. The same argument with Lebesgue measure restricted to a convex body \(K\subseteq\mathbb R^d\) shows that \(x\mapsto\delta_K(x)\) attains its maximum.

We prove (7). Fix \(x\in C_z\). Let \(H\subseteq\mathbb R^{n+d}\) be any closed halfspace containing \((z,x)\). Its restriction \(H_z\subseteq\mathbb R^d\) is either all of \(\mathbb R^d\) or a proper closed halfspace containing \(x\). In the first case
\[
\operatorname{vol}_d(C_z\cap H_z)
=\operatorname{vol}_d(C_z)
\geq\delta_{C_z}(x),
\]
and in the second case the same inequality follows from (5). Therefore
\[
\mu_C(H)
\geq\operatorname{vol}_d(C_z\cap H_z)
\geq\delta_{C_z}(x).
\]
Taking the infimum over \(H\) gives
\[
h_C(z,x)\geq\delta_{C_z}(x).
\tag{20}
\]

For the converse, fix \(\varepsilon>0\). By the definition of the infimum in (5), there is a proper closed halfspace
\[
L_0=\{y:\langle v,y\rangle\geq b\},
\qquad v\ne0,
\qquad b\leq\langle v,x\rangle,
\tag{21}
\]
such that
\[
\operatorname{vol}_d(C_z\cap L_0)
\leq\delta_{C_z}(x)+\varepsilon.
\tag{22}
\]
The boundary-through-\(x\) cap
\[
L:=\{y:\langle v,y-x\rangle\geq0\}
\tag{23}
\]
is contained in \(L_0\), is a proper closed halfspace, and contains \(x\) on its boundary. Thus
\[
\operatorname{vol}_d(C_z\cap L)
\leq\delta_{C_z}(x)+\varepsilon.
\tag{24}
\]
This justifies the boundary-through-\(x\) near-minimizer rather than assuming it.

Suppose first that \(D_+(C)\setminus\{z\}\ne\varnothing\). Define
\[
\kappa:=
\min_{w\in D_+(C)\setminus\{z\}}
\bigl(\ell(z)-\ell(w)\bigr)>0
\tag{25}
\]
and
\[
M:=\max\left\{
0,
\max_{\substack{w\in D_+(C)\setminus\{z\}\\y\in C_w}}
\langle v,y-x\rangle
\right\}<\infty.
\tag{26}
\]
Choose \(R>M/\kappa\), and set
\[
H_R:=
\left\{
(u,y):
\langle v,y-x\rangle
+R\bigl(\ell(u)-\ell(z)\bigr)\geq0
\right\}.
\tag{27}
\]
This is a proper closed halfspace whose boundary contains \((z,x)\), and its restriction to the target fiber is exactly \(L\). If \(w\in D_+(C)\setminus\{z\}\) and \(y\in C_w\), then
\[
\langle v,y-x\rangle
+R\bigl(\ell(w)-\ell(z)\bigr)
\leq M-R\kappa<0.
\tag{28}
\]
Thus \(H_R\) excludes every other positive-volume fiber. It may meet nonempty zero-volume or lower-dimensional fibers, but each such fiber contributes zero to the mixed measure. Consequently,
\[
\mu_C(H_R)=\operatorname{vol}_d(C_z\cap L)
\leq\delta_{C_z}(x)+\varepsilon.
\tag{29}
\]

If \(D_+(C)=\{z\}\), use instead the proper closed halfspace
\[
H:=\{(u,y):\langle v,y-x\rangle\geq0\}.
\tag{30}
\]
Its target restriction is \(L\), and every other lattice fiber has zero \(d\)-volume, so (29) again holds with \(H\) in place of \(H_R\). In either case,
\[
h_C(z,x)\leq\delta_{C_z}(x)+\varepsilon.
\]
Letting \(\varepsilon\downarrow0\) and combining with (20) proves (7), including points on the boundary of \(C_z\) and the case \(\delta_{C_z}(x)=0\).

We next prove the product identity. For \(C^{\square}_{n,K}\), the nonempty lattice fibers are exactly
\[
(C^{\square}_{n,K})_z=K
\qquad(z\in\{0,1\}^n).
\tag{31}
\]
They all have volume \(v\), so their total mixed mass is \(2^nv\). Fix \(z\in\{0,1\}^n\) and define
\[
\ell_z(u):=\sum_{i=1}^n(2z_i-1)u_i.
\tag{32}
\]
For every other \(w\in\{0,1\}^n\),
\[
\ell_z(z)-\ell_z(w)
=\#\{i:z_i\ne w_i\}>0.
\tag{33}
\]
Thus every positive fiber is strictly exposed. Applying (7) to every point of every fiber proves the pointwise identity in (9), and maximizing proves (10).

We prove (12). Let \(g\) be the centroid of \(\Delta_d\). In accepted fact `6769574fc1bd9f8d`, take \(K=\Delta_d\) and \(m=v\). The only admissible selector of total mass \(v\) is \(f=1\) almost everywhere, so \(\mathsf M_v(\Delta_d)=\{g\}\). The accepted metronoid-Grünbaum sandwich therefore gives
\[
\delta_{\Delta_d}(g)\geq\gamma_dv.
\tag{34}
\]

Conversely, fix \(x\in\Delta_d\), and let \(\lambda_0,\ldots,\lambda_d\) be its barycentric coordinates. Choose \(i\) with
\[
\lambda_i(x)\geq\frac1{d+1}.
\tag{35}
\]
The vertex cap
\[
L_i(x):=\{y\in\mathbb R^d:\lambda_i(y)\geq\lambda_i(x)\}
\tag{36}
\]
is a proper closed halfspace whose boundary contains \(x\). If \(q_i\) is the \(i\)-th vertex of \(\Delta_d\), then
\[
\Delta_d\cap L_i(x)
=\lambda_i(x)q_i+\bigl(1-\lambda_i(x)\bigr)\Delta_d.
\tag{37}
\]
Hence
\[
\operatorname{vol}_d(\Delta_d\cap L_i(x))
=\bigl(1-\lambda_i(x)\bigr)^dv
\leq\left(\frac d{d+1}\right)^dv
=\gamma_dv.
\tag{38}
\]
Thus \(\delta_{\Delta_d}(x)\leq\gamma_dv\) for every \(x\in\Delta_d\). Together with (34), this proves (12). Equations (10) and (12), followed by the mass identity in (9), give (13).

The cube-simplex body is an admissible body in the infimum (14), so (13) proves (15). For \(d=1\), accepted fact `6d6fcf377e68c79c` applied to the mixed-volume measure of an arbitrary admissible \(C\subseteq\mathbb R^n\times\mathbb R\) gives
\[
h_{\max}(C)
\geq\frac{\mu_C(\mathbb R^{n+1})}{2^n(1+1)}.
\tag{39}
\]
Therefore \(\Theta_{n,1}\geq2^{-(n+1)}\). The reverse inequality is (15) with \(d=1\), since \(\gamma_1=1/2\), or equivalently the exact interval product in (10). This proves (16). Finally,
\[
2\gamma_d\Theta_{n,1}
=2\gamma_d2^{-(n+1)}
=\gamma_d2^{-n}.
\tag{40}
\]
Combining (40) with the universal upper bound (15) proves the equivalence of (17) and (18).

This theorem is not a restatement of the earlier cube-bundle upper calibration, which isolates an entire fiber and gives no pointwise equality with intrinsic depth. It is also distinct from general truncated-excess lower bounds, which give neither the matching cube-simplex upper bound nor the extremal identities (15)-(18). The new step is the tilted boundary-through-\(x\) cap construction proving (7); neither earlier route is invoked here.

## External sources

none
