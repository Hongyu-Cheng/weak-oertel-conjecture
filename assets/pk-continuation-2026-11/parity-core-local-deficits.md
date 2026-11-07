# Parity-core repair with local loads and exact deficit clipping

**Status:** pending research note. The discrete and measure arguments below are complete deductions from the explicitly stated local-star property (LS). Its proposed proof is in pending candidate `ff31d56304dd901a`, Section 2; it is not an accepted premise of the shared graph. Consequently the unconditional geometric applications below remain pending as well. No unrestricted Oertel theorem is claimed.

This note combines the local-load extension and the row-deficit calculation, using a single clipping lemma. It concerns positive full-dimensional mixed volume, with (n\ge1,d\ge2\). It does not assert an intrinsic-measure extension.

## 1. Definitions and exact geometric input

For a full-dimensional convex body (Q\subset\mathbb R^d\), let
\[
 D(Q)=\max_{y\in Q}\min_{u\in\mathbb S^{d-1}}
 \frac{|Q\cap\{x:u\cdot x\ge u\cdot y\}|}{|Q|},
 \qquad \Gamma=\left(\frac d{d+1}\right)^d.
\]
Joint continuity of cap volume follows by dominated convergence, because every boundary hyperplane is volume-null. Minimizing over the compact sphere gives a continuous function of (y\), so the maximum exists. Ordinary Grünbaum gives (D(Q)\ge\Gamma\).

Fix constants (\alpha>\Gamma\) and (\theta_*>0\) with the following property:

**(LS).** For every finite nonempty collection of (d\)-dimensional convex bodies (A_j,B,C_j\) with
\[
 (A_j+C_j)/2\subset B,\quad
 D(B),D(C_j)\le\Gamma(1+\theta_*),\quad
 (1+\theta_*)^{-1}\le |C_j|/|B|\le1+\theta_*,\quad
 0<e=\sum_j|A_j|\le\theta_*|B|,
\]
there is one (y\in\operatorname{int}B\) such that, for every nonconstant affine (f\) and every simultaneous list of real thresholds (\beta_j\),
\[
 |B\cap\{f\ge f(y)\}|+
 \sum_j\bigl(|A_j\cap\{f\ge f(y)+\beta_j\}|+
 |C_j\cap\{f\ge f(y)-\beta_j\}|\bigr)
 \ge\Gamma|B|+\alpha e. \tag{LS}
\]
The pending proof proposes (\alpha=(\Gamma+\lceil(d+1)/2\rceil/(d+1))/2\). In particular (\Gamma<\alpha\le1\). All results here use this choice. Decrease (\theta_*\), if necessary, so (\Gamma+\alpha\theta_*<1\).

Let (C\subset\mathbb R^n\times\mathbb R^d\) be a convex body, (K_z=\{x:(z,x)\in C\}\), and (V_z=|K_z|\). A core (P\subset\mathbb Z^n\) contains exactly one representative of each parity class, all with positive (V_z\). Put
\[
 L=2^n,\quad V=\max_{w\in P}V_w,\quad m=\min_{w\in P}V_w,
 \quad E=\sum_{p\notin P}V_p,\quad W=\sum_{w\in P}V_w+E,
 \quad b=W/L.
\]
All sums are finite. Empty or lower-dimensional fibers have zero (d\)-volume. The measure is exactly (\mu(H)=\sum_z|K_z\cap H_z|=\mathcal H_d(S\cap H)\). We seek an actual point of raw depth at least (T=\Gamma b\).

For each parity (r\) and core target (w\), define
\[
 F_r=\sum_{p\notin P,\ p\equiv r\pmod2}V_p,
 \qquad R_w=\sum_{v\in P,\ 2w-v\notin P}V_{2w-v}.
 \tag{1}
\]

## 2. Exact grouping and clipping

For any nonempty outer fiber (p\), let (v(p)\) be its unique parity representative and (w(p)=(p+v(p))/2\). If (w(p)\) is a core point, regard (p\) as an edge from partner (v(p)\) to target (w(p)\), of weight (V_p\). For fixed (w\), the partners are distinct because (p=2w-v\). No partner equals (w\); outer fibers are distinct from core fibers. Thus one star uses each actual fiber at most once.

For every (x\in K_p\), convexity gives
\[
 (x+K_{v(p)})/2\subset K_{w(p)},\qquad
 V_{w(p)}\ge2^{-d}V_{v(p)}. \tag{2}
\]
Consequently either of the following is enough to put the stated midpoints in the core:

* If (\max_{p\notin P}V_p<2^{-d}m\), every nonempty outer fiber has (w(p)\in P\).
* If (F_r\le\varepsilon V\) for all (r\), (V_{v(p)}\ge(1-\eta)V\), and (\varepsilon<2^{-d}(1-\eta)\), then (w(p)\in P\).

Both assertions also hold for nonempty outer fibers of zero (d\)-volume, since (2) uses one point of that fiber.

**Clipping lemma.** Suppose the middle (K_w\) and the partners in a star satisfy the depth and volume-ratio hypotheses of (LS). If its positive outer mass is (e_w\), then for every
\[
 0<r\le\min(e_w,\theta_*V_w)
\]
there is an actual point ((w,y_w)\in S\) whose depth is at least (\Gamma V_w+\alpha r\).

Choose (c_p\in\operatorname{int}K_p\) and replace each outer witness by the subbody
\[
 A'_p=c_p+(r/e_w)^{1/d}(K_p-c_p).
\]
These full-dimensional convex subbodies have total volume exactly (r\), and ((A'_p+K_{v(p)})/2\subset K_w\). Apply (LS). No actual source is changed: the subbodies are witnesses contained in its fibers.

For an ambient halfspace through ((w,y_w)\), write its inequality as
\[
 a\cdot(z-w)+u\cdot(x-y_w)\ge0.
\]
When (u\ne0\), use (f(x)=u\cdot x\) and (\beta_p=-a\cdot(p-w)\). The partner threshold is the opposite one since (v(p)-w=-(p-w)\). Distinctness of physical fibers justifies adding all contributions. When (u=0\), the whole middle fiber is present and (V_w>\Gamma V_w+\alpha\theta_*V_w\). A containing halfspace contains its parallel through-point halfspace. This proves the lemma for all closed ambient halfspaces, including boundary mass. For (r=0\), the ordinary centroid gives (\Gamma V_w\).

## 3. Exact deficit test

Assume pointwise outer smallness (\max_{p\notin P}V_p<2^{-d}m\). If any (V_w\ge b\), its centroid already attains the target. Otherwise write
\[
 \delta_w=b-V_w>0,\qquad \sum_{w\in P}\delta_w=E.
\]
For (0<\tau\le\theta_*\), put
\[
 G_\tau=\{w\in P:V_w\ge b/(1+\tau)\},\quad
 e_w(\tau)=\sum_{p:w(p)=w,\ v(p)\in G_\tau}V_p
 \quad(w\in G_\tau).
\]
Then either condition below is sufficient for sharp OC:
\[
 e_w(\tau)\ge(\Gamma/\alpha)\delta_w
 \quad\text{for some }w\in G_\tau, \tag{3}
\]
or the aggregate condition
\[
 G_\tau\ne\varnothing,\qquad
 \sum_{w\in G_\tau}e_w(\tau)
 \ge(\Gamma/\alpha)\sum_{w\in G_\tau}\delta_w. \tag{4}
\]
To prove this, suppose no actual point attains (T\). Ordinary deepest points then give (D(K_w)V_w<T\). On (G_\tau\), this bounds ordinary depths by (\Gamma(1+\tau)\), bounds relative volumes by (1+\tau\), and gives (\delta_w\le\tau V_w\). Under (3), retain exactly (r=(\Gamma/\alpha)\delta_w<\theta_*V_w\). The clipping lemma attains (T\), a contradiction. Condition (4) forces at least one successful row.

Thus failure forces, at every nonempty (G_\tau\),
\[
 e_w(\tau)<(\Gamma/\alpha)\delta_w,\qquad
 E_{\mathrm{bad}}(\tau)>
 (1-\Gamma/\alpha)E+(\Gamma/\alpha)\sum_{w\notin G_\tau}\delta_w. \tag{5}
\]
Here (E_{\mathrm{bad}}\) is the mass of edges touching a core outside (G_\tau\). If (G_\tau\) is empty the strict aggregate inequality is replaced by equality, and its non-strict version remains valid. Large incoming mass at a good target is therefore a success certificate, not a reason to lose mass by clipping.

For a finite multiscale consequence, set (t_w=b/V_w-1\) and (t_p=\max(t_{v(p)},t_{w(p)})\). Integrating the summed non-strict row inequality over (\tau\in(0,\theta_*)\) gives
\[
 \sum_p V_p(\theta_*-t_p)_+
 \le(\Gamma/\alpha)\sum_w\delta_w(\theta_*-t_w)_+. \tag{6}
\]
Finite sums justify the integration. It is strict if some (t_w<\theta_*\). The original row tests need only the finitely many thresholds (t_w\le\theta_*\).

## 4. A distributed-load theorem

Set
\[
 \theta=\min(\theta_*,1/4),\quad \eta=\theta/4,\quad
 k=\frac{\alpha-\Gamma}{4\alpha},\quad
 \varepsilon=\min\{\theta/4,\ 2^{-d-1}(1-\eta),\ \eta k\}.
\]
Let (G=\{w\in P:V_w\ge(1-\eta)V\}\), (B=P\setminus G\), and
\[
 \Delta=\sum_{w\in P}(V-V_w).
\]
Assume
\[
 F_r\le\varepsilon V\quad\text{for every parity }r,
 \qquad \sum_{w\in B}R_w\le k\Delta. \tag{7}
\]
Then (LS) implies a deterministic actual point with depth at least (\Gamma W/2^n\). No incoming-load condition is imposed on good targets; no comparability of all core volumes is assumed.

**Proof.** If (E=0\), use the largest-core centroid. Suppose (E>0\) and the target fails. The same centroid shows (\Gamma V<T\), equivalently (\Delta<E\). Since every bad core contributes more than (\eta V\) to (\Delta\),
\[
 |B|\eta V<\Delta\quad\text{when }B\ne\varnothing.
\]
The outside mass with bad parity partner is at most (|B|\varepsilon V\le k\Delta<kE\); for empty (B\) it is zero. Every outside fiber with good partner has a core midpoint by (2). Discarding those with bad target loses at most (\sum_{w\in B}R_w\le k\Delta<kE\). The retained good-to-good outer mass (E_{GG}\) therefore satisfies
\[
 E_{GG}\ge(1-2k)E. \tag{8}
\]
Also (E\le L\varepsilon V\), so failure implies, on every good core,
\[
 D(K_w)<\Gamma\frac{1+\varepsilon}{1-\eta}
 \le\Gamma(1+\theta),\qquad
 (1-\eta)\le V_v/V_w\le(1-\eta)^{-1}\le1+\theta.
\]
For a good target let (e_w\) be its entire incoming good-to-good mass. Its required repair mass is
\[
 r_w=(T-\Gamma V_w)/\alpha>0.
\]
Since (b\le(1+\varepsilon)V\),
\[
 r_w\le(\Gamma/\alpha)(\eta+\varepsilon)V
 \le(\theta/2)V<\theta V_w.
\]
If (e_w\ge r_w\), clipping proves the target. Thus failure forces (e_w<r_w<\theta V_w\) at every good target. Apply (LS) to each full retained star, giving actual candidate depth (\Gamma V_w+\alpha e_w\). At every other core use its ordinary centroid with bound (\Gamma V_w\). These are separate candidate points, not a sum of source measures.

The average of the (L\) certified depths is at least
\[
 \frac{\Gamma\sum_{w\in P}V_w+\alpha E_{GG}}L
 \ge\frac{\Gamma\sum_{w\in P}V_w+
 [\Gamma+(\alpha-\Gamma)/2]E}{L}>T,
\]
because (\alpha(1-2k)=\Gamma+(\alpha-\Gamma)/2\). At least one candidate attains the target, a contradiction. The clipping lemma already verifies every ambient orientation and boundary convention. This proves the theorem conditional exactly on (LS).

Two useful sufficient versions of (7) follow immediately:

1. It is enough to impose (R_w\le\varepsilon V\) only for bad (w\), since (\sum_{w\in B}R_w\le(\varepsilon/\eta)\Delta\le k\Delta\).
2. If every core volume is at least ((1-\eta)V\), there are no bad targets, and the per-parity bounds alone suffice.

In particular total outside mass need not be small compared with a single core fiber, and good targets can receive arbitrarily many small outer fibers.

## 5. Two exact geometric checks

For strict enlargement over total-smallness, let (Q\) be a convex (d\)-body containing zero, and (0<t<1\) with (t^d\le\varepsilon\). In one integer variable take the convex hull of fibers (tQ,Q,Q\) at (-1,0,1\), then take the product with ([0,1]^{n-1}\). These are the exact integer fibers, since the forced middle section ((tQ+Q)/2\) is contained in (Q\). With (P=\{0,1\}^n\), every core volume is (V=|Q|\), each nonzero outside parity load is (t^dV\), and
\[
 E/\min_{w\in P}V_w=2^{n-1}t^d\longrightarrow\infty.
\]
Thus no fixed condition (E\le\rho_d\min V_w\) contains this family in every integer dimension.

To test congestion, take
\[
 C_n=\operatorname{conv}\bigl(([0,1]^n\times Q)\cup([-1,0]^n\times tQ)\bigr).
\]
The integer projection is precisely the union of the two binary cubes: an integral coordinate (1\) forces the positive product in any convex combination, and an integral coordinate (-1\) forces the negative product, so mixed signs cannot occur. Positive nonzero fibers and the zero fiber equal (Q\); negative nonzero fibers equal (tQ\). All (L-1\) outside fibers target zero, with partners their opposites. Thus (E=(L-1)t^dV\), all cores are good, and (3) succeeds at zero. However
\[
 \frac{\sum_w\min(e_w,\theta V_w)}E
 =\frac{\theta}{(L-1)t^d}\longrightarrow0
\]
once (E\ge\theta V\). This rigorously refutes a universal positive lower bound on the sum of capped credits relative to (E\). It does not refute the row-deficit test or OC.

## 6. Relation to the existing graph and the remaining issue

Accepted `e4253a0d6f78849c` already proves the sharp result when all positive fibers have equal volume. The examples here have smaller outer fibers. Clipping outer witnesses does not create a new equal-volume induced source, so that accepted theorem is not being reapplied under false hypotheses.

In accepted `cf896cdbe870d267`, the disjoint matching mass bound is (\Gamma W/2-3HW/2\), where (H=2^n h_{\max}/W\). Near the sharp threshold (H<\Gamma\), this expression need not be positive; it cannot supply (7). Accepted `be359f8a6c628483` retains oblique halfspaces through dominated midpoint measures, but its residual-rank conversion does not supply the exact gain (\alpha>\Gamma\). These comparisons identify compatible ingredients without attributing an unproved consequence to them.

The remaining issue in this route is a geometric exclusion or alternate center when a substantial amount of outside mass reaches low-volume core targets. Neither (5) nor (7) is proved automatically for arbitrary bodies. The hypotheses are explicit restrictions, and (LS) itself remains a pending nonstandard input.
