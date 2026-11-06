---
fact_id: c5abe3c72b8b89eb
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3br-unbounded-block-family-averaged-price-moment-consumer
depends_on: ["075a3f88fa24d326","bf1ff94487296374","e1538bd5cc63f818"]
verifier_run: 2b9b422001f04199
target_match: null
---

## Statement

All logarithms are natural. Retain the notation of accepted fact bf1ff94487296374. For a strictly positive probability law \(p\) on a finite nonempty support \(A\subseteq\mathbb R^m\), its actual closed-halfspace depth and entropy capacity are
\[
\begin{aligned}
\tau_p(\mathbf j)
&:=\inf_{\substack{H\subseteq\mathbb R^m\text{ a proper closed halfspace}\\\mathbf j\in H}}
       \sum_{\mathbf x\in A\cap H}p_{\mathbf x},\\
\mathsf C_p(\mathbf j)
&:=\inf_{\mathbf u\in\mathbb R^m}
       \sum_{\mathbf x\in A}p_{\mathbf x}
          e^{\mathbf u\cdot(\mathbf x-\mathbf j)}.
\end{aligned}
\]
Extend its moment notation by \(\mathcal M_t(p):=\sum_{\mathbf j\in A}p_{\mathbf j}\tau_p(\mathbf j)^t\) for \(t\in\{2,3\}\) and \(\mathcal B_t(p):=\sum_{\mathbf j\in A}p_{\mathbf j}\mathsf C_p(\mathbf j)^t\) for \(t\in\{2,3,4\}\); thus the order-two quantities are unchanged. A singleton in zero ambient dimension is assigned depth one, equivalently computed after embedding it into \(\mathbb R\). Its capacity and all these moments are one.

Fix finite constants \(\kappa\ge3\), \(V_0\ge0\), and \(g>1\). For every integer \(k\ge1\), choose arbitrary integers \(n_i\ge0\), finite nonempty complete supports \(A_i=\operatorname{conv}(A_i)\cap\mathbb Z^{n_i}\), and arbitrary tilts \(\boldsymbol\ell_i\in\mathbb R^{n_i}\). Set
\[
\begin{aligned}
p_{i,\mathbf x}
&:=\frac{e^{\boldsymbol\ell_i\cdot\mathbf x}}
         {\sum_{\mathbf y\in A_i}e^{\boldsymbol\ell_i\cdot\mathbf y}},
& r_i&:=\dim\operatorname{aff}(A_i),\\
P&:=\bigotimes_{i=1}^k p_i,
& R&:=\sum_{i=1}^k r_i,\\
I&:=\{i:|A_i|>2^{r_i}\},
& b&:=|I|.
\end{aligned}
\]
For every \(\mathbf j\in A_i\), let \(\nu_{i,\mathbf j}\) be the unique relative-entropy minimizing law on \(A_i\) with mean \(\mathbf j\), where \(D(\nu\|p_i):=\sum_{\mathbf x}\nu_{\mathbf x}\log(\nu_{\mathbf x}/p_{i,\mathbf x})\), omitting zero summands. Its exact aliases in bf1ff94487296374 are the row \(r_{i,\mathbf j}\) in the product-conversion proof and, because \(p_i\) is log-affine, the maximum-entropy row \(r_{A_i,\mathbf j}\), taking the whole face support \(E=A_i\) in that predecessor's definition of \(r_{E,\mathbf j}\). Define
\[
\begin{aligned}
\omega_{i,\mathbf j}
&:=\frac{p_{i,\mathbf j}\mathsf C_{p_i}(\mathbf j)^2}
          {\mathcal B_2(p_i)},\\
V_{i,\mathbf j}
&:=\operatorname{Var}_{\nu_{i,\mathbf j}}
       \left[\log\frac{\nu_{i,\mathbf j}(\mathbf X_i)}
                          {p_{i,\mathbf X_i}}\right].
\end{aligned}
\]
The logarithm is evaluated only on the positive support of the row. On scalar interval supports these are exactly the laws and quantities \(\nu_{i,j_i},\omega_{i,j_i},V_{i,j_i}\) of accepted fact 075a3f88fa24d326, under \(\mathbf j=j_i\). The assignment's \(C_i(\mathbf j)\) and \(B2_i\) are exactly \(\mathsf C_{p_i}(\mathbf j)\) and \(\mathcal B_2(p_i)\).

Assume the following three certificates for each \(i\in I\), with the same \(\kappa,V_0,g\) for every certified block:
\[
\begin{aligned}
\mathbb E_{\nu_{i,\mathbf j}}
   [(\mathbf u\cdot(\mathbf X_i-\mathbf j))^4]
&\le\kappa
   \left(\operatorname{Var}_{\nu_{i,\mathbf j}}
             [\mathbf u\cdot\mathbf X_i]\right)^2
&& (\mathbf j\in A_i,\ \mathbf u\in\mathbb R^{n_i}),\\
\mathcal B_2(p_i)&\ge g\,4^{-r_i},\\
\sum_{\mathbf j\in A_i}\omega_{i,\mathbf j}V_{i,\mathbf j}
&\le V_0.
\end{aligned}
\]
There is no row, price, or surplus assumption for \(i\notin I\). In particular, the direction vectors and their norms are unrestricted. No bound on support cardinalities, positive atom masses, positive row masses, or the size of the family of available supports is assumed.

Define
\[
\alpha_{\mathrm{block}}:=\frac1{8\kappa},
\qquad
\beta_{\mathrm{block}}:=\sqrt{8\kappa V_0},
\qquad
a_{\mathrm{block}}:=\alpha_{\mathrm{block}}
       \exp\!\left(-\frac{\beta_{\mathrm{block}}^2}{2\log g}\right)>0.
\]
The assignment's \(a\) is \(a_{\mathrm{block}}\). These are certificate-dependent constants, not the fixed-family constants in bf1ff94487296374; under \(\kappa=K_{\mathrm{row}}\) and \(V_0=c_{\mathrm{lik}}\), the first two coincide with \(\alpha_{\mathrm{row}},\beta_{\mathrm{row}}\) of 075a3f88fa24d326.

Then
\[
\begin{aligned}
4^R\mathcal M_2(P)
&\ge\alpha_{\mathrm{block}}^2
       \exp\!\left(b\log g-2\beta_{\mathrm{block}}\sqrt b\right)
 \ge a_{\mathrm{block}}^2,\\
8^R\mathcal M_3(P)
&\ge\alpha_{\mathrm{block}}^3
       \exp\!\left(\tfrac32 b\log g-3\beta_{\mathrm{block}}\sqrt b\right)
 \ge a_{\mathrm{block}}^3.
\end{aligned}
\]
If \(b=0\), the stronger bounds \(\mathcal M_2(P)\ge4^{-R}\) and \(\mathcal M_3(P)\ge8^{-R}\) hold without any certificates. Capacity factorization and its moments, including order four, hold exactly:
\[
\begin{aligned}
\mathsf C_P(\mathbf j)&=\prod_{i=1}^k\mathsf C_{p_i}(\mathbf j_i),\\
\mathcal B_t(P)&=\prod_{i=1}^k\mathcal B_t(p_i)
\qquad(t\in\{2,3,4\}),\\
\mathcal B_2(P)&\ge g^b4^{-R}.
\end{aligned}
\]
Here \(\mathbf j=(\mathbf j_1,\ldots,\mathbf j_k)\). The same coefficient therefore applies simultaneously to every finite selection, with repetitions, from a possibly infinite family of supports and tilts satisfying the stated certificates. For displayed total ambient dimension \(\sum_i n_i\), the weaker bounds with \(4^{-\sum_i n_i}\) and \(8^{-\sum_i n_i}\) follow as well. The hypotheses remain explicit: the complete log-affine examples in accepted fact e1538bd5cc63f818 rule out an automatic uniform all-row fourth-moment certificate based on completeness and log-affinity, even when likelihood variances vanish.

## Proof

First identify the rows and capacities, including boundary targets. For any mean-\(\mathbf j\) law \(\nu\) on \(A_i\), log-affinity gives \(\sum_{\mathbf x}\nu_{\mathbf x}\log p_{i,\mathbf x}=\log p_{i,\mathbf j}\). Consequently
\[
D(\nu\|p_i)=-H(\nu)-\log p_{i,\mathbf j},
\qquad
H(\nu):=-\sum_{\mathbf x}\nu_{\mathbf x}\log\nu_{\mathbf x}.
\]
Thus the unique relative-entropy minimizer is the unique maximum-entropy mean-\(\mathbf j\) law. The boundary-inclusive entropy-capacity identity of bf1ff94487296374, with the aliases stated above, yields
\[
\mathsf C_{p_i}(\mathbf j)
=e^{-D(\nu_{i,\mathbf j}\|p_i)}
=p_{i,\mathbf j}e^{H(\nu_{i,\mathbf j})}.
\]
No finite ambient exponential parameter for a boundary row is required. Every capacity is positive, since the term at \(\mathbf x=\mathbf j\) bounds its exponential infimum below by \(p_{i,\mathbf j}>0\). Hence every \(\mathcal B_2(p_i)\) is positive and \(\omega_i\) is a probability law. Every row likelihood variance is finite on its positive finite support; no positive lower bound for its atoms is used.

Capacity factorization holds independently of the certificates. For a block vector \(\mathbf u=(\mathbf u_1,\ldots,\mathbf u_k)\), the exponential sum centered at \(\mathbf j\) factorizes as
\[
\sum_{\mathbf x}P_{\mathbf x}
       e^{\mathbf u\cdot(\mathbf x-\mathbf j)}
=\prod_{i=1}^k
       \left(\sum_{\mathbf x_i\in A_i}p_{i,\mathbf x_i}
          e^{\mathbf u_i\cdot(\mathbf x_i-\mathbf j_i)}\right).
\]
Each product is at least the product of the positive block infima. Conversely, independently approach each block infimum and take a limit in this finite product. This proves the exact capacity formula, without assuming attainment. Raising it to \(t\) and summing with the original product target probabilities proves \(\mathcal B_t(P)=\prod_i\mathcal B_t(p_i)\) for \(t=2,3,4\). For \(i\notin I\), the complete-support log-affine baseline of bf1ff94487296374 gives \(\mathcal B_2(p_i)\ge4^{-r_i}\). For \(i\in I\) use the surplus certificate. Their product proves \(\mathcal B_2(P)\ge g^b4^{-R}\).

Suppose now \(b>0\). Write \(P_{\mathrm{big}}:=\bigotimes_{i\in I}p_i\), retaining exactly the big-product notation of bf1ff94487296374. For a target tuple \(\mathbf j=(\mathbf j_i)_{i\in I}\), set \(Q_{\mathbf j}:=\bigotimes_{i\in I}\nu_{i,\mathbf j_i}\). This is the row-product law denoted \(Q\) in that fact and \(Q_{\mathbf j}\) in 075a3f88fa24d326, now on general finite blocks. Its mean is \(\mathbf j\).

For any direction \(\mathbf u=(\mathbf u_i)_{i\in I}\), let \(Y_i:=\mathbf u_i\cdot(\mathbf X_i-\mathbf j_i)\) and \(v_i:=\mathbb E_{Q_{\mathbf j}}Y_i^2\). Independence and centering give the exact fourth-moment expansion
\[
\begin{aligned}
\mathbb E_{Q_{\mathbf j}}\left[\left(\sum_{i\in I}Y_i\right)^4\right]
&=\sum_{i\in I}\mathbb E_{Q_{\mathbf j}}Y_i^4
       +6\sum_{\substack{i<h\\i,h\in I}}v_iv_h\\
&\le\kappa\sum_{i\in I}v_i^2
       +6\sum_{\substack{i<h\\i,h\in I}}v_iv_h
 \le\kappa\left(\sum_{i\in I}v_i\right)^2.
\end{aligned}
\]
The final inequality uses \(\kappa\ge3\). Thus taking independent sums preserves the same directional fourth-moment constant, regardless of block dimensions or norms. Zero-variance block projections are included.

Any proper closed halfspace containing \(\mathbf j\) contains its parallel translate through \(\mathbf j\). Membership in the latter is the event \(Y:=\sum_{i\in I}Y_i\ge0\). Let \(\sigma^2:=\mathbb E_{Q_{\mathbf j}}Y^2\), with \(\sigma\ge0\). If \(\sigma>0\), Hölder applied to \(|Y|^{2/3}|Y|^{4/3}\) gives
\[
\mathbb E Y^2
\le(\mathbb E|Y|)^{2/3}(\mathbb E Y^4)^{1/3},
\qquad
\mathbb E|Y|
\ge\frac{(\mathbb E Y^2)^{3/2}}{(\mathbb E Y^4)^{1/2}}
\ge\frac{\sigma}{\sqrt\kappa}.
\]
All expectations in this paragraph are under \(Q_{\mathbf j}\). Since \(\mathbb E Y=0\), \(\mathbb E Y_+=\mathbb E|Y|/2\). Cauchy--Schwarz then gives \((\mathbb E Y_+)^2\le\mathbb E Y^2\,Q_{\mathbf j}(Y\ge0)\), and hence \(Q_{\mathbf j}(Y\ge0)\ge1/(4\kappa)\). If \(\sigma=0\), then \(Y=0\) almost surely and this probability is one. Therefore every containing halfspace has \(Q_{\mathbf j}\)-mass at least \(1/(4\kappa)\), including directions constant on its affine support.

Define, on the positive support of \(Q_{\mathbf j}\), the log likelihood \(L_{\mathbf j}:=\log(Q_{\mathbf j}(\mathbf X)/P_{\mathrm{big}}(\mathbf X))\), and write \(v(\mathbf j):=\sum_{i\in I}V_{i,\mathbf j_i}\). The row entropy identities and independence imply
\[
\begin{aligned}
\mathbb E_{Q_{\mathbf j}}L_{\mathbf j}
&=\sum_{i\in I}D(\nu_{i,\mathbf j_i}\|p_i)
=-\sum_{i\in I}\log\mathsf C_{p_i}(\mathbf j_i),\\
\operatorname{Var}_{Q_{\mathbf j}}L_{\mathbf j}
&=v(\mathbf j).
\end{aligned}
\]
If \(v(\mathbf j)>0\), Chebyshev bounds the event \(L_{\mathbf j}>\mathbb E_{Q_{\mathbf j}}L_{\mathbf j}+\sqrt{8\kappa v(\mathbf j)}\) by \(1/(8\kappa)\). If \(v(\mathbf j)=0\), the exceptional event with threshold zero is empty. Intersect the complementary likelihood event with any containing halfspace. Its \(Q_{\mathbf j}\)-mass is at least \(\alpha_{\mathrm{block}}\). On that intersection,
\[
P_{\mathrm{big}}(\mathbf x)
=Q_{\mathbf j}(\mathbf x)e^{-L_{\mathbf j}(\mathbf x)}
\ge Q_{\mathbf j}(\mathbf x)
     e^{-\sqrt{8\kappa v(\mathbf j)}}
     \prod_{i\in I}\mathsf C_{p_i}(\mathbf j_i).
\]
Summing only there and then taking the halfspace infimum proves the pointwise bound
\[
\tau_{P_{\mathrm{big}}}(\mathbf j)
\ge\alpha_{\mathrm{block}}
      e^{-\sqrt{8\kappa v(\mathbf j)}}
      \prod_{i\in I}\mathsf C_{p_i}(\mathbf j_i).
\]
Any original-law mass outside the positive row support is nonnegative; it is not needed for this lower bound.

We now extend the averaged-likelihood mechanism of 075a3f88fa24d326, rather than replacing the prices by their maxima over rows. Squaring the last inequality and averaging against the original target law \(P_{\mathrm{big}}\) gives exactly the weight change
\[
\begin{aligned}
\mathcal M_2(P_{\mathrm{big}})
&\ge\alpha_{\mathrm{block}}^2
 \sum_{\mathbf j}P_{\mathrm{big}}(\mathbf j)
       \left(\prod_{i\in I}\mathsf C_{p_i}(\mathbf j_i)^2\right)
       e^{-2\sqrt{8\kappa}\sqrt{v(\mathbf j)}}\\
&=\alpha_{\mathrm{block}}^2
       \left(\prod_{i\in I}\mathcal B_2(p_i)\right)
       \mathbb E_{\Omega}
          e^{-2\sqrt{8\kappa}\sqrt{v(\mathbf j)}},
\qquad \Omega:=\bigotimes_{i\in I}\omega_i.
\end{aligned}
\]
Thus \(\Omega\) appears only algebraically after averaging the squared actual-depth bound with the original root weights. It is neither the original law nor the law used for halfspace probabilities. The price certificate and Cauchy--Schwarz yield
\[
\mathbb E_{\Omega}\sqrt{v(\mathbf j)}
\le\sqrt{\mathbb E_{\Omega}v(\mathbf j)}
=\sqrt{\sum_{i\in I}\sum_{\mathbf j_i\in A_i}
                   \omega_{i,\mathbf j_i}V_{i,\mathbf j_i}}
\le\sqrt{bV_0}.
\]
Because \(z\mapsto e^{-2\sqrt{8\kappa}z}\) is convex and decreasing on \([0,\infty)\), Jensen gives
\[
\begin{aligned}
\mathbb E_{\Omega}e^{-2\sqrt{8\kappa}\sqrt{v(\mathbf j)}}
&\ge e^{-2\sqrt{8\kappa}\,\mathbb E_{\Omega}\sqrt{v(\mathbf j)}}
 \ge e^{-2\beta_{\mathrm{block}}\sqrt b},\\
\mathcal M_2(P_{\mathrm{big}})
&\ge\alpha_{\mathrm{block}}^2e^{-2\beta_{\mathrm{block}}\sqrt b}
       \prod_{i\in I}\mathcal B_2(p_i)\\
&\ge\alpha_{\mathrm{block}}^2
       e^{b\log g-2\beta_{\mathrm{block}}\sqrt b}
       4^{-\sum_{i\in I}r_i}.
\end{aligned}
\]
This proves the certified-block conversion without a coefficient per factor.

Restore every small block using actual depth, not an entropy-row assumption. For any law \(p\) on \(M\) atoms, every halfspace containing \(\mathbf j\) contains its atom, so \(\tau_p(\mathbf j)\ge p_{\mathbf j}\). Jensen for the uniform average of \(p_{\mathbf j}^3\) gives \(\sum_{\mathbf j}p_{\mathbf j}^3\ge M^{-2}\). Consequently, for each \(i\notin I\),
\[
\mathcal M_2(p_i)
\ge\sum_{\mathbf j\in A_i}p_{i,\mathbf j}^3
\ge|A_i|^{-2}
\ge4^{-r_i}.
\]
Here there is no loss of a fixed prefactor, even for a small block with irregular entropy rows.

For completeness, actual depth is pointwise supermultiplicative. For two finite laws \(p,q\) and a product target \((\mathbf x,\mathbf y)\), a halfspace through that target has the form \(\mathbf u\cdot(\mathbf X-\mathbf x)+\mathbf w\cdot(\mathbf Y-\mathbf y)\ge0\). It contains the product event where both summands are nonnegative. If a block normal is nonzero, its event has probability at least that block's depth; if it is zero, its event has probability one. Independence and translation through the target therefore give
\[
\tau_{p\otimes q}(\mathbf x,\mathbf y)
\ge\tau_p(\mathbf x)\tau_q(\mathbf y),
\qquad
\mathcal M_2(p\otimes q)\ge\mathcal M_2(p)\mathcal M_2(q).
\]
This also proves the corresponding assertion for any finite grouping of blocks by iteration. Apply it to \(P_{\mathrm{big}}\) and all small blocks. Their atom bounds prove the asserted refined second-moment inequality when \(b>0\). If \(b=0\), apply the same argument only to the small blocks to get \(\mathcal M_2(P)\ge4^{-R}\); this implies the refined displayed inequality because \(\alpha_{\mathrm{block}}\le1\).

Completing the square gives, for every \(b\ge0\),
\[
b\log g-2\beta_{\mathrm{block}}\sqrt b
=\log g\left(\sqrt b-\frac{\beta_{\mathrm{block}}}{\log g}\right)^2
 -\frac{\beta_{\mathrm{block}}^2}{\log g}
\ge-\frac{\beta_{\mathrm{block}}^2}{\log g}.
\]
This proves \(\mathcal M_2(P)\ge a_{\mathrm{block}}^2 4^{-R}\).

Finally, still using the original product target probabilities, Jensen for \(z^{3/2}\) applied to \(z=\tau_P(\mathbf j)^2\) gives
\[
\mathcal M_3(P)
=\sum_{\mathbf j}P_{\mathbf j}\bigl(\tau_P(\mathbf j)^2\bigr)^{3/2}
\ge\left(\sum_{\mathbf j}P_{\mathbf j}\tau_P(\mathbf j)^2\right)^{3/2}
=\mathcal M_2(P)^{3/2}.
\]
Taking the power \(3/2\) of the refined second-moment bound gives exactly the refined third-moment bound, since \((4^{-R})^{3/2}=8^{-R}\); the uniform coefficient is \(a_{\mathrm{block}}^3\). When \(b=0\), the sharper second-moment bound gives the stated sharper third-moment bound.

Rank-zero supports are singletons, so their capacities, depths, and moments are exactly one and they contribute no rank, gain, price, or prefactor loss. If a displayed ambient dimension is zero, embed its singleton as stated. Appending a constant coordinate does not change depth: a containing halfspace restricts either to a containing halfspace in the remaining coordinates or to the entire support, and every halfspace in the remaining coordinates extends by assigning zero to the appended normal component. When all coordinates are constant, every containing halfspace has mass one. This verifies the zero-dimensional convention and every degenerate case. The ambient-normalized conclusions follow from \(R\le\sum_i n_i\). Every proof step involved only a finite selected product and the three fixed certificate constants, establishing the stated uniformity over arbitrary, possibly infinite, families.

The scope of the certificates cannot be enlarged using the accepted inputs. Fact e1538bd5cc63f818 exhibits complete positive log-affine laws with zero row likelihood variances but unbounded directional row kurtosis and actual-to-capacity second-moment ratio tending to zero. Hence an automatic all-support row certificate or an automatic absolute capacity-conversion prefactor would contradict that accepted example. The present small-block branch does not require such a certificate. In particular, the complete triangular support \(\{(0,0),(1,0),(0,1)\}\) has rank two and three atoms, so it is handled without certificates. A standard integral triangle of side length at least two contains the six sites \((0,0),(1,0),(0,1),(2,0),(1,1),(0,2)\), hence has more than four atoms and belongs to the certified branch. No uniform fourth-moment, capacity-surplus, or weighted-price certificate for those larger triangular blocks is asserted here.

## External sources

None.
