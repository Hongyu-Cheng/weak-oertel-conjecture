---
fact_id: cdf4b723cb4dc8ec
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct22-top-height-halfline-all-spatial-h3
depends_on: ["032423921efad6c8","604889294a17d7df","6edf2d6eb3514aa3","dbbd63823b5f4870"]
verifier_run: 4e5afef467f1439a
target_match: null
---

## Statement

Fix an integer \(k\ge8\). Use exactly the \(\rho_t=2^{-t}\) constructed support of 604889294a17d7df and the rooted-tree objects of 032423921efad6c8. Explicitly, put
$$
b_\ell=0\quad(1\le\ell<8),\qquad
b_\ell=\left\lfloor\frac{2^\ell}{8\ell}\right\rfloor\quad(8\le\ell\le k),
\qquad Q_0=0,\qquad Q_\ell=\sum_{r=1}^{\ell}b_r,\qquad Q=Q_k,
$$
$$
m=2(Q+1)^4,\qquad
n=\sum_{r=1}^{Q}m^r,\qquad N=n+1.
$$
Thus \(k\) is the height cutoff, \(Q\) is the tree depth, \(m\) is the branching number, and \(n\) is the spatial dimension. Put \(a_0=0\) and \(a_s=\ell\) whenever \(Q_{\ell-1}<s\le Q_\ell\).

The spatial coordinates are indexed by
$$
\mathcal T_{m,Q}=\bigcup_{r=1}^{Q}[m]^r.
$$
Choose any symmetric saturated chain partition of \(\lbrace0,1\rbrace^m\), with its nonterminal set \(D_m\) and injective successor
\(F_m(c)=c+e_{i_m(c)}\), where \(c_{i_m(c)}=0\), as in 032423921efad6c8. For a Boolean source \(b\), start at the empty root and select the child \(v i_m(b[v])\) whenever \(b[v]\in D_m\), stopping on the first failure or on reaching depth \(Q\). Here \(b[v]\) is the block of the \(m\) children of \(v\). Write the selected path as \(u_1,\ldots,u_{h(b)}\), and retain the original spatial points
$$
z_s(b)=b+2\sum_{r=1}^{s}e_{u_r},
\qquad 0\le s\le h(b).
$$
Their union is \(A_{m,Q}\); the level of a point is its number of coordinates equal to two. Retain the exact original height support
$$
\widehat A=
\left\lbrace
(z,t):z\in A_{m,Q},\
a_{\operatorname{level}(z)}\le t\le k,\
t\in\mathbb Z
\right\rbrace.
$$
In particular, none of \(b_\ell,Q,m,a_s,A_{m,Q},\widehat A\) is rebuilt when the following coefficients change.

For every \(\gamma\in\mathbb R^{\mathcal T_{m,Q}}\) and every real \(\zeta\ge-(\log 2)/2\), put
$$
w_{(z,t)}=\exp(\gamma\cdot z+\zeta t)
\quad((z,t)\in\widehat A),\qquad
w_{\mathbf I}=0\quad(\mathbf I\notin\widehat A),
$$
$$
W=\sum_{\mathbf I\in\widehat A}w_{\mathbf I},\qquad
p_{\mathbf I}=\frac{w_{\mathbf I}}W,
$$
and define
$$
\tau_p(\mathbf I)=
\inf\left\lbrace
p(H):H\subseteq\mathbb R^N
\text{ is a closed halfspace containing }\mathbf I
\right\rbrace,
\qquad
M_3(p)=\sum_{\mathbf I\in\widehat A}
p_{\mathbf I}\tau_p(\mathbf I)^3.
$$
Then
$$
M_3(p)\ge2^{-200}8^{-N}.
$$
There is no restriction on the signs, magnitudes, or homogeneity of the spatial coefficients. All original height atoms, the full original normalizer, and every containing closed halfspace of the original ambient space occur in this statement.

## Proof

Write
$$
\eta=2^{-m}|D_m|
=1-2^{-m}\binom m{m/2},
\qquad \delta=1-\eta,
\qquad
\mathcal L_s=\lbrace z\in A_{m,Q}:\operatorname{level}(z)=s\rbrace.
$$
The support, unique-source property, inverse reconstruction, and level census from 032423921efad6c8, with the exact parameter specialization and columns from 604889294a17d7df, give
$$
|\mathcal L_s|=2^n\eta^s\le2^n,\qquad
0<\delta<(Q+1)^{-2},\qquad
\eta^Q>\frac34.
\tag{1}
$$
The last inequality also follows from
\(\eta^Q\ge1-Q\delta>1-Q/(Q+1)^2>3/4\), since \(Q\ge4\).
Directly, \(b_8=4\) and \(b_9=7\). Thus \(k=8\) gives \(Q=4\), whereas \(k\ge9\) gives \(Q\ge11\). In particular, \(Q<7\) or \(Q\ge11\) exhausts all cases. All columns are nonempty and all the displayed weights on the support are positive.

We first establish the conditional estimates that will be used with the new height weights. For a nonempty spatial class \(E\subseteq A_{m,Q}\), let \(\widehat E\) retain every original allowed height of every point of \(E\). Let \(\nu_{\widehat E}\) be the restriction of the unnormalized weighted measure to \(\widehat E\), let \(W_{\widehat E}>0\) be its mass, and let \(p^{\widehat E}=\nu_{\widehat E}/W_{\widehat E}\). For an index \(\mathbf I\in\widehat E\), set
$$
h_{\nu_{\widehat E}}(\mathbf I)=
\inf_{H\ni\mathbf I}\nu_{\widehat E}(H)
=W_{\widehat E}\tau_{p^{\widehat E}}(\mathbf I),
$$
where the infimum is over all original ambient closed halfspaces. Every such halfspace contains the atom itself, so
$$
M_3(p^{\widehat E})
=W_{\widehat E}^{-4}
\sum_{\mathbf I\in\widehat E}
w_{\mathbf I}h_{\nu_{\widehat E}}(\mathbf I)^3
\ge W_{\widehat E}^{-4}
\sum_{\mathbf I\in\widehat E}w_{\mathbf I}^4.
\tag{2}
$$
For a finite partition into nonempty lifted spatial classes, put
\(\alpha_{\widehat E}=W_{\widehat E}/W\). On \(\widehat E\), every containing halfspace has full probability at least \(\alpha_{\widehat E}\) times its conditional probability. Therefore
$$
M_3(p)\ge
\sum_{\widehat E}\alpha_{\widehat E}^{\,4}M_3(p^{\widehat E}).
\tag{3}
$$
If \(M_3(p^{\widehat E})\ge8^{-n}\kappa_{\widehat E}\), with every \(\kappa_{\widehat E}>0\), Hölder gives
$$
M_3(p)\ge
8^{-n}\left(\sum_{\widehat E}\kappa_{\widehat E}^{-1/3}\right)^{-3}.
\tag{4}
$$
Indeed,
$$
1=\sum_{\widehat E}\alpha_{\widehat E}
\le
\left(\sum_{\widehat E}\kappa_{\widehat E}
\alpha_{\widehat E}^{\,4}\right)^{1/4}
\left(\sum_{\widehat E}\kappa_{\widehat E}^{-1/3}\right)^{3/4}.
$$
Empty classes are omitted before defining a conditional measure.

For any probability law \(q\) on finitely many ordered heights, define its closed-tail depth at \(t\) by
$$
d_q(t)=\min\left(
\sum_{r\le t}q_r,\ \sum_{r\ge t}q_r
\right).
$$
The heights where the first sum is less than \(1/4\) form an initial segment of total mass less than \(1/4\); the analogous final segment for the second sum also has mass less than \(1/4\). Consequently the heights where both sums are at least \(1/4\) have mass at least \(1/2\). It follows that
$$
\sum_tq_t d_q(t)^3\ge\frac1{128}.
\tag{5}
$$
This uses closed tails, so it also applies when a single atom carries most or all of the mass.

For the present weights, write
$$
L_s^{\mathrm{ht}}(\zeta)=\sum_{t=a_s}^{k}e^{\zeta t}.
$$
This is the height-tail notation of dbbd63823b5f4870 with the height coefficient made explicit; its value at \(\zeta=-\log 2\) is that predecessor's height tail. Suppose that \(E\) is a nonempty subset of one level \(s\), with arbitrary positive spatial weights \(v_z\), and its lifted weights are \(v_ze^{\zeta t}\). Its conditional law factors as
$$
p^{\widehat E}_{(z,t)}
=r_z\,q_t,\qquad
r_z=\frac{v_z}{\sum_{x\in E}v_x},
\qquad
q_t=\frac{e^{\zeta t}}{L_s^{\mathrm{ht}}(\zeta)}
\quad(a_s\le t\le k).
$$
The intersection of a containing ambient closed halfspace with the same vertical column is a closed upper tail, a closed lower tail, or the whole column, and contains the sample height \(t\). Hence
\(\tau_{p^{\widehat E}}(z,t)\ge r_zd_q(t)\). Equation (5) yields
$$
M_3(p^{\widehat E})
\ge\frac1{128}\sum_{z\in E}r_z^4
\ge\frac1{128|E|^3}.
\tag{6}
$$
The last inequality is the finite Hölder inequality
\((\sum x_j)^4\le K^3\sum x_j^4\).
Thus (6) is independent of the column length and of the height coefficient.

If \(Q<7\), partition by all \(Q+1\le7\) spatial levels. By (1) and (6), each has conditional moment at least \(8^{-n}/128\). Equation (4) gives
$$
M_3(p)\ge\frac{8^{-n}}{128\cdot7^3}
>2^{-16}8^{-N}.
\tag{7}
$$
This proves the requested bound in that case, including \(k=8\). For the rest of the proof assume \(Q\ge11\).

The required new height normalizer is the sum over the positive spatial levels:
$$
R_{\mathrm{pos}}(\zeta)
=\sum_{s=1}^{Q}L_s^{\mathrm{ht}}(\zeta).
$$
We claim that, for every \(k\ge8\) and every \(\zeta\ge-(\log 2)/2\),
$$
R_{\mathrm{pos}}(\zeta)\le64Qe^{\zeta k}.
\tag{8}
$$
For integers \(\ell\ge8\), induction gives
$$
\sum_{j=8}^{\ell}\frac{2^j}{j}
\le\frac{4\cdot2^\ell}{\ell},
\qquad
Q_\ell\le\frac{2^{\ell-1}}{\ell}.
$$
The first inequality holds at \(\ell=8\). In its induction step the preceding bound plus the new term is at most the proposed bound because
\(2/(\ell-1)+1/\ell\le4/\ell\) for \(\ell\ge9\). The second inequality follows by using \(b_j\le2^j/(8j)\). Moreover \(2^k/(8k)\ge4\), so
$$
Q\ge b_k
\ge\frac{2^k}{16k}.
$$
At an integer height \(t\ge8\), exactly \(Q_t\) positive levels have entered. Swapping the two finite sums and putting \(r=k-t\) therefore gives
$$
\begin{aligned}
\frac{R_{\mathrm{pos}}(\zeta)}{Qe^{\zeta k}}
&=\sum_{r=0}^{k-8}e^{-\zeta r}\frac{Q_{k-r}}Q\\
&\le8\sum_{r=0}^{k-8}\frac{k}{k-r}\,2^{-r/2}.
\end{aligned}
\tag{9}
$$
For \(r\le k/2\) the sum on the right is at most
\(16/(1-2^{-1/2})<56\).
For \(r>k/2\), the denominator \(k-r\) is at least eight, so the remaining portion is at most
$$
\frac{k2^{-k/4}}{1-2^{-1/2}}<7.
$$
Here \(k2^{-k/4}\le2\) for \(k\ge8\): it equals two at eight and is nonincreasing on that real interval, since its logarithmic derivative is \(1/k-(\log 2)/4\le0\), using \(\log 2\ge1/2\). Also
\((1-2^{-1/2})^{-1}=2+\sqrt2<7/2\).
Empty portions of either split contribute zero. Thus (9) is less than \(63\), which proves (8). The estimate includes equality at the allowed lower endpoint for \(\zeta\) in the first inequality of (9), and has no upper restriction on \(\zeta\). Level zero was excluded from \(R_{\mathrm{pos}}\); it is handled by (6).

We now prove an interface on the original support for a polynomial-size forest. Let a nonempty family of \(B\) full rooted paths of length \(Q\) be given, with
$$
1\le B\le64(Q+1)^{11}.
$$
Let \(P_j\) be their depth-\(j\) node sets, including \(P_0=\lbrace\varnothing\rbrace\), and set
$$
S=\bigcup_{j=0}^{Q-1}\ \bigcup_{v\in P_j}
\lbrace vi:1\le i\le m\rbrace,
\qquad
U=S\cup\lbrace u:|u|\le7\rbrace,\qquad n_U=|U|.
\tag{10}
$$
These are exactly the forest objects of 6edf2d6eb3514aa3, including its distinction between the node sets \(P_j\) and the coordinate set \(S\). In particular, an exit child of a forest node can still be in \(S\).

Let \(G\) be any positive function on
\(R_U=\lbrace z|_U:z\in A_{m,Q}\rbrace\). Let a field \(\lambda\) vanish on \(U\), and define, for any field \(\theta\),
$$
\Pi(\theta)=
\max_{v_0,\ldots,v_Q}
\sum_{j=0}^{Q-1}\sum_{i=1}^{m}|\theta_{v_ji}|,
\tag{11}
$$
where \(v_0=\varnothing\) and \(v_{j+1}\) is a child of \(v_j\). This is the child-block convention of dbbd63823b5f4870 and 6edf2d6eb3514aa3, without any rescaling. Put \(P_\lambda=\Pi(\lambda)\), and suppose \(P_\lambda\le1\).
In the interface, let the weights on the same original support be
$$
v_z=G(z|_U)e^{\lambda\cdot z},
\qquad w_{(z,t)}=v_ze^{\zeta t},
\tag{12}
$$
and let \(W,p\) and their conditional laws have the definitions already given, for this table. We will prove
$$
M_3(p)\ge2^{-96}8^{-N}.
\tag{13}
$$
The original field \(\gamma\) will be identified with (12) after the interface is proved.

Use the following spatial partition, exactly as in 6edf2d6eb3514aa3. There are seven early classes of levels \(0,\ldots,6\). The class \(\mathrm{GOOD}\) consists of points of level \(s\ge7\) whose seventh selected node \(u_7\) is outside \(P_7\). For \(7\le j\le Q\), the class \(\mathrm{STOP}_j\) consists of level-\(j\) points with \(u_j\in P_j\). For \(7\le j<Q\), the class \(\mathrm{BRANCH}_j\) consists of points of level at least \(j+1\) with \(u_j\in P_j\) and \(u_{j+1}\notin P_{j+1}\). The STOP condition describes the level of the point; it does not require the source to fail its next forward test. Ancestor closure of the forest makes this a disjoint exhaustive partition. Lift every class by keeping all its original heights.

We use the following purely spatial conclusions proved in 6edf2d6eb3514aa3, with the identical \(P_j,S,U\) and chain partition. If \(\mathcal B_j\) is the set of level-\((j+1)\) anchors of \(\mathrm{BRANCH}_j\), then
$$
|\mathrm{STOP}_j|\le2^nB\delta^j,
\qquad
|\mathcal B_j|\le2^nB\delta^j.
\tag{14}
$$
These bounds count the original sources. In detail, the fraction of block patterns selecting any prescribed direction \(i\) is
\(\vartheta_i=2^{-m}|\lbrace c\in D_m:i_m(c)=i\rbrace|\le\delta\), because each symmetric chain adds coordinate \(i\) at most once. Prescribing a length-\(j\) forest path therefore gives \(2^n\prod_{r=1}^j\vartheta_{i_r}\) sources. Sum over its at most \(B\) terminal nodes. For a branch anchor the additional exit test has total permitted fraction at most one, giving the same bound. Unique sources and the disjoint visited child blocks justify these counts.

For a branch point, its level-\((j+1)\) anchor has the same full Boolean source. All spikes after the anchor are outside \(U\). Indeed, the first exit spike may lie in \(S\), and is retained in the anchor; every later spike has its parent outside the ancestor-closed forest and has depth greater than seven. Thus the anchor and point have exactly the same \(G\)-multiplier. At a fixed later level the map to anchors is injective by parity, and their spatial weights have ratio at most \(e^{2P_\lambda}\).

For GOOD, let
$$
\mathcal L=
\lbrace z|_U:z\in\mathrm{GOOD},\
\operatorname{level}(z)=7\rbrace.
$$
If GOOD is nonempty, this label set is nonempty. Every GOOD point has the same \(U\)-label as its level-seven anchor. Conversely every \(\omega\in\mathcal L\) at level seven occurs with every Boolean assignment outside \(U\), and parity on \(\mathcal L\) is injective. Hence
$$
|\mathcal L|\le2^{n_U}.
\tag{15}
$$
These are the full labels in 6edf2d6eb3514aa3; they include all of \(S\), rather than merely coordinates on the spines. The reason is that the first seven tests and their spikes depend only on the fixed coordinates in \(U\), and every later selected coordinate is outside \(U\).

For \(7\le s\le Q\) and \(\omega\in\mathcal L\), let \(\mathcal C_s(\omega)\) be the GOOD level-\(s\) points with this label whose canonical inverse reconstruction from 032423921efad6c8 succeeds through depth \(Q\). For any \(\theta\) vanishing on \(U\), put
$$
Z_\theta^{\mathrm{out}}=
\prod_{u\notin U}(1+e^{\theta_u}).
$$
An empty product is one. This is exactly the outside normalizer of 6edf2d6eb3514aa3; its full Boolean normalizer is \(Z_\theta=2^{n_U}Z_\theta^{\mathrm{out}}\). The complete-reconstruction census proved there is
$$
\sum_{z\in\mathcal C_s(\omega)}e^{\theta\cdot z}
\ge
\eta^{Q-7}e^{-3\Pi(\theta)}Z_\theta^{\mathrm{out}}.
\tag{16}
$$
For completeness, the census uses \(s-7\) forward block tests in \(D_m\), followed by \(Q-s\) inverse block tests in \(\operatorname{im}F_m\), starting after the seven fixed tests. Their \(Q-7\) fresh child blocks are disjoint and outside \(U\). Under fair outside bits their success probability is \(\eta^{Q-7}\). Their disjoint successful transcript cylinders have product-law probability at least \(e^{-\Pi(\theta)}\) times their fair probability, since a revealed bit has likelihood ratio
\(2e^{\theta_ub_u}/(1+e^{\theta_u})\ge e^{-|\theta_u|}\).
The forward spikes have field factor at least \(e^{-2\Pi(\theta)}\), and parity and inverse injectivity identify the resulting points exactly with \(\mathcal C_s(\omega)\). This gives (16). In particular, (14)--(16) have no height weights in their definitions or proofs. No moment assertion at the predecessor's fixed height coefficient is being transferred here.

The seven early classes have, by (1) and (6),
$$
M_3(p^{\widehat E})\ge8^{-n}/128.
\tag{17}
$$
For a nonempty STOP class, put \(K_j=|\mathrm{STOP}_j|\) and
\(L_j=\sum_{z\in\mathrm{STOP}_j}v_z\).
Its full mass is \(L_j^{\mathrm{ht}}(\zeta)L_j\), which by (8) is at most \(64Qe^{\zeta k}L_j\). Retain only its actual top atoms \((z,k)\) in (2), and use finite Hölder. In view of (14),
$$
\begin{aligned}
M_3(p^{\widehat{\mathrm{STOP}}_j})
&\ge\frac{e^{4\zeta k}\sum_zv_z^4}
{(64Qe^{\zeta k}L_j)^4}\\
&\ge\frac1{(64Q)^4K_j^3}
\ge8^{-n}\frac1{(64Q)^4(B\delta^j)^3}.
\end{aligned}
\tag{18}
$$
Here \(L_j^{\mathrm{ht}}\) denotes the previously defined height tail, whereas the undecorated \(L_j\) in this paragraph is a spatial sum.

For a nonempty BRANCH class, let
\(L_j^{\mathrm b}=\sum_{z\in\mathcal B_j}v_z\).
The injective anchor maps and the spatial ratio established above show that its full mass, including all later levels and all their heights, is at most
$$
e^{2P_\lambda}L_j^{\mathrm b}
\sum_{s=j+1}^{Q}L_s^{\mathrm{ht}}(\zeta)
\le64Qe^{\zeta k}e^{2P_\lambda}L_j^{\mathrm b}.
$$
Its actual top anchor atoms have fourth-weight sum
\(e^{4\zeta k}\sum_{z\in\mathcal B_j}v_z^4\).
Applying (2), finite Hölder, and (14) gives
$$
M_3(p^{\widehat{\mathrm{BRANCH}}_j})
\ge8^{-n}
\frac{e^{-8}}{(64Q)^4(B\delta^j)^3}.
\tag{19}
$$
The first exit spike was included in every anchor; thus no comparison between different \(G\)-labels occurs in (19).

Suppose GOOD is nonempty. Define
$$
\mathfrak g_1=\sum_{\omega\in\mathcal L}G(\omega),
\qquad
\mathfrak g_4=\sum_{\omega\in\mathcal L}G(\omega)^4.
$$
Finite Hölder, (15), and \((1+x)^4\le8(1+x^4)\) for \(x>0\) give
$$
\frac{\mathfrak g_4}{\mathfrak g_1^4}\ge8^{-n_U},
\qquad
\frac{Z_{4\lambda}^{\mathrm{out}}}
{(Z_\lambda^{\mathrm{out}})^4}
\ge8^{-(n-n_U)}.
\tag{20}
$$
At any fixed level \(s\ge7\) and fixed label, parity injects the GOOD points into all Boolean assignments outside \(U\). The seven first spikes have zero \(\lambda\)-field, and the other spikes increase the spatial field factor by at most \(e^{2P_\lambda}\). Therefore, keeping all original heights in the normalizer and using (8),
$$
W_{\widehat{\mathrm{GOOD}}}
\le e^{2P_\lambda}\mathfrak g_1
Z_\lambda^{\mathrm{out}}
\sum_{s=7}^{Q}L_s^{\mathrm{ht}}(\zeta)
\le64Qe^{\zeta k}e^{2P_\lambda}
\mathfrak g_1Z_\lambda^{\mathrm{out}}.
\tag{21}
$$

Fix \(z\in\mathcal C_s(\omega)\), with \(7\le s<Q\), and use its actual top-height sample \((z,k)\). Let \(u_{s+1},\ldots,u_Q\) be its inverse continuation, and put
$$
V_r=\sum_{q=s+1}^{r}e_{u_q}\qquad(s<r\le Q).
$$
The complete inverse reconstruction in 032423921efad6c8 gives the original spatial endpoint pair \(z-V_r,z+V_r\), with levels \(s,r\), respectively. Both endpoints are still GOOD and have \(U\)-label \(\omega\): all modified coordinates descend from \(u_7\notin P_7\) and have depth greater than seven, so are outside \(U\). Every column reaches height \(k\). Thus
$$
(z-V_r,k),\qquad (z+V_r,k)
\tag{22}
$$
are original indices in \(\widehat{\mathrm{GOOD}}\), and their midpoint is exactly \((z,k)\).

All \(2(Q-s)\) endpoints in (22) are distinct. Upper endpoints have the distinct levels \(r>s\); lower endpoints have level \(s\) and distinct nested nonzero displacements \(V_r\); an upper endpoint cannot equal a lower endpoint because their levels differ. Every ambient closed halfspace containing the sample contains at least one endpoint from each pair, since the value of its defining linear functional at the midpoint is the average of its endpoint values. This holds whatever the height coefficient of that halfspace is. Also
\(\left|\lambda\cdot V_r\right|\le P_\lambda\), by the child-block convention (11). Every endpoint therefore has weight at least
\(e^{\zeta k}G(\omega)e^{\lambda\cdot z-P_\lambda}\).
We conclude, for every such original sample, that
$$
h_{\nu_{\widehat{\mathrm{GOOD}}}}(z,k)
\ge (Q-s)e^{\zeta k}G(\omega)
e^{\lambda\cdot z-P_\lambda}.
\tag{23}
$$
This is a direct estimate for every containing original ambient closed halfspace.

Put \(T_{\mathrm{tail}}=Q-6\ge5\) and
\(h_*=\lfloor T_{\mathrm{tail}}/2\rfloor\).
Retain samples only at the first \(h_*\) levels \(s=7,\ldots,6+h_*\), and only their points in the sets \(\mathcal C_s(\omega)\). These are actual top atoms and are distinct across levels and labels. At these levels
$$
h_*\ge T_{\mathrm{tail}}/3,\qquad
Q-s\ge T_{\mathrm{tail}}/2,\qquad
T_{\mathrm{tail}}/Q\ge1/3.
\tag{24}
$$
Use the cube of (23) against their actual sampling weights, then (16) with \(\theta=4\lambda\), for which \(\Pi(4\lambda)=4P_\lambda\). Keeping the fourth power of the full conditional normalizer gives
$$
\begin{aligned}
M_3(p^{\widehat{\mathrm{GOOD}}})
&\ge
\frac{e^{4\zeta k-3P_\lambda}}
{W_{\widehat{\mathrm{GOOD}}}^4}
\sum_{s=7}^{6+h_*}(Q-s)^3
\sum_{\omega\in\mathcal L}G(\omega)^4
\sum_{z\in\mathcal C_s(\omega)}e^{4\lambda\cdot z}\\
&\ge
\frac{\eta^{Q-7}e^{-23P_\lambda}}
{(64Q)^4}
h_*(T_{\mathrm{tail}}/2)^3
\frac{\mathfrak g_4}{\mathfrak g_1^4}
\frac{Z_{4\lambda}^{\mathrm{out}}}
{(Z_\lambda^{\mathrm{out}})^4}\\
&\ge
8^{-n}\frac{e^{-23}}{32\cdot81\cdot64^4}
>2^{-96}8^{-n}.
\end{aligned}
\tag{25}
$$
In the second line the exponential cost is three from the cubed depth, twelve from the fourth-field census, and eight from the fourth normalizer (21); the four factors \(e^{\zeta k}\) cancel exactly. The third line uses (1), (20), and (24):
\((3/4)(T_{\mathrm{tail}}^4/24)/(64Q)^4
\ge1/(32\cdot81\cdot64^4)\).
For the last generous numerical estimate, \(e^{23}<3^{23}<2^{37}\), while \(32\cdot81\cdot64^4<2^{36}\). Thus the displayed coefficient is in fact greater than \(2^{-73}\).

We finish the interface using (4). The valid coefficients furnished by (17)--(19) and (25) are
$$
\begin{aligned}
\kappa_{\mathrm{early},s}&=1/128
&& (0\le s\le6),\\
\kappa_{\widehat{\mathrm{STOP}}_j}
&=\frac1{(64Q)^4(B\delta^j)^3}
&& (7\le j\le Q),\\
\kappa_{\widehat{\mathrm{BRANCH}}_j}
&=\frac{e^{-8}}{(64Q)^4(B\delta^j)^3}
&& (7\le j<Q),\\
\kappa_{\widehat{\mathrm{GOOD}}}&=2^{-96}.
\end{aligned}
\tag{26}
$$
As always, only nonempty classes enter the sum. The early contribution to
\(\sum\kappa^{-1/3}\) is less than \(42\), and the GOOD contribution, if present, is \(2^{32}\). From the forest-size bound and (1),
$$
BQ^{4/3}\delta^7
\le64\frac{Q^{4/3}}{(Q+1)^3}
\le64,\qquad
\frac1{1-\delta}<2.
$$
Consequently the combined STOP and BRANCH contribution is at most
$$
64^{4/3}(1+e^{8/3})
\frac{BQ^{4/3}\delta^7}{1-\delta}
<
256\cdot28\cdot64\cdot2
<2^{20},
\tag{27}
$$
using \(e^{8/3}<27\). The total capacity is less than
\(2^{32}+2^{20}+42<2^{33}\). Equation (4) yields
$$
M_3(p)>2^{-99}8^{-n}=2^{-96}8^{-N},
$$
which proves (13). This proves the new interface with the new height normalizer and actual top-height halfspace witnesses, for arbitrary positive \(G\).

It remains to cover every original spatial field \(\gamma\). We use the spatial transcript-entropy estimate of dbbd63823b5f4870 with its exact original support. Put
$$
R(x)=\frac{8(1+e^{4x})}{(1+e^x)^4},
\qquad \beta_u=\log R(\gamma_u),
\qquad \varepsilon=\frac1{mQ}.
$$
Choose exactly \(mQ\) coordinates with the largest values of \(\beta_u\), calling this set \(T_0\), and put
\(E_{\mathrm{rem}}=\sum_{u\notin T_0}\beta_u\).
This choice exists because \(n\ge mQ\). The accepted scalar properties in dbbd63823b5f4870 give nonnegative \(\beta_u\), evenness and monotonicity of \(R\) in absolute value, and
\(\log R(x)\ge x^2/3\) for \(0\le x\le\log 2\). Its spatial conclusion, independent of every height coefficient, is
$$
Z_s(\gamma)=\sum_{z\in\mathcal L_s}e^{\gamma\cdot z},
\qquad
\frac{Z_s(4\gamma)}{Z_s(\gamma)^4}
\ge8^{-n}e^{E_{\mathrm{rem}}}
\quad(0\le s\le Q).
\tag{28}
$$

First suppose \(E_{\mathrm{rem}}\ge\log(8m)\). The full original mass of level \(s\) is
\(W_s=L_s^{\mathrm{ht}}(\zeta)Z_s(\gamma)\).
Some level \(s_*\) has \(W_{s_*}/W\ge1/(Q+1)\). Its conditional law has spatial probabilities proportional to \(e^{\gamma\cdot z}\) and the common original height law. Equations (3), (6), and (28), with that one class retained, show
$$
M_3(p)\ge
\frac{8^{-n}e^{E_{\mathrm{rem}}}}
{128(Q+1)^4}.
$$
Since \(m=2(Q+1)^4\) and \(N=n+1\),
$$
8^NM_3(p)\ge\frac{e^{E_{\mathrm{rem}}}}{8m}\ge1.
\tag{29}
$$
Thus large spatial entropy proves the requested bound with the actual height law, even if a single top atom has arbitrarily small conditional probability.

Now suppose \(E_{\mathrm{rem}}<\log(8m)\). This threshold differs from the fixed-height threshold in dbbd63823b5f4870, so we check the required cardinality anew. Define
$$
T=T_0\cup
\lbrace u\notin T_0:|\gamma_u|>\varepsilon\rbrace.
$$
Here \(0<\varepsilon\le1/8<\log 2\). Each additional coordinate contributes at least \(\varepsilon^2/3\) to \(E_{\mathrm{rem}}\), by the accepted scalar properties just stated. Therefore
$$
|T|\le mQ+3m^2Q^2E_{\mathrm{rem}}
<mQ+3m^2Q^2\log(8m).
\tag{30}
$$
For \(Q\ge4\),
$$
\log(8m)=4\log 2+4\log(Q+1)\le4(Q+1),
$$
using \(\log 2<1\) and \(\log(Q+1)\le Q\). Hence
$$
\begin{aligned}
|T|
&<2Q(Q+1)^4+48Q^2(Q+1)^9\\
&\le50(Q+1)^{11}
<64(Q+1)^{11}.
\end{aligned}
\tag{31}
$$
Outside \(T\), the coefficients have magnitude at most \(\varepsilon\). Every full path contains exactly \(Q\) disjoint child blocks of \(m\) coordinates, so
$$
\Pi\bigl(\gamma\mathbf1_{\mathcal T_{m,Q}\setminus T}\bigr)
\le mQ\varepsilon=1.
\tag{32}
$$

For every coordinate in the nonempty set \(T\), choose a full rooted path through that node, and discard duplicate paths. Their number \(B\) is at least one and at most \(|T|\), hence satisfies the forest threshold by (31). Form \(P_j,S,U\) as in (10). Each coordinate of \(T\) is a child of a node on one chosen path, so \(T\subseteq S\subseteq U\). Define
$$
\lambda_u=
\begin{cases}
0,&u\in U,\\
\gamma_u,&u\notin U,
\end{cases}
\qquad
G(\omega)=
\exp\left(\sum_{u\in U}\gamma_u\omega_u\right)
\quad(\omega\in R_U).
$$
The function \(G\) is positive, \(\lambda\) vanishes on \(U\), and (32) gives \(\Pi(\lambda)\le1\), since \(T\subseteq U\). At every original index,
$$
G(z|_U)e^{\lambda\cdot z+\zeta t}
=e^{\gamma\cdot z+\zeta t}
=w_{(z,t)}.
$$
The new forest interface (13) therefore applies to the original law exactly, and gives the stronger bound \(M_3(p)\ge2^{-96}8^{-N}\) in this case. Together with (7) and (29), this proves the asserted \(2^{-200}8^{-N}\) bound for all \(k\ge8\), all spatial fields, and the entire stated height half-line.

Every conditional denominator in the proof retained every original height in its class. The exhaustive partition and (3)--(4) retained the full original normalizer. The common-top-height pairs and the column tails were tested against all original containing closed ambient halfspaces. No support parameter was changed, and no comparison of the full tilted law with a fixed-height law was used.

## External sources

None. Accepted fact 032423921efad6c8 supplies the chain/tree support, unique sources, inverse pairs, and level counts. Accepted fact 604889294a17d7df supplies the original height support and its exact parameter specialization. The forest objects, source counts, label geometry, and height-independent complete-reconstruction census are used from 6edf2d6eb3514aa3 with the explicit maps above. The spatial entropy ratio and scalar entropy properties are used from dbbd63823b5f4870. The vertical closed-tail estimate, positive-level height normalizer, conditional top-height moment estimates, capacity sum for the new height range, and the changed entropy threshold are proved here.
