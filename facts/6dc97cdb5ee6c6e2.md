---
fact_id: 6dc97cdb5ee6c6e2
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: dyadic-midpoint-pooling-capacity
depends_on: ["3016926516cc39df","6b09aae189415c70","9c47a4888e8a2947","dfd25e72c1f45a4e"]
verifier_run: 295d417a43e848d4
target_match: null
---

## Statement

Retain the exact canonical hard-branch setting and notation of accepted facts `3016926516cc39df` and `9c47a4888e8a2947`. Thus \(n,d\in\mathbb Z_{>0}\), \(C\subseteq\mathbb R^n\times\mathbb R^d\) is a convex body, and, for every positive-volume integral fiber,
\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
 \qquad
 a_z:=\operatorname{vol}_d(C_z),
 \qquad
 c_z:=\frac1{a_z}\int_{C_z}x\,dx.
\tag{1}
\]
The globally endpoint-disjoint dyadic matching is \(\mathcal M_2\). For \(e=\{u,v\}\in\mathcal M_2\), put
\[
 t_e:=\min\{\tau_u,\tau_v\},
 \qquad
 m_e:=\frac{u+v}{2},
 \qquad
 \bar p_e:=\frac{p_u+p_v}{2},
\tag{2}
\]
and
\[
 S_2:=\sum_{e\in\mathcal M_2}t_e>\frac{59}{200}Q.
\tag{3}
\]
For each endpoint \(y\), accepted fact `9c47a4888e8a2947` supplies actual occurrence contacts \(x_{\sigma,y}\), positive occurrence weights \(\theta_\sigma\), and half-mass witnesses \(F_{\sigma,y}\) such that
\[
 0\leq F_{\sigma,y}\leq1,
 \qquad
 \int_{C_y}F_{\sigma,y}=\frac{a_y}{2},
 \qquad
 \frac2{a_y}\int_{C_y}xF_{\sigma,y}(x)\,dx=x_{\sigma,y},
\tag{4}
\]
\[
 \tau_y=\sum_\sigma\theta_\sigma,
 \qquad
 p_y=\sum_\sigma\frac{\theta_\sigma}{\tau_y}x_{\sigma,y}.
\tag{5}
\]
The sum in (4)--(5) is over the actual positive occurrences of \(y\).

For a physical midpoint \(m\), let
\[
 \mathcal E(m):=\{e\in\mathcal M_2:m_e=m\},
 \qquad
 T(J):=\sum_{e\in J}t_e
\tag{6}
\]
for \(J\subseteq\mathcal E(m)\). Call nonempty \(J\) poolable when
\[
 \frac1{T(J)}\sum_{e\in J}t_e\bar p_e
 \in\mathsf M_{T(J)}(C_m),
\tag{7}
\]
and define \(P_{\mathrm{pool}}\) by
\[
 P_{\mathrm{pool}}
 :=\sum_m\max\bigl(\{T(J):J\subseteq\mathcal E(m)
 \text{ is poolable}\}\cup\{0\}\bigr).
\tag{8}
\]
Retain the canonical capacities of accepted fact `6b09aae189415c70` and put
\[
 B_{\mathrm{cap}}
 :=R+G+R_{\mathrm{sel}}(C)+M_{\mathrm{off}}(C)
 +R_{\mathrm{cloud}}(C),
 \qquad
 D:=2^nh_{\max}(C),
\tag{9}
\]
\[
 \gamma_k:=\left(\frac{k}{k+1}\right)^k
 \qquad(k\in\mathbb Z_{>0}).
\tag{10}
\]

Then the following assertions hold.

1. For every endpoint \(y\) of \(e\in\mathcal M_2\), there is a density \(g_{e,y}\) on \(C_y\), formed from the actual occurrence witnesses in (4), such that
\[
 0\leq g_{e,y}\leq\frac12,
 \qquad
 \int_{C_y}g_{e,y}=t_e,
 \qquad
 \frac1{t_e}\int_{C_y}xg_{e,y}(x)\,dx=p_y.
\tag{11}
\]
Every edge consequently has the strengthened target membership
\[
 \boxed{\bar p_e\in\mathsf M_{2t_e}(C_{m_e}).}
\tag{12}
\]
Equivalently, there is a target density \(f_e\) satisfying
\[
 \boxed{
 0\leq f_e\leq\frac12,
 \qquad
 \int_{C_{m_e}}f_e=t_e,
 \qquad
 \frac1{t_e}\int_{C_{m_e}}xf_e(x)\,dx=\bar p_e.}
\tag{13}
\]

2. Every nonempty \(J\subseteq\mathcal E(m)\) with \(|J|\leq2\) is poolable, using the densities in (13) simultaneously in the one target fiber. If \(t_m^{(1)}\geq t_m^{(2)}\geq0\) are the two largest weights in \(\mathcal E(m)\), with missing weights set to zero, then
\[
 \boxed{
 P_{\mathrm{pool}}
 \geq\sum_m\bigl(t_m^{(1)}+t_m^{(2)}\bigr).}
\tag{14}
\]

3. For nonempty \(J\subseteq\mathcal E(m)\), put
\[
 \bar c_e:=\frac{c_u+c_v}{2}
 \quad(e=\{u,v\}),
 \qquad
 r_c(J):=\dim\operatorname{aff}\{\bar c_e:e\in J\}.
\tag{15}
\]
Then the exact reflected-cloud normalization gives
\[
 \boxed{
 B_{\mathrm{cap}}+D
 \geq R_{\mathrm{cloud}}(C)
 \geq
 4\gamma_{2d}2^n\frac{T(J)}{r_c(J)+1}.}
\tag{16}
\]
In particular,
\[
 r_c(J)+1\leq64\gamma_{2d}2^n
 \quad\Longrightarrow\quad
 B_{\mathrm{cap}}+D\geq\frac{T(J)}{16}.
\tag{17}
\]
For \(n=2,d=1\), every such family obeys the sharper exact estimate
\[
 \boxed{
 B_{\mathrm{cap}}+D
 \geq\frac{32}{9}T(J).}
\tag{18}
\]
More generally, when \(n=2\) and \(r_c(J)\leq93\), equation (17) always applies. Hence it applies to every fixed-midpoint collision family when \(n=2\) and \(d\leq93\). In particular, a canonical one-dimensional preflight with three or more reflected dyadic pairs at one physical midpoint is already locally terminal through the displayed canonical capacity. If all of \(\mathcal M_2\) has one physical midpoint in that preflight, (18) proves the second branch of the registered alternative with \(T(J)=S_2\).

4. The two-edge guarantee in Part 2 cannot be improved to three edges from the local endpoint ancestry, volume ratios, and target half-density witnesses alone, even for a genuine full-dimensional interval-fiber body. Put
\[
\begin{aligned}
 v_1&=(6,0),&v_2&=(4,4),&v_3&=(2,6),\\
 v_4&=(-2,6),&v_5&=(-4,4),
\end{aligned}
\tag{19}
\]
let \(P:=\operatorname{conv}\{\pm v_i:1\leq i\leq5\}\), and define
\[
 C^\triangle
 :=\operatorname{conv}\left(
 (\{0\}\times[0,6])
 \cup
 \bigcup_{i=1}^5(\{v_i,-v_i\}\times[0,5])
 \right)
 \subseteq\mathbb R^2\times\mathbb R.
\tag{20}
\]
Then \(C^\triangle\) is a full-dimensional convex body, its ten displayed vertex fibers are \([0,5]\), and \(C^\triangle_0=[0,6]\). On the five reflected pairs \(e_i=\{v_i,-v_i\}\), assign the equal local endpoint data
\[
 \tau_{v_i}=\tau_{-v_i}=t_{e_i}=1,
 \qquad
 p_{v_i}=p_{-v_i}=\bar p_{e_i}=\frac54.
\tag{21}
\]
All ten endpoints are even lattice points, the five pairs are globally endpoint-disjoint same-parity pairs, and their equal endpoint weights can be placed in one dyadic bin. These data satisfy the literal local conclusions used above: \(p_y\in\mathsf M_{5/2}([0,5])\), they have a half-density occurrence-form witness of mass one, \(3a_y/640<t_e\leq a_y/4\), and every target atom has a density as in (13). For the local pooling functional on these five edges,
\[
 \boxed{S=5,\qquad P_{\mathrm{pool}}^{\mathrm{local}}=2<\frac S2.}
\tag{22}
\]
Nevertheless their reflected centroid averages all equal \(5/2\), and the canonical reflected-cloud formula gives
\[
 \boxed{R_{\mathrm{cloud}}(C^\triangle)\geq\frac{400}{9}>\frac5{16}.}
\tag{23}
\]
The assignment (21) is a diagnostic local ancestry calibration, not a claim that \(C^\triangle\) enters the canonical hard branch or that its weights are produced by the full canonical reservoir and atlas. Thus (22) is not a counterexample to the registered alternative. It identifies the first false local implication, while (23) audits rather than discards the second branch.

The theorem does not sum the separate fixed-midpoint lower bounds in (16), does not control collision families with continuous centroid rank at least \(94\) when \(n=2\), and does not prove either branch of the registered alternative for a matching spread across many physical midpoints.

## Proof

For an endpoint \(y\), define the occurrence-ancestral half-mass density
\[
 F_y:=\sum_\sigma\frac{\theta_\sigma}{\tau_y}F_{\sigma,y}.
\tag{24}
\]
Equations (4)--(5), which are the literal occurrence decomposition of accepted fact `9c47a4888e8a2947`, give
\[
 0\leq F_y\leq1,
 \qquad
 \int_{C_y}F_y=\frac{a_y}{2},
 \qquad
 \frac2{a_y}\int_{C_y}xF_y(x)\,dx=p_y.
\tag{25}
\]
For \(y\in e\), accepted fact `3016926516cc39df` gives \(t_e\leq a_y/4\). Put
\[
 g_{e,y}:=\frac{2t_e}{a_y}F_y.
\tag{26}
\]
Then \(0\leq g_{e,y}\leq2t_e/a_y\leq1/2\), and (25) gives its mass and normalized first moment exactly as in (11). In particular, \(2g_{e,y}\) is an admissible density of mass \(2t_e\) and barycenter \(p_y\), so
\[
 p_y\in\mathsf M_{2t_e}(C_y).
\tag{27}
\]

Let \(e=\{u,v\}\). Apply the positive-root fiber-metronoid convexity of accepted fact `dfd25e72c1f45a4e` to the two equal-root triples represented by (27). Their graph midpoint has base \(m_e\), continuous point \(\bar p_e\), and unchanged positive root \((2t_e)^{1/d}\). Hence (12) holds. Choose an admissible density \(F_e\) on \(C_{m_e}\) of mass \(2t_e\) and barycenter \(\bar p_e\). Then \(f_e:=F_e/2\) proves (13). This proves Part 1 with the original occurrence ancestry retained through (24), rather than replacing \(p_y\) by arbitrary metronoid points.

If \(J=\{e\}\), density \(f_e\) proves poolability. If \(J=\{e,e'\}\), the two target bases agree and
\[
 0\leq f_e+f_{e'}\leq1,
 \qquad
 \int(f_e+f_{e'})=t_e+t_{e'},
\tag{28}
\]
while its normalized first moment is
\[
 \frac{t_e\bar p_e+t_{e'}\bar p_{e'}}{t_e+t_{e'}}.
\tag{29}
\]
Thus every one- or two-edge family is poolable. At each midpoint select the two largest edges, or every edge if fewer than two exist, and sum their weights over the distinct midpoints. This proves (14).

We prove the reflected-cloud estimate. Fix nonempty \(J\subseteq\mathcal E(m)\). Distinct matching edges are distinct unordered reflected pairs about \(m\), because the matching is endpoint-disjoint. For \(e=\{u,v\}\), put
\[
 \alpha_e:=\min\{a_u,a_v\}.
\tag{30}
\]
The pair-scale bound of accepted fact `3016926516cc39df` gives
\[
 \alpha_e\geq4t_e.
\tag{31}
\]
Use in the definition of \(R_{\mathrm{cloud}}(C)\) from accepted fact `6b09aae189415c70` the noncentral reflected subcloud indexed by \(J\). Its points are precisely \(\bar c_e\), so (30)--(31) give
\[
 R_{\mathrm{cloud}}(C)
 \geq
 2^n\frac{\gamma_{2d}\sum_{e\in J}\alpha_e}{r_c(J)+1}
 \geq
 4\gamma_{2d}2^n\frac{T(J)}{r_c(J)+1}.
\tag{32}
\]
All summands of \(B_{\mathrm{cap}}+D\) are nonnegative and \(R_{\mathrm{cloud}}(C)\) is one of them, so (16) follows. Equation (17) is immediate.

If \(n=2,d=1\), then \(r_c(J)+1\leq2\) and \(\gamma_2=4/9\). Substitution in (16) gives
\[
 4\gamma_2 2^2\frac{T(J)}2
 =\frac{32}{9}T(J),
\tag{33}
\]
which proves (18).

For the rank-\(93\) calibration, the elementary inequalities
\[
 \gamma_k>\frac1e
 \qquad(k\geq1),
 \qquad
 e<\frac{87}{32}<\frac{128}{47}
\tag{34}
\]
give \(256\gamma_{2d}>94\). The first inequality follows from \((1+1/k)^k<e\). For the middle bound, the exponential series and \(k!\geq24\cdot5^{k-4}\) for \(k\geq4\) give
\[
 e
 <\frac83+\frac1{24}\sum_{j=0}^{\infty}5^{-j}
 =\frac{87}{32},
\tag{35}
\]
and \(87\cdot47=4089<4096=32\cdot128\). Thus \(r_c(J)+1\leq94<256\gamma_{2d}=64\gamma_{2d}2^2\), proving the stated \(n=2\) consequence. Since \(r_c(J)\leq d\), it covers every \(d\leq93\) collision family.

It remains to verify the genuine interval calibration. The ten points in (19) and their negatives, in the cyclic order
\[
 (6,0),(4,4),(2,6),(-2,6),(-4,4),(-6,0),
 (-4,-4),(-2,-6),(2,-6),(4,-4),
\tag{36}
\]
have strictly positive consecutive edge determinants. Hence they are exactly the exposed vertices of a two-dimensional centrally symmetric decagon \(P\). It follows from (20) that \(C^\triangle\) is a compact full-dimensional convex body, that every displayed vertex fiber is exactly \([0,5]\), and that the central fiber is exactly \([0,6]\): every generator has vertical coordinate between zero and six, the central segment attains both central endpoints, and every noncentral generator has height at most five.

For an interval \([0,A]\) and \(0<s\leq A\), direct one-dimensional rearrangement gives
\[
 \mathsf M_s([0,A])=\left[\frac s2,A-\frac s2\right].
\tag{37}
\]
Indeed, among densities \(0\leq f\leq1\) of mass \(s\), the first moment is minimized by \(\mathbf1_{[0,s]}\), maximized by \(\mathbf1_{[A-s,A]}\), and all intermediate moments follow by convexity of the admissible density set.

The endpoint contact \(p=5/4\) is the barycenter of the half-mass witness
\[
 F=\mathbf1_{[0,5/2]}.
\tag{38}
\]
The occurrence-form density \(g=(2/5)F\) has mass one, barycenter \(5/4\), and pointwise bound \(2/5<1/2\). At the target interval \([0,6]\),
\[
 f=\frac12\mathbf1_{[1/4,9/4]}
\tag{39}
\]
has mass one, barycenter \(5/4\), and pointwise bound \(1/2\). Thus (21) satisfies every asserted local density and volume condition.

For a nonempty family of \(k\) of the five equal edges, its total weight is \(k\) and its weighted point is \(5/4\). Equation (37) gives
\[
 \frac54\in\mathsf M_k([0,6])
 \quad\Longleftrightarrow\quad
 \frac k2\leq\frac54\leq6-\frac k2
 \quad\Longleftrightarrow\quad
 k\leq2.
\tag{40}
\]
This proves (22), including the failure of every three-edge pooling, even though every pair uses the densities (39) simultaneously.

Finally, all ten endpoint fibers have centroid \(5/2\), so the five reflected centroid averages have affine dimension zero, and every reflected pair has \(\alpha_e=5\). With \(n=2,d=1\), the all-five noncentral subcloud in the accepted normalization gives
\[
 R_{\mathrm{cloud}}(C^\triangle)
 \geq
 2^2\gamma_2\frac{5\cdot5}{0+1}
 =4\cdot\frac49\cdot25
 =\frac{400}{9}.
\tag{41}
\]
This proves (23). The calculation also shows why (22) is only the first false local implication and not a canonical counterexample: the second branch is overwhelmingly positive. Every assertion of the lemma is now proved.

## External sources

none
