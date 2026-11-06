---
fact_id: b14e36d0dd8bfdb7
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: canonical-descendant-universality
depends_on: ["39f0a775ae931bc3","51ff186e1aaeaa85"]
verifier_run: bae212b59b094657
target_match: null
---

## Statement

For a nonzero finite Borel measure \(\mu\) on a positive-dimensional Euclidean space and any point \(p\), define
\[
h_\mu(p):=\inf\{\mu(H):H\text{ is a proper closed affine halfspace and }p\in H\}.
\tag{1}
\]
Let \(V_1,V_2\) be finite-dimensional Euclidean spaces with \(\dim V_1,\dim V_2\geq1\), let \(\mu_i\) be a nonzero finite Borel measure on \(V_i\), let \(\varnothing\neq P_i\subseteq V_i\), and put
\[
M_i:=\sup_{p_i\in P_i}h_{\mu_i}(p_i)\qquad(i=1,2).
\tag{2}
\]
Then
\[
M_1M_2
\leq
\sup_{(p_1,p_2)\in P_1\times P_2}
h_{\mu_1\otimes\mu_2}(p_1,p_2)
\leq
\min\{|\mu_2|M_1,|\mu_1|M_2\}.
\tag{3}
\]
These inequalities do not require either supremum or any depth infimum to be attained.

Now let \(K\subseteq\mathbb R^k\times\mathbb R^d\) be an arbitrary convex body of positive mixed mass \(W_K\), where \(k,d\in\mathbb Z_{>0}\). In accepted fact 39f0a775ae931bc3, rename its arbitrary input body \(B\) as \(K\), retain its genuine two-cap parent \(C_K\), and write the fiber-preserving shear in canonical base-continuous order as
\[
\Sigma(z,\tau;x,t)=(z,\tau;x,t+z_1).
\tag{4}
\]
Thus \(\Sigma^{-1}C_K\) is the regrouped product of \(K\) with
\[
\mathcal D=\{(\tau,t):0\leq\tau\leq2,\ -1\leq t\leq q(\tau)\},
\qquad
q(\tau)=4(1-|\tau-1|).
\tag{5}
\]
Let \(G_+,G_-\) be the two caps in that accepted datum and put \(A_\pm:=C_K\cap G_\pm\). For \(0\leq\tau\leq2\), one has \((\Sigma^{-1}A_\pm)_{(z,\tau)}=K_z\times I_\pm(\tau)\), where
\[
I_+(\tau)=[-1/4,q(\tau)],
\qquad
I_-(\tau)=[-1,\min\{q(\tau),5/4-\tau\}].
\tag{6}
\]
Let \(\mathcal B_K\) be the canonical equal-weight descendant supplied by accepted fact 51ff186e1aaeaa85, so that
\[
(\mathcal B_K)_{(z,\tau)}
=\tfrac12(A_+)_{(z,\tau)}+\tfrac12(A_-)_{(z,\tau)}.
\tag{7}
\]
Define
\[
r(\tau)=
\begin{cases}
4\tau,&0\leq\tau\leq1/4,\\[1mm]
\frac32\tau+\frac58,&1/4\leq\tau\leq1,\\[1mm]
\frac{37}{8}-\frac52\tau,&1\leq\tau\leq2,
\end{cases}
\tag{8}
\]
and
\[
\mathcal U_*:=\{(\tau,t):0\leq\tau\leq2,\ -5/8\leq t\leq r(\tau)\}.
\tag{9}
\]
Then \(\mathcal U_*\) is a convex body in \(\mathbb R\times\mathbb R\), and the descendant identity holds on every real base fiber:
\[
\Sigma^{-1}\mathcal B_K=K\times\mathcal U_*,
\tag{10}
\]
where the product is regrouped from \((z,x;\tau,t)\) to \((z,\tau;x,t)\). Its three nonzero integer fibers are
\[
(\mathcal U_*)_0=[-5/8,0],
\qquad
(\mathcal U_*)_1=[-5/8,17/8],
\qquad
(\mathcal U_*)_2=[-5/8,-3/8].
\tag{11}
\]
Consequently,
\[
W(\mathcal U_*)=\frac{29}{8},
\qquad
h_{\max}(\mathcal U_*)=\frac32,
\qquad
\frac{h_{\max}(\mathcal U_*)}{W(\mathcal U_*)}=\frac{12}{29}.
\tag{12}
\]
The shear preserves mixed mass and halfspace depth, so
\[
W(\mathcal B_K)=\frac{29}{8}W_K
\tag{13}
\]
and
\[
\frac32h_{\max}(K)
\leq h_{\max}(\mathcal B_K)
\leq
\min\left\{\frac{29}{8}h_{\max}(K),\frac32W_K\right\}.
\tag{14}
\]
Equivalently, with \(\Delta(L):=h_{\max}(L)/W(L)\),
\[
\frac{12}{29}\Delta(K)
\leq\Delta(\mathcal B_K)
\leq\min\left\{\Delta(K),\frac{12}{29}\right\}.
\tag{15}
\]

For \(c>0\), let \({\rm CD}(c)\) be the assertion that every canonical descendant \(\mathcal B_K\) above satisfies
\[
h_{\max}(\mathcal B_K)
\geq c\,2^{-(k+1)}W(\mathcal B_K).
\tag{16}
\]
Let \({\rm WO}(c)\) be the weak Oertel inequality with constant \(c\) for every positive-mass mixed convex body in every positive integer and continuous dimension. Then
\[
{\rm WO}(c)\Longrightarrow {\rm CD}(c),
\qquad
{\rm CD}(c)\Longrightarrow {\rm WO}(c/2).
\tag{17}
\]
In particular, the existence of any absolute positive constant for the class of canonical descendants is equivalent to the full locked weak Oertel statement, after replacing the resulting constant by a smaller one in \((0,1/e)\) if necessary.

## Proof

We first prove (3), including the degenerate section cases. Fix \(p_i\in P_i\), and let
\[
H=\{(x,y):\langle a,x\rangle+\langle b,y\rangle\geq c\}
\tag{18}
\]
be a proper closed halfspace containing \((p_1,p_2)\). Put
\[
J:=\{x:\langle a,x\rangle+\langle b,p_2\rangle\geq c\}.
\tag{19}
\]
If \(a\neq0\), then \(J\) is a proper closed halfspace containing \(p_1\); if \(a=0\), the fact that \((p_1,p_2)\in H\) makes \(J\) the whole first ambient space. Hence in both cases
\[
\mu_1(J)\geq h_{\mu_1}(p_1).
\tag{20}
\]
For \(x\in J\), the section
\[
H_x:=\{y:\langle b,y\rangle\geq c-\langle a,x\rangle\}
\tag{21}
\]
contains \(p_2\). If \(b\neq0\), this is a proper closed halfspace; if \(b=0\), it is the whole second ambient space. Therefore
\[
\mu_2(H_x)\geq h_{\mu_2}(p_2)
\qquad(x\in J).
\tag{22}
\]
Tonelli's theorem gives
\[
\begin{aligned}
(\mu_1\otimes\mu_2)(H)
&=\int\mu_2(H_x)\,d\mu_1(x)\\
&\geq\int_J\mu_2(H_x)\,d\mu_1(x)\\
&\geq h_{\mu_2}(p_2)\mu_1(J)\\
&\geq h_{\mu_1}(p_1)h_{\mu_2}(p_2).
\end{aligned}
\tag{23}
\]
Taking the infimum over \(H\) proves the pointwise lower product bound.

For the pointwise upper bound, let \(\varepsilon>0\). Because \(\dim V_1\geq1\), proper closed halfspaces containing \(p_1\) exist; by the definition of the infimum, one can choose such a halfspace \(J_1\ni p_1\) with
\[
\mu_1(J_1)\leq h_{\mu_1}(p_1)+\varepsilon.
\tag{24}
\]
The lifted halfspace \(J_1\times V_2\) contains \((p_1,p_2)\) and has product mass \(|\mu_2|\mu_1(J_1)\). Letting \(\varepsilon\downarrow0\) yields
\[
h_{\mu_1\otimes\mu_2}(p_1,p_2)
\leq |\mu_2|h_{\mu_1}(p_1).
\tag{25}
\]
Interchanging the factors is valid because \(\dim V_2\geq1\), and gives the other upper bound. Taking suprema proves the upper half of (3). For the lower half, the pointwise lower bound can be evaluated along independently chosen sequences in \(P_1\) and \(P_2\) whose depths converge to \(M_1\) and \(M_2\). If either \(M_i=0\), the claim is immediate; otherwise their products converge to \(M_1M_2\). This proves (3) without assuming supremum attainment. Notice also that no boundary-null hypothesis was used.

We next compute the descendant. Accepted fact 39f0a775ae931bc3, with its input \(B\) renamed \(K\), gives (4)-(6). Accepted fact 51ff186e1aaeaa85 gives the weighted fiberwise Minkowski average (7) for its support-minimal two-normal circuit, whose weights in this gadget are \(1/2,1/2\). On a fixed real base fiber, the inverse shear is the same translation in the continuous \(t\)-coordinate for both cap pieces, so it commutes with their equal-weight Minkowski average. Since every nonempty \(K_z\) is convex,
\[
\tfrac12(K_z+K_z)=K_z.
\tag{26}
\]
The interval average has lower endpoint
\[
\tfrac12(-1/4-1)=-5/8
\tag{27}
\]
and upper endpoint
\[
\tfrac12\left(q(\tau)+\min\{q(\tau),5/4-\tau\}\right).
\tag{28}
\]
For \(0\leq\tau\leq1\), one has \(q(\tau)=4\tau\), and the two arguments of the minimum cross at \(\tau=1/4\). For \(1\leq\tau\leq2\), one has \(q(\tau)=8-4\tau>5/4-\tau\). Thus (28) is exactly \(r(\tau)\) in (8). This proves (10) on all real base fibers, including empty fibers. The successive slopes of \(r\) are \(4,3/2,-5/2\), so \(r\) is concave; together with the constant lower endpoint this proves that \(\mathcal U_*\) is a compact full-dimensional convex body.

Evaluating (8) at the only integer points \(0,1,2\) in its base projection gives (11). Their lengths are \(5/8,11/4,1/4\), so
\[
W(\mathcal U_*)=\frac58+\frac{11}{4}+\frac14=\frac{29}{8}.
\tag{29}
\]

We now prove the exact template depth, with every closed-halfspace orientation and every mixed point covered. Put
\[
p_*=(1,5/8).
\tag{30}
\]
Given any proper closed halfspace containing \(p_*\), translate its boundary parallel toward \(p_*\) until the boundary passes through \(p_*\). The translated halfspace is contained in the original one, so it is enough to bound its mass from below. If its boundary is vertical, the halfspace contains the entire middle integer fiber, of mass \(11/4\). Otherwise its boundary has the form
\[
t=5/8+a(\tau-1)
\tag{31}
\]
for some \(a\in\mathbb R\). The upper side contains, on the middle layer, the interval from \(5/8\) to \(17/8\), of mass \(3/2\). The lower side contains a middle-layer interval of mass \(5/4\). If \(a\leq1\), its threshold on layer \(0\) is \(5/8-a\geq-3/8\), so it contains at least \(1/4\) of that layer. If \(a\geq1\), its threshold on layer \(2\) is \(5/8+a\geq13/8\), so it contains the entire layer \(2\), of mass \(1/4\). Every closed halfspace containing \(p_*\) therefore has mixed mass at least \(3/2\), including the equality and boundary cases. Hence
\[
h_{\mathcal U_*}(p_*)\geq3/2.
\tag{32}
\]

For the reverse inequality, a point on layer \(0\) is contained in the vertical halfspace \(\{\tau\leq0\}\), whose mass is \(5/8\), and a point on layer \(2\) is contained in \(\{\tau\geq2\}\), whose mass is \(1/4\). Consider a point \((1,t)\) on the middle layer, where \(-5/8\leq t\leq17/8\). If \(t\geq5/8\), the horizontal upper halfspace has mass
\[
17/8-t\leq3/2,
\tag{33}
\]
because both outer layers lie strictly below its threshold. If \(t\leq0\), the horizontal lower halfspace has mass at most
\[
2(t+5/8)+1/4\leq3/2.
\tag{34}
\]
Here the first two terms are exactly the layer-\(0\) and middle-layer contributions, and the last term bounds the layer-\(2\) contribution by its full mass, so (34) also covers all interval endpoints. Finally, if \(0<t<5/8\), take the lower halfspace below the line through \((1,t)\) of slope
\[
a=t+5/8.
\tag{35}
\]
Its threshold on layer \(0\) is \(-5/8\), so that layer contributes zero one-dimensional measure; it contains all of layer \(2\); and its middle-layer contribution is \(t+5/8\). Its total mixed mass is therefore
\[
t+5/8+1/4=t+7/8<3/2.
\tag{36}
\]
Thus every mixed point of \(\mathcal U_*\) has depth at most \(3/2\). Together with (32) and (29), this proves (12).

Let \(\mu_K\) and \(\mu_{\mathcal U_*}\) be the mixed-volume measures, and let their admissible point sets be \(K\cap(\mathbb Z^k\times\mathbb R^d)\) and \(\mathcal U_*\cap(\mathbb Z\times\mathbb R)\), respectively. Under the fixed coordinate regrouping, the mixed point set of \(K\times\mathcal U_*\) is the corresponding product point set. On each integer base pair \((z,j)\), its continuous fiber is \(K_z\times(\mathcal U_*)_j\); product Lebesgue measure on that fiber and summation over \((z,j)\) show that its mixed-volume measure is exactly \(\mu_K\otimes\mu_{\mathcal U_*}\). The ambient spaces for these two measures have dimensions \(k+d\geq2\) and \(2\), so the positive-dimensional hypotheses of (3) hold. Applying (3), (12), and \(|\mu_K|=W_K\) gives (13)-(14) before the shear. The map \(\Sigma\) fixes every base coordinate, has determinant one on every continuous fiber, and maps closed affine halfspaces bijectively to closed affine halfspaces. It therefore preserves mixed mass and every point depth. This proves (13)-(15) for \(\mathcal B_K\). This application also permits mixed points outside the measure-theoretic support, because (1)-(3) were proved for arbitrary point sets \(P_i\).

The first implication in (17) is immediate because every \(\mathcal B_K\) is itself a mixed convex body in integer dimension \(k+1\). Conversely, assume \({\rm CD}(c)\). By (13), (14), and (16),
\[
\frac{29}{8}h_{\max}(K)
\geq h_{\max}(\mathcal B_K)
\geq c\,2^{-(k+1)}\frac{29}{8}W_K.
\tag{37}
\]
Canceling \(29/8\) gives
\[
h_{\max}(K)
\geq c\,2^{-(k+1)}W_K
=\frac c2\,2^{-k}W_K.
\tag{38}
\]
Since \(k,d\) and \(K\) were arbitrary, this is \({\rm WO}(c/2)\). If only existence of an absolute positive constant is assumed, choosing any smaller constant in \((0,1/e)\) matches the locked quantifier. This proves (17) and the claimed strategy no-go without asserting the locked target.

## External sources

none
