---
fact_id: eec4218faa0ffa76
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-three-interval-sharp-fixed-endpoint-ratio
depends_on: ["c680a307d3f26cec"]
verifier_run: eec52aae56f10ca7
target_match: null
---

## Source

- [5048c7e97ca98aef](../candidates/5048c7e97ca98aef.json), §1 (5), §4 (8) and optimization, §5.

## Statement

Fix an endpoint ratio $r=a/b\in(0,1]$ in the three-positive-interval model of the preceding exact depth formula. Among all convex bodies with only these three nonempty integer fibers and with this endpoint ratio, the minimum of the normalized global maximum depth $Q/(a+b+U)$ is
$$
B(r)=
\begin{cases}
1/(4-2r),&0<r\le1/5,\\
(1+5r)/(6(1+r)),&1/5\le r\le1/3,\\
(1+3r)/(4+6r),&1/3\le r\le1 .
\end{cases}
$$
In the normalized coordinates with endpoint lengths $a\le b$, the complete set of minimizing middle parameters is as follows.
- For $0<r<1/5$, take $U=b-2a$ and any compatible $s$.
- For $1/5\le r<1/3$, take $U=(a+b)/2$ and $s=0$.
- For $r=1/3$, take either $U=(a+b)/2$ and $s=0$ or $U=b+2a$ and $|s|=U/2-(a+b)/4$.
- For $1/3<r\le1$, take $U=b+2a$ and $|s|=U/2-(a+b)/4$.

The function $B$ is continuous and strictly increasing, satisfies $B(r)>1/4$ for $r>0$, has limit $1/4$ as $r\downarrow0$, and has $B(1)=2/5$. Thus the unrestricted infimum within this three-positive-interval model is $1/4$, approached as the ratio tends to zero.

## Proof

The positive-length, midpoint-compatible hypotheses are exactly those of the preceding depth formula. At fixed $a,b,U$, its monotonicity in $|s|$ shows that the smallest normalized value is attained at a contact shift. There it is $\max\{b/2,F_{\mathrm{contact}}(a,b,U)\}/(a+b+U)$. All lengths scale by the same factor under a common height dilation, so divide by $b$ and write $b=1$, $a=r$. Put $T=1+r+U$.

On the first range $(1+r)/2\le U\le1$, the numerator is $\max\{1/2,U/2+r\}$. Its two terms cross at $U=1-2r$, which lies in this range exactly when $r\le1/5$. The quotient is strictly decreasing in $U$ while the numerator is $1/2$. When the numerator is $U/2+r$, the derivative is $(1-r)/(2T^2)$. This is strictly positive for $r<1$, and at $r=1$ the first range is a singleton. Thus the unique minimizing $U$ in this range is $1-2r$ for $r\le1/5$ and $(1+r)/2$ for $r\ge1/5$, with the same $U$ at equality. The corresponding quotient values are $1/(4-2r)$ and $(1+5r)/(6(1+r))$.

On the second range $1\le U\le1+2r$, the numerator $(U+1)/4+r$ is strictly larger than $1/2$ and the derivative of the quotient is $-3r/(4T^2)<0$. On the third range $U\ge1+2r$, the numerator $(U+r)/2$ is also strictly larger than $1/2$ and the derivative is $1/(2T^2)>0$. Thus across these two ranges the unique minimizing $U$ is $1+2r$, where the value is $(1+3r)/(4+6r)$.

For $r\le1/5$, the third-range candidate minus $1/(4-2r)$ has numerator $2r(2-3r)>0$ over the positive product of their denominators. For $r\ge1/5$, the third-range candidate minus $(1+5r)/(6(1+r))$ has numerator $2(1-3r)(1+2r)$ over the positive product. This gives the stated piecewise value and the two minimizing lengths exactly at $r=1/3$.

For $U\le b$ the entire feasible range of $|s|$ lies in the constant first branch of $F$, so any compatible shift attains the minimum at $U=b-2a$. At $U=(a+b)/2$ compatibility forces $s=0$. At $U=b+2a$ the contact shift has magnitude $(b+3a)/4$, the upper seam of the strictly decreasing branch. Every smaller magnitude gives a larger $F$, and $F>b/2$ for this $U$. Hence a contact shift is necessary at this length. Compatibility realizes all listed choices by the lifted convex hull.

The three expressions for $B$ agree at their seams and have strictly positive derivatives in the interiors of their respective ranges. The first tends to $1/4$ as $r\downarrow0$ and the last gives $2/5$ at $r=1$. The excesses over $1/4$ are respectively $r/(8-4r)$, $(7r-1)/(12(1+r))$, and $3r/(8+12r)$, all strictly positive on the stated ranges. The limiting assertion uses only positive $r$ and the same one-dimensional mixed measure.
