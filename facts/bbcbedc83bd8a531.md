---
fact_id: bbcbedc83bd8a531
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-fixed-coupling-one-sided-convex-weight-entropy
depends_on: []
verifier_run: 4835746817d21b5e
target_match: null
---

## Source

- [fc542fd7a6ea864e](../candidates/fc542fd7a6ea864e.json), fc542fd7a6ea864e:01–02 §§1–3 (1)–(2).

## Statement

Let $C$ be a compact convex set, let $L=\min_i A_i>0$ there for finitely many affine $A_i$, and let $q\ge0$ on $C$ be the restriction of a finite global convex function. For $d\ge1$ define
$$
F(q,L)=\sup_{t\ge0}\{tq-(e^t-1)L\},\quad F_q(w)=F(q(w),L(w)),\quad w_q=(q-L)_+.
$$
The scalar $F$ is zero for $q\le L$ and equals $q\log(q/L)-q+L$ for $q>L$. It is convex in the pair, nondecreasing in $q$, and nonincreasing in positive $L$. The two physical functions $F_q,w_q$ have finite global convex extensions. For any endpoints $w_-,w_+\in C$, midpoint $b$, $a=(L(w_-)+L(w_+))/(2L(b))$, and $\delta_F=(F_q(w_-)+F_q(w_+))/2-F_q(b)$, one has
$$
w_q(b)(1-a^d)\ \le\ w_q(b)[1-e^{-d\delta_F/w_q(b)}]\ \le\ d\delta_F
$$
with the middle expression zero for $w_q(b)=0$.

Suppose finite nonnegative endpoint couplings $\pi,\pi_{\rm old}$ have the same respective marginals $\gamma_-,\gamma_+$ and midpoint laws $\rho,\rho_{\rm old}$, with $\rho_{\rm old}\preceq_{\rm cx}\rho$. Put $E=b_\#((1-a^d)\pi)$, $\eta=(\gamma_-+\gamma_+)/2$, $\Delta_{\rm old}=\int F_q\,d(\eta-\rho_{\rm old})$, and $T_{\rm end}=\int w_q\,d\eta$. Then
$$
\int w_q\,dE\ \le\ T_{\rm end}[1-e^{-d\Delta_{\rm old}/T_{\rm end}}]\ \le\ d\Delta_{\rm old},
$$
with zero middle expression for $T_{\rm end}=0$. The same $\pi$ works for every admissible $q$. If a prescribed source $\nu\preceq_{\rm cx}\rho_{\rm old}$ is given, the bound also holds with $\Delta_{\rm old}$ replaced by $\int F_q\,d(\eta-\nu)$. Over already supplied measurable components with finite summed budgets, the total is bounded by the same formula with the summed or integrated $T_{\rm end}$ and $\Delta_{\rm old}$. In particular this summation introduces no parity multiplier in the error bound.

## Proof

Optimizing in $t$ gives $t=(\log(q/L))_+$ on $C$, taking $t=0$ at $q=0$. The optimizer is bounded there because $\min_C L>0$ and $q$ is bounded. The scalar convexity and monotonicity follow from the supremum of affine functions with nonnegative coefficient of $q$ and nonpositive coefficient of $L$. Take a finite upper bound $B$ on the maximizing $t$ on $C$. The globally finite convex extension of $F_q$ is $\max_i\sup_{0\le t\le B}\{tq-(e^t-1)A_i\}$, which is convex in the physical coordinates because $t\ge0$. The same argument with the maximum of $0$ and the functions $q-A_i$ gives the extension of $w_q$.

Let $V=(L(w_-)+L(w_+))/2=aL(b)$ and $\bar q=(q(w_-)+q(w_+))/2\ge q(b)$. Then $0<a\le1$ by concavity and positivity of $L$. Scalar Jensen and monotonicity give $\delta_F\ge F(\bar q,V)-F(q(b),L(b))\ge F(q(b),V)-F(q(b),L(b))$. If $q(b)\le L(b)$ the tuple assertion follows from nonnegative $\delta_F$. Otherwise both terms use the positive branch and their difference is
$$
q(b)\log(1/a)-L(b)(1-a)\ \ge\ (q(b)-L(b))\log(1/a),
$$
by $-\log a\ge1-a$. This proves the nonlinear tuple bound by exponentiation, and $1-e^{-x}\le x$ gives its last inequality.

Let $T=\int w_q\,d\rho$ and $\Delta=\int\delta_F\,d\pi=\int F_q\,d(\eta-\rho)$. Both are nonnegative. When $T=0$ the error integral vanishes. Otherwise integrate the tuple inequality and use concavity of $1-e^{-dx}$ with probability weights $w_q(b)\,d\pi/T$ on positive weight. The weighted integral of $\delta_F/w_q(b)$ there is at most $\Delta/T$. Thus $\int w_q\,dE\le B_d(T,\Delta)$ where $B_d(T,\Delta)=T(1-e^{-d\Delta/T})$ for $T>0$, extended by zero for $T=0$. Convex order tested with $F_q$ gives $\Delta\le\Delta_{\rm old}$. Midpoint Jensen for $w_q$ gives $T\le T_{\rm end}$. The function $B_d$ is nondecreasing in $\Delta$, and in $T$ because its derivative there is $1-(1+d\Delta/T)e^{-d\Delta/T}\ge0$. This proves the endpoint inequality. Convex order tested with the same extension of $F_q$ also proves the source option. The estimate uses only the fixed couplings. Finally $B_d$ is the concave, positively homogeneous perspective of $1-e^{-dx}$, with its continuous zero extension at $T=0$. Hence the sum or integral of the component bounds is at most $B_d$ of their summed budgets, with the zero case immediate. No claim of existence or geometric capacity of the supplied couplings is used.
