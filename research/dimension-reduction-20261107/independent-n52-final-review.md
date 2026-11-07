# Independent final review of the n=52 dimension reduction

This review checks `improved-n52.md`, `check_improved_n52.py`, and
`support-dimension-obstruction.md` against the generalized geometric lemma
in `facts/df488edae05a1702.md`.

## Verified result

The proposed parameters give an exact analytic counterexample to
\(1/(e2^{52})\), with

\[
n=52,\qquad h=2\,747\,786,\qquad
\ell=1\,350\,000\,000\,000\,000\,000,\qquad
d=1\,350\,000\,000\,002\,747\,789.
\]

An independent replay of `check_improved_n52.py` returned
`PASS_EXACT_RATIONAL_PARAMETER_IMPROVEMENT`. Its integer floor and ceiling
operations preserve the claimed positive power intervals under both
multiplication and squaring. All scalar and geometric hypotheses of the
generalized lemma hold, and its exact middle-cut, mass-surplus, and padding
margins are respectively positive, positive, and positive. The last margin
is approximately \(7.08507398\cdot10^{-6}\).

The proof correctly distinguishes the padding dimension \(\ell\) from the
total continuous dimension \(d\). At nonzero bases the cap bound uses
\(\Gamma_\ell\); the comparison with the sharp bound uses
\(\Gamma_d>1/e\). The middle cuts and the exposed-fiber simplex caps give
two uniform bounds, so the conclusion is a strict bound on the supremum,
not only a strict inequality at each individual point with a possibly
vanishing margin.

The geometric assertions are supplied by the complete generalized lemma,
not inferred from the numerical certificate. In particular, the affine
facet inequalities determine the origin fiber exactly, the projection
argument excludes unlisted integer fibers, and finite exposing tilts
remove all other fibers without changing the chosen simplex cap.

No proof gap was found in this parameter specialization. This review does
not constitute a Lean formalization. The construction refutes the exact
constant \(1/e\), not the existence of some smaller universal positive
constant.

## Verified obstructions

An independent replay of `check_support_obstruction.py` returned
`PASS_EXACT_OBSTRUCTION_PREMISES`.

For any full-dimensional convex fibers on the same integer support,
the centroid of a largest fiber gives
\(D(C)\ge\Gamma_d/F\), where
\(F\le2^{52}+32764\). The identity
\(\log(e\Gamma_d)=\int_0^1 t/(d+t)\,dt\)
and the strict bound \(e^x>1+x\) imply

\[
d+1>\frac{2^{51}}{32764}
=68\,727\,866\,368+\frac{1024}{8191}.
\]

Thus \(d\ge68\,727\,866\,368\) is a necessary condition for an exact
\(1/e\) counterexample on that support, regardless of all fiber shapes
and volumes. The conversion from the strict rational inequality to this
integer bound is correct.

The equal-block argument is also correct. AM-GM gives
\((1-rx)(1+x)^r\le1\), and the strict parameter inequality
\(\delta_t>\delta_s\) implies
\(\alpha_r m^r<\theta^{r+1}\). Combining the resulting upper bound on
\(E\) with the two current sufficient inequalities rules out
\(N\le12\), hence requires \(n=4N\ge52\). The note correctly confines
this conclusion to this construction and its certification conditions.
It does not rule out better cuts or unrelated families.

## Useful unfinished optimization observation

For the equal-block family with \(N=13\), the limiting scalar envelope is

\[
E_{\mathrm{lim}}(m)=4\theta
\left[\left(1+\frac{\theta}{m}\right)^{13}-1\right].
\]

The numerical intersection
\(\beta+E_{\mathrm{lim}}(m)/4=m/e\) occurs near
\(m=1.4632521158297211\), with
\(E_{\mathrm{lim}}(m)=0.4657014826574730\) and
\(1+E_{\mathrm{lim}}(m)-m=0.00244936682775188\).
It suggests a limiting padding dimension near
\(1.3452255515\cdot10^{18}\) under the present scalar certification
method. This is a numerical optimization observation, not an additional
certified witness or a claimed minimum for arbitrary counterexamples.

The certified choice \(\ell=1.35\cdot10^{18}\) is already within about
0.354% of that limiting scalar value. Further tuning could improve the
reported dimension modestly, but cannot address the goal \(d<100\).
The support obstruction proves that a substantially different integer
support is necessary for that goal when the target remains \(1/e\).
