---
fact_id: 11cb4cde5378cfcd
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: cap23-product
depends_on: ["488f0a583886b5fc"]
verifier_run: bf850eac21914955
target_match: null
---

## Statement

For every integer \(n\ge1\) and every collection of nonzero, nonnegative, finitely supported tables \(w_i:\mathbb Z\to[0,\infty)\), each agreeing at every integer (zeros included) with a finite-valued log-concave function on \(\mathbb R\), let \(w(z)=\prod_{i=1}^n w_i(z_i)\) and \(W=\sum_z w(z)\). Then
\[
\mathcal B_{\log}^{\mathrm{hit}}(w)\ge e^{-150}2^{-n}W.
\]
Here \(D=\{z:w(z)>0\}\), \(\phi_z=\log(w_{\max}/w_z)\), \(m_{\log}(J,L;w)\), and \(\mathcal B_{\log}^{\mathrm{hit}}(w)=\max_{J\in D,L\ge0}m_{\log}(J,L;w)/(1+L)\) have exactly the meanings of accepted fact `488f0a583886b5fc`. In particular this is the integral hitting score, not the fractional packing score. The source archive's symbol \(\mathcal B(w)\) is an alias for this \(\mathcal B_{\log}^{\mathrm{hit}}(w)\), whereas the canonical unadorned \(B\) remains \(\max_D\phi\). Define \(\alpha(w)=2^n\mathcal B_{\log}^{\mathrm{hit}}(w)/W\) for this proof only. The asserted bound concerns the full arbitrary product class and makes no log-affinity assumption.

## Proof

Normalize the factors to probability tables \(\pi_i=w_i/\sum w_i\). Multiplication by a positive scalar does not change potentials or normalized scores. Their supports are finite integer intervals by `488f0a583886b5fc`; their log probabilities are concave sequences. The product of their extensions is log-concave, so the same accepted fact applies to the product. Write \(m\) for \(m_{\log}\) in the proof, always with its displayed table argument or the current probability table.

1. Cap products and reflection.

Equation (15) of `488f0a583886b5fc` gives equivalently
\[
m(J,L;w)=\inf_{b\in\mathbb R^n}\sum_{z:\ \phi_z-\phi_J-b\cdot(z-J)\le L}w_z.
\tag{1}
\]
Indeed the normals with positive last coordinate are precisely these cuts. Every vertical cut in (15) contains one of these cuts: multiply its horizontal normal by a sufficiently large positive scalar to exclude all points strictly outside the vertical cut. There are finitely many such points, and points on the vertical boundary that the resulting cut might exclude cause no problem. Thus adding vertical cuts does not lower the infimum in (1).

For two product blocks and prescribed nonnegative levels \(L_1,L_2\), every cap at the product center and level \(L_1+L_2\) contains the Cartesian product of the two caps with the corresponding slopes and levels. Hence
\[
m((J_1,J_2),L_1+L_2;w_1\otimes w_2)\ge m(J_1,L_1;w_1)m(J_2,L_2;w_2).
\tag{2}
\]
Since \(1+L_1+L_2\le(1+L_1)(1+L_2)\), this proves \(\alpha(w_1\otimes w_2)\ge\alpha(w_1)\alpha(w_2)\). Iteration applies to any finite partition into blocks.

For any table and any center \(J\), put
\(H_J(v)=(\phi_{J+v}+\phi_{J-v})/2-\phi_J\) whenever both endpoints are in \(D\). This is nonnegative. Its exact normalization relative to the canonical curvature quantity is \(H_J(v)=\Delta_J(v)/2\), where \(\Delta_J(v)=\log(w_J^2/(w_{J+v}w_{J-v}))\). Every hitting set at level \(L\) contains \(J\), and meets every pair \(\{J+v,J-v\}\), \(v\ne0\), with \(H_J(v)\le L\). These pairs are mutually disjoint when indexed without orientation. Consequently
\[
m(J,L;w)\ge\frac12\sum_{v:\ J\pm v\in D}\min(w_{J+v},w_{J-v})\,\mathbf1_{\{H_J(v)\le L\}}.
\tag{3}
\]
This follows directly from the singleton and two-point members of the defining family in the accepted fact, so it does not assume a fractional/integral equivalence.

For a one-dimensional probability factor at center \(J_i\), define, on its symmetric displacement support,
\[
s_i(k)=\sqrt{\pi_i(J_i+k)\pi_i(J_i-k)},\quad
H_i(k)=\log\frac{p_i}{s_i(k)},\quad
a_i(k)=\frac12\log\frac{\pi_i(J_i-k)}{\pi_i(J_i+k)},\quad
p_i=\pi_i(J_i),\quad \beta_i=\sum_k s_i(k).
\]
Thus \(\beta_i\) is the source's Bhattacharyya coefficient \(\mathrm{BC}_i\); it is not a cap slope. The function \(H_i\) is even and convex as a sequence, \(H_i(0)=0\), and \(a_i\) is odd. Let \(Z_i\) be independent with law \(s_i/\beta_i\), let \(A=\sum_i a_i(Z_i)\), and put \(\gamma_i=\log(2\beta_i)\). Applying (3) and \(\min(u,v)=\sqrt{uv}\exp(-|\log(u/v)|/2)\) gives
\[
\frac{2^n m(J,L;w)}W\ge\frac12\exp\Bigl(\sum_i\gamma_i\Bigr)
\mathbb E\left[e^{-|A|}\mathbf1_{\{\sum_i H_i(Z_i)\le L\}}\right].
\tag{4}
\]
Conditional on all \(|Z_i|\), the signs of the nonzero displacements are independent fair signs. Thus all subsequent estimates are independent of the cap slope.

2. Elementary one-dimensional estimates.

For a log-concave probability sequence write \(F(k)=\sum_{t\le k}\pi(t)\), \(S(k)=\sum_{t\ge k}\pi(t)\). The ratios \(\pi(k+j)/\pi(k)\) are nonincreasing in \(k\) for each \(j\ge0\), by multiplying successive nonincreasing adjacent ratios. Summing shows that \(S(k)/\pi(k)\) is nonincreasing. Reversing the sequence shows that \(F(k)/\pi(k)\) is nondecreasing. In particular the outward right and left hazards are nondecreasing.

If \(J\) is a median, meaning \(F(J),S(J)\ge1/2\), then \(p=\pi(J)\ge\pi_{\max}/2\). To see this, choose a mode \(M\). If \(M\ge J\), use \(F(J)/p\le F(M)/\pi_{\max}\le1/\pi_{\max}\); if \(M\le J\), use the analogous inequality for \(S\). Therefore \(\phi(J)\le\log2\). Since both endpoint potentials are nonnegative, \(H(k)\pm a(k)\ge-\phi(J)\), so
\( |a(k)|\le H(k)+\log2\).

For every center, not necessarily a median, the law \(Z\) above satisfies, with \(q=\Pr(Z\ne0)\),
\[
\Pr(H(Z)>t)\le\min(q,4e^{-t}),\qquad
\mathbb EH(Z)\le q(1+\log(4/q))\le1+\log4.
\tag{5}
\]
The expectation is zero when \(q=0\). Here is a proof of the tail bound. It is trivial for \(t<\log2\). Otherwise let \(r\) be the largest nonnegative support integer with \(H(r)\le t\); if all support is included there is no tail. If \(r=0\), convexity bounds the unnormalized tail \(2\sum_{k\ge1}e^{-H(k)}\) by \(2e^{-t}/(1-e^{-t})\le4e^{-t}\), while the mass at zero is one. If \(r\ge1\), convexity beyond \(r+1\) bounds this tail by \(2e^{-t}/(1-e^{-t/(r+1)})\). Inside, convexity gives \(H(k)\le kt/r\) for \(0\le k\le r\), and, because \(e^{-t}\le1/2\),
\(1+2\sum_{k=1}^r e^{-kt/r}\ge1/(1-e^{-t/r})\).
Their ratio is at most \(2e^{-t}(r+1)/r\le4e^{-t}\): the inequality used is \((1-e^{-ay})/(1-e^{-y})\le a\) for \(a\ge1\), which follows by integrating the decreasing function \(e^{-u}\) over the two intervals. This ratio bounds the normalized tail. Finally integrate \(\min(q,4e^{-t})\) over \(t\ge0\); the last bound in (5) follows since \(q(1+\log(4/q))\) is increasing on \([0,1]\).

Suppose now that \(J\) is a median and \(p<1/2\). Put \(\eta=\log(\beta/p)\), \(\delta=-\log(2p)\), so \(\gamma=\eta-\delta\) and \(q=1-e^{-\eta}\). Both neighbors of \(J\) exist, since the strict side masses \(T_+,T_-\) are each at least \(1/2-p>0\). Hazard monotonicity gives
\(\pi(J+1)\ge pT_+/(p+T_+)\) and its left analogue. Let \(h(T)=T/(p+T)\). As \(\max(T_+,T_-)\ge(1-p)/2\) and \(p<1/2\), we have \(h(\max T)>1/3\); also \(h(\min T)\ge h(1/2-p)=1-2p\). Hence
\[
(e^\eta-1)^2\ge4h(T_+)h(T_-) >\frac43(1-2p).
\tag{6}
\]
In particular \(\eta>0\). For \(0<\eta\le1/5\), the power series bound \(e^\eta\le1/(1-\eta)\) implies \(e^\eta-1\le5\eta/4\). Set \(y=3(e^\eta-1)^2/4\); then \(y\le75\eta^2/64\le3/64\). Using \(-\log(1-y)\le y/(1-y)\) in (6) gives
\[
\delta\le\frac{75}{61}\eta^2<\frac54\eta^2,\qquad
\gamma\ge\frac34\eta,\qquad
\frac9{10}\eta\le q\le\eta.
\tag{7}
\]
For the last assertion use \(e^{-\eta}\le1-\eta+\eta^2/2\) and \(e^{-\eta}\ge1-\eta\). These follow, for example, by twice differentiating the corresponding differences.

3. A uniform Bhattacharyya gain for wide factors.

We prove that at a median with \(p<1/2\) and \(\eta\ge1/5\),
\[
\beta\ge13/25,\qquad \gamma\ge\log(26/25)\ge1/26.
\tag{8}
\]
All numerical assertions in this step are certified below with rational arithmetic.

First the neighbor estimate above and concavity of \(\log h(T)\) yield
\[
\beta\ge B_1(p):=p\left(1+2\sqrt{\frac{1-2p}{1+2p}}\right).
\tag{9}
\]
Indeed \(T_++T_-=1-p\), each \(T_\pm\ge1/2-p\), and a concave function on this segment has its minimum at an endpoint. Thus \(h(T_+)h(T_-)\) is at least its value at \((1/2,1/2-p)\), namely \((1-2p)/(1+2p)\). Retain only \(s(0),s(1),s(-1)\) in \(\beta\).

A second bound, useful for small \(p\), is
\[
\beta\ge B_{\rm HM}(p):=p+(1+p)\log(2(1-p))
+\frac{p(1+2p)}{1-2p}\log(4p(1-p)).
\tag{10}
\]
We derive it completely. Put \(S_k=\Pr(Y\ge J+k)\), \(U_k=\Pr(Y\le J-k)\), \(C_k=\sqrt{S_kU_k}\), and, while \(C_k>0\), let \(\mu_k=\pi(J+k)/S_k\), \(\nu_k=\pi(J-k)/U_k\). They are nondecreasing in \(k\). We have
\[
s(k)=C_k\sqrt{\mu_k\nu_k},\quad
C_{k+1}=C_k\sqrt{(1-\mu_k)(1-\nu_k)},\quad
s(k)=R(\mu_k,\nu_k)(C_k-C_{k+1}),
\]
where \(R(u,v)=\sqrt{uv}/(1-\sqrt{(1-u)(1-v)})\), for \(u,v\in(0,1]\).

Let \(\rho=\pi(J+1)/p\). Log-concavity gives \(\pi(J+k)\le p\rho^k\). The left hazard inequality gives \(\pi(J-1)\ge p(1-\nu_0)\); log-concavity then gives \(\rho\le1/(1-\nu_0)\). Also \(U_k\le U_0(1-\nu_0)^k\). It follows that \(C_k^2\mu_k=\pi(J+k)U_k\le pU_0=C_0^2\mu_0\). The symmetric estimate holds for \(\nu_k\). Thus, writing \(c_k=C_k/C_0\), both hazards lie in \([m_0,\min(1,M_0/c_k^2)]\), with \(m_0=\min(\mu_0,\nu_0)\), \(M_0=\max(\mu_0,\nu_0)\).

Direct differentiation shows that \(\partial_v\log R(u,v)\) has the sign of \(u-v\). Symmetry and \(R(u,u)=1\) therefore show that the minimum of \(R\) on \([m,M]^2\) is \(R(m,M)\); this value increases with \(m\) and decreases with \(M\). Consequently \(\psi(c)=R(m_0,\min(1,M_0/c^2))\) is nondecreasing. Summing over the finite decreasing sequence \(c_0=1,c_1,\ldots,0\) gives an upper-end Riemann sum, whence
\(\sum_{k\ge0}s(k)\ge C_0\int_0^1\psi(c)\,dc\).
At a median \(S_0,U_0\in[1/2,1/2+p]\) and \(S_0+U_0=1+p\). Therefore \(m_0\ge2p/(1+2p)\), \(M_0\le2p\), \(2C_0\ge\sqrt{1+2p}\), and
\[
\beta\ge\sqrt{1+2p}\int_0^1
R\left(\frac{2p}{1+2p},\min(1,2p/c^2)\right)dc-p.
\tag{11}
\]
For \(x=1-u,y=1-v\), the inequality \(\sqrt{xy}\ge2xy/(x+y)\), interpreted by continuity when necessary, gives
\(R(u,v)\ge\sqrt{uv}(2-u-v)/(u+v-2uv)\).
Set \(r=2p\). On \(0\le c\le\sqrt r\), the integrand in (11), including the factor \(\sqrt{1+2p}\), is exactly \(\sqrt r\). On \(\sqrt r\le c\le1\), the displayed lower bound for this integrand is
\[
\frac{(2+r)c^2-r(1+r)}{c(c^2+1-r)}
=-\frac{r(1+r)}{1-r}\frac1c+\frac2{1-r}\frac{c}{c^2+1-r}.
\]
Integrating these terms and subtracting \(p\) gives
\(p+\log(2-2p)/(1-2p)+p(1+2p)\log(2p)/(1-2p)\), which equals (10) after collecting the logarithms. This proves (10) without relying on symbolic software.

Here is the finite certificate for \(B_{\rm HM}(p)>13/25\) on \((0,1/4]\) and \(B_1(p)>13/25\) on \([1/4,11/25]\). It uses only the Python standard library and exact fractions. The code was executed successfully as printed. Its output was:

```text
exact certificate passed: 125 HM cells and 95 B1 cells
```

For completeness, the justification of its interval bounds is as follows. For \(1\le x\le2\), setting \(u=(x-1)/(x+1)\in[0,1/3]\), the first twenty terms of \(\log x=2\sum_{j\ge0}u^{2j+1}/(2j+1)\) give a lower bound, and the remainder is at most \(2u^{41}/(41(1-u^2))\). Binary scaling extends these rational enclosures to every positive rational. On a cell \([a,b]\subset(0,1/4]\), the first term of (10) is at least \(a\), the second term is at least \((1+b)\log(2(1-b))\), since its derivative is negative, and the negative final term is at least
\(b(1+2b)\log(4a(1-a))/(1-2b)\).
Here the positive coefficient is increasing and \(\log(4p(1-p))<0\) is increasing. On the initial interval \((0,b]\), use \(4p(1-p)\ge2p\) and that \(p\log(1/(2p))\) is increasing up to \(1/(2e)\); the chosen \(b=1/500\) is below that value. For example \(e<3\), directly from its factorial series, suffices to check this. These give exactly the first-cell bound below. Finally (9) on \([a,b]\) is bounded below by \(a+2a\sqrt{(1-2b)/(1+2b)}\); squaring its comparison with \(13/25\) is valid since \(a<13/25\). Thus every assertion below is a rational inequality implying the required inequality on its entire closed cell. The first cell includes every strictly positive point down to zero; no endpoint is constructed from a floating-point number.

```python
from fractions import Fraction as Q

def unit_log(x):
    u = (x - 1) / (x + 1)
    lo = 2 * sum((u ** (2*j + 1) / Q(2*j + 1)
                  for j in range(20)), Q(0))
    return lo, lo + 2*u**41 / (41*(1-u*u))

L2, U2 = unit_log(Q(2))
def log_bounds(x):
    k = 0
    while x < 1:
        x *= 2
        k -= 1
    while x > 2:
        x /= 2
        k += 1
    a, b = unit_log(x)
    return a + min(k*L2, k*U2), b + max(k*L2, k*U2)

b = Q(1, 500)
first = ((1+b)*log_bounds(2*(1-b))[0]
         - (1+2*b)/(1-2*b)*b*log_bounds(1/(2*b))[1])
assert first > Q(13, 25)
for i in range(1, 125):
    a, b = Q(i, 500), Q(i+1, 500)
    lo = (a + (1+b)*log_bounds(2*(1-b))[0]
          + b*(1+2*b)/(1-2*b)*log_bounds(4*a*(1-a))[0])
    assert lo > Q(13, 25)
for i in range(95):
    a, b = Q(1, 4)+Q(i, 500), Q(1, 4)+Q(i+1, 500)
    assert 4*a*a*(1-2*b) > (Q(13, 25)-a)**2*(1+2*b)
print('exact certificate passed: 125 HM cells and 95 B1 cells')
```

For \(p\ge11/25\) and \(\eta\ge1/5\), simply use \(\beta=pe^\eta\ge(11/25)(6/5)=66/125>13/25\). This and the certificate prove the first assertion of (8). The last assertion follows by integrating \(1/t\) on \([1,26/25]\), where it is at least \(25/26\).

4. Sign cancellation.

If \(|c_i|\le c\) for \(1\le i\le N\) and the \(\varepsilon_i\) are independent fair signs, then
\[
\Pr\left(\left|\sum_i\varepsilon_i c_i\right|\le c\right)\ge\frac1{N+1}.
\tag{12}
\]
Starting from any sign vector, flip its first \(j\) signs, for \(j=0,\ldots,N\). The sum moves from its initial value to its negative in jumps of magnitude at most \(2c\). At least one visited sum therefore lies in \([-c,c]\). Each of these \(N+1\) flip maps preserves the uniform measure on sign vectors; a union bound proves (12). The assertion also holds for \(N=0\), with empty sum zero.

5. Wide blocks, uniformly in their size.

For each factor whose maximum atom is less than \(1/2\), choose a median center. Call it wide if \(\eta>1/5\). For a block of \(k\ge1\) wide factors, (8) gives \(\sum\gamma_i\ge k/26\). By (5) and Markov's inequality, the event \(\sum H_i\le4k(1+\log4)\) has probability at least \(3/4\). The union bound and (5) show that \(\max H_i\le\log(16k)\) also has probability at least \(3/4\). Their intersection, which depends only on the magnitudes, has probability at least \(1/2\). On it, \(|a_i(Z_i)|\le\log(32k)\). Conditional sign cancellation (12) then gives probability at least \(1/(k+1)\) that \(|A|\le\log(32k)\). Using (4) at \(L=4k(1+\log4)\) gives
\[
\alpha(\text{wide block})\ge
\frac{e^{k/26}}{128k(k+1)(1+4k(1+\log4))}.
\tag{13}
\]
This bound is uniform over all positive integers \(k\), with no finite dimension scan. Indeed \(\log4<3/2\), since \(1+3/2+(3/2)^2/2+(3/2)^3/6>4\). Thus the denominator is at most \(2816k^3\). The positive exponential series gives \(e^{k/26}\ge k^3/(6\cdot26^3)\). Therefore (13) is at least \(1/(16896\cdot26^3)>2^{-29}>e^{-29}\); the integer comparison is \(16896\cdot26^3=296964096<536870912=2^{29}\).

6. Narrow blocks and their sparse remainder.

For \(j=0,1,\ldots\), let \(G_j\) consist of the remaining median factors with
\(\eta_i\in(2^{-j}/10,2^{-j}/5]\). These intervals partition all \(0<\eta_i\le1/5\). Let \(s\) be the number of factors in one nonempty group, and \(\mu=\sum_{i\in G_j}q_i>0\). From (7),
\[
s\le12\mu2^j,\qquad
\sum_{i\in G_j}\gamma_i\ge3\mu/4,\qquad
\mathbb E\sum_{i\in G_j}H_i\le\mu(j+5).
\tag{14}
\]
For the first bound use \(q_i>(9/100)2^{-j}\). For the last, (5) and the same lower bound give \(1+\log(4/q_i)\le1+\log(400/9)+j\log2<5+j\). Here \(\log2<1\), and \(e^4>400/9\), as is already shown by \(e>8/3\) and \((8/3)^4>400/9\).

Call \(G_j\) dense if \(\mu\ge100(j+1)\). Let \(N\) count its nonzero displacements. Markov's inequality for \(N\) and \(\sum H_i\), and the union bound for \(\max H_i\), show that the three events
\(N\le4\mu\), \(\sum H_i\le4\mu(j+5)\), and \(\max H_i\le\log(16s)\)
hold simultaneously with probability at least \(1/4\). Conditional on magnitudes, use (12) with at most \(4\mu\) signs and \(c=\log(32s)\). Formula (4), now with \(L=4\mu(j+5)\), yields
\[
\alpha(G_j)\ge
\frac{e^{3\mu/4}}{256s(4\mu+1)(1+4\mu(j+5))}
\ge\frac{e^{3\mu/4}}{76800\mu^3(j+5)2^j}\ge1.
\tag{15}
\]
For the second inequality use (14), \(4\mu+1\le5\mu\), and \(1+4\mu(j+5)\le5\mu(j+5)\), since \(\mu\ge100\). To prove the last inequality for every \(j\ge0\), first take \(\mu=100(j+1)\). Its denominator is at most
\(384000000000(j+1)^4 2^j\), whose logarithm is less than \(40+5j\), using \(e>2\), \(2^{40}>384000000000\), \(\log(j+1)\le j\), and \(\log2<1\). This is less than \(75(j+1)=3\mu/4\). For larger \(\mu\), the logarithm of the final ratio in (15) has derivative \(3/4-3/\mu>0\). This proves (15) on the whole unbounded range without numerical scanning.

Collect all non-dense \(G_j\) into one sparse block. At the product of its chosen medians, the singleton belongs to every hitting set already at level zero. Its normalized coefficient is consequently at least \(\prod_i2p_i=\exp(-\sum_i\delta_i)\). By (7) and the upper endpoints of the dyadic intervals,
\[
\sum_{\text{sparse }i}\delta_i
\le\frac14\sum_{j\ge0}2^{-j}\sum_{i\in G_j}\eta_i
\le\frac5{18}\sum_{j\ge0}2^{-j}\mu_j
<\frac{250}{9}\sum_{j\ge0}(j+1)2^{-j}
=\frac{1000}{9}<112.
\tag{16}
\]
Only non-dense groups are included; extending to all \(j\ge0\) merely bounds the sum above. The geometric-series identity in (16) follows by differentiating the finite-radius geometric series, or directly by summing \(j+1\) copies of each power of \(1/2\). Thus the sparse block has coefficient at least \(e^{-112}\).

7. Completion.

If a factor has an atom of mass at least \(1/2\), choose a mode for its center. Its singleton at level zero gives coefficient at least one. Partition the coordinates into these atom factors, the wide block (if nonempty), the finitely many nonempty dense groups, and the sparse block (if nonempty). Every remaining factor has maximum atom below \(1/2\), so all the median lemmas apply and \(\eta>0\); the partition is exhaustive. Empty blocks contribute the neutral factor one and need no separate definition of a zero-dimensional score.

Multiply the block bounds using (2). Dense groups and atom factors contribute at least one, the wide block contributes at least \(e^{-29}\), and the sparse block contributes at least \(e^{-112}\). Therefore \(\alpha(w)\ge e^{-141}\ge e^{-150}\), proving the stated theorem for all finite products and all dimensions. No assertion about arbitrary nonproduct tables or about the locked full conjecture is used or concluded.

## External sources

None. Accepted fact `488f0a583886b5fc` supplies the canonical definitions, support and convexity facts, and cap identity. The unaccepted archive `.math-prover/source_archives/2026-09-23-cap-gain/handoff.md`, Sections 1-4 and Appendix A.1/A.3, supplied the strategy; every additional assertion used from that strategy has been proved above, and its rounded numerical constants and floating-point endpoint construction have been replaced.
