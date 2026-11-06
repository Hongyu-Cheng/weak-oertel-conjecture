---
fact_id: 25ecc4ac9b2ae01d
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: n2-root-concave-level-concentration
depends_on: ["e6af28280337b587"]
verifier_run: d9cefa62fad1402f
target_match: null
---

## Statement

Let
\[
T:=\operatorname{conv}\{(1,0),(-1,1),(-1,-1)\}\subseteq\mathbb R^2
\]
and let its Minkowski functional be
\[
p(z_1,z_2):=\max\{-z_1,z_1+2z_2,z_1-2z_2\}.
\tag{1}
\]
Let \(e_1,\ldots,e_{10}\) be the standard basis of \(\mathbb R^{10}\), put
\[
K:=\operatorname{conv}\{e_1,\ldots,e_{10},-\mathbf 1\},
\qquad
V:=\operatorname{vol}_{10}(K)=\frac{11}{10!},
\tag{2}
\]
and write \(p_K\) for the Minkowski functional of \(K\).  Define
\[
C:=
\left\{
(z,x)\in\mathbb R^2\times\mathbb R^{10}:
p(z)+p_K(x)\leq40
\right\},
\qquad
z_0:=0.
\tag{3}
\]
For \(z\in\mathbb Z^2\), put
\[
C_z:=\{x:(z,x)\in C\},
\qquad
w_z:=\operatorname{vol}_{10}(C_z),
\qquad
W:=\sum_{z\in\mathbb Z^2}w_z.
\]
Then \(C\) is a compact full-dimensional convex body and
\[
C_z=(40-p(z))K
\quad\text{when }p(z)\leq40.
\tag{4}
\]
The complete positive lattice-fiber profile is
\[
\{z:w_z>0\}=\{z\in\mathbb Z^2:p(z)\leq39\},
\qquad
w_z=V(40-p(z))^{10},
\tag{5}
\]
and
\[
W=V\overline W,
\qquad
\overline W=515400808270776000.
\tag{6}
\]

For each positive-volume fiber, let \(M(z)\) be its maximal absolute Tukey
depth as in the registered subgoal.  Then
\[
M(z)=\gamma w_z,
\qquad
\gamma:=\left(\frac{10}{11}\right)^{10}.
\tag{7}
\]
The body and anchor satisfy every hypothesis of
`n2-root-concave-level-concentration`, including
\[
\mathcal E^\Psi_{10}(w;0)<\frac W{64}
\tag{8}
\]
and
\[
\{z:w_z\geq W/(64\gamma)\}=\varnothing.
\tag{9}
\]
Nevertheless, with \(D_t\) and \(\eta(t)\) defined in that subgoal,
\[
\sup_{0<t\leq M(0)}t\,\eta(t)
\leq
\gamma V\cdot25\cdot34^{10}
<
\frac{3W}{64}.
\tag{10}
\]

## Proof

The triangle \(T\) contains \(0\) in its interior, and (1) is exactly its
Minkowski functional.  The simplex \(K\) contains \(0\) in its interior
because the average of its eleven vertices is \(0\).  The determinant of
the ten edge vectors \(e_i+\mathbf 1\) is
\(\det(I+\mathbf 1\mathbf 1^{\mathsf T})=11\), proving the volume in
(2).  Both gauges are continuous, convex, positively homogeneous, and
coercive.  Hence their sum is coercive and convex.  Its sublevel set (3)
is compact and convex and contains a neighborhood of \(0\), so \(C\) is a
full-dimensional convex body.

Positive homogeneity of \(p_K\) gives (4).  Since \(p(z)\) is an integer
at every lattice point and \(p(z)\geq0\), with equality only at \(z=0\),
(5) follows, including every zero-volume boundary fiber.

We next enumerate the profile.  For \(k\geq1\), set
\[
S_k:=\{z\in\mathbb Z^2:p(z)=k\}.
\]
The triangle \(kT\) has vertices
\[
A_k=(k,0),\qquad B_k=(-k,k),\qquad C_k=(-k,-k).
\]
Its three edges have the following lattice parametrizations:
\[
\begin{aligned}
A_kB_k&:\ (k-2i,i),&&0\leq i\leq k,\\
A_kC_k&:\ (k-2i,-i),&&0\leq i\leq k,\\
B_kC_k&:\ (-k,j),&&-k\leq j\leq k.
\end{aligned}
\tag{11}
\]
After subtracting the three duplicated vertices, (11) gives
\[
\#S_k=(k+1)+(k+1)+(2k+1)-3=4k.
\tag{12}
\]
Also \(S_0=\{0\}\).  Consequently
\[
\overline W
=40^{10}+4\sum_{k=1}^{39}k(40-k)^{10}
=515400808270776000,
\]
which proves (6).

The exact maximal depth (7) follows from the simplex calculation recorded
in accepted fact `e6af28280337b587`; for completeness, its short argument
is as follows.  If \(\lambda_0,\ldots,\lambda_{10}\) are the barycentric
coordinates of a point \(x\in K\), then some
\(\lambda_i(x)\geq1/11\).  The closed halfspace
\[
\{y\in\mathbb R^{10}:\lambda_i(y)\geq\lambda_i(x)\}
\]
contains \(x\), and its intersection with \(K\) is a homothetic simplex
of volume
\[
(1-\lambda_i(x))^{10}V\leq\left(\frac{10}{11}\right)^{10}V.
\]
At the centroid \(0\), Grünbaum's simplex bound gives the reverse
inequality for every containing closed halfspace.  Thus the maximal depth
of \(K\) is exactly \(\gamma V\).  Homothety in (4) multiplies both volume
and absolute depth by \((40-p(z))^{10}\), proving (7).

We now check every residual condition.

First, the largest fiber is the anchor fiber.  The exact singleton gap is
\[
\overline W-4\cdot40^{10}
=473457768270776000>0.
\tag{13}
\]
Thus \(w_z<W/4\) for every lattice point.

For the primitive-line condition, let \(\ell\) be any affine line in
\(\mathbb R^2\).  Unless \(\ell\) contains an edge of \(kT\), it meets the
boundary of \(kT\) in at most two points.  If it contains an edge, (11)
shows that it contains at most \(2k+1\) points of \(S_k\).  A fixed affine
line can contain an edge of at most one member of the homothetic family
\(\{kT:k\geq1\}\).  It follows that
\[
\sum_{z\in\ell\cap\mathbb Z^2}\frac{w_z}{V}
\leq
2\sum_{r=1}^{40}r^{10}
+
\max_{1\leq k\leq39}(2k-1)(40-k)^{10}.
\tag{14}
\]
The continuous function
\[
g(x):=(2x-1)(40-x)^{10}
\]
increases up to \(x=45/11\) and decreases afterward.  Hence its maximum
on the integers \(1,\ldots,39\) is at \(4\) or \(5\), and
\[
7\cdot36^{10}-9\cdot35^{10}
=766182898800207>0.
\]
Therefore the right side of (14) is
\[
\begin{aligned}
\overline L
&:=
2\sum_{r=1}^{40}r^{10}+7\cdot36^{10}\\
&=
87182411918675400+25593109080440832\\
&=
112775520999116232.
\end{aligned}
\]
The exact gap
\[
\overline W-2\overline L
=289849766272543536>0
\tag{15}
\]
shows that every affine lattice line, and hence every coset of every
primitive rank-one sublattice, has mass strictly below \(W/2\).

We next prove the anchor halfspace condition.  Give each primitive lattice
segment on \(\partial T\) length one.  The three edge lengths
\(A_1B_1,B_1C_1,C_1A_1\) are then \(1,2,1\).  Let \(L\) be a nonzero
linear functional, and write
\[
a=L(A_1),\qquad b=L(B_1),\qquad c=L(C_1).
\]
The barycentric identity
\[
0=\frac12A_1+\frac14B_1+\frac14C_1
\]
gives
\[
2a+b+c=0.
\tag{16}
\]
We claim that the part of \(\partial T\) in the closed halfplane
\(\{L\geq0\}\) has lattice length at least \(1\).  Zero vertex values
follow by a limit, so consider nonzero signs.  If two vertex values are
positive, the boundary part contains their connecting edge, whose lattice
length is at least \(1\).  If only \(a\) is positive, write
\(b=-ra\), \(c=-sa\).  Equation (16) gives \(r+s=2\), and the two positive
edge pieces have total length
\[
\frac1{1+r}+\frac1{1+s}
=\frac4{3+rs}\geq1.
\tag{17}
\]
If only \(b\) is positive, write \(a=-rb\), \(c=-sb\).  Then
\(s=1-2r\), with \(0\leq r\leq1/2\), and the two positive edge pieces
have total lattice length
\[
\frac1{1+r}+\frac2{1+s}
=\frac1{1+r}+\frac1{1-r}
=\frac2{1-r^2}\geq2.
\tag{18}
\]
The case in which only \(c\) is positive is symmetric.  This proves the
claim.

Scaling by \(k\) shows that every closed halfplane through \(0\) meets
\(\partial(kT)\) in a closed boundary arc of lattice length at least
\(k\).  The lattice points on this boundary occur at integer positions in
the lattice-length coordinate.  A closed interval of length at least the
integer \(k\) contains at least \(k\) integer positions.  Hence
\[
\#(S_k\cap Q)\geq k
\tag{19}
\]
for every closed halfplane \(Q\) through \(0\).  Any proper closed
halfplane containing \(0\) contains a parallel boundary-through-\(0\)
halfplane.  Equations (12) and (19) therefore give
\[
\begin{aligned}
\sum_{z\in Q\cap\mathbb Z^2}w_z
&\geq
V\left(40^{10}+\sum_{k=1}^{39}k(40-k)^{10}\right)\\
&=
V\cdot136714522067694000\\
&=
\frac W4+\frac34V40^{10}
>
\frac W4.
\end{aligned}
\tag{20}
\]
The support contains the three vertices of \(39T\), and (16) has strictly
positive coefficients.  Thus \(w_0>0\) and
\[
0\in\operatorname{int}\operatorname{conv}\{z:w_z>0\}.
\tag{21}
\]

We next check parity.  Order the four parity classes as
\((00,01,10,11)\).  Directly from (11),
\[
\bigl(\#(S_k\cap r)\bigr)_r
=
\begin{cases}
(2k,2k,0,0),&k\text{ even},\\
(0,0,2k,2k),&k\text{ odd}.
\end{cases}
\tag{22}
\]
Including the origin in class \(00\), exact summation yields
\[
\begin{aligned}
\overline W_{00}
&=
40^{10}
+
\sum_{\substack{1\leq k\leq39\\k\ {\rm even}}}
2k(40-k)^{10}
=134129731598336000,\\
\overline W_{01}
&=
\sum_{\substack{1\leq k\leq39\\k\ {\rm even}}}
2k(40-k)^{10}
=123643971598336000,\\
\overline W_{10}
=\overline W_{11}
&=
\sum_{\substack{1\leq k\leq39\\k\ {\rm odd}}}
2k(40-k)^{10}
=128813552537052000,
\end{aligned}
\tag{23}
\]
where \(W_r=V\overline W_r\).  The diagonal square mass is
\[
\sum_z w_z^2
=V^2\overline D,
\qquad
\overline D
=40^{20}+4\sum_{k=1}^{39}k(40-k)^{20}
=1596865703638933688849343927831360.
\tag{24}
\]
Thus
\[
Q^\circ
=V^2\overline Q,
\qquad
\overline Q
=64867613542044552038572295272168640,
\tag{25}
\]
and the exact certificate
\[
256\overline Q-16\overline W^2
=12355901176104698082717137314859171840>0
\tag{26}
\]
proves
\[
Q^\circ>\frac1{16}W^2>
\frac{16-e}{256}W^2.
\]

It remains to verify the support-safe energy and the heavy-set failure.
Put
\[
q:=\left(1-\gamma\right)^{1/10}.
\]
Since \(R_0=w_0^{1/10}=40V^{1/10}\), the energy budget is
\[
S_0=80qV^{1/10}.
\]
The exact integer inequality
\[
80^{10}(11^{10}-10^{10})-76^{10}11^{10}
=4377971658631502299239809024>0
\tag{27}
\]
gives
\[
S_0>76V^{1/10}.
\tag{28}
\]

For a nonzero lattice vector \(v=(x,y)\), a direct calculation from (1)
gives
\[
p(v)+p(-v)
=2\max\{|x|+|y|,2|y|\}.
\tag{29}
\]
This is an even positive integer.  It equals \(2\) only for
\(v=\pm(1,0)\), and is at least \(4\) otherwise.  Set
\[
A:=(40-p(v))_+,\qquad B:=(40-p(-v))_+.
\]
If \(v\neq\pm(1,0)\), then either one root is zero or (29) gives
\[
A+B\leq76.
\]
Equations (28) and the feasible choice
\((s,t)=(A,B)V^{1/10}\) therefore show that the corresponding
\(\Phi\)- and \(\Psi\)-terms are exactly zero.  There is only one unordered
exceptional pair, \(\{(1,0),(-1,0)\}\), and it has \(A=B=39\).  The feasible
choice
\[
(s,t)=(39,37)V^{1/10}
\]
has sum \(76V^{1/10}<S_0\), so its contribution is at most
\[
V(39^{10}-37^{10})
=V\cdot3{,}331{,}821{,}712{,}773{,}752.
\tag{30}
\]
Consequently
\[
\mathcal E^\Psi_{10}(w;0)
\leq
V\left[
\frac{10^{10}}{11^{10}}40^{10}
+39^{10}-37^{10}
\right].
\tag{31}
\]
The exact gap
\[
\begin{aligned}
&11^{10}\overline W\\
&\quad
-64\left[
10^{10}40^{10}
+11^{10}(39^{10}-37^{10})
\right]\\
&=
1126475238438901943160507072>0
\end{aligned}
\tag{32}
\]
proves (8).

Also
\[
11^{10}\overline W-64\cdot10^{10}40^{10}
=6657283203817709691760376000>0.
\tag{33}
\]
Since \(w_z\leq w_0=V40^{10}\), equation (33) gives
\[
w_z<\frac{V\overline W}{64\gamma}=\frac W{64\gamma}
\qquad(z\in\mathbb Z^2).
\]
Thus the heavy set is empty, proving (9) and in particular the registered
heavy-hull failure.

Finally, we control every level exactly.  For \(0<t\leq M(0)\), set
\[
s:=\left(\frac{t}{\gamma V}\right)^{1/10},
\qquad
k:=\lfloor40-s\rfloor.
\]
Then \(0\leq k\leq39\), and integrality of \(p(z)\) gives the complete
level set
\[
D_t=\{z\in\mathbb Z^2:p(z)\leq k\}=kT\cap\mathbb Z^2.
\tag{34}
\]
Use the proper closed halfplane
\[
Q_+:=\{(x,y):x\geq0\}.
\]
For a fixed integer \(x\in[0,k]\), the points of \(kT\cap Q_+\) satisfy
\[
|y|\leq\frac{k-x}{2}.
\]
Therefore
\[
\begin{aligned}
H_k
&:=
\#(kT\cap Q_+\cap\mathbb Z^2)\\
&=
\sum_{j=0}^k\left(2\left\lfloor\frac j2\right\rfloor+1\right)\\
&=
\begin{cases}
2m^2+2m+1,&k=2m,\\
2(m+1)^2,&k=2m+1.
\end{cases}
\end{aligned}
\tag{35}
\]
Since \(Q_+\) contains \(0\), equations (34) and (35) imply
\[
\eta(t)\leq H_k.
\tag{36}
\]
The definition of \(k\) also gives
\[
t\leq\gamma V(40-k)^{10}.
\tag{37}
\]

For both parities in (35),
\[
H_k\leq\frac{(k+1)^2+1}{2}.
\tag{38}
\]
Consider
\[
F(x):=\frac{(x+1)^2+1}{2}(40-x)^{10},
\qquad 0\leq x\leq39.
\]
Its derivative has the sign of
\[
41(x+1)-6(x+1)^2-5.
\]
The larger root lies strictly between \(6\) and \(7\) in the variable
\(x+1\).  Hence the integer maximum of \(F(k)\) is at \(k=5\) or \(k=6\).
The exact comparison
\[
25\cdot34^{10}-\frac{37}{2}\,35^{10}
=\frac{1{,}152{,}635{,}622{,}910{,}675}{2}>0
\tag{39}
\]
shows that the maximum is at \(k=6\).  Thus, for every \(k=0,\ldots,39\),
\[
H_k(40-k)^{10}
\leq
25\cdot34^{10}
=51609443851494400.
\tag{40}
\]
Combining (36), (37), and (40) controls every real level \(t\), not only
sampled endpoints:
\[
t\,\eta(t)
\leq
\gamma V\cdot25\cdot34^{10}.
\]
The final exact certificate is
\[
3\cdot11^{10}\overline W
-64\cdot10^{10}\cdot25\cdot34^{10}
=7074464746496713075281128000>0.
\tag{41}
\]
After multiplication by \(V/(64\cdot11^{10})>0\), equation (41) is exactly
the strict inequality in (10).  This completes the counterexample.

## External sources

None beyond the accepted predecessor.
