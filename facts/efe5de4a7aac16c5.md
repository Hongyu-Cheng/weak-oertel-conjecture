---
fact_id: efe5de4a7aac16c5
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w35-sweeps-six-ray-formal-weights
depends_on: []
verifier_run: f6d7b69ba4a3eea1
target_match: null
---

## Source

- [fcbc840f56d4b6b6](../candidates/fcbc840f56d4b6b6.json), fcbc840f56d4b6b6:01 §1, exact normalized scalar screen certificate.
- [28c45f4fbd3dc45b](../candidates/28c45f4fbd3dc45b.json), 28c45f4fbd3dc45b:02 §1, formal endpoint-section array.

## Statement

Let $T=\{x:x_1\le1,\ x_2\le1,\ x_1+x_2\ge-1\}$, let $K=r(-T)$, and use the three normals $v_i=(1,0),(0,1),(-1,-1)$ at the middle mark $0$. In direction $Jv_i$ for a quarter turn $J$, each middle chord has length parameter $k_i=2r$, center $c_i=0$, and rays of length parameter $r$. The middle area is $k=9r^2/2$, with each actual middle cap of area $q_i=2r^2$. For assigned endpoint chord lengths $a_i$, set $s_i=k_i+2a_i$, $\Lambda=\sum_i1/s_i$, $p_i=1/(\Lambda s_i)$ and $t_i=a_i/s_i$.

For $r=501/404$, assign $(a_1,a_2,a_3)=(r,r/100,r/100)$ and independent endpoint area $a=r^2/100$. Then $\Lambda=1$, $p=(101,200,200)/501$ with $\min p_i<2/9$, and $t=(1/4,1/202,1/202)$. The strict center bounds $|c_i|<a_i(k_i-a_i)/s_i$, strict six-ray convexity comparisons, and the following screen all hold: $q_i/k=4/9<c=128/279$, $q_{\min}+q_{\rm mid}+q_{\max}/4=k$, the six-ray core has area $3r^2<k$ with double-sector total $D_{\rm core}=3r^2/2$, and $4D_{\rm core}/(3c)<k$. Each two-line unique-sector envelope has area $E_i=r^2$ with $(1-2c)k<E_i-r^2/2$, where the subtracted area is the opposite double-sector core triangle. Also $a>a_i a_j/2$ for every pair $i\ne j$ and $a/k=1/450<1/31$.

In a separate unscaled formal array $r=1$ and $(a_1,a_2,a_3)=(2,0,0)$, the weak center bounds hold, the same middle caps and tight profile hold, and $p=(1,3,3)/7$, $t=(1/3,0,0)$. In neither example are the assigned endpoint sections required to be realized by a compatible critical endpoint fiber.

## Proof

The middle triangle has vertices $r(-1,-1)$, $r(2,-1)$, $r(-1,2)$, so its area is $9r^2/2$. For each of the three caps the captured triangle has area $2r^2$ by direct clipping (or cyclic symmetry under $(x_1,x_2)\mapsto(x_2,-x_1-x_2)$), and the chord parameters are $\pm r$ in the basis $Jv_i$. The caps therefore satisfy the displayed ordinary profile exactly. The ray hull has cyclic vertices $r(1,0),r(0,1),r(-1,1),r(-1,0),r(0,-1),r(1,-1)$. Each successive determinant has magnitude $r^2$, so the six triangles from the origin have area $r^2/2$ apiece, with three double and three unique sectors. The sum of the two neighboring ray vertices equals the middle vertex, so the chord between the neighbors meets the middle ray at half its radial parameter, proving the strict ray comparisons.

For the unique sector $x_1,x_2\le0$, write a point as $(-u,-v)$ with $u,v\ge0$. The actual chords to $(r,-r)$ and $(-r,r)$, respectively, cross the vertical and horizontal axes at $-r(u+v)/(r+u)$ and $-r(u+v)/(r+v)$. Since the actual negative intercepts are both $-r$, these give $v\le r$ and $u\le r$. Thus the two-line envelope is the coordinate square of side $r$ in this quadrant and has area $r^2$. Cyclic coordinate changes of determinant one give the other two areas. The opposite double-sector core triangle has area $r^2/2$. Substitution gives $4D_{\rm core}/(3c)=(279/64)r^2<(9/2)r^2$ and $(1-2c)k=(23/62)r^2<r^2/2$.

For the first array the inverses at $r=1$ are $1/4,50/101,50/101$ with sum $501/404$. Scaling by that sum gives $\Lambda=1$ and the stated $p,t$. Then $\min p_i=101/501<2/9$. The center bounds are strict since $0<a_i<k_i$, and the largest $a_i a_j/2$ is $r^2/200<a$. For the second array $s=(6,2,2)$, which gives the asserted inverse weights and $t$; since $0\le a_i\le k_i$ and centers vanish the non-strict inequalities hold.
