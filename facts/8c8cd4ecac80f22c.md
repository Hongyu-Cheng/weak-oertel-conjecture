---
fact_id: 8c8cd4ecac80f22c
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: zero-fresh-canonical-cross-pair-completion
depends_on: ["4a0b86dc432ab3e1","ae0161dd5d4ea672","ca061f9c44376a53"]
verifier_run: acb3a01fd76b4081
target_match: null
---

## Statement

Retain one common canonical zero-fresh system of accepted fact ca061f9c44376a53. Thus \(C\subseteq\mathbb R^n\times\mathbb R^d\) is a convex body, \(a_z:=\operatorname{vol}_d(C_z)\), \(r\) is the half-strength complete-product reservoir, \(q\leq r\), and \(F\) is a nonempty family of positive-\(q\) child edges with unique parents. In particular,
\[
 A_f:=(q_f-b_{p(f)})_+,
 \qquad
 \mathfrak A:=\sum_{f\in F}A_f.
\tag{1}
\]
Let
\[
 G:=\mathfrak C_{\mathrm{core}}(C)
\tag{2}
\]
in the exact normalization of accepted fact ae0161dd5d4ea672.

Suppose there are \(z_0,v\in\mathbb Z^n\), with \(v\ne0\), an integer \(M\geq3\), and \(a>0\) such that
\[
 z_j:=z_0+2jv,
 \qquad
 a_{z_j}=a
 \quad(0\leq j<M),
\tag{3}
\]
and every endpoint of every child edge \(f\in F\) belongs to
\[
 P:=\{z_0,z_1,\ldots,z_{M-1}\}.
\tag{4}
\]
Then
\[
 \boxed{G\geq(2M-1)a,}
\tag{5}
\]
\[
 \boxed{\mathfrak A\leq\frac{|F|a}{4M},}
\tag{6}
\]
and consequently
\[
 \boxed{
 G\geq\frac{4M(2M-1)}{|F|}\,\mathfrak A.}
\tag{7}
\]

Here is the exact specialization to the canonical-interface family recorded for this subgoal. Let \(N\) be divisible by \(160\), take \(n=1\), and suppose
\[
 a_{2i}=1
 \quad\left(\frac N5\leq i\leq\frac{4N}{5}-1\right).
\tag{8}
\]
Put
\[
 I_-:=\left\{0,\ldots,\frac{3N}{20}-1\right\},
 \qquad
 I_+:=\left\{\frac{17N}{20},\ldots,N-1\right\}.
\tag{9}
\]
Assume each \(f\in F\) is the child of some parent
\[
 p_{ij}:=\{2i,2j\},
 \qquad
 i\in I_-,\quad j\in I_+,
 \quad j-i\equiv4\pmod8.
\tag{10}
\]
Then
\[
 \boxed{
 G\geq
 \left(128-\frac{320}{3N}\right)\mathfrak A
 \geq\frac{382}{3}\mathfrak A
 \geq4\mathfrak A.}
\tag{11}
\]
In particular, (11) gives the requested one-shot factor \(K=4>e\). If additionally \(\mathfrak A>Q/200\), then (11) gives \(G>Q/50\), contradicting the strict canonical hard inequality \(G<Q/100\). Hence no calibration with all the displayed hypotheses and that amplified-mass lower bound can occur in a genuine canonical hard body. The theorem makes no claim for a non-flat amplified family.

## Proof

We first prove the actual-convexity completion (5). Define the line pullback
\[
 \widehat C
 :=\{(t,y)\in\mathbb R\times\mathbb R^d:
       (z_0+tv,y)\in C\}.
\tag{12}
\]
It is compact and convex. The positive-volume fibers at \(t=0\) and \(t=2M-2\) imply that it has nonempty interior in \(\mathbb R^{1+d}\), so it is a convex body. Its even fibers satisfy
\[
 \operatorname{vol}_d(\widehat C_{2j})=a
 \quad(0\leq j<M).
\tag{13}
\]
Apply accepted fact 4a0b86dc432ab3e1 with base dimension one and \(K=M\). It gives
\[
 \operatorname{vol}_d(C_{z_0+tv})=a
 \quad(0\leq t\leq2M-2),
\tag{14}
\]
and the centroids on this line are affine: for some \(u,b\in\mathbb R^d\),
\[
 c_{z_0+tv}=ut+b
 \quad(0\leq t\leq2M-2).
\tag{15}
\]

Use in the complete-core definition of accepted fact ae0161dd5d4ea672 the integer fiber set
\[
 E:=\{z_0+tv:0\leq t\leq2M-2,\ t\in\mathbb Z\},
 \qquad
 t_z:=a\quad(z\in E),
\tag{16}
\]
and the integer center
\[
 m:=z_0+(M-1)v.
\tag{17}
\]
There are \(2M-1\) members of \(E\), so their selected mass is
\[
 T=(2M-1)a.
\tag{18}
\]
Every proper closed halfspace in \(\mathbb R^n\) containing \(m\) either contains the entire affine line \(z_0+\mathbb Rv\), or cuts it in a closed ray containing the parameter \(M-1\). In the latter case it contains at least \(M\) members of \(E\). Since \(n\geq1\),
\[
 Ma>\frac{(2M-1)a}{2}\geq2^{-n}T.
\tag{19}
\]
Thus the exact base-balance condition holds.

For every \(z\in E\), the full-mass metronoid is the centroid singleton,
\[
 \mathsf M_a(C_z)=\{c_z\}.
\tag{20}
\]
The affine centroid map in (15) extends from the line to an affine map on \(\mathbb R^n\). Hence, for every barycentric representation
\[
 \lambda\in\Lambda_m(E),
\]
one has
\[
 \sum_{z\in E}\lambda_zc_z=c_m.
\tag{21}
\]
Therefore every barycentric Minkowski sum in the complete core is the same singleton \(\{c_m\}\), and the core is nonempty. Equations (16)-(21) verify every condition in the defining supremum of \(G\). This proves (5), including all convexity-forced odd integer fibers between the original even sources.

We next prove (6). All points in \(P\) have one parity class \(\xi\). Since \(F\) is a family of positive-\(q\) edges and \(q\leq r\), the class \(\xi\) is good. Put
\[
 A_\xi:=\sum_{z\equiv\xi\pmod2}a_z.
\tag{22}
\]
Equation (3) gives
\[
 A_\xi\geq Ma.
\tag{23}
\]
Every \(f\in F\) has two endpoints in \(P\), so the complete-product formula in ca061f9c44376a53 gives
\[
 r_f=\frac{a^2}{4A_\xi}.
\tag{24}
\]
Moreover, (1) and \(0\leq q_f\leq r_f\) give
\[
 0\leq A_f\leq q_f\leq r_f.
\tag{25}
\]
Summing (24)-(25) and using (23) proves
\[
 \mathfrak A
 \leq\frac{|F|a^2}{4A_\xi}
 \leq\frac{|F|a}{4M},
\]
which is (6). Multiplying this inequality by \(4M(2M-1)/|F|\) and using (5) proves (7).

It remains to check the recorded calibration exactly. In (8), take
\[
 z_0:=\frac{2N}{5},
 \qquad v:=1,
 \qquad M:=\frac{3N}{5},
 \qquad a:=1.
\tag{26}
\]
For a parent in (10), write its child endpoints as
\[
 \left\{\frac{3(2i)+2j}{4},
             \frac{2i+3(2j)}{4}\right\}
 =\{2x,2y\},
 \qquad
 x:=\frac{3i+j}{4},
 \quad y:=\frac{i+3j}{4}.
\tag{27}
\]
The congruence in (10) makes \(x,y\) integers. The ranges in (9) give
\[
 \frac N5<x<\frac{29N}{80},
 \qquad
 \frac{51N}{80}\leq y<\frac{4N}{5}.
\tag{28}
\]
Thus both child endpoints lie in the block (8). Also
\[
 |F|
 \leq |I_-|\,|I_+|
 =\frac{9N^2}{400}.
\tag{29}
\]
Substituting (26) and (29) into (7) gives
\[
 \begin{aligned}
 G
 &\geq
 \frac{4(3N/5)(6N/5-1)}{9N^2/400}\,\mathfrak A\\
 &=\left(128-\frac{320}{3N}\right)\mathfrak A.
 \end{aligned}
\tag{30}
\]
Because \(N\geq160\), the coefficient in (30) is at least
\[
 128-\frac23=\frac{382}{3}>4>e.
\tag{31}
\]
This proves (11). It uses the actual forced intermediate fibers and the exact complete-core terminal, not the dyadic potential, KKT saturation, cross counting as a substitute for geometry, circuit decomposition, or residual-rank packing.

## External sources

none
