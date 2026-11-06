---
fact_id: 3ecc2f69fbd9c9ca
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct21-saturated-eligible-pool
depends_on: ["f7e7a56b865cd7a0"]
verifier_run: 4505c8aebee049d0
target_match: null
---

## Statement

Let \(k\ge1\), \(v\ge0\), and \(T\ge0\) be integers, let \(\beta\ge0\) be finite, and let \(B_i\ge2\) and \(C_{4,i}\ge2B_i-1\) be integers for \(i\in[k]\). Put \(g_i=(0,1,B_i,C_{4,i})\) on \(\lbrace0,1,2,3\rbrace\). For \(k<i\le k+v\), put \(g_i(0)=0\) and \(g_i(1)=1\). The arithmetic ambient dimension, including height, is \(N=k+v+1\). Define
$$
\begin{aligned}
D_{\rm full}&=\lbrace0,1,2,3\rbrace^k\times\lbrace0,1\rbrace^v,
&\Gamma(\mathbf x)&=\sum_{i=1}^{k+v}g_i(x_i),\\
f_E&=\begin{cases}
\displaystyle\sum_{t=E}^T e^{-\beta t},&0\le E\le T,\\
0,&E>T,
\end{cases}
&Z_{\rm full}&=\sum_{\mathbf x\in D_{\rm full}}f_{\Gamma(\mathbf x)}.
\end{aligned}
\tag{1}
$$
Here \(E\) is a nonnegative integer. Choose disjoint \(P,J\subseteq[k]\), with \(m=|P|\ge1\), and an integer \(b\ge2\) such that
$$
B_i\le b\quad(i\in P),\qquad B_i\ge b\quad(i\in J).
\tag{2}
$$
No comparison with \(b\) is imposed outside \(P\cup J\). Define
$$
\begin{aligned}
D_{\rm sel}
&=\lbrace\mathbf y\in D_{\rm full}:y_i\ne3\text{ for all }i\in J\rbrace,
&Z_{\rm sel}&=\sum_{\mathbf y\in D_{\rm sel}}f_{\Gamma(\mathbf y)},\\
A_P(\mathbf y)&=|\lbrace i\in P:y_i=1\rbrace|,
&Q_{P,J}(\mathbf y)&=|\lbrace i\in P\cup J:y_i\in\lbrace2,3\rbrace\rbrace|,\\
F_{P,J}(\mathbf y)
&=\frac{Q_{P,J}(\mathbf y)(Q_{P,J}(\mathbf y)+A_P(\mathbf y)/b)}{m},
&\mathcal B^{\rm sat}_{P,J}
&=\frac1{Z_{\rm sel}}\sum_{\mathbf y\in D_{\rm sel}}
f_{\Gamma(\mathbf y)}
\exp\!\left(64\min\lbrace F_{P,J}(\mathbf y),Q_{P,J}(\mathbf y)\rbrace\right).
\end{aligned}
\tag{3}
$$
The counts \(A_P,Q_{P,J},F_{P,J}\) also apply to full source vectors. The normalization and the meanings of \(g_i,\Gamma,f_E,Z_{\rm full},Z_{\rm sel},A_P,Q_{P,J},F_{P,J},N\) are exactly those in accepted fact f7e7a56b865cd7a0; the only changed hypothesis is that \(B_i=b\) on \(P\) is replaced by \(B_i\le b\). In particular, \(Q_{P,J}\) counts retained pool threes, as well as twos in \(P\cup J\). The present \(N\) is the arithmetic epigraph dimension and does not redefine the locked \(n,d\) or mixed set \(S\).

Then
$$
\frac{Z_{\rm full}}{Z_{\rm sel}}\le\mathcal B^{\rm sat}_{P,J}
=\mathbb E_{\rm sel}
\exp\!\left(64\min\lbrace F_{P,J},Q_{P,J}\rbrace\right),
\tag{4}
$$
where \(\mathbb E_{\rm sel}\) uses the original selective spatial law \(f_{\Gamma(\mathbf y)}/Z_{\rm sel}\), with the same \(T,\beta\) as the full law.

For \(a\in\lbrace{\rm full},{\rm sel}\rbrace\), define the complete epigraph support and original probability law by
$$
\mathcal A_a=\lbrace(\mathbf x,t):\mathbf x\in D_a,\ t\in\mathbb Z,\
\Gamma(\mathbf x)\le t\le T\rbrace,
\qquad
p^a_{(\mathbf x,t)}=\frac{e^{-\beta t}}{Z_a}.
\tag{5}
$$
For any finite probability law \(p\) on \(\mathbb R^N\), let \(\tau_p(\mathbf z)\) be the infimum of \(p(H)\) over all closed affine halfspaces \(H\subseteq\mathbb R^N\) with nonzero normal and \(\mathbf z\in H\), and put \(M_3(p)=\sum_{\mathbf z}p_{\mathbf z}\tau_p(\mathbf z)^3\). Both laws in (5) use this same ambient halfspace family. One has
$$
M_3(p^{\rm full})\ge
\bigl(\mathcal B^{\rm sat}_{P,J}\bigr)^{-4}M_3(p^{\rm sel}).
\tag{6}
$$
Consequently, for any \(\kappa>0\) and finite \(L_0\ge1\), the hypotheses \(M_3(p^{\rm sel})\ge\kappa8^{-N}\) and \(\mathcal B^{\rm sat}_{P,J}\le L_0\) imply \(M_3(p^{\rm full})\ge\kappa L_0^{-4}8^{-N}\).

## Proof

All normalizers are positive, because the zero spatial vector at height zero is present. Every sum is finite. Also \(f_E\le f_{E'}\) whenever \(0\le E'\le E\). We reprove the exchange argument with (2), rather than invoke the equal-pool-cost theorem of accepted f7e7a56b865cd7a0 under changed hypotheses.

Call a spatial vector feasible if its energy is at most \(T\). We construct a nonnegative kernel \(K(\mathbf x,\mathbf y)\) from feasible full sources to feasible selective targets. Every row will sum to 1, and every positive entry will satisfy \(\Gamma(\mathbf y)\le\Gamma(\mathbf x)\). For its column load \(L(\mathbf y)=\sum_{\mathbf x}K(\mathbf x,\mathbf y)\), monotonicity of the original complete height tails gives
$$
\begin{aligned}
Z_{\rm full}
&=\sum_{\mathbf x,\mathbf y}f_{\Gamma(\mathbf x)}K(\mathbf x,\mathbf y)\\
&\le\sum_{\mathbf x,\mathbf y}f_{\Gamma(\mathbf y)}K(\mathbf x,\mathbf y)
=\sum_{\mathbf y}f_{\Gamma(\mathbf y)}L(\mathbf y).
\end{aligned}
\tag{7}
$$
All vectors in (7) are feasible in their respective domains. Infeasible spatial vectors contribute zero to the original normalizers.

A source with no three in \(J\) maps to itself with kernel entry 1. These identity sources contribute exactly 1 to every feasible selective target's column load. For every other source put
\(\ell=|\lbrace i\in J:x_i=3\rbrace|\ge1\),
\(q_{\rm src}=Q_{P,J}(\mathbf x)\), and \(a=A_P(\mathbf x)\).
One always has \(\ell\le q_{\rm src}\). Each such source belongs to exactly one of the following three cases. Coordinates not mentioned in a transformation are unchanged, including binary companions, pool threes, and all coordinates outside \(P\cup J\).

First, suppose \(q_{\rm src}\ge m/32\). Clip every three in \(J\) to two and send the source to that single target with entry 1. This lowers energy, since \(C_{4,i}\ge2B_i-1\ge B_i\), and preserves \(Q_{P,J}\). For a fixed target write \(q=Q_{P,J}(\mathbf y)\). A clipping preimage is determined by a nonempty subset of the target two-coordinates in \(J\), which are restored to threes. Thus the clipping contribution is zero for \(q<m/32\), and at most \(2^q-1\) otherwise. For \(q\ge m/32\), using \(\log2<3/4\) gives
\(q\log2<24q^2/m\le24F_{P,J}(\mathbf y)\). It follows in all cases that
$$
L_{\rm clip}(\mathbf y)\le e^{24F_{P,J}(\mathbf y)}-1.
\tag{8}
$$
For completeness, \(e^{3/4}>1+3/4+(3/4)^2/2>2\) proves the logarithm bound.

Second, suppose \(q_{\rm src}<m/32\) and \(a\ge m/4\). For each \(\ell\)-element subset of the pool one-coordinates, clip all threes in \(J\) to twos and change the selected pool ones to twos. Give each of these distinct targets entry \(1/\binom a\ell\). The choices exist because \(\ell\le q_{\rm src}<m/32\le a\). If the chosen pool coordinates form a set \(V\), the exact energy change is
$$
\sum_{j\in V}(B_j-1)
-\sum_{i\in J:x_i=3}(C_{4,i}-B_i)
\le\ell(b-1)-\sum_{i\in J:x_i=3}(B_i-1)\le0.
\tag{9}
$$
The first inequality uses \(B_j\le b\) on the pool and \(C_{4,i}-B_i\ge B_i-1\) on the deleted tail; the last uses \(B_i\ge b\) on that tail. This is the only pool-energy comparison needed in this case, and it holds for unequal pool costs. All targets are feasible, selective, and distinct for different \(V\), so the row sums to 1.

On these edges the target occupancy is
\(Q_{P,J}(\mathbf y)=q_{\rm src}+\ell\): clipping preserves occupancy and each selected pool one adds exactly one occupied coordinate. In particular every target reached in this second case satisfies
$$
Q_{P,J}(\mathbf y)\le2q_{\rm src}<m/16.
\tag{10}
$$
This strict target restriction will be used for saturation.

Fix a target with \(q=Q_{P,J}(\mathbf y)\) and an integer \(\ell\ge1\). An inverse source in the second case is specified by an \(\ell\)-subset of target twos in \(J\), restored to threes, and an \(\ell\)-subset of target twos in \(P\), restored to ones. These choices determine the source uniquely and require no matching or pairing factor. Both available sets have cardinality at most \(q\), so there are at most \(q^{2\ell}/(\ell!)^2\) inverse sources. For any such source the one-count is \(a=A_P(\mathbf y)+\ell\), and
$$
\binom a\ell
\ge\frac{(a-\ell+1)^\ell}{\ell!}
\ge\frac{(m/8)^\ell}{\ell!},
\tag{11}
$$
because \(a\ge m/4\) and \(\ell<m/32\). Its row entry is the reciprocal of this binomial coefficient. Summing the inverse counts times that reciprocal, and then allowing all positive \(\ell\), yields
$$
L_{\rm one}(\mathbf y)
\le\sum_{\ell\ge1}\frac{(8q^2/m)^\ell}{\ell!}
\le e^{8F_{P,J}(\mathbf y)}-1.
\tag{12}
$$
Infeasible inverse choices or choices failing the case conditions only decrease this bound.

Third, suppose \(q_{\rm src}<m/32\) and \(a<m/4\). Put
$$
h=\min\left\lbrace b-1,\left\lfloor\frac{m}{8q_{\rm src}}\right\rfloor\right\rbrace,
\qquad
z=|\lbrace i\in P:x_i=0\rbrace|.
\tag{13}
$$
Here \(q_{\rm src}\ge\ell\ge1\), so division by \(q_{\rm src}\) is legitimate. The integer \(h\) is positive. At most \(q_{\rm src}\) pool coordinates have value two or three, whence
$$
z\ge m-a-q_{\rm src}>\frac{23m}{32},
\qquad
h\ell\le\frac{m\ell}{8q_{\rm src}}\le\frac m8.
\tag{14}
$$
For each \(h\ell\)-subset of pool zero-coordinates, clip every three in \(J\) to two and change the chosen zeros to ones. Give each distinct target entry \(1/\binom z{h\ell}\). The choices exist by (14), and the energy change obeys
$$
h\ell-\sum_{i\in J:x_i=3}(C_{4,i}-B_i)
\le h\ell-\ell(b-1)\le0.
\tag{15}
$$
Changing a pool zero to one costs exactly 1, independent of \(B_i\). Thus (15) uses only the stated tail lower bound and \(h\le b-1\), and remains valid for the heterogeneous pool. All these targets are feasible and selective, and the normalized row sums to 1.

This third transformation preserves \(Q_{P,J}\). Therefore every target it reaches has
$$
q=Q_{P,J}(\mathbf y)=q_{\rm src}<m/32,
\tag{16}
$$
and the target fixes \(h=\min\lbrace b-1,\lfloor m/(8q)\rfloor\rbrace\). In particular it cannot reach any target of occupancy at least \(m/16\).

Fix a target reached by this case and write \(A=A_P(\mathbf y)\) and \(z_{\rm tar}=|\lbrace i\in P:y_i=0\rbrace|\). For an inverse source with \(\ell\) deleted-tail threes, one has
\(A=a+h\ell\) and \(z=z_{\rm tar}+h\ell\). The target and \(\ell\) therefore fix the denominator \(\binom z{h\ell}\). An inverse source is specified uniquely by an \(\ell\)-subset of target twos in \(J\), restored to threes, and an \(h\ell\)-subset of target pool ones, restored to zeros. Hence its total fixed-\(\ell\) load is at most
$$
\binom q\ell\frac{\binom A{h\ell}}{\binom z{h\ell}}.
\tag{17}
$$
There is no pairing factor, and invalid inverse choices only reduce this expression.

If the inverse class is nonempty, (14) and \(a<m/4\) imply \(A<3m/8\) and \(z_{\rm tar}>19m/32\). Put \(\theta=A/(z_{\rm tar}+1)\). The product formula for binomial coefficients gives
$$
\frac{\binom A{h\ell}}{\binom z{h\ell}}
=\prod_{j=0}^{h\ell-1}\frac{A-j}{z-j}
\le\theta^{h\ell},
\qquad
0\le\theta\le\frac23,\qquad \theta\le\frac{2A}{m}.
\tag{18}
$$
Indeed \(z-j\ge z_{\rm tar}+1\); also
\(A/(z_{\rm tar}+1)<(3m/8)/(19m/32)=12/19<2/3\) and
\(1/(z_{\rm tar}+1)<32/(19m)<2/m\).

We next bound \(\theta^h\) using the same threshold \(b\) as in (2)-(3). If \(h=b-1\), then
$$
\theta^h\le\frac{2A}{m}\left(\frac23\right)^{b-2}
\le\frac{4A}{bm}
\le\frac{32(q+A/b)}m.
\tag{19}
$$
The middle inequality follows from \(b(2/3)^{b-2}\le2\) for integers \(b\ge2\): the value is 2 at \(b=2\), and its successive ratio is \(2(b+1)/(3b)\le1\). If \(h=\lfloor m/(8q)\rfloor\), then \(q<m/32\) implies \(m/(8q)>4\), and therefore \(h\ge m/(16q)\). Bernoulli's inequality gives \((3/2)^h\ge1+h/2\ge h/2\), so
$$
\theta^h\le(2/3)^h\le2/h\le32q/m
\le\frac{32(q+A/b)}m.
\tag{20}
$$
At least one of these two cases holds, including when the entries defining the minimum in (13) coincide. Combining (17)-(20) with \(\binom q\ell\le q^\ell/\ell!\) bounds the fixed-\(\ell\) load by \((32F_{P,J}(\mathbf y))^\ell/\ell!\). The same \(q,h,A,z_{\rm tar}\) apply to every inverse source for this target, so no extra sum over source count classes is needed. Summing over \(\ell\ge1\) gives, also for targets with no inverse source in this case,
$$
L_{\rm zero}(\mathbf y)\le e^{32F_{P,J}(\mathbf y)}-1.
\tag{21}
$$

These constructions exhaust the feasible full sources and have disjoint source classes. Their target sets may overlap, and their loads must be added. With \(F=F_{P,J}(\mathbf y)\), (8), (12), and (21) give
$$
\begin{aligned}
L(\mathbf y)
&\le1+(e^{24F}-1)+(e^{8F}-1)+(e^{32F}-1)\\
&\le e^{24F}e^{8F}e^{32F}=e^{64F}.
\end{aligned}
\tag{22}
$$
The product dominates the displayed sum because each exponential is 1 plus a nonnegative number. Thus (22) pays for every target overlap. The normalized source rows used in (7) avoid duplication of source mass.

We now improve the column envelope to its saturated form. Fix any feasible selective target and again put \(q=Q_{P,J}(\mathbf y)\). If \(q<m/16\), then \(A_P(\mathbf y)\le m\) and \(b\ge2\) imply
$$
F_{P,J}(\mathbf y)
=q\left(\frac q m+\frac{A_P(\mathbf y)}{bm}\right)
\le\frac9{16}q\le q.
\tag{23}
$$
This includes \(q=0\). Consequently the right side of (22) is already
\(\exp(64\min\lbrace F_{P,J}(\mathbf y),q\rbrace)\) on these targets.

If \(q\ge m/16\), (10) excludes all second-case preimages and (16) excludes all third-case preimages. Only the identity source and clipping sources remain. Let \(j_{\rm tar}=|\lbrace i\in J:y_i=2\rbrace|\le q\). The clipping sources correspond to nonempty subsets of these \(j_{\rm tar}\) coordinates, so their number, including the identity, is at most \(2^{j_{\rm tar}}\le2^q\). Feasibility restrictions can only decrease it. Hence \(L(\mathbf y)\le2^q\le e^{64q}\), while (22) also holds at this same target. Taking the smaller of these two upper bounds proves
$$
L(\mathbf y)
\le\min\lbrace e^{64F_{P,J}(\mathbf y)},e^{64q}\rbrace
=\exp\!\left(64\min\lbrace F_{P,J}(\mathbf y),q\rbrace\right).
\tag{24}
$$
Equations (23)-(24) prove this saturated envelope at every feasible target. Substitution into (7), followed by division by \(Z_{\rm sel}\), proves (4). Adding infeasible selective targets does not change the sum, because their original weight \(f_{\Gamma(\mathbf y)}\) is zero. Thus the expectation in (4) retains exactly the original selective marginal, without a change of tilt, cap, or normalizer.

To prove (6), set \(\delta=Z_{\rm sel}/Z_{\rm full}\). The complete supports in (5) satisfy \(\mathcal A_{\rm sel}\subseteq\mathcal A_{\rm full}\), with no height atom discarded inside a retained spatial fiber. At each selective atom \(\mathbf z\), one has \(p^{\rm full}_{\mathbf z}=\delta p^{\rm sel}_{\mathbf z}\). Therefore every closed ambient affine halfspace \(H\) satisfies \(p^{\rm full}(H)\ge\delta p^{\rm sel}(H)\). Taking infima over the same family of halfspaces containing a selective atom gives
\(\tau_{p^{\rm full}}(\mathbf z)\ge\delta\tau_{p^{\rm sel}}(\mathbf z)\).
Restricting the nonnegative full moment sum to the selective atoms now yields
$$
\begin{aligned}
M_3(p^{\rm full})
&\ge\sum_{\mathbf z\in\mathcal A_{\rm sel}}
\delta p^{\rm sel}_{\mathbf z}
\bigl(\delta\tau_{p^{\rm sel}}(\mathbf z)\bigr)^3\\
&=\delta^4M_3(p^{\rm sel})
\ge\bigl(\mathcal B^{\rm sat}_{P,J}\bigr)^{-4}M_3(p^{\rm sel}),
\end{aligned}
\tag{25}
$$
where (4) gives the last inequality. The four powers are one sampling factor and three depth factors, all in the same \(\mathbb R^N\). The stated consequence with \(\kappa,L_0\) follows by substitution.

If \(J\) is empty, there are only identity sources and \(Z_{\rm full}=Z_{\rm sel}\); (4) and (6) still hold since \(\mathcal B^{\rm sat}_{P,J}\ge1\). If \(T=0\), positivity of every nonzero site cost leaves only the zero spatial vector at height zero; then \(F_{P,J}=Q_{P,J}=0\) on the support and \(\mathcal B^{\rm sat}_{P,J}=1\). If \(q=0\), no nonidentity source can reach the target, and no division by \(q\) has been used for it. If \(m\le32\), a nonidentity source has \(q_{\rm src}\ge1\ge m/32\), so neither small-source case occurs. The argument includes \(\beta=0\), \(B_i=b\) at either boundary, unequal \(B_i\) on the pool, and \(C_{4,i}=2B_i-1\). All energy and support comparisons are weak and all halfspaces remain closed, so boundary atoms and halfspace boundaries are retained.

## External sources

None. All changed-hypothesis exchange estimates, target support restrictions, column overlaps, and moment comparisons are proved above. Accepted fact f7e7a56b865cd7a0 supplies the canonical notation and the selective-exchange framework; its equal-pool-cost conclusion is not invoked for the present heterogeneous pool.
