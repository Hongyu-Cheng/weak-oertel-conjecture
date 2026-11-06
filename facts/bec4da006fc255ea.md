---
fact_id: bec4da006fc255ea
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: subcubic-tree-half-integer-flow-folding
depends_on: []
verifier_run: 6092a28d92914c08
target_match: null
---

## Statement

Let \(G\) have vertices \(a,b,a^+,a^-,b^+,b^-,p_1,\ldots,p_{94}\). Its edges are \(ab,aa^+,aa^-,bb^+,bb^-\), together with the path \(a^+p_1,p_1p_2,\ldots,p_{93}p_{94}\). Thus \(n=100\), \(m=99\), and the maximum degree is three. If a rooted presentation is needed, root at the leaf \(a^-\) and label it \(1\). Take the allowed rational parameter \(k=1\), so \(R=n/2+k=51\). The corresponding original-body continuous dimension is \(d=3n-2=298\).

Let \(B\) be the unsigned vertex-edge incidence matrix, and retain the canonical definitions

\[
E_{\mathbf u}(\boldsymbol\xi)
=\sum_e|\xi_e|+\sum_v|u_v-(B\boldsymbol\xi)_v|,
\qquad
F(\boldsymbol\xi)
=\sum_e|\xi_e|+\sum_v\operatorname{dist}((B\boldsymbol\xi)_v,\mathbb Z+1/2).
\]

Define \(\boldsymbol\xi^\ast\in[-1/2,1/2]^{99}\) by

\[
\begin{aligned}
\xi^\ast_{ab}&=1/5, &
\xi^\ast_{aa^+}=\xi^\ast_{bb^+}&=2/5, &
\xi^\ast_{aa^-}=\xi^\ast_{bb^-}&=-1/10,\\
\xi^\ast_{a^+p_1}&=0, &
\xi^\ast_{p_i p_{i+1}}&=
\begin{cases}
1/2,&i\text{ odd},\\
0,&i\text{ even}
\end{cases}
&& (1\le i\le93).
\end{aligned}
\]

Then

\[
\inf_{\substack{\boldsymbol\varepsilon\in\{-1,1\}^{99}\\
                 \mathbf h\in\mathbb Z^{99}}}
E_{(1/2,\ldots,1/2)}
 \bigl(\boldsymbol\varepsilon\boldsymbol\xi^\ast+\mathbf h/2\bigr)
=\frac{129}{5}
>\frac{257}{10}
=F(\boldsymbol\xi^\ast)
<51.
\]

Moreover, the strict inequality with infimum greater than \(F(\boldsymbol\xi)\) holds for every \(\boldsymbol\xi\in[-1/2,1/2]^{99}\) with \(\|\boldsymbol\xi-\boldsymbol\xi^\ast\|_1<1/120\). All these source flows satisfy \(F(\boldsymbol\xi)<R\), and their set has positive \(99\)-dimensional Lebesgue measure.

## Proof

The tree has six initial vertices and 94 new vertices, and five initial edges and 94 new edges. Only \(a\) and \(b\) have degree three; the added path and its attachment have degree at most two. The new endpoint \(p_{94}\) and the three unextended initial leaves have degree one. This verifies the stated tree and parameter conditions, including \(1\le k\le n/100\).

For the proof only, use the explicit scaling aliases \(\boldsymbol\zeta=2\boldsymbol\xi\) for source flows and \(\boldsymbol\theta=2\boldsymbol\eta\) for output flows. Put

\[
\begin{aligned}
\widehat F(\boldsymbol\zeta)
&:=2F(\boldsymbol\zeta/2)
=\sum_e|\zeta_e|
  +\sum_v\operatorname{dist}((B\boldsymbol\zeta)_v,2\mathbb Z+1),\\
\widehat E(\boldsymbol\theta)
&:=2E_{(1/2,\ldots,1/2)}(\boldsymbol\theta/2)
=\sum_e|\theta_e|+\sum_v|1-(B\boldsymbol\theta)_v|.
\end{aligned}
\]

The allowed outputs become exactly \(\boldsymbol\theta=\boldsymbol\varepsilon\boldsymbol\zeta+\mathbf h\), with independent edge signs and arbitrary integer coordinates of \(\mathbf h\). Thus the source \(\boldsymbol\zeta^\ast=2\boldsymbol\xi^\ast\) has central value \(2/5\), two positive leaf-edge values \(4/5\), two negative leaf-edge values \(-1/5\), and alternating path values zero and one. Its allowed central output values are \(\{\pm2/5+j:j\in\mathbb Z\}\). Each of the four initial leaf edges has allowed output values \(\{\pm1/5+j:j\in\mathbb Z\}\). Every added path edge has arbitrary integer output values. These descriptions include all permitted transformations, including choices depending on the entire source.

At both central vertices, \((B\boldsymbol\zeta^\ast)_v=2/5+4/5-1/5=1\). Each of the 94 added vertices also has incident sum one, because precisely one adjacent path edge has value one. The incident sums at \(a^+,b^+\) are \(4/5\), and those at \(a^-,b^-\) are \(-1/5\). Their distances to \(2\mathbb Z+1\) are respectively \(1/5\) and \(4/5\). The 47 path edges of value one contribute 47 to the edge norm. The other five edges contribute \(2/5+2(4/5+1/5)=12/5\). Consequently

\(\widehat F(\boldsymbol\zeta^\ast)=47+12/5+2(1/5+4/5)=257/5\).

The nearest odd charges in this calculation are one at every vertex except \(a^-\) and \(b^-\), where they are minus one. After division by two they are allowed original half-integer charges, so the displayed value uses the original minimum over integer bases.

We next remove the padding exactly from the target optimization. Fix an arbitrary real output value \(s\) on \(aa^+\). Write \(\theta_0\) for the output on \(a^+p_1\), and \(\theta_i\) for that on \(p_i p_{i+1}\) for \(1\le i\le93\); set \(\theta_{94}=0\) solely as an endpoint convention. For each even index \(j\in\{2,4,\ldots,94\}\), the triangle inequality gives
\(|1-\theta_{j-1}-\theta_j|+|\theta_{j-1}|+|\theta_j|\ge1\).
Summing these 47 inequalities counts every internal path-edge norm \(|\theta_i|\), \(1\le i\le93\), exactly once. The uncounted residuals at odd-indexed path vertices are nonnegative. Thus the total target cost on the 94 new vertices and their internal edges is at least 47, for arbitrary real values of these flows. Adding the attachment edge and the residual at \(a^+\) yields the lower bound

\(47+|\theta_0|+|1-s-\theta_0|\ge47+|1-s|\).

Equality is attained by the allowed integer choices \(\theta_0=0\) and \(\theta_i=1\) for odd \(i\), \(\theta_i=0\) for even \(i\). Therefore, for every fixed \(s\), this entire padded leaf contributes exactly 47 plus the cost of an ordinary target leaf. Including the edge \(aa^+\), its minimized contribution is \(47+L(s)\), where \(L(s):=|s|+|1-s|\). Each other initial leaf and its edge contribute \(L(s)\).

For any \(s\in\{\pm1/5+j:j\in\mathbb Z\}\), there is \(\pi(s)\in\{1/5,4/5\}\) such that \(L(s)\ge1+|s-\pi(s)|\). Indeed, if \(s\in[0,1]\), then \(s\) is one of these two values and we take \(\pi(s)=s\). If \(s\notin[0,1]\), put \(D=\operatorname{dist}(s,[0,1])\). The allowed phases give \(D\ge1/5\). Choosing \(\pi(s)=1/5\) below the interval and \(\pi(s)=4/5\) above it gives \(|s-\pi(s)|=D+1/5\le2D=L(s)-1\).

Fix a real central-edge output \(t\). At either central vertex, let \(s_1,s_2\) denote its two initial leaf-edge outputs. The preceding bound and the triangle inequality imply

\[
\begin{aligned}
L(s_1)+L(s_2)+|1-t-s_1-s_2|
&\ge2+|1-t-\pi(s_1)-\pi(s_2)|\\
&\ge2+\operatorname{dist}\bigl(t,\{-3/5,0,3/5\}\bigr).
\end{aligned}
\]

The second line uses the three possible sums \(\pi(s_1)+\pi(s_2)\in\{2/5,1,8/5\}\). Conversely, every such sum is attainable by allowed outputs \(s_1,s_2\in\{1/5,4/5\}\), each with \(L(s_i)=1\). Hence the minimum contribution from that central residual and its two leaves and leaf edges is exactly \(2+\operatorname{dist}(t,\{-3/5,0,3/5\})\), apart from the already determined padding constant 47 on one side.

It follows that every permitted output satisfies

\[
\widehat E(\boldsymbol\theta)
\ge47+4+|t|+2\operatorname{dist}\bigl(t,\{-3/5,0,3/5\}\bigr),
\qquad
t\in\{\pm2/5+j:j\in\mathbb Z\}.
\]

If \(|t|\ge3/5\), the last two terms sum to at least \(3/5\). If \(|t|<3/5\), the allowed central phase forces \(t=2/5\) or \(t=-2/5\); its distance to the three-point set is then \(1/5\), and those terms sum to \(4/5\). This proves the lower bound \(\widehat E\ge47+4+3/5=258/5\) over every sign choice and every integer carry, without bounding the carries in advance.

The bound is attained. Set the central output to \(3/5\), all four initial leaf-edge outputs to \(1/5\), and the path outputs to the alternating zero-one values already specified. The two central residuals vanish, each leaf and its edge contribute one, and the path adds 47. The central change is \(3/5=-(2/5)+1\), the positive leaf-edge changes are \(1/5=-(4/5)+1\), and the negative leaf-edge changes are \(1/5=-(-1/5)\). Thus this is a permitted global transformation. Dividing the exact input and output values by two proves the displayed strict inequality in the statement.

Finally, both \(F\) and every fixed-target energy \(E_{\mathbf u}\) are \(3\)-Lipschitz in the edge \(\ell^1\) norm. Each absolute value or distance term is \(1\)-Lipschitz, and each edge occurs in exactly two vertex sums, so
\(|F(\boldsymbol\xi)-F(\boldsymbol\xi^\ast)|\le3\|\boldsymbol\xi-\boldsymbol\xi^\ast\|_1\), with the same estimate for \(E_{\mathbf u}\).
For arbitrary \(\boldsymbol\varepsilon,\mathbf h\), the two corresponding outputs from \(\boldsymbol\xi\) and \(\boldsymbol\xi^\ast\) differ in \(\ell^1\) norm by exactly \(\|\boldsymbol\xi-\boldsymbol\xi^\ast\|_1\). Writing this norm as \(\delta\), the already proved uniform lower bound gives

\[
\begin{aligned}
E_{(1/2,\ldots,1/2)}
 (\boldsymbol\varepsilon\boldsymbol\xi+\mathbf h/2)
&\ge\frac{129}{5}-3\delta,\\
F(\boldsymbol\xi)&\le\frac{257}{10}+3\delta.
\end{aligned}
\]

For \(\delta<1/120\), the gap is greater than \(1/20\), and the source energy is less than \(257/10+1/40<51\). Intersecting this neighborhood with \([-1/2,1/2]^{99}\) leaves a positive-measure set: coordinates initially equal to \(1/2\) may be perturbed toward the cube interior, and every other coordinate already lies in its interior. This proves the final assertion.

## External sources

None. The argument is self-contained and uses no computation or finite certificate as a proof premise.
