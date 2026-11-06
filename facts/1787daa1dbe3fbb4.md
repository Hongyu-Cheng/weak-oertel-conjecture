---
fact_id: 1787daa1dbe3fbb4
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: linear-threshold-depth
depends_on: ["48f7ad59d388c8c8","4cfd86cd551df9e7","978e8555ec5bac42","b80d9c776d7d7d77"]
verifier_run: 0e06c14cf62643ea
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subset\mathbb R^{n+d}\) be a convex body, and put
\[
\Lambda:=\mathbb Z^n\times\mathbb R^d,\qquad
S:=C\cap\Lambda,\qquad
K:=\operatorname{proj}_{\mathbb R^n}(C).
\]
For every measurable \(T\subseteq\Lambda\), use the mixed-integer volume
\[
\mathcal H_d(T):=
\sum_{\mathbf z\in\mathbb Z^n}
\mathcal H_d\!\left(T\cap(\{\mathbf z\}\times\mathbb R^d)\right).
\]
Suppose that, for some \(\mathbf z_0\in\mathbb R^n\) and \(k>0\),
\[
\mathbf z_0+k\mathbb B_\infty^n\subseteq K,
\qquad
\mathbb B_\infty^n:=\{\mathbf u\in\mathbb R^n:\|\mathbf u\|_\infty\leq1\},
\qquad
k\geq\frac{3e}{2}(n+d).
\]
Then there exists \(\mathbf y^\star\in S\) such that every closed halfspace \(H\subseteq\mathbb R^{n+d}\) containing \(\mathbf y^\star\) satisfies
\[
\mathcal H_d(S\cap H)
\geq
\left(\frac1e-\frac{3(n+d)}{2k}\right)\mathcal H_d(S).
\]
If in addition \(k\geq3e(n+d)\), then the same point satisfies
\[
\mathcal H_d(S\cap H)
\geq\frac1{2e}\mathcal H_d(S)
\geq\frac1{2^ne}\mathcal H_d(S)
\]
for every such \(H\).

## Proof

Put \(m:=n+d\). For a Borel set \(D\subseteq\mathbb R^m\), write
\[
V(D):=\mathcal H_m(D),
\qquad
\mu(D):=
\sum_{\mathbf z\in\mathbb Z^n}
\mathcal H_d\!\left(D\cap(\{\mathbf z\}\times\mathbb R^d)\right).
\]
Thus \(\mu(C)=\mathcal H_d(S)\) and \(\mu(C\cap H)=\mathcal H_d(S\cap H)\).

First check every parameter range used below. Since \(n,d\geq1\), one has \(m\geq2\), and the assumed threshold gives
\[
k\geq\frac{3e}{2}m\geq3e>\frac32.
\]
Consequently \(k>\frac12\), \(k-\frac12>\frac12\), and
\[
R:=\frac{k-\frac12}{2}=\frac{2k-1}{4}>\frac12.
\]
These are exactly the three radii to which the mixed-continuous comparison will be applied. Also \(0<1/(2k)<1\), \(0<4/(2k+1)<1\), and \(0<3/(2k+1)<1\), so the homothety and both Bernoulli estimates below are valid throughout the stated range, including its lower endpoint.

Apply the accepted centroid-rounding fact \(48f7ad59d388c8c8\) with \(\epsilon=1/(2k)\). It gives \(\mathbf w\in C\) and the convex body
\[
C':=\left(1-\frac1{2k}\right)C+\frac1{2k}\mathbf w\subseteq C
\]
such that
\[
V(C')=\left(\frac{2k-1}{2k}\right)^mV(C),
\]
\(\operatorname{proj}_{\mathbb R^n}(C')\) contains a translate of \((k-\frac12)\mathbb B_\infty^n\), and
\[
\mathbf y^\star:=\mathfrak c(C')\in C'\cap\Lambda\subseteq S.
\]

The accepted mixed-continuous comparison fact \(4cfd86cd551df9e7\), applied first to \(C\) with radius \(k\), gives
\[
\mu(C)\leq
\left(1+\frac1{2k}\right)^mV(C).
\]
Combining this with the exact volume of \(C'\) yields the global conversion
\[
V(C')
\geq
\left(\frac{2k-1}{2k+1}\right)^m\mu(C).
\tag{1}
\]

By the accepted boundary-reduction fact \(978e8555ec5bac42\), it is enough to prove the desired bound for a closed halfspace whose boundary contains \(\mathbf y^\star\). Fix such a halfspace and write
\[
H:=\{\mathbf y:\mathbf a^\top(\mathbf y-\mathbf y^\star)\geq0\},
\qquad
\bar H:=\{\mathbf y:\mathbf a^\top(\mathbf y-\mathbf y^\star)\leq0\},
\qquad
\mathbf a\neq\mathbf0.
\]
Set \(A:=C'\cap H\) and \(B:=C'\cap\bar H\). With
\[
\gamma_m:=\left(\frac{m}{m+1}\right)^m,
\]
the exact Grünbaum inequality, applied to both closed halfspaces because both contain \(\mathfrak c(C')=\mathbf y^\star\), gives
\[
V(A)\geq\gamma_mV(C'),
\qquad
V(B)\geq\gamma_mV(C').
\tag{2}
\]
Here \(\gamma_m=(1+1/m)^{-m}\geq e^{-1}\). In particular, \(A\) and \(B\) have positive \(m\)-dimensional volume and hence are convex bodies. Since their common part lies in the hyperplane \(\partial H\), which has zero \(m\)-dimensional volume,
\[
V(A)+V(B)=V(C'),
\qquad
V(B)\leq(1-\gamma_m)V(C')\leq\left(1-\frac1e\right)V(C').
\tag{3}
\]

The accepted halfspace-bisection fact \(b80d9c776d7d7d77\), applied to \(C'\), \(H\), and \(\bar H\), says that at least one of \(A\) and \(B\) contains a translate of \(\frac12C'\). The projection of that piece therefore contains a translate of
\[
\frac{k-\frac12}{2}\mathbb B_\infty^n=R\mathbb B_\infty^n.
\]
We treat both possibilities.

Case 1: \(A\) contains such a translate. Applying \(4cfd86cd551df9e7\) to \(A\) with radius \(R=(2k-1)/4\), and then using (2) and (1), gives
\[
\begin{aligned}
\mu(C\cap H)
&\geq\mu(A)\\
&\geq
\left(1-\frac1{2R}\right)^mV(A)\\
&=
\left(\frac{2k-3}{2k-1}\right)^mV(A)\\
&\geq
\gamma_m\left(\frac{2k-3}{2k+1}\right)^m\mu(C)\\
&\geq
\frac1e\left(\frac{2k-3}{2k+1}\right)^m\mu(C).
\end{aligned}
\tag{4}
\]
Every factor has thus arisen from, respectively, comparison at radius \(R\), exact Grünbaum, and the conversion (1).

Case 2: \(B\) contains such a translate. Mixed-integer volume may charge \(\partial H\), so the two closed sides cannot be added as a disjoint partition. Use instead the open complementary halfspace
\[
H_-:=\{\mathbf y:\mathbf a^\top(\mathbf y-\mathbf y^\star)<0\}.
\]
The sets \(H\) and \(H_-\) are disjoint and cover \(\mathbb R^m\), while \(H_-\subseteq\bar H\). Hence, with \(S':=C'\cap\Lambda\),
\[
\begin{aligned}
\mu(C'\cap H)
&=\mu(C')-\mu(C'\cap H_-)\\
&\geq\mu(C')-\mu(B).
\end{aligned}
\tag{5}
\]
This retains all mixed-integer mass on the cutting hyperplane in \(C'\cap H\).

Apply \(4cfd86cd551df9e7\) from below to \(C'\), whose projection radius is \(k-\frac12\), and from above to \(B\), whose projection contains the radius-\(R\) translate. Together with (3), this gives
\[
\mu(C')
\geq
\left(1-\frac1{2k-1}\right)^mV(C')
=
\left(\frac{2k-2}{2k-1}\right)^mV(C'),
\tag{6}
\]
\[
\mu(B)
\leq
\left(1+\frac1{2R}\right)^mV(B)
\leq
(1-\gamma_m)
\left(\frac{2k+1}{2k-1}\right)^mV(C').
\tag{7}
\]
Define
\[
q:=
\left(\frac{2k-2}{2k-1}\right)^m
-(1-\gamma_m)
\left(\frac{2k+1}{2k-1}\right)^m,
\qquad
\rho:=\frac{2k-1}{2k+1}.
\]
Before using the lower bound (1) for \(V(C')\), we must check that \(q\geq0\). Bernoulli's inequality and the main threshold give
\[
\begin{aligned}
q\rho^m
&=
\left(\frac{2k-2}{2k+1}\right)^m-(1-\gamma_m)\\
&=
\left(1-\frac3{2k+1}\right)^m-(1-\gamma_m)\\
&\geq
\gamma_m-\frac{3m}{2k+1}\\
&\geq
\frac1e-\frac{3m}{2k+1}>0,
\end{aligned}
\tag{8}
\]
because \(2k+1>3em\). Thus \(q>0\), so (1) may be multiplied by \(q\) without reversing the inequality. Equations (5)-(8) now yield
\[
\begin{aligned}
\mu(C\cap H)
&\geq\mu(C'\cap H)\\
&\geq qV(C')\\
&\geq q\rho^m\mu(C)\\
&=
\left[
\left(\frac{2k-2}{2k+1}\right)^m-(1-\gamma_m)
\right]\mu(C)\\
&\geq
\left[
\left(\frac{2k-2}{2k+1}\right)^m-\left(1-\frac1e\right)
\right]\mu(C).
\end{aligned}
\tag{9}
\]

It remains to reduce the two case bounds to the stated common coefficient. Bernoulli's inequality \((1-t)^m\geq1-mt\), valid here because the two values of \(t\) lie in \([0,1]\), gives for (4)
\[
\begin{aligned}
\frac1e\left(\frac{2k-3}{2k+1}\right)^m
&=
\frac1e\left(1-\frac4{2k+1}\right)^m\\
&\geq
\frac1e-\frac{4m}{e(2k+1)}\\
&\geq
\frac1e-\frac{2m}{ek}\\
&\geq
\frac1e-\frac{3m}{2k}.
\end{aligned}
\tag{10}
\]
The penultimate inequality uses \(4/(2k+1)\leq2/k\), and the last uses \(2/e\leq3/2\). For (9),
\[
\begin{aligned}
\left(\frac{2k-2}{2k+1}\right)^m-\left(1-\frac1e\right)
&=
\left(1-\frac3{2k+1}\right)^m-\left(1-\frac1e\right)\\
&\geq
\frac1e-\frac{3m}{2k+1}\\
&\geq
\frac1e-\frac{3m}{2k}.
\end{aligned}
\tag{11}
\]
Thus both large-side cases give
\[
\mu(C\cap H)
\geq
\left(\frac1e-\frac{3m}{2k}\right)\mu(C)
\]
whenever \(\mathbf y^\star\in\partial H\). The boundary-reduction fact \(978e8555ec5bac42\) extends the same inequality to every closed halfspace containing \(\mathbf y^\star\).

All ranges in the statement are now explicit. For \(\frac{3e}{2}m\leq k<3em\), the displayed coefficient ranges from \(0\) at the lower endpoint to a value below \(1/(2e)\), and the preceding proof remains valid. If \(k\geq3em\), then
\[
\frac1e-\frac{3m}{2k}\geq\frac1{2e}.
\]
Finally \(n\geq1\) implies \(2^n\geq2\), so
\[
\frac1{2e}\geq\frac1{2^ne}.
\]
This is the article's Oertel coefficient. On the large-projection subclass it also implies the locked weakened coefficient \(c_0\,2^{-n}\) for every fixed \(c_0\in(0,1/e)\), but no step removes the projection hypothesis.

## External sources

Source-manuscript cross-reference: Hongyu Cheng and Amitabh Basu, "Linear Threshold for Oertel's Conjecture on the Mixed-Integer Volume," `Cheng and Basu, Linear Threshold for Oertel’s Conjecture on the Mixed-Integer Volume (source manuscript)`. Lines 123-128 state the exact Grünbaum inequality; lines 142-154 state Theorem 2.4 and its \(k\geq3e(n+d)\) consequence; lines 598-610 give boundary reduction; lines 614-662 give centroid rounding; lines 666-687 give halfspace bisection; lines 689-874 give the theorem proof, including the open complementary halfspace at lines 715-721, the two large-side cases at lines 747-833, and the Bernoulli estimates at lines 835-865; lines 878-886 restate the \(\frac1{2e}\) consequence.

Primary Grünbaum source: Branko Grünbaum, "Partitions of Mass-Distributions and of Convex Bodies by Hyperplanes," Pacific Journal of Mathematics 10(4) (1960), 1257-1261, Theorem 2 and its proof in Section 3, pp. 1259-1260, https://doi.org/10.2140/pjm.1960.10.1257, journal PDF https://msp.org/pjm/1960/10-4/pjm-v10-n4-p18-p.pdf. Exact form used: if \(D\subset\mathbb R^m\) is a convex body with centroid \(\mathfrak c(D)\), then every closed halfspace \(G\) containing \(\mathfrak c(D)\) satisfies \(V(D\cap G)\geq(m/(m+1))^mV(D)\). Applicability: \(C'\) above is a convex body in \(\mathbb R^m\), \(\mathbf y^\star=\mathfrak c(C')\), and both \(H\) and \(\bar H\) are closed and contain \(\mathbf y^\star\), so the theorem applies to both pieces. The standard normalization of \(\mathcal H_m\) on \(\mathbb R^m\) is Lebesgue volume, and \((m/(m+1))^m=(1+1/m)^{-m}\geq e^{-1}\).
