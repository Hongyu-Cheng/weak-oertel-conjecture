---
fact_id: e49b3faee87f1dff
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-actual-own-depth-capacity-obstruction
depends_on: ["7f0686c3a3a5d6d7"]
verifier_run: cbd5f1d8a21b3b3b
target_match: null
---

## Source

- [325d279c18e3a49e](../candidates/325d279c18e3a49e.json), 325d279c18e3a49e:02 §§1, 3–5, (1), (3)–(10), using §2.

## Statement

Let $T=\operatorname{conv}(0,(1,0),(0,1))$, $U=\operatorname{conv}(0,(4/5,0),(0,8/25))$, $\eta=2^{-20}$ and $s=3/128+\eta$. Let $C$ be the hull of the lifts of $K_-=(2-s)U$, $K_0=T$ and $K_+=sU$ at bases $-1,0,1$. These are its three actual positive integer fibers. For an ambient closed halfspace $H$, define $\nu(H)=\sum_{j=-1}^1 \sup\{f_{K_j}(x):x\in K_j,\ (j,x)\in H\}$, with empty suprema zero and $f_{K_j}$ the raw ordinary depth in $K_j$. Set $A(K)=\max_K f_K$. Then the maximum of $\inf_{H\ni y}\nu(H)$ over actual mixed points $y$ equals $(4/9)|K_-|$, strictly below $\tfrac12\sum_j A(K_j)$ by exactly $1/9216000$. Every $\nu(H)$ is at most the actual mixed area captured by $H$.

## Proof

The two outer bases are extreme. Their Minkowski average is $U\subset T$, so at base zero every convex combination of lifted points lies in $T$ by grouping the two outer terms. The projection is $[-1,1]$ and the hull has interior because both endpoint triangles have interior in their parallel fiber planes. Each nonempty fiber trace of $H$ is a halfplane cap or the entire fiber and bounds the depth of all its points by its area. This proves the last assertion.

Write $a=|K_-|$, $b=|K_+|$, $c=|T|=1/2$, $\gamma=4/9$, $e=(32/125)s^2$ and $\delta=(128/125)\eta$. Scaling areas gives $b/c=e$, $a/c=1+e-\delta$ and $(a+b+c)/c=2+2e-\delta$. Here $e>(32/125)(3/128)^2=9/64000>\delta=1/1024000$, and $s<1$ gives $b<c$. Thus $a>c>b$, and the preceding triangle lemma gives $A(K_j)=\gamma |K_j|$ on all three fibers. The target exceeds $\gamma a$ by $\gamma c\delta/2=1/9216000$.

Put $k=2/3-\eta$, $p=1-k$, $h=13/40$ and $B=(8/25)(1-s)$. The three closed caps
$$
H_A=\{y+Bz\ge h\},\qquad
H_B=\{x+y-2z\le k\},\qquad
H_C=\{x+2z\ge p\}
$$
cover the middle triangle, since a point there outside $H_A$ and $H_C$ has $x+y<p+h<k$, with $k-p-h=1/120-2\eta>0$. At both endpoint bases the maximum of $y+Bz$ is $8/25<h$, and on the middle trace $y\ge h$ the centroid is included. Thus $\nu(H_A)=\gamma c<\gamma a$.

In $H_B$ the left fiber is excluded since its minimum of $x+y-2z$ is $2>k$, and the right fiber is included since its maximum is $(4/5)s-2<k$. In $H_C$ the left fiber is excluded since its maximum of $x+2z$ is $(4/5)(2-s)-2<p$, and the right fiber is included since its minimum is $2>p$. The middle traces $x+y\le k$ and $x\ge p$ are both vertex caps of ratio $k$. The triangle lemma therefore gives $\nu(H_B)=\nu(H_C)=ck^2+\gamma b$. Both are below $\gamma a$ because
$$
(\gamma a-ck^2-\gamma b)/c=\gamma(1-\delta)-k^2=(988/1125)\eta-\eta^2>0.
$$
Every point in the left or right fiber belongs to a vertical isolating cap of capacity $\gamma a$ or $\gamma b$, respectively. At the centroid of $K_-$, every containing ambient cap contributes at least $\gamma a$ from $K_-$ alone. Together these bounds give the exact maximum.
