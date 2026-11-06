---
fact_id: fafb27232ee5ee3d
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: square-complement-selector-or-target-pack
depends_on: ["26568e8dd7d872e1","446c8f7967309a83","d5d5de35c3f25af9"]
verifier_run: 81366773c6e0493a
target_match: null
---

## Statement

Use the canonical degree-weighted notation and tagged whole-label multiplicities of accepted facts d5d5de35c3f25af9 and 446c8f7967309a83, and the canonical capacities

\[
 \tau_m:=\min\{h_m,2d_m\}
\]

from accepted fact 26568e8dd7d872e1. There are exact rational data with

\[
 n=8,\qquad Q=1,\qquad
 \Lambda:=\sum_m\lambda_m=1,\qquad
 P_{\mathrm{tar}}:=\frac12\sum_m d_m=\frac12,
\tag{1}
\]

and with the full canonical orbit family

\[
 \beta_{\xi,t,[u]}=
 \begin{cases}
 d_{t+u}d_{t-u}/L_\xi,&u\ne0,\\[1mm]
 d_t^2/(2L_\xi),&u=0,
 \end{cases}
 \qquad
 L_\xi:=\sum_{m\equiv\xi\pmod2}d_m,
\tag{2}
\]

and every complete cross-color coefficient

\[
 \theta_{t;\xi,[u];\eta,[v]}
 =\frac{2\beta_{\xi,t,[u]}\beta_{\eta,t,[v]}}{\alpha_t},
 \qquad
 \alpha_t:=\sum_{\zeta,[w]}\beta_{\zeta,t,[w]},
 \qquad \xi<\eta,
\tag{3}
\]

for which, writing \(\Theta:=\sum_\sigma\theta_\sigma\),

\[
 \Theta>\frac14=\frac{P_{\mathrm{tar}}}{2},
 \qquad
 \sum_m(\lambda_m-h_m)=\frac15<\Theta,
\tag{4}
\]

but the exact whole-label synchronization LP

\[
 \begin{aligned}
 \mathsf S(\tau):=\max\quad&\sum_\sigma q_\sigma\\
 \text{subject to}\quad
 &0\le q_\sigma\le\theta_\sigma,\\
 &\sum_\sigma
 \operatorname{mult}_m(\mathcal O_\sigma)q_\sigma
 \le\tau_m\qquad(m\in\mathbb Z^8)
 \end{aligned}
\tag{5}
\]

satisfies

\[
 \boxed{\mathsf S(\tau)=0<\frac Q{100}.}
\tag{6}
\]

All four occurrences in

\[
 \mathcal O_\sigma=[t+u,t-u,t+v,t-v]
\tag{7}
\]

are retained with multiplicity, including zero-orbit loops. The construction also satisfies

\[
 0\le d_m,h_m\le\lambda_m\le\frac{a_m}{2},
 \qquad
 B_{\xi,t}:=\sum_{[u]}\beta_{\xi,t,[u]}\le\frac{a_t}{4},
\tag{8}
\]

\[
 R_m:=\sum_\sigma\theta_\sigma
 \operatorname{mult}_m(\mathcal O_\sigma)
 \le2d_m\le a_m,
 \qquad
 \sum_mR_m=4\Theta\le2Q,
\tag{9}
\]

\[
 \sum_m\min\{h_m,d_m\}=\frac45
 \ge2P_{\mathrm{tar}}-\Theta,
 \qquad
 \sum_m\tau_m=\frac45
 \ge4P_{\mathrm{tar}}-\Lambda-\Theta,
\tag{10}
\]

and one may choose the finite rational fiber-volume ledger so that

\[
 W:=\sum_ma_m=8Q,
 \qquad
 W-4\Theta\ge6Q.
\tag{11}
\]

This is a counterexample to the finite-dimensional synchronization implication, not a counterexample to the locked weak Oertel conjecture or to the full registered subgoal with its additional geometric provenance.

## Proof

Put

\[
 N:=10000,\qquad
 \mathcal C:=\{0,1\}^8,\qquad
 \mathcal Z:=\{0,1,\ldots,N-1\}^8.
\]

For \(c,r\in\mathcal C\) and \(z\in\mathcal Z\), define the distinct lattice source

\[
 y(c,z,r):=c+4z+2r\in\mathbb Z^8.
\tag{12}
\]

The decomposition in (12) is unique: \(c\) is the residue modulo \(2\), \(r\) is the next binary residue modulo \(4\), and then \(z\) is determined. Give these sources the rational degrees

\[
 d_{y(c,z,r)}:=
 \begin{cases}
 \displaystyle\frac{4}{5\cdot256\,N^8},&r=0,\\[3mm]
 \displaystyle\frac{1}{5\cdot255\cdot256\,N^8},&r\ne0,
 \end{cases}
\tag{13}
\]

and put \(d_m:=0\) elsewhere. For every color \(c\),

\[
 L_c=\sum_{m\equiv c\pmod2}d_m
 =\frac{4}{5\cdot256}+\frac{1}{5\cdot256}
 =\frac1{256}.
\tag{14}
\]

Consequently \(\sum_md_m=1\) and \(P_{\mathrm{tar}}=1/2\). These degrees are realized by an exact rational off-diagonal same-parity fractional matching. Indeed, in each color, partition a circle of circumference \(L_c\) into consecutive rational intervals of lengths \(d_m\), and couple each point with its antipode at distance \(L_c/2\). Every interval has length strictly below \(L_c/2\), so it is disjoint from its antipodal translate. The intersection lengths define symmetric rational edge weights, have degree \(d_m\), have no loops, and have total mass \(L_c/2\). Summing over the \(256\) colors gives mass \(1/2\), as required by the canonical \(d_m\) normalization.

Set

\[
 \lambda_m:=d_m,\qquad
 h_{y(c,z,r)}:=
 \begin{cases}
 d_{y(c,z,0)},&r=0,\\
 0,&r\ne0,
 \end{cases}
\tag{15}
\]

and put \(h_m:=0\) off the source set. Call \(r=0\) sources survivors and \(r\ne0\) sources blockers. Equations (13)--(15) give

\[
 \Lambda=1,\qquad
 \sum_{m\text{ blocker}}d_m=\frac15,\qquad
 \sum_{m\text{ survivor}}d_m=\frac45,
\tag{16}
\]

and

\[
 \tau_m=\min\{h_m,2d_m\}=h_m.
\tag{17}
\]

We next prove the strict square-mass estimate in (4) for the complete product (2)--(3), rather than for a diagonal subfamily. Conditional on a color \(c\), choose a source with probability \(d_m/L_c\). By (12)--(14), it has the form

\[
 Y=c+2X,\qquad X=2Z+R,
\tag{18}
\]

where \(Z\) is uniform on \(\mathcal Z\), independent of \(R\), and

\[
 \Pr(R=0)=\frac45,\qquad
 \Pr(R=r)=\frac{1}{5\cdot255}\quad(r\ne0).
\tag{19}
\]

Let \(X'\) be an independent copy of \(X\), and let

\[
 q(s):=\Pr(X+X'=s).
\]

The loop normalization and the two ordered orientations of every nonloop show directly from (2) that

\[
 B_{c,t}=\frac{L_c}{2}q(t-c)=\frac1{512}q(t-c).
\tag{20}
\]

Thus \(\sum_t\alpha_t=P_{\mathrm{tar}}=1/2\). The exact complete-product identity in (3) gives

\[
 P_{\mathrm{tar}}-\Theta
 =\sum_{t:\alpha_t>0}
 \frac{\sum_cB_{c,t}^2}{\alpha_t}.
\tag{21}
\]

There is a useful probabilistic reading of the ratio in (21). Let \(C\) be uniform on \(\mathcal C\), independently of \(S:=X+X'\), and observe

\[
 T:=C+S.
\]

Bayes' formula and (20) yield

\[
 \delta:=\frac{P_{\mathrm{tar}}-\Theta}{P_{\mathrm{tar}}}
 =\mathbb E_T\sum_{c\in\mathcal C}\Pr(C=c\mid T)^2.
\tag{22}
\]

We bound (22) by exact rational estimates. Write

\[
 A:=Z+Z',\qquad
 G:=(R+R')\bmod2,\qquad
 H:=\frac{R+R'-G}{2}\in\{0,1\}^8,
\tag{23}
\]

so \(S=2(A+H)+G\). Let \(\pi_g:=\Pr(G=g)\). On the group \((\mathbb F_2)^8\), every nontrivial Fourier coefficient of the law (19) equals

\[
 a:=\frac45-\frac1{5\cdot255}=\frac{1019}{1275}.
\]

Since \(G=R\mathbin\oplus R'\), Parseval's identity gives the exact collision probability

\[
 \delta_0:=\sum_g\pi_g^2
 =\frac{1+255a^4}{256}
 =\frac{4252175491}{10363359375}
 <\frac{411}{1000}.
\tag{24}
\]

For one coordinate of \(A\), put

\[
 f(j):=\Pr(A_i=j)=\frac{1}{N^2}
 \begin{cases}
 j+1,&0\le j\le N-1,\\
 2N-1-j,&N\le j\le2N-2,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{25}
\]

Let \(U:=\lfloor T/2\rfloor\) coordinatewise and put \(K:=500\). Call \(T\) good if

\[
 K\le U_i\le2N-2-K\qquad(1\le i\le8).
\tag{26}
\]

For the actually generated \(T\), one has

\[
 U=A+H+J,\qquad J_i:=\left\lfloor\frac{C_i+G_i}{2}\right\rfloor\in\{0,1\}.
\]

Hence \(A_i\in[K,2N-4-K]\) for every \(i\) implies (26). The triangular law (25) and a union bound give

\[
 \Pr(T\text{ is not good})
 \le\frac{8(K+2)(K+3)}{N^2}
 =\frac{8\cdot502\cdot503}{10000^2}
 <\frac{21}{1000}.
\tag{27}
\]

Fix a good value \(t=2u+\tau\). A candidate color \(c\) determines bijectively

\[
 g=\tau\mathbin\oplus c,\qquad
 j_i=\left\lfloor\frac{c_i+g_i}{2}\right\rfloor.
\]

Conditioning on \(G=g\), its likelihood is

\[
 q(t-c)=\pi_g
 \sum_h\Pr(H=h\mid G=g)
 \prod_{i=1}^8 f(u_i-j_i-h_i).
\tag{28}
\]

Every shift \(j_i+h_i\) belongs to \(\{0,1,2\}\). From (25)--(26),

\[
 \frac{K-1}{K+1}
 \le\frac{f(u_i-j_i-h_i)}{f(u_i)}
 \le\frac{K+3}{K+1}.
\tag{29}
\]

Therefore the likelihood multiplier following \(\pi_g\) in (28), after division by \(\prod_if(u_i)\), lies between

\[
 L:=\left(\frac{K-1}{K+1}\right)^8
 \quad\text{and}\quad
 U_0:=\left(\frac{K+3}{K+1}\right)^8.
\]

The posterior collision probability at a good \(t\) is consequently at most

\[
 \left(\frac{U_0}{L}\right)^2\delta_0
 =\left(\frac{503}{499}\right)^{16}\delta_0.
\tag{30}
\]

The exact integer comparison \(7\cdot503^{16}<8\cdot499^{16}\) gives

\[
 \left(\frac{503}{499}\right)^{16}<\frac87.
\tag{31}
\]

Combining (22), (24), (27), and (30)--(31), while bounding a bad posterior collision by \(1\), gives

\[
 \delta
 <\frac{21}{1000}+\frac87\frac{411}{1000}
 =\frac{687}{1400}<\frac12.
\tag{32}
\]

Equations (21)--(22) and \(P_{\mathrm{tar}}=1/2\) now prove

\[
 \Theta=P_{\mathrm{tar}}(1-\delta)
 >\frac{P_{\mathrm{tar}}}{2}=\frac14.
\tag{33}
\]

In particular, (16) and (33) prove the deficit inequality in (4). Notice that (20)--(33) sum every positive orbit pair in (3); no diagonal-only thinning or omitted cross pair occurs.

It remains to exhibit the zero-cost cover. If both endpoints of a color-\(c\) orbit are survivors, (12) gives them as \(c+4z\) and \(c+4z'\), so their midpoint satisfies

\[
 t=c+2(z+z')\equiv c\pmod2.
\tag{34}
\]

A positive whole square label joins orbits of two distinct colors \(c\ne c'\) over the same physical target \(t\). If neither orbit contained a blocker, (34) would give simultaneously \(t\equiv c\pmod2\) and \(t\equiv c'\pmod2\), a contradiction. Hence every complete-product square label contains at least one blocker occurrence. This argument includes a zero orbit: its repeated source is either already a blocker, or its survivor midpoint still has parity equal to its color.

The dual of (5) is

\[
 \begin{aligned}
 \min\quad&\sum_m\tau_m z_m+\sum_\sigma\theta_\sigma s_\sigma\\
 \text{subject to}\quad
 &\sum_m\operatorname{mult}_m(\mathcal O_\sigma)z_m+s_\sigma\ge1,\\
 &z_m,s_\sigma\ge0.
 \end{aligned}
\tag{35}
\]

Set \(z_m:=1\) on blockers, \(z_m:=0\) elsewhere, and \(s_\sigma:=0\) for every label. The preceding paragraph proves every constraint in (35), with every repeated tag counted. Equation (17) gives \(\tau_m=0\) on the support of \(z\), so the objective is exactly zero. Nonnegativity of (5) and finite LP duality prove (6).

We finish by auditing the stated ledgers. The complete-product occurrence bound of accepted fact d5d5de35c3f25af9, with the whole-label multiplicities retained as in accepted fact 446c8f7967309a83, gives \(R_m\le2d_m\) and \(\sum_mR_m=4\Theta\). The identity (21) gives \(\Theta\le P_{\mathrm{tar}}=1/2\), proving (9). Also (15)--(17) give

\[
 \sum_m\min\{h_m,d_m\}=\sum_m\tau_m=\frac45.
\]

By (33), both right sides in (10) equal \(1-\Theta<3/4\), so the overlap inequalities of accepted fact 26568e8dd7d872e1 hold strictly. Every individual label also obeys the accepted atom scale: \(\beta\le\max_m d_m=1/(320N^8)\), and hence

\[
 \theta_\sigma\le2\min\{\beta_{\xi,t,[u]},\beta_{\eta,t,[v]}\}
 \le\frac1{160N^8}<\frac1{200}=\frac Q{200}.
\]

Finally, let \(z_\star\) be any lattice point outside the finite supports of \(d\) and \(\alpha\), and define the rational volume ledger

\[
 a_m:=2d_m+4\alpha_m+4\mathbf1_{\{m=z_\star\}}.
\tag{36}
\]

Then \(\sum_ma_m=2\sum_md_m+4\sum_m\alpha_m+4=8\), while \(\lambda_m=d_m\le a_m/2\), \(B_{c,m}\le\alpha_m\le a_m/4\), and \(R_m\le2d_m\le a_m\). Thus (8) and the first part of (11) hold. Since \(\Theta\le1/2\), the second part follows from

\[
 W-4\Theta=8-4\Theta\ge6.
\]

This verifies every claimed coefficient, pointwise-capacity, complete-product, repeated-tag, and global ledger exactly, while (35) has cost zero.

## External sources

none
