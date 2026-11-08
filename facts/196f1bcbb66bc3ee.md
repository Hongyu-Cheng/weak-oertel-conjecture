---
fact_id: 196f1bcbb66bc3ee
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-opposite-adjacent-centroid-partitions-fail
depends_on: []
verifier_run: 00ba1a95911d1a23
target_match: null
---

## Source

- [4dd47d721f3f1640](../candidates/4dd47d721f3f1640.json), 4dd47d721f3f1640:01 §§1–3, moment extrema, complements, and all four actual cap witnesses.

## Statement

Let $C=[-1,2]\times[0,1]$, with $\mu$ equal to the sum of lengths on its four integer fibers. For measurable $0\le f\le1$ with $\int f\,d\mu=2$ and $\int zf\,d\mu=2$, the possible continuous centroid coordinates $\tfrac12\int xf\,d\mu$ form $[3/10,7/10]$. The unique extremal sources up to null sets are the indicators of $x-z/5\le2/5$ and $x+z/5\ge3/5$, respectively. The exposed-source centroids and their complementary-source centroids are $(1,3/10),(1,7/10),(0,7/10),(0,3/10)$. All four have normalized depth in the original mixed measure at most $9/40<1/4$.

## Proof

The cap $H_+=\{x+z/5\ge3/5\}$ retains lengths $(1/5,2/5,3/5,4/5)$ at bases $-1,0,1,2$. Their sum is two and their base moment is $-1/5+3/5+8/5=2$. A retained upper interval of length $m$ has continuous moment $m-m^2/2$. Summing gives $7/5$, so the centroid is $(1,7/10)$.

Let $L=x+z/5-3/5$. For every feasible $f$ the function $L(\mathbf1_{H_+}-f)$ is pointwise nonnegative. In its integral the mass and base terms cancel by feasibility, leaving $\int_{H_+} x\,d\mu-\int xf\,d\mu\ge0$. Equality requires $f=\mathbf1_{H_+}$ except on a null set, since $L=0$ meets each fiber in one point. Reflection $x\mapsto1-x$ preserves feasibility and gives the unique minimum, the cap $x-z/5\le2/5$ with continuous centroid $3/10$. Convex mixtures of the two indicators fill the interval. The original source has total mass four, base moment two and continuous moment two. Thus each complement has mass two, base moment zero and continuous centroid one minus that of its source. The two closed complementary caps meet only along the corresponding level line of zero mixed length.

The halfspace $x+(3/10)z\ge1$ contains $(1,7/10)$ and retains lengths $(0,0,3/10,3/5)$, with a length-zero singleton at base zero. Its normalized mass is $(9/10)/4=9/40$. The affine reflections $x\mapsto1-x$ and $z\mapsto1-z$ preserve the entire mixed measure and the family of closed halfspaces. They carry this point to all three other candidates and transport the same bound.
