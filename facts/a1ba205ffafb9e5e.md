---
fact_id: a1ba205ffafb9e5e
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-balanced-extraction-enlargement-slack-budget
depends_on: []
verifier_run: 8b100286942ada04
target_match: null
---

## Source

- [149b5f35c717786d](../candidates/149b5f35c717786d.json), 149b5f35c717786d:06 Proof §6, (14)–(16).

## Statement

Use summed $d$-volume, $d\ge1$, on the integer fibers of ambient convex bodies inside a common source. Suppose $D'$ enlarges each positive fiber of $D$, adds mass $\delta\ge0$ to mass $m>0$, and has the same true integer centroid base $j$ as $D$. Write $(j,c)$ for the original centroid. Let $R_0$ bound $\|x-c\|$ on the added mixed mass and let $L_0$ bound the sum, over original positive fibers, of their respective maximal $(d-1)$-dimensional section volumes, using counting at $d=1$. For an old feasible threshold $\beta$ put
$
\sigma=\inf_{H\ni(j,c)}[\mu_D(H)-\beta m].
$
The enlarged body remains feasible whenever $\beta\delta+L_0R_0\delta/(m+\delta)\le\sigma$. In particular, a mass maximizer admitting integer-balanced enlargements of arbitrarily small positive mass addition must have $\sigma=0$.

## Proof

Write $c'$ for the new continuous centroid. The mixed measure of $D'$ dominates that of $D$; their difference $\nu$ has mass $\delta$. Subtracting first moments gives $c'-c=\int(x-c)\,d\nu/(m+\delta)$, so $\|c'-c\|\le R_0\delta/(m+\delta)$. It suffices to test caps through the new centroid. With a nonzero continuous normal normalize it to norm one and translate the cap parallel to pass through the original centroid. The changed threshold on every fiber moves by at most $\|c'-c\|$, independently of the base tilt. Fubini bounds lost old mass by $L_0\|c'-c\|$. With a pure-base normal both thresholds are equal. The old through-mark cap has mass at least $\beta m+\sigma$ and added mass is nonnegative. Thus each new cap has mass at least $\beta m+\sigma-L_0R_0\delta/(m+\delta)$, proving the sufficient condition. If arbitrarily small positive additions are possible inside the fixed bounded source, take a common finite $R_0$. For $\sigma>0$ a sufficiently small positive addition then gives a larger feasible extraction, contradicting maximality.
