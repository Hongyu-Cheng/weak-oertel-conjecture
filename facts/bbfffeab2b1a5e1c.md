---
fact_id: bbfffeab2b1a5e1c
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-eight-base-revised-independent-patch-budget-obstruction
depends_on: ["ae4e01ead61ea9c3"]
verifier_run: aaf1959b7851b33b
target_match: null
---

## Source

- [f1f97e5764053b3f](../candidates/f1f97e5764053b3f.json), §3, revised radius, inherited faces, and independent patch gap.
- [39e0ea36e1546d5b](../candidates/39e0ea36e1546d5b.json), §4, (9)–(15), same revised construction and strict budget failure.

## Statement

Let $p_0,\ldots,p_7$ in order be $(-1,-2),(-1,-1),(-1,0),(0,0),(0,1),(0,2),(1,2),(2,3)$, $Q=\operatorname{conv}\lbrace p_0,p_2,p_5,p_7\rbrace$, and
$$
r(z)=\min\lbrace1+z_2/4,\ 17/25-(8/25)z_1\rbrace,\qquad
C=\lbrace(z,x): z\in Q,\ 0\le x\le r(z)\rbrace.
$$
Then $C$ is a full-dimensional compact convex body with exactly these eight positive integer fibers, whose lengths are $(50,75,100,68,68,68,36,4)/100$. The volume-maximal parity roots, with minimum Euclidean norm breaking the sole tie, are $2,1,3,4$ in parities $(1,0),(1,1),(0,0),(0,1)$, respectively. The four exact Minkowski midpoint edges $0\to1,5\to4,6\to4,7\to6$ have partners $2,3,2,4$. In the lifted radius hull the corresponding root faces at $1,2,3,4$ have index sets $E=\lbrace0,1,2\rbrace$, $\lbrace2\rbrace$, $\lbrace3\rbrace$, and $F=\lbrace2,3,4,5,6,7\rbrace$, with exact relative Helly numbers $2,1,1,3$. Their projections are lattice-complete. Their patch masses in hundredth units are $225,100,68,344$, with overlap $E\cap F=\lbrace2\rbrace$ of mass $100$ and total $469$. Even giving each patch its full overlap mass, the maximum independent guarantee $W_{\rm face}/h({\rm face})$ is $344/3<469/4$ in hundredth units, a strict shortfall of $31/1200$ in actual interval mass. This refutes the inference that some individual root-face guarantee must reach one quarter of the total.

## Proof

The polygon and its eight integer sites are those in the declared original upper-face lemma. The minimum of two affine functions is concave; direct substitution gives the listed eight radii, with smallest value $1/25$ attained at the vertex $p_7$. Concavity makes this a lower bound throughout $Q$. The hypograph bounded below by $x=0$ is consequently full-dimensional, compact, and convex, and gives exactly the stated integer intervals.

The parity classes in the displayed order are $\lbrace0,2,6\rbrace$, $\lbrace1\rbrace$, $\lbrace3,5\rbrace$, and $\lbrace4,7\rbrace$. The width list shows strict maxima except for $3,5$, and $\|p_3\|=0<\|p_5\|=2$. The coordinates give the four designated base midpoints, and the respective width equalities in hundredth units are $50+100=2(75)$, $68+68=2(68)$, $36+100=2(68)$, and $4+68=2(36)$. For intervals with common left endpoint zero these identities give exact Minkowski midpoint equalities. Every nonroot reaches a root along these edges.

To transfer the face calculation, write $t_i=t(p_i)$ for the old heights in the declared upper-face lemma and $\widetilde t_i=100r(p_i)$. The two height lists satisfy $7\widetilde t_i=76-274(p_i)_1+100(p_i)_2+25t_i$ for each $i$. The associated affine map fixes the base and has positive height coefficient, so it is invertible and carries upper supporting planes, all faces, their projected lattices and the relative Helly numbers to the corresponding new ones. Thus the old lemma gives exactly the stated root faces in the revised profile. For these interval fibers the centroid graph is itself affinely isomorphic to the radius graph via $(z,r)\mapsto(z,r/2)$, so the same relative Helly numbers apply to the patch centroid sets.

The four stated patch sums follow from the width list. The two maximal patches cover all points and their overlap has weight $100$, giving $225+344-100=469$. The largest of $225/2,100,68,344/3$ is $344/3$, and $469/4-344/3=31/12$ in hundredth units. Thus the independently guaranteed scores fail to pay the quarter budget even before any overlap weight is removed. This is a bound on the prescribed scores, with no upper bound claimed on actual cap depth.
