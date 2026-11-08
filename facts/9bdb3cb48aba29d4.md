---
fact_id: 9bdb3cb48aba29d4
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-one-apex-mass-dependent-centroid-surplus
depends_on: ["54914cbd1c766b42", "56bee7482878022f"]
verifier_run: 8228baefd8cb64d5
target_match: null
---

## Source

- [b29a253caa27d987](../candidates/b29a253caa27d987.json), b29a253caa27d987:10 §8 (14)–(17) and final axial-coverage paragraph.

## Statement

Let $M$ be a rectangle of area $m$ and $K$ its convex hull with one point on the perpendicular bisector of a side strictly beyond that side. For $1\le m\le4/3$ and $35/12\le k=|K|\le3$, the ordinary raw depth at the uniform centroid $g_K$ is
$$
\min\left\{\frac{(8k^2-4km-m^2)^2}{144k^2(k-m)},\
\frac{32k^3+3km^2+m^3}{72k^2}\right\}>\frac{k+1}{3}.
$$
This lower bound also holds for the mixed raw depth at $(0,g_K)$ whenever $K$ is an actual middle fiber. In the reciprocal-width rectangle family with unit-area endpoints, take this same type of one-apex enlargement of the midpoint rectangle $M_R$, with $k\le3$. If its displayed axial threshold comparison $J_R<(k+1)/3$ holds, then the above parameter conditions hold and $(0,g_K)$ pays the strict edge bound.

## Proof

Use independent affine rescalings along the perpendicular bisector and its transverse direction to make the apex triangle the part $0\le X\le1$ of $P_w$. This part has area one, so the inverse area factor is $k-m$ and $w=1+m/[2(k-m)]$. The parameter bounds give $w\le27/19<1+1/\sqrt3$. Substitute into the exact ordinary centroid depth of $P_w$ and multiply both entries by $k-m$. In this substitution $g=(8k^2-4km-m^2)/[12k(k-m)]$ and $2g-w=(2k+m)/(6k)$. This gives the displayed expressions.

After subtracting $(k+1)/3$ the two numerators over the same positive denominators are
$$
N_1=16k^4-16k^3m-48k^3+48k^2m+8km^3+m^4,\qquad
N_2=8k^3-24k^2+3km^2+m^3.
$$
Both partial derivatives of $N_2$ are positive on the rectangle because $k>2$. Also $\partial_m N_1=16k^2(3-k)+24km^2+4m^3>0$, and
$$
(\partial_k N_1)/8=k^2(8k-18-6m)+12km+m^3\ge-24+35+m^3>0.
$$
The latter uses $8k-18-6m\ge-8/3$, $k^2\le9$, and $12km\ge35$. At $(m,k)=(1,35/12)$ the values are $3361/1296$ and $881/216$. Each ambient containing halfspace retains at least its ordinary containing trace in $K$, including the whole fiber for a purely integer normal.

For the reciprocal rectangle family the axial cut retains the same middle area at its minimizing tilt when the added triangle is attached to the left axial side of $M_R$. More generally midpoint containment makes every actual axial cap at least the rectangle family's minimum $J_R$, so any actual axial shortfall implies the comparison used here. Since $J_R<(k+1)/3\le4/3$, the exact rectangle formula gives $5/3<R<3$ and $1\le m_R=(R+2+1/R)/4\le4/3$. Also $k>3J_R-1\ge(5+3\sqrt5)/4>35/12$, by its minimum over $R$. Thus the shape-dependent estimate applies.
