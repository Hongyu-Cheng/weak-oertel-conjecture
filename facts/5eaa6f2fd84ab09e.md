---
fact_id: 5eaa6f2fd84ab09e
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct21-common-spatial-coupled-moment
depends_on: ["21a3de2e8e8e3fd6","57ab2aa6c8ea80e0"]
verifier_run: c1a70c07600744fd
target_match: null
---

## Statement

For every fixed real \(a>0\) and \(D\ge0\), there exists \(\kappa(a,D)>0\) with the following property. Let \(k\ge1\), \(b\ge2\), and \(T\ge0\) be integers, with \(b\ge a\sqrt{k}\), and let \(0<\rho\le1\) and \(\beta\ge0\) be real. For every \(i\in[k]=\lbrace1,\ldots,k\rbrace\), let \(B_i,C_{4,i}\) be integers satisfying \(b\le B_i\le2b\) and \(C_{4,i}\ge2B_i-1\). Let \(\Phi:\mathbb Z_{\ge0}\to\mathbb Z_{\ge0}\) be nondecreasing with \(\Phi(0)=0\). Define

$$
\begin{aligned}
g_i(0)&=0,&g_i(1)&=1,&g_i(2)&=B_i,&g_i(3)&=C_{4,i},\\
r(\mathbf x)&=\sum_{i=1}^k\max(x_i-1,0),&
\Gamma_\Phi(\mathbf x)&=\sum_{i=1}^k g_i(x_i)+\Phi(r(\mathbf x)),\\
A_4&=\lbrace(\mathbf x,t):\mathbf x\in\lbrace0,1,2,3\rbrace^k,\ t\in\mathbb Z,\ \Gamma_\Phi(\mathbf x)\le t\le T\rbrace,\\
f_E&=\begin{cases}\displaystyle\sum_{t=E}^T e^{-\beta t},&0\le E\le T,\\0,&E>T,\end{cases}\\
Z_{4,\Phi,\rho}&=\sum_{\mathbf x\in\lbrace0,1,2,3\rbrace^k}\rho^{\sum_i x_i}f_{\Gamma_\Phi(\mathbf x)},&
Z_{3,\Phi,\rho}&=\sum_{\mathbf x\in\lbrace0,1,2\rbrace^k}\rho^{\sum_i x_i}f_{\Gamma_\Phi(\mathbf x)},\\
p_{(\mathbf x,t)}&=\frac{\rho^{\sum_i x_i}e^{-\beta t}}{Z_{4,\Phi,\rho}}\qquad((\mathbf x,t)\in A_4).
\end{aligned}
\tag{1}
$$

Here \(f_E\) is used only for nonnegative integer \(E\). Every original spatial vector has multiplicity one, and every integer height in its displayed closed interval is retained. For \(\mathbf z\in A_4\), put

$$
\tau_p(\mathbf z)=\inf_{H\ni\mathbf z}\sum_{\mathbf v\in A_4\cap H}p_{\mathbf v},
\qquad
M_3(p)=\sum_{\mathbf z\in A_4}p_{\mathbf z}\tau_p(\mathbf z)^3,
\tag{2}
$$

where the infimum ranges over all closed affine halfspaces \(H\) of \(\mathbb R^{k+1}\) with nonzero normal. If

$$
T\le\frac{k\rho}{1+\rho}+Db[1+\log^2(k+1)],
\tag{3}
$$

then

$$
M_3(p)\ge\kappa(a,D)\,8^{-(k+1)}.
\tag{4}
$$

The objects \(k,b,T,\beta,B_i,C_{4,i},g_i,r,\Gamma_\Phi,f_E,Z_{4,\Phi,\rho},Z_{3,\Phi,\rho}\) have exactly the meanings of their namesakes in accepted fact 21a3de2e8e8e3fd6. Its high-coordinate count remains \(Q(\mathbf x)=|\lbrace i:x_i\in\lbrace2,3\rbrace\rbrace|\), and its scalar \(p_\rho=\rho/(1+\rho)\) is distinct from the law \(p\) in (1). Thus \(\rho\) is spatial activity and \(\beta\) is height tilt. The locked problem's \(n,d,C,\Lambda,S,c_0\) and any preexisting notation \(N\) retain their meanings.

## Proof

All energies are nonnegative integers and \(\Gamma_\Phi(\mathbf0)=0\). Thus \(A_4\) is finite, contains \((\mathbf0,0)\), and has positive weights; both normalizers and \(f_0\) are positive. Also \(\Gamma_\Phi\) is coordinatewise nondecreasing: each \(g_i\) is nondecreasing because \(B_i\ge2\) and \(C_{4,i}\ge2B_i-1\ge B_i\), and both \(r\) and \(\Phi\) are nondecreasing.

We first prove the restriction transfer using the same ambient halfspaces. For any nonempty \(A'\subseteq A_4\), define

$$
Z'=\sum_{(\mathbf x,t)\in A'}\rho^{\sum_i x_i}e^{-\beta t},
\qquad
q_{(\mathbf x,t)}=\frac{\rho^{\sum_i x_i}e^{-\beta t}}{Z'},
\qquad
\theta=\frac{Z'}{Z_{4,\Phi,\rho}}.
\tag{5}
$$

Define \(\tau_q,M_3(q)\) by (2) on \(A'\), with the identical family of closed affine halfspaces of \(\mathbb R^{k+1}\). For every \(\mathbf z\in A'\) and every such \(H\ni\mathbf z\),

$$
\sum_{\mathbf v\in A_4\cap H}p_{\mathbf v}
\ge\sum_{\mathbf v\in A'\cap H}p_{\mathbf v}
=\theta\sum_{\mathbf v\in A'\cap H}q_{\mathbf v}
\ge\theta\tau_q(\mathbf z).
\tag{6}
$$

Taking the infimum gives \(\tau_p(\mathbf z)\ge\theta\tau_q(\mathbf z)\). Since \(p_{\mathbf z}=\theta q_{\mathbf z}\) on \(A'\), it follows that

$$
M_3(p)
\ge\sum_{\mathbf z\in A'}\theta q_{\mathbf z}
                        [\theta\tau_q(\mathbf z)]^3
=\theta^4M_3(q).
\tag{7}
$$

One normalizer factor comes from sampling and three come from the cubic depth. This proof also applies to restrictions in proper affine subspaces, since the ambient halfspaces are unchanged.

Take first

$$
A_3=\lbrace(\mathbf x,t)\in A_4:\mathbf x\in\lbrace0,1,2\rbrace^k\rbrace,
\qquad
q^{(3)}_{(\mathbf x,t)}
=\frac{\rho^{\sum_i x_i}e^{-\beta t}}{Z_{3,\Phi,\rho}}.
\tag{8}
$$

In accepted fact 57ab2aa6c8ea80e0, set its \(\Gamma\) equal to \(\Gamma_\Phi\) restricted to the ternary cube, keep its \(k,T,\beta\), and set its \(\alpha_i=-\log\rho\ge0\). Its \(A_T,Z,p,\tau_p,M_3(p)\) then equal the present \(A_3,Z_{3,\Phi,\rho},q^{(3)},\tau_{q^{(3)}},M_3(q^{(3)})\), respectively. The verified monotonicity and value at zero establish its energy hypotheses. Its halfspaces are exactly those used here. Therefore that fact and (7) imply

$$
M_3(q^{(3)})\ge\frac1{2939328}\,8^{-(k+1)},
\qquad
M_3(p)\ge\frac1{2939328}
\left(\frac{Z_{3,\Phi,\rho}}{Z_{4,\Phi,\rho}}\right)^4
8^{-(k+1)}.
\tag{9}
$$

Fix \(a,D\). The final uniform conclusion of accepted fact 21a3de2e8e8e3fd6 supplies an integer \(K=K(a,D)\ge2\) such that every model (1)-(3) with \(k\ge K\) satisfies

$$
Z_{4,\Phi,\rho}\le\left(e+\frac12\right)Z_{3,\Phi,\rho}.
\tag{10}
$$

Choose any integer at least two and at least its eventual threshold. That parent states that the threshold depends only on \(a,D\), uniformly in all the other parameters here. Its normalizers and cap are exactly (1) and (3). Thus, for \(k\ge K\), (9) gives

$$
M_3(p)\ge\frac1{2939328}\left(e+\frac12\right)^{-4}8^{-(k+1)}.
\tag{11}
$$

To cover smaller dimensions uniformly in the remaining parameters, define on the ternary cube the artificial energy

$$
\widehat\Gamma(\mathbf x)=(T+1)\sum_{i=1}^k x_i.
\tag{12}
$$

It is nonnegative, integer-valued and coordinatewise nondecreasing, and vanishes at zero. Every nonzero ternary vector has energy at least \(T+1\), so its capped support is exactly

$$
A_0=\lbrace(\mathbf0,t):t\in\mathbb Z,\ 0\le t\le T\rbrace.
\tag{13}
$$

Apply accepted fact 57ab2aa6c8ea80e0 again, mapping its \(\Gamma,A_T,Z,p\) to \(\widehat\Gamma,A_0,f_0,q^{(0)}\), where

$$
q^{(0)}_{(\mathbf0,t)}=e^{-\beta t}/f_0.
\tag{14}
$$

Keep its \(k,T,\beta\) and \(\alpha_i=-\log\rho\). The spatial weight on this support is \(\rho^0=1\). Its depth and moment become \(\tau_{q^{(0)}}\) and \(M_3(q^{(0)})\), with the same ambient halfspaces. It follows that

$$
M_3(q^{(0)})\ge\frac1{2939328}\,8^{-(k+1)}.
\tag{15}
$$

Because \(\Gamma_\Phi(\mathbf0)=0\), \(A_0\) is a restriction of the original full support and \(q^{(0)}\) is its normalized restriction. For every full spatial vector, \(\rho^{\sum_i x_i}\le1\) and \(f_{\Gamma_\Phi(\mathbf x)}\le f_0\). There are \(4^k\) such vectors, so

$$
Z_{4,\Phi,\rho}\le4^k f_0.
\tag{16}
$$

Applying (7) with \(A'=A_0\) and \(\theta=f_0/Z_{4,\Phi,\rho}\ge4^{-k}\) proves, for every \(k\ge1\),

$$
M_3(p)\ge\frac1{2939328}\,4^{-4k}8^{-(k+1)}.
\tag{17}
$$

For \(1\le k<K\), its coefficient is at least \((1/2939328)4^{-4(K-1)}\). Consequently the single positive choice

$$
\kappa(a,D)=\frac1{2939328}
\min\left\lbrace
\left(e+\frac12\right)^{-4},\
4^{-4(K(a,D)-1)}
\right\rbrace
\tag{18}
$$

gives (4) for every dimension by (11) and (17).

At \(\rho=1\), the ternary applications have \(\alpha_i=0\), as permitted. At \(\beta=0\), every comparison remains valid and \(f_0=T+1\). At \(T=0\), every nonzero spatial vector has positive original energy, so \(A_4=\lbrace(\mathbf0,0)\rbrace\) and \(M_3(p)=1\); the proof also includes this case. All energy, height, and halfspace inequalities are weak, so cost equalities and boundary atoms remain included.

## External sources

None.
