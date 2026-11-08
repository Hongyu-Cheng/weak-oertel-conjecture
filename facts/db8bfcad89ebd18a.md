---
fact_id: db8bfcad89ebd18a
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-actual-homothetic-shell-shared-source-credit
depends_on: []
verifier_run: 5d1c1907c18d7f48
target_match: null
---

## Source

- [046287857a52d424](../candidates/046287857a52d424.json), §1, (1)–(3), and §2, common signature transport.
- [c7b6ab042f325988](../candidates/c7b6ab042f325988.json), §§1–3 and 5, affine hit implications, fixed packing, and finite signature transport.

## Statement

Let $K_z$ be the positive $d$-dimensional fibers of a compact mixed-integer convex body, measured by the sum of their Lebesgue volumes. Fix a target base $p$, a shared source $s\ne p$, and disjoint nonempty exclusive source sets $A,B$, disjoint from $\{p,s\}$. Assume two positive barycentric relations give $p$ from $\{s\}\cup A$ and from $\{s\}\cup B$, respectively. Put $I=\{s\}\cup A\cup B$, $V_z=|K_z|$, and $V_I=\sum_{z\in I}V_z$. For $z\in I$ fix $c_z\in\operatorname{int}K_z$. Assume that replacing $K_z$ by $c_z+(1-\varepsilon)(K_z-c_z)$ for $z\in I$, with all other measured fibers fixed, is an actual compatible deformation with the same measured base set for all sufficiently small $\varepsilon\ge0$. Its total mass satisfies $M'(0+)=-dV_I$.

Let $\nu_z$ be the boundary cone probability of $K_z$ about $c_z$. Fix two couplings of these cone probabilities, one for each relation, and any one gluing of the two couplings over the common $\nu_s$. Let $Y_1,Y_2$ be the resulting continuous barycentric outputs at $p$. Take any finite family of closed ambient halfspaces $H_j$ whose boundaries have probability zero under all the lifted source laws and both lifted output laws. Write $f_{rj}=\Pr((p,Y_r)\in H_j)$ and $o_j=\Pr((p,Y_1),(p,Y_2)\in H_j)$, with the latter denoting joint membership of both outputs. Put
$$
a=dV_s,\quad b=d\min_{z\in A}V_z,\quad c=d\min_{z\in B}V_z,\quad
c_1=\min(a,b),\ c_2=\min(a,c),\ c_{12}=\min(a,b+c),\ \rho=c_1+c_2-c_{12}.
$$
The fixed-cap loss derivative exists for every $j$ and satisfies $L_j\ge B_j:=c_1f_{1j}+c_2f_{2j}-\rho o_j$. The limiting joint source and target signature law is the law of the one chosen cone gluing. The increase of $B_j$ over the best fixed independent allocation with coefficients $0\le x\le b,\ 0\le y\le c,\ x+y\le a$ is exactly $\rho[\min(f_{1j},f_{2j})-o_j]$. For prescribed nonnegative weights on the cap family, an optimizing gluing for the weighted sum of the $B_j$ exists and uses the same two relation marginals for the entire family.

## Proof

Write $\tau_\varepsilon=1-(1-\varepsilon)^d$. Radial integration about $c_z$ gives normalized shell volume as the law of $X_z=c_z+R(U_z-c_z)$, where $U_z$ has law $\nu_z$ and $R$, independent of all the cone variables, has density $d r^{d-1}/\tau_\varepsilon$ on $[1-\varepsilon,1]$. This follows by differentiating the $r^d$ volume scaling on each cone over a Borel boundary subset. Use one common $R$ for all $z$ and the chosen gluing of the cone variables. Such gluings exist by disintegration over the shared coordinate and taking the product of its two conditional kernels. All spaces here are standard Borel. The old fiber $K_p$ contains each barycentric output by convexity. The sum of the removed volumes is $\tau_\varepsilon V_I$.

For a fixed cap, if one lifted barycentric output of the $X_z$ belongs to the cap, at least one source of its relation belongs to the cap, since the defining affine margin is the weighted average of the source margins. Charge a source in the cap its shell volume $\tau_\varepsilon V_z$. On the four possible output-hit states (none, first only, second only, both), the cost is at least $\tau_\varepsilon/d$ times $0,c_1,c_2,c_{12}$, respectively. For both, a hit of the shared source costs at least $a$ in these units, and otherwise each exclusive set must supply one hit, at cost at least $b+c$. The same reasoning bounds each of the one-hit states. The expected total cost is exactly the actual removed cap mass, since every $X_z$ is uniform on its shell. Taking expectations of this pointwise bound gives the expression with the shell-output probabilities. As $\varepsilon\downarrow0$, all $X_z$ converge to $U_z$, since $1-\varepsilon\le R\le1$ (one may realize the radii by a common uniform random variable). All source and output indicators for the finite cap family converge almost surely by boundary nullity. Dominated convergence gives the joint signature limit and the loss derivative, using $\tau_\varepsilon/\varepsilon\to d$. The two separately weighted target inequalities yield fixed coefficients as in the statement. When $f_{1j}\ge f_{2j}$ the optimal value of that linear program is $c_1 f_{1j}+(c_{12}-c_1)f_{2j}$, by first filling the larger coefficient and then filling the remaining joint capacity; interchanging the labels handles the reverse order. Subtracting gives the stated gain formula.

For the last assertion, at each shared cone point disintegrate the two relation laws and form the conditional laws of their finite output signatures. Choose a transportation matrix with those marginals minimizing the weighted overlap cost $\sum_j \omega_j\rho\,\sigma_j\sigma'_j$ on the paired signatures. A Borel choice exists: remove one redundant row from the marginal equations, enumerate the finitely many column bases, and take the first feasible minimum-cost basic solution. Feasibility and cost comparison are Borel in the marginal entries, and a nonempty compact transportation polytope has an optimal vertex. Given the shared point and the two drawn signatures, sample the remaining relation coordinates from the respective original conditional laws given that point and signature. Integration over the shared point recovers both original relation laws and attains the weighted optimum in one gluing.
