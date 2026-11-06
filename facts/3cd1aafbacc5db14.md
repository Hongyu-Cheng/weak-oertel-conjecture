---
fact_id: 3cd1aafbacc5db14
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: intake13-layer-one-dimensional-sharp
depends_on: []
verifier_run: 796b4e2c0bc64e92
target_match: null
---

## Statement

Let \(I=\{a,a+1,\ldots,a+m-1\}\subset\mathbb Z\), where \(m\ge1\), and let \(w_j=\exp(\alpha+\lambda j)>0\) on \(I\). Put
\[
W=\sum_{j\in I}w_j,
\qquad
A_s=\{j\in I:w_j\ge s\},
\qquad
d_{A_s}(j)=\inf_{H\ni j}|A_s\cap H|,
\]
where \(H\subset\mathbb R\) ranges over closed halfspaces, and define
\[
L(w)=3\int_0^\infty s^2\sum_{j\in A_s}d_{A_s}(j)^2\,ds.
\]
After translating and, if necessary, reflecting \(I\), and after dividing all weights by a common positive constant, the table is
\[
I=\{0,1,\ldots,m-1\},\qquad w_j=q^j,\qquad 0<q\le1.
\]
For this normalization one has the exact identity
\[
L(w)=\sum_{r=0}^{m-1}\left\lceil\frac{r+1}{2}\right\rceil^2q^{3r}.
\tag{1}
\]
For every such finite positive log-affine interval table,
\[
L(w)\ge\frac1{54}W^3,
\tag{2}
\]
and \(1/54\) is optimal over finite admissible interval tables.

More generally, let \(N\ge1\), let \(Q\subset\mathbb R^N\) be compact and convex, let \(D=Q\cap\mathbb Z^N\ne\varnothing\), and give \(D\) log-affine weights \(w_{\mathbf z}=\exp(\boldsymbol\ell\cdot\mathbf z)\). Define \(W,A_s,d_{A_s}\), and \(L(w)\) by the same formulas in ambient dimension \(N\). If an integer unimodular affine map sends \(D\) into \(\{0,1\}^{N-1}\times\mathbb Z\), then
\[
L(w)\ge\frac{2}{27}\,4^{-N}W^3.
\tag{3}
\]
The coefficient \(2/27\) in (3) is optimal for this class, in the sense that the infimum of \(4^NL(w)/W^3\) over its finite admissible tables is \(2/27\).

## Proof

Integer translations and reflections send closed halfspaces to closed halfspaces and preserve all counting depths. Multiplying every weight by \(c>0\) changes \(W\) to \(cW\), sends the superlevel set at height \(s\) to the old superlevel set at height \(s/c\), and, after the substitution \(s=ct\), changes \(L(w)\) to \(c^3L(w)\). Thus it suffices for the one-dimensional assertions to use the normalization in the statement.

For \(k\ge1\), let
\[
F(k)=\sum_{j=0}^{k-1}\min\{j+1,k-j\}^2.
\]
The two closed rays based at \(j\) show that the counting depth of \(j\) in \(\{0,\ldots,k-1\}\) is exactly \(\min\{j+1,k-j\}\). Moreover,
\[
F(k)-F(k-1)=\left\lceil\frac{k}{2}\right\rceil^2,
\tag{4}
\]
with \(F(0)=0\). Indeed,
\[
F(2h)=2\sum_{i=1}^h i^2,
\qquad
F(2h-1)=2\sum_{i=1}^{h-1}i^2+h^2,
\]
which gives (4) for both parities.

Assume first \(0<q<1\). Up to threshold values, which do not affect the integral, the superlevel set is \(\{0,\ldots,k-1\}\) for \(q^k<s<q^{k-1}\), and the full interval occurs for \(0<s<q^{m-1}\). Hence
\[
\begin{aligned}
L(w)
&=\sum_{k=1}^{m-1}\bigl(q^{3(k-1)}-q^{3k}\bigr)F(k)
  +q^{3(m-1)}F(m)\\
&=F(1)+\sum_{r=1}^{m-1}\bigl(F(r+1)-F(r)\bigr)q^{3r}.
\end{aligned}
\]
Equation (4) gives (1). When \(q=1\), every nonempty superlevel set is the full interval and \(L(w)=F(m)\), which is the same identity by telescoping.

It remains to prove the sharp cubic comparison. Write
\[
W^3=\sum_{s=0}^{3m-3}N_m(s)q^s,
\]
where \(N_m(s)\) is the number of ordered triples \((i_1,i_2,i_3)\in\{0,\ldots,m-1\}^3\) with sum \(s\), and set \(N_m(s)=0\) outside this range. Plainly
\[
N_m(s)\le\binom{s+2}{2}\qquad(s\ge0),
\tag{5}
\]
because the right side counts all ordered triples of nonnegative integers with sum \(s\).

For \(\varepsilon\in\{0,1,2\}\), weighted arithmetic-geometric mean gives
\[
q^{3r+\varepsilon}
\le
\left(1-\frac{\varepsilon}{3}\right)q^{3r}
+\frac{\varepsilon}{3}q^{3(r+1)}.
\tag{6}
\]
Apply (6) to every term in the preceding expansion. This gives
\[
W^3\le\sum_{r=0}^{m-1}C_{m,r}q^{3r},
\]
where, with the zero convention on \(N_m\),
\[
\begin{aligned}
C_{m,r}={}&N_m(3r)+\frac23N_m(3r+1)+\frac13N_m(3r+2)\\
&+\frac13N_m(3r-2)+\frac23N_m(3r-1).
\end{aligned}
\]
Using (5), with \(\binom{0}{2}=\binom{1}{2}=0\), gives the complete coefficient bound
\[
\begin{aligned}
C_{m,r}
&\le \binom{3r+2}{2}
+\frac23\binom{3r+3}{2}
+\frac13\binom{3r+4}{2}
+\frac13\binom{3r}{2}
+\frac23\binom{3r+1}{2}\\
&=\frac{27}{2}r(r+1)+5\\
&\le\frac{27}{2}(r+1)^2
\le54\left\lceil\frac{r+1}{2}\right\rceil^2.
\end{aligned}
\tag{7}
\]
No endpoint term is lost here: \(N_m(s)=0\) beyond \(3m-3\), so (6) creates no \(q^{3m}\) term. Summing (7) and using (1) proves \(W^3\le54L(w)\), hence (2).

To prove optimality using finite intervals, fix \(q\in(0,1)\) and let \(m\to\infty\). From (1), with \(x=q^3\),
\[
\begin{aligned}
\lim_{m\to\infty}L(w)
&=\sum_{h\ge1}h^2\bigl(x^{2h-2}+x^{2h-1}\bigr)
=\frac{(1+x)(1+x^2)}{(1-x^2)^3}\\
&=\frac{(1+q^3)(1+q^6)}{(1-q^6)^3},
\qquad
\lim_{m\to\infty}W=\frac1{1-q}.
\end{aligned}
\]
Therefore
\[
\lim_{q\uparrow1}\lim_{m\to\infty}\frac{L(w)}{W^3}
=\lim_{q\uparrow1}
\frac{(1+q^3)(1+q^6)(1-q)^3}{(1-q^6)^3}
=\frac1{54}.
\tag{8}
\]
For each \(q\), both limits in \(m\) are limits of finite admissible tables. Choosing \(q\uparrow1\) and then a sufficiently large finite \(m\) gives a diagonal sequence of finite tables whose ratios converge to \(1/54\). Thus the constant in (2) is optimal.

We now prove (3). An integer unimodular affine map bijects \(\mathbb Z^N\), maps closed halfspaces bijectively to closed halfspaces, and preserves all transported weight values. The transported logarithm is affine; its constant term is harmless by the common-weight scaling already proved. Thus the map preserves \(W\), every superlevel counting depth, and \(L(w)\), and we may assume
\[
D\subseteq\{0,1\}^{N-1}\times\mathbb Z.
\]
For a Boolean label \(\boldsymbol\eta\in\{0,1\}^{N-1}\), let
\[
D_{\boldsymbol\eta}=\{t\in\mathbb Z:(\boldsymbol\eta,t)\in D\},
\qquad
W_{\boldsymbol\eta}=\sum_{t\in D_{\boldsymbol\eta}}w_{(\boldsymbol\eta,t)}.
\]
Convexity of \(Q\) and the identity \(D=Q\cap\mathbb Z^N\) imply that every nonempty \(D_{\boldsymbol\eta}\) is a finite integer interval. The restricted weights remain positive and log-affine on that interval.

Fix \(s>0\), a nonempty fiber superlevel set
\[
B_{s,\boldsymbol\eta}
=\{t\in D_{\boldsymbol\eta}:w_{(\boldsymbol\eta,t)}\ge s\},
\]
and \(t\in B_{s,\boldsymbol\eta}\). If an ambient closed halfspace \(H\subset\mathbb R^N\) contains \((\boldsymbol\eta,t)\), then its intersection with the affine fiber \(\{\boldsymbol\eta\}\times\mathbb R\) is a closed halfline containing that point or the whole line. Consequently
\[
d_{A_s}(\boldsymbol\eta,t)
\ge d_{B_{s,\boldsymbol\eta}}(t),
\tag{9}
\]
where the right side is one-dimensional counting depth. Summing (9), integrating, and applying (2) separately to every nonempty fiber yields
\[
L(w)\ge\sum_{\boldsymbol\eta}L(w|_{D_{\boldsymbol\eta}})
\ge\frac1{54}\sum_{\boldsymbol\eta}W_{\boldsymbol\eta}^3.
\tag{10}
\]
There are at most \(2^{N-1}\) nonempty labels. Hölder's inequality therefore gives
\[
W^3=\left(\sum_{\boldsymbol\eta}W_{\boldsymbol\eta}\right)^3
\le 4^{N-1}\sum_{\boldsymbol\eta}W_{\boldsymbol\eta}^3.
\tag{11}
\]
Combining (10) and (11) proves (3), including empty and singleton fibers.

Finally, fix \(N\ge1\) and take
\[
D_{N,m}=\{0,1\}^{N-1}\times\{0,\ldots,m-1\},
\qquad
w_{(\boldsymbol\eta,t)}=q^t.
\]
This is the complete lattice support of the displayed product box, and all \(2^{N-1}\) fibers have the same mass. At every superlevel, each Boolean-labeled fiber is an exposed face of the convex hull of that superlevel support. More explicitly, for a fixed label \(\boldsymbol\eta\), the affine function
\[
\psi_{\boldsymbol\eta}(\mathbf u)
=\sum_{i:\eta_i=1}u_i+\sum_{i:\eta_i=0}(1-u_i)
\]
equals \(N-1\) at \(\boldsymbol\eta\) and is at most \(N-2\) at every other Boolean label. Adding a sufficiently large positive multiple of \(\psi_{\boldsymbol\eta}-(N-1)\) to either one-dimensional ray inequality through \(t\) excludes every other label while preserving the chosen ray in the target fiber. Together with (9), this proves equality of ambient and fiber counting depths. Hence, writing \(L_{m,q}\) and \(W_{m,q}\) for one fiber,
\[
L(w)=2^{N-1}L_{m,q},
\qquad
W=2^{N-1}W_{m,q},
\]
and therefore
\[
4^N\frac{L(w)}{W^3}
=4\frac{L_{m,q}}{W_{m,q}^3}.
\]
The finite diagonal sequence from (8) makes the last expression tend to \(4/54=2/27\). This proves optimality in (3), also for \(N=1\), where there is a single fiber and the exposing term is unnecessary.

## External sources

none
