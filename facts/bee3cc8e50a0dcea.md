---
fact_id: bee3cc8e50a0dcea
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3ek-midpoint-closed-lattice-graph-helly
depends_on: ["c6b7777f667984de"]
verifier_run: 95364e4a72854e7e
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(D\subset\mathbb Z^n\) be finite and nonempty, and assign one vector \(b_z\in\mathbb R^d\) to each \(z\in D\). Put \(T=\{(z,b_z):z\in D\}\). Assume that whenever \(z,z'\in D\) satisfy \(z-z'\in(2\mathbb Z)^n\), their graph midpoint belongs to \(T\):

\[
\left(\frac{z+z'}2,\frac{b_z+b_{z'}}2\right)\in T.
\tag{1}
\]

Then the Helly number of intersections of \(T\) with ordinary ambient convex sets is at most \(2^n\). Explicitly, for every finite family of convex sets in \(\mathbb R^{n+d}\) whose full intersection misses \(T\), a subfamily of at most \(2^n\) already has intersection missing \(T\). The convex sets need not be closed, and no full-dimensionality hypothesis is imposed on \(T\).

For every assignment of finite nonnegative real weights \(w_z\), let \(W=\sum_{z\in D}w_z\). There is one \(q=(z^\star,b_{z^\star})\in T\), fixed before a halfspace is tested, such that every closed ambient halfspace \(H\) containing \(q\) satisfies \(\sum_{(z,b_z)\in H}w_z\ge 2^{-n}W\). If \(W>0\), the point can also be chosen in \(\operatorname{conv}\{(z,b_z):w_z>0\}\).

The graph labels \(b_z\) here are arbitrary given vectors. When they are actual volume centroids, and the weights are actual fiber volumes, \(b_z,w_z,W\) agree exactly with those objects in accepted fact \(\texttt{c6b7777f667984de}\). For its generic atomic construction, the alias and normalization map used below is \(\mathcal E=\mathbb R^{n+d}\), location set equal to the present finite graph \(T\), Helly bound \(h=2^n\), and \(\eta=W^{-1}\sum_{z\in D}w_z\delta_{(z,b_z)}\). The product location set used elsewhere in that accepted fact is not identified with this graph.

## Proof

We first prove the needed finite-set witness lemma from first principles. Let \(F\) be any nonempty finite subset of a Euclidean space. Call \(R\subseteq F\) an empty vertex set if every point of \(R\) is a vertex of \(\operatorname{conv}R\) and \(\operatorname{conv}R\cap F=R\). Let \(g\) be the largest cardinality of such a set; it exists, since \(F\) is finite and singletons are empty vertex sets. We claim that every finite family of convex sets with intersection missing \(F\) has a subfamily of at most \(g\) whose intersection misses \(F\).

Suppose instead that convex sets \(K_1,\ldots,K_s\) have intersection missing \(F\), but each subfamily of at most \(g\) has a common point of \(F\). Every trace \(F\cap K_i\) is nonempty. Define the compact polytope \(P_i=\operatorname{conv}(F\cap K_i)\), which is contained in \(K_i\) by convexity. For each \(x\in F\setminus K_i\), choose a closed affine halfspace containing \(P_i\) and excluding \(x\). Such strict separation exists even when \(P_i\) has lower affine rank: if \(k\in P_i\) is nearest to \(x\), then \((x-k)\cdot(y-k)\le0\) for every \(y\in P_i\), while \((x-k)\cdot(x-k)>0\). The halfspace defined by the former inequality has the required property.

Pool these finitely many halfspaces, retaining their indices \(i\). Their common intersection misses \(F\), because every point of \(F\) is excluded by at least one original \(K_i\) and hence by its corresponding separating halfspace. Every subfamily of at most \(g\) pooled halfspaces nevertheless has a common point of \(F\): it uses at most \(g\) original indices, and a common point in the corresponding original traces belongs to every selected halfspace. Choose an inclusion-minimal pooled subsystem whose intersection misses \(F\), and write its inequalities as \(a_i(x)\le\rho_i\), \(1\le i\le m\), where each \(a_i\) is linear. Thus \(m>g\). Minimality gives \(x_i\in F\) such that \(a_j(x_i)\le\rho_j\) for \(j\ne i\), whereas \(a_i(x_i)>\rho_i\).

Since the full closed subsystem misses the finite set \(F\), the number \(\delta=\min_{x\in F}\max_i(a_i(x)-\rho_i)\) is positive. Set \(\varepsilon=\delta/2\), \(\ell_i=\rho_i+\varepsilon\), and \(u_i=a_i(x_i)\). The witness inequalities imply \(u_i-\rho_i\ge\delta\), so \(\ell_i<u_i\). Consider the threshold vectors satisfying

\[
\ell_i\le t_i\le u_i\quad(1\le i\le m),
\qquad
\text{for every }x\in F\text{ there is an }i\text{ with }a_i(x)\ge t_i.
\tag{2}
\]

They form a compact set: for each fixed \(x\), the second condition is a finite union of closed sets, and the threshold box is compact. This set is nonempty, because \(t_i=\ell_i\) satisfies (2). Choose a vector maximizing \(\sum_i t_i\).

For each \(i\), there is \(y_i\in F\) such that \(a_i(y_i)=t_i\) and \(a_j(y_i)<t_j\) for all \(j\ne i\). If \(t_i=u_i\), take \(y_i=x_i\), since \(a_j(x_i)\le\rho_j<\ell_j\le t_j\). If \(t_i<u_i\), define \(B_i=\{x\in F:a_j(x)<t_j\text{ for all }j\ne i\}\). This finite set is nonempty because it contains \(x_i\). Feasibility in (2) gives \(a_i(x)\ge t_i\) for every \(x\in B_i\). If all these inequalities were strict, one could increase \(t_i\) by a sufficiently small positive amount, less than both \(u_i-t_i\) and every gap \(a_i(x)-t_i\) with \(x\in B_i\). Points of \(B_i\) would still satisfy (2) using index \(i\), and every other point of \(F\) already satisfies (2) using an index different from \(i\). This contradicts maximality, and proves the asserted contact.

The points \(y_i\) are distinct, since \(a_i(y_i)=t_i\) while \(a_i(y_j)<t_i\) for \(j\ne i\). Let \(R=\{y_1,\ldots,y_m\}\). Each \(y_i\) uniquely maximizes \(a_i\) on \(R\), so it is a vertex of \(\operatorname{conv}R\). For any \(x\in F\cap\operatorname{conv}R\), all inequalities \(a_i(x)\le t_i\) hold by convexity. Condition (2) forces equality for some \(i\). In a convex combination of the \(y_j\), the equality \(a_i(x)=t_i\) is possible only if all weight is on \(y_i\), because every other \(y_j\) has strict inequality. Hence \(x=y_i\). Thus \(R\) is an empty vertex set of size \(m>g\), a contradiction. The witness lemma is proved for all affine ranks and all original convex sets.

Apply this lemma to \(F=T\). Any empty vertex set \(R\subseteq T\) contains at most \(2^n\) points. Otherwise two distinct points \((z,b_z),(z',b_{z'})\in R\) have the same base parity. There is one point per base, so \(z\ne z'\). Their midpoint in (1) is a point of \(T\cap\operatorname{conv}R\), distinct from both endpoints. It cannot be a vertex of \(\operatorname{conv}R\), because it is the midpoint of two distinct points of that convex hull. Consequently it cannot belong to \(R\), contradicting the defining equality \(T\cap\operatorname{conv}R=R\). The finite-set witness lemma therefore gives the claimed Helly bound \(h=2^n\) directly in the graph's ambient space.

If \(W=0\), all weights vanish and any \(q\in T\) gives the required inequality. Assume now \(W>0\). The finite graph is closed, and the probability \(\eta\) specified in the statement has finite nonempty support in \(T\). The generic atomic centerpoint construction proved in accepted fact \(\texttt{c6b7777f667984de}\) applies using exactly the stated alias map and the graph Helly bound just proved. We detail its construction here to check the weight and boundary cases.

Let \(P_\eta=\operatorname{conv}(\operatorname{supp}\eta)\), and consider it together with every closed ambient halfspace \(J\) having \(\eta(J)>1-1/h\). Any at most \(h\) members of this family have a common support point: the complement of each halfspace member has probability strictly less than \(1/h\), and the complement of \(P_\eta\) has probability zero, so the union of their complements has probability strictly less than one. Helly therefore gives a common point of \(T\) for every finite subfamily. A common point for the entire family exists as well because \(T\) is finite. Indeed, if it did not exist, choose for each point of \(T\) one member excluding it; the resulting finite subfamily would miss \(T\), a contradiction. Choose such a point \(q\in T\cap P_\eta\).

Suppose a closed halfspace \(H=\{x:\lambda(x)\ge\tau\}\) contains \(q\) but has \(\eta(H)<1/h\), where \(\lambda\) is linear. Its complement has probability greater than \(1-1/h\). Since the positive support of \(\eta\) is finite, there is \(\kappa>0\) such that every support point outside \(H\) satisfies \(\lambda(x)\le\tau-\kappa\). The closed halfspace \(J=\{x:\lambda(x)\le\tau-\kappa\}\) has \(\eta(J)=1-\eta(H)>1-1/h\). It belongs to the defining family but excludes \(q\), contradicting the construction. Thus every containing closed halfspace has mass at least \(1/h\). Multiplication by \(W\) proves the weighted inequality. Zero weights never enter the positive support, and normals that are constant on the affine hull of that support cause no exception: since \(q\in P_\eta\), every containing halfspace of that type contains the entire support and has mass one. The argument therefore includes all affine ranks, arbitrary nonnegative weights, and all closed-halfspace boundaries.

## External sources

None. The finite-set Helly witness lemma and the parity argument are proved completely above. The weighted selection uses the generic atomic centerpoint construction from the declared accepted predecessor \(\texttt{c6b7777f667984de}\), with its applicability and boundary cases checked explicitly.
