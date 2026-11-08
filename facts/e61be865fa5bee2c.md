---
fact_id: e61be865fa5bee2c
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-planar-grid-hull-exact-trapezoid-mass
depends_on: []
verifier_run: 279127c7f6af54ad
target_match: null
---

## Source

- [f525b2b4bb53c54e](../candidates/f525b2b4bb53c54e.json), f525b2b4bb53c54e:7 §3, (8)–(11), exact planar area.
- [f525b2b4bb53c54e](../candidates/f525b2b4bb53c54e.json), f525b2b4bb53c54e:6 §3, adjacent interval interpolation.

## Statement

Let $G=t+h\mathbb Z$, $h>0$, and let $Q\subset\mathbb R_u\times\mathbb R_x$ be nonempty, compact and convex, with $Q=\operatorname{conv}(Q\cap(G\times\mathbb R))$. Its nonempty grid fibers have consecutive indices $j=a,\ldots,b$. Write $N=b-a+1$, their lengths $w_j\ge0$, $T=\sum_jw_j$, and $E=(w_a+w_b)/2$, counting the same endpoint twice if $N=1$. Then $|Q|_2=h(T-E)$. If $N\ge2$, then $T\ge NE$ and $(1-1/N)T\le|Q|_2/h\le T$, so $T\le2|Q|_2/h$. Affine widths attain the lower inequality and zero endpoint widths attain the upper one.

## Proof

The projection is the hull of the finitely many nonempty sampled bases, with both endpoints on the grid. Every intervening sampled fiber is nonempty by convexity. At $N=1$ the hull is a single interval with zero area and $E=T$.

For $N\ge2$ write the sampled intervals as $[\ell_j,r_j]$, permitting equal endpoints. Convexity makes the consecutive slopes of $\ell_j$ nondecreasing and those of $r_j$ nonincreasing. Their piecewise affine interpolants therefore bound a convex region containing the sampled sections. Each strip of the region is exactly the hull of its two adjacent sections, so it lies in $Q$. The grid-hull assumption gives the reverse inclusion. The strip width is affine and Fubini gives strip area $h(w_j+w_{j+1})/2$. Summing yields the claimed identity.

The widths form a concave sequence. Summing the pointwise lower bound by the affine chord joining its two endpoint widths gives $T\ge N(w_a+w_b)/2$. Combining this with $E\ge0$ proves the bounds. Affine widths give equality in the chord sum, and $E=0$ when both endpoints have zero width.
