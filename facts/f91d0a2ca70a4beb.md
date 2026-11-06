---
fact_id: f91d0a2ca70a4beb
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct21-window-truncated-occupation
depends_on: ["7777b3e7563f2742"]
verifier_run: 1dcd3f019cc5419f
target_match: null
---

## Statement

Let \(k\ge1\), \(b\ge2\), and \(T\ge0\) be integers, let \(\beta\ge0\) be real, and let the integer costs satisfy \(b\le B_i\le2b\) and \(C_{4,i}\ge2B_i-1\) for every \(i\in[k]=\lbrace1,\ldots,k\rbrace\). Give every spatial vector multiplicity one, and define
$$
\begin{aligned}
g_i(0)&=0,&g_i(1)&=1,&g_i(2)&=B_i,&g_i(3)&=C_{4,i},\\
\Gamma(\mathbf x)&=\sum_{i=1}^k g_i(x_i),&
f_E&=\begin{cases}\displaystyle\sum_{t=E}^{T}e^{-\beta t},&0\le E\le T,\\0,&E>T,\end{cases}\\
Z_4&=\sum_{\mathbf x\in\lbrace0,1,2,3\rbrace^k}f_{\Gamma(\mathbf x)},&
Z_3&=\sum_{\mathbf x\in\lbrace0,1,2\rbrace^k}f_{\Gamma(\mathbf x)}.
\end{aligned}
\tag{1}
$$
Here \(E\) is a nonnegative integer. These are precisely the objects \(k,b,T,\beta,B_i,C_{4,i},g_i,\Gamma,f_E,Z_4,Z_3\) of accepted fact `7777b3e7563f2742`, with its aliases \(Z_{\rm full}=Z_4\) and \(Z_{\rm sel}=Z_3\). In particular the height tails include every original integer height, including both endpoints. The locked objects \(S\), \(n\), \(d\), \(C\), and \(c_0\) retain their locked meanings.

For a full spatial vector define \(Q(\mathbf x)=|\lbrace i:x_i\in\lbrace2,3\rbrace\rbrace|\). For every integer \(H\) with \(1\le H\le k/128\), put
$$
\begin{aligned}
Z_4^{Q\le H}&=\sum_{\substack{\mathbf x\in\lbrace0,1,2,3\rbrace^k\\Q(\mathbf x)\le H}}f_{\Gamma(\mathbf x)},\\
h_H&=\min\left\lbrace b-1,\left\lfloor\frac{k-H}{16H}\right\rfloor\right\rbrace,\qquad
D_H=\frac{100H^{3/2}}{\sqrt{k}}+2H\left(\frac23\right)^{h_H}.
\end{aligned}
\tag{2}
$$
Then \(h_H\ge1\), and
$$
\frac{Z_4^{Q\le H}}{Z_3}\le \exp(D_H).
\tag{3}
$$
The constants and the right-hand side are independent of \(T\) and \(\beta\), and independent of the individual costs subject to the displayed window hypotheses.

More explicitly, for every fixed real \(a>0\), \(A>0\), and \(p\ge0\), there is an integer \(k_0=k_0(a,A,p)\) such that all the displayed models with \(k\ge k_0\), \(b\ge a\sqrt{k}\), and \(1\le H\le A(1+\log k)^p\) satisfy \(H\le k/128\) and \(Z_4^{Q\le H}\le e Z_3\). The upper bound in (3) is \(\exp(o(1))\) uniformly over those models as \(k\to\infty\).

## Proof

The zero spatial vector at height zero is present, so \(Z_3>0\). If \(0\le E'\le E\), the original tails in (1) satisfy \(f_E\le f_{E'}\), with the same conclusion when the larger energy exceeds \(T\). Consequently every energy-decreasing transformation compares the complete original tails. We will use the weighted edge-counting mechanism of accepted fact `7777b3e7563f2742`, proving below the occupation restrictions and all coefficients needed here. For any collection of energy-decreasing edges from sources \(\mathbf x\) to targets \(\mathbf y\), one has
$$
\sum_{\mathbf x\sim\mathbf y} f_{\Gamma(\mathbf x)}
\le \sum_{\mathbf x\sim\mathbf y} f_{\Gamma(\mathbf y)}.
\tag{4}
$$
The inequality also holds after multiplying each edge by a nonnegative entry. In particular, a kernel with row sums one and column sums at most \(L\) bounds its total source mass by \(L\) times its allowed target mass.

First prove a single-third estimate on an arbitrary set of \(\nu\) coordinates satisfying the same cost hypotheses, with any nonnegative integer cap and the same original form of height tails. Here \(\nu\) is the number of coordinates in this local model; the notation will later be applied with \(\nu=k-\ell+1\). For an integer \(u\) with \(1\le u\le\nu/16\), write \(V_1(u)\) for the mass with exactly one three and occupation at most \(u\), and \(V_0(u+1)\) for the all-ternary mass with occupation at most \(u+1\). Define the common integer
\(h(\nu,u)=\min\lbrace b-1,\lfloor\nu/(8u)\rfloor\rbrace\). We claim
$$
V_1(u)\le
\left[\frac{32u^{3/2}}{\sqrt{\nu}}+
 u\left(\frac23\right)^{h(\nu,u)}\right]V_0(u+1).
\tag{5}
$$
All occupations and one-counts in this local argument refer only to its \(\nu\) coordinates.

Order these coordinates by nondecreasing \(B_i\), breaking ties in a fixed manner, and let \(m=\lceil\sqrt{\nu u}\rceil\). Let \(I_{\rm low}\) be the first \(m\) labels and \(I_{\rm high}\) the rest. Because \(1\le u\le\nu/16\), one has \(\nu\ge16\), \(\sqrt{\nu u}\ge4\), and
$$
\sqrt{\nu u}\le m\le\frac54\sqrt{\nu u},\qquad
m\ge4u,\qquad m-u\ge\frac34m,\qquad m<\nu.
\tag{6}
$$
For the last inequality, \(m\le\nu/4+1\le5\nu/16<\nu\).

Let \(v\) be a source's number of ones, and \(q\le u\) its occupation. Consider first the sources with \(v\ge\nu/4\) whose three is at \(i\in I_{\rm low}\). For every source one-position \(j\), replace the three at \(i\) by zero and the one at \(j\) by two. The energy change is
\(B_j-1-C_{4,i}\le2b-1-(2B_i-1)\le0\). There are exactly \(v\) distinct targets, and their occupation is \(q\). A target has at most \(mQ(\mathbf y)\le mu\) inverse sources, specified by a zero-position in \(I_{\rm low}\) to restore to three and a two-position to restore to one. Equation (4) bounds this source mass by \((4mu/\nu)V_0(u+1)\).

Next take the sources with \(v\ge\nu/4\) whose three is at \(i\in I_{\rm high}\). For every source one-position \(j\in I_{\rm low}\), clip the three at \(i\) to two and promote the one at \(j\) to two. The energy change is
$$
(B_j-1)-(C_{4,i}-B_i)
\le (B_j-1)-(B_i-1)\le0.
\tag{7}
$$
The target occupation is exactly \(q+1\), and hence at most \(u+1\).

To bound the source-weighted outdegree, fix \(i\), the source set \(I_2\) of two-positions, and the integer \(v\ge\nu/4\). Then \(q=|I_2|+1\le u\), and the ones can be any \(v\)-subset of the \(\nu-q\) coordinates outside \(I_2\cup\lbrace i\rbrace\). All those placements have exactly the same energy \(C_{4,i}+\sum_{j\in I_2}B_j+v\) and the same original tail weight. Their average number of ones in \(I_{\rm low}\) is
$$
\frac{v\bigl(m-|I_2\cap I_{\rm low}|\bigr)}{\nu-q}
\ge\frac{m-q+1}{4}\ge\frac{m-u}{4}.
\tag{8}
$$
Indeed each available position appears in the fraction \(v/(\nu-q)\) of all those subsets, and \(v/(\nu-q)\ge1/4\). The restrictions on source occupation and one-count hold throughout each class, and feasibility is constant throughout that class. Thus summing (8) proves the same lower bound for the outdegree averaged with the actual original weights.

Every target has at most \(Q(\mathbf y)^2\le(u+1)^2\le4u^2\) inverse sources: choose its two-position in \(I_{\rm high}\) to restore to three and its two-position in \(I_{\rm low}\) to restore to one. This bound explicitly allows the target occupation to have increased. Equations (4) and (8) therefore bound this source mass by \(16u^2/(m-u)\) times \(V_0(u+1)\). The two high-one coefficients together satisfy
$$
\frac{4mu}{\nu}+\frac{16u^2}{m-u}
\le\left(5+\frac{64}{3}\right)\frac{u^{3/2}}{\sqrt{\nu}}
\le\frac{32u^{3/2}}{\sqrt{\nu}},
\tag{9}
$$
by (6).

It remains to treat every source with \(v<\nu/4\), wherever its unique three lies. Put \(h=h(\nu,u)\). Then \(h\ge1\), \(h\le b-1\), and \(h\le\nu/(8u)\le\nu/8\). If \(z=\nu-v-q\) is the source zero-count, the hypotheses give
$$
z>\frac{11\nu}{16},\qquad
z-h>\frac{9\nu}{16},\qquad
v+h<\frac{3\nu}{8}.
\tag{10}
$$
Clip the unique three to two and promote any \(h\) source zeros to ones. The energy change is at most
\(h-(C_{4,i}-B_i)\le(b-1)-(B_i-1)\le0\). Give each of the \(\binom zh\) distinct targets kernel entry \(1/\binom zh\). The row sum is one and occupation is preserved.

For a target with an inverse source, its one-count and zero-count determine \(v\) and \(z\), because \(h\) is common to all sources. Its inverse sources are specified by a target two-position to restore to three and \(h\) target one-positions to restore to zero. Therefore its column sum is at most
$$
Q(\mathbf y)\frac{\binom{v+h}{h}}{\binom zh}
\le Q(\mathbf y)\left(\frac{v+h}{z-h+1}\right)^h
\le u\left(\frac23\right)^h.
\tag{11}
$$
The product formula proves the first inequality; each numerator factor is at most \(v+h\), and each denominator factor is at least \(z-h+1\). Equation (10) proves the last inequality. Since target occupation is at most \(u\), the kernel form of (4) bounds this entire low-one source mass by \(u(2/3)^hV_0(u+1)\). No bound on the cap or on \(v\) in terms of the cap has been used. The three source cases are disjoint and exhaustive, so (9) and (11) prove (5).

We next iterate (5) with the exact source-count multiplicities. For integers \(0\le\ell\le k\) and \(J\ge0\), let \(Z^{(\ell)}_{\le J}\) be the original mass in (1) with exactly \(\ell\) threes and occupation at most \(J\). Thus it is a restriction of the count mass \(Z^{(\ell)}\) in accepted fact `7777b3e7563f2742`, and \(Z^{(0)}_{\le J}\le Z_3\).

Fix \(1\le\ell\le H\), and let \(J\) be any integer satisfying \(\ell\le J\) and \(J-\ell+1\le2H\). Fix a set \(F\subseteq[k]\) of size \(\ell-1\) at site three. Put \(E_F=\sum_{i\in F}C_{4,i}\), \(T_F=T-E_F\), \(\nu=k-\ell+1\), and \(u=J-\ell+1\). Let \(U_1(F,J)\) be the original mass with these fixed threes, exactly one additional three, and total occupation at most \(J\). Let \(U_0(F,J+1)\) be the original mass with exactly these threes, every other coordinate ternary, and total occupation at most \(J+1\).

If \(T_F<0\), both masses are zero. If \(T_F\ge0\), exact translation of every original integer height gives
$$
f_{E_F+E}=e^{-\beta E_F}
\sum_{t'=E}^{T_F}e^{-\beta t'}
\tag{12}
$$
for all nonnegative integer residual energies \(E\), with an empty sum equal to zero. The residual source occupation bound is \(u\), and the residual target bound is \(u+1\). The common factor \(e^{-\beta E_F}\) in (12) cancels from (5).

Because \(H\le k/128\), \(\nu\ge k-H\), and \(u\le2H\), one has
\(u/\nu\le2H/(k-H)\le2/127<1/16\). Thus (5) applies. Moreover
$$
\begin{aligned}
h(\nu,u)&\ge
\min\left\lbrace b-1,\left\lfloor\frac{k-H}{16H}\right\rfloor\right\rbrace=h_H,\\
\frac{32u^{3/2}}{\sqrt{\nu}}+
 u\left(\frac23\right)^{h(\nu,u)}
&\le\frac{32(2H)^{3/2}}{\sqrt{k-H}}+
2H\left(\frac23\right)^{h_H}
\le D_H.
\end{aligned}
\tag{13}
$$
The last inequality follows from \(k-H\ge127k/128\) and
\(32\cdot2^{3/2}\sqrt{128/127}<100\). Also \((k-H)/(16H)\ge127/16\), so \(h_H\ge1\). Combining (5), (12), and (13), including the zero-mass case, gives \(U_1(F,J)\le D_H U_0(F,J+1)\).

Summing over all \(F\) of size \(\ell-1\) yields the exact identities
$$
\sum_{|F|=\ell-1}U_1(F,J)=\ell Z^{(\ell)}_{\le J},
\qquad
\sum_{|F|=\ell-1}U_0(F,J+1)=Z^{(\ell-1)}_{\le J+1}.
\tag{14}
$$
A source with exactly \(\ell\) threes occurs for the \(\ell\) sets formed by omitting one of its three-positions. A target with exactly \(\ell-1\) threes occurs only for its full set of three-positions. Every occurrence carries its identical original full height tail. Hence
$$
\ell Z^{(\ell)}_{\le J}\le D_H Z^{(\ell-1)}_{\le J+1}
\tag{15}
$$
for the specified \(\ell,J\).

For a fixed \(1\le\ell\le H\), apply (15) successively with current third-count \(s=\ell,\ell-1,\ldots,1\) and current occupation cutoff \(J_s=H+\ell-s\). At each step \(J_s\ge s\), and its residual cutoff satisfies \(J_s-s+1=H+\ell-2s+1\le2H-1\); therefore all these applications meet the stated conditions. The resulting estimate is
$$
Z^{(\ell)}_{\le H}
\le\frac{D_H^\ell}{\ell!}Z^{(0)}_{\le H+\ell}
\le\frac{D_H^\ell}{\ell!}Z_3.
\tag{16}
$$
Thus the final all-ternary cutoff may reach \(H+\ell\le2H\); it was never assumed to stay at \(H\). A vector with occupation at most \(H\) has at most \(H\) threes, and the \(\ell=0\) term is at most \(Z_3\). Summing (16) proves
\(Z_4^{Q\le H}\le Z_3\sum_{\ell=0}^H D_H^\ell/\ell!\le e^{D_H}Z_3\), which is (3).

For the final uniform consequence, fix \(a,A,p\) as in the statement. When \(H\le A(1+\log k)^p\), one has \(H/k\to0\) and \(H/\sqrt{k}\to0\), uniformly over those integers \(H\). For all sufficiently large \(k\) depending only on \(a,A,p\), both \(b-1\ge(a/2)\sqrt{k}\) and \(\lfloor(k-H)/(16H)\rfloor\ge(a/2)\sqrt{k}\) follow from \(b\ge a\sqrt{k}\) and this bound on \(H\). Consequently
$$
D_H\le
\frac{100A^{3/2}(1+\log k)^{3p/2}}{\sqrt{k}}
+2A(1+\log k)^p\left(\frac23\right)^{(a/2)\sqrt{k}}
\longrightarrow0.
\tag{17}
$$
Enlarging \(k_0\) ensures \(H\le k/128\) and \(D_H\le1\), proving the claimed absolute comparison and the uniform \(\exp(o(1))\) upper bound.

All energy comparisons were weak inequalities, so tied costs and the endpoint costs \(B_j=2b\), \(B_i=b\), \(C_{4,i}=2b-1\) are included. The residual cap can equal zero, the original cap can equal zero, and \(\beta=0\) is allowed in (4) and (12). When \(T=0\), only the zero spatial vector is feasible and (3) holds directly as well. For \(k<128\) there is no integer \(H\) in the asserted range. No moment or ambient halfspace object is redefined; the result is a comparison of the specified original masses.

## External sources

None. Accepted fact `7777b3e7563f2742` supplies the canonical original model and the weighted single-third exchange mechanism. The source restriction, the larger target occupation, the cap-free low-one estimate, the enlarged-cutoff recurrence, and its factorial summation are all proved above.
