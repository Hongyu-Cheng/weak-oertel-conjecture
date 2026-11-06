---
fact_id: 5aaf913ea4b6cc8d
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct21-coupled-ratio-calibration
depends_on: ["bd644bc98ce0e229"]
verifier_run: 06bc1a985f9e4ffd
target_match: null
---

## Statement

Use the original costs and complete integer height-tail normalizers of accepted fact `bd644bc98ce0e229`. Its uncoupled objects \(g_i,\Gamma,f_E,Z_4,Z_3\) are exactly the present \(g_i,\Gamma_0,f_E,Z_4(0),Z_3(0)\), respectively; the coupling below is an additional term. Set
$$
\begin{aligned}
k&=2048,\quad b=180,\quad T=1426,\quad\beta=0,\\
B_i&=180,\quad C_{4,i}=359\qquad(1\le i\le k).
\end{aligned}
$$
and retain \(g_i(0)=0\), \(g_i(1)=1\), \(g_i(2)=180\), and \(g_i(3)=359\). For every nonnegative integer \(\lambda\), define
$$
\begin{aligned}
\Gamma_\lambda(\mathbf x)
&=\sum_{i=1}^{2048}g_i(x_i)
 +\lambda\left(\sum_{i=1}^{2048}\max(x_i-1,0)\right)^2,\\
f_E&=\max(1426-E+1,0),\\
Z_4(\lambda)&=\sum_{\mathbf x\in\lbrace0,1,2,3\rbrace^{2048}}
 f_{\Gamma_\lambda(\mathbf x)},\qquad
Z_3(\lambda)=\sum_{\mathbf x\in\lbrace0,1,2\rbrace^{2048}}
 f_{\Gamma_\lambda(\mathbf x)}.
\end{aligned}
$$
Here \(E\) is a nonnegative integer, and each spatial vector has multiplicity one. These are the original normalizers: each summand counts all integer heights \(t\) with \(\Gamma_\lambda(\mathbf x)\le t\le1426\), each with weight one. Both low costs 0 and 1 remain distinct. Then
$$
Z_4(1)Z_3(0)-Z_4(0)Z_3(1)>0.
$$
In particular \(R(1)>R(0)\), where \(R(\lambda)=Z_4(\lambda)/Z_3(\lambda)\). The models at \(\lambda=0\) and \(\lambda=1\) both arise from bounded full-dimensional convex epigraphs.

## Proof

First check legality. All parameters are integers, \(k\ge1\) and \(b\ge2\), and \(b\le B_i\le2b\) holds because \(B_i=b=180\). Also \(C_{4,i}=2B_i-1=359\), exactly the legal lower endpoint. The scalar function \(u+178\max(u-1,0)\) on \([0,3]\) is convex, with successive slopes 1,179,179 and values 0,1,180,359 at the four integer sites. Therefore the continuous extension
$$
\widetilde\Gamma_\lambda(\mathbf y)
=\sum_{i=1}^{2048}\left[y_i+178\max(y_i-1,0)\right]
 +\lambda\left(\sum_{i=1}^{2048}\max(y_i-1,0)\right)^2
$$
is convex for every \(\lambda\ge0\). Indeed the sum inside the square is nonnegative and convex, and squaring is convex and nondecreasing on the nonnegative reals. Consequently the set of \((\mathbf y,t)\) with \(\mathbf y\in[0,3]^{2048}\) and \(\widetilde\Gamma_\lambda(\mathbf y)\le t\le1426\) is compact and convex. It has nonempty interior: at every \(y_i=1/4\) and \(t=1000\) its energy is 512, the coupling term is zero, and all defining inequalities are strict. Its integer points are precisely the original capped-height atoms used above. This verifies the convex epigraph condition without replacing the original law.

We now give finite exact formulas for all four normalizers and an integer certificate for their strict comparison. A spatial vector has \(a\) coordinates at site 2, \(j\) coordinates at site 3, and \(v\) coordinates at site 1; the other coordinates are at site 0. Its energy is
$$
180a+359j+v+\lambda(a+2j)^2,
$$
and its multiplicity is \(\binom{2048}{j}\binom{2048-j}{a}\binom{2048-a-j}{v}\). This last factor counts the literal unit-cost sites, rather than identifying sites 0 and 1.

If \(a+2j\ge8\), its uncoupled energy is at least \(180(a+2j)-j\ge(359/2)(a+2j)\ge1436>1426\). The coupling is nonnegative. Thus no such vector contributes at either \(\lambda=0\) or \(\lambda=1\). Conversely, for every pair with \(0\le j\le3\) and \(0\le a\le7-2j\), there are contributing vectors at both couplings. Its permitted number of ones has upper endpoint \(1426-180a-359j-\lambda(a+2j)^2\). For \(\lambda\in\lbrace0,1\rbrace\), this endpoint lies between 117 and 1426, whereas the number \(2048-a-j\) of available binary coordinates is at least 2041. Hence the following sums have precisely their displayed endpoints.

For integers \(m\ge1\) and \(0\le r\le m\), define the finite integer
$$
\mathcal B_m(r)=\sum_{v=0}^{r}\binom mv(r-v+1).
$$
The factor \(r-v+1\) is exactly the original complete height tail, including both height endpoints. The four original normalizers are the following explicit finite integers:
$$
\begin{aligned}
Z_4(1)
 &=\sum_{j=0}^{3}\sum_{a=0}^{7-2j}
 \binom{2048}{j}\binom{2048-j}{a}
 \mathcal B_{2048-a-j}\left(1426-180a-359j-(a+2j)^2\right),\\
Z_3(1)
 &=\sum_{a=0}^{7}\binom{2048}{a}
 \mathcal B_{2048-a}\left(1426-180a-a^2\right),\\
Z_4(0)
 &=\sum_{j=0}^{3}\sum_{a=0}^{7-2j}
 \binom{2048}{j}\binom{2048-j}{a}
 \mathcal B_{2048-a-j}\left(1426-180a-359j\right),\\
Z_3(0)
 &=\sum_{a=0}^{7}\binom{2048}{a}
 \mathcal B_{2048-a}\left(1426-180a\right).
\end{aligned}
$$
Thus each four-site normalizer is a sum of 20 displayed occupancy strata, and each three-site normalizer is a sum of eight. The finite formulas, together with the parameters, specify the normalizers exactly without a decimal approximation or asymptotic limit.

For a short strict integer certificate, put \(D=10^{610}\). Exact evaluation of those finite sums gives the following quotients. Each table entry \(q\) means the pair of integer inequalities \(Dq\le Z<D(q+1)\).

| Original normalizer \(Z\) | Exact quotient \(\lfloor Z/D\rfloor\) |
|---|---:|
| \(Z_4(1)\) | 69203971590829 |
| \(Z_3(1)\) | 69068852958831 |
| \(Z_4(0)\) | 75778765782366 |
| \(Z_3(0)\) | 75630810983354 |

It follows by integer multiplication that
$$
\begin{aligned}
&Z_4(1)Z_3(0)-Z_4(0)Z_3(1)\\
&\quad>D^2\left[
69203971590829\cdot75630810983354
-75778765782367\cdot69068852958832\right]\\
&\quad=D^2\cdot63459312035895545122>0.
\end{aligned}
$$
The strict lower bound uses the strict upper inequalities for the second product. All normalizers are positive, since the all-zero vector alone contributes 1427 heights. Dividing therefore proves \(R(1)>R(0)\).

For reproducibility, the following standalone Python certificate evaluates the four finite formulas with arbitrary-precision integers, verifies the quotient bounds, and checks the original strict cross product. It also independently checks each weighted binomial tail using \(v\binom mv=m\binom{m-1}{v-1}\). No floating-point number is used.

```python
from math import comb

k, b, C4, T, D = 2048, 180, 359, 1426, 10**610

def height_tail(n, r):
    assert 0 <= r <= n
    direct = sum(comb(n, v) * (r-v+1) for v in range(r+1))
    alternative = ((r+1) * sum(comb(n, v) for v in range(r+1))
                   - n * sum(comb(n-1, v) for v in range(r)))
    assert direct == alternative
    return direct

def normalizer(lam, sites):
    return sum(
        comb(k, j) * comb(k-j, a)
        * height_tail(k-a-j, T-b*a-C4*j-lam*(a+2*j)**2)
        for j in range(4 if sites == 4 else 1)
        for a in range(8-2*j)
    )

z41, z31, z40, z30 = (
    normalizer(1, 4), normalizer(1, 3),
    normalizer(0, 4), normalizer(0, 3),
)
quotients = (69203971590829, 69068852958831,
             75778765782366, 75630810983354)
assert tuple(z // D for z in (z41, z31, z40, z30)) == quotients
q41, q31, q40, q30 = quotients
assert q41*q30-(q40+1)*(q31+1) == 63459312035895545122
assert z41*z30-z40*z31 > D*D*63459312035895545122 > 0
```

This is a finite counterexample to the requested comparison from \(\lambda=0\) itself. No monotonicity failure between two positive coupling parameters is used. Only the original normalization from `bd644bc98ce0e229` is consumed; its depth-moment theorem is not applied to the coupled model, and the strict normalizer inequality supplies no disproof of that moment statement or of the locked conjecture.

## External sources

None.
