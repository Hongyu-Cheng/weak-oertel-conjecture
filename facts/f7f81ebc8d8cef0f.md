---
fact_id: f7f81ebc8d8cef0f
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: square-complement-selector-or-target-pack
depends_on: ["6bfe50fed9a5540b","6e6a3b541bc64f05","8aac56c49321466c","dfd25e72c1f45a4e"]
verifier_run: 8118b295f73d416c
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let
\(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body of positive mixed volume, and write
\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
 \qquad
 a_z:=\operatorname{vol}_d(C_z),
 \qquad
 I_+:=\{z\in\mathbb Z^n:a_z>0\},
\tag{1}
\]
\[
 W:=\sum_{z\in I_+}a_z,
 \qquad
 G:=\mathfrak C_{\mathrm{core}}(C).
\tag{2}
\]
Retain one common canonical zero-fresh hard instance of accepted facts `6bfe50fed9a5540b` and `6e6a3b541bc64f05`.  Thus the half-strength reservoir \(r=(r_e)\) has positive unordered off-diagonal edges, mass and endpoint degrees
\[
 Q:=\sum_er_e>0,
 \qquad
 \delta_z:=d_z(r)=\sum_{e\ni z}r_e
 \leq\frac{a_z}{4},
\tag{3}
\]
and the hard ledger gives
\[
 G<\frac Q{100}.
\tag{4}
\]

Let \(\mathcal L^\square\) be the canonical degree-weighted complete-product whole-label family from accepted fact `6e6a3b541bc64f05`.  Every
\(\sigma\in\mathcal L^\square\) has mass \(\theta_\sigma>0\), physical target \(t(\sigma)\in\mathbb Z^n\), and a four-entry tagged occurrence multiset
\[
 \mathcal O_\sigma=
 [y_{\sigma,1},y_{\sigma,2},y_{\sigma,3},y_{\sigma,4}],
 \qquad
 \frac14\sum_{o=1}^4y_{\sigma,o}=t(\sigma),
\tag{5}
\]
where repeated physical sources remain separate tags.  Its aggregate physical occurrence loads satisfy
\[
 R_z:=\sum_{\sigma\in\mathcal L^\square}
 \theta_\sigma\operatorname{mult}_z(\mathcal O_\sigma)
 \leq a_z.
\tag{6}
\]
For every occurrence source put
\[
 c_z:=\frac1{a_z}\int_{C_z}x\,dx,
\tag{7}
\]
and define, for every whole label,
\[
 r_\sigma^c:=\frac14\sum_{o=1}^4c_{y_{\sigma,o}}.
\tag{8}
\]

Then
\[
 \boxed{W\geq8Q.}
\tag{9}
\]
Every positive physical fiber satisfies
\[
 \boxed{
 a_t\leq64\,2^{-n}G
 <\frac{16}{25}\,2^{-n}Q
 \qquad(t\in I_+).}
\tag{10}
\]
Every whole-label mass satisfies
\[
 \boxed{
 \theta_\sigma\leq64\,2^{-n}G
 <\frac{16}{25}\,2^{-n}Q
 \qquad(\sigma\in\mathcal L^\square).}
\tag{11}
\]
More precisely, define the maximum physical tagged multiplicity
\[
 m_\sigma:=
 \max_{z\in\mathbb Z^n}
 \operatorname{mult}_z(\mathcal O_\sigma)
 \in\{1,2,3,4\}.
\tag{12}
\]
Then the formally multiplicity-based improvement is
\[
 \boxed{
 \theta_\sigma\leq\frac{64}{m_\sigma}\,2^{-n}G.}
\tag{13}
\]
In particular, any label having at least two tags at one physical source satisfies
\(\theta_\sigma\leq32\,2^{-n}G\), and a label whose four tags are the same physical source satisfies
\(\theta_\sigma\leq16\,2^{-n}G\).  These hypotheses refer only to the displayed tagged multiplicity; no unstated pairing of the four tags is used.

For
\[
 \mathsf M_m(C_t):=
 \left\{
 \frac1m\int_{C_t}x f(x)\,dx:
 0\leq f\leq1\ \text{a.e.},\quad
 \int_{C_t}f=m
 \right\},
\tag{14}
\]
every prescribed whole-label barycenter is individually realizable at full label mass in its physical target:
\[
 \boxed{
 r_\sigma^c\in
 \mathsf M_{\theta_\sigma}(C_{t(\sigma)})
 \qquad(\sigma\in\mathcal L^\square).}
\tag{15}
\]

Finally retain the positive whole-label subfamily
\(\Gamma\subseteq\mathcal L^\square\) of accepted fact `6e6a3b541bc64f05`, and define its prescribed-barycenter target-packing capacity by
\[
 \mathsf P_\Gamma:=
 \sup\left\{
 \sum_{\sigma\in\Gamma}q_\sigma:
 \begin{array}{l}
 0\leq q_\sigma\leq\theta_\sigma,\\
 h_\sigma:C_{t(\sigma)}\to[0,\infty)\text{ measurable},\\
 \displaystyle\int_{C_{t(\sigma)}}h_\sigma=q_\sigma,\quad
 \displaystyle\int_{C_{t(\sigma)}}x h_\sigma(x)\,dx
 =q_\sigma r_\sigma^c,\\
 \displaystyle
 \sum_{\sigma\in\Gamma:t(\sigma)=t}h_\sigma\leq1
 \text{ a.e. on }C_t\text{ for every physical target }t
 \end{array}
 \right\}.
\tag{16}
\]
Then
\[
 \boxed{
 \mathsf P_\Gamma
 \geq
 \sum_{t\in t(\Gamma)}
 \max_{\substack{\sigma\in\Gamma\\t(\sigma)=t}}
 \theta_\sigma.}
\tag{17}
\]
This is a collision-safe legal packing bound.  No lower bound on its right side as an absolute fraction of
\(\sum_{\sigma\in\Gamma}\theta_\sigma\) is asserted.

## Proof

Every positive reservoir edge is unordered and off-diagonal, so reversing the finite endpoint-edge sums in (3) gives
\[
 \sum_z\delta_z=2\sum_er_e=2Q.
\tag{18}
\]
Using \(\delta_z\leq a_z/4\) and summing over the positive fiber support yields
\[
 2Q\leq\frac14\sum_{z\in I_+}a_z=\frac W4.
\tag{19}
\]
This proves (9).

Fix \(t\in I_+\).  Apply the uniform low-rank slice theorem of accepted fact `8aac56c49321466c` to the affine slice \(A=\{t\}\).  Its intrinsic base rank is zero and its slice mass is \(W_A=a_t\), so that theorem gives
\[
 G\geq\frac1{64}\min\{W,2^na_t\}.
\tag{20}
\]
The first entry cannot attain this minimum in the hard instance: by (4) and (9),
\[
 G<\frac Q{100}<\frac Q8\leq\frac W{64}.
\tag{21}
\]
Therefore (20) uses its second entry and gives
\[
 G\geq\frac{2^na_t}{64}.
\tag{22}
\]
This proves (10).

Fix \(\sigma\in\mathcal L^\square\), and first suppose that the four tagged occurrence sources contain at least two distinct physical sources.  Choose any two distinct sources
\[
 u,v\in\{y_{\sigma,1},y_{\sigma,2},y_{\sigma,3},y_{\sigma,4}\},
 \qquad u\ne v.
\tag{23}
\]
Each chosen physical source contains at least one tagged occurrence of \(\sigma\).  Aggregate multiplicity in (6) therefore gives
\[
 a_u\geq R_u\geq\theta_\sigma,
 \qquad
 a_v\geq R_v\geq\theta_\sigma.
\tag{24}
\]
Let \(A=\operatorname{aff}\{u,v\}\).  Since \(u,v\in I_+\) are distinct, the intrinsic base rank of the positive fibers on \(A\) is one, and
\[
 W_A:=\sum_{z\in I_+\cap A}a_z
 \geq a_u+a_v
 \geq2\theta_\sigma.
\tag{25}
\]
Accepted fact `8aac56c49321466c` gives
\[
 G\geq\frac1{64}\min\{W,2^{n-1}W_A\}.
\tag{26}
\]
Equation (21) excludes the \(W\)-entry, so (25)-(26) imply
\[
 G\geq\frac{2^{n-1}W_A}{64}
 \geq\frac{2^n\theta_\sigma}{64}.
\tag{27}
\]
This proves the first inequality in (11) whenever at least two physical occurrence sources are distinct.

Suppose instead that all four tagged occurrences are the same physical source \(z\).  Then exact tagged multiplicity in (6) gives
\[
 a_z\geq R_z\geq4\theta_\sigma.
\tag{28}
\]
Apply the rank-zero bound (22) to this positive fiber and use (28):
\[
 G\geq\frac{2^na_z}{64}
 \geq\frac{2^{n+2}\theta_\sigma}{64}.
\tag{29}
\]
Thus
\[
 \theta_\sigma\leq16\,2^{-n}G,
\tag{30}
\]
which is stronger than (11).  The two cases exhaust every four-entry tagged multiset and nowhere assume a pairing or a pairwise midpoint identity.  The strict comparison with \(Q\) in (11) follows from (4).

The general multiplicity refinement follows directly from the same physical ledger.  Choose \(z_\sigma\) attaining the maximum in (12).  Its \(m_\sigma\) separate tags contribute
\[
 a_{z_\sigma}\geq R_{z_\sigma}
 \geq m_\sigma\theta_\sigma.
\tag{31}
\]
Applying (22) at \(z_\sigma\) gives
\[
 G\geq\frac{2^na_{z_\sigma}}{64}
 \geq\frac{2^nm_\sigma\theta_\sigma}{64},
\tag{32}
\]
which is exactly (13).  This also rederives (30) when \(m_\sigma=4\).  Cross-label reuse and collisions among different tags only add nonnegative terms to \(R_{z_\sigma}\), so they cannot weaken (31).

We prove the individual target realization.  Fix
\(\sigma\in\mathcal L^\square\).  For every tagged occurrence
\(y=y_{\sigma,o}\), equation (6) gives
\[
 0<\theta_\sigma\leq a_y.
\tag{33}
\]
The constant density
\[
 f_{\sigma,o}(x):=
 \frac{\theta_\sigma}{a_y}\mathbf1_{C_y}(x)
\tag{34}
\]
has mass \(\theta_\sigma\) and barycenter \(c_y\), and hence
\[
 c_y\in\mathsf M_{\theta_\sigma}(C_y).
\tag{35}
\]
Put \(s:=\theta_\sigma^{1/d}>0\).  Apply the positive-root fiber-metronoid convexity proved in accepted fact `dfd25e72c1f45a4e` successively to the four equal-root triples
\[
 (y_{\sigma,o},c_{y_{\sigma,o}},s),
 \qquad o=1,2,3,4.
\tag{36}
\]
Their equal average is a legal positive-root triple.  Equations (5) and (8) identify it as
\[
 \left(t(\sigma),r_\sigma^c,s\right).
\tag{37}
\]
Its packet mass remains \(s^d=\theta_\sigma\), so
\[
 r_\sigma^c\in
 \mathsf M_{\theta_\sigma}(C_{t(\sigma)}).
\tag{38}
\]
This proves (15).  If physical sources repeat, their identical triples are repeated in (36) exactly according to the four tagged entries.  This is an individual membership statement; it does not add target densities belonging to different labels.

It remains to prove (17).  The family \(\Gamma\) is finite.  For every distinct physical target \(t\in t(\Gamma)\), choose
\[
 \sigma_t\in
 \operatorname*{arg\,max}_{\substack{\sigma\in\Gamma\\t(\sigma)=t}}
 \theta_\sigma.
\tag{39}
\]
By (15), choose one density \(h_{\sigma_t}\leq1\) on \(C_t\) of mass \(\theta_{\sigma_t}\) and barycenter \(r_{\sigma_t}^c\).  Put
\[
 q_{\sigma_t}:=\theta_{\sigma_t},
 \qquad
 q_\sigma:=0\quad(\sigma\ne\sigma_t),
\tag{40}
\]
and assign the zero density to every unselected label.  There is exactly one nonzero density in every physical target collision class, so the pointwise target capacity in (16) is satisfied.  This jointly feasible family has mass
\[
 \sum_{t\in t(\Gamma)}\theta_{\sigma_t}
 =
 \sum_{t\in t(\Gamma)}
 \max_{\substack{\sigma\in\Gamma\\t(\sigma)=t}}
 \theta_\sigma.
\tag{41}
\]
Taking the supremum in (16) proves (17).  No second label density at a colliding physical target has been added, and no individual low-rank core has been summed with another core.

## External sources

none
