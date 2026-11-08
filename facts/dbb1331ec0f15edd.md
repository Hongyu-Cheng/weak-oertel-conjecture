---
fact_id: dbb1331ec0f15edd
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-physical-retained-mass-right-derivative
depends_on: ["efa4558174ce60cf"]
verifier_run: eaeaeb9807423fbb
target_match: null
---

## Source

- [cb7ea417552f0084](../candidates/cb7ea417552f0084.json), Introduction (1)–(2), §§1–4, (3)–(16).

## Statement

Let $d\ge1$, let $K\subset\mathbb R^d$ be a compact convex body with nonempty interior, and let $y,o\in\operatorname{int}K$. Let $K_\varepsilon$ be nested compact convex bodies for $\varepsilon\ge0$ with $K_0=K$. Suppose that for some $C\ge0$ and all sufficiently small $\varepsilon>0$,
$$
o+(1-C\varepsilon)(K-o)\subseteq K_\varepsilon\subseteq K.
$$
For $x\in\partial K$, write the radial endpoint of $K_\varepsilon$ on the ray from $o$ through $x$ as $o+(1-t_\varepsilon(x))(x-o)$. At a regular boundary point $x$, let $n(x)$ be its unique outward unit normal and set $dS=d\mathcal H^{d-1}$ on $\partial K$. Assume that for a bounded measurable $v$,
$$
\frac{t_\varepsilon(x)}{\varepsilon}\longrightarrow
\frac{v(x)}{n(x)\cdot(x-o)}
\qquad\text{for $dS$ almost every }x.
$$
Then $v\ge0$ almost everywhere. Take $y_\varepsilon=y+\varepsilon w+o(\varepsilon)$ for a fixed $w\in\mathbb R^d$. For a body $L$ and $q\in\operatorname{int}L$, let
$$
T_L(q)=\max\left\{\int_L f(x)\,dx:\ 0\le f\le1,\ f\text{ measurable},\
                       \int_L(x-q)f(x)\,dx=0\right\}.
$$
Set $T=T_K(y)$ and let $U$ be the compact nonempty set of minimizers of $G_0(u)=\int_K[1+u\cdot(x-y)]_+\,dx$, where $[a]_+=\max(a,0)$. For all sufficiently small $\varepsilon$, $y_\varepsilon\in\operatorname{int}K_\varepsilon$. The following right derivative exists, and the minimum is attained:
$$
\left.\frac{d}{d\varepsilon}\right|_{0+}T_{K_\varepsilon}(y_\varepsilon)
=\min_{u\in U}\left\{
-\int_{\partial K}[1+u\cdot(x-y)]_+v(x)\,dS(x)-T\,u\cdot w
\right\}. \tag{1}
$$
When $y$ differs from the centroid $g_K$, $U$ is a singleton. When $y=g_K$, put $V=|K|$, $D=\int_{\partial K}v\,dS$ and $B=\int_{\partial K}(x-y)v(x)\,dS(x)$. For the Minkowski gauge $p_{K-y}(z)=\inf\{t\ge0:z\in t(K-y)\}$, (1) becomes
$$
\left.\frac{d}{d\varepsilon}\right|_{0+}T_{K_\varepsilon}(y_\varepsilon)
=-D-p_{K-y}(-B-Vw).
\tag{2}
$$
The ordinary centroid satisfies $g_{K_\varepsilon}=y-\varepsilon B/V+o(\varepsilon)$. The derivative in (2) equals $-D$ exactly when $w=-B/V$, and is strictly smaller otherwise. In dimension $1$, $dS$ is counting measure on the two endpoints. The formula allows hinge hyperplanes incident with vertices, edges, and supporting facets; it does not require a differentiable cutting section.

## Proof

The retained-cap part of accepted fact efa4558174ce60cf applies to every compact full-dimensional convex body and interior mark. It gives the attained hinge minimum and, for each minimizing $u$, the optimizing indicator of the cap $D_u(q)=L\cap\{1+u\cdot(x-q)\ge0\}$, of volume $T_L(q)$. That fact's proof specializes 2c093df4eb8158a9 to one packet $(t,q)$: tests with affine value $\ell(q)\le0$ are automatic and the others normalize to $\ell(q)=1$. The retained-cap proof also gives uniqueness of the normalized proper hinge off the centroid. No energy comparison is needed.

Write $H(x)=n(x)\cdot(x-o)$, which is at least the radius of an inner ball centered at $o$, and note $0\le t_\varepsilon\le C\varepsilon$. In particular $v\ge0$ almost everywhere. For a continuous weight $f$, the radial area formula gives
$$
\int_{K\setminus K_\varepsilon}f(z)\,dz
=\int_{\partial K}\int_0^{t_\varepsilon(x)}
   f(o+(1-s)(x-o))H(x)(1-s)^{d-1}\,ds\,dS(x).
\tag{3}
$$
Indeed a convex body's boundary is locally a Lipschitz graph and has a tangent hyperplane almost everywhere. The $d-1$ tangential derivatives of the radial parametrization are scaled by $1-s$; the remaining derivative is $-(x-o)$, with normal component of magnitude $H(x)$. The area formula gives (3) since distinct old endpoints index distinct rays and the thin layer has $s<1$. In dimension one this is the usual substitution on each endpoint interval. The uniform thickness and boundedness of $H$ give $Ht_\varepsilon/\varepsilon\to v$ in $L^1(dS)$ by dominated convergence.

On every compact $u$-set the hinges $[1+u\cdot(x-y_\varepsilon)]_+$ are uniformly bounded and uniformly Lipschitz in $x$. In (3) replacing $o+(1-s)(x-o)$ by $x$, $y_\varepsilon$ by $y$, and $(1-s)^{d-1}$ by $1$ has $O(\varepsilon^2)$ total error, because each change is $O(\varepsilon)$ and the thickness is $O(\varepsilon)$. Thus, uniformly on that $u$-set by the $L^1$ convergence, the removed hinge integral is
$$
\varepsilon\int_{\partial K}[1+u\cdot(x-y)]_+v(x)\,dS(x)+o(\varepsilon).
\tag{4}
$$
Where the old hinge vanishes, including on a coincident supporting facet, its thin-layer value is $O(\varepsilon)$, so there is no first-order boundary cost there.

On the fixed body $K$, the gradient in the mark $q$ of the hinge integral is $-|D_u(q)|u$, now with $L=K$. For $u\ne0$ the zero hyperplane has zero $d$-volume; near $u=0$ the hinge is strictly positive on $K$ for marks in a compact neighborhood of $y$. Dominated convergence gives the gradient and joint continuity of the cap volume in $(u,q)$, hence a uniform mark expansion on compact $u$-sets. Combining with (4) gives
$$
\begin{aligned}
G_\varepsilon(u)&:=\int_{K_\varepsilon}[1+u\cdot(x-y_\varepsilon)]_+\,dx
                 =G_0(u)+\varepsilon\Phi(u)+o(\varepsilon),\\
\Phi(u)&=-\int_{\partial K}[1+u\cdot(x-y)]_+v\,dS-|D_u(y)|u\cdot w .
\end{aligned}
\tag{5}
$$
The expansion is compact-uniform in $u$ and $\Phi$ is continuous.

The inner homothet of a ball about $y$ shows that $K_\varepsilon$ contains a ball of fixed positive radius centered at $y_\varepsilon$ for all small $\varepsilon$, since the two centers differ by $O(\varepsilon)$. The positive linear part integrated over that ball gives $G_\varepsilon(u)\ge c\lVert u\rVert$ for one $c>0$ independent of $\varepsilon$, while $G_\varepsilon(0)\le|K|$. Thus all minimizing parameters lie in one compact ball, including at zero. Uniform convergence gives that every cluster point of minimizers $u_\varepsilon$ lies in $U$. Evaluating (5) at a minimizer of $\Phi$ on $U$ bounds the upper right difference quotient of $\min G_\varepsilon$ by $\min_U\Phi$. Conversely,
$$
\frac{\min G_\varepsilon-\min G_0}{\varepsilon}
=\frac{G_0(u_\varepsilon)-\min G_0}{\varepsilon}
  +\Phi(u_\varepsilon)+o(1)
\ge\Phi(u_\varepsilon)+o(1).
$$
Compactness and continuity give the reverse lower bound. The hinge result gives $|D_u(y)|=T$ on $U$, proving (1).

When $y=g_K$, the untruncated affine integral is $V$, and its positive-part integral equals $V$ exactly when the affine function is nonnegative throughout $K$. A negative value anywhere would entail negativity on a positive-volume subset by full dimension and convexity. Thus $U=-(K-y)^\circ$, where $L^\circ=\{q:q\cdot x\le1\ \forall x\in L\}$. Every optimal hinge has boundary cost $D+u\cdot B$. Separation from dilates of $K-y$ gives $\max_{q\in(K-y)^\circ}q\cdot z=p_{K-y}(z)$, so substitution in (1) gives (2). The gauge vanishes only at zero, since $K-y$ is bounded. Applying (3) to the constant and coordinate weights gives $|K_\varepsilon|=V-\varepsilon D+o(\varepsilon)$ and $\int_{K_\varepsilon}x\,dx=Vy-\varepsilon(Dy+B)+o(\varepsilon)$, proving the centroid expansion and the equality criterion.
