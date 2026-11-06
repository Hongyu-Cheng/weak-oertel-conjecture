---
fact_id: 284ed29f0cbbaaa9
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3dp-convex-radius-coordinate-halving-moment-test
depends_on: []
verifier_run: 5e6f569d0c754efc
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(R>0\), and let \(\psi:[0,\infty)\to[0,\infty)\) be finite, convex, and nondecreasing, with \(\psi(0)=0\) and \(\psi(1)>0\). Define \(V_i(z)=\psi(|z_i|)\) for \(z\in\mathbb Z^n\), and set

\[
\begin{aligned}
D_+&=\left\{z\in\mathbb Z^n:\sum_{i=1}^nV_i(z)<R\right\},
\qquad a_z=R-\sum_{i=1}^nV_i(z),\\
w_z&=(2a_z)^d,
\qquad W=\sum_{z\in D_+}w_z,
\qquad p_z=\frac{w_z}{W}.
\end{aligned}
\]

Here \(a_z\) is the radius and \(p\) is the original volume law. For every real \(k\), define \(\mathcal Z_k=\sum_{z\in D_+}a_z^k\) and \(q_z^{(k)}=a_z^k/\mathcal Z_k\); in particular \(p=q^{(d)}\). These are well-defined finite laws. The lattice random vector remains denoted by \(Z\). Write \(V(Z)=(V_1(Z),\ldots,V_n(Z))\) and \(L=\sum_iV_i(Z)\). For \(\psi(t)=t\), the energy vector \(V(Z)\) is exactly \(|Z|\), the total energy \(L\) is exactly \(\sum_i|Z_i|\), and \(D_+,a_z,w_z,W,p_z,\mathcal Z_k,q^{(k)}\) reduce to their linear radial normalizations.

For every coordinate \(i\) and every real moment order \(m\) with \(0<m<d\),

\[
\mathbb E_p\left[\frac{V_i(Z)^m}{a_Z^m}\right]
\le 4(2m)^m\frac{(d-m)^{d-m}}{d^d}.
\tag{1}
\]

For \(d\ge 2m\), the right side of (1) is at most \(4m^m/d^m\). In particular, uniformly over all \(n,R,\psi\),

\[
\begin{aligned}
\mathbb E_p\left[\frac{V_i(Z)^2}{a_Z^2}\right]&\le\frac{16}{d^2}
&&\text{if }d\ge4,\\
\mathbb E_p\left[\frac{V_i(Z)^4}{a_Z^4}\right]&\le\frac{1024}{d^4}
&&\text{if }d\ge8.
\end{aligned}
\tag{2}
\]

For every real \(k\ge0\) and every distinct pair \(i,j\), \(\operatorname{Cov}_{q^{(k)}}(V_i(Z),V_j(Z))\le0\). If “every \(a^k\) law” includes negative powers, that assertion is false: for \(n=2\), \(R=5/2\), \(\psi(t)=t^2\), and \(k=-1\), the covariance is \(80/6889>0\). No negative-association assertion or centered fourth-moment bound for \(L\) is included.

## Proof

Convexity and \(\psi(0)=0\) imply \(\psi(t)\ge t\psi(1)\) for every \(t\ge1\): apply convexity to \(1=(1/t)t+(1-1/t)0\). Thus every \(z\in D_+\) has \(|z_i|<R/\psi(1)\) whenever \(z_i\ne0\). The support is finite, contains \(0_n\), and has \(a_z>0\). Every partition function in the statement is therefore finite and positive, including at negative powers. Cancelling the common factor \(2^d\) gives \(p_z=a_z^d/\mathcal Z_d\).

Fix a coordinate \(i\). Define \(H_i:\mathbb Z^n\to\mathbb Z^n\) by leaving all other coordinates unchanged and putting \((H_i z)_i=0\) if \(z_i=0\), and \((H_i z)_i=\operatorname{sgn}(z_i)\lfloor |z_i|/2\rfloor\) otherwise. Nondecreasingness and convexity give

\[
V_i(H_i z)
\le \psi(|z_i|/2)
\le \tfrac12\psi(|z_i|)
=\tfrac12V_i(z),
\qquad
a_{H_i z}\ge a_z+\tfrac12V_i(z).
\tag{3}
\]

This also holds at \(z_i=0\). Consequently \(H_i(D_+)\subseteq D_+\). An image with \(i\)-th coordinate zero has at most the three possible preimage coordinates \(-1,0,1\). An image with \(i\)-th coordinate \(h>0\) has only the possible preimages \(2h,2h+1\), and one with coordinate \(h<0\) has only \(2h,2h-1\). All other coordinates are fixed. In particular, every image has at most four preimages, also after restriction to \(D_+\).

For \(z\in D_+\), put \(r=V_i(z)/a_z\ge0\). By (3),
\(a_z^d r^m\le a_{H_i z}^d r^m/(1+r/2)^d\). For \(0<m<d\), the function \(f(r)=r^m/(1+r/2)^d\) tends to zero at both endpoints \(0\) and \(+\infty\). On \(r>0\), its logarithmic derivative is \(m/r-d/(2+r)\), which vanishes exactly at \(r=2m/(d-m)\), is positive before that point, and negative after it. Its exact maximum is therefore
\(\sup_{r\ge0}f(r)=(2m)^m(d-m)^{d-m}/d^d\). Using the bounded multiplicity and the original weights gives

\[
\begin{aligned}
\sum_{z\in D_+}a_z^d\frac{V_i(z)^m}{a_z^m}
&\le (2m)^m\frac{(d-m)^{d-m}}{d^d}
       \sum_{z\in D_+}a_{H_i z}^d\\
&\le 4(2m)^m\frac{(d-m)^{d-m}}{d^d}
       \sum_{u\in D_+}a_u^d.
\end{aligned}
\]

Divide by \(\mathcal Z_d\) to obtain (1). There is no change to a root-weight law or to any other probability measure in this comparison.

For completeness, for fixed \(m>0\) and real \(d>m\), the logarithmic derivative in \(d\) of \(g(d)=(1-m/d)^{d-m}\) is \(\log(1-m/d)+m/d<0\). The inequality follows, for example, by integrating \(1/(1-t)>1\) from \(0\) to \(m/d\). Thus if \(d\ge2m\), then \(g(d)\le g(2m)=2^{-m}\). Since the right side of (1) is \(4(2m)^m d^{-m}g(d)\), it is at most \(4m^m/d^m\). Substituting \(m=2\) and \(m=4\) gives (2).

Now fix \(k\ge0\). The pairwise covariance assertion is vacuous for \(n=1\), so suppose \(n\ge2\). Fix distinct \(i,j\). For any value \(t\) in the support of \(V_i(Z)\) under \(q^{(k)}\), the conditional law of the remaining signed coordinates \(z_{-i}\) is proportional to \((R-t-s)^k\) on \(s<R-t\), where \(s=\sum_{\ell\ne i}\psi(|z_\ell|)\). The number of signed choices of the removed coordinate having energy \(t\) is constant in \(z_{-i}\) and cancels on conditioning.

Let \(t_1<t_2\) be two such values. On the remaining-coordinate support for \(t_1\), when \(k>0\), define
\(\rho(s)=((R-t_2-s)_+/(R-t_1-s))^k\), where \((u)_+=\max\{u,0\}\). When \(k=0\), instead define \(\rho(s)=\mathbf 1_{\{s<R-t_2\}}\). In either case \(\rho\) is nonnegative and nonincreasing in \(s\). Indeed, on \(s<R-t_2\), the ratio before taking the positive power is \(1-(t_2-t_1)/(R-t_1-s)\), which decreases as \(s\) increases; beyond that interval \(\rho\) is zero. Its conditional expectation at \(t_1\) is positive, since the zero remaining-coordinate vector is permitted at \(t_2<R\).

The conditional law at \(t_2\) is exactly the conditional law at \(t_1\) tilted by \(\rho(s)\) and normalized. For any finite random variable \(Y\) and an independent copy \(Y'\), the identity
\(2\operatorname{Cov}(Y,\rho(Y))=\mathbb E[(Y-Y')(\rho(Y)-\rho(Y'))]\) shows that this covariance is nonpositive when \(\rho\) is nonincreasing. Therefore

\[
\mathbb E[s\mid V_i=t_2]-\mathbb E[s\mid V_i=t_1]
=\frac{\operatorname{Cov}(s,\rho(s)\mid V_i=t_1)}
       {\mathbb E[\rho(s)\mid V_i=t_1]}
\le0.
\]

The conditional remaining coordinates are exchangeable. Hence
\(\mathbb E[V_j\mid V_i=t]=\mathbb E[s\mid V_i=t]/(n-1)\) is nonincreasing in \(t\). Conditional expectation and the same independent-copy covariance identity now give
\(\operatorname{Cov}_{q^{(k)}}(V_i,V_j)=\operatorname{Cov}_{q^{(k)}}(V_i,\mathbb E[V_j\mid V_i])\le0\). This proves the assertion for every nonnegative real \(k\) without a claim about higher joint dependence.

Finally, in the stated negative-power example, \(D_+=\{0,-1,1\}^2\), since \(\psi(2)=4>5/2\), whereas the total energy of any two allowed coordinates is at most \(2<5/2\). Under \(q^{(-1)}\), the total unnormalized weights for energy pairs \((0,0),(1,0),(0,1),(1,1)\) are respectively \(2/5,4/3,4/3,8\); the factors two and four count all signs. Their sum is \(\mathcal Z_{-1}=166/15\). Thus \(\mathbb E[V_1]=\mathbb E[V_2]=70/83\) and \(\mathbb E[V_1V_2]=60/83\). The covariance is \(60/83-(70/83)^2=80/6889>0\), verifying the claimed negative-power failure.

## External sources

none
