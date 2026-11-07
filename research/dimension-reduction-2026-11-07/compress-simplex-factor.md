# One simplex factor can supply both volume amplification and small caps

Research note, 7 November 2026. This is a new, exact-certificate-backed
construction derived from [fact df488edae05a1702](../../facts/df488edae05a1702.md).
It has independent mathematical reviews and is not Lean-formalized.

There is a full-dimensional rational convex polytope in
$\mathbb R^{52}\times\mathbb R^{1345226000000000003}$ for which every point
of the mixed-integer intersection has a containing proper closed ambient
halfspace of normalized mass strictly below $1/(e2^{52})$. Every nonempty
integer fiber has the full continuous dimension. The continuous dimension
is about 41.66% smaller than that of the accepted construction, but is
still far above 100.

The change is to use a simplex in place of the free box. Its homothetic
expansion amplifies the positive-fiber volume, and its barycentric caps
simultaneously give the required small caps on exposed fibers. A second,
common padding factor is unnecessary.

## General replacement lemma

Use all the notation, hypotheses, integer bases, tetrahedral factors, and
parameters in the complete geometric lemma of fact df488edae05a1702.
Replace $F=[-1,1]^h$ by any rational full-dimensional $h$-simplex containing
zero in its interior. One explicit choice is
$F=\operatorname{conv}(e_1,\ldots,e_h,-\sum_{i=1}^h e_i)$.
Keep $B=B_0\times F$ and use the same positive and negative fibers:

$$
\begin{aligned}
K(a,k)&=[2P_a^0+(k-1)c_a]\times (2qF),\\
G_{a,r}&=[t_r(T_a-c_a)-(r-1)c_a]\times(u_rF),\\
t_r&=1-r(1-t),\qquad u_r=1-r(2q-1).
\end{aligned}
$$

All free-factor scales are positive under the original hypotheses.
The projection census, exposure of every nonzero integer base, and
tetrahedral facet inequalities are unchanged: their proofs do not use
the shape of $F$.

To check the remaining origin-fiber condition, write
$F=\{w:L_j(w)\leq1,\ 0\leq j\leq h\}$, where the $L_j$ are rational
linear forms. Such a representation exists because $F$ is a rational
simplex with zero in its interior. For the explicit simplex above one may
take $L_0(w)=\sum_iw_i$ and
$L_j(w)=\sum_iw_i-(h+1)w_j$ for $1\leq j\leq h$.
With $\delta_q=2q-1$, use the affine
inequalities

$$
L_j(w)\leq1+\delta_q\sum_i z_i,\qquad 0\leq j\leq h.
$$

At a positive Boolean base of size $k$, the maximum of $L_j$ on the
free factor is $2q=1+\delta_q\leq1+k\delta_q$. At a negative base of
size $r$, that maximum is $u_r=1-r\delta_q$, exactly the right side.
The origin generator satisfies the inequalities as well. Therefore every
point of the convex hull satisfies them. At $z=0$, they say precisely
$w\in F$. Together with the unchanged four tetrahedron facet inequalities,
they show that the origin fiber is contained in $B_0\times F$. Its reverse
inclusion is a generator, so the origin fiber is exactly $B$.

Thus all integer fibers are exactly those listed in the fact, all are full
dimensional, and the resulting convex hull is a full-dimensional rational
polytope. Writing $b=|B|$, their volume ratios remain

$$
\begin{aligned}
m&=\frac{3}{32}(2s)^3(2q)^h,\\
\alpha_r&=\frac{3}{32}t_r^3u_r^h,\\
E&=4\sum_{r=1}^{N}\binom{N}{r}\alpha_r,\\
W/b&=(2^{n}-1)m+1+E,\qquad n=4N.
\end{aligned}
$$

The four old origin cuts ignore the free factor. They cover the entire
origin fiber and each has exact mass $b(27/64+E/4)$, with strict exclusion
of all unpaid fibers, just as in the accepted proof.

At any point of any nonzero fiber, choose a largest barycentric coordinate
of its homothetic simplex free factor. It is at least $1/(h+1)$. The cap
where that coordinate is at least its value at the chosen point has relative
volume at most $\Gamma_h=(h/(h+1))^h$. This cuts only the free factor, so
the relative volume in the entire product fiber has the same bound. The
simplex coordinate is a nonconstant affine functional, including when the
point is on a simplex boundary.

Every nonzero integer base $z_0$ is exposed among finitely many bases by
some integer-coordinate functional $\psi$. If the selected barycentric
coordinate is $\lambda$ and the point's free coordinate is $w_0$, use
$\lambda(w)-\lambda(w_0)+Q[\psi(z)-\psi(z_0)]\geq0$.
Compactness bounds the first difference on the other finitely many fibers,
and the exposure gaps are strictly positive. A sufficiently large finite
$Q>0$ therefore gives a proper closed ambient halfspace which agrees with
the cap on the chosen fiber and strictly misses every other fiber.
Since $\alpha_r<3/32<m$, its mass is at most $\Gamma_h mb$.

## Exact parameters and certificate

Take $N=13$, $n=52$, and $h=1345226000000000000$. Set

$$
\begin{aligned}
\delta_s&=10^{-24},& s&=(1+\delta_s)/2,\\
\delta_t&=2\cdot10^{-24},&t&=1-\delta_t,\\
\eta&=1-\frac{3}{2\cdot10^{24}},&\epsilon&=10^{-30},\\
\delta_q&=\frac{274778504931}{10^{11}h},&q&=(1+\delta_q)/2.
\end{aligned}
$$

The integer-only program [compress-certificate.py](compress-certificate.py)
checks all geometric hypotheses and all scalar inequalities below. Its
saved output is [compress-certificate.json](compress-certificate.json).
It establishes the strict rational enclosures

$$
\begin{aligned}
\frac{1463252115845211}{10^{15}}&<m<\frac{1463252115845212}{10^{15}},\\
\frac{465701482650506}{10^{15}}&<E<\frac{465701482650507}{10^{15}}.
\end{aligned}
$$

Call these bounds $m_-,m_+,E_-,E_+$ respectively. The program uses
$e_+=\sum_{i=0}^{50}1/i!+52/(51\cdot51!)$. This exceeds $e$: the tail
starting at $1/51!$ is bounded above by a geometric series of ratio
$1/52$, and the subsequent factorial ratios are strictly smaller.
Exact rational arithmetic proves

$$
\begin{aligned}
\frac{m_-}{e_+}-\frac{27}{64}-\frac{E_+}{4}&>0,\\
1+E_--m_+&=\frac{1224683402647}{500000000000000}>0,\\
1+E_--m_+-\frac{2^{52}m_+}{2h-1}
&=\frac{1068183633138351260764777}
{1345225999999999999500000000000000}>0.
\end{aligned}
$$

For completeness, each rational power is enclosed with outward-rounded
integer interval arithmetic at scale $10^{80}$. Starting with floor and
ceiling bounds for the rational base, multiplication uses the floor of the
product of lower endpoints and the ceiling of the product of upper
endpoints, both divided by the scale. Binary exponentiation applies these
operations at every multiplication and squaring. Induction over the
binary expansion of $h$ proves the resulting intervals contain the exact
powers. All subsequent factors and sums are nonnegative rational numbers,
so the reported enclosures are rigorous. No floating-point result enters
the certificate.

## Every-point conclusion

The accepted finite-dimensional bound follows directly from
$\log(e\Gamma_h)=\int_0^1 t/(h+t)\,dt<1/(2h)$ and
$\exp(x)<1/(1-x)$ for $0<x<1$:
$e\Gamma_h<1+1/(2h-1)$.
Consequently the last certified inequality implies
$e\Gamma_h2^{52}m<(2^{52}-1)m+1+E=W/b$.
The first certified inequality gives
$27/64+E/4<m/e<W/(e2^{52}b)$.

At an origin-fiber point, use one of the four covering cuts. At any
nonzero-fiber point, use the isolated simplex cap constructed above.
These arguments give the uniform strict bound

$$
\sup_{y\in S}\operatorname{depth}_S(y)
\leq \frac{\max\{b(27/64+E/4),\Gamma_hmb\}}{W}
<\frac1{e2^{52}}.
$$

All cuts are proper closed ambient halfspaces. Their continuous boundaries
have zero fiber volume; all discarded fibers are strictly excluded.
The common continuous dimension is $d=h+3$, so fiber Lebesgue measure
agrees with the standard-normalized intrinsic Hausdorff measure used in
the problem. Since $\Gamma_d>1/e$, this also violates the sharp
$\Gamma_d/2^{52}$ bound. It does not refute the assertion that some smaller
positive absolute constant works.

## Scope of the optimization

For orientation, in the limiting balanced family with
$\delta_s,\delta_t\to0$ and $h\delta_q\to x$, one has
$m=(3/32)e^x$ and
$E=(3/8)[(1+e^{-x})^{13}-1]$.
The root of $m/e=27/64+E/4$ is numerically
$x\approx2.7477850492994134$; the limiting mass surplus divided by $m$
is about $0.00167391989477$. The corresponding first-order cap requirement
is $h\gtrsim1.34522555155\cdot10^{18}$.
These decimal values explain the parameter choice only; they are not
used in the proof and are not a global optimality claim.

There is also an exact lower bound for any construction retaining these
same normalized fiber masses. Since $m>1$, its largest fiber has mass $m$.
The ordinary centroid Grünbaum inequality forces
$e\Gamma_d<1+(1+E-m)/(2^{52}m)$ for a $1/e$ counterexample.
The integral identity gives $e\Gamma_d>1+1/[2(d+1)]$, so the certified
mass intervals imply

$$
d+1>\frac{2^{52}m}{2(1+E-m)}
>\frac{2^{52}m_-}{2(1+E_+-m_-)}
=\frac{205934427614674440789015134208}{153085425331}.
$$

This is about $1.34522556389\cdot10^{18}$. The chosen dimension exceeds
this necessary lower bound by a factor smaller than $1.000000325$.
Reducing the dimension substantially further therefore requires changing
the fiber masses or the lattice support, as well as changing the factor
used for caps.
