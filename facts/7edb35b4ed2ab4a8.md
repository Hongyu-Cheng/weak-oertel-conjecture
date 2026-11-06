---
fact_id: 7edb35b4ed2ab4a8
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: sublinear-radius-sharpness
depends_on: []
verifier_run: bcc8917190744981
target_match: null
---

## Statement

Let \(\log\) denote the natural logarithm. Fix \(\alpha>\log 2\), and define
\[
\gamma_\alpha:=\frac{\min\{\log 2,\alpha-\log 2\}}{2(\alpha+1)}
\quad\text{and}\quad
M_\alpha:=1+\frac{1}{1-\exp(-(\alpha-\log 2))}.
\]
For every integer \(k\geq 2\) and every integer \(m\geq 2(1+\alpha k)\), there exist integers \(n,d\geq 1\) with \(n+d=m\) and a convex body \(C\subseteq\mathbb{R}^{n+d}\) such that, with
\[
\mathbb{B}_\infty^n:=\{\mathbf{u}\in\mathbb{R}^n:\|\mathbf{u}\|_\infty\leq 1\},
\qquad
K:=\operatorname{proj}_{\mathbb{R}^n}(C),
\qquad
S:=C\cap(\mathbb{Z}^n\times\mathbb{R}^d),
\]
the set \(K\) contains a translate of \(k\mathbb{B}_\infty^n\), and
\[
\sup_{\mathbf{y}\in S}\frac{h_S(\mathbf{y})}{\mathcal{H}_d(S)}
\leq M_\alpha\exp\!\left(-\gamma_\alpha\frac{m}{k}\right).
\]
Here, for measurable \(A\subseteq\mathbb{Z}^n\times\mathbb{R}^d\),
\[
\mathcal{H}_d(A):=
\sum_{\mathbf{z}\in\mathbb{Z}^n}
\mathcal{H}_d\!\left(A\cap(\{\mathbf{z}\}\times\mathbb{R}^d)\right),
\]
and
\[
h_S(\mathbf{y}):=
\inf\{\mathcal{H}_d(S\cap H):H\subseteq\mathbb{R}^{n+d}
\text{ is a closed halfspace and }\mathbf{y}\in H\}.
\]

## Proof

Fix \(\alpha,k,m\) as in the statement and set
\[
n:=\left\lfloor\frac{m}{1+\alpha k}\right\rfloor,
\qquad d:=m-n.
\]
Since \(m/(1+\alpha k)\geq 2\), one has \(n\geq 2\). Also \(n<m\), so \(d\geq 1\), and \((1+\alpha k)n\leq m\) gives
\[
d=m-n\geq \alpha k n.
\]
Thus \(n,d\) are positive integers and \(n+d=m\).

Let
\[
\mathbf{c}:=\left(k+\frac12\right)(1,\ldots,1),
\qquad
K:=\mathbf{c}+k\mathbb{B}_\infty^n
=\left[\frac12,2k+\frac12\right]^n,
\]
and, for \(\mathbf{z}\in K\), let
\[
t(\mathbf{z}):=1-\frac{\|\mathbf{z}-\mathbf{c}\|_\infty}{k}.
\]
Define
\[
C:=\{(\mathbf{z},\mathbf{x})\in\mathbb{R}^n\times\mathbb{R}^d:
\mathbf{z}\in K,\ \|\mathbf{x}\|_2\leq t(\mathbf{z})\}.
\]
Equivalently,
\[
C=\left\{(\mathbf{z},\mathbf{x}):
\frac{\|\mathbf{z}-\mathbf{c}\|_\infty}{k}+\|\mathbf{x}\|_2\leq 1\right\}.
\]
The function on the left is convex, so \(C\) is convex. It is closed and bounded, hence compact. The defining inequality is strict at \((\mathbf{c},\mathbf{0})\), so continuity gives a neighborhood of \((\mathbf{c},\mathbf{0})\) contained in \(C\); hence \(C\) has nonempty interior and is a convex body. For every \(\mathbf{z}\in K\), the point \((\mathbf{z},\mathbf{0})\) belongs to \(C\), while every point of \(C\) has its first component in \(K\). Therefore \(\operatorname{proj}_{\mathbb{R}^n}(C)=K=\mathbf{c}+k\mathbb{B}_\infty^n\).

Let \(v_d\) be the \(d\)-dimensional volume of the Euclidean unit ball in \(\mathbb{R}^d\). Since
\[
K\cap\mathbb{Z}^n=\{1,\ldots,2k\}^n,
\]
the fiber of \(S\) over any \(\mathbf{z}\in K\cap\mathbb{Z}^n\) is the Euclidean \(d\)-ball of radius \(t(\mathbf{z})\), and hence has \(\mathcal{H}_d\)-measure \(v_dt(\mathbf{z})^d\). Consequently,
\[
\mathcal{H}_d(S)
=v_d\sum_{\mathbf{z}\in K\cap\mathbb{Z}^n}t(\mathbf{z})^d.
\]
Set
\[
V_0:=\{k,k+1\}^n,\qquad
a:=1-\frac{1}{2k},\qquad
T:=\sum_{\mathbf{z}\in(K\cap\mathbb{Z}^n)\setminus V_0}t(\mathbf{z})^d.
\]
For an integer vector \(\mathbf{z}\), every coordinate of \(\mathbf{z}-\mathbf{c}\) is a half-integer. Thus the minimum possible value of \(\|\mathbf{z}-\mathbf{c}\|_\infty\) is \(1/2\), attained exactly on \(V_0\). Hence \(\#V_0=2^n\), \(t(\mathbf{z})=a\) on \(V_0\), and
\[
\mathcal{H}_d(S)=v_d(2^na^d+T)>0.
\]

We next give, for every \(\mathbf{y}\in S\), a closed halfspace containing \(\mathbf{y}\) whose mixed-integer volume is small. Write \(\mathbf{y}=(\mathbf{z},\mathbf{x})\).

First suppose \(\mathbf{z}=\mathbf{v}\in V_0\). Define \(\boldsymbol{\sigma}(\mathbf{v})\in\{-1,1\}^n\) by
\[
\sigma_i(\mathbf{v})=2(v_i-k)-1
\]
and take
\[
H_{\mathbf{v}}:=
\{(\mathbf{u},\mathbf{w})\in\mathbb{R}^n\times\mathbb{R}^d:
\boldsymbol{\sigma}(\mathbf{v})^\top\mathbf{u}
\geq\boldsymbol{\sigma}(\mathbf{v})^\top\mathbf{v}\}.
\]
This is a closed halfspace containing \(\mathbf{y}\). In coordinate \(i\), the sign is \(1\) when \(v_i=k+1\) and \(-1\) when \(v_i=k\). Therefore \(\mathbf{v}\) is the unique maximizer of \(\boldsymbol{\sigma}(\mathbf{v})^\top\mathbf{u}\) over \(\mathbf{u}\in V_0\). It follows that \(H_{\mathbf{v}}\) meets \(V_0\times\mathbb{R}^d\) in exactly the fiber over \(\mathbf{v}\). All other fibers together have normalized weight \(T\), so
\[
\mathcal{H}_d(S\cap H_{\mathbf{v}})\leq v_d(a^d+T).
\]

Now suppose \(\mathbf{z}\notin V_0\). Some coordinate satisfies either \(z_i\leq k-1\) or \(z_i\geq k+2\). In the first case use the closed halfspace
\[
H:=\{(\mathbf{u},\mathbf{w}):u_i\leq k-1\},
\]
and in the second use
\[
H:=\{(\mathbf{u},\mathbf{w}):u_i\geq k+2\}.
\]
The chosen halfspace contains \(\mathbf{y}\) and is disjoint from \(V_0\times\mathbb{R}^d\), so \(\mathcal{H}_d(S\cap H)\leq v_dT\). In both cases, the definition of depth now gives
\[
h_S(\mathbf{y})\leq v_d(a^d+T)
\quad\text{for every }\mathbf{y}\in S.
\]
Therefore,
\[
\sup_{\mathbf{y}\in S}\frac{h_S(\mathbf{y})}{\mathcal{H}_d(S)}
\leq\frac{a^d+T}{2^na^d+T}
\leq 2^{-n}+\frac{T}{2^na^d}.
\]

It remains to bound the noncentral fibers. For \(j=0,\ldots,k-1\), define
\[
V_j:=\left\{\mathbf{z}\in K\cap\mathbb{Z}^n:
\|\mathbf{z}-\mathbf{c}\|_\infty=\frac{2j+1}{2}\right\}.
\]
These shells partition \(K\cap\mathbb{Z}^n\), and the noncentral vectors are the union of \(V_j\) for \(1\leq j\leq k-1\). The integer vectors satisfying
\(\|\mathbf{z}-\mathbf{c}\|_\infty\leq(2j+1)/2\) have each coordinate in
\(\{k-j,\ldots,k+j+1\}\), a set of \(2j+2\) integers. Hence
\[
\#V_j\leq(2j+2)^n
\quad\text{and}\quad
\frac{\#V_j}{2^n}\leq(j+1)^n.
\]
For \(\mathbf{z}\in V_j\),
\[
\frac{t(\mathbf{z})}{a}
=\frac{2k-2j-1}{2k-1}
=1-\frac{2j}{2k-1}.
\]
For \(1\leq j\leq k-1\), the last fraction lies strictly between \(0\) and \(1\). Using \(\log(1-u)\leq-u\) for \(0<u<1\), followed by \(d\geq\alpha kn\), gives
\[
\left(\frac{t(\mathbf{z})}{a}\right)^d
\leq\exp\!\left(-\frac{2jd}{2k-1}\right)
\leq\exp(-\alpha jn).
\]
It follows that
\[
\frac{T}{2^na^d}
\leq\sum_{j=1}^{k-1}(j+1)^n\exp(-\alpha jn).
\]
The elementary inequality \(j+1\leq 2^j\) for \(j\geq 1\) and
\(\beta:=\alpha-\log 2>0\) imply
\[
\frac{T}{2^na^d}
\leq\sum_{j=1}^{\infty}\exp(-\beta jn)
=\frac{\exp(-\beta n)}{1-\exp(-\beta n)}
\leq\frac{\exp(-\beta n)}{1-\exp(-\beta)}.
\]
Thus
\[
\sup_{\mathbf{y}\in S}\frac{h_S(\mathbf{y})}{\mathcal{H}_d(S)}
\leq 2^{-n}
+\frac{\exp(-(\alpha-\log 2)n)}
{1-\exp(-(\alpha-\log 2))}.
\]
Let \(\lambda:=\min\{\log 2,\alpha-\log 2\}\). By the definition of \(M_\alpha\), the last display is at most \(M_\alpha\exp(-\lambda n)\).

Finally, \(x:=m/(1+\alpha k)\geq 2\), so
\[
n=\lfloor x\rfloor\geq x-1\geq\frac{x}{2}
=\frac{m}{2(1+\alpha k)}
\geq\frac{m}{2(\alpha+1)k},
\]
where the last inequality uses \(1+\alpha k\leq(\alpha+1)k\) for \(k\geq 1\). Hence
\[
\sup_{\mathbf{y}\in S}\frac{h_S(\mathbf{y})}{\mathcal{H}_d(S)}
\leq M_\alpha
\exp\!\left(-\frac{\lambda}{2(\alpha+1)}\frac{m}{k}\right)
=M_\alpha\exp\!\left(-\gamma_\alpha\frac{m}{k}\right),
\]
as claimed.

This theorem does not disprove the locked assertion that some point always has depth at least \(c_0\,2^{-n}\mathcal{H}_d(S)\) for an absolute \(c_0\in(0,1/e)\). The construction-specific estimate proved above is
\[
\sup_{\mathbf{y}\in S}\frac{h_S(\mathbf{y})}{\mathcal{H}_d(S)}
\leq 2^{-n}
+\frac{\exp(-(\alpha-\log 2)n)}
{1-\exp(-(\alpha-\log 2))},
\]
whose right-hand side is strictly larger than \(2^{-n}\), and therefore larger than \(c_0 2^{-n}\). An upper bound at that level cannot contradict the locked lower target. The result rules out only a positive lower fraction independent of \(n\), not a lower fraction on the \(2^{-n}\) scale.

## External sources

none
