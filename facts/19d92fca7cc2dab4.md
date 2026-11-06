---
fact_id: 19d92fca7cc2dab4
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: large-box-sharp-target-and-symmetry-refinements
depends_on: ["0790372855abe672","252f1e9b01e7d3b0","48f7ad59d388c8c8","4cfd86cd551df9e7"]
verifier_run: 39a2ac4a9b5d45be
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), put \(m:=n+d\), and define \(\gamma_j:=(j/(j+1))^j\) for every positive integer \(j\). Let \(\Lambda:=\mathbb Z^n\times\mathbb R^d\). For a Borel set \(E\subseteq\mathbb R^m\), write \(E_{\mathbf z}:=\{\mathbf x\in\mathbb R^d:(\mathbf z,\mathbf x)\in E\}\) and \(\mu(E):=\sum_{\mathbf z\in\mathbb Z^n}\operatorname{vol}_d(E_{\mathbf z})\).

Let \(C\subseteq\mathbb R^m\) be a convex body, set \(S:=C\cap\Lambda\) and \(W:=\mu(C)\), and suppose that \(\mathbf a+k[-1,1]^n\subseteq\operatorname{proj}_{\mathbb R^n}(C)\) for some \(\mathbf a\in\mathbb R^n\) and \(k>0\). For \(\mathbf p\in S\), use the locked depth notation \(h_S(\mathbf p):=\inf\{\mu(C\cap H):H\text{ is a closed halfspace containing }\mathbf p\}\).

1. If \(k\ge 7m/n\), there is one point \(\mathbf p\in S\) such that \(h_S(\mathbf p)\ge\gamma_d2^{-n}W\).

2. If \(C\) is centrally symmetric and \(k>1\), there is one point \(\mathbf p\in S\) such that

   \[
   h_S(\mathbf p)\ge\frac12\left(\frac{2k-2}{2k+1}\right)^m W.
   \tag{1}
   \]

   If moreover \(k\ge\tfrac52m/n\), this same point satisfies \(h_S(\mathbf p)\ge\gamma_d2^{-n}W\).

In each assertion the point is chosen independently of the containing closed halfspace, so every such halfspace satisfies the corresponding lower bound.

## Proof

Compactness of \(C\) makes \(W\) finite, since only finitely many integer fibers meet \(C\) and each fiber has finite \(d\)-volume. We never divide by \(W\); if it is zero, each stated depth inequality is automatic at the point constructed below.

First record two elementary estimates. The inequality \(\log(1+x)<x\) for \(x>0\) gives \(\gamma_j>e^{-1}\), while the binomial inequality \((1+1/j)^j\ge 1+j/j=2\) gives \(\gamma_j\le1/2\). We will also use the exact bound
\[
\log 2
=2\int_0^{1/3}\frac{dt}{1-t^2}
>2\int_0^{1/3}(1+t^2)\,dt
=\frac{56}{81}
>\frac{15}{22}.
\tag{2}
\]
The strict integral comparison follows from \((1-t^2)^{-1}>1+t^2\) for \(0<t\le1/3\); the last comparison is \(1232>1215\).

For assertion 1, apply accepted fact \(0790372855abe672\), with its radius \(R\) identified exactly with the present \(k\), and with its \(\mathbf a,m,\Lambda,\mu\) unchanged. Its hypothesis \(R>3/2\) holds because \(k\ge7m/n>7\). It supplies one \(\mathbf p\in S\), independent of \(H\), with
\[
h_S(\mathbf p)\ge
\gamma_m\left(\frac{2k-3}{2k+1}\right)^m W.
\tag{3}
\]
The radius assumption and \(n/m<1\) imply
\[
\begin{aligned}
m\log\frac{2k+1}{2k-3}
&=m\log\left(1+\frac{2}{k-3/2}\right)\\
&<\frac{2m}{k-3/2}
\le\frac{2n}{7-3n/(2m)}
\le\frac{4n}{11}.
\end{aligned}
\tag{4}
\]
Since \(n\ge1\), (2) gives \((n+1)\log2>15(n+1)/22\ge1+4n/11\); the last difference is \(7(n-1)/22\). Consequently
\[
\gamma_m\left(\frac{2k-3}{2k+1}\right)^m
>e^{-1-4n/11}
>2^{-(n+1)}
\ge\gamma_d2^{-n}.
\tag{5}
\]
Multiplying by \(W\ge0\) and using (3) proves assertion 1, including equality in its radius hypothesis.

Now assume that \(C\) is centrally symmetric and \(k>1\). Apply accepted fact \(48f7ad59d388c8c8\), identifying its box center \(\mathbf z_0\) with \(\mathbf a\), its \(\mathbb B_\infty^n\) with \([-1,1]^n\), and its radius with the present \(k\). Write \(\epsilon:=1/(2k)\). This fact provides \(\mathbf w\in C\) and the convex body \(C':=(1-\epsilon)C+\epsilon\mathbf w\subseteq C\), whose Lebesgue centroid \(\mathbf p:=\mathfrak c(C')\) belongs to \(C'\cap\Lambda\). It also gives \(\operatorname{vol}_m(C')=(1-\epsilon)^m\operatorname{vol}_m(C)\) and a translated box of radius \(k-1/2\) in the projection of \(C'\).

If \(\mathbf c\) is the symmetry center of \(C\), reflection in \(\mathbf c\) in the centroid integral gives \(\mathfrak c(C)=2\mathbf c-\mathfrak c(C)\), hence \(\mathfrak c(C)=\mathbf c\). Affine equivariance of the centroid under the defining homothety yields \(\mathbf p=(1-\epsilon)\mathbf c+\epsilon\mathbf w\). Therefore \(2\mathbf p-C'=(1-\epsilon)(2\mathbf c-C)+\epsilon\mathbf w=C'\): the smaller body is centrally symmetric about the mixed-integer point \(\mathbf p\).

Apply the reflection bound of accepted fact \(252f1e9b01e7d3b0\) with its body replaced by \(C'\), its center point by \(\mathbf p\), and its mixed measure equal to \(\mu\). Since \(C'\cap(2\mathbf p-C')=C'\), this gives \(\mu(C'\cap H)\ge\mu(C')/2\) for every closed halfspace \(H\) containing \(\mathbf p\). In particular, this invocation does not assume that a cutting hyperplane has zero mixed mass. Indeed, the map \((\mathbf z,\mathbf x)\mapsto(2\mathbf p_I-\mathbf z,2\mathbf p_C-\mathbf x)\), where \(\mathbf p=(\mathbf p_I,\mathbf p_C)\) and \(\mathbf p_I\in\mathbb Z^n\), permutes the integer fibers and preserves their \(d\)-volumes. If \(H_0\subseteq H\) is the parallel closed halfspace with boundary through \(\mathbf p\), reflection exchanges \(H_0\) and its opposite closed halfspace. Thus
\[
2\mu(C'\cap H_0)
=\mu(C')+\mu(C'\cap\partial H_0)
\ge\mu(C').
\tag{6}
\]
The whole-space case, if included among halfspaces, is immediate. Since \(C'\subseteq C\), (6) gives \(h_S(\mathbf p)\ge\mu(C')/2\).

Use accepted fact \(4cfd86cd551df9e7\) twice, with its mixed volume \(\mathcal H_d(S_D)\) identified with \(\mu(D)\) and its continuous volume with \(\operatorname{vol}_m(D)\). For its lower bound take \(D=C'\) and radius \(k-1/2>1/2\); for its upper bound take \(D=C\) and radius \(k>1/2\). Both translated-box hypotheses were verified above. These applications and the homothety volume formula give
\[
\begin{aligned}
\mu(C')
&\ge\left(1-\frac1{2k-1}\right)^m\operatorname{vol}_m(C')\\
&=\left(\frac{2k-2}{2k}\right)^m\operatorname{vol}_m(C),\\
W&\le\left(\frac{2k+1}{2k}\right)^m\operatorname{vol}_m(C).
\end{aligned}
\tag{7}
\]
The upper bound in (7) implies \(\operatorname{vol}_m(C)\ge(2k/(2k+1))^m W\), so its lower bound implies \(\mu(C')\ge((2k-2)/(2k+1))^mW\). Together with \(h_S(\mathbf p)\ge\mu(C')/2\), this proves (1). The strict condition \(k>1\) is precisely what permits the lower comparison for \(C'\); no claim at \(k=1\) is used.

Finally put \(\theta:=n/m\in(0,1)\). If \(k\ge5/(2\theta)\), the increasing function \((2k-2)/(2k+1)\) is at least \((5-2\theta)/(5+\theta)\). The function \(\theta\mapsto\log(5-2\theta)-\log(5+\theta)+\theta\log2\) vanishes at both endpoints of \([0,1]\) and has second derivative \(-4/(5-2\theta)^2+1/(5+\theta)^2<0\) throughout that interval. It is therefore concave and lies above its zero endpoint chord. Thus \((5-2\theta)/(5+\theta)\ge2^{-\theta}\), so \(((2k-2)/(2k+1))^m\ge2^{-n}\). Equation (1) and \(\gamma_d\le1/2\) now give \(h_S(\mathbf p)\ge2^{-n-1}W\ge\gamma_d2^{-n}W\). This includes equality in the threshold \(k=\tfrac52m/n\), which is greater than \(1\). The point \(\mathbf p\) was chosen before any halfspace, and all comparisons hold for every containing closed halfspace, completing the proof.

## External sources

none
