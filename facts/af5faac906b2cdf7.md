---
fact_id: af5faac906b2cdf7
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w31-canonical-star-joint-quadratic-escape
depends_on: ["dad8b277ce2587c7"]
verifier_run: 2da3332c1779dc9b
target_match: null
---

## Source

- [30d7d56bee7b8657](../candidates/30d7d56bee7b8657.json), 30d7d56bee7b8657:01 §§1–4, (1)–(16).
- [30d7d56bee7b8657](../candidates/30d7d56bee7b8657.json), 30d7d56bee7b8657:03 §6, (17)–(18).

## Statement

Let $d\ge2$, $m=d+1$, and $\Gamma=(d/m)^d$. Take a centrally symmetric compact convex mixed-integer source centered at $(0,0)$ with finitely many integer fibers, using the sum of their $d$-volumes as its measure. Suppose a positive fiber at a nonzero base $p$ is a full $d$-simplex of volume $V$, and every sufficiently small labeled vertex perturbation of that fiber is realizable with all other positive fibers unchanged and no new positive fibers. Choose a base linear functional $v$ with $v\cdot p=1$. After the volume-preserving fiber shear that centers the simplex and its reflected mate, write its barycentric functions as $\lambda_i(x)=l_i(x)+1/m$ and select the caps
$$
H_i(a)=\{l_i(x)-(a_i-1/m)v\cdot z\ge0\},\qquad \sum_i a_i=1.
$$
At $a^*=m^{-1}\mathbf 1$ these caps all have the original maximal raw depth $D=M/2$ as mass, where $M$ is the original total mixed mass. The cap Jacobian on the physical simplex-vertex space is onto and the stationary normalized objective-one weights are $1/(m\Gamma)$.

There is an analytic path $a(t)=a^*+t(e_1-e_0)$ and an explicit degree-two path in the simplex-vertex matrix with first variation zero for total volume and every selected cap. On the displayed velocity in the proof the normalized Lagrangian has fixed-threshold Hessian $-(d-1)/(dm)$ and mixed block $(d-1)/d$, hence joint Hessian $Q=(d-1)(2-1/m)/d>0$. The paths give
$$
M(t)=M+\frac{VQ}{4}t^2+O(t^3),\qquad
\mu_t(H_i(a(t)))=D-\frac{V\Gamma Q}{4}t^2+O(t^3)
$$
for every selected cap. Consequently the perturbed maximal raw depth is strictly below $D$ for all sufficiently small $t>0$. In particular the conclusions apply to the actual star with fibers $K,K-K,-K$ at $-1,0,1$, with the simplex at $p=-1$ moving and the other two fibers fixed.

## Proof

Write $c$ for the simplex centroid at $p$. The map $(z,x)\mapsto(z,x-c(v\cdot z))$ leaves integer bases and fiber volumes unchanged and commutes with central reflection. Thus it centers both opposite simplex fibers and preserves the actual depth and free perturbability. Each selected cap passes through the symmetry center and has nonzero continuous normal. Its boundary is null for the full mixed measure, so its old mass is $D$ for every nearby $a$. Every closed halfspace containing $(0,0)$ has mass at least $D$ by reflection, and a nonvertical opposite pair of caps through $(0,0)$ covers the ambient space at mass $D$. Hence $D$ is the actual old maximum.

Let the columns of $W$ be the new labeled simplex vertices in the old barycentric coordinates. They sum to one in each column and the old vertex matrix is $I$. The volume is $V\det W$ near $I$ since $W$ induces the identity on the quotient by the zero-sum direction space. In the trace $\lambda_i(x)\ge a_i$, one vertex lies strictly inside and the rest outside for $(W,a)$ near $(I,a^*)$. Multiplying the $d$ edge fractions of the resulting cap simplex gives its mass $VP_i(W,a)$, where
$$
P_i(W,a)=\det W\frac{(W_{ii}-a_i)^d}{\prod_{j\ne i}(W_{ii}-W_{ij})}.
$$
All other positive fibers are unchanged. For every nearby $a$ the complete original source had cap mass $D$. Thus the normalized global increment is $c_i(W,a)=P_i(W,a)-P_i(I,a)$. In particular $c_i(I,a)=0$ identically, including when other old fibers' individual cap masses depend on $a$.

For a physical matrix $B$ with zero column sums put $T=\operatorname{tr}B$, $b_i=B_{ii}$ and $s_i=\sum_{j\ne i}B_{ij}$. At $(I,a^*)$ the derivative $f_i(B)=D_Wc_i[B]$ is $\Gamma(T+s_i+b_i)$ by logarithmic differentiation. Given $f\in\mathbb R^m$, put $z_i=f_i/(m\Gamma)$, $Z=\sum_i z_i$, and set
$$
S(f)_{ii}=z_i,\qquad S(f)_{ij}=z_i-Z/d\quad(i\ne j).
$$
Its columns sum to zero and its trace is $Z$. Its row sums are $mz_i-Z$, giving $f_i(S(f))=f_i$. Since $\sum_i(s_i+b_i)=0$, the first derivative of $\mathcal L=\det W-(m\Gamma)^{-1}\sum_i c_i(W,a)$ vanishes in the physical directions, and its threshold derivative vanishes by $c_i(I,a)=0$.

Take $E_{01}=1$, $E_{11}=-1$, all other entries zero, and use $B=E-S(f(E))$, $\omega=e_1-e_0$. Then $f(B)=0$, $T=0$ and $s_i=-b_i$. Here $b_0=0$, $b_1=-(d-1)/m$, and $b_i=1/m$ for $i\ge2$. The nonzero off-diagonal entries by rows are $B_{01}=(d-1)/d$, $B_{0j}=-1/d$ for $j\ge2$, $B_{1j}=(d-1)/(md)$ for $j\ne1$, and $B_{ij}=-1/(md)$ for $i\ge2$, $j\ne i$. Hence
$$
\sum_i b_i^2=\frac{d(d-1)}{m^2},\quad
\sum_{i\ne j}B_{ij}^2=\frac{d-1}{d}+\frac{d-1}{m^2},\quad
b\cdot\omega=-\frac{d-1}{m}.
$$
Put $\sigma=\operatorname{tr}(B^2)$ and $R_i=\sum_{j\ne i}(b_i-B_{ij})^2$. Since each first derivative $f_i(B)$ vanishes, a second logarithmic derivative gives
$$
D^2_{WW}c_i[B,B]=\Gamma\bigl(-\sigma-m^2b_i^2/d+R_i\bigr).
$$
At general $a$ the first derivative is $(1-a_i)^d[T+s_i+(d/(1-a_i)-d)b_i]$. Its bracket vanishes at $a^*$, so differentiating in $a$ gives $D_aD_Wc_i[B,\omega]=\Gamma m^2b_i\omega_i/d$. The pure threshold block is zero. Since $D^2\det(I)[B,B]=-\sigma$ and $\sum_i R_i=(d+2)\sum_i b_i^2+\sum_{i\ne j}B_{ij}^2$, the fixed-threshold Hessian of $\mathcal L$ is $(m/d)\sum_i b_i^2-m^{-1}\sum_iR_i=-(d-1)/(dm)$. Its mixed block is $-(m/d)b\cdot\omega=(d-1)/d$. Their sum, counting the mixed block twice, is the stated $Q$.

Let $q_i=\Gamma(-\sigma-m^2b_i^2/d+R_i+2m^2b_i\omega_i/d)$ and $\epsilon=\Gamma Q/2$. The straight-path second derivatives of the caps are $q_i$, so $-\sigma-(m\Gamma)^{-1}\sum_iq_i=Q$. Set
$$
W(t)=I+tB+\tfrac12t^2 S(-q-\epsilon\mathbf 1),\qquad a(t)=a^*+t\omega.
$$
The normalized cap second derivatives become $-\epsilon$ and the normalized volume second derivative becomes $-\sigma-(m\Gamma)^{-1}\sum_iq_i-\epsilon/\Gamma=Q/2$. The analytic cap and determinant formulas now give the stated expansions, with one small time interval for the finite list. The prescribed simplex perturbations are actual by hypothesis. The cap margins sum to zero throughout, so the finite selected family covers every mixed point and bounds its depth by the largest selected mass. All these masses are strictly below $D$ for small $t>0$.

For the star, the hull projects to $[-1,1]$ and its only nontrivial compatibility requirement is that the endpoint midpoint belongs to $K-K$. The free-endpoint proof in fact dad8b277ce2587c7 gives strict slack, since the old midpoint body is $(K-K)/2\subset\operatorname{int}(K-K)$. The shear is the identity for the centered $K$, and $v\cdot z=-z$ gives the star margins in the original coordinates. For $d=2$ the constants specialize to $Q=5/6$ and $\Gamma=4/9$.
