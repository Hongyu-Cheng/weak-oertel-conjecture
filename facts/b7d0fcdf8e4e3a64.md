---
fact_id: b7d0fcdf8e4e3a64
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-sharp-parity-midpoint-density-and-class-cap-constants
depends_on: ["ce6f5ea7607bbbd2"]
verifier_run: ad85f7eab61b9262
target_match: null
---

## Source

- [9af97e78b545b0b8](../candidates/9af97e78b545b0b8.json), 9af97e78b545b0b8:04 §5, optimality of the density and separate-class cap constants.

## Statement

For parity-conditioned midpoint transport with original class masses and independent ordered base pairs within a class, the pooled density bound $2^n\mu$ is sharp for each $n,d\ge1$ among class outputs satisfying $\eta_r\le\mu$. On $C=[0,2]^n\times K$ with a convex $d$-body $K$ of volume $a>0$, the pooled density is exactly $2^n$ on the fiber at $(1,\ldots,1)$, relative to its Lebesgue volume. The constant $2$ in the separate-class bound $\eta_r(H)\le2\mu_r(H)$ is also sharp as a supremum, for every $d\ge1$ already with one integer coordinate.

## Proof

The simultaneous density and cap transport theorem supplies the upper bounds with the indicated base law. For the product example, the complete integer base set is $\{0,1,2\}^n$ and all its fibers are copies of $K$. A parity class with $s$ even coordinates has $2^s$ bases of equal weight and total mass $2^s a$. Each of its bases has exactly one reflected partner about $k=(1,\ldots,1)$ in the class, including the class with $s=0$. Hence its independent ordered pair has midpoint $k$ with probability $2^{-s}$. The class output has mass $a$ at $k$, and because it is dominated there by Lebesgue measure on $K$, its restriction equals that measure. All $2^n$ class outputs have this restriction, giving the claimed exact pooled density.

For the cap constant in one integer coordinate take the convex hull of homothetic convex $d$-bodies of positive volumes $A,b$ lifted to bases $0,2$. The only other integer fiber is their Minkowski midpoint at base $1$, in the odd class. In the even class the independent ordered pairs yielding a midpoint in the closed halfspace $z\ge1$ have weights $Ab,Ab,b^2$ before class normalization. The even-class input has mass $b$ there and the output mass is $(2Ab+b^2)/(A+b)$. Their ratio tends to $2$ as $b/A\downarrow0$. This calculation uses only the base law, so it holds for every conditional continuous coupling used by the construction.
