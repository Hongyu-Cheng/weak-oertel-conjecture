---
fact_id: fee1ed7cc2e6ca62
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: cyclic-dyadic-all-temperature-reflection
depends_on: ["6c4f6e6754070930"]
verifier_run: 9e379db8484742ce
target_match: null
---

## Statement

For every integer \(N\ge2\), put \(m=2^N-1\), \(b_i=2^{i-1}\), and \(r=0\). Write the registered congruence lattice \(L\) as \(\mathcal L\), with no change of lattice or normalization:

\[
\mathcal L=\left\{z\in\mathbb Z^N:\sum_{i=1}^N b_i z_i\equiv0\pmod m\right\},
\qquad
D=\mathcal L\cap\mathbb Z_{\ge0}^N,
\qquad
w_z=\begin{cases}q^{\sum_i z_i},&z\in D,\\0,&z\notin D,\end{cases}
\qquad W=\sum_{z\in D}w_z,
\]

where \(q\in(0,1)\). These are exactly the objects in accepted fact \(6c4f6e6754070930\), with its weight parameters \(a_i=-\log q\). For each original integer center \(J\in D\), retain

\[
S_J=\sum_{v\in\mathbb Z^N}\min\{w_{J+v},w_{J-v}\}
=\sum_{\substack{v\in\mathcal L\\J+v\ge0,\ J-v\ge0}}
q^{\sum_iJ_i+|\sum_i v_i|}.
\tag{1}
\]

Thus displacements are oriented and zero is counted once. Then \(0<W<\infty\), the maximum of \(S_J\) over \(J\in D\) is attained, and

\[
\max_{J\in D}S_J\ge\frac{1}{624000000}\,2^{-N}W
\qquad\text{for every }N\ge2\text{ and }q\in(0,1).
\tag{2}
\]

Write \(\mathbf1=(1,\ldots,1)\). For \(q\le7/10\), the original center \(J=0\) satisfies (2). For \(7/10\le q\le19/20\), a center in \(\{3\mathbf1,6\mathbf1,9\mathbf1,12\mathbf1,15\mathbf1,18\mathbf1\}\) satisfies (2), with the explicit choice given in the proof. For \(19/20\le q<1\), the original center \(J=h\mathbf1\), where \(h=2\lceil1/(-2\log q)\rceil\), satisfies the stronger inequality \(S_J\ge(1/48)2^{-N}W\).

## Proof

All uses of the accepted predecessor \(6c4f6e6754070930\) retain its \(N,m,b_i,r,D,w_z,W,S_J,\mathbf1,\ell,s\). Its full congruence lattice is the \(\mathcal L\) defined above. In particular, the following two bounds are its equations (6) and (1), respectively. For \(q<s<1\) and every integer \(\ell\ge1\),

\[
W\le\frac{1+q}{1-q/s}(1-qs)^{-N},
\qquad
\frac{S_{3\ell\mathbf1}}{2^{-N}W}
\ge\frac{1-q/s}{1+q}\,
\frac{\bigl[2(2\ell+1)q^{3\ell}(1-qs)\bigr]^N}{2\ell N+1}.
\tag{3}
\]

These bound the full infinite total mass and the original score; they are not bounds for a restricted support or a modified score. Every center used below is a nonnegative integer multiple of \(\mathbf1\), hence belongs to \(D\), because \(\sum_i b_i=m\).

First suppose \(0<q\le1/2\). The full nonnegative-orthant sum gives \(W\le(1-q)^{-N}\), and (1) gives \(S_0=1\). Therefore \(S_0/(2^{-N}W)\ge[2(1-q)]^N\ge1\).

For \(1/2<q\le7/10\), set \(s=71/100\) in the first bound of (3), which is valid since \(q<s<1\). Since \(S_0=1\),

\[
\frac{S_0}{2^{-N}W}
\ge\frac{1-q/s}{1+q}\,[2(1-qs)]^N
\ge\frac{10}{1207}\left(\frac{503}{500}\right)^N
\ge\frac{10}{1207}.
\tag{4}
\]

Here \(1-q/s\ge1/71\), \(1+q\le17/10\), and \(qs\le497/1000\). In particular, (2) holds in both of these ranges.

We next cover \([7/10,19/20]\) by finitely many explicit analytic estimates. Define \(f_\ell(q)=2(2\ell+1)q^{3\ell}(1-q^2)\). Its derivative is

\[
f_\ell'(q)
=2(2\ell+1)q^{3\ell-1}\bigl[3\ell-(3\ell+2)q^2\bigr].
\tag{5}
\]

Thus it increases and then decreases, so its minimum on any closed subinterval of \((0,1)\) occurs at an endpoint. Choose \(\ell\) by the following table. The last two columns give rational lower bounds for \(q^{3\ell}\) at the left and right endpoint, respectively.

| \(\ell\) | Interval for \(q\) | Left power lower bound | Right power lower bound |
|---|---|---|---|
| \(1\) | \([7/10,17/20]\) | \(343/1000\) | \(49/80\) |
| \(2\) | \([17/20,9/10]\) | \(3/8\) | \(531/1000\) |
| \(3\) | \([9/10,23/25]\) | \(387/1000\) | \(471/1000\) |
| \(4\) | \([23/25,187/200]\) | \(367/1000\) | \(446/1000\) |
| \(5\) | \([187/200,189/200]\) | \(364/1000\) | \(427/1000\) |
| \(6\) | \([189/200,19/20]\) | \(361/1000\) | \(397/1000\) |

All power bounds have short rational checks. At \(q=7/10\), the displayed cube is exact. At \(q=17/20\), \(q^3=4913/8000>49/80\) and \((49/80)^2=2401/6400>3/8\). At \(q=9/10\), \(q^6=531441/1000000>531/1000\) and \(q^9=387420489/1000000000>387/1000\).

For \(q=23/25\), direct cubing gives \(q^3>1557/2000\); squaring this lower bound gives \(q^6>303/500\). Consequently \(q^9>(303/500)(1557/2000)=471771/1000000>471/1000\), and \(q^{12}>(303/500)^2=91809/250000>367/1000\).

For \(q=187/200\), direct cubing gives \(q^3=6539203/8000000>4087/5000\). Since \((4087/5000)^2=16703569/25000000>167/250\), we obtain \(q^6>167/250\), \(q^{12}>(167/250)^2=27889/62500>223/500=446/1000\), and \(q^{15}>(223/500)(4087/5000)=911401/2500000>364/1000\).

For \(q=189/200\), its cube is \(6751269/8000000>8439/10000\). Squaring gives \(q^6>7121/10000\), because \(8439^2=71216721>71210000\). Squaring again gives \(q^{12}>507/1000\), because \(7121^2=50708641>50700000\). Hence \(q^{15}>(507/1000)(8439/10000)=4278573/10000000>427/1000\), and \(q^{18}>(507/1000)(7121/10000)=3610347/10000000>361/1000\).

Finally, for \(q=19/20\), \(q^6=47045881/64000000>147/200\); therefore \(q^{18}>(147/200)^3=3176523/8000000>397/1000\). This proves every power entry in the table by elementary rational arithmetic.

Substitution of the table's power bounds into \(2(2\ell+1)q^{3\ell}(1-q^2)\) gives the following endpoint lower bounds, in the same row order:

\[
\begin{array}{c|cc}
\ell&\text{left endpoint}&\text{right endpoint}\\\hline
1&52479/50000&16317/16000\\
2&333/320&10089/10000\\
3&51471/50000&79128/78125\\
4&79272/78125&10097217/10000000\\
5&5036031/5000000&20098463/20000000\\
6&20081347/20000000&201279/200000
\end{array}
\tag{6}
\]

Each displayed rational number is greater than \(501/500\). Equation (5) therefore proves \(f_\ell(q)>501/500\) throughout its entire assigned interval. This is an explicit uniform margin over the full intervals; no inference of uniformity in \(N\) from continuity in \(q\) is needed.

Now set \(\varepsilon=1/26000\) and \(s=q+\varepsilon\). Throughout these intervals, \(q<s<1\). With the same \(\theta=2(2\ell+1)q^{3\ell}(1-qs)\) as in the predecessor, we have

\[
\theta
=f_\ell(q)-2(2\ell+1)q^{3\ell+1}\varepsilon
\ge\frac{501}{500}-26\varepsilon
=\frac{1001}{1000},
\qquad
\frac{1-q/s}{1+q}
=\frac{\varepsilon}{s(1+q)}
\ge\frac1{52000}.
\tag{7}
\]

We used \(\ell\le6\) and \(q,s<1\). Bernoulli's inequality gives \(\theta^N\ge1+N/1000\). Since \(12000(1+N/1000)=12000+12N\ge2\ell N+1\), the second bound in (3) yields

\[
\frac{S_{3\ell\mathbf1}}{2^{-N}W}
\ge\frac1{52000}\frac{1+N/1000}{2\ell N+1}
\ge\frac1{624000000}.
\tag{8}
\]

This proves (2) throughout the middle range, with explicit original centers and a constant independent of both parameters.

It remains to treat \(19/20\le q<1\). We first prove the required congruence count for every translated integer box of side four. Let \(\zeta=e^{2\pi\mathrm i/m}\). For \(1\le k\le m-1\), none of the numbers \(\zeta^{k b_i}\) is one, because each \(b_i\) is coprime to \(m\). Finite geometric sums therefore give

\[
\begin{aligned}
\sum_{u\in\{0,1,2,3\}^N}
\zeta^{k\sum_i b_i u_i}
&=\prod_{i=1}^N\frac{1-\zeta^{4k b_i}}{1-\zeta^{k b_i}}\\
&=1.
\end{aligned}
\tag{9}
\]

The last equality holds because \(4b_i\) modulo \(m\) is \(b_{i+2}\), with cyclic subscripts; the numerator factors are a permutation of the denominator factors. This remains true when \(N=2\).

For any residue \(\eta\) modulo \(m\), the identity \(m^{-1}\sum_{k=0}^{m-1}\zeta^{k a}=1\) if \(m\mid a\) and zero otherwise follows from the finite geometric sum. Applying it and then (9),

\[
\#\left\{u\in\{0,1,2,3\}^N:\sum_i b_i u_i\equiv\eta\pmod m\right\}
=\frac{4^N+\sum_{k=1}^{m-1}\zeta^{-k\eta}}{m}
=\begin{cases}
(4^N+m-1)/m=2^N+2,&\eta\equiv0,\\
(4^N-1)/m=2^N+1,&\eta\not\equiv0.
\end{cases}
\tag{10}
\]

Translation of the box shifts \(\eta\) and changes only which residue has the extra point. In particular, every box \(\beta+\{0,1,2,3\}^N\), with \(\beta\in\mathbb Z^N\), contains either \(2^N+1\) or \(2^N+2\) points of the full lattice \(\mathcal L\).

Partition \(\mathbb Z_{\ge0}^N\) into the disjoint boxes \(4u+\{0,1,2,3\}^N\), with \(u\in\mathbb Z_{\ge0}^N\). In the box indexed by \(u\), every support point has weight at most \(q^{4\sum_i u_i}\), and there are at most \(2^N+2\) such points by (10). Summing over all boxes gives the full infinite bound

\[
W\le(2^N+2)\sum_{u\in\mathbb Z_{\ge0}^N}q^{4\sum_i u_i}
=(2^N+2)(1-q^4)^{-N}.
\tag{11}
\]

Put \(t=-\log q\), \(h=2\lceil1/(2t)\rceil\), and \(A=h/2\). Since
\(0<t\le\log(20/19)\le1/19\), we have \(h\ge20\) and \(A\ge10\). Partition the integer box \([-h,h-1]^N\cap\mathbb Z^N\) into \(A^N\) disjoint boxes of side four. Their representative vectors are

\[
\xi_i=-h+2+4\alpha_i,
\qquad \alpha_i\in\{0,\ldots,A-1\},
\qquad
v_i\in\{\xi_i-2,\xi_i-1,\xi_i,\xi_i+1\}.
\tag{12}
\]

The representatives in one coordinate form a symmetric arithmetic progression. We prove that at least \(A^N/40\) of these boxes satisfy \(|\sum_i\xi_i|\le hN/20\).

For integers \(j\ge1\) and \(k\), let \(\nu_j(k)\) count the vectors in \(\{0,\ldots,A-1\}^j\) with coordinate sum \(k\); set it to zero outside the support. These counts are symmetric about \(j(A-1)/2\) and nonincreasing as the distance from this center increases. Here is an elementary induction. For \(j=1\), the counts are constant on their interval of support. Convolution with \(\{0,\ldots,A-1\}\) preserves symmetry, and

\[
\nu_{j+1}(k+1)-\nu_{j+1}(k)
=\nu_j(k+1)-\nu_j(k-A+1).
\tag{13}
\]

If \(k\ge(j+1)(A-1)/2\), then \(k+1\) is at least as far from \(j(A-1)/2\) as \(k-A+1\) is. Indeed, their distance comparison is equivalent to
\(k+1-j(A-1)/2\ge A/2\), which follows from this bound on \(k\). The induction hypothesis makes the right side of (13) nonpositive. Symmetry handles the other half of the support, including the equal middle pair when the center is a half-integer. This proves the claim for every \(j\).

Equation (12) gives \(\sum_i\xi_i=4\sum_i\alpha_i-2N(A-1)\). Thus the desired boxes correspond exactly to the integers \(k\) with

\[
\left|k-\frac{N(A-1)}2\right|\le\frac{AN}{40}.
\tag{14}
\]

The interval in (14) lies inside \([0,N(A-1)]\), since \(A\ge10\). Its radius \(AN/40\) is at least \(1/2\). An interval centered at an integer or half-integer with radius \(u\ge1/2\) contains at least \(u\) integers: for \(1/2\le u<1\) it contains at least one, and for \(u\ge1\) the count is at least \(2u-1\ge u\). Therefore (14) contains at least \(AN/40\) integer positions. There are \(N(A-1)+1\le AN\) positions in the whole support of \(\nu_N\). By the proved symmetry and unimodality, the average of \(\nu_N\) on the central positions is at least its average over the whole support. As \(\sum_k\nu_N(k)=A^N\), the number of boxes satisfying (14) is at least \(A^N/40\), as claimed.

Retain those boxes and take the original center \(J=h\mathbf1\). Each point \(v\) in a retained box satisfies \(|v_i|\le h\) and

\[
\left|\sum_i v_i\right|
\le\left|\sum_i\xi_i\right|+\sum_i|v_i-\xi_i|
\le\left(\frac h{20}+2\right)N.
\tag{15}
\]

Every retained box contains at least \(2^N+1\) points of \(\mathcal L\), by (10). Each such point is an allowed original displacement in (1): its endpoints \(J+v,J-v\) are nonnegative and belong to \(\mathcal L\). Its summand is at least \(q^{((21/20)h+2)N}\), by (15). The boxes are disjoint, so these are distinct terms of the original oriented sum; no identification of \(v\) and \(-v\) or division by two occurs. Consequently

\[
S_{h\mathbf1}
\ge\frac{A^N}{40}(2^N+1)q^{((21/20)h+2)N}.
\tag{16}
\]

Combining (11) and (16), using \(2A=h\), gives

\[
\frac{S_{h\mathbf1}}{2^{-N}W}
\ge\frac1{40}\frac{2^N+1}{2^N+2}
\left[h(1-q^4)q^{(21/20)h+2}\right]^N
\ge\frac1{48}\left[h(1-q^4)q^{(21/20)h+2}\right]^N.
\tag{17}
\]

The last step uses \(2^N\ge4\), so \((2^N+1)/(2^N+2)\ge5/6\).

For completeness, the bracket in (17) has an explicit uniform lower bound greater than one. Put \(x=th\). The choice of \(h\) gives \(1\le x\le1+2t\le21/19\). Also \(e^{-u}\ge1-u\) for \(u\ge0\), so integration gives \(1-e^{-4t}\ge4t-8t^2=4t(1-2t)\). Hence

\[
\begin{aligned}
h(1-q^4)q^{(21/20)h+2}
&=h(1-e^{-4t})e^{-(21/20)x-2t}\\
&\ge4x(1-2t)e^{-(21/20)x-2t}\\
&\ge\frac{68}{19}e^{-481/380}.
\end{aligned}
\tag{18}
\]

Indeed, \(x\ge1\), \(1-2t\ge17/19\), and \((21/20)x+2t\le(21/20)(21/19)+2/19=481/380\). To verify the remaining numerical comparison analytically, use \(49/87>9/16\) and the positive geometric remainder in \((1-u^2)^{-1}\):

\[
\begin{aligned}
\log\frac{68}{19}
&=2\int_0^{49/87}\frac{du}{1-u^2}\\
&>2\int_0^{9/16}(1+u^2+u^4)\,du\\
&=2\left(\frac9{16}+\frac{(9/16)^3}{3}+\frac{(9/16)^5}{5}\right)\\
&=\frac{3319209}{2621440}
=\frac{481}{380}+\frac{19339}{49807360}
>\frac{481}{380}.
\end{aligned}
\tag{19}
\]

It follows that the last expression in (18) is greater than one. Equation (17) proves \(S_{h\mathbf1}/(2^{-N}W)\ge1/48\) for every \(N\ge2\) and \(19/20\le q<1\).

Finally, convergence and attainment retain exactly the interpretation in accepted fact \(6c4f6e6754070930\). They also follow directly here: \(1\le W\le(1-q)^{-N}<\infty\), and for a fixed original center only displacements with \(|v_i|\le J_i\) contribute. Thus

\[
0<w_J\le S_J
\le q^{\sum_iJ_i}\prod_{i=1}^N(2J_i+1)
=\prod_{i=1}^N\bigl[q^{J_i}(2J_i+1)\bigr].
\tag{20}
\]

For fixed \(N,q\), the one-coordinate factors are bounded and tend to zero as their coordinate tends to infinity. The right side therefore tends to zero as \(\|J\|_\infty\to\infty\). Since \(S_0=1\), only finitely many original centers can have score at least one, and the maximum is attained among them. All infinite sums and all original lattice sites are accounted for.

The bounds (4), (8), and (17), together with the singleton argument for \(q\le1/2\), cover every \(q\in(0,1)\). Their common lower constant is \(1/624000000\), proving (2).

## External sources

None. The sole accepted predecessor is cited above. The new finite congruence identity, central-box count, and scalar estimates are proved directly; no numerical sweep, optimization output, or computer-certified finite result is a proof premise.
