---
fact_id: 68b2c92decf5def7
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w35-normality-projective-cap-bias-obstruction
depends_on: ["d90ba05577427854"]
verifier_run: 5e0f7850977ebb2a
target_match: null
---

## Source

- [cc20b8cd85280ba0](../candidates/cc20b8cd85280ba0.json), cc20b8cd85280ba0:01 §§1–3, comparison (X) and all rational data.

## Statement

There is a tetrahedron with a marked interior point and four oriented sections through the mark whose section centroids equal that mark. The area-weighted inward unit normals admit a minimal positive balance with probability weights $\theta$. If $P$ is the $\theta$-weighted cap fraction before applying the unique admissible central projective map for which the transformed body has centroid at the translated origin, and $P'$ is that weighted fraction after the map with the same weights and oriented halfspaces, then
$$
P>2699/5000>2697/5000>P'>1/2.
$$
Consequently $|P-1/2|>|P'-1/2|$. Reversing the four orientations preserves this strict failure and puts both means strictly between $\gamma_3=27/64$ and $1/2$.

## Proof

Use the standard simplex with coordinates $(\xi_1,\xi_2,\xi_3)$, $\xi_0=1-\xi_1-\xi_2-\xi_3$, and translate the point with barycentrics $\lambda=(191/846,518/2115,527/2538,2041/6345)$ to zero. Its coordinates are positive, less than $1/3$, and sum to one. Specify a cut by its raw signed values at the four vertices, taking the nonnegative side.

For values $(p,q,-r,-s)$ with positive $p,q,r,s$, the section vertices in cyclic order are
$$
A=(r/(p+r),0,p/(p+r),0),\quad B=(s/(p+s),0,0,p/(p+s)),
$$
$$
C=(0,s/(q+s),0,q/(q+s)),\quad D=(0,r/(q+r),q/(q+r),0).
$$
Writing $\alpha=ps/[(p+r)(p+s)(q+s)]$ and $\delta=qr/[(p+r)(q+s)(q+r)]$, the cross products for $ABC,ACD$ in the three ordinary coordinates are $-\alpha n,-\delta n$, where $n=(q-p,-r-p,-s-p)$. Thus the section centroid is $(A+C+(\alpha B+\delta D)/(\alpha+\delta))/3$, and section area divided by $|n|$ and by tetrahedron volume is $3(\alpha+\delta)$. The cap is the union, up to common faces, of the pyramids from vertex $0$ to the triangles $ABC$, $ACD$, and the triangle with vertices $1,C,D$. The first two have total normalized volume $p(\alpha+\delta)$ by the area times perpendicular height formula. The third has normalized volume $q^2/[(q+s)(q+r)]$ by the simplex determinant. For $(p,q,r,s)=(14,11,22,4)$ this gives centroid $\lambda$, cap fraction $626/1215$ and normalized coarea $47/810$.

For a vertex-$i$ cap with values $3$ at $i$ and $3-1/\lambda_j$ at $j\ne i$, the section intercepts on the three edges from $i$ are at fractions $3\lambda_j$ measured from $i$. Their mean is $\lambda$, and the cap fraction is $27\prod_{j\ne i}\lambda_j$. Its normalized coarea equals its cap fraction, because the vertex-to-plane height is $3/|n|$ for its own raw normal $n$. Complements keep section centroids and reverse the area vectors.

Use the two-versus-two cap followed by the vertex-$3$ cap and the complements of the vertex-$0$ and vertex-$1$ caps. The area vectors divided by body volume, computed by multiplying the raw normals by the normalized coareas, are
$$
\begin{aligned}
q_1&=(-47/270,-94/45,-47/45),\\
q_2&=(4743/44180,-11914/99405,136493/99405),\\
q_3&=(1075607/596430,1057238/497025,136493/99405),\\
q_4&=(-1075607/596430,46943/298215,-641359/1192860).
\end{aligned}
$$
For $\theta=(220438125401,35599660824,204746742725,185588180712)/646372709662$, multiplication gives $\sum_i\theta_i=1$, $\sum_i\theta_i q_i=0$ and $\det(q_1,q_2,q_3)=-1007454833/210241575$. The nullspace is one-dimensional and all four weights are positive. The four fractions are $(626/1215,26070163/84096630,352142512/630724725,299138843/504579780)$, giving $P=1570274946076/2908677193479$.

If the original vertices are $v_i$ and the mark is $y$, set the affine projective denominator at $v_i$ equal to $1/(4\lambda_i)$. It is positive on the simplex and equals one at $y$ by its barycentrics. The transformed vertices $4\lambda_i(v_i-y)$ sum to zero, so the image has centroid zero. This admissible map is the unique volume minimizer by the strict convexity and centroid stationarity of d90ba05577427854, applied to the translated simplex and its interior origin. Equivalently, the derivative of the volume integral vanishes exactly when the image centroid is zero. Raw values $t_i$ of any central cut transform to $4\lambda_i t_i$. For one positive value $a$ and three negative values $-b_j$, the intercept fractions $a/(a+b_j)$ give cap fraction $a^3/\prod_j(a+b_j)$; a reversed cut complements the fraction. Using this and the two-versus-two formula gives the transformed fractions
$$
(7600699714514571/14642033640793712,\
1308023834/3094640563,\ 668014703/1190605028,\ 2063099/3673043).
$$
Their mean with the same $\theta$ is $P'=3158781764622875088029132138218662810582905066533/5857054776644612955546677390460838594107476184416$. Cross-multiplication gives the stated strict inequalities, and also $P<37/64$, so the two complementary means exceed $27/64$. The simultaneous section-area minimum under projective transformations remains valid: the calculation compares the cap fractions at fixed weights.
