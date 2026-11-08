---
fact_id: 6ae2eb173ed91aee
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-guarded-planar-diffuse-curvature-generators
depends_on: []
verifier_run: 7ce53db05fe81373
target_match: null
---

## Source

- [c7a0c159c6cf35f0](../candidates/c7a0c159c6cf35f0.json), c7a0c159c6cf35f0:01 §§2–3, (1)–(4), guarded sources.
- [181e74b2f3c435dc](../candidates/181e74b2f3c435dc.json), §1, diffuse locality of the BV derivative.
- [ed7be0e1efdfe13b](../candidates/ed7be0e1efdfe13b.json), §§2–4, compact Green potentials and signed curvature perturbations.

## Statement

Let finitely many planar convex bodies $K_z$ with interior have support functions $h_z$ satisfying the finite Jensen rows $g_a=\sum_z q_{az}h_z\ge0$ that describe their compatibility. Fix finitely many nonvertical caps, with fixed planar halfplanes at each fiber. Let $R_z=h_z+h_z''$ be the full curvature measure, $R=\sum_z R_z^{\rm diff}$ the sum of the nonatomic parts, and $r_z=dR_z^{\rm diff}/dR$. At an angle $\theta$ let $J(\theta)=\{z:r_z(\theta)>0\}$, $A(\theta)=\{a:g_a(\theta)=0\}$, and
$$
L(\theta)=\{v:v_z=0\text{ for }z\notin J(\theta),\quad q_a\cdot v=0\text{ for }a\in A(\theta)\}.
$$
At $R$-almost every angle the whole exposed face in each fiber in $J(\theta)$ has a strict side for every cap, and $r(\theta)\in L(\theta)$.

The exact patterns $(A,J,(I_{jz})_{j,z\in J})$, where $I_{jz}$ is the strict inside bit of cap $j$, admit a countable exhaustion up to $R$-null sets by bounded nonatomic source measures $\nu$ dominated by every $R_z$ for $z\in J$. Each has a compact interval guard of length less than $\pi$, on which the inactive Jensen gaps have a common positive lower bound and the entire exposed faces for $z\in J$ have the prescribed strict cap signs with a positive margin. For each such source and $v$ in its fixed pattern kernel, there exists a compactly supported signed feasible support variation $t v_z\phi$ in that guard, feasible for both small signs of $t$. Its first total and cap area derivatives are zero and its second total and cap area derivatives may be normalized to $-\sum_z v_z^2$ and $-\sum_z I_{jz}v_z^2$, respectively.

## Proof

A line cutting the interior of a planar convex body meets its boundary in at most two points. If it is supporting, its contact set is a point or a segment. The normal cone of a boundary point contributes zero curvature in its interior, since there $h$ is the dot product of that point with the unit normal and solves $h+h''=0$. Cone endpoints, and the facet normal in the segment case, form a finite set. Thus the angles at which an exposed face meets a fixed cap line have zero nonatomic curvature measure of that fiber. On $\{r_z>0\}$ such a set is also $R$-null, by the Radon–Nikodym formula. At every remaining relevant angle the whole exposed face has a strict sign. Upper semicontinuity of exposed faces, obtained by taking limits of maximizing points, gives a neighborhood with a positive uniform margin.

For each nonnegative Jensen gap $g_a$, its derivative is BV, since $h_z''$ is a finite signed measure and the supports are Lipschitz. At each continuity point of that BV derivative at which $g_a=0$, the derivative is zero by differentiability and nonnegativity. To see diffuse locality, for a one-dimensional BV function $u$ apply the BV chain rule to $T_\epsilon(u)=\epsilon\arctan(u/\epsilon)$. Its diffuse derivative is $T'_\epsilon(u)D^{\rm diff}u$, and its jumps are the differences of $T_\epsilon$ at the two one-sided traces. The functions tend uniformly to zero, the jump differences tend to zero and are bounded by the summable original jump sizes, and $T'_\epsilon(u)\to\mathbf1_{\{u=0\}}$ with bound one on the diffuse part. Passing to distributions gives $D^{\rm diff}u|_{\{u=0\}}=0$ with the representative at continuity points. Thus the diffuse part of $g_a+g_a''=\sum_z q_{az}R_z$ vanishes on $\{g_a=0\}$. Taking its density with respect to $R$ yields $q_a\cdot r=0$ on that set almost everywhere, and proves $r\in L$. The chain rule used here is [Vol'pert, The spaces BV and quasilinear equations](https://doi.org/10.1070/SM1967v002n02ABEH002340).

For each finite pattern discard the above null sets. Cover the remainder by a countable collection of intervals with rational endpoints whose compact closures lie in neighborhoods of all strict cap and inactive Jensen margins and whose lengths are less than $\pi$. Exhaust each by compact subintervals, intersect each with the pattern and with $\min_{z\in J}r_z\ge1/k$ for integers $k\ge1$. For each resulting set $E$ of positive measure, use $\nu=(1/k)R|_E$. It is nonatomic and $\nu\le R_z^{\rm diff}\le R_z$ for each $z\in J$. Its support is contained in the compact guard and in every closed active zero set. This gives the claimed exhaustion by restrictions of $R$ with bounded density relative to each affected curvature.

Take a compact interval $[a,b]$ strictly inside the guard with positive $\nu$ mass, and use the restriction of the source there. For bounded $\psi$ on that restriction set
$$
\phi(\theta)=\int_{[a,\theta]}\sin(\theta-s)\psi(s)\,d\nu(s)
\quad(a\le\theta\le b).
$$
Impose $\int\cos(s)\psi\,d\nu=\int\sin(s)\psi\,d\nu=0$ so that $\phi$ and $\phi'$ vanish at both endpoints and extend by zero. Since $\nu$ has no atoms, the extension is $C^1$ and $\phi''+\phi=\psi\nu$ distributionally. Impose in addition $\int\phi\,dR_z=0$ for every fiber. Choose $\psi$ constant on each of $|P|+3$ disjoint sets of positive $\nu$ measure, and zero elsewhere, where $|P|$ is the number of fibers. The two endpoint equations and the $|P|$ area equations are homogeneous linear equations in those constants. A nonzero solution gives a nonzero $\psi\nu$ and thus a nonzero $\phi$. Dirichlet Poincaré on $[a,b]$ of length less than $\pi$ gives $\int(\phi^2-\phi'^2)<0$, so scale to make this integral $-1$.

For small $|t|$, $R_z+t v_z\psi\nu\ge0$ by domination in the changed fibers. A continuous periodic function with nonnegative $h+h''$ is a planar support function. This follows by circular smoothing and adding a small positive constant, using the smooth curve $h u+h'u'$ for $u(\theta)=(\cos\theta,\sin\theta)$ and its derivative $(h+h'')u'$, then taking the uniform limit of the smooth supports. The perturbed supports stay close to the original ones, hence their bodies retain positive inballs. Every active row variation vanishes on the entire circle since $q_a\cdot v=0$. The remaining gaps stay nonnegative because on the guard they have a positive margin and elsewhere the variation is zero. This proves feasibility without requiring any active contact interval.

The area formula $\frac12\int(h_z^2-h_z'^2)\,d\theta$ follows by integrating the smooth boundary curve and passing to the limit by circular smoothing in $H^1$. It gives first derivative $v_z\int\phi\,dR_z=0$ and second derivative $v_z^2\int(\phi^2-\phi'^2)=-v_z^2$. For a fixed cap, all affected exposed faces, including their endpoints at atom angles, remain on their original strict sides because their endpoints shift by $t v_z(\phi u+\phi' u')$. The two body boundaries have a common path outside the guard, and the difference of their remaining arcs is a closed path entirely on the same strict side of the cap line. The difference of the interior indicators off the boundaries is the winding number of that path. It vanishes in the opposite halfplane, since the path contracts in its own halfplane. Therefore the change of cap area is exactly the inside bit times the full area change. Summing these identities gives all asserted derivatives.
