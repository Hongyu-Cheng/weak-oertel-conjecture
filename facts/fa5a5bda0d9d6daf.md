---
fact_id: fa5a5bda0d9d6daf
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w32-explicit-shared-triangle-fixed-cap-escape
depends_on: ["e42e4ad8eaa4f705", "2acc8bc803acf1c0"]
verifier_run: 348d1fc043d544dc
target_match: null
---

## Source

- [3ff8967854167565](../candidates/3ff8967854167565.json), 3ff8967854167565:02 §3, (9)–(13), explicit shared-budget two-fiber improvement.

## Statement

Put a copy of $T=\operatorname{conv}\{(0,0),(1,0),(0,1)\}$ at each of the integer bases $0,1$. Fix the three cylindrical caps with continuous margins $2/3-x-y,\ x-1/3,\ y-1/3$. The reference total area is $1$ and each total cap budget is $4/9$; the objective-one first stress has all three multipliers $3/4$. For $0<t\le1/10$ put $q=t^2/3$, $L=1+7t^2/18$ and replace the two actual fibers by
$$
T_\pm(t)=\operatorname{conv}\{(q\pm t,q\pm t),(L,0),(0,L)\}.
$$
The same fixed caps still cover both entire planes, each has mass strictly below $4/9$, and the actual total area is $1+t^2/9-35t^4/324>1$. The total area and cap first derivatives at zero vanish, and the aggregate Lagrangian second derivative is $2/3$. At $t=1/10$ the total area and the three cap masses are $648713/648000$, $685451117/1546212500$, and $923058069551/2080858248000$ for each of the last two caps. The three initial budgets exceed the actual initial maximum raw mixed depth $2/9$.

## Proof

The convex hull of the two displayed lifted triangles has precisely the displayed integer fibers because they are the exposed endpoints at consecutive bases. The caps cover the plane because if $x<1/3$ and $y<1/3$ then $x+y<2/3$. The reference triangle has each cap area $2/9$ by its two edge ratios $2/3$. These are the canonical fixed barycentric caps in e42e4ad8eaa4f705, with $d=2$ and $V=1/2$, so the objective-one multiplier is $3/4$ for each cap and this stationarity adds over both triangles. The opposite first velocities at their first vertices cancel every total derivative. The reference depth $2/9$ follows from the exposed-product simplex case of 2acc8bc803acf1c0.

Throughout the asserted interval, $q+t<1/3<L$, $L>2/3$ and $L-2(q+t)>0$. Thus the determinant has positive sign and each cap keeps exactly its designated vertex, with strict margins. The area of one triangle with first vertex $(h,h)$ is $L(L-2h)/2$; summing gives $M=L(L-2q)$ and its claimed polynomial. Dividing the retained vertex margin by each of the two edge margin differences and multiplying the resulting ratios by the triangle area gives the exact summed masses
$$
\begin{aligned}
C_0&=\sum_{\sigma=\pm1}\frac{L(2/3-2(q+\sigma t))^2}{2(L-2(q+\sigma t))},\\
C_1=C_2&=\sum_{\sigma=\pm1}\frac{(L-2(q+\sigma t))(L-1/3)^2}{2(L-q-\sigma t)}.
\end{aligned}
$$
Substitution and collecting common denominators gives
$$
\begin{aligned}
\tfrac49-C_0
&=\frac{4t^2(35t^6-1303t^4-2892t^2+108)}
{9(5t^2-36t-18)(5t^2+36t-18)},\\
\tfrac49-C_1
&=\frac{t^2(245t^6+36120t^4+105948t^2+7776)}
{324(t^2-18t+18)(t^2+18t+18)}.
\end{aligned}
$$
Both factors of the first denominator product are negative and both factors of the second are positive on this interval. The first numerator polynomial in parentheses is at least $108-2892/100-1303/10000=789497/10000>0$, and the second has positive coefficients. The polynomial for $M$ has strictly positive gain there. At $t=1/10$ these exact formulas give the stated rational values. Taking the coefficients of $t^2$ in the area and cap gaps gives $M=1+t^2/9+O(t^4)$, $C_0=4/9-4t^2/27+O(t^4)$, and $C_1=C_2=4/9-2t^2/27+O(t^4)$. Hence the coefficient of $t^2$ in the Lagrangian is $1/3$, and its second derivative is $2/3$.
