---
fact_id: 1a9ab99ebb8f86bd
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: ternary-convex-pair-amplification
depends_on: []
verifier_run: 202f27e2974c48e8
target_match: null
---

## Statement

For a nonempty finite set \(A\subseteq\mathbb Z^n\) and an integer center \(j\in\mathbb Z^n\), define \(r_A(j):=|\{v\in\mathbb Z^n:j+v\in A,\ j-v\in A\}|\). This counts oriented displacements, including zero exactly once when \(j\in A\).

Let \(P_4\subseteq\mathbb R^4\) be the polytope defined by \(0\le x_i\le2\) for \(1\le i\le4\) and the six inequalities

\[
\begin{aligned}
2x_1+x_3+x_4&\ge2,\\
-2x_1+x_2-x_3+x_4&\le2,\\
x_1-2x_2+2x_3+2x_4&\le8,\\
2x_1+4x_2+x_3&\le10,\\
2x_1+5x_2+x_3-9x_4&\le2,\\
4x_1+x_2-2x_3-x_4&\le4.
\end{aligned}
\]

Put \(A_4:=P_4\cap\mathbb Z^4\). Then \(P_4\) is a full-dimensional compact convex body, \(A_4\subseteq\{0,1,2\}^4\), \(|A_4|=29\), and \(\max_{j\in\mathbb Z^4}r_{A_4}(j)=3\). Every integer midpoint of two points of \(A_4\) belongs to \(A_4\).

For each integer \(k\ge1\), let \(P_{4k}:=P_4^k\subseteq\mathbb R^{4k}\) and \(A_{4k}:=P_{4k}\cap\mathbb Z^{4k}\). Then \(P_{4k}\) is a full-dimensional compact convex body, \(A_{4k}=A_4^k\subseteq\{0,1,2\}^{4k}\), \(|A_{4k}|=29^k\), and \(\max_j r_{A_{4k}}(j)=3^k\). In particular,

\[
\frac{\max_j r_{A_{4k}}(j)}{(|A_{4k}|/2^{4k})^2}
=\left(\frac{768}{841}\right)^k\longrightarrow0.
\]

Consequently there is no absolute \(a>0\) such that \(\max_jr_A(j)\ge a(|A|/2^n)^2\) holds for every nonempty \(A=P\cap\mathbb Z^n\subseteq\{0,1,2\}^n\) with \(P\) convex. More generally, for each real \(p>\log3/\log(29/16)\), there is no such absolute positive coefficient for exponent \(p\). The threshold is approximately \(1.8473165603\); no impossibility is asserted here for all exponents greater than one.

## Proof

The set \(P_4\) is the intersection of finitely many closed halfspaces and the bounded box \([0,2]^4\), so it is compact and convex. At \((1,1,1,1)\), every box inequality is strict. The left sides of the six additional inequalities, in their displayed order, are respectively \(4,-1,3,7,-1,2\), so these inequalities are also strict. An open neighborhood of this point therefore lies in \(P_4\), proving full dimensionality and nonemptiness.

The box constraints ensure that all integer points of \(P_4\) lie in \(\{0,1,2\}^4\). The following table is a complete enumeration of the integer points satisfying the six additional inequalities. A row with first two coordinates \((x_1,x_2)\) lists all and only the allowed last two coordinates \((x_3,x_4)\).

| \((x_1,x_2)\) | Allowed \((x_3,x_4)\) |
| --- | --- |
| \((0,0)\) | \((0,2),(1,1),(1,2),(2,0),(2,1),(2,2)\) |
| \((0,1)\) | \((1,1),(1,2),(2,1),(2,2)\) |
| \((0,2)\) | \((1,1),(2,2)\) |
| \((1,0)\) | \((0,0),(0,1),(0,2),(1,1),(1,2),(2,1)\) |
| \((1,1)\) | \((0,1),(0,2),(1,1),(1,2),(2,1),(2,2)\) |
| \((1,2)\) | \((0,2)\) |
| \((2,0)\) | \((1,2),(2,1)\) |
| \((2,1)\) | \((2,1),(2,2)\) |
| \((2,2)\) | None |

For an explicit way to check every entry and exclusion, at any fixed \((a,b)=(x_1,x_2)\in\{0,1,2\}^2\), a pair \((c,d)=(x_3,x_4)\in\{0,1,2\}^2\) is allowed exactly when all six following integer comparisons hold:

\[
\begin{aligned}
c+d&\ge2-2a,& d-c&\le2+2a-b,\\
2c+2d&\le8-a+2b,&c&\le10-2a-4b,\\
c-9d&\le2-2a-5b,&-2c-d&\le4-4a-b.
\end{aligned}
\]

These are just the defining inequalities after substitution, with no approximation or convex-hull membership oracle involved. Checking the nine possibilities \((c,d)\) for each of the nine rows gives the displayed table. Its row counts sum to \(6+4+2+6+6+1+2+2+0=29\).

It remains to count all possible nonzero reflected displacements. Two distinct integer points have an integer midpoint exactly when they agree coordinatewise modulo two. The parity-class sizes of the 29 enumerated points are as follows; a four-digit parity word lists the four coordinate residues in order.

| Parity | Size | Parity | Size |
| --- | --- | --- | --- |
| 0000 | 4 | 1000 | 3 |
| 0001 | 2 | 1001 | 2 |
| 0010 | 2 | 1010 | 1 |
| 0011 | 2 | 1011 | 1 |
| 0100 | 2 | 1100 | 2 |
| 0101 | 2 | 1101 | 2 |
| 0110 | 1 | 1110 | 1 |
| 0111 | 1 | 1111 | 1 |

There is one parity class of size four, one of size three, eight of size two, and six of size one. Hence the total number of unordered distinct pairs with an integer midpoint is exactly \(\binom42+\binom32+8\binom22=6+3+8=17\). Here is their complete list. In this table, a four-digit word such as 0011 denotes the lattice point \((0,0,1,1)\), not an integer written in base ten.

| First endpoint | Second endpoint | Midpoint |
| --- | --- | --- |
| 0002 | 0020 | 0011 |
| 0002 | 0022 | 0012 |
| 0020 | 0022 | 0021 |
| 0011 | 0211 | 0111 |
| 0002 | 0222 | 0112 |
| 0020 | 0222 | 0121 |
| 0022 | 0222 | 0122 |
| 1000 | 1002 | 1001 |
| 1001 | 1021 | 1011 |
| 0012 | 2012 | 1012 |
| 0021 | 2021 | 1021 |
| 1000 | 1202 | 1101 |
| 1002 | 1202 | 1102 |
| 1101 | 1121 | 1111 |
| 1102 | 1122 | 1112 |
| 0121 | 2121 | 1121 |
| 0122 | 2122 | 1122 |

Each listed endpoint belongs to the membership table, the endpoints in each row agree modulo two, and direct coordinatewise averaging gives its displayed midpoint. The 17 rows are distinct and exhaust the count established by the parity table. Their 17 midpoints are pairwise distinct, and each of these midpoints also appears in the membership table.

An unordered distinct pair with midpoint \(j\) contributes exactly the two displacements \(v\) and \(-v\) to \(r_{A_4}(j)\). The diagonal pair contributes only the zero displacement, and it does so exactly when \(j\in A_4\). Thus each of the 17 listed centers has reflected count three, each of the other 12 points of \(A_4\) has reflected count one, and every integer point outside \(A_4\) has reflected count zero. This proves the exact maximum three over all integer centers. In particular the maximum is also three when restricted to centers in \(A_4\).

The integer-midpoint closure also follows directly from convexity: if \(x,y\in A_4\) and \((x+y)/2\) is integral, it belongs to \(P_4\cap\mathbb Z^4=A_4\). Thus the counterexample satisfies the stated geometric closure, not merely a pair-count condition on an arbitrary ternary subset.

For completeness, the two enumeration tables and the claimed maximum can be checked independently by the following finite certificate. It uses only integer arithmetic and the 81 points of the box; it invokes no optimization solver, floating-point feasibility decision, or unproved search-completeness assertion.

```python
from itertools import product, combinations

def inside(x):
    a, b, c, d = x
    return (2*a+c+d >= 2
            and -2*a+b-c+d <= 2
            and a-2*b+2*c+2*d <= 8
            and 2*a+4*b+c <= 10
            and 2*a+5*b+c-9*d <= 2
            and 4*a+b-2*c-d <= 4)

box = list(product(range(3), repeat=4))
A = {x for x in box if inside(x)}
rows = {
    (0,0): {(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)},
    (0,1): {(1,1),(1,2),(2,1),(2,2)},
    (0,2): {(1,1),(2,2)},
    (1,0): {(0,0),(0,1),(0,2),(1,1),(1,2),(2,1)},
    (1,1): {(0,1),(0,2),(1,1),(1,2),(2,1),(2,2)},
    (1,2): {(0,2)},
    (2,0): {(1,2),(2,1)},
    (2,1): {(2,1),(2,2)},
    (2,2): set(),
}
assert A == {ab+cd for ab, cds in rows.items() for cd in cds}
assert len(A) == 29
midpoints = [tuple((u+v)//2 for u,v in zip(x,y))
             for x,y in combinations(sorted(A), 2)
             if all((u+v) % 2 == 0 for u,v in zip(x,y))]
assert len(midpoints) == len(set(midpoints)) == 17
assert set(midpoints) <= A
counts = {j: sum(tuple(2*u-v for u,v in zip(j,x)) in A
                 for x in A) for j in box}
assert max(counts.values()) == 3
assert sorted(counts.values()) == [0]*52 + [1]*12 + [3]*17
assert 3 * 2**8 == 768 < 841 == len(A)**2
```

For the product assertion, partition a vector in \(\mathbb R^{4k}\) into its \(k\) consecutive blocks of four coordinates. A lattice point belongs to \(P_4^k\) exactly when each block belongs to \(P_4\cap\mathbb Z^4\). Hence \(A_{4k}=A_4^k\) and \(|A_{4k}|=29^k\). Compactness and convexity pass to finite Cartesian products. The product of the open neighborhoods of \((1,1,1,1)\) used above is an open subset of \(P_4^k\), so \(P_{4k}\) is full-dimensional.

At an integer center \(j=(j^{(1)},\ldots,j^{(k)})\), a displacement \(v=(v^{(1)},\ldots,v^{(k)})\) is counted exactly when each \(v^{(s)}\) is counted at \(j^{(s)}\) in the corresponding factor. This is a bijection of the displacement set with the Cartesian product of the factor displacement sets, including their zero displacements. Consequently \(r_{A_{4k}}(j)=\prod_{s=1}^k r_{A_4}(j^{(s)})\). Each factor is at most three, and taking every block center equal to \((0,0,1,1)\) attains three in every factor. Therefore the product maximum is exactly \(3^k\).

Since \(|A_{4k}|/2^{4k}=(29/16)^k\), the ratio for exponent two is \([3/(29/16)^2]^k=(768/841)^k\). This tends to zero because \(0<768<841\). Already \(k=1\) refutes the proposed coefficient-one quadratic inequality, because \(3<841/256\).

Finally fix a real \(p>\log3/\log(29/16)\). The denominator \(\log(29/16)\) is positive, so \(3/(29/16)^p<1\). The ratio for this exponent along the product family is \([3/(29/16)^p]^k\), which tends to zero. For any proposed absolute coefficient \(a>0\), some integer \(k\) therefore makes the ratio smaller than \(a\), violating the claimed inequality in dimension \(4k\). The threshold belongs to \((1,2)\), since \(29/16<3<(29/16)^2\). At or below this threshold the present ratio does not tend to zero, which is why the construction leaves the existence of a smaller uniform superlinear exponent unresolved.

## External sources

None. The polytope, every integer point, every noncentral integer-midpoint pair, and the Cartesian-product calculation are certified above by explicit inequalities and integer arithmetic. No accepted predecessor is used as a premise.
