---
fact_id: dbcf5be1e541e0cf
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct21-four-site-fixed-profile-joint-moment
depends_on: ["0cd230a98ae241c3"]
verifier_run: 22297426e89d40ba
target_match: null
---

## Statement

Let \(k\ge1\) and \(T\ge0\) be integers and let \(\beta\ge0\) be real. Define \(g\) on \(\lbrace0,1,2,3\rbrace\) by
$$
g(0)=0,\qquad g(1)=1,\qquad g(2)=2,\qquad g(3)=4.
$$
For \(\mathbf x\in\lbrace0,1,2,3\rbrace^k\), put \(\Gamma(\mathbf x)=\sum_{i=1}^k g(x_i)\), and define the original finite epigraph, its complete normalizer, and its probability law by
$$
\begin{aligned}
A_T&=\lbrace(\mathbf x,t):\mathbf x\in\lbrace0,1,2,3\rbrace^k,
\ t\in\mathbb Z,\ \Gamma(\mathbf x)\le t\le T\rbrace,\\
Z&=\sum_{(\mathbf x,t)\in A_T}e^{-\beta t},\qquad
p_{(\mathbf x,t)}=\frac{e^{-\beta t}}Z\quad((\mathbf x,t)\in A_T).
\end{aligned}
\tag{1}
$$
For every original atom \(\mathbf z\), let
$$
\tau_p(\mathbf z)=\inf_{H\ni\mathbf z}\sum_{\mathbf v\in A_T\cap H}p_{\mathbf v},
\qquad
M_3(p)=\sum_{\mathbf z\in A_T}p_{\mathbf z}\tau_p(\mathbf z)^3,
\tag{2}
$$
where the infimum is over all closed affine halfspaces in \(\mathbb R^{k+1}\) containing \(\mathbf z\). Then
$$
M_3(p)\ge\frac{2^{-96}}{3584}\,8^{-k}
\ge2^{-105}\,8^{-(k+1)}.
\tag{3}
$$
More precisely, put \(f_E=\sum_{t=E}^T e^{-\beta t}\) for integers \(0\le E\le T\), and put \(f_E=0\) for integers \(E>T\). Define a table on \(\mathbb Z^k\) by \(a_{\mathbf x}=f_{\Gamma(\mathbf x)}\) on the displayed spatial box and zero outside it. With the exact finite-table notation of accepted fact `0cd230a98ae241c3`, namely
$$
\begin{aligned}
D_a&=\lbrace\mathbf x:a_{\mathbf x}>0\rbrace,&
M_a&=\sum_{\mathbf x}a_{\mathbf x}=Z,&
a_{\max}&=\max_{\mathbf x}a_{\mathbf x},\\
A^a_\omega&=\lbrace\mathbf x:a_{\mathbf x}\ge\omega\rbrace,&
r^a_\omega(\mathbf q)&=|A^a_\omega\cap(2\mathbf q-A^a_\omega)|,\\
E(a)&=\sum_{\mathbf q\in D_a}
\max_{0<\omega\le a_{\mathbf q}}\omega^4r^a_\omega(\mathbf q)^3,
\end{aligned}
\tag{4}
$$
one has
$$
E(a)\ge2^{-96}\,8^{-k}Z^4,
\qquad
M_3(p)\ge\frac{E(a)}{3584Z^4}.
\tag{5}
$$
The \(Z\) in every formula is the full original normalizer (1). The locked symbols \(n,d,C,W,c_0\) retain their original meanings and are not auxiliary quantities here. No evenness hypothesis on \(g\) is made. The conclusion includes \(T=0\), \(\beta=0\), singleton height intervals, and equality at all energy, height, and halfspace boundaries.

## Proof

The original support is finite and contains \((\mathbf0,0)\), so \(0<Z<\infty\). The linear interpolation \(\widetilde g\) of \(g\) on \([0,3]\) has slopes \(1,1,2\), hence is convex and nonnegative, with \(\widetilde g(0)=0\). In particular
$$
\lbrace(\mathbf x,t):\mathbf x\in[0,3]^k,
\ \textstyle\sum_i\widetilde g(x_i)\le t\le T\rbrace
$$
is compact and convex and its lattice points are exactly \(A_T\). The proof below uses the probabilities in (1) without conditioning on a spatial subfamily.

Write \(r=e^{-\beta}\), so \(0<r\le1\). The profile \(f_E=\sum_{t=E}^T r^t\) is positive on \(\lbrace0,\ldots,T\rbrace\) and strictly decreasing there, since \(f_E-f_{E+1}=r^E\). For \(1\le E<T\), using \((1-r)f_E=r^E-r^{T+1}\), which also holds when \(r=1\), gives
$$
\begin{aligned}
f_E^2-f_{E-1}f_{E+1}
&=f_E^2-(f_E+r^{E-1})(f_E-r^E)\\
&=r^{2E-1}-(1-r)r^{E-1}f_E
=r^{E+T}>0.
\end{aligned}
\tag{6}
$$
Thus the finite profile is nonincreasing and logconcave. Its total spatial table mass is exactly the mass in (1): summing the height tail separately over each spatial site gives \(M_a=Z\). If \(T=0\), both tables are singletons, \(E(a)=Z^4=1\), and \(M_3(p)=1\). Henceforth suppose \(T\ge1\).

We first establish the spatial energy estimate. We will use only the positivity, nonincrease, and logconcavity of \(f_0,\ldots,f_T\) until returning to the height variable.

For \(0<\omega\le f_0\), let \(t_\omega\) be the largest index in \(\lbrace0,\ldots,T\rbrace\) with \(f_{t_\omega}\ge\omega\). The exact weak level is
$$
A^a_\omega
=\lbrace\mathbf x\in\lbrace0,1,2,3\rbrace^k:
\Gamma(\mathbf x)\le t_\omega\rbrace.
\tag{7}
$$
If two sites in this level have an integer midpoint, that midpoint lies in the same box, and convexity of \(\widetilde g\) gives its energy at most the average of the endpoint energies. Every positive level is therefore integer-midpoint-closed. Also \(a_{\max}=f_0\). The maximum in (4) is attained: replacing any allowed \(\omega\) by the smallest positive attained table value at least \(\omega\) leaves its level unchanged, weakly increases \(\omega\), and keeps it at most \(a_{\mathbf q}\). This also accounts for tied table values.

All finite-table hypotheses of accepted `0cd230a98ae241c3` now hold with exactly the same meanings and normalizations of \(k,a,D_a,M_a,a_{\max},A^a_\omega,r^a_\omega,E(a)\). Its finite-table conclusion gives
$$
E(a)\ge\frac{512}{19683(1+\chi(a))^3}\,8^{-k}M_a^4,
\qquad
\chi(a)=\frac1{M_a}\sum_{\mathbf x\in D_a}
a_{\mathbf x}\log\frac{f_0}{a_{\mathbf x}}.
\tag{8}
$$
No actual-body conclusion of that predecessor is used.

For a dimension-dependent bound on this spread, let \(\phi\) be the piecewise linear interpolation of \(-\log(f_t/f_0)\) on \([0,T]\). Its slopes \(\log(f_t/f_{t+1})\) are nonnegative and nondecreasing, so \(\phi\) is convex, nondecreasing, and zero at zero. Normalize only the auxiliary table by \(u_{\mathbf x}=a_{\mathbf x}/f_0\), and put \(M_u=M_a/f_0\). Define rounding toward zero on the spatial box by \(F(\mathbf x)_i=\lfloor x_i/2\rfloor\). Since each coordinate is nonnegative, convexity of \(\widetilde g\) and \(\widetilde g(0)=0\) give
$$
g(F(\mathbf x)_i)\le\tfrac12g(x_i),\qquad
\Gamma(F(\mathbf x))\le\tfrac12\Gamma(\mathbf x).
$$
For example, the only nonzero rounded value is \(g(1)=1\), coming from an original coordinate \(2\) or \(3\), whose costs are \(2\) and \(4\). Thus \(F(D_a)\subseteq D_a\), and convexity and nonincrease of the profile imply
$$
\phi(\Gamma(F(\mathbf x)))\le\tfrac12\phi(\Gamma(\mathbf x)),
\qquad
\sqrt{u_{\mathbf x}}\le u_{F(\mathbf x)}.
\tag{9}
$$
All arguments of \(\phi\) remain in \([0,T]\). Each coordinate value has at most two preimages, so each vector has at most \(2^k\le3^k\) preimages. Summing (9) and applying Jensen under the full original spatial law \(a_{\mathbf x}/M_a=u_{\mathbf x}/M_u\) gives
$$
\sum_{\mathbf x\in D_a}\sqrt{u_{\mathbf x}}\le3^kM_u,
\qquad
e^{\chi(a)/2}\le\frac1{M_u}\sum_{\mathbf x\in D_a}\sqrt{u_{\mathbf x}}\le3^k.
$$
Consequently
$$
\chi(a)\le2k\log3,
\qquad
\frac{E(a)}{M_a^4}\ge
\frac{512}{19683(1+2k\log3)^3}\,8^{-k}.
\tag{10}
$$

We next prove the scalar input that supplies a uniform estimate in large dimension. Extend \(g\) by \(+\infty\) outside \(\lbrace0,1,2,3\rbrace\). For \(s>0\), define
$$
\begin{aligned}
Z_g(s)&=\sum_{j=0}^3e^{-sg(j)},\\
I_j&=\lbrace v\in\mathbb Z:j+v,j-v\in\lbrace0,1,2,3\rbrace\rbrace,\\
K_s(j)&=\sum_{v\in I_j}
\exp\!\left[-\frac{2s}{3}(g(j+v)+g(j-v))\right],\\
P_g(s)&=\sum_{j=0}^3K_s(j)^3.
\end{aligned}
\tag{11}
$$
The exact admissible displacements are \(I_0=I_3=\lbrace0\rbrace\) and \(I_1=I_2=\lbrace-1,0,1\rbrace\). With \(x=e^{-s/3}\), direct substitution gives
$$
\begin{aligned}
(K_s(0),K_s(1),K_s(2),K_s(3))
&=(1,3x^4,x^8+2x^{10},x^{16}),\\
P_g(s)&=1+27x^{12}+x^{24}+6x^{26}+12x^{28}+8x^{30}+x^{48},\\
Z_g(s)&=1+x^3+x^6+x^{12}.
\end{aligned}
\tag{12}
$$
We prove the full scalar surplus
$$
P_g(s)\ge\frac16Z_g(s)^4.
\tag{13}
$$
Here is a complete integer polynomial certificate, with the exact arithmetic verification below. Let \(Q(x)=6P_g(s)-Z_g(s)^4\), interpreting the right side through (12) as a polynomial in \(x\). Its nonzero power coefficients \(q_j\), indexed by \(j\), are
$$
\begin{array}{c|rrrrrrrrr}
j&0&3&6&9&12&15&18&21&24\\ \hline
q_j&5&-4&-10&-16&139&-28&-34&-32&-25
\end{array}
\qquad
\begin{array}{c|rrrrrrrrr}
j&26&27&28&30&33&36&39&42&48\\ \hline
q_j&36&-24&72&26&-12&-10&-4&-4&5
\end{array}
\tag{14}
$$
All other coefficients between zero and degree \(48\) are zero. For each \(0\le i\le48\), put
$$
N_i=\sum_{j=0}^i q_j\binom{48-j}{i-j}.
\tag{15}
$$
Their values, in increasing index order, are the following positive integers; each row continues the preceding row:
$$
\begin{array}{r|rrrrrrr}
0\text{--}6&5&240&5640&86476&972720&8557560&61300790\\
7\text{--}13&367548960&1881849324&8352838144&32520941076&112105270524&344745415855&951609403044\\
14\text{--}20&2369811306168&5346750182104&10967267394204&20510884476096&35056014082478&54858533732124&78714903173478\\
21\text{--}27&103671416083688&125414993100042&139404161339820&142377053793365&133569041205720&115029235686846&90859755889428\\
28\text{--}34&65756920981950&43555461424200&26380239017336&14604907829112&7397007800850&3436893998484&1473298391574\\
35\text{--}41&587864106684&220658087744&78536905692&26485432620&8352396244&2405605941&614844468\\
42\text{--}48&135410582&24975228&3750825&444888&39888&2448&80
\end{array}
\tag{16}
$$
The identity
$$
x^j=x^j\bigl(x+(1-x)\bigr)^{48-j}
=\sum_{i=j}^{48}\binom{48-j}{i-j}x^i(1-x)^{48-i}
$$
proves directly from (14)-(15) that
$$
Q(x)=\sum_{i=0}^{48}N_i x^i(1-x)^{48-i}.
\tag{17}
$$
Every term on the right is nonnegative on \([0,1]\), so (13) follows. This is an exact sign certificate, without a floating-point positivity test.

For reproducibility, the following self-contained rational Python calculation first expands \(6P-Z_g^4\), then produces (15), checks every integer in (16), and checks the minimum of the normalized degree-48 Bernstein coefficients of \(P-Z_g^4/6\):

```python
from fractions import Fraction
from math import comb


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] += u * v
    return out


zg = [0] * 13
for j in (0, 3, 6, 12):
    zg[j] = 1
zg4 = multiply(multiply(zg, zg), multiply(zg, zg))
power_p = [0] * 49
for j, v in ((0, 1), (12, 27), (24, 1), (26, 6),
             (28, 12), (30, 8), (48, 1)):
    power_p[j] = v
q = [6 * power_p[j] - zg4[j] for j in range(49)]
expected_q = {0: 5, 3: -4, 6: -10, 9: -16, 12: 139,
              15: -28, 18: -34, 21: -32, 24: -25,
              26: 36, 27: -24, 28: 72, 30: 26, 33: -12,
              36: -10, 39: -4, 42: -4, 48: 5}
assert q == [expected_q.get(j, 0) for j in range(49)]
numerators = [sum(q[j] * comb(48 - j, i - j)
                  for j in range(i + 1)) for i in range(49)]
expected_numerators = [
    5, 240, 5640, 86476, 972720, 8557560, 61300790,
    367548960, 1881849324, 8352838144, 32520941076,
    112105270524, 344745415855, 951609403044,
    2369811306168, 5346750182104, 10967267394204,
    20510884476096, 35056014082478, 54858533732124,
    78714903173478, 103671416083688, 125414993100042,
    139404161339820, 142377053793365, 133569041205720,
    115029235686846, 90859755889428, 65756920981950,
    43555461424200, 26380239017336, 14604907829112,
    7397007800850, 3436893998484, 1473298391574,
    587864106684, 220658087744, 78536905692,
    26485432620, 8352396244, 2405605941, 614844468,
    135410582, 24975228, 3750825, 444888, 39888, 2448, 80
]
assert numerators == expected_numerators
assert all(v > 0 for v in numerators)
bernstein = [Fraction(numerators[i], 6 * comb(48, i))
             for i in range(49)]
assert min(bernstein) == Fraction(5443186173, 10718236072)
assert bernstein.index(min(bernstein)) == 35
```

We also need scalar moment and high-rate estimates for the same kernel. For \(j\in\lbrace0,1,2,3\rbrace\) and \(v\in I_j\), define the excess and imbalance
$$
e_j(v)=\frac{g(j+v)+g(j-v)}2-g(j),
\qquad
b_j(v)=\frac{g(j+v)-g(j-v)}2.
\tag{18}
$$
Convexity gives \(e_j(v)\ge0\). Put
$$
H_s(j)=\sum_{v\in I_j}e^{-(4s/3)e_j(v)},
\qquad
Q_s(j)=\frac{K_s(j)^3}{P_g(s)}.
\tag{19}
$$
Then \(K_s(j)=e^{-(4s/3)g(j)}H_s(j)\), and \(H_s(j)\ge1\). Let \(J\) have law \(Q_s\), and, conditionally on \(J=j\), give \(V\) the law
$$
\mathbb P(V=v\mid J=j)
=\frac{e^{-(4s/3)e_j(v)}}{H_s(j)}\qquad(v\in I_j).
\tag{20}
$$
Both laws are auxiliary laws; they are used to count original spatial reflection stocks below and never replace the original sampling law (1).

To check their moments and derivative, expand the kernel cube on the fixed finite tuple domain
$$
\mathcal T=\lbrace(j,v_1,v_2,v_3):0\le j\le3,
\ v_\ell\in I_j\ (1\le\ell\le3)\rbrace.
$$
It contains \(1+27+27+1=56\) tuples. The energy of a tuple is
$$
\Xi(j,v_1,v_2,v_3)
=\frac23\sum_{\ell=1}^3[g(j+v_\ell)+g(j-v_\ell)]
=4g(j)+\frac43\sum_{\ell=1}^3 e_j(v_\ell),
\tag{21}
$$
and \(P_g(s)=\sum_{\mathcal T}e^{-s\Xi}\). There is exactly one zero-energy tuple, namely \((0,0,0,0)\). Every other tuple has \(j\ge1\), hence \(\Xi\ge4\). In particular
$$
P_g(s)\ge1,\qquad
P_g(s/2)-1\le55e^{-2s},\qquad
\mathbb P(J\ne0)\le55e^{-4s}.
\tag{22}
$$
The finite list of possible values of \((g(j),e_j(v),b_j(v))\) is
$$
(0,0,0),\quad(1,0,0),\quad(1,0,\pm1),\quad
(2,0,0),\quad(2,\tfrac12,\pm\tfrac32),\quad(4,0,0).
$$
Thus \(g(j)^2+e_j(v)^2+b_j(v)^2\le16\), and it vanishes at \(j=0\). Equations (20)-(22) imply
$$
\mathbb E[g(J)^2+e_J(V)^2+b_J(V)^2]
\le880e^{-4s}\le\frac{220}{e^2s^2}<\frac{1024}{s^2}.
\tag{23}
$$
The middle inequality uses the exact maximum \(\sup_{s>0}s^2e^{-4s}=1/(4e^2)\). The last inequality follows already from \(e>1\).

Negating \(v\) preserves \(I_j\) and the conditional law (20), preserves \(e_j(v)\), and negates \(b_j(v)\). Thus \(\mathbb E[b_j(V)\mid J=j]=0\) at every root. This uses symmetry of the displacement law at a fixed root, which holds for this asymmetric \(g\).

For convenience define
$$
\begin{aligned}
m_s(j)&=\mathbb E[e_j(V)\mid J=j],\\
v_s^e(j)&=\mathbb E[e_j(V)^2\mid J=j],\qquad
v_s^b(j)=\mathbb E[b_j(V)^2\mid J=j],\\
\alpha_s(j)&=g(j)+m_s(j),\qquad
\mu_g(s)=\mathbb E_{Q_s}\alpha_s(J),\qquad
\mu(s)=k\mu_g(s).
\end{aligned}
\tag{24}
$$
Writing \(R_{\mathrm{aux}}=1024\), conditional Cauchy-Schwarz and (23) give
$$
\mathbb E_{Q_s}\alpha_s(J)^2\le\frac{2R_{\mathrm{aux}}}{s^2},
\qquad
\mathbb E_{Q_s}[v_s^e(J)+v_s^b(J)]\le\frac{R_{\mathrm{aux}}}{s^2}.
\tag{25}
$$
Under the normalized tuple weights \(e^{-s\Xi}/P_g(s)\), the root marginal is exactly \(Q_s\), and the three displacements, conditionally on the root, are independent with law (20). Thus their mean tuple energy is \(4\mu_g(s)\) by (21). Differentiating the finite sum proves
$$
\frac{d}{ds}\log P_g(s)=-4\mu_g(s),
\qquad
\frac14\frac{d}{ds}\log(P_g(s)^k)=-\mu(s).
\tag{26}
$$
In particular \(\mu\) is continuous on \((0,\infty)\).

Choose the absolute auxiliary constants
$$
B_{\mathrm{aux}}=128,\qquad D_{\mathrm{aux}}=640=5B_{\mathrm{aux}},
\qquad s_{\max}=12\log2,\qquad N_{\mathrm{aux}}=2^{28}.
\tag{27}
$$
For \(s>0\), set
$$
\begin{aligned}
\mathcal F(s)&=\max_{0\le t\le T,\ t\in\mathbb Z}
\left(\log\frac{f_t}{f_0}+st\right),\\
\mathcal J(s)&=\left\lbrace t\in\lbrace0,\ldots,T\rbrace:
\log\frac{f_t}{f_0}+st=\mathcal F(s)\right\rbrace,\\
\theta(s)&=\mu(s)+\frac{D_{\mathrm{aux}}\sqrt{k}}s.
\end{aligned}
\tag{28}
$$
For every positive spatial site, the maximum defining \(\mathcal F\) gives \(a_{\mathbf x}\le f_0e^{\mathcal F(s)}e^{-s\Gamma(\mathbf x)}\). Summing all original sites and enlarging the finite sum to the complete box yields
$$
M_a\le f_0e^{\mathcal F(s)}Z_g(s)^k
=f_t e^{st}Z_g(s)^k\qquad(t\in\mathcal J(s)).
\tag{29}
$$
There is no change to \(M_a\) in this comparison.

Minimize the continuous function
$$
\Psi(s)=\mathcal F(s)+\tfrac14\log(P_g(s)^k)
-D_{\mathrm{aux}}\sqrt{k}\log s
\tag{30}
$$
on \(0<s\le s_{\max}\). The index zero gives \(\mathcal F(s)\ge0\), and (22) gives \(P_g(s)\ge1\); hence \(\Psi(s)\to+\infty\) as \(s\downarrow0\). Excluding a sufficiently small interval near zero and minimizing on the remaining compact interval proves existence of a minimizing positive rate.

Let \(t_-(s)=\min\mathcal J(s)\) and \(t_+(s)=\max\mathcal J(s)\). A maximum of finitely many affine functions has left derivative equal to its smallest active slope and right derivative equal to its largest active slope. Indeed inactive affine functions have positive gaps at the specified rate and remain inactive for sufficiently small changes; among the active ones the smallest slope wins on the left and the largest on the right. Thus (26) gives
$$
\Psi'_-(s)=t_-(s)-\theta(s),\qquad
\Psi'_+(s)=t_+(s)-\theta(s).
$$
At an interior minimum, \(t_-\le\theta(s)\le t_+\). Logconcavity of \(f_t\) makes \(t\mapsto\log(f_t/f_0)+st\) a concave sequence. Between two maximizing integer indices, its linear interpolation lies at least on their constant chord and cannot exceed the maximum; all intervening indices are therefore active. Consequently in the interior case we can choose
$$
t_\star=\lceil\theta(s)\rceil\in\mathcal J(s),\qquad
\theta(s)\le t_\star\le\theta(s)+1.
\tag{31}
$$
If instead the minimum is at \(s=s_{\max}\), its left derivative is nonpositive, and we choose
$$
t_\star=t_-(s_{\max})\in\mathcal J(s_{\max}),\qquad
 t_\star\le\theta(s_{\max}).
\tag{32}
$$
These alternatives include ties and the original finite cap.

Consider an interior minimizing rate. Give the spatial root \(\mathbf J=(J_1,\ldots,J_k)\) the product law \(\mathcal Q_s=Q_s^{\otimes k}\). Call a root \(\mathbf j\in\lbrace0,1,2,3\rbrace^k\) good when
$$
\left|\sum_i\alpha_s(j_i)-\mu(s)\right|
\le\frac{B_{\mathrm{aux}}\sqrt{k}}s,
\qquad
\sum_i[v_s^e(j_i)+v_s^b(j_i)]
\le\frac{B_{\mathrm{aux}}^2k}{s^2}.
\tag{33}
$$
Let \(\mathcal G_s\) be the set of good roots. Independence and (25) bound the variance of the first sum by \(2R_{\mathrm{aux}}k/s^2\), and the mean of the second sum by \(R_{\mathrm{aux}}k/s^2\). Chebyshev, Markov, and a union bound give
$$
\mathcal Q_s(\mathcal G_s)
\ge1-\frac{3R_{\mathrm{aux}}}{B_{\mathrm{aux}}^2}
=\frac{13}{16}>\frac12.
\tag{34}
$$

At a fixed good root, sample the coordinate displacements independently by (20). Put
$$
m_s(\mathbf j)=\sum_i m_s(j_i),\quad
\varepsilon_{\mathbf j}(\mathbf v)=\sum_i e_{j_i}(v_i),\quad
b_{\mathbf j}(\mathbf v)=\sum_i b_{j_i}(v_i).
$$
Their last two conditional means are \(m_s(\mathbf j)\) and zero. The sum of their conditional variances is at most the second sum in (33). Applying Chebyshev to both and adding their failure bounds shows that
$$
\mathcal V_{\mathbf j}=
\left\lbrace\mathbf v\in\prod_iI_{j_i}:
|\varepsilon_{\mathbf j}(\mathbf v)-m_s(\mathbf j)|
\le\frac{2B_{\mathrm{aux}}\sqrt{k}}s,
\quad |b_{\mathbf j}(\mathbf v)|\le\frac{2B_{\mathrm{aux}}\sqrt{k}}s
\right\rbrace
\tag{35}
$$
has conditional probability at least \(3/4\), hence at least \(1/2\). The total failure bound is at most
$$
\frac{B_{\mathrm{aux}}^2k/s^2}{4B_{\mathrm{aux}}^2k/s^2}=\frac14.
$$
Independence between excess and imbalance within one coordinate is not needed.

The endpoint identities following from (18) are exact:
$$
\Gamma(\mathbf j\pm\mathbf v)
=\Gamma(\mathbf j)+\varepsilon_{\mathbf j}(\mathbf v)
\pm b_{\mathbf j}(\mathbf v).
$$
For a good root and a displacement in (35), these identities and (33) imply
$$
\begin{aligned}
\Gamma(\mathbf j\pm\mathbf v)
&\le\Gamma(\mathbf j)+m_s(\mathbf j)
+\frac{4B_{\mathrm{aux}}\sqrt{k}}s\\
&\le\mu(s)+\frac{5B_{\mathrm{aux}}\sqrt{k}}s
=\theta(s)\le t_\star\le T.
\end{aligned}
\tag{36}
$$
Since \(m_s(j_i)\ge0\), (33) also gives \(\Gamma(\mathbf j)\le\mu(s)+B_{\mathrm{aux}}\sqrt{k}/s\le t_\star\). Therefore the root and both endpoints lie in the actual spatial level \(A^a_{f_{t_\star}}\), and \(f_{t_\star}\le a_{\mathbf j}\) is a legal threshold for the energy maximum at this original root. The injective map \(\mathbf v\mapsto\mathbf j+\mathbf v\) gives
$$
r^a_{f_{t_\star}}(\mathbf j)\ge|\mathcal V_{\mathbf j}|.
$$
The conditional probability of a displacement is exactly
$$
p_s(\mathbf v\mid\mathbf j)
=\frac{e^{-(4s/3)\varepsilon_{\mathbf j}(\mathbf v)}}{\prod_iH_s(j_i)}.
$$
Reciprocal density and the lower excess bound in (35) now give
$$
\begin{aligned}
|\mathcal V_{\mathbf j}|
&=\left(\prod_iH_s(j_i)\right)
\sum_{\mathbf v\in\mathcal V_{\mathbf j}}
 p_s(\mathbf v\mid\mathbf j)e^{(4s/3)\varepsilon_{\mathbf j}(\mathbf v)}\\
&\ge\frac12\left(\prod_iH_s(j_i)\right)
\exp\!\left(\frac{4s}{3}m_s(\mathbf j)
-\frac{8B_{\mathrm{aux}}}{3}\sqrt{k}\right).
\end{aligned}
\tag{37}
$$
The exact product law (19) also gives
$$
\prod_iH_s(j_i)^3
=e^{4s\Gamma(\mathbf j)}P_g(s)^k\mathcal Q_s(\mathbf j).
$$
Use the single allowed threshold \(f_{t_\star}\) at every good root, cube (37), sum over these roots, and use the lower bound in (33) and the probability bound (34). We obtain
$$
\begin{aligned}
E(a)
&\ge f_{t_\star}^4\sum_{\mathbf j\in\mathcal G_s}
 r^a_{f_{t_\star}}(\mathbf j)^3\\
&\ge\frac18f_{t_\star}^4P_g(s)^k
\sum_{\mathbf j\in\mathcal G_s}\mathcal Q_s(\mathbf j)
 e^{4s[\Gamma(\mathbf j)+m_s(\mathbf j)]-8B_{\mathrm{aux}}\sqrt{k}}\\
&\ge\frac1{16}f_{t_\star}^4P_g(s)^k
 e^{4s\mu(s)-12B_{\mathrm{aux}}\sqrt{k}}.
\end{aligned}
\tag{38}
$$
The other roots contribute nonnegatively. Dividing by the fourth power of (29) at the active index and using (13) and (31) proves
$$
\begin{aligned}
\frac{E(a)}{M_a^4}
&\ge\frac1{16}e^{-4s(t_\star-\mu(s))-12B_{\mathrm{aux}}\sqrt{k}}
\left(\frac{P_g(s)}{Z_g(s)^4}\right)^k\\
&\ge\frac1{16}e^{-(4D_{\mathrm{aux}}+12B_{\mathrm{aux}})\sqrt{k}-4s}6^{-k}\\
&\ge2^{-52}e^{-4096\sqrt{k}}6^{-k}.
\end{aligned}
\tag{39}
$$
Here \(4D_{\mathrm{aux}}+12B_{\mathrm{aux}}=4096\), and \(e^{-4s}/16\ge e^{-48\log2}/16=2^{-52}\). The integer rounding loss is at most one unit of the original energy index.

It remains to bound the endpoint alternative (32). This uses the finite scalar domain, rather than any evenness of \(g\). At \(s=s_{\max}\), let \(u=e^{-s}=2^{-12}\). Directly from (12),
$$
Z_g(s)=1+u+u^2+u^4\le1+3u,
\qquad \log Z_g(s)<3/4096<1/16.
\tag{40}
$$
Also (22) gives \(P_g(s/2)-1\le55\cdot2^{-24}<1\). For every positive-energy tuple, the elementary maximum \(\sup_{y\ge0}ye^{-y/2}=2/e\) gives
$$
(s\Xi)e^{-s\Xi}\le(2/e)e^{-s\Xi/2}.
$$
Using the exact tuple mean in (26) and the unique zero tuple, we get
$$
s\mu_g(s)
=\frac1{4P_g(s)}\sum_{\mathcal T:\Xi>0}(s\Xi)e^{-s\Xi}
\le\frac{P_g(s/2)-1}{2eP_g(s)}<\frac14,
\tag{41}
$$
where \(P_g(s)\ge1\) and \(e>2\). Since \(f_{t_\star}\le f_0\), equations (29), (32), (40), and (41) imply
$$
\log\frac{M_a}{f_0}
\le st_\star+k\log Z_g(s)
\le s\mu(s)+D_{\mathrm{aux}}\sqrt{k}+k\log Z_g(s)
\le\frac5{16}k+640\sqrt{k}.
\tag{42}
$$
At the original spatial root \(\mathbf0\), the level \(f_0\) has reflected count at least one, so \(E(a)\ge f_0^4\). Thus the endpoint alternative gives
$$
\frac{E(a)}{M_a^4}\ge e^{-(5/4)k-2560\sqrt{k}}.
\tag{43}
$$

If \(k\ge N_{\mathrm{aux}}=2^{28}\), then \(\sqrt{k}\ge16384\), so \(4096\sqrt{k}\le k/4\). The integral representation of the logarithm gives \(\log(4/3)>1/4\). Therefore
$$
6^{-k}e^{-4096\sqrt{k}}
=8^{-k}e^{k\log(4/3)-4096\sqrt{k}}\ge8^{-k},
$$
and (39) gives \(E(a)\ge2^{-52}8^{-k}M_a^4\). In the endpoint case, \(2560\sqrt{k}\le(5/32)k\), so (43) is at least \(e^{-(45/32)k}\). Since \(\log2>1/2\), we have \(\log8>3/2>45/32\), and this gives \(E(a)\ge8^{-k}M_a^4\).

For \(1\le k<N_{\mathrm{aux}}\), use (10). The integrals over \([1,2]\) and \([2,3]\) show \(\log3<3/2\), so
$$
1+2k\log3<1+3k\le3N_{\mathrm{aux}}-2<2^{30}.
$$
As \(512=2^9\) and \(19683<2^{15}\), equation (10) implies
$$
\frac{E(a)}{M_a^4}
\ge\frac{512}{19683(1+2k\log3)^3}\,8^{-k}
\ge2^{-96}8^{-k}.
\tag{44}
$$
The two large-dimension coefficients are also at least \(2^{-96}\). This proves the first inequality of (5), because \(M_a=Z\).

We finish by deriving the original-height consumer, including its scalar input. Let \(m\ge0\) be an integer and let \(0<r\le1\). Define \(z_{\mathrm{aux}}=\sum_{i=0}^m r^i\) and \(q_j=r^j/z_{\mathrm{aux}}\) on \(\lbrace0,\ldots,m\rbrace\), zero elsewhere. Put
$$
L_j=\sum_{i=0}^j q_i,\qquad R_j=\sum_{i=j}^m q_i,
\qquad \delta_j=\min(L_j,R_j),
\qquad F_q(j)=\sum_{h\in\mathbb Z}\min(q_{j+h},q_{j-h}).
$$
Partition \([0,1]\) into the successive probability intervals \([L_j-q_j,L_j]\), ignoring only their measure-zero overlaps. For \(v\) in the \(j\)-th interval, \(v\le L_j\) and \(1-v\le R_j\), whence \(\min(v,1-v)\le\delta_j\). It follows that
$$
\sum_{j=0}^m q_j\delta_j^6
\ge\int_0^1\min(v,1-v)^6\,dv=\frac1{448}.
\tag{45}
$$
Writing \(b_j=\min(j,m-j)\), monotonicity of the geometric masses gives the exact identity \(F_q(j)=q_j(1+2\sum_{h=1}^{b_j}r^h)\). If \(j\le m/2\), then
$$
F_q(j)\ge q_j\sum_{h=0}^j r^h=r^jL_j,
\qquad
R_j=r^j\frac{\sum_{i=0}^{m-j}r^i}{z_{\mathrm{aux}}}\le r^j.
$$
Consequently \(F_q(j)\ge L_jR_j\ge\delta_j^2\). If \(j\ge m/2\), then \(b_j=m-j\), so \(F_q(j)\ge q_j\sum_{h=0}^{m-j}r^h=R_j\ge R_j^2\ge\delta_j^2\). These statements include \(m=0\), \(r=1\), and equality at the midpoint. Cubing and using (45) proves
$$
\sum_{j=0}^m q_jF_q(j)^3\ge\frac1{448}.
\tag{46}
$$

Fix one original spatial root \(\mathbf q\in D_a\). Choose an attaining threshold for its maximum in (4). It is an attained table value and thus equals \(f_E\) for an attained integer energy \(E\in[0,T]\). Strict decrease of the tail profile gives
$$
\Gamma(\mathbf q)\le E,
\qquad
A^a_{f_E}=\lbrace\mathbf x\in\lbrace0,1,2,3\rbrace^k:
\Gamma(\mathbf x)\le E\rbrace.
$$
Put \(R=r^a_{f_E}(\mathbf q)\), and let \(\mathcal V\) be the set of its oriented spatial displacements, namely all \(\mathbf v\in\mathbb Z^k\) with both \(\mathbf q+\mathbf v\) and \(\mathbf q-\mathbf v\) in that level. Its cardinality is \(R\); it is invariant under negation and includes zero.

For every integer \(E\le t\le T\) and \(|h|\le\min(t-E,T-t)\), the two original atoms
$$
(\mathbf q+\mathbf v,t+h),\qquad(\mathbf q-\mathbf v,t-h)
\tag{47}
$$
belong to \(A_T\) and have midpoint \((\mathbf q,t)\). For this root the map \((\mathbf v,h)\mapsto(\mathbf q+\mathbf v,t+h)\) is injective, and the involution \((\mathbf v,h)\mapsto(-\mathbf v,-h)\) exchanges the endpoints. Its only fixed index is \((\mathbf0,0)\). Thus its nonfixed orbits give disjoint pairs of original atoms, avoiding the root itself. Every closed halfspace containing the root contains at least one endpoint of each pair, because strict exclusion of both endpoints would strictly exclude their midpoint. The smaller endpoint probability is exactly \(e^{-\beta(t+|h|)}/Z\). Charging each nonfixed orbit once and half the fixed root mass gives
$$
\tau_p(\mathbf q,t)
\ge\frac{R}{2Z}
\sum_{|h|\le\min(t-E,T-t)}e^{-\beta(t+|h|)}.
\tag{48}
$$
This holds for every containing halfspace, including its boundary atoms.

Let \(q^{(E)}_t=e^{-\beta t}/f_E\) on \(E\le t\le T\), zero elsewhere. This is exactly the translated scalar geometric law in (46) with
$$
j=t-E,\qquad m=T-E,\qquad r=e^{-\beta},\qquad
z_{\mathrm{aux}}=e^{\beta E}f_E.
$$
In particular
$$
F_{q^{(E)}}(t)=\frac1{f_E}
\sum_{|h|\le\min(t-E,T-t)}e^{-\beta(t+|h|)},
\qquad
\sum_{t=E}^T q^{(E)}_tF_{q^{(E)}}(t)^3\ge\frac1{448}.
\tag{49}
$$
The original sampled root mass is still
$$
p_{(\mathbf q,t)}=\frac{e^{-\beta t}}Z
=\frac{f_E}Zq^{(E)}_t.
$$
Cubing (48), multiplying by this original root probability, and using (49) yields
$$
\sum_{t=E}^T p_{(\mathbf q,t)}\tau_p(\mathbf q,t)^3
\ge\frac{R^3f_E^4}{8Z^4}
\sum_{t=E}^Tq^{(E)}_tF_{q^{(E)}}(t)^3
\ge\frac{R^3f_E^4}{3584Z^4}.
\tag{50}
$$
The four factors of the original normalizer consist of one from the sampled root and three from the halfspace masses.

Apply (50) once for the chosen maximizing threshold at each spatial root. Distinct spatial roots correspond to disjoint sampled atoms. For each root all unused heights have nonnegative contributions, so summing these bounds gives exactly
$$
M_3(p)\ge\frac1{3584Z^4}
\sum_{\mathbf q\in D_a}
\max_{0<\omega\le a_{\mathbf q}}\omega^4r^a_\omega(\mathbf q)^3
=\frac{E(a)}{3584Z^4}.
\tag{51}
$$
No levels or thresholds are independently added at the same sampled root, and no source-table normalizer is substituted. Combining (44), its large-dimension counterparts, and (51) proves the first inequality of (3). Finally \(3584=8\cdot448\) and \(448<2^9\), hence
$$
\frac{2^{-96}}{3584}\,8^{-k}
=\frac{2^{-96}}{448}\,8^{-(k+1)}
\ge2^{-105}\,8^{-(k+1)}.
$$
All scalar domains were finite; zero displacement was available at both hard spatial endpoints. Every cutoff obeyed \(t_\star\le T\), every selected energy \(E\) was an original attained integer energy, and the scalar height law included singleton intervals and \(r=1\). All level and feasibility inequalities were weak, and the closed-halfspace argument retained equality atoms. Thus the estimates include all stated boundary cases.

## External sources

None. The only imported mathematical assertion is the finite-table energy/spread estimate of the declared accepted fact `0cd230a98ae241c3`, with the literal alias map in (4) and (8). The scalar polynomial certificate, displacement moments, rate and cutoff argument, spread estimate, and original-height consumer are proved internally.
