---
fact_id: 9cffeaea85f6fe61
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3an-all-separable-log-concave-profile-packing
depends_on: ["0dc72eecb73c50bd","15da936de919780f","488f0a583886b5fc","8660ffca617b9702"]
verifier_run: ad13e097a4ec409b
target_match: null
---

## Statement

Let \(N\ge1\) be an integer. For each \(i\in\{1,\ldots,N\}\), let \(a_i,b_i\in\mathbb Z\), \(a_i\le b_i\), and let \(w^i=(w^i_t)_{t\in\mathbb Z}\) be positive on \(D_i=\{a_i,\ldots,b_i\}\), zero elsewhere, and satisfy \((w^i_t)^2\ge w^i_{t-1}w^i_{t+1}\) for every integer \(t\). Set

\[
\begin{aligned}
W_i&=\sum_{t\in D_i}w^i_t,&
w_{\max,i}&=\max_{t\in D_i}w^i_t,&
\phi^i_t&=\log\frac{w_{\max,i}}{w^i_t}\quad(t\in D_i),\\
D&=\prod_{i=1}^N D_i,&
w_{\mathbf I}&=\prod_{i=1}^N w^i_{I_i}\quad(\mathbf I\in D),&
W&=\sum_{\mathbf I\in D}w_{\mathbf I}=\prod_{i=1}^N W_i.
\end{aligned}
\]

Put \(w_{\mathbf I}=0\) off \(D\). Its canonical maximum and potential are \(w_{\max}=\prod_iw_{\max,i}\) and \(\phi_{\mathbf I}=\log(w_{\max}/w_{\mathbf I})=\sum_i\phi^i_{I_i}\). All logarithms are natural. Here \(N\) is the integer dimension \(n\) of accepted fact `488f0a583886b5fc`; \(D,w,W,w_{\max},\phi\) retain that fact's meanings. The indexed scalar quantities \(D_i,W_i,w_{\max,i},\phi^i\) are its corresponding one-dimensional objects for profile \(w^i\).

For completeness, use precisely the following canonical score. At \(\mathbf J\in D\), let \(\mathcal E_{\mathbf J}\) consist of the nonempty affinely independent \(E\subseteq D\) with \(\mathbf J\in\operatorname{relint}\operatorname{conv}E\), and let \(\lambda_{E,\mathbf I}>0\) be their unique barycentric coefficients. Define

\[
\begin{aligned}
G_E&=\sum_{\mathbf I\in E}\lambda_{E,\mathbf I}\phi_{\mathbf I}-\phi_{\mathbf J},
&\mathcal E_{\mathbf J}^{\log}(L)&=\{E\in\mathcal E_{\mathbf J}:G_E\le L\},\\
P_{\log}(\mathbf J,L;w)
&=\max\left\{\sum_{E\in\mathcal E_{\mathbf J}^{\log}(L)}x_E:
 x_E\ge0,\quad
 \sum_{\substack{E\in\mathcal E_{\mathbf J}^{\log}(L)\\\mathbf I\in E}}x_E\le w_{\mathbf I}
 \ (\mathbf I\in D)\right\},\\
\mathcal B_{\log}(w)&=\max_{\mathbf J\in D,\ L\ge0}\frac{P_{\log}(\mathbf J,L;w)}{1+L}.
\end{aligned}
\]

Each source in a component is charged the full component mass, independently of its barycentric coefficient, and the singleton \(\{\mathbf J\}\) is allowed. These are exactly the definitions and full-occurrence capacities in `488f0a583886b5fc`.

Every table above is globally extendable, and there is one absolute \(c>0\) such that \(\mathcal B_{\log}(w)\ge c\,2^{-N}W\) for all these profiles and all \(N\). One explicit choice, without constant optimization, is

\[
K_\ast=64000,\qquad M_\ast=(16\cdot27000)^2,
\qquad
c=\frac{e^{-8800K_\ast}}{2(1+8M_\ast)}
\left(\frac{e^{-8}}2\right)^{M_\ast}.
\]

## Proof

Taking logarithms of scalar log-concavity shows that the successive differences of each \(\phi^i\) are nondecreasing. Its piecewise-affine interpolation on \([a_i,b_i]\) is therefore convex; for a singleton interval it is simply its value zero. The sum of these interpolations is convex on \(\prod_i[a_i,b_i]=\operatorname{conv}D\), agrees with \(\phi\) at all sites of \(D\), and proves convex-admissibility for every barycentric representation. Also \((\operatorname{conv}D)\cap\mathbb Z^N=D\). The globally extendable-table equivalence in accepted fact `488f0a583886b5fc` thus applies, including when some intervals are singletons.

For each coordinate define

\[
R_i=\max_{J\in D_i}\sum_{v\in\mathbb Z}\sqrt{w^i_{J+v}w^i_{J-v}},
\qquad
\delta_i=\frac{R_i}{W_i}-\frac12,
\qquad
p^i_{\max}=\frac{w_{\max,i}}{W_i}.
\]

Here \(R_i\) is exactly \(R_{1/2}(w^i)\) of accepted fact `8660ffca617b9702`, and the sum at any fixed center is that fact's \(\mathcal R_J(w^i)\). Cauchy-Schwarz bounds every centered sum by \(W_i\), since each of the two shifted weight sums over all integers equals \(W_i\). Accepted fact `8660ffca617b9702` gives the other bound \(R_i\ge W_i/2\). Hence \(0\le\delta_i\le1/2\).

First freeze every coordinate with \(p^i_{\max}\ge1/2\) at any mode \(J_i\). Its retained atom \(w^i_{J_i}=w_{\max,i}\) is at least its benchmark \(W_i/2\), and its displacement and logarithmic cost are zero. Call this coordinate set \(\mathcal F_0\). For every remaining coordinate, \(p^i_{\max}<1/2\) and \(\delta_i>0\): if \(\delta_i=0\), the equality characterization in `8660ffca617b9702` gives two equal adjacent weights, contrary to \(p^i_{\max}<1/2\). Partition the remaining coordinates into the near-critical coordinates \(0<\delta_i<1/27000\) and the moderate coordinates \(\delta_i\ge1/27000\).

We next prove the pooling estimate used for groups of coordinates. At any chosen center \(J_i\in D_i\), put

\[
\begin{aligned}
\mathcal U_i&=\{v\in\mathbb Z:J_i+v,J_i-v\in D_i\},\\
G_i(v)&=\frac{\phi^i_{J_i+v}+\phi^i_{J_i-v}}2-\phi^i_{J_i},&
A_i(v)&=\frac{\phi^i_{J_i+v}-\phi^i_{J_i-v}}2,\\
\alpha_i(v)&=\min\{w^i_{J_i+v},w^i_{J_i-v}\}.
\end{aligned}
\]

These are exactly the scalar \(\mathcal U_J,G_J,A_J,\alpha_J\) of accepted facts `15da936de919780f` and `0dc72eecb73c50bd`, with profile \(w^i\) and center \(J=J_i\); \(\alpha_i\) is also the suppressed-center \(\alpha\) of `488f0a583886b5fc`. In particular \(G_i\ge0\), \(G_i\) is even, \(A_i\) is odd, and \(G_i(0)=A_i(0)=0\). Whenever \(J_i\) is a maximizing Hellinger center, define \(Q_i(v)=\sqrt{w^i_{J_i+v}w^i_{J_i-v}}/R_i\) on \(\mathcal U_i\). This is precisely the auxiliary displacement probability \(Q_{J_i}\) of those two accepted facts, not the source probability \(w^i/W_i\).

Let \(\mathcal I\) be a nonempty set of coordinates used at maximizing centers, and take independent displacements with the product probability \(Q_{\mathcal I}=\prod_{i\in\mathcal I}Q_i\). Write

\[
\begin{aligned}
\mathcal U_{\mathcal I}&=\prod_{i\in\mathcal I}\mathcal U_i,&
W_{\mathcal I}&=\prod_{i\in\mathcal I}W_i,\\
\alpha_{\mathcal I}(\mathbf v)
&=\min\left\{\prod_{i\in\mathcal I}w^i_{J_i+v_i},
                 \prod_{i\in\mathcal I}w^i_{J_i-v_i}\right\},&
L_{\mathcal I}&=2\sum_{i\in\mathcal I}\mathbb E_{Q_i}G_i.
\end{aligned}
\]

Thus \(\alpha_{\mathcal I}\) is the canonical reflected endpoint minimum for this coordinate subproduct. Directly from the potential definitions,

\[
\alpha_{\mathcal I}(\mathbf v)
=\left(\prod_{i\in\mathcal I}R_i\right)Q_{\mathcal I}(\mathbf v)
 \exp\left(-\left|\sum_{i\in\mathcal I}A_i(v_i)\right|\right).
\tag{1}
\]

The event \(\mathcal V_{\mathcal I}=\{\sum_iG_i\le L_{\mathcal I}\}\) has probability \(\vartheta\ge1/2\). Indeed, if \(L_{\mathcal I}>0\), nonnegativity gives
\(\mathbb P\{\sum_iG_i>L_{\mathcal I}\}\le\mathbb E[\sum_iG_i]/L_{\mathcal I}=1/2\). If \(L_{\mathcal I}=0\), the nonnegative sum has expectation zero, so it vanishes almost surely and \(\vartheta=1\).

Evenness of \(Q_i\) and oddness of \(A_i\) give \(\mathbb E_{Q_i}A_i=0\). Independence therefore gives
\(\mathbb E_{Q_{\mathcal I}}[(\sum_iA_i)^2]=\sum_i\mathbb E_{Q_i}A_i^2\). Since the square is nonnegative, conditioning on \(\mathcal V_{\mathcal I}\) increases this bound by at most \(1/\vartheta\le2\). Cauchy-Schwarz then gives
\(\mathbb E[|\sum_iA_i|\mid\mathcal V_{\mathcal I}]\le\sqrt{2\sum_i\mathbb E_{Q_i}A_i^2}\).
For any finite random variable \(X\ge0\), the inequality \(e^t\ge1+t\), applied with \(t=\mathbb EX-X\), proves \(\mathbb E e^{-X}\ge e^{-\mathbb EX}\). Applying it under this conditional probability and then using (1) proves

\[
\sum_{\substack{\mathbf v\in\mathcal U_{\mathcal I}\\\sum_iG_i(v_i)\le L_{\mathcal I}}}
\alpha_{\mathcal I}(\mathbf v)
\ge\frac12\left(\prod_{i\in\mathcal I}R_i\right)
\exp\left(-\sqrt{2\sum_{i\in\mathcal I}\mathbb E_{Q_i}A_i^2}\right).
\tag{2}
\]

All probabilities and expectations here are finite sums. In particular (2) is an estimate for actual endpoint minima, not an allocation of geometric-mean capacities. The stock \(\alpha_{\mathcal I}\mathbf 1_{\mathcal V_{\mathcal I}}\) is even under \(\mathbf v\mapsto-\mathbf v\), and every displacement it retains has total gap at most \(L_{\mathcal I}\).

Two elementary inequalities will pay the losses in (2). For \(0\le\delta\le1/2\), one has \(\log(1+2\delta)\ge\delta\), since the difference is zero at zero and has derivative \(2/(1+2\delta)-1\ge0\). For \(x\ge0\), one has \(\log(1+x)\le\sqrt x\): the difference \(\sqrt x-\log(1+x)\) is zero at zero and, for \(x>0\), has derivative \((\sqrt x-1)^2/[2\sqrt x(1+x)]\ge0\).

Now place the near-critical coordinates in disjoint dyadic bins
\(\mathcal I_j=\{i:2^{-j-1}\le\delta_i<2^{-j}\}\), \(j\ge0\), restricted to the near-critical set. These half-open bins assign every such coordinate exactly once. Let \(m_j=|\mathcal I_j|\) and \(x_j=m_j2^{-j-1}\). Declare a bin active if \(x_j\ge K_\ast(j+2)^2\), and inactive otherwise. Only finitely many bins are nonempty.

Freeze each coordinate in an inactive bin at any mode, and enlarge \(\mathcal F_0\) by these coordinates to obtain \(\mathcal F\). The near-critical atom-deficit assertion in `8660ffca617b9702` gives
\(w_{\max,i}\ge(W_i/2)(1-100\delta_i^2)\).
For \(0\le y\le1/2\), integrating \(1/(1-t)\le2\) on \([0,y]\) gives \(\log(1-y)\ge-2y\). Here \(100\delta_i^2<1/2\), so the atom ratios are at least \(e^{-200\delta_i^2}\). The total squared surplus of the inactive coordinates obeys

\[
\begin{aligned}
\sum_{j\ \mathrm{inactive}}\sum_{i\in\mathcal I_j}\delta_i^2
&\le\sum_{j\ \mathrm{inactive}}m_j2^{-2j}
=\sum_{j\ \mathrm{inactive}}2x_j2^{-j}\\
&\le2K_\ast\sum_{j=0}^{\infty}(j+2)^2 2^{-j}
=44K_\ast.
\end{aligned}
\tag{3}
\]

For the last equality, the geometric sum is \(\sum_{j\ge0}2^{-j}=2\). Subtracting the half-shift of \(\sum_{j\ge0}j2^{-j}\) gives that sum as \(2\); subtracting the half-shift of \(\sum_{j\ge0}j^22^{-j}\) then gives it as \(6\). Consequently the displayed sum is \(6+4\cdot2+4\cdot2=22\). These series converge absolutely, for instance because successive term ratios tend to \(1/2\).

Define the frozen stock on its coordinate displacement space by \(\beta_{\mathcal F}(\mathbf0)=\prod_{i\in\mathcal F}w_{\max,i}\), with zero stock at every other displacement, and set \(L_{\mathcal F}=0\). Its oriented sum \(Z_{\mathcal F}=\sum\beta_{\mathcal F}\) satisfies

\[
Z_{\mathcal F}\ge e^{-8800K_\ast}\,2^{-|\mathcal F|}W_{\mathcal F}.
\tag{4}
\]

The original frozen coordinates lose nothing against their benchmarks, and (3) proves the single constant loss in (4) for all inactive bins together. Empty coordinate products and the stock on the empty tuple are understood to equal one.

For each active bin choose any maximizing center in every coordinate and apply (2) to \(\mathcal I_j\). Accepted fact `15da936de919780f` gives
\(\mathbb E_{Q_i}(G_i+A_i^2)\le1000\delta_i[1+\log(1/\delta_i)]^2\)
for every one of these maximizing centers. In this bin,
\(1+\log(1/\delta_i)\le1+(j+1)\log2\le j+2\)
and \(x_j\le\sum_{i\in\mathcal I_j}\delta_i\le2x_j\). Therefore, with \(L_j=2\sum_{i\in\mathcal I_j}\mathbb E_{Q_i}G_i\),

\[
L_j\le4000x_j(j+2)^2,
\qquad
\sqrt{2\sum_{i\in\mathcal I_j}\mathbb E_{Q_i}A_i^2}
\le\sqrt{4000x_j(j+2)^2}\le\frac{x_j}{4}.
\tag{5}
\]

The last inequality is exactly the active-bin condition and \(K_\ast=64000\). That condition also gives \(x_j\ge4K_\ast\ge64\) and
\(L_j\le(4000/K_\ast)x_j^2\le x_j^2\). Thus

\[
\begin{aligned}
\log\bigl(2(1+L_j)\bigr)
&\le1+\log(1+x_j^2)
\le1+2\log(1+x_j)\\
&\le1+2\sqrt{x_j}\le\frac{x_j}{2}.
\end{aligned}
\tag{6}
\]

The final step uses \(2\sqrt{x_j}\le x_j/4\) for \(x_j\ge64\), and \(1\le x_j/4\). The Hellinger surplus pays both (5) and (6), because

\[
\log\prod_{i\in\mathcal I_j}(1+2\delta_i)
\ge\sum_{i\in\mathcal I_j}\delta_i
\ge x_j
\ge\sqrt{2\sum_{i\in\mathcal I_j}\mathbb E_{Q_i}A_i^2}
  +\log\bigl(2(1+L_j)\bigr).
\tag{7}
\]

Define \(\beta_j(\mathbf v)=\alpha_{\mathcal I_j}(\mathbf v)\mathbf1_{\{\sum_{i\in\mathcal I_j}G_i(v_i)\le L_j\}}\), and let \(Z_j=\sum\beta_j\). Since \(R_i=(W_i/2)(1+2\delta_i)\), (2) and (7) give

\[
Z_j\ge(1+L_j)\,2^{-m_j}W_{\mathcal I_j}.
\tag{8}
\]

This stock is even and is bounded pointwise by the actual block endpoint minimum.

It remains to handle the moderate coordinates, denoted \(\mathcal I_{\mathrm{mod}}\), with \(m_{\mathrm{mod}}=|\mathcal I_{\mathrm{mod}}|\). Choose maximizing centers for all of them. Accepted fact `0dc72eecb73c50bd` gives, at every such center,

\[
\mathbb E_{Q_i}(G_i^2+A_i^2)<32,
\qquad
\sum_{\substack{v\in\mathcal U_i\\G_i(v)^2+A_i(v)^2\le64}}\alpha_i(v)
\ge\frac{e^{-8}}2R_i.
\tag{9}
\]

If \(m_{\mathrm{mod}}\ge M_\ast\), use the pooled stock from (2), with
\(L_{\mathrm{mod}}=2\sum_{i\in\mathcal I_{\mathrm{mod}}}\mathbb E_{Q_i}G_i\).
Cauchy-Schwarz and (9) give \(L_{\mathrm{mod}}\le12m_{\mathrm{mod}}\) and
\(\sqrt{2\sum_i\mathbb E_{Q_i}A_i^2}\le8\sqrt{m_{\mathrm{mod}}}\).
Also

\[
\begin{aligned}
\log\bigl(2(1+L_{\mathrm{mod}})\bigr)
&\le1+\sqrt{12m_{\mathrm{mod}}}
\le5\sqrt{m_{\mathrm{mod}}},\\
\log\prod_{i\in\mathcal I_{\mathrm{mod}}}(1+2\delta_i)
&\ge\frac{m_{\mathrm{mod}}}{27000}
\ge16\sqrt{m_{\mathrm{mod}}}.
\end{aligned}
\tag{10}
\]

Here \(m_{\mathrm{mod}}\ge1\) justifies the first line, and \(m_{\mathrm{mod}}\ge(16\cdot27000)^2\) justifies the last inequality. The loss in (2), including its factor \(1/2\) and the cutoff denominator, is at most \(13\sqrt{m_{\mathrm{mod}}}\) on the logarithmic scale. Thus the stock \(\beta_{\mathrm{mod}}\) supplied by (2) has oriented sum
\(Z_{\mathrm{mod}}\ge(1+L_{\mathrm{mod}})2^{-m_{\mathrm{mod}}}W_{\mathcal I_{\mathrm{mod}}}\).

If instead \(0\le m_{\mathrm{mod}}<M_\ast\), use the coordinatewise restricted legal stock

\[
\beta_{\mathrm{mod}}(\mathbf v)
=\prod_{i\in\mathcal I_{\mathrm{mod}}}
\left(\alpha_i(v_i)\mathbf1_{\{G_i(v_i)^2+A_i(v_i)^2\le64\}}\right),
\qquad L_{\mathrm{mod}}=8m_{\mathrm{mod}}.
\tag{11}
\]

Every retained coordinate has \(G_i(v_i)\le8\), so the total cost is at most this cutoff. The product of coordinate minima is no larger than either product of endpoints, hence \(\beta_{\mathrm{mod}}\le\alpha_{\mathcal I_{\mathrm{mod}}}\). Summing (11) over the full Cartesian displacement set and using (9) gives

\[
Z_{\mathrm{mod}}
\ge\left(\frac{e^{-8}}2\right)^{m_{\mathrm{mod}}}
  2^{-m_{\mathrm{mod}}}W_{\mathcal I_{\mathrm{mod}}}
\ge\left(\frac{e^{-8}}2\right)^{M_\ast}
  2^{-m_{\mathrm{mod}}}W_{\mathcal I_{\mathrm{mod}}}.
\tag{12}
\]

This also covers the empty moderate set, with stock one and cutoff zero. Define
\(c_{\mathrm{mod}}=(e^{-8}/2)^{M_\ast}/(1+8M_\ast)\).
In both moderate cases we have an even stock bounded by its block endpoint minimum, supported at total gap at most \(L_{\mathrm{mod}}\), and satisfying

\[
Z_{\mathrm{mod}}\ge c_{\mathrm{mod}}(1+L_{\mathrm{mod}})
  2^{-m_{\mathrm{mod}}}W_{\mathcal I_{\mathrm{mod}}}.
\tag{13}
\]

For the bounded case this follows from \(1+L_{\mathrm{mod}}\le1+8M_\ast\); for the large case it follows from the stronger bound after (10), since \(c_{\mathrm{mod}}\le1\). No moderate coordinate was frozen at a mode merely because its block was small.

We finally convert the stocks into one physical packing. Fix the global center \(\mathbf J=(J_1,\ldots,J_N)\) chosen above. The coordinate partition consists of \(\mathcal F\), the finitely many active bins, and \(\mathcal I_{\mathrm{mod}}\); empty groups contribute one. On their Cartesian displacement space define

\[
\beta(\mathbf v)=\beta_{\mathcal F}(\mathbf v_{\mathcal F})
 \beta_{\mathrm{mod}}(\mathbf v_{\mathcal I_{\mathrm{mod}}})
 \prod_{j\ \mathrm{active}}\beta_j(\mathbf v_{\mathcal I_j}),
\qquad
L=L_{\mathrm{mod}}+\sum_{j\ \mathrm{active}}L_j.
\tag{14}
\]

This is a finite even stock. Its positive stock has both global endpoints \(\mathbf J\pm\mathbf v\) in \(D\). The product of block endpoint minima is at most the actual global endpoint minimum: for each block the minimum is at most either endpoint, and multiplying proves both inequalities. Equivalently, writing each block minimum as its geometric mean times \(e^{-\left|\sum_{i\text{ in block}}A_i(v_i)\right|}\), this is the triangle inequality
\(|\sum_iA_i(v_i)|\le\sum_{\text{blocks}}|\sum_{i\text{ in block}}A_i(v_i)|\).
Every block stock is bounded by its endpoint minimum, so
\(\beta(\mathbf v)\le\min\{w_{\mathbf J+\mathbf v},w_{\mathbf J-\mathbf v}\}\).
The frozen block has only zero displacement and zero gap. Additivity of the potential gives the exact global pair cost

\[
\frac{\phi_{\mathbf J+\mathbf v}+\phi_{\mathbf J-\mathbf v}}2-\phi_{\mathbf J}
=\sum_{i=1}^N G_i(v_i)\le L
\quad\text{whenever }\beta(\mathbf v)>0.
\tag{15}
\]

For frozen coordinates the same displayed definition of \(G_i\) is used at their modal centers, and \(G_i(0)=0\).

Choose one representative from each nonzero global reflection pair \(\{\mathbf v,-\mathbf v\}\) with positive stock. Give the component \(\{\mathbf J+\mathbf v,\mathbf J-\mathbf v\}\), with barycentric coefficients \(1/2,1/2\), mass \(\beta(\mathbf v)\). Give the singleton \(\{\mathbf J\}\) mass \(\beta(\mathbf0)\), omitting zero masses. A nonzero pair is affinely independent and has \(\mathbf J\) in its relative interior; (15) is precisely its canonical \(G_E\). The singleton has cost zero. Thus these are members of \(\mathcal E_{\mathbf J}^{\log}(L)\) as defined in `488f0a583886b5fc`.

Different global reflection pairs have disjoint original source sets: an endpoint \(\mathbf I\) uniquely determines its displacement \(\mathbf I-\mathbf J\) and its reflected endpoint \(2\mathbf J-\mathbf I\). The center occurs only in the singleton. Each used source is therefore charged once, and its component mass is at most its original capacity \(w_{\mathbf I}\). This is a feasible full-occurrence packing, without any per-block orientation or arity loss. Evenness gives its mass as

\[
\beta(\mathbf0)+\frac12\sum_{\mathbf v\ne\mathbf0}\beta(\mathbf v)
=\frac12\left(\sum_{\mathbf v}\beta(\mathbf v)+\beta(\mathbf0)\right)
\ge\frac12 Z_{\mathcal F}Z_{\mathrm{mod}}\prod_{j\ \mathrm{active}}Z_j.
\tag{16}
\]

The product identity for the oriented sum follows by finite Cartesian summation, including the empty products. For nonnegative cutoffs, multiplying \((1+s)(1+t)\ge1+s+t\) inductively gives
\((1+L_{\mathrm{mod}})\prod_{j\ \mathrm{active}}(1+L_j)\ge1+L\).
Combining (4), (8), (13), and (16), and using that the coordinate groups partition all \(N\) coordinates, proves

\[
\begin{aligned}
\mathcal B_{\log}(w)
&\ge\frac{P_{\log}(\mathbf J,L;w)}{1+L}\\
&\ge\frac{e^{-8800K_\ast}c_{\mathrm{mod}}}{2}
\,2^{-N}W\,
\frac{(1+L_{\mathrm{mod}})\prod_{j\ \mathrm{active}}(1+L_j)}{1+L}\\
&\ge c\,2^{-N}W.
\end{aligned}
\]

All cutoffs use weak inequalities, so tied costs and displacement atoms are retained. Mode and maximizing-center ties may be resolved arbitrarily, because the cited near-critical and uniform estimates hold at every maximizing center. The argument keeps the complete reflected intervals, including zero and every supported endpoint; it uses no potential at a zero-weight site. Singleton profiles and the zero-surplus two-equal-atom profiles are frozen in \(\mathcal F_0\). Flat profiles of any other length satisfy the same estimates, and the proof also covers the absence of active bins or of moderate coordinates. The displayed \(c\) depends on none of the profiles, their support lengths, or \(N\).

## External sources

None. Accepted fact `488f0a583886b5fc` supplies the canonical logarithmic score, globally extendable-table interpretation, and full-occurrence capacities. Accepted fact `8660ffca617b9702` supplies the Hellinger half-mass threshold, its equality characterization, and the near-critical atom deficit. Accepted fact `15da936de919780f` supplies the near-critical expectation price at every maximizing center. Accepted fact `0dc72eecb73c50bd` supplies the uniform second-moment price and bounded-cost legal capacity at every maximizing center. The probability pooling, dyadic bookkeeping, surplus payments, Cartesian stock composition, and physical once-only packing are proved in this packet.
