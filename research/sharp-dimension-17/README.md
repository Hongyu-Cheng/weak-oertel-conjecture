# A counterexample to Oertel's conjecture on mixed-integer centerpoints

Hongyu Cheng and Phillip Kerger

[Manuscript (PDF)](../../output/pdf/oertel-sharp-dimension-17.pdf) ·
[LaTeX source](oertel-sharp-dimension-17.tex) ·
[exact checker](check.py) ·
[Lean proof](../../lean/SharpOC/Selector17Counterexample.lean) ·
[accepted fact](../../facts/ecbacdec2c429376.md)

## The result

For a convex body $C\subset\mathbb R^n\times\mathbb R^d$, the mixed-integer volume $\mu(C)$ is the sum of the $d$-dimensional volumes of the fibers $C_z=\lbrace x:(z,x)\in C\rbrace$ over $z\in\mathbb Z^n$. When $\mu(C)>0$, the depth of a point $p\in\mathbb Z^n\times\mathbb R^d$ is the infimum of $\mu(C\cap H)/\mu(C)$ over the closed halfspaces $H$ containing $p$. Oertel conjectured that every such body has a point of depth at least $2^{-n}\Gamma_d$, where $\Gamma_d=(d/(d+1))^d$ is the constant in Grünbaum's inequality. The product of the cube $[0,1]^n$ and a $d$-simplex shows that this would be best possible. The manuscript disproves the conjecture for $(n,d)=(12,5)$, a total dimension of 17. Its main theorem (Theorem 1.2) reads as follows.

> There is a full-dimensional rational polytope $C\subset\mathbb R^{12}\times\mathbb R^5$ and a rational number $r<2^{-12}\Gamma_5$ such that every point of $\mathbb Z^{12}\times\mathbb R^5$ lies in a closed halfspace $H$ with $\mu(C\cap H)\le r\mu(C)$.

Here $10^5r=9.81146409\ldots$ and $10^5\cdot2^{-12}\Gamma_5=9.81146416\ldots$, a relative gap of about $6.5\cdot10^{-9}$. Every strict inequality in the proof compares explicit rational numbers. The counterexample was obtained by GPT-6 Astra in Codex and is the accepted fact [`ecbacdec2c429376`](../../facts/ecbacdec2c429376.md) of this repository's fact graph; the AI disclosure at the end of Section 6 of the manuscript gives the details.

## The construction

The construction depends on rational parameters $a$, $\delta$, $\varepsilon$, $h$ and $t_0,\dots,t_5$, whose values are given at the end of this section. Write $z=(y,s)\in\mathbb R^{10}\times\mathbb R^2$, $u=y_1+\dots+y_{10}$, $\tau=(\tau_1,\tau_2,\tau_3)=(u-s_2,\ u-s_1,\ u-s_1-s_2)$ and $\sigma=\tau_1+\tau_2+\tau_3$. For $J\subseteq\lbrace1,\dots,10\rbrace$, let $\mathbf 1_J$ be the indicator vector of $J$ and $b_J$ the same vector with its entries in positions $1,\dots,4$ negated. The points $(\mathbf 1_J,0)$ with $J\ne\emptyset$ and $(b_J,s)$ with $s\in\lbrace e_1,e_2,e_1+e_2\rbrace$ represent the 4095 nonzero classes of $\mathbb Z^{12}/2\mathbb Z^{12}$, and $\sigma\ne0$ on each of them. Multiplied by the sign of $\sigma$, they are the *heavy* points. Every heavy point has $\tau\ge0$ and is *paired* of type $j$ if $\tau=e_j$, *one-sided* of type $j$ if $\tau=\mathbf 1-e_j$, and *free* if $\tau\ge\mathbf 1$, where $e_j$ is a unit vector of $\mathbb R^3$, $\mathbf 1=(1,1,1)$, and vector inequalities are componentwise. For each paired point $z$, the point $-z$ is *light* of the same type. The set $\mathcal Z$ consists of the origin and the heavy and light points (Lemma 3.1 and Table 1 of the manuscript).

| points of $\mathcal Z$ | number | $\tau(z)$ | $\sigma(z)$ | fiber $A_z$ |
| --- | ---: | :---: | :---: | :---: |
| origin | 1 | $0$ | $0$ | $B$ |
| paired, type $j$ | $3\times252$ | $e_j$ | $1$ | $(1+\delta)K_j$ |
| light, type $j$ | $3\times252$ | $-e_j$ | $-1$ | $(1-\delta)T_j$ |
| one-sided, type $j$ | $3\times210$ | $\mathbf 1-e_j$ | $2$ | $(1+2\delta)N_j$ |
| free | 2709 | $\ge\mathbf 1$ | $\ge3$ | $hB$ |

The fibers are built from a simplex $B\subset\mathbb R^5$ with centroid at the origin. Volumes are normalized so that $\operatorname{vol}(B)=1$, and dilations such as $hB$ are about the origin. With $x_1,\dots,x_6$ the barycentric coordinates of $B$ and indices $1,2,3$ taken cyclically, the linear functionals $f_j=x_j-a x_{j+1}-(1-a)x_{j+2}$ satisfy $f_1+f_2+f_3=0$, so the caps $B\cap\lbrace f_j\ge0\rbrace$, of volume $\beta$ each, cover $B$. The region $T_j=B\cap\lbrace f_i\le0\text{ for }i\ne j\rbrace$ is the union of two simplices $U_j$ and $P_j$ with a common facet. Then $K_j$ adds to $U_j$ the slab of $P_j$ on which the barycentric coordinate of the vertex opposite this facet is at most $\varepsilon$, and $N_j\subseteq B\cap\lbrace f_j\le0\rbrace$ is a simplex of volume $h^5/(1+2\delta)^5$. The polytope of the theorem is

```math
C=\operatorname{conv}\bigcup_{z\in\mathcal Z}\lbrace z\rbrace\times A_z\subset\mathbb R^{12}\times\mathbb R^5,
```

and its fiber over $z\in\mathbb Z^{12}$ is $A_z$ if $z\in\mathcal Z$ and empty otherwise (Lemmas 3.2 and 4.3).

Every point of $\mathcal Z$ other than the origin is a vertex of $\operatorname{conv}(\mathcal Z)$. So for each such point $z$ and each halfspace $G$ of $\mathbb R^5$, there is a halfspace $H$ of $\mathbb R^{12}\times\mathbb R^5$ with $H_z=G$ that misses all other fibers. Free and one-sided fibers are simplices of volume $h^5$, so each of their points lies in such a tilted Grünbaum cap, of mass $M=(5h/6)^5$. A paired fiber $(1+\delta)K_j$ is covered by six tilted halfspaces $\lbrace x:\nu_i(x/(1+\delta))\ge t_i\rbrace$, where $\nu_0,\dots,\nu_5$ are the barycentric coordinates of $U_j$ in the vertex order of Section 4 and $\sum_it_i=1$; their masses are $(1+\delta)^5V_i$ with $V_i=\operatorname{vol}(K_j\cap\lbrace\nu_i\ge t_i\rbrace)$ (Lemma 5.4). The origin, however, is the midpoint of every pair $z,-z$ of a paired and a light point, so its fiber cannot be isolated. Instead, the three halfspaces $H_j=\lbrace(z,x):f_j(x)\ge3\tau_j(z)\rbrace$ cover the origin fiber and all light fibers: $H_j$ meets $B$ in the cap $B\cap\lbrace f_j\ge0\rbrace$, contains the 252 light fibers of type $j$, of total volume $L$, and meets every other fiber in a set of volume zero, so its mass is $\beta+L$.

A point of $\mathbb Z^{12}\times\mathbb R^5$ outside $C$ lies in a halfspace disjoint from $C$. The theorem therefore holds with $r=M/\mu(C)$ as soon as

```math
\beta+L<M,\qquad (1+\delta)^5V_i<M\quad(i=0,\dots,5),\qquad 4096h^5<W,
```

where $W=\mu(C)=1+756(1+\delta)^5V+3L+3339h^5$ with $V=\operatorname{vol}(K_j)$, and $3339=630+2709$ counts the one-sided and free points. The first two inequalities put each point of $C\cap(\mathbb Z^{12}\times\mathbb R^5)$ in a halfspace of mass at most $M$, and the third gives $r<(5/6)^5/4096$. The only gain over isolated simplex fibers comes from the origin cluster: it contributes $1+3L$ to $\mu(C)$ while each of its points lies in a halfspace of mass $\beta+L$, and $(1+3L)/(\beta+L)\approx2.48874$ slightly exceeds the ratio $(6/5)^5=2.48832$ of the volume of a simplex to that of a Grünbaum cap. The manuscript takes

```math
a=\tfrac{663}{1000},\qquad \delta=\tfrac{664201}{10^6},\qquad \varepsilon=\tfrac{13}{20000},\qquad h=\tfrac{1111946415}{10^9},
```

```math
(t_0,\dots,t_5)=10^{-9}(166735371,\ 166735294,\ 166324902,\ 166734811,\ 166734811,\ 166734811),
```

and evaluates the closed forms of $\beta$, $L$, $V$ and $V_i$ in exact rational arithmetic (Sections 4 to 6).

## Reproduce the verification

Run both checks from the repository root. The exact checker needs only Python 3. The Lean build needs `elan`, which installs the pinned toolchain `leanprover/lean4:v4.34.1`, and it builds against mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.

```sh
python3 research/sharp-dimension-17/check.py
cd lean && lake exe cache get && lake build && lake env lean CheckAxioms.lean
```

[`check.py`](check.py) uses exact rational arithmetic. It generates the points of $\mathcal Z$ and confirms the census: 4095 heavy points, among them $3\times252$ paired, 630 one-sided and 2709 free, and 756 light points. It asserts the inequalities among the parameters that the construction uses (for $\frac12<a$, $\varepsilon<10^{-3}$ and $\frac17<t_i<\frac15$, only the consequences that Lemma 5.4 needs) and the three margins. Its output is

```text
integer fibers       4852 (4095 heavy, 756 light, 1 origin)
origin-cut slack     1.26243969153e-06
paired-cap slack     1.21127530129e-09
total-volume surplus 4.54594731886e-05
```

The last three lines are $M-\beta-L$, $M-\max_i(1+\delta)^5V_i$ and $W-4096h^5$, which the script asserts to exceed $10^{-6}$, $10^{-9}$ and $4\cdot10^{-5}$. The script does not prove that $\mathcal Z$ contains every integer point of $\operatorname{conv}(\mathcal Z)$; that is Lemma 3.2.

The Lean theorem [`SharpOC.Selector17.sharp_oc_counterexample`](../../lean/SharpOC/Selector17Counterexample.lean) formalizes the bound on the depth, including the consequences of Lemma 3.2. It states that there are a compact convex set $C\subset\mathbb R^{12}\times\mathbb R^5$ with nonempty interior, containing the origin, with $0<\mu(C)<\infty$, and a real number $r$ with $0<r<2^{-12}\Gamma_5$ such that every point of $\mathbb Z^{12}\times\mathbb R^5$ lies in a closed halfspace $H$ with $\mu(C\cap H)\le r\mu(C)$. Rationality of $C$ and $r$ is not part of the statement. The last command fails unless this theorem and the other results listed in [`CheckAxioms.lean`](../../lean/CheckAxioms.lean) depend only on the axioms `propext`, `Classical.choice` and `Quot.sound`.

## Build the manuscript

Use XeLaTeX and latexmk, with `DejaVuSansMono.ttf` available to XeLaTeX (it is included in TeX Live). Run from the repository root, since the manuscript includes the TikZ figures in [`figures/`](figures) by paths relative to it.

```sh
build_dir=$(mktemp -d)
latexmk -xelatex -halt-on-error -outdir="$build_dir" \
  research/sharp-dimension-17/oertel-sharp-dimension-17.tex
```

The PDF is written to `$build_dir/oertel-sharp-dimension-17.pdf`. The committed copy is [`output/pdf/oertel-sharp-dimension-17.pdf`](../../output/pdf/oertel-sharp-dimension-17.pdf).
