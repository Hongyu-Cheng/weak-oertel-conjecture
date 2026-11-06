---
fact_id: e44c68dddb0a3a1e
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: regular-simplex-active-family
depends_on: ["314b32bda8a0b01e","981a6c3aa5982216"]
verifier_run: ffaf452eb79d46d6
target_match: null
---

## Statement

For every integer \(m\ge2\), there are \(n=d=m\), a convex body \(C_m\subseteq\mathbb R^{m+m}\), an anchor \((z_0,y_0)\in C_m\cap(\mathbb Z^m\times\mathbb R^m)\), and \(r=m+1\) ordinary halfspaces \(H_1,\ldots,H_r\) satisfying all the active-family conclusions of accepted fact `981a6c3aa5982216` with \(\varepsilon=0\), with the following additional properties:

1. the weights are \(\lambda_i=1/r\);
2. the continuous normal components are unit regular-simplex vertices;
3. every \(H_i\) is an exact depth-minimizing cap at the common anchor;
4. \(z_0\) is a weighted lattice centerpoint and \(y_0\) maximizes depth on \(C_{z_0}\);
5. \(\bar a=0\), so \(Q=\mathbb R^m\) and \(W_Q=W\);
6. if \(t=h_S((z_0,y_0))\), then
   \[
   \frac{t}{W_Q}=\frac{3}{2(m+2)}\longrightarrow0.
   \]

Consequently no absolute \(c>0\) can satisfy \(t\ge cW_Q\) in the regular-simplex active-family case. This does not disprove the locked Oertel target: the primitive slice over \(z_0\) has mass at least \(2^{-m}W\), so accepted fact `314b32bda8a0b01e` applies under its lower-rank induction hypothesis.

## Proof

Put \(r=m+1\), let \(B\subseteq\mathbb R^m\) be the Euclidean unit ball, and write \(v_m:=\operatorname{vol}_m(B)\). In the base space define
\[
z_i=e_i\quad(1\le i\le m),
\qquad
z_r=-\sum_{i=1}^m e_i,
\qquad
P:=\operatorname{conv}\{z_1,\ldots,z_r\}.
\]
In the continuous space choose unit vectors \(b_1,\ldots,b_r\) satisfying
\[
\sum_{i=1}^r b_i=0,
\qquad
b_i^\top b_j=-\frac1m\quad(i\ne j).
\tag{1}
\]
Thus the \(b_i\) are the vertices of a unit regular simplex. The assignment \(z_i\mapsto b_i\) is induced by an invertible linear map \(L:\mathbb R^m\to\mathbb R^m\): define \(Le_i=b_i\) for \(1\le i\le m\), and then (1) gives \(Lz_r=b_r\). Set \(R:=m+1\) and
\[
C_m:=\{(z,RLz+q):z\in P,\ q\in B\}.
\tag{2}
\]
This is the image of \(P\times B\) under the invertible shear \((z,q)\mapsto(z,RLz+q)\), hence is a compact full-dimensional convex body.

We first determine all lattice fibers. If \(x\in P\cap\mathbb Z^m\), write
\[
x=\sum_{i=1}^m\lambda_i e_i-\lambda_r\mathbf1,
\qquad
\lambda_i\ge0,
\qquad
\sum_{i=1}^r\lambda_i=1.
\]
Let \(s:=\lambda_r\). Coordinatewise, \(\lambda_i=x_i+s\), and summing gives
\[
s=\frac{1-\sum_i x_i}{m+1}.
\tag{3}
\]
If \(0<s<1\), then \(x_i\ge0\) for every \(i\), while (3) gives \(\sum_i x_i<1\); hence \(x=0\). If \(s=0\), then the nonnegative integers \(x_i=\lambda_i\) sum to \(1\), so \(x=e_i\) for some \(i\). If \(s=1\), then \(x_i\ge-1\) and \(\sum_i x_i=-m\), so \(x=-\mathbf1=z_r\). Therefore
\[
P\cap\mathbb Z^m=\{0,z_1,\ldots,z_r\}.
\tag{4}
\]
Equation (2) now gives
\[
(C_m)_0=B,
\qquad
(C_m)_{z_i}=Rb_i+B\quad(1\le i\le r).
\tag{5}
\]
All \(r+1=m+2\) positive-mass fibers have mass \(v_m\), and hence
\[
W=(m+2)v_m.
\tag{6}
\]

Take \(z_0=0\) and \(y_0=0\). Every proper closed base halfspace containing \(0\) contains the entire anchor fiber, so its fiber mass is at least \(v_m\). Since \(m+2\le2^m\) for \(m\ge2\), (6) implies
\[
v_m\ge2^{-m}W.
\tag{7}
\]
Thus \(z_0\) has exactly the weighted lattice centerpoint property required in accepted fact `981a6c3aa5982216`.

We next compute the depth at \((0,0)\). It is enough to consider closed halfspaces whose boundary contains \((0,0)\), because translating the boundary of any halfspace containing the anchor to the anchor only decreases the halfspace. Write such a halfspace as
\[
H(a,b):=\{(z,x):a^\top z+b^\top x\ge0\},
\qquad
(a,b)\ne(0,0).
\tag{8}
\]
If \(b=0\), the anchor fiber is wholly contained. Moreover \(\sum_{i=1}^r z_i=0\), so \(a^\top z_i\ge0\) for at least one \(i\); the corresponding remote fiber is also wholly contained. Hence
\[
\mathcal H_m(S\cap H(a,0))\ge2v_m.
\tag{9}
\]

Suppose \(b\ne0\), put \(e=b/\|b\|\), and define
\[
\Phi(s):=\frac1{v_m}\operatorname{vol}_m\{q\in B:e^\top q\ge-s\}.
\tag{10}
\]
Rotational symmetry makes \(\Phi\) independent of \(e\). It is increasing and satisfies
\[
\Phi(-s)=1-\Phi(s),
\qquad
\Phi(0)=\frac12.
\tag{11}
\]
For the remote fiber over \(z_i\), its fraction inside (8) is \(\Phi(s_i)\), where
\[
s_i:=\frac{a^\top z_i+R\,b^\top b_i}{\|b\|}.
\tag{12}
\]
Both simplex vertex sets sum to zero, so
\[
\sum_{i=1}^r s_i=0.
\tag{13}
\]
We claim that for any real numbers satisfying (13),
\[
\sum_{i=1}^r\Phi(s_i)\ge1.
\tag{14}
\]
If at least two \(s_i\) are nonnegative, (14) follows from \(\Phi(s_i)\ge1/2\). Otherwise exactly one, say \(s_1\), is positive and all the others are negative. For every \(j>1\), (13) gives \(-s_j\le s_1\). By monotonicity and (11),
\[
\Phi(s_1)\ge\Phi(-s_j)=1-\Phi(s_j),
\]
so the two terms indexed by \(1,j\) already sum to at least \(1\). The all-zero case is immediate as well. This proves (14).

The anchor ball is bisected by every halfspace (8) with \(b\ne0\), while (14) says that the remote fibers contribute at least \(v_m\). Consequently
\[
\mathcal H_m(S\cap H(a,b))\ge\frac32v_m.
\tag{15}
\]

For each \(i\), define the pure-continuous cap
\[
H_i:=\{(z,x):b_i^\top x\ge0\}.
\tag{16}
\]
On its matching remote fiber, (1) and (5) give
\[
\min_{x\in Rb_i+B}b_i^\top x=R-1=m>0.
\tag{17}
\]
On every other remote fiber,
\[
\max_{x\in Rb_j+B}b_i^\top x
=-\frac{R}{m}+1
=-\frac1m<0.
\tag{18}
\]
The anchor ball is bisected. Thus (16) contains exactly one whole remote fiber and half of the anchor fiber:
\[
\mathcal H_m(S\cap H_i)=\frac32v_m.
\tag{19}
\]
Equations (9), (15), and (19) prove
\[
h_S((0,0))=t=\frac32v_m.
\tag{20}
\]

The anchor is also a fiberwise depth maximizer. For any \(y\in B\), (1) implies that \(b_i^\top y\ge0\) for some \(i\). Consider the boundary-through-\((0,y)\) halfspace
\[
H_i(y):=\{(z,x):b_i^\top(x-y)\ge0\}.
\tag{21}
\]
Its anchor-fiber cap has volume at most \(v_m/2\). The matching remote fiber is wholly included because
\[
\min_{x\in Rb_i+B}b_i^\top x=m\ge b_i^\top y,
\tag{22}
\]
whereas every other remote fiber is excluded by (18) and \(b_i^\top y\ge0\). Hence
\[
h_S((0,y))\le\mathcal H_m(S\cap H_i(y))\le\frac32v_m=t.
\tag{23}
\]
Together with (20), this proves that \(y_0=0\) maximizes depth on \((C_m)_0\).

Finally, in the notation of accepted fact `981a6c3aa5982216`, the caps (16) have unit normals
\[
u_i=(a_i,b_i)=(0,b_i),
\qquad
\lambda_i=\frac1r.
\]
They are exact minimizers by (19)-(20), their continuous components balance by (1), and \(\bar a=0\). Therefore \(Q=\mathbb R^m\) and \(W_Q=W\). The union cover is also literal: for every \(x\), the equality \(\sum_i b_i^\top x=0\) implies \(b_i^\top x\ge0\) for some \(i\). From (6) and (20),
\[
\frac{t}{W_Q}=\frac{3}{2(m+2)}\to0.
\tag{24}
\]
This proves the claimed failure of every dimension-free cap-to-base-mass bound.

For calibration against accepted fact `314b32bda8a0b01e`, the primitive codimension-\(m\) base slice \(A=\{0\}\) has mass \(v_m\). Equation (7) is exactly its heavy-slice hypothesis. Thus, under the lower-rank induction hypothesis of that accepted fact, the locked Oertel conclusion follows for this family even though the regular-simplex active-family bound fails.

## External sources

none
