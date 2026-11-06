---
fact_id: 9d1d5a9de0bda95d
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3en-resource-three-coordinate-consumer
depends_on: []
verifier_run: 2aa2c9e03fea40dc
target_match: null
---

## Statement

Let \(n=3\), let \(a_1,a_2,a_3>0\), let \(R\ge0\) be finite, and let \(\theta_1,\theta_2,\theta_3\le0\) be finite real numbers. Define
\[
D=\{z\in\mathbb Z_{\ge0}^3:a\cdot z\le R\},\qquad
Z=\sum_{z\in D}e^{\theta\cdot z},\qquad
p(z)=Z^{-1}e^{\theta\cdot z}\quad(z\in D).
\]
Extend \(p\) by zero outside \(D\). For \(j\in D\), let \(\tau_p(j)=\inf_{H\ni j}p(H)\), where the infimum ranges over proper closed halfspaces of \(\mathbb R^3\), and let \(M_3(p)=\sum_{j\in D}p(j)\tau_p(j)^3\), with the original root probabilities. Then, with the explicit absolute constant \(\kappa=[8(6e)^{12}]^{-1}\),
\[
M_3(p)\ge\kappa\,8^{-3}=\frac{1}{4096(6e)^{12}}.
\tag{1}
\]
All coefficients may be real and incommensurable. The conclusion includes exact resource-boundary points, zero capacity, zero penalties, and coordinates with only one feasible value. The symbols in this finite-law statement are auxiliary base-law quantities; no mixed-integer convex body or continuous dimension from the locked problem is identified with them. No accepted predecessor is used.

## Proof

Put \(t_i=-\theta_i\ge0\). Positivity of the resource coefficients makes \(D\) finite, and \(0\in D\), so \(0<Z<\infty\). Define integers \(b_i=\lfloor R/(3a_i)\rfloor\), the box \(B=\prod_{i=1}^3\{0,\ldots,b_i\}\), and its unnormalized partition function \(Z_B=\sum_{z\in B}e^{-t\cdot z}\). Since \(\sum_i a_i b_i\le R\), one has \(B\subseteq D\).

For every \(z\in D\), set \(f(z)_i=\lfloor z_i/3\rfloor\). The inequalities \(z_i\le R/a_i\) imply \(f(z)_i\le b_i\), so \(f(z)\in B\). Each point of \(B\) has at most \(3^3=27\) preimages, because each coordinate of a preimage of \(w\) is one of \(3w_i,3w_i+1,3w_i+2\). Moreover \(z_i\ge f(z)_i\) and \(t_i\ge0\), so \(e^{-t\cdot z}\le e^{-t\cdot f(z)}\). Summing over the preimages gives the exact original-denominator bound
\[
Z\le27Z_B,\qquad
Z_B=\prod_{i=1}^3 Z_i,\qquad
Z_i=\sum_{r=0}^{b_i}e^{-t_i r}.
\tag{2}
\]

For each coordinate choose an integer
\[
c_i=
\begin{cases}
b_i,&t_i=0,\\
\min\{b_i,\lfloor1/t_i\rfloor\},&0<t_i\le1,\\
0,&t_i>1,
\end{cases}
\qquad
\eta_i=\frac{(c_i+1)e^{-t_i c_i}}{Z_i}.
\tag{3}
\]
We prove \(\eta_i\ge(2e)^{-1}\) in every case. If \(t_i=0\), then \(\eta_i=1\). If \(0<t_i\le1\) and \(b_i\le\lfloor1/t_i\rfloor\), then \(c_i=b_i\), \(t_i c_i\le1\), and \(Z_i\le c_i+1\), giving \(\eta_i\ge e^{-1}\). If \(0<t_i\le1\) and \(b_i>\lfloor1/t_i\rfloor\), then \(c_i=\lfloor1/t_i\rfloor\), \(t_i c_i\le1\), and \(c_i+1>1/t_i\). From \(e^{t_i}\ge1+t_i\) one gets \(1-e^{-t_i}\ge t_i/(1+t_i)\), and hence
\[
Z_i\le\frac{1}{1-e^{-t_i}}
\le\frac{1+t_i}{t_i}
\le\frac2{t_i}<2(c_i+1).
\]
Thus \(\eta_i\ge(2e)^{-1}\) in this case as well. Finally, if \(t_i>1\), then \(c_i=0\) and \(Z_i\le(1-e^{-t_i})^{-1}\), so \(\eta_i\ge1-e^{-t_i}>1-e^{-1}>1/2>(2e)^{-1}\). This uses \(e>2\). All of these arguments also allow \(b_i=0\).

Let \(K=\prod_{i=1}^3\{0,\ldots,c_i\}\subseteq B\), put \(N=|K|=\prod_i(c_i+1)\), and let \(U\) be uniform probability on \(K\), extended by zero elsewhere. Set \(\eta=N e^{-\sum_i t_i c_i}/Z\). At any \(j\in K\), decreasing weights give
\[
p(j)\ge\frac{e^{-\sum_i t_i c_i}}{Z}=\eta U(j),\qquad
\eta=\frac{Z_B}{Z}\prod_i\eta_i
\ge\frac1{27(2e)^3}=(6e)^{-3}.
\tag{4}
\]
Outside \(K\), \(U=0\), so the pointwise comparison holds everywhere. In particular \(p(H)\ge\eta U(H)\) for every halfspace, and \(\tau_p(j)\ge\eta\tau_U(j)\) for every \(j\in K\). Therefore
\[
M_3(p)\ge\sum_{j\in K}\eta U(j)(\eta\tau_U(j))^3
=\eta^4 M_3(U).
\tag{5}
\]
The fourth power consists of one original root-probability factor and three original depth factors. There is no replacement of the original root law in the left side.

It remains to give an elementary uniform-box bound. For \(j\in K\), let \(k_j=\#\{x\in K:2j-x\in K\}\) and \(B_j=k_j/N\). Reflection about \(j\) partitions these \(k_j\) points into the singleton \(j\) and \((k_j-1)/2\) antipodal pairs. Every closed halfspace containing \(j\) contains at least one point of each pair: if both endpoints were outside, their midpoint would be outside that halfspace. Consequently \(\tau_U(j)\ge(k_j+1)/(2N)\ge B_j/2\).

For \(r\in\{0,1\}^3\), let \(N_r\) be the number of points of \(K\) in coordinatewise parity class \(r\). The sum \(\sum_{j\in K}k_j\) counts precisely the ordered pairs \((x,y)\in K^2\) with \(x+y\) coordinatewise even: such a pair has the integer midpoint \(j=(x+y)/2\), and this midpoint belongs to the box \(K\). Thus Cauchy--Schwarz gives
\[
\mathbb E_U B_j=\frac{\sum_{j\in K}k_j}{N^2}
=\frac{\sum_{r\in\{0,1\}^3}N_r^2}{N^2}
\ge\frac18.
\]
Zero parity counts and zero side lengths cause no change. Jensen's inequality for the nonnegative variable \(B_j\) now yields
\[
M_3(U)\ge\frac18\mathbb E_U B_j^3
\ge\frac18(\mathbb E_U B_j)^3
\ge\frac18\,8^{-3}.
\tag{6}
\]
This reflection comparison is used only for the auxiliary uniform box, for which every point has weight \(1/N\). Combining (4), (5), and (6) proves (1). Every resource inequality used was weak, all floors were taken on their exact real inputs, and all supports retain their boundary points. In particular the same proof covers \(R=0\), when the supports are singletons.

## External sources

none
