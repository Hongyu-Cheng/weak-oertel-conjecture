---
fact_id: b3dd5f87b2f6ec9e
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-exact-local-hull-additions
depends_on: []
verifier_run: 8cd28218ae14eaaa
target_match: null
---

## Source

- [97eab0f821e54041](../candidates/97eab0f821e54041.json), §2 and §2.1, Lemmas 2–3, (3)–(5), exact own-fiber bump geometry.

## Statement

Let $K\subset\mathbb R^d$, $d\ge1$, be a compact convex body with nonempty interior. Let $v\in\partial K$ have a unique outward unit supporting normal $u$, with $K\cap\{x:u\cdot x=h_K(u)\}=\{v\}$. Fix $h$ with $u\cdot h>0$. Then $K(t)=\operatorname{conv}(K\cup\{v+th\})$ has added volume $\Delta(t)=|K(t)|-|K|>0$ for $t>0$. The function $\Delta$ is continuous and strictly increasing, with $\Delta(0)=0$, and $\sup_{x\in K(t)\setminus K}\lVert x-v\rVert\to0$ as $t\downarrow0$. In particular each sufficiently small prescribed positive added volume has a unique small positive parameter.

For a finite list of distinct points $v_i$ with these hypotheses and corresponding directions $h_i$, write $a_i=v_i+t_i h_i$. For all sufficiently small positive $t_i$ one has the exact disjoint union
$$
\operatorname{conv}(K\cup\{a_i:i\})\setminus K
=\bigsqcup_i\bigl(\operatorname{conv}(K\cup\{a_i\})\setminus K\bigr).
$$

## Proof

Let $a(t)=v+th$. The bodies $K(t)$ are nested for increasing $t$ because the earlier apex lies on the segment from $v$ to the later apex. Their $u$-supports are $h_K(u)+t u\cdot h$, which strictly increase. For strictly nested convex bodies of nonempty interior, the larger one has strictly more volume. Indeed, an exterior point of the smaller body in the larger one can be joined to an interior point of the larger body to find a small ball in the difference. Hausdorff continuity of $K(t)$, including at zero, follows by comparing the apices in the convex combinations. Volume continuity on convex bodies gives the claimed continuity and the exact inverse.

For locality, let $t_k\downarrow0$ and $x_k=(1-\lambda_k)c_k+\lambda_k a(t_k)$ be in $K(t_k)\setminus K$, with $c_k\in K$ and $0<\lambda_k\le1$. Choose a strictly separating unit normal $n_k$, so $n_k\cdot x_k>h_K(n_k)$ and $n_k\cdot a(t_k)>h_K(n_k)$. Then $0\le h_K(n_k)-n_k\cdot v<t_k\lVert h\rVert$. Every limiting normal therefore supports $K$ at $v$, hence equals $u$. Along any convergent subsequence of $(\lambda_k,c_k)$, a limit $\lambda_k\to1$ gives $x_k\to v$. Otherwise, from separation we have
$$
(1-\lambda_k)(h_K(n_k)-n_k\cdot c_k)
<\lambda_k(n_k\cdot a(t_k)-h_K(n_k))\le t_k\lVert h\rVert.
$$
The limit of $c_k$ must lie in the singleton $u$-support face, again giving $x_k\to v$. Compactness gives the uniform locality.

For several apices, set $N_i(t_i)=\{n\in\mathbb S^{d-1}:n\cdot a_i\ge h_K(n)\}$. The same support bound with a non-strict inequality puts each of these closed sets in any prescribed neighborhood of $u_i$ for all sufficiently small $t_i>0$. The normals $u_i$ are distinct because each supports a singleton face at its own distinct $v_i$. Therefore the $N_i(t_i)$ are pairwise disjoint. Let $L=\operatorname{conv}(K\cup\{a_i:i\})$. At a boundary point of $L$ outside $K$, any supporting face uses an apex, and every apex in the face has supporting normal in its corresponding $N_i(t_i)$. Only one apex can occur. That face is contained in $\operatorname{conv}(K\cup\{a_i\})$ for this apex. For any point of $L\setminus K$, extend the ray from a fixed interior point of $K$ through it to $\partial L$. The endpoint is outside $K$, so the segment to it belongs to one single-apex hull. Finally, a point in two single-apex hulls outside $K$ would have a strictly separating normal in both visible sets. This proves exact disjointness.
