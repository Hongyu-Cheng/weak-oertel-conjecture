---
fact_id: 22ba6debf3e38e3f
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3ew-cyclic-lazy-zero
depends_on: ["4862d5efd356636d","cbe047e54dd24a26"]
verifier_run: 92704b2967654be0
target_match: null
---

## Statement

Let \(q\ge1\) and \(m\ge0\) be integers, and let \(X_1,\ldots,X_m\) be independent random variables taking values in \(\mathbb Z/q\mathbb Z\). The empty sum is zero. For every real \(0<\varepsilon\le1/2\), if \(\Pr(X_i=0)\ge\varepsilon\) for every \(i\), then
\[
\Pr\!\left(\sum_{i=1}^m X_i=0\right)\ge\varepsilon^{q-1}.
\tag{1}
\]
For \(q\ge2\), this bound is sharp for every such \(\varepsilon\): take \(m=q-1\) and independent increments with probabilities \(\varepsilon\) at zero and \(1-\varepsilon\) at the residue of 1. In particular the hypothesis \(\Pr(X_i=0)\ge1/2\) gives the sharp bound \(2^{-(q-1)}\), and hence the requested bound holds with \(C=1\).

For the cubic application, use exactly the rate normalization of accepted fact `4862d5efd356636d`: for \(s>0\) and \(j\in\mathbb Z_{\ge0}\), put
\[
F_3(s)=\sum_{j\ge0}(2j+1)^3e^{-4sj},\qquad
Q_s(j)=\frac{(2j+1)^3e^{-4sj}}{F_3(s)}.
\tag{2}
\]
The geometric variable called \(q\) in accepted fact `cbe047e54dd24a26` is called \(x\) here and is \(x=e^{-4s}\); our \(q\) is only the integer modulus. Thus its generating-function normalization, denoted \(G_3(x)\) here to distinguish the arguments, is exactly
\[
G_3(x)=\frac{1+23x+23x^2+x^3}{(1-x)^4},\qquad F_3(s)=G_3(e^{-4s}).
\tag{3}
\]
These are the same auxiliary coordinate laws as in both accepted predecessors.

Let \(u_1,\ldots,u_m\in\mathbb Z\), let \(s_i>0\), and let the coordinates \(J_i\) be independent with laws \(Q_{s_i}\), allowing any coordinates instead to be deterministic zero. Write \(Q\) for their product law and \(A_0=\{j:u\cdot j\equiv0\pmod q\}\). Define \(\varepsilon_q=2^{-16}q^{-4}\) and \(\beta_q=\varepsilon_q^{q-1}\). Then
\[
Q(A_0)\ge\beta_q\ge\exp\bigl(-20q\log(q+1)\bigr).
\tag{4}
\]
There is no coprimality assumption in (4). If there is a coordinate with \(qs_i\le1\) and \(\gcd(u_i,q)=1\), the stronger lower bound \(c_{\mathrm{mod}}/q\) for every residue follows already from `4862d5efd356636d`, with its unchanged constant \(c_{\mathrm{mod}}=1/(8e^4(1+e^4))\).

For every event \(B\) under this same, unconditioned product law, one has \(Q(B\cap A_0)\ge\beta_q-Q(B^c)\). Consequently \(Q(B^c)\le\beta_q/2\) implies \(Q(B\cap A_0)\ge\beta_q/2\). No resource restriction or conditioning is part of the hypotheses of (4), and (4) by itself asserts neither a resource-restricted probability bound nor the locked Weak Oertel conjecture.

## Proof

First prove (1) for fixed \(q,m,\varepsilon\). For each residue \(g\), define the probability measure \(L_g=\varepsilon\delta_0+(1-\varepsilon)\delta_g\), so \(L_0=\delta_0\). Every probability measure \(\mu\) on \(\mathbb Z/q\mathbb Z\) with \(\mu(0)\ge\varepsilon\) is a convex combination of these measures. Indeed the weights
\[
w_0=\frac{\mu(0)-\varepsilon}{1-\varepsilon},\qquad
w_g=\frac{\mu(g)}{1-\varepsilon}\quad(g\ne0)
\tag{5}
\]
are nonnegative and sum to one. At each nonzero residue the combination \(\sum_gw_gL_g\) has mass \((1-\varepsilon)w_g=\mu(g)\), and its mass at zero is \(w_0+\varepsilon\sum_{g\ne0}w_g=\mu(0)\). This also covers the one-element group.

Independence and multilinearity of convolution now express the sum distribution as a convex combination of distributions obtained by choosing one fixed \(L_{g_i}\) at each coordinate. It suffices to prove the lower bound for every such fixed sequence \(g_1,\ldots,g_m\). Let \(f_i\) be the mass function of the sum of its first \(i\) increments, let \(S_i=\{a:f_i(a)>0\}\), and let \(b_i=\min_{a\in S_i}f_i(a)\). Initially \(S_0=\{0\}\) and \(b_0=1\). Convolution gives
\[
f_i(a)=\varepsilon f_{i-1}(a)+(1-\varepsilon)f_{i-1}(a-g_i),\qquad
S_i=S_{i-1}\cup(S_{i-1}+g_i).
\tag{6}
\]
The supports increase by inclusion. If \(S_i\) strictly contains \(S_{i-1}\), every positive value in (6) has at least one summand whose mass-function factor is at least \(b_{i-1}\). Both coefficients are at least \(\varepsilon\), because \(\varepsilon\le1/2\). Thus \(b_i\ge\varepsilon b_{i-1}\).

If the support does not grow, \(S_{i-1}+g_i\subseteq S_{i-1}\); translation preserves cardinality, so equality holds. Hence for every \(a\in S_i=S_{i-1}\), both \(a\) and \(a-g_i\) belong to \(S_{i-1}\). Formula (6) then gives \(f_i(a)\ge(\varepsilon+1-\varepsilon)b_{i-1}=b_{i-1}\), so \(b_i\ge b_{i-1}\).

Every strictly growing step adds at least one residue. There can therefore be at most \(q-1\) such steps, since the initial support has one element. It follows that \(b_m\ge\varepsilon^{q-1}\). Also zero belongs to every \(S_i\), by (6) and the positivity of the zero coefficient. Thus \(f_m(0)\ge\varepsilon^{q-1}\). Averaging over the convex combination proves (1), including \(m=0\) and \(q=1\).

For sharpness when \(q\ge2\), the stated \(q-1\) increments have an ordinary integer sum in \(\{0,1,\ldots,q-1\}\). Its residue is zero exactly when every increment is zero, which has probability \(\varepsilon^{q-1}\). With \(\varepsilon=1/2\), this also rules out any positive absolute lower bound of the form \(c/q\) over all lazy increment sequences. Finally \((q-1)\log2\le q\log(q+1)\), so the sharp lazy bound implies the requested exponential bound with \(C=1\).

We next establish a zero-atom bound for each cubic coordinate residue, using the unchanged definitions (2) and the alias (3). Fix a positive rate \(s\) and an integer coefficient \(u\). If \(qs\le1\), apply accepted fact `4862d5efd356636d` with one coordinate and coefficient 1. Its coprimality hypothesis then holds, and it gives \(\Pr_{Q_s}(J\equiv0\pmod q)\ge c_{\mathrm{mod}}/q\). The event \(J\equiv0\pmod q\) implies \(uJ\equiv0\pmod q\) for every integer \(u\), so
\[
\Pr_{Q_s}(uJ\equiv0\pmod q)\ge\frac{c_{\mathrm{mod}}}{q}
\quad\text{when }qs\le1.
\tag{7}
\]
This use of the diffuse-coordinate estimate does not require that the resulting residue law be lazy.

If \(qs>1\), the actual atom at \(J=0\) suffices. The numerator polynomial in (3), supplied by accepted fact `cbe047e54dd24a26` with the explicit variable map above, is at most 48 for \(0\le x<1\). The function \(t\mapsto1-e^{-4t}\) is concave on \([0,1]\) and vanishes at zero. Since \(1/q\in(0,1]\), this implies
\[
1-e^{-4s}\ge1-e^{-4/q}
\ge\frac{1-e^{-4}}q\ge\frac1{2q}.
\tag{8}
\]
The first inequality uses \(s>1/q\), and the last follows from \(e^4>2\). Therefore \(F_3(s)\le48(2q)^4=768q^4\), and
\[
\Pr_{Q_s}(uJ\equiv0\pmod q)\ge Q_s(0)
=\frac1{F_3(s)}\ge\frac1{768q^4}
\quad\text{when }qs>1.
\tag{9}
\]
In particular (9) is a lower bound on a zero atom, not a claim that this atom is at least one half.

The elementary bound \(e<3\) gives \(8e^4(1+e^4)<8\cdot81\cdot82=53136<65536\), hence \(c_{\mathrm{mod}}>2^{-16}\). Equations (7) and (9) now show that every residue increment \(u_iJ_i\pmod q\) has zero probability at least \(2^{-16}q^{-4}=\varepsilon_q\); in (7) use \(q^{-1}\ge q^{-4}\), and in (9) use \(768<65536\). A deterministic zero coordinate also satisfies this bound. Independence is preserved by taking coordinate residues, and \(0<\varepsilon_q\le1/2\), so (1) applies and proves \(Q(A_0)\ge\beta_q\).

All logarithms being natural, the exponent satisfies
\[
-\log\beta_q
=(q-1)(16\log2+4\log q)
\le20(q-1)\log(q+1)
\le20q\log(q+1).
\tag{10}
\]
This proves (4), also when \(q=1\), for which \(\beta_1=1\) and the congruence is automatic. The stronger statement when a coprime diffuse coordinate exists is exactly the convolution conclusion of accepted fact `4862d5efd356636d`, with the same rates, coefficients, and modulus normalization.

Lastly \(Q(B\cap A_0)=Q(A_0)-Q(A_0\cap B^c)\ge\beta_q-Q(B^c)\), proving the stated resource-event intersection implication. This subtractive estimate requires the failure probability under the same unconditioned product law. It supplies no bound for that failure probability and does not replace a proof on an original resource-restricted support or its actual normalizer.

## External sources

None. The finite-group theorem and its sharpness are proved directly. The cubic application uses only the declared accepted predecessors with the explicit normalization map (2)-(3).
