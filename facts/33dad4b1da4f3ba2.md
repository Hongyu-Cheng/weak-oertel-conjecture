---
fact_id: 33dad4b1da4f3ba2
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-contact-gradient-logarithmic-boundary-trace
depends_on: []
verifier_run: 4bf9e27a57c2d859
target_match: null
---

## Source

- [79036a0d1b9e182a](../candidates/79036a0d1b9e182a.json), §§1–3, (1)–(3), active contact gradients and fiberwise Gauss–Green.

## Statement

Let finitely many positive convex $d$-bodies $K_z\subset R B_d$, $d\ge1$, have inballs of radius $r_b>0$. Let $S$ be their lifted sampled union with mixed $d$-volume $dm$ and mass $M>0$, and let $L>0$ be the minimum of finitely many affine functions on its canonical hull. Assume $\int_S\log L\,dm=0$. Suppose positive weights $\sigma_i$ sum to one, the marks $Y_i=(p_i,y_i)$ satisfy $B(y_i,r_s)\subset K_{p_i}$ for $r_s>0$, and there are probability measures $\rho_i$ with
$$
\int w\,d\rho_i=Y_i,\qquad \int L\,d\rho_i=L_i:=L(Y_i),\qquad
\sum_i(\sigma_i/L_i)\rho_i=dm/(ML).
$$
Put $L_{\max}=\max_S L$, and write $dS$ for the sum of the sampled fiber boundary area measures, with endpoint counting measure if $d=1$. Then
$$
\int_S|\nabla_X\log L|\,dm\le M/r_s,\qquad
\int_S|\log L|\,dm\le2M\log L_{\max},
$$
and
$$
\int_{\partial S}|\log L|\,dS\le
\frac{2dM}{r_b}\log L_{\max}+\frac{2RM}{r_b r_s}.
$$

## Proof

Each row is absolutely continuous with respect to $dm$ by positivity of the mixture weights. For any active affine plane $A$ at a mark $Y_i$, the nonnegative function $A-L$ has zero $\rho_i$ integral by the barycenter and $L$ identities. Two such planes with different continuous-coordinate gradients agree only on a mixed-null hyperplane in each fiber, so every active plane at $Y_i$ has the same continuous gradient $c_i$. For $\rho_i$-almost every target, the continuous gradient of $L$ exists and equals $c_i$. Indeed, the different-continuous-slope ties between finitely many planes are mixed-null, and $A=L$ almost everywhere in this row. The same conclusion holds when ties of base slopes extend over an entire fiber.

On the own source ball any active plane is positive, since it majorizes $L$. Evaluate that plane in the direction $-c_i/\|c_i\|$ at distance $r_s$ from $y_i$, using a radial limit if the ball is open. This gives $r_s\|c_i\|\le L_i$, also for $c_i=0$. Integrating the norm of the continuous gradient of $L$ against the mixture yields
$$
M^{-1}\int_S|\nabla_X\log L|\,dm=\sum_i \sigma_i\|c_i\|/L_i\le1/r_s .
$$
Log normalization gives $L_{\max}\ge1$ and $\int|\log L|=2\int(\log L)_+\le2M\log L_{\max}$, with volume measure on $S$.

For each fiber let $o_z$ be its inball center. The finite-plane formula is positive in a neighborhood of the compact hull, so $\log L$ and its absolute value are Lipschitz there. Gauss–Green on the fiber with vector field $(X-o_z)|\log L|$ gives, using $n\cdot(X-o_z)\ge r_b$ and $\|X-o_z\|\le2R$,
$$
r_b\int_{\partial K_z}|\log L|\,dS
\le d\int_{K_z}|\log L|\,dX+2R\int_{K_z}|\nabla_X\log L|\,dX.
$$
The bound on the first weak derivative of $|\log L|$ follows from the Lipschitz chain rule. In dimension one the formula is the fundamental theorem for a Lipschitz function on an interval. Sum over the fibers and apply the volume estimates.
