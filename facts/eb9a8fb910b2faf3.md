---
fact_id: eb9a8fb910b2faf3
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: reflection-symmetric-entropy-row-formula
depends_on: ["488f0a583886b5fc","57c57a5fe0d4d1cc"]
verifier_run: 2e96e49ec0604596
target_match: null
---

## Statement

Let \(n\ge1\), let \(D\subset\mathbb Z^n\) be finite and nonempty with \(D=\operatorname{conv}(D)\cap\mathbb Z^n\), and let \(p_{\mathbf I}>0\) on \(D\), with \(\sum_{\mathbf I\in D}p_{\mathbf I}=1\) and \(p_{\mathbf I}=0\) off \(D\). Assume that \(p\) has a finite-valued globally log-concave extension agreeing with every lattice value, including every zero, in the sense of accepted fact `488f0a583886b5fc`. Assume also that \(p\) is invariant under each coordinate reflection \(I_i\mapsto1-I_i\), acting on the complete table.

Use precisely the arrays, objective, and entropy of accepted fact `57c57a5fe0d4d1cc`:

\[
\begin{aligned}
\mathcal F&=\left\{r\ge0:
\sum_{\mathbf J\in D}r_{\mathbf J,\mathbf I}=p_{\mathbf I}\quad(\mathbf I\in D),\quad
\sum_{\mathbf I\in D}r_{\mathbf J,\mathbf I}(\mathbf I-\mathbf J)=\mathbf0\quad(\mathbf J\in D)
\right\},\\
q_{\mathbf J}&=\sum_{\mathbf I\in D}r_{\mathbf J,\mathbf I},\qquad
V(r)=\sum_{\mathbf J\in D}q_{\mathbf J}\|\mathbf J\|^2,\qquad
H(r)=-\sum_{\mathbf J,\mathbf I\in D}r_{\mathbf J,\mathbf I}
\log\frac{r_{\mathbf J,\mathbf I}}{p_{\mathbf I}}.
\end{aligned}
\]

Here \(0\log0=0\). Let \(\mathcal F_{\min}\) minimize \(V\) on \(\mathcal F\), and let \(r^\star\) be the entropy maximizer on \(\mathcal F_{\min}\). Retain \(\mathcal T=\{(\mathbf J,\mathbf I):r_{\mathbf J,\mathbf I}>0\text{ for some }r\in\mathcal F_{\min}\}\), \(\mathcal J=\{\mathbf J:(\mathbf J,\mathbf I)\in\mathcal T\text{ for some }\mathbf I\}\), \(D_{\mathbf J}=\{\mathbf I:(\mathbf J,\mathbf I)\in\mathcal T\}\), and \(\psi_{\mathbf J}(\mathbf I)=-\log(r^\star_{\mathbf J,\mathbf I}/p_{\mathbf I})\) on \(D_{\mathbf J}\), with the same meanings as in that fact.

Put \(R_i(\mathbf I)=|I_i-\tfrac12|\), \(\mathbf R(\mathbf I)=(R_1(\mathbf I),\ldots,R_n(\mathbf I))\), and let \(\mathcal X=\{i:\max_{\mathbf I\in D}R_i(\mathbf I)>\tfrac12\}\) be the expanded axes. For each \(i\in\mathcal X\), there is exactly one finite \(\theta_i>0\) satisfying

\[
\mathbb E_p\!\left[R_i\tanh(\theta_iR_i)\right]=\frac12.
\]

For \(i\notin\mathcal X\), every supported \(I_i\) is in \(\{0,1\}\), and the assignment on this axis is the exact deterministic rule \(J_i=I_i\). Empty products below equal one, and empty sums equal zero.

The cube \(\{0,1\}^n\) is contained in \(D\), and the unique entropy maximizer is

\[
r^\star_{\mathbf J,\mathbf I}=
\begin{cases}
\displaystyle p_{\mathbf I}
\prod_{i\in\mathcal X}
\frac{\exp\!\left((2J_i-1)\theta_i(I_i-\tfrac12)\right)}
{2\cosh\!\left(\theta_iR_i(\mathbf I)\right)},
&\mathbf J\in\{0,1\}^n,\quad I_i=J_i\ (i\notin\mathcal X),\\
0,&\text{otherwise},
\end{cases}
\qquad(\mathbf J,\mathbf I\in D).
\]

For an expanded axis its displayed factor is \(\bigl[1+(2J_i-1)\tanh(\theta_i(I_i-\tfrac12))\bigr]/2\). For an unexpanded axis its deterministic factor is \(\bigl[1+(2J_i-1)(2I_i-1)\bigr]/2\). Thus this is exactly the proposed product of assignment factors, with the unexpanded-axis limit implemented by structural zeros. The resulting face and support are

\[
\begin{aligned}
\min_{r\in\mathcal F}V(r)&=\frac n2,\qquad
\mathcal J=\{0,1\}^n,\qquad q^\star_{\mathbf J}=2^{-n}\quad(\mathbf J\in\mathcal J),\\
\mathcal T&=\{(\mathbf J,\mathbf I)\in\{0,1\}^n\times D:
I_i=J_i\text{ for every }i\notin\mathcal X\},\\
\mathcal F_{\min}&=\{r\in\mathcal F:r_{\mathbf J,\mathbf I}=0
\text{ whenever }(\mathbf J,\mathbf I)\notin\mathcal T\},\\
D_{\mathbf J}&=\{\mathbf I\in D:I_i=J_i\text{ for every }i\notin\mathcal X\}
\quad(\mathbf J\in\mathcal J).
\end{aligned}
\]

In particular, every entry in the displayed \(\mathcal T\) is positive at \(r^\star\), and there are no further forced zeros.

For each \(\mathbf u\in(\tfrac12+\mathbb Z_{\ge0})^n\), define its original joint radius mass by \(\rho_{\mathbf u}=\sum_{\mathbf I\in D:\mathbf R(\mathbf I)=\mathbf u}p_{\mathbf I}\). Every normalized positive row retains this exact joint law:

\[
\sum_{\substack{\mathbf I\in D_{\mathbf J}\\\mathbf R(\mathbf I)=\mathbf u}}
\frac{r^\star_{\mathbf J,\mathbf I}}{q^\star_{\mathbf J}}
=\rho_{\mathbf u}
\qquad(\mathbf J\in\{0,1\}^n).
\]

For \(\rho_{\mathbf u}>0\), the conditional source-coordinate means under that normalized row are

\[
\mathbb E_{r^\star_{\mathbf J,\cdot}/q^\star_{\mathbf J}}
\!\left[I_i\mid\mathbf R=\mathbf u\right]
=
\begin{cases}
\displaystyle\frac12+(2J_i-1)u_i\tanh(\theta_i u_i),&i\in\mathcal X,\\
J_i,&i\notin\mathcal X.
\end{cases}
\]

On an expanded axis this need not equal \(J_i\) at a fixed joint radius. Its average over the original law \(\rho\) equals \(J_i\). Thus the atoms at one joint radius need not themselves have barycenter \(\mathbf J\) under the row weights.

The finite entropy multipliers \(\boldsymbol\beta_{\mathbf J}\) of accepted fact `57c57a5fe0d4d1cc` can be chosen by the exact normalization map

\[
\begin{aligned}
\beta_{\mathbf J,i}&=
\begin{cases}(2J_i-1)\theta_i,&i\in\mathcal X,\\0,&i\notin\mathcal X,\end{cases}\\
N(\mathbf I)&=
\exp\!\left(-\frac12\sum_{i\in\mathcal X}\theta_i\right)
\prod_{i\in\mathcal X}2\cosh\!\left(\theta_iR_i(\mathbf I)\right).
\end{aligned}
\]

Here \(N\) is exactly the sum over the active targets \(\mathcal A(\mathbf I)=\{\mathbf J:(\mathbf J,\mathbf I)\in\mathcal T\}\) in that fact. On \(D_{\mathbf J}\), the assignment-share potential is

\[
\begin{aligned}
\psi_{\mathbf J}(\mathbf I)
&=\log N(\mathbf I)-\boldsymbol\beta_{\mathbf J}\cdot(\mathbf I-\mathbf J)\\
&=\sum_{i\in\mathcal X}
\left[\log\!\left(2\cosh\!\left(\theta_iR_i(\mathbf I)\right)\right)
-(2J_i-1)\theta_i(I_i-\tfrac12)\right].
\end{aligned}
\]

For the original logarithmic costs use the normalization of accepted fact `488f0a583886b5fc`: \(w=p\), \(W=1\), \(w_{\max}=\max_{\mathbf I\in D}p_{\mathbf I}\), and \(\phi_{\mathbf I}=\log(w_{\max}/p_{\mathbf I})\). Every cube target satisfies \(p_{\mathbf J}=w_{\max}\), hence \(\phi_{\mathbf J}=0\). The original potential \(\phi\) depends only on the joint radius vector, so its entire distribution, and in particular its expectation, is unchanged in every normalized row:

\[
\sum_{\mathbf I\in D_{\mathbf J}}
\frac{r^\star_{\mathbf J,\mathbf I}}{q^\star_{\mathbf J}}\phi_{\mathbf I}
=\sum_{\mathbf I\in D}p_{\mathbf I}\phi_{\mathbf I}.
\]

For any nonempty \(E\subseteq D_{\mathbf J}\) and any positive coefficients \(\lambda_{\mathbf I}\) of sum one and barycenter \(\sum_{\mathbf I\in E}\lambda_{\mathbf I}\mathbf I=\mathbf J\), write \(G_\lambda(u)=\log u_{\mathbf J}-\sum_{\mathbf I\in E}\lambda_{\mathbf I}\log u_{\mathbf I}\). Then the exact comparison, with no affine-independence assumption, is

\[
\begin{aligned}
G_\lambda(r^\star_{\mathbf J,\cdot}/q^\star_{\mathbf J})
&=G_\lambda(r^\star_{\mathbf J,\cdot})\\
&=G_\lambda(p)+
\sum_{i\in\mathcal X}\sum_{\mathbf I\in E}\lambda_{\mathbf I}
\log\frac{\cosh(\theta_iR_i(\mathbf I))}{\cosh(\theta_i/2)}\\
&\ge G_\lambda(p)=\sum_{\mathbf I\in E}\lambda_{\mathbf I}\phi_{\mathbf I}\ge0.
\end{aligned}
\]

## Proof

Coordinate reflections preserve \(D\) because the symmetry includes the zero values off \(D\). Each \(R_i(\mathbf I)\) is a positive half-integer. For any \(\mathbf I\in D\), its reflection orbit consists of all \(2^n\) lattice points whose coordinates are \(\tfrac12+\varepsilon_iR_i(\mathbf I)\), with \(\varepsilon_i\in\{-1,1\}\). They all have the same positive mass \(p_{\mathbf I}\). The convex hull of this orbit is the box with coordinate intervals \([\tfrac12-R_i(\mathbf I),\tfrac12+R_i(\mathbf I)]\), and it contains \([0,1]^n\). Lattice convexity therefore gives \(\{0,1\}^n\subseteq D\). Global log-concavity, applied to a convex representation of any cube vertex by this orbit, also gives \(p_{\mathbf J}\ge p_{\mathbf I}\) for every cube vertex \(\mathbf J\). All cube vertices have equal mass by reflection symmetry. This proves \(p_{\mathbf J}=w_{\max}\) and \(\phi_{\mathbf J}=0\).

Every occurring joint radius vector has exactly these \(2^n\) sign choices in its orbit, each with mass \(2^{-n}\rho_{\mathbf u}\). Thus, conditional on the complete joint radius vector under \(p\), all signs are uniform and independent. This assertion concerns conditional signs only; it imposes no independence on the radius coordinates. It also proves that \(p_{\mathbf I}\), and therefore \(\phi_{\mathbf I}\), depends only on \(\mathbf R(\mathbf I)\). Averaging a single coordinate reflection gives \(\mathbb E_p I_i=\tfrac12\) for every \(i\).

For an expanded axis, the function \(t\mapsto\mathbb E_p[R_i\tanh(tR_i)]\) is continuous on \([0,\infty)\), equals zero at zero, and has derivative \(\mathbb E_p[R_i^2/\cosh^2(tR_i)]>0\) at every finite \(t\). Its limit at infinity is \(\mathbb E_pR_i>\tfrac12\), since \(R_i\ge\tfrac12\) and at least one positive-mass source has a strictly larger radius. The intermediate value theorem and strict increase prove the unique finite positive solution \(\theta_i\). If the axis is unexpanded, \(R_i=\tfrac12\) everywhere, so the same expression is \(\tfrac12\tanh(t/2)<\tfrac12\) at every finite \(t\) and tends to \(\tfrac12\) at infinity. On that axis the displayed assignment factors have the exact limiting values one for \(I_i=J_i\) and zero for \(I_i\ne J_i\).

Let \(\widehat r\) denote the array in the statement until its entropy optimality has been proved. It is nonnegative. At a fixed source \(\mathbf I\), the sum of each expanded factor over \(J_i\in\{0,1\}\) is one, and the unexpanded rule admits exactly one value of \(J_i\). Since all cube targets are in \(D\), summing over targets gives \(\sum_{\mathbf J\in D}\widehat r_{\mathbf J,\mathbf I}=p_{\mathbf I}\).

For a fixed occurring \(\mathbf u\) and target \(\mathbf J\), use the uniform signs in the source orbit. Summing the assignment factors over the source signs gives one on each axis, including the deterministic axes. Consequently

\[
\sum_{\substack{\mathbf I\in D\\\mathbf R(\mathbf I)=\mathbf u}}
\widehat r_{\mathbf J,\mathbf I}=2^{-n}\rho_{\mathbf u},
\qquad
\widehat q_{\mathbf J}=2^{-n}
\quad(\mathbf J\in\{0,1\}^n).
\]

After conditioning both on this row and on \(\mathbf R=\mathbf u\), the probability of a source sign vector \(\boldsymbol\varepsilon\in\{-1,1\}^n\) is exactly

\[
\prod_{i\in\mathcal X}
\frac{1+(2J_i-1)\varepsilon_i\tanh(\theta_i u_i)}2
\prod_{i\notin\mathcal X}\mathbf1_{\{\varepsilon_i=2J_i-1\}}.
\]

This proves conditional independence of the row signs and the conditional-mean formula in the statement. Averaging that formula over the just-proved unchanged joint radius law gives, on each expanded axis,
\(\mathbb E_{\widehat r_{\mathbf J,\cdot}/\widehat q_{\mathbf J}}I_i=\tfrac12+(2J_i-1)\mathbb E_p[R_i\tanh(\theta_iR_i)]=J_i\).
On an unexpanded axis \(I_i=J_i\) identically in the row. Thus every positive row has mean \(\mathbf J\), and every zero row automatically satisfies its moment equation. This proves \(\widehat r\in\mathcal F\), its uniform row masses, and its exact joint radius conservation. The conditional means have been averaged over the original law; no conditional barycenter assertion at individual radii was used.

For an arbitrary \(r\in\mathcal F\), summing the row identities and using the column sums gives \(\sum_{\mathbf J}q_{\mathbf J}J_i=\mathbb E_pI_i=\tfrac12\). Hence

\[
V(r)-\frac n2
=\sum_{\mathbf J\in D}q_{\mathbf J}
\sum_{i=1}^n J_i(J_i-1)\ge0.
\]

Each summand \(J_i(J_i-1)\) is nonnegative for integral \(J_i\), and it vanishes exactly for \(J_i\in\{0,1\}\). Equality holds if and only if every positive row target lies in the cube. The feasible array \(\widehat r\) has precisely such targets, so the minimum is \(n/2\), and the entire minimizing face consists of feasible arrays with zero rows outside the cube.

There are further entrywise restrictions on this face at unexpanded axes. If \(J_i=0\), its row moment equation in coordinate \(i\) is a sum of the nonnegative quantities \(r_{\mathbf J,\mathbf I}I_i\), with \(I_i\in\{0,1\}\); every entry with \(I_i=1\) must vanish. If \(J_i=1\), use the nonnegative quantities \(r_{\mathbf J,\mathbf I}(1-I_i)\) to obtain the reverse deterministic restriction. Therefore every variance-minimal array vanishes outside the stated \(\mathcal T\). Conversely, \(\widehat r\) is strictly positive at each entry of this set: \(p_{\mathbf I}>0\), all expanded multipliers are finite, and all deterministic restrictions hold there. No entry in that set is forced to vanish. This proves exactly the claimed \(\mathcal T\), \(D_{\mathbf J}\), and characterization of \(\mathcal F_{\min}\). The positive masses of all cube rows prove \(\mathcal J=\{0,1\}^n\).

We next compare entropy with every member of this true optimal face, allowing arbitrary row masses and arbitrary nonsymmetric arrays. For \((\mathbf J,\mathbf I)\in\mathcal T\), the identity \((2J_i-1)(J_i-\tfrac12)=\tfrac12\) gives

\[
\log\frac{\widehat r_{\mathbf J,\mathbf I}}{p_{\mathbf I}}
=\boldsymbol\beta_{\mathbf J}\cdot(\mathbf I-\mathbf J)-\log N(\mathbf I),
\]

with the finite \(\boldsymbol\beta\) and \(N\) in the statement. In particular, the unexpanded components of \(\boldsymbol\beta\) may be zero because their structural zeros have already been imposed. These are finite multipliers on the exact support, not infinite multipliers inserted into the formula of accepted fact `57c57a5fe0d4d1cc`. The active targets at \(\mathbf I\) have all expanded bits free and all other bits fixed. Summing \(\exp(\boldsymbol\beta_{\mathbf K}\cdot(\mathbf I-\mathbf K))\) over those targets factors into
\(\exp(-\tfrac12\sum_{i\in\mathcal X}\theta_i)\prod_{i\in\mathcal X}2\cosh(\theta_iR_i(\mathbf I))\).
Thus \(N\) has exactly the active-sum meaning required by that accepted representation.

For every \(r\in\mathcal F_{\min}\), all entries outside \(\mathcal T\) vanish, and the moment and column constraints give

\[
\sum_{(\mathbf J,\mathbf I)\in\mathcal T}
r_{\mathbf J,\mathbf I}
\log\frac{\widehat r_{\mathbf J,\mathbf I}}{p_{\mathbf I}}
=-\sum_{\mathbf I\in D}p_{\mathbf I}\log N(\mathbf I).
\]

The same equality holds for \(\widehat r\), so direct subtraction yields

\[
\begin{aligned}
H(r)&=H(\widehat r)-
\sum_{(\mathbf J,\mathbf I)\in\mathcal T}
r_{\mathbf J,\mathbf I}
\log\frac{r_{\mathbf J,\mathbf I}}{\widehat r_{\mathbf J,\mathbf I}},\\
H(\widehat r)&=\sum_{\mathbf I\in D}p_{\mathbf I}\log N(\mathbf I)
=\sum_{i\in\mathcal X}
\left(\mathbb E_p\log(2\cosh(\theta_iR_i))-\frac{\theta_i}2\right).
\end{aligned}
\]

The relative-entropy sum is nonnegative, with equality exactly when the two arrays agree. Indeed, for \(x\ge0\) and \(y>0\), \(x\log(x/y)-x+y\ge0\), with equality exactly at \(x=y\); this follows by minimizing \(t\log t-t+1\) on \([0,\infty)\). Sum the inequality with \(x=r_{\mathbf J,\mathbf I}\), \(y=\widehat r_{\mathbf J,\mathbf I}\). The linear terms cancel because each array has total mass one, and \(\widehat r\) is positive throughout \(\mathcal T\). This proves entropy optimality and uniqueness on the full face, and hence \(\widehat r=r^\star\).

The share-potential formula follows by taking the negative logarithm of the now-proved optimizer. Radius conservation and the fact that \(\phi\) depends only on the complete joint radius vector give its distributional and expectation assertions. The original normalization \(w=p\), \(W=1\) and the scale-invariant cost \(G_\lambda\) agree with accepted fact `488f0a583886b5fc` and with the row-cost normalization in `57c57a5fe0d4d1cc`.

For a stated barycentric component, subtracting the two logarithmic costs gives
\(G_\lambda(r^\star_{\mathbf J,\cdot})-G_\lambda(p)=\sum_{\mathbf I\in E}\lambda_{\mathbf I}\psi_{\mathbf J}(\mathbf I)-\psi_{\mathbf J}(\mathbf J)\).
The affine term in the displayed share potential cancels under the barycentric constraint, and \(R_i(\mathbf J)=\tfrac12\). This gives exactly the sum of logarithms of cosh ratios in the statement. Every ratio is at least one because \(R_i(\mathbf I)\ge\tfrac12\), \(\theta_i>0\), and cosh is increasing on \([0,\infty)\). Common scaling of a table cancels in \(G_\lambda\), giving equality under row normalization. Finally \(\phi_{\mathbf J}=0\) gives \(G_\lambda(p)=\sum\lambda_{\mathbf I}\phi_{\mathbf I}\ge0\). This proves the full original-cost comparison without a product assumption on the source table.

Here is an exact coupled example, including a check of the conditional-mean distinction. Take \(n=2\), \(D=\{-1,0,1,2\}^2\), and

\[
p_{\mathbf I}=\begin{cases}
43/256,&\mathbf I\in\{0,1\}^2,\\
7/256,&\mathbf I\in D\setminus\{0,1\}^2,\\
0,&\mathbf I\notin D.
\end{cases}
\]

The total mass is \((4\cdot43+12\cdot7)/256=1\). A finite globally log-concave extension with all the required zeros is

\[
f(x)=\begin{cases}
\displaystyle\frac{43}{256}
\exp\!\left[-\log(43/7)
\left(\max\{|x_1-\tfrac12|,|x_2-\tfrac12|\}-\tfrac12\right)\right],
&x\in[-1,2]^2,\\
0,&x\notin[-1,2]^2.
\end{cases}
\]

The maximum of the two absolute values is convex, and the square is convex, proving log-concavity including pairs with a zero endpoint. Its lattice values are exactly the stated table. The complete support is lattice convex and is invariant under both reflections.

The original joint radius law, with row and column order \((\tfrac12,\tfrac32)\), and either one-coordinate marginal are

\[
\bigl(\rho_{(u,v)}\bigr)_{u,v\in\{1/2,3/2\}}
=\frac1{64}\begin{pmatrix}43&7\\7&7\end{pmatrix},
\qquad
\mathbb P_p(R_i=\tfrac12)=\frac{25}{32},\quad
\mathbb P_p(R_i=\tfrac32)=\frac7{32}.
\]

This law is nonproduct because \(43/64\ne(25/32)^2\). Both axes are expanded. Their unique multipliers are \(\theta_1=\theta_2=\log3\): the identities \(\tanh(\tfrac12\log3)=\tfrac12\) and \(\tanh(\tfrac32\log3)=\tfrac{13}{14}\) give

\[
\frac{25}{32}\frac12\frac12
+\frac7{32}\frac32\frac{13}{14}
=\frac{25}{128}+\frac{39}{128}=\frac12.
\]

Thus the entropy maximizer has four rows of mass \(1/4\), variance objective one, and positive entries at all \(\{0,1\}^2\times D\). Each normalized row retains the displayed nonproduct joint radius law, so each row itself is nonproduct as a distribution of the source coordinates. In the row \(\mathbf J=(1,1)\), conditional on a joint radius vector, the signs are independent and the probability of a positive sign on axis \(i\) is \(3/4\) for \(u_i=\tfrac12\) and \(27/28\) for \(u_i=\tfrac32\). The corresponding conditional coordinate means are \(3/4\) and \(53/28\), respectively, both different from \(J_i=1\). Their average is exactly \((25/32)(3/4)+(7/32)(53/28)=1\).

For this example the original potential is zero on the central cube and \(\log(43/7)\) elsewhere on \(D\). Moreover \(\cosh(\tfrac32\log3)/\cosh(\tfrac12\log3)=7/3\), so the extra row cost for every stated component is exactly

\[
G_\lambda(r^\star_{\mathbf J,\cdot}/q^\star_{\mathbf J})-G_\lambda(p)
=\log(7/3)\sum_{\mathbf I\in E}\lambda_{\mathbf I}
\left(\mathbf1_{\{I_1\in\{-1,2\}\}}+
\mathbf1_{\{I_2\in\{-1,2\}\}}\right).
\]

All radius probabilities in this example and in the proof are the original joint probabilities, rather than products of their marginals. The conclusion is the explicit entropy-row formula and its cost identity; it asserts no actual halfspace-depth bound or universal original-capacity hitting bound.

## External sources

None.
