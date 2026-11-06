---
fact_id: 8f149cd316cabfac
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct28-mersenne-parity-unbounded-minimum
depends_on: []
verifier_run: 1aae19baa3b546a6
target_match: null
---

## Statement

A finite support \(W\subset\mathbb Z^m\) is called complete here if \(W=\operatorname{conv}(W)\cap\mathbb Z^m\). For each integer \(L\ge 2\), define
$$
P_2(L)=\operatorname{conv}\lbrace (0,1),(2L,1),(1,0)\rbrace,\qquad
P_{m+1}(L)=\operatorname{conv}\bigl((P_m(L)\times\lbrace 0\rbrace)
\cup(\sigma_m P_m(L)\times\lbrace 2\rbrace)\bigr)
\quad(m\ge 2),
$$
where \(\sigma_m:\mathbb R^m\to\mathbb R^m\) exchanges the first and last coordinates and fixes all other coordinates. Set \(W_m(L)=P_m(L)\cap\mathbb Z^m\). For \(\varepsilon\in\lbrace 0,1\rbrace^m\), let \(c_m(\varepsilon;L)=|W_m(L)\cap(\varepsilon+2\mathbb Z^m)|\), and let \(K_m(L)\) denote the number of parity vectors with positive \(c_m(\varepsilon;L)\).

Every \(P_m(L)\) is a full-dimensional lattice polytope, and every \(W_m(L)\) is finite, full-dimensional, and complete. The three-dimensional parity census, with bits ordered as coordinates \(x,y,z\), is
$$
\begin{aligned}
&\bigl(c_3(000;L),c_3(100;L),c_3(010;L),c_3(110;L),
c_3(001;L),c_3(101;L),c_3(011;L),c_3(111;L)\bigr)\\
&\hspace{1em}=
\bigl(0,L+2,L+2,2L,a^2,ab+1,ab+1,b^2\bigr),
\qquad
a=\lfloor L/2\rfloor,\quad b=\lceil L/2\rceil.
\end{aligned}
$$
Here, for example, \(100\) denotes \((1,0,0)\). Thus \(W_3(6)\) has census \((0,8,8,12,9,10,10,9)\), cardinality \(66\), occupied count \(K_3(6)=7\), and minimum occupied-class cardinality \(8\).

For every pair of integers \(n\ge 3\), \(M\ge 1\), the explicit choice
$$
L=1+2^{n-3}(2M-1)
$$
gives \(c_n(\mathbf 0;L)=0\) and \(c_n(\varepsilon;L)\ge M\) for every nonzero \(\varepsilon\in\lbrace 0,1\rbrace^n\). In particular \(K_n(L)=2^n-1\). For every integer \(r\ge 2\), taking \(n=2r\) and \(M=q=2^{2r}-1\) gives exactly \(q\) occupied classes, each with at least \(q\) points.

## Proof

Fix an integer \(L\ge 2\). The triangle \(P_2(L)\) has affinely independent integer vertices: the two difference vectors \((2L,0)\) and \((1,-1)\) have determinant \(-2L\ne 0\). If \(P_m(L)\) is the convex hull of finitely many integer points, the defining two copies for \(P_{m+1}(L)\) have the same property, so their convex hull is again a lattice polytope. If \(P_m(L)\) is full-dimensional, its copy at last coordinate \(0\) has affine dimension \(m\), and any point of the nonempty copy at last coordinate \(2\) lies outside that affine hull. Thus \(P_{m+1}(L)\) is full-dimensional. This proves the asserted polytope properties by induction. Boundedness makes \(W_m(L)\) finite. The integer vertices of \(P_m(L)\) belong to \(W_m(L)\), so \(\operatorname{conv}(W_m(L))=P_m(L)\). Therefore \(W_m(L)\) is full-dimensional and complete.

We first establish an exact section formula. For nonempty convex sets \(A,B\subset\mathbb R^m\), put \(D=\operatorname{conv}((A\times\lbrace 0\rbrace)\cup(B\times\lbrace 2\rbrace))\). Then
$$
\lbrace u\in\mathbb R^m:(u,t)\in D\rbrace
=
\begin{cases}
(1-t/2)A+(t/2)B,&0\le t\le 2,\\
\varnothing,&t\notin[0,2].
\end{cases}
$$
The plus sign denotes a Minkowski sum, with scalar multiplication applied to the sets. Indeed, in any convex combination of points from the two copies, let \(\lambda\) be the total coefficient on the second copy. Its last coordinate is \(2\lambda\). Convexity allows the points within each copy to be combined into one point of that copy, giving horizontal coordinate \((1-\lambda)a+\lambda b\), with \(a\in A\) and \(b\in B\). When one coefficient is zero, choose an arbitrary point of the unused nonempty set. Conversely every such combination belongs to \(D\). This proves the formula, including both endpoint sections.

Since \(\sigma_m\) is a bijection of \(\mathbb Z^m\), the section formula gives the following exact, disjoint description of the entire lattice support:
$$
\begin{aligned}
W_{m+1}(L)
={}&(W_m(L)\times\lbrace 0\rbrace)\\
&{}\sqcup
\left(\left(\tfrac12(P_m(L)+\sigma_m P_m(L))\cap\mathbb Z^m\right)
\times\lbrace 1\rbrace\right)\\
&{}\sqcup(\sigma_m W_m(L)\times\lbrace 2\rbrace).
\end{aligned}
$$
There are no other integer heights. In particular, for each \(\varepsilon\in\lbrace 0,1\rbrace^m\),
$$
\begin{aligned}
c_{m+1}((\varepsilon,0);L)
&=c_m(\varepsilon;L)+c_m(\sigma_m\varepsilon;L),\\
c_{m+1}((\varepsilon,1);L)
&=\left|(P_m(L)+\sigma_m P_m(L))
\cap(2\varepsilon+4\mathbb Z^m)\right|.
\end{aligned}
$$
For the second equality, multiplication by \(2\) bijects the integer points in the middle section having parity \(\varepsilon\) with the displayed set. These equalities include boundary lattice points; the middle section is the full continuous Minkowski average, not merely the averages of integer points from the two endpoint supports.

For the base census, write \(T=P_2(L)\), and let \(T^{\mathsf T}=\sigma_2T\) be its coordinate swap. The integer points of \(T\) are exactly
$$
T\cap\mathbb Z^2
=\lbrace(x,1):x=0,1,\ldots,2L\rbrace\cup\lbrace(1,0)\rbrace.
$$
To see this, the triangle has \(0\le y\le 1\); its section at \(y=0\) is the single vertex \((1,0)\), and its section at \(y=1\) is the segment from \((0,1)\) to \((2L,1)\). Accordingly,
$$
T^{\mathsf T}\cap\mathbb Z^2
=\lbrace(1,y):y=0,1,\ldots,2L\rbrace\cup\lbrace(0,1)\rbrace.
$$

Let \(Q=(T+T^{\mathsf T})/2\), the middle section of \(P_3(L)\). We claim that its entire integer support is
$$
Q\cap\mathbb Z^2
=\bigl([1,L]^2\cap\mathbb Z^2\bigr)
\cup\lbrace(0,1),(1,0)\rbrace.
$$
For the inclusion from left to right, every \((x,y)\in Q\) has nonnegative coordinates and satisfies
$$
\begin{gathered}
x\le L+\tfrac12,\qquad y\le L+\tfrac12,\qquad x+y\ge 1,\\
x-(2L-1)y\le 1,\qquad y-(2L-1)x\le 1.
\end{gathered}
$$
The coordinate upper bounds follow because the coordinate maxima of \(T\) are \(2L,1\), and those of \(T^{\mathsf T}\) are \(1,2L\). The other three displayed inequalities hold on both triangles, as direct evaluation at their vertices shows, so they hold on their average. If \((x,y)\) is integral, it follows that \(0\le x,y\le L\). If \(x=0\), the last inequality and \(x+y\ge1\) force \(y=1\). If \(y=0\), the preceding inequality forces \(x=1\). Otherwise both coordinates lie in \(\lbrace1,\ldots,L\rbrace\), which proves the required inclusion.

For the opposite inclusion, the segments \([1,2L-1]\times\lbrace1\rbrace\subset T\) and \(\lbrace1\rbrace\times[1,2L-1]\subset T^{\mathsf T}\) have Minkowski average exactly \([1,L]^2\). Also \((0,1)\) and \((1,0)\) belong to both triangles, hence to \(Q\). This proves the claimed complete integer census of \(Q\) and the useful continuous containment \([1,L]^2\subset Q\).

Combining these three exact sections counts all points of \(W_3(L)\). At the two even heights, parity \(100\) occurs once at height \(0\) and \(L+1\) times at height \(2\). Parity \(010\) occurs \(L+1\) times at height \(0\) and once at height \(2\). Parity \(110\) occurs \(L\) times at each height. Parity \(000\) does not occur. In the square at height \(1\), each coordinate has \(a=\lfloor L/2\rfloor\) even choices and \(b=\lceil L/2\rceil\) odd choices. This gives counts \(a^2,ab,ab,b^2\) for \(001,101,011,111\), respectively. The two additional points \((1,0,1)\) and \((0,1,1)\) add one to \(101\) and \(011\). This proves the asserted eight-entry table. Its entries sum to \(L^2+4L+6\); substituting \(L=6\) gives total \(66\) and the stated seven positive cardinalities, whose minimum is \(8\).

It remains to show that the central boxes stay large through the dimension induction. For every \(m\ge3\), define \(s_m=1+(L-1)/2^{m-3}\). We prove
$$
[1,s_m]^{m-1}\times\lbrace1\rbrace\subset P_m(L).
$$
The case \(m=3\) is the just-proved containment \([1,L]^2\subset Q\). For the induction step, let \(B_m=[1,s_m]^{m-1}\times\lbrace1\rbrace\). The coordinate exchange gives \(\sigma_m B_m=\lbrace1\rbrace\times[1,s_m]^{m-1}\), so
$$
\tfrac12(B_m+\sigma_m B_m)
=
[1,(s_m+1)/2]\times[1,s_m]^{m-2}\times[1,(s_m+1)/2].
$$
Since \(s_m\ge1\) and \(s_{m+1}=(s_m+1)/2\le s_m\), this set contains \([1,s_{m+1}]^m\). The exact section formula places this entire box in the height-\(1\) section of \(P_{m+1}(L)\). This proves the continuous box containment in all dimensions.

Now fix the target integers \(n\ge3\) and \(M\ge1\), and choose \(L=1+2^{n-3}(2M-1)\). This is an integer and \(L\ge2M\ge2\). For \(3\le m\le n\), the box parameters are
$$
s_m=1+2^{n-m}(2M-1)\ge2M.
$$
In particular, at each such dimension \(m\), the middle section contains the integer box \(\lbrace1,\ldots,2M\rbrace^{m-1}\). Each coordinate in this box has exactly \(M\) choices of either parity.

We finish by induction over \(m=3,\ldots,n\), proving that the zero parity is absent and every other parity has at least \(M\) points. For \(m=3\), the exact table applies. Its three positive even-height counts are at least \(M\), and \(a,b\ge M\) imply that each odd-height count is at least \(M^2\ge M\). Its zero-parity count is zero.

Suppose the assertion holds in dimension \(m<n\). The exact even-height count formula gives \(c_{m+1}((\mathbf0,0);L)=0\). For nonzero \(\varepsilon\), the vector \(\sigma_m\varepsilon\) is also nonzero, so that formula gives \(c_{m+1}((\varepsilon,0);L)\ge2M\). For every \(\varepsilon\), including zero, the box \(\lbrace1,\ldots,2M\rbrace^m\) at height \(1\) contains exactly \(M^m\ge M\) integer points of lower-coordinate parity \(\varepsilon\). Thus \(c_{m+1}((\varepsilon,1);L)\ge M\). Any further points in the middle section have odd last coordinate, so they cannot introduce the omitted zero parity. The complete section description rules out any other height or additional source of all-even points.

This proves the claimed absence and lower bounds in dimension \(n\). Since there are exactly \(2^n\) binary parity vectors, precisely \(2^n-1\) are occupied. Finally, for \(r\ge2\), substitute \(n=2r\) and \(M=q=2^{2r}-1\). This gives the stated Mersenne specialization and completes the proof.

## External sources

None.
