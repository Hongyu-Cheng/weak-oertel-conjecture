---
fact_id: bd7eeefd1636ff7d
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: common-normal-stress-aware-centroid-host-extraction
depends_on: ["2c7ef442c71a1564","3d1f63abf09b2abb","62f2ec156b347dfe","6d6fcf377e68c79c","8aac56c49321466c","daef2580cdfec07b","dfd25e72c1f45a4e","fbeb0a501b268d12"]
verifier_run: bdc989476e4644bd
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and use the fiber notation
\[
 C_z:=\{y\in\mathbb R^d:(z,y)\in C\},
 \qquad
 a_z:=\operatorname{vol}_d(C_z),
 \qquad
 I_+:=\{z\in\mathbb Z^n:a_z>0\},
\]
\[
 W:=\sum_{z\in I_+}a_z,
 \qquad
 G:=\mathfrak C_{\mathrm{core}}(C).
\tag{1}
\]
Let \(A\subseteq\mathbb R^n\) be an affine subspace such that
\[
 D_A:=I_+\cap A\ne\varnothing,
 \qquad
 \operatorname{aff}(D_A)=A,
 \qquad
 \dim A=2,
 \qquad
 W_A:=\sum_{z\in D_A}a_z.
\tag{2}
\]
Then there are a finite nonempty \(E\subseteq D_A\), masses \(0<t_z\leq a_z\), and an integer point \(m\in A\cap\mathbb Z^n\cap\operatorname{conv}E\) such that
\[
 \bigcap_{\lambda\in\Lambda_m(E)}
 \sum_{z\in E}\lambda_z\mathsf M_{t_z}(C_z)
 \ne\varnothing,
\tag{3}
\]
every proper relative closed halfspace \(J_A\subseteq A\) containing \(m\) satisfies
\[
 \sum_{z\in E\cap J_A}t_z
 \geq\frac14\sum_{z\in E}t_z,
\tag{4}
\]
and the attained total mass obeys
\[
 \boxed{
 \tau:=\sum_{z\in E}t_z\geq\frac{W_A}{32}.}
\tag{5}
\]

Now retain the common actual canonical hard instance and the notation of accepted fact 2c7ef442c71a1564. Thus \(Q>0\),
\[
 G<\frac Q{100},
 \qquad
 W\geq8Q,
\tag{6}
\]
the larger provenance color is the off-diagonal color, \(q^*\ne0\) is its balanced optimizer, and
\[
 |q^*|>\frac{553}{51200}Q,
 \qquad
 A:=\operatorname{aff}(T_*),
 \qquad
 \dim A=2,
 \qquad
 W_A\geq8|q^*|.
\tag{7}
\]
Then the case \(n=4\) is impossible. More precisely, if \(n=4\), the tuple in (3)-(5) satisfies
\[
 \boxed{G\geq4\tau\geq\frac{W_A}{8}\geq|q^*|>\frac Q{100},}
\tag{8}
\]
contradicting (6).

## Proof

We first prove a planar lattice extraction that improves the factor used in accepted fact 8aac56c49321466c. Let \(K\subseteq\mathbb R^2\) be compact and convex, let
\[
 D:=K\cap\mathbb Z^2,
 \qquad
 N:=|D|>0.
\tag{9}
\]
There is a lattice simplex \(T\subseteq\operatorname{conv}D\), of affine dimension zero, one, or two, such that
\[
 \boxed{|T\cap\mathbb Z^2|\geq\frac N4.}
\tag{10}
\]
If \(D\) has affine dimension zero or one, take \(T=\operatorname{conv}D\). Convexity gives \(T\cap\mathbb Z^2=D\), so (10) is immediate.

Suppose that \(D\) has affine dimension two and put \(P:=\operatorname{conv}D\). Since \(P\subseteq K\),
\[
 P\cap\mathbb Z^2=D.
\tag{11}
\]
Choose a maximum-area triangle contained in \(P\). A maximizing triangle can be chosen with all three vertices among the vertices of \(P\): with two vertices fixed, the area is the absolute value of an affine functional of the third vertex, so a maximum over the polygon is attained at a vertex; replacing the three vertices successively preserves maximality. Hence the resulting \(T\) is a lattice triangle.

Write \(I\) and \(B\) for the numbers of interior and boundary lattice points of \(P\), so \(N=I+B\). Suppose first that \(I>0\). Blaschke's maximum-inscribed-triangle theorem gives
\[
 \operatorname{area}(T)
 \geq\frac{3\sqrt3}{4\pi}\operatorname{area}(P)
 >\frac25\operatorname{area}(P).
\tag{12}
\]
Scott's lattice-polygon inequality gives
\[
 B\leq2I+7.
\tag{13}
\]
Using Pick's formula in the exact form recorded in accepted fact daef2580cdfec07b, first for \(T\) and then for \(P\), yields
\[
 \begin{aligned}
 |T\cap\mathbb Z^2|
 &\geq\operatorname{area}(T)+1\\
 &>\frac25\left(I+\frac B2-1\right)+1.
 \end{aligned}
\tag{14}
\]
The difference between the last expression and \(N/4=(I+B)/4\) is
\[
 \frac{3I-B+12}{20}
 \geq\frac{I+5}{20}>0
\tag{15}
\]
by (13). Thus (10) holds when \(I>0\).

Suppose instead that \(I=0\). The classification of hollow lattice polygons says that, up to an affine unimodular transformation and an integral translation, \(P\) is either \(2\Delta_2\) or a Lawrence polygon
\[
 \operatorname{conv}\{(0,0),(1,0),(0,h_0),(1,h_1)\}
 \qquad(h_0,h_1\in\mathbb Z_{\geq0}).
\tag{16}
\]
In the first case take \(T=P\). In the second case all lattice points of \(P\) lie on the two lattice lines with first coordinate zero or one. Choose the longer of the two lattice segments as one side of \(T\), and choose any lattice point on the other line as its third vertex. This triangle lies in \(P\), contains every lattice point of the longer segment, and contains its third vertex. Consequently it contains at least
\[
 \max\{h_0+1,h_1+1\}+1
 \geq\frac{h_0+h_1+2}{2}
 =\frac N2
\tag{17}
\]
lattice points. This proves (10) in the hollow case and completes the planar extraction.

We now construct the slice tuple. Use the saturated intrinsic lattice chart from accepted fact 8aac56c49321466c. Fix \(b\in D_A\), put
\[
 \Gamma:=(A-b)\cap\mathbb Z^n,
\tag{18}
\]
choose a \(\mathbb Z\)-basis of this rank-two lattice, and let \(U:\mathbb R^2\to A-b\) be the induced linear isomorphism with \(U\mathbb Z^2=\Gamma\). Define
\[
 \widehat C:=\{(u,y)\in\mathbb R^2\times\mathbb R^d:
 (b+Uu,y)\in C\}.
\tag{19}
\]
Accepted fact 8aac56c49321466c proves that this is a convex body, that its integer fibers correspond exactly and volume-preservingly to the fibers indexed by \(D_A\), and that, with
\[
 P:=\operatorname{proj}_{\mathbb R^2}\widehat C,
 \qquad
 g(u):=\operatorname{vol}_d(\widehat C_u)^{1/d},
\tag{20}
\]
the function \(g:P\to[0,\infty)\) is concave and
\[
 \sum_{u\in P\cap\mathbb Z^2}g(u)^d=W_A.
\tag{21}
\]
This concavity is the projection consequence of the positive-root metronoid-lift convexity in accepted fact dfd25e72c1f45a4e.

Apply accepted fact 62f2ec156b347dfe in integer dimension two. There is \(s>0\) such that, with
\[
 D_s:=\{u\in P\cap\mathbb Z^2:g(u)\geq s\},
 \qquad N:=|D_s|,
\tag{22}
\]
one has
\[
 s^dN\geq\frac{W_A}{8}.
\tag{23}
\]
Concavity gives
\[
 \operatorname{conv}(D_s)\cap\mathbb Z^2=D_s.
\tag{24}
\]
Apply (10) to the convex set \(\operatorname{conv}(D_s)\). It supplies a lattice simplex \(T\subseteq\operatorname{conv}(D_s)\), of dimension \(k\in\{0,1,2\}\), such that, for
\[
 E_0:=T\cap\mathbb Z^2,
\tag{25}
\]
one has
\[
 |E_0|\geq\frac N4,
 \qquad
 E_0\subseteq D_s.
\tag{26}
\]

Put \(t:=s^d\), and, for \(u\in E_0\), put
\[
 Q_u:=\mathsf M_t(\widehat C_u).
\tag{27}
\]
These sets are nonempty because \(t\leq g(u)^d\). Let \(v_0,\ldots,v_k\) be the vertices of \(T\), with barycentric coordinates \(\lambda_0,\ldots,\lambda_k\). The positive-root convexity in accepted fact dfd25e72c1f45a4e, used at the same root \(s\) at every vertex, gives the set-valued interpolation
\[
 \sum_{i=0}^k\lambda_i(u)Q_{v_i}\subseteq Q_u
 \qquad(u\in E_0).
\tag{28}
\]
For \(k=0\), (28) is the identity at the unique point.

Apply accepted fact 6d6fcf377e68c79c to the uniform finite measure \(t\sum_{u\in E_0}\delta_u\) on \(\mathbb Z^2\). It gives an \(m_0\in\mathbb Z^2\cap\operatorname{conv}E_0\) such that every proper closed halfspace \(J\subseteq\mathbb R^2\) containing \(m_0\) satisfies
\[
 t|E_0\cap J|\geq\frac14t|E_0|.
\tag{29}
\]
The set-valued simplex-core principle in accepted fact fbeb0a501b268d12, applied to (28), gives
\[
 \varnothing\ne
 \sum_{i=0}^k\lambda_i(m_0)Q_{v_i}
 \subseteq
 \bigcap_{\eta\in\Lambda_{m_0}(E_0)}
 \sum_{u\in E_0}\eta_uQ_u.
\tag{30}
\]

Map (25)-(30) back to \(A\) by \(u\mapsto b+Uu\), and assign the common mass \(t\) to every selected fiber. The chart is an affine lattice isomorphism, so it preserves every barycentric representation and every relative halfspace. Equations (29)-(30) therefore prove (3)-(4). The total selected mass is
\[
 \tau=t|E_0|
 \geq\frac14s^dN
 \geq\frac{W_A}{32}
\tag{31}
\]
by (23) and (26). This proves (5).

It remains to apply the improvement to the common-normal instance. Assume \(n=4\). The two-plane \(A\) in (7) is proper. Apply the complete-capacity one-sided augmentation theorem in accepted fact 3d1f63abf09b2abb to the actual tuple just constructed, with relative balance \(\beta=1/4\). Its support-free heavier-side form gives
\[
 G\geq
 \min\left\{
 \tau+\frac{W-W_A}{2},
 \ 4\tau
 \right\}.
\tag{32}
\]
By (5), the first entry satisfies
\[
 \tau+\frac{W-W_A}{2}
 \geq\frac{W_A}{32}+\frac{W-W_A}{2}
 \geq\frac W{32}
 \geq\frac Q4
 >G,
\tag{33}
\]
where (6) supplies the last two comparisons. Hence the second entry in (32) must be at most \(G\), and therefore
\[
 G\geq4\tau\geq\frac{W_A}{8}\geq|q^*|.
\tag{34}
\]
Finally,
\[
 \frac{553}{51200}-\frac1{100}
 =\frac{41}{51200}>0.
\tag{35}
\]
Equations (6), (7), and (34)-(35) give \(G>Q/100\), contradicting the canonical hard inequality. This proves (8) and rules out \(n=4\).

## External sources

Wilhelm Blaschke, "Über affine Geometrie VII: Neue Extremeigenschaften von Ellipse und Ellipsoid," Berichte über die Verhandlungen der Königlich-Sächsischen Gesellschaft der Wissenschaften zu Leipzig, Mathematisch-Physische Klasse 69 (1917), 306-319, archive record https://archiv.saw-leipzig.de/saw-archive/publikationen-quellen/publikationen/berichte-ueber-die-verhandlungen-der-koeniglich-saechsischen-gesellschaft-der-wissenschaften-zu-leipzig-mathematisch-physische-klasse-bd-1/berichte-ueber-die-verhandlungen-der-koeniglich-saechsischen-gesellschaft-der-wissenschaften-zu-leipzig-mathematisch-physische-klasse-bd-69/ueber-affine-geometrie-vii-neue-extremeigenschaften-von-ellipse-und-ellipsoid. The exact result used in (12) is that a maximum-area triangle inscribed in a planar convex body \(P\) has area at least \(3\sqrt3/(4\pi)\) times the area of \(P\). The constant is strictly larger than \(2/5\). The hypotheses apply because \(P\) is a nondegenerate compact convex lattice polygon, and the vertex-replacement argument above shows that a maximum triangle may be chosen with lattice vertices.

Christian Haase and Josef Schicho, "Lattice polygons and the number \(2i+7\)," author version https://arxiv.org/abs/math/0406224, Proposition 3. The exact result used in (13) is: if a convex lattice polygon has \(I>0\) interior lattice points and \(B\) boundary lattice points, then \(B\leq2I+7\). The polygon \(P\) in that case is convex, two-dimensional, and has \(I>0\), so the theorem applies directly.

Jaron Treutlein, "3-Dimensional Lattice Polytopes Without Interior Lattice Points," https://arxiv.org/abs/0809.1787, Introduction, citing the complete two-dimensional classification of Arkinstall, Khovanskii, Koelman, and Schicho. The exact two-dimensional result used in (16) is: every two-dimensional lattice polygon with no interior lattice point is affine-unimodularly equivalent either to \(2\Delta_2\) or to a Lawrence polygon \(\operatorname{conv}\{0,e_1,h_0e_2,e_1+h_1e_2\}\) with nonnegative integral heights. This applies exactly when the rank-two polygon \(P\) has \(I=0\).
