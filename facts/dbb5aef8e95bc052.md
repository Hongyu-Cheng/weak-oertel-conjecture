---
fact_id: dbb5aef8e95bc052
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-homothetic-pair-budget-at-own-centroid
depends_on: ["0255a3c283c1a796", "e561372a5640eef8", "6769574fc1bd9f8d"]
verifier_run: 060edb225be0f715
target_match: null
---

## Source

- [af36a5fc25ebff84](../candidates/af36a5fc25ebff84.json), §§1–3, (2)–(8).

## Statement

Let $n,d\ge1$ and let $C\subseteq\mathbb R^n\times\mathbb R^d$ be a convex body. Fix a full-dimensional compact convex body $K\subseteq\mathbb R^d$ with volume centroid zero and volume $V>0$. Suppose that the actual fiber at $j\in\mathbb Z^n$ is $C_j=c_j+r_jK$ with $r_j>0$. Select any finite family of pairs $(p_\ell,q_\ell)$ with $p_\ell+q_\ell=2j$, $p_\ell\ne q_\ell$, and all endpoint bases distinct. At each selected endpoint $i$ suppose the actual fiber is $C_i=c_i+r_iK$ with $r_i>0$.

Write $\Gamma_d=(d/(d+1))^d$ and $c_d=(2\Gamma_d)^{1/d}$. For $0<r\le s$ put
$$
\Phi_d(r,s)=
\begin{cases}
r,&d=1,\\
\left[r c_d+\dfrac{s-r}{d-1}(1-c_d)\right]^d,&d\ge2,\ r\le s\le dr,\\
r^d,&d\ge2,\ s\ge dr,
\end{cases}
$$
and extend $\Phi_d$ symmetrically to $r>s$. The branches agree at $s=dr$.

For each pair write
$$
\rho_\ell=\frac{r_{p_\ell}+r_{q_\ell}}2,\qquad
m_\ell=\frac{c_{p_\ell}+c_{q_\ell}}2,\qquad
\delta_\ell=r_j-\rho_\ell,\qquad
\theta_\ell=\frac{\gamma_K(c_j-m_\ell)}{\rho_\ell},
$$
where $\gamma_K(x)=\inf\{t\ge0:x\in tK\}$ is the Minkowski gauge. Then $\delta_\ell\ge0$, and the compatibility inclusion $m_\ell+\rho_\ell K\subseteq C_j$ is equivalent to $m_\ell-c_j\in\delta_\ell K$. In particular $\theta_\ell\le d\delta_\ell/\rho_\ell$.

Write $H_i=\{x:(i,x)\in H\}$ for a closed ambient halfspace $H$ containing $(j,c_j)$, and $t_+=\max\{t,0\}$. For each selected pair,
$$
|C_{p_\ell}\cap H_{p_\ell}|+|C_{q_\ell}\cap H_{q_\ell}|
\ge V(1-\theta_\ell)_+^d\Phi_d(r_{p_\ell},r_{q_\ell})
\ge V(1-d\delta_\ell/\rho_\ell)_+^d\Phi_d(r_{p_\ell},r_{q_\ell}).
$$
Writing $S=C\cap(\mathbb Z^n\times\mathbb R^d)$, the raw depth obeys
$$
h_S((j,c_j))\ge V\left[\Gamma_d r_j^d+
\sum_\ell (1-\theta_\ell)_+^d\Phi_d(r_{p_\ell},r_{q_\ell})\right].
$$
The same inequality holds with each factor replaced by the conservative one above. For a pair with $a=\rho_\ell^dV$ and $b=r_j^dV$, that conservative factor equals $[(d+1)-d(b/a)^{1/d}]_+^d$, positive exactly when $a>\Gamma_d b$. To obtain the corresponding normalized bounds, divide by the full mixed volume $\mathcal H_d(S)$.

## Proof

For a selected pair suppress $\ell$ and write $(p,q)$ for its bases. Midpoint convexity gives $m+\rho K\subseteq C_j$, so comparing volumes gives $r_j\ge\rho$. If $h_K$ is the support function of $K$, the inclusion is equivalent to $u\cdot(m-c_j)\le(r_j-\rho)h_K(u)$ for every $u$. This is precisely $m-c_j\in\delta K$, including $\delta=0$. The two support length bounds in the proof of 0255a3c283c1a796 apply to $K$ as the sole integer fiber in $[-1/2,1/2]\times K$. For a projection with support $[-a',b']$ and mean zero, both $a'$ and $b'$ are at most $d(a'+b')/(d+1)$, so $a'\le db'$ and $b'\le da'$. Therefore $-K\subseteq dK$. Reversing the displacement gives $c_j-m\in d\delta K$, hence $\theta\le d\delta/\rho$.

The centroid zero is interior to $K$, since any supporting plane containing the centroid would place the positive-volume interior strictly on one side of its mean. Thus the gauge is finite and vanishes only at zero. If $\theta\ge1$ the first bound on the pair mass is zero. For $0<\theta<1$ let $k=(c_j-m)/(\theta\rho)\in K$, using compactness to attain the gauge. At each endpoint $i=p,q$ take
$$
\widetilde C_i=c_i+\theta r_i k+(1-\theta)r_iK\subseteq C_i.
$$
The inclusion follows from convexity of $K$. The two copy centroids $\widetilde c_i=c_i+\theta r_i k$ average to $m+\theta\rho k=c_j$. If $\theta=0$, take the original endpoint copies, whose centroids already average to $c_j$. In either case the retained radii are $(1-\theta)r_p,(1-\theta)r_q>0$.

Tighten a containing halfspace parallel to itself until its boundary passes through $(j,c_j)$. Write its margin as $A\cdot(z-j)+u\cdot(x-c_j)$, and write $p=j-v$, $q=j+v$ with $v\ne0$. If $u\ne0$, in coordinates centered at $\widetilde c_p,\widetilde c_q$ the endpoint thresholds are $t=A\cdot v-u\cdot(\widetilde c_p-c_j)$ and $-t$. After ordering the scales, reversing the sign of $t$ if needed, e561372a5640eef8 gives volume at least $V\Phi_d((1-\theta)r_p,(1-\theta)r_q)$ from the two copies. If $u=0$, at least one entire retained endpoint is captured, including both if $A\cdot v=0$. This gives the same lower bound because $\Phi_d$ is at most the smaller radius raised to the power $d$. The defining formula is homogeneous of degree $d$, which yields the first pair inequality. The inequality for $\theta$ gives the second by monotonicity of the positive-part factor.

On the actual own fiber $C_j$, the full-volume centroid case of 6769574fc1bd9f8d, with $f=1$ and mass $r_j^dV$, pays $\Gamma_d r_j^dV$ in every containing ordinary trace. The whole-fiber trace also meets this bound. No endpoint equals $j$ because $p+q=2j$ and $p\ne q$, and no two selected endpoints are repeated. All these volumes therefore add within each halfspace before taking the infimum. Any remaining fibers contribute nonnegative mass. The volume $\mathcal H_d(S)$ is finite and positive since $C$ is compact and $C_j$ has positive volume. Finally $b/a=(r_j/\rho_\ell)^d$ and $1-d\delta_\ell/\rho_\ell=(d+1)-d(b/a)^{1/d}$, giving the asserted strict positivity criterion.
