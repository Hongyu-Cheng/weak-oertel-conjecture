# Independent audit of the original sharp-bound construction (168,99)

## Verdict and audit identity

**PASS**, with one explicit clarification of the endpoint-cap isolation argument below. The original construction gives a counterexample to the sharp bound with integer dimension 168 and continuous dimension 99. It does **not** give a counterexample to the weak bound with constant 1/e, and it does not meet the goal that both dimensions are less than 100.

The audited source is `sharp-n168-d99.md`, with its original SHA256:

```text
1a677eb84071ec3a45ecc19998e1f47f70c10ea2509a1cb88265971a0bd20bfa
```

This fingerprint identifies the source actually audited; it is intentionally not updated for subsequent edits. The independent standard-library checker is `join_audit_checker.py`, and its saved output is `join_audit_results.json`. The completed run exited successfully and passed **1,035,123 exact rational predicates**, including **57,288 positive-fiber middle-cut cases**. All decisive comparisons used `fractions.Fraction`, rather than floating-point arithmetic. This note records an analytic proof audit supported by exact arithmetic, not a Lean formalization.

The original parameters audited were

\[
\varepsilon=10^{-14},\quad
\delta=\frac{3258435}{10^8},\quad
\delta'=\frac{325843501}{10^{10}},\quad
\eta=\frac{19348312999}{20000000000},\quad R=507.
\]

There are three blocks of 56 integer coordinates; negative supports have sizes from 1 through 30. The later simplified parameter proposal was not audited to completion and is not covered by this verdict. The subsequent (167,99) construction is also outside this audit; this document preserves the supplementary (168,99) record.

## Geometric obligations checked

1. **Source simplices and central caps.** In the 99-dimensional affine simplex model with 100 barycentric coordinates, each source simplex has full dimension and volume ratio \(\theta=5/36\). Exact elimination verifies the determinant; analytically the nontrivial calculation is a three-coordinate block with the other 97 coordinates unchanged. The sign assertions for the three cyclic linear functionals hold at every source vertex and therefore on each simplex. The central cap ratio is \(\beta=49/108\): its two nontrivial edge ratios are \(7/9\) and \(7/12\), whose product gives the determinant ratio. The remaining vertices form the common join face and do not introduce an additional exponent.

2. **Interior centers.** Each specified center has strictly positive barycentric coefficients in both the ambient simplex and its source simplex. In the latter the coefficients are \(3/100-35\varepsilon/13\), \(7\varepsilon/5\), \(84\varepsilon/65\), and 97 copies of \(1/100\). They sum to one and reconstruct the stated center exactly. Its three functional values are \(2\varepsilon,-\varepsilon,-\varepsilon\).

3. **Affine constants in the prescribed fibers.** These require care because the central-simplex coordinates \(\lambda_j\) are affine. For a positive support of size \(k\),

   \[
   \lambda_j((1+\delta)u+(k-\delta)c)
   =(1+\delta)\lambda_j(u)+(k-\delta)\lambda_j(c)-k/100.
   \]

   For a negative support of size \(r\), with \(t=1-\delta'\) and \(t_r=1-r\delta'\),

   \[
   \lambda_j(t_ru-rt c)
   =t_r\lambda_j(u)-rt\lambda_j(c)+r/100.
   \]

   Both identities and all positivity requirements were checked. In particular, \(t_r>0\) through \(r=30\), so every prescribed fiber has full continuous dimension. The central fiber and the positive unit-coordinate bases imply full dimension of the complete convex body.

4. **Integer projection census.** The projection lies in \([-1,1]^{168}\). If an integer point has a coordinate equal to \(-1\), every generator in a convex representation must have \(-1\) in that coordinate. Those generators all come from the same negative block. Integrality in the remaining coordinates then forces their supports to coincide, leaving exactly a listed negative base. If there is no negative coordinate, the point is Boolean, and every Boolean base is already listed. Thus the census is exact.

5. **Exposure and exact noncentral fibers.** For a positive support, assign coefficient 1 on the support and \(-1/169\) outside. For a negative support, assign coefficient \(-1\) on the support and \(1/169\) outside. In each case the prescribed base uniquely maximizes the resulting linear functional over the full projection. The inequalities were checked by support and intersection cardinalities. Consequently taking the full convex hull does not enlarge any noncentral fiber.

6. **Exact central fiber, including all balanced combinations.** Put

   \[
   v=\delta/100+(1-\delta)35\varepsilon/39.
   \]

   Every generator satisfies the affine facet guards

   \[
   \lambda_j(x)+v\sum_i z_i\ge0.
   \]

   For positive generators the remaining lower-bound difference is
   \((k-1)\delta(1/100-35\varepsilon/39)\ge0\). For negative generators, the strict per-unit difference is

   \[
   \frac{\delta'-\delta}{100}
   -\left((1-\delta)\frac{35}{39}+(1-\delta')\frac{49}{39}\right)\varepsilon
   =\frac{38187370854049}{39000000000000000000000000}>0.
   \]

   Affine guards pass to arbitrary convex combinations. At integer base zero they give all the ambient simplex inequalities. Since that simplex was included initially, the actual central fiber is exactly the prescribed one. This argument handles arbitrary balanced combinations, not merely pairs of opposite bases.

7. **Middle cuts for every fiber type.** For cut \(j\), use coefficient \(-R\) on integer block \(j\) and \(\eta\varepsilon\) elsewhere. Positive supports meeting that block have strict upper bound \(2k-R<0\). For positive supports avoiding it the bound is \([k\eta-(k-\delta)]\varepsilon<0\). Negative fibers in another block have upper bound \(r(t-\eta)\varepsilon<0\), while negative fibers in block \(j\) have lower bound \(r(R-2t\varepsilon)>0\). Thus each middle cut retains exactly one central cap and all negative fibers in its own block. The three cuts cover the central simplex because the three continuous functionals sum to zero. Closed-halfspace boundary cases therefore cause no omission.

## Endpoint-cap isolation clarification

At a point of a 99-simplex, some barycentric coordinate is at least \(1/100\). The cap through that point in the increasing-coordinate direction has relative volume at most
\(\Gamma=(99/100)^{99}\).

To isolate this cap in the full mixed-integer set, let \(h\) expose its integer base \(z_0\), and let \(a(x)\ge0\) be the cap inequality through the chosen point. The ambient inequality must be written

\[
a(x)+Q\bigl(h(z)-h(z_0)\bigr)\ge0.
\]

For every other integer base \(z\), the gap \(h(z_0)-h(z)\) is strictly positive, and \(a\) has a finite maximum on that compact fiber. There are finitely many integer fibers, so a finite sufficiently large \(Q\) strictly excludes all of them while preserving the desired cap at \(z_0\). Its continuous normal is nonzero, giving a proper closed halfspace.

The source's instruction to add a large multiple of the exposing functional is valid when the functional is centered in this way, or when the halfspace threshold is adjusted equivalently. Adding the uncentered functional with a fixed threshold would not leave the cap unchanged. This is an exposition clarification with an explicit repair; no change to the construction or its parameters is required.

## Exact inequalities and resulting scope

Writing volumes in units of the central simplex volume, define

\[
\begin{aligned}
m&=\frac5{36}(1+\delta)^{99},\\
E&=3\frac5{36}\sum_{r=1}^{30}\binom{56}{r}(1-r\delta')^{99},\\
s&=1+E-m,\qquad
W_0=2^{168}m+s.
\end{aligned}
\]

The independently recomputed values, shown approximately only for readability, are:

| Quantity | Approximate value |
| --- | ---: |
| \(m\) | 3.32120603225623471547 |
| \(E\) | 2.32158774220109470359 |
| \(s\) | 0.000381709944859988126 |
| \(\Gamma m-\beta-E/3\) | 0.000382018428782490769 |

The checker proves both final margins exceed \(38/100000\) using exact rational comparisons. Every negative fiber has smaller volume than \(m\). Central points admit the middle cuts, and noncentral points admit the isolated simplex caps. Hence

\[
\sup\operatorname{depth}\le\frac{\Gamma m}{W_0}
<\frac{\Gamma}{2^{168}}.
\]

The relative deficit from the sharp bound is approximately \(3.07184\times10^{-55}\), so ordinary floating-point subtraction would not certify the final strict inequality. Its exact proof is simply \(s>0\). Applying the usual simplex centroid halfspace bound to a positive fiber also gives equality in the first displayed upper bound; equality is unnecessary for the sharp-bound violation.

This distinction matters for the weak conjecture. The exact checker also establishes

\[
\frac{65}{24}\Gamma>1+\frac{s}{2^{168}m}.
\]

Since \(e>\sum_{j=0}^4 1/j!=65/24\), the attained maximum depth is strictly **greater** than \(1/(e2^{168})\). Thus this construction refutes the sharp constant at (168,99), but does not refute the weak constant. The audit makes no dimension-minimality claim and covers neither the optional simplified parameters nor the later asymmetric (167,99) improvement.

## Amendment: endpoint clarification incorporated

The revised Section 7 of `sharp-n168-d99.md` has been read and now explicitly uses the centered halfspace \(a(x)+Q[h(z)-h(z_0)]\ge0\), together with the finite-gap and compact-fiber argument. The requested clarification is therefore incorporated. The revision identified by the integrating author has SHA256:

```text
808b048e91aed89f99d4979caa7edfd25d5f0e9aeecf1facc6499bd6521b605a
```

The original reviewed fingerprint above and the saved exact-checker results remain unchanged. This amendment reviews only the revised Section 7; the mathematical parameters are unchanged, and the million-predicate checker was not rerun. The PASS verdict and its stated scope are unchanged.
