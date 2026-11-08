---
fact_id: a7b09eaaf3adb06e
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-truncated-triangle-energy-chart-residual-base-work
depends_on: ["54209ffcf6adbb64", "d90ba05577427854", "d7ff9f9aad2b6512"]
verifier_run: 298fc60029d8ee47
target_match: null
---

## Source

- [ad7cea9b764c02b5](../candidates/ad7cea9b764c02b5.json), ad7cea9b764c02b5:05 §7, (10)–(12), actual deepest mark and residual base work.
- [e0241fcf7902a02f](../candidates/e0241fcf7902a02f.json), e0241fcf7902a02f:01 §§1–2, (1)–(9), exact nonaffine calibration and centering.

## Statement

Use the actual truncated triangles $K_{1+ez}$, $z=-1,0,1$, of 54209ffcf6adbb64, where $K_r=\{x_1,x_2\ge0:h\le x_1+x_2\le r\}$, $h=20/97$, $e=1/100$, and $t=100/291$. Their unique globally deepest mixed mark is $Y=(0,t,t)$, of raw depth $Q=18200/28227$ and total mass $M=135144409/94090000$. Use the three proper critical caps
$$
H_1=\{x_1+x_2\le2t\},\qquad
H_2=\{tx_1+(3t-1)x_2-et z\ge t(4t-1)\},
$$
and $H_3$ obtained from $H_2$ by swapping the continuous coordinates. Their coarea-normalized response weights are $(109,100,100)/309$. The ordinary centroid coordinate in $K_r$ is $r/3+h^2/[3(r+h)]$, so the centroid graph is nonaffine.

The optimal projective parameter of the middle fiber at $(t,t)$ is $(c,c)$, where
$$
c=\frac{44426-1067\sqrt{1702}}{25480}
\quad\text{and}\quad \frac{15957301}{10^9}<c<\frac{15957302}{10^9}.
$$
The energy tangent chart of d7ff9f9aad2b6512 has base coefficient $b_E=e[1+c(1-2t)]^{-3}/(3E)>0$, where $E$ is the middle marked projective energy. Every nonnegative combination of the displayed cap normals with continuous component $(c,c)$ has coefficients $( (4t-1)s-c,s,s )$ for $s\ge c/(4t-1)>0$, and has base component $-2ets$. Its residual base coefficient relative to the energy chart is therefore $b_E+2ets>0$. The whole mixed body has base moment $2e$, while each of the three critical cap sections has zero summed base coarea moment.

## Proof

The exact actual fibers, mass, global depth and three proper critical caps follow from 54209ffcf6adbb64 at its stated parameters. The endpoint caps isolate fibers of strictly smaller mass than $Q$. At any other middle mark some cap margin is strictly positive, since the continuous normals span $\mathbb R^2$ and their positive dependence has coefficients $(4t-1,1,1)$. Raising the threshold of this cap slightly while retaining the mark removes a strip of positive area from its old proper middle cut. This excludes a second deepest mark.

The first cap section is the same on all three fibers, and the other two sections are translates of their middle sections by the endpoint translations in the predecessor. Divide section length by the norm of the displayed continuous normal to obtain coarea. For $H_1$ this gives $2t$ per fiber. For $H_2$ the middle cut endpoints $(4t-1,0)$ and $(1-2t,2t)$ differ by $2(-(3t-1),t)$, giving coarea $2$, and the same holds for $H_3$. The total coareas are $6t,6,6$. Dividing the positive normal relation by these coareas and normalizing the coefficients gives the asserted weights. Equal coareas across the three bases give zero summed base coarea moment for each cap. The whole-body moment is $|K_{1+e}|-|K_{1-e}|=2e$. Integrating the triangle sections gives $|K_r|=(r^2-h^2)/2$ and each unnormalized coordinate moment $(r^3-h^3)/6$. Their ratio yields the displayed centroid coordinate, whose second derivative is $2h^2/[3(r+h)^3]>0$.

By strict uniqueness and coordinate-swap invariance in d90ba05577427854, the minimizing parameter has the form $(c,c)$. With $u=x_1+x_2$ the stationary equation along this diagonal is
$$
\int_h^1\frac{u(u-2t)}{[1+c(u-2t)]^4}\,du=0.
$$
Indeed the marginal area in $u$ is $u\,du$. To evaluate the integral, let $A=h-2t=-140/291$, $B=1-2t=91/291$ and change variable to $v=(u-2t)/(1+c(u-2t))$. Its integrand becomes $v(2t+(1-2tc)v)\,dv$. Divide the integrated difference by $(v(B)-v(A))/3>0$, where $v(A)=A/(1+cA)$ and $v(B)=B/(1+cB)$. Clearing the positive denominator $(1+cA)^2(1+cB)^2$ gives
$$
3t(X+2cJ)(1+cX+c^2J)+(1-2tc)(X^2-J+3cJX+3c^2J^2),
\qquad X=A+B,\quad J=AB .
$$
The cubic terms cancel. Substitution yields $49(509600c^2-1777040c+28227)/265587843$. The smaller root is the stated radical. The polynomial has opposite signs, positive then negative, at the two rational bounds in the statement and is strictly decreasing between them. This root is admissible because $0<c<1/50$ and $|u-2t|<1$ on $[h,1]$. Swap symmetry makes the two coordinate derivatives equal, so the diagonal stationary equation implies full stationarity. Strict convexity gives the asserted parameter.

At each real base $z\in[-1,1]$ the real fiber $K_{1+ez}$ is the corresponding convex combination of the endpoint fibers. This follows by interpolating each of their four vertices and using the defining halfspaces for the reverse inclusion. Thus this is the canonical hull required in d7ff9f9aad2b6512. Near the middle base with mark $(t,t)$ fixed, the objective is smooth in $z$ and in the parameter near the positive optimizing denominator. One can see smoothness by integrating $u$ from $h$ to $1+ez$ and the first coordinate from $0$ to $u$. The parameter Hessian is positive definite as in d90ba05577427854. The implicit function theorem gives a smooth stationary branch which, by strict convexity, consists of the minimizers. Differentiating the attained energy leaves only the partial derivative in $z$, since its parameter gradient vanishes. At the old symmetric parameter this derivative is $e[1+c(1-2t)]^{-3}$. The normalized base derivative of $E^{1/2}$ is this value divided by $2E$. At the interior base both signs are available, so every energy supergradient has that normalized base derivative. The positive chart of d7ff9f9aad2b6512 multiplies it by $2/3$, giving $b_E$.

Subtract the two continuous coordinates in a representation of $(c,c)$ by the three cap normals. Since $t-(3t-1)=1-2t>0$, the two coefficients of $H_2,H_3$ coincide. Solving either coordinate gives the displayed coefficients and their nonnegativity condition. Only those two caps have nonzero base component, both equal to $-et$. The base work difference is therefore $b_E+2ets>0$.
