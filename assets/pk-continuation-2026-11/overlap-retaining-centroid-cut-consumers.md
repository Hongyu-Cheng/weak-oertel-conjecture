# Shape-dependent centroid-cut consumers retaining original-cap overlaps

Status: proved scoped improvement of the nested-root-retention consumer. This note makes no claim that the new minimization always reaches OC. Its new datum is an exact original-target cap arrangement, not just the remaining target volume. All source geometry still enters through the already proved Phi remainder-loss lemma.

## 1. Notation and the original-cap multiplicity identity

Use the positive-volume mixed body C, target j, original target K=C_j, target volume w>0 and root-retention functional Phi_j from `nested-root-retention-depth-functional.md`. Write mu for the unnormalized original mixed measure and h for original mixed halfspace depth. Let k>=1 be fixed.

For a sequence of k successive ordinary centroid cuts in K, let G_i be the REMOVED closed halfspace through the centroid of the current target remainder, and let K_i be the retained opposite closed intersection. Define

    A_i=K intersect G_i,
    a_i=|A_i|,
    t=|K_k|/w,
    Omega=sum_i a_i - |union_i A_i|
         =sum_i a_i-w(1-t)>=0.                         (1)

All measures here are d-dimensional ordinary volume. Since each hyperplane is null for that measure, whether the removed cap contains its boundary makes no change to these identities. Notice that A_i uses ORIGINAL K, not just the current remainder K_{i-1}.

For any corresponding ambient removed halfspaces H_i, whose traces at j are G_i, the elementary multiplicity identity gives

    sum_i mu(H_i)-mu(union_i H_i)
      =integral [sum_i 1_(H_i)-1_(union_i H_i)] dmu
      >= Omega.                                        (2)

The integrand is nonnegative everywhere, and its integral over the original target fiber is exactly Omega. This counts every repeated capture once for each excess multiplicity; it does not require disjoint source supports or independent cuts.

The remaining actual convex body C intersect intersection_i H_i^c has target volume tw, where H_i^c is interpreted as the opposite closed halfspace. Its boundary discrepancies on non-target fibers need care: the removed OPEN union is contained in the closed union, while on the positive-volume target the discrepancies are null. The remainder-loss lemma applies to the closed retained intersection and gives

    mu(union_i H_i) >= Phi_j(t).                        (3)

Indeed C outside that closed intersection is the OPEN removed union, already of measure at least Phi_j(t), so (3) follows even if vertical source hyperplanes carry mass.

Combining (2)--(3),

    sum_i mu(H_i) >= Phi_j(t)+Omega.                    (4)

This is the precise correction to the earlier union-bound consumer.

## 2. Attained finite-dimensional sequence minima

All normalized continuous cut directions lie in the compact space (S^(d-1))^k. The maps from these directions to each current target remainder, its centroid, and all intersections of original target caps are continuous. The first two facts follow inductively from positive retained volume, centroid continuity, and the closed intersection continuity proved in `uniform-two-centroid-cut-gap.md`. The last fact follows by dominated convergence of cap indicators: each limiting target boundary hyperplane has zero ordinary d-volume. Therefore t, every a_i, and Omega are continuous functions of the direction tuple. Phi_j is continuous by its finite assignment formula. In particular each minimum below is attained.

Write m=m_j(infinity), the minimum original mass of a source set meeting every root support at j. The predecessor note proves

    w<=m,  0<=Phi_j(t)<=(1-t)m<=m.                     (5)

Define

    B_(j,k)=min_sequences max{
                max_i a_i,
                [Phi_j(t)+Omega]/k
                             }.                       (6)

This value is at most m. Indeed a_i<=w<=m and Omega<=sum_i a_i-max_i a_i<=(k-1)w. Thus the second entry is at most [m+(k-1)w]/k<=m for every sequence.

Then

    max_(y in K) h((j,y)) >= B_(j,k).                   (7)

Proof: suppose the attained maximum of h on the compact target fiber were below B_(j,k), and choose delta strictly between them. At each successive current target centroid choose a containing original ambient cap of measure below delta, move its boundary to the queried point, and retain its opposite side. A vertical containing cap has mass at least m by the root-hitting argument, whereas delta<B_(j,k)<=m. Hence every selected cap has nonzero continuous normal and gives a genuine ordinary target centroid cut. All successive target remainders have positive volume by ordinary centroid Gruenbaum.

After k cuts each a_i<=mu(H_i)<delta, and (4) gives [Phi_j(t)+Omega]/k<delta. This contradicts the sequence minimum (6). The depth maximum is attained by upper semicontinuity with closed-boundary mass, as in the predecessor note. This proves (7).

For k=1, B_(j,1)=min_direction Phi_j(t), since Phi_j(t)>=w(1-t)=a_1. Thus this special case is the original single-centroid consumer evaluated using the target's actual directional cap volumes.

## 3. Every subset of cuts supplies an exact original-target constraint

For a nonempty subset I of {1,...,k}, put

    t_I = |K intersect intersection_(i in I) G_i^c|/w,
    a(I)=|union_(i in I) A_i|=w(1-t_I),
    r_I=Phi_j(t_I)-a(I)>=0.                            (8)

The nonnegativity is the mandatory own-fiber term in Phi. Applying the remainder-loss lemma only to this subset of ambient cuts proves

    mu_out(union_(i in I) H_i)>=r_I,                   (9)

where mu_out omits the original target fiber. This uses an actual convex intersection for each I and remains valid although the cuts in I need not be successive centroid cuts when considered alone.

Let x_J>=0, for every nonempty J subset {1,...,k}, stand for outside mass captured by exactly the caps indexed by J. Actual outside cap atoms form such a vector and satisfy

    sum_(J:J intersect I nonempty) x_J >= r_I
                    for every nonempty I.              (10)

Define the finite linear-program value

    L(sequence)=min_{x_J>=0} max_i
                  [a_i+sum_(J:i in J)x_J]
        subject to (10).                              (11)

This is feasible, for instance by assigning enough mass to J={1,...,k}. The infimum is attained: restrict to a feasible finite objective sublevel; then each x_J is bounded because every nonempty J contains some i whose cap cost bounds it. The feasible sublevel is closed and bounded.

For the actual cut sequence,

    max_i mu(H_i)>=L(sequence).                         (12)

The bound L(sequence)<=m holds uniformly: assign x_[k]=m-w and all other atoms zero. Indeed (5) gives

    r_I=Phi_j(t_I)-w(1-t_I)<=(1-t_I)(m-w)<=m-w,

so this assignment is feasible and each resulting cap cost is at most w+(m-w)=m. Consequently the same bad-cap construction, with its vertical exclusion fully justified, proves

    max_(y in K) h((j,y))
       >= inf_sequences L(sequence).                  (13)

An attainment assertion for the outer sequence infimum is unnecessary for this implication; every constructed sequence satisfies L>=that infimum. All of its LP coefficients t_I,a_i are ordinary target geometry.

The elementary consumer (6) follows as a relaxation: singleton cap costs imply L>=max_i a_i; summing costs and using (10) for the full set gives

    kL>=sum_i a_i+r_[k]=Phi_j(t)+Omega.

Thus (13) retains at least all the information in (7), and can additionally retain source losses forced by proper subsets.

## 4. Exact two-cut simplification

For k=2, write a=a_1,b=a_2 and r_1,r_2,r_12 as in (8). The LP has variables x_{1},x_{2},x_{12}. Its exact value is

    L=max{a+r_1, b+r_2, (a+b+r_12)/2}.                 (14)

Necessity is immediate from the two singleton constraints and the union constraint. For sufficiency set z equal to the right side and choose outside cap marginal costs u=z-a>=r_1, v=z-b>=r_2. Then u,v>=0 and u+v>=r_12. Set x_12=0,x_1=u,x_2=v; this satisfies all constraints and gives both total cap costs exactly z. Thus (14) is exact without assuming outside disjointness in the actual body: the LP may use a disjoint hypothetical allocation as a lower relaxation.

For the equal-endpoint three-fiber profile (s,1,s) with target volume one, r_I=(s-t_I)_+. In particular the overlap-sensitive two-cut consumer uses

    max{ Phi_0(1-a), Phi_0(1-b),
                   [a+b+(s-t_12)_+]/2 }.              (15)

Unlike a universal retained-volume bound, this expression keeps both original target cap masses and their overlap. No assertion is made here that its minimum over all centroid-cut sequences reaches the sharp target gamma_d(1+2s)/2. Establishing or refuting such a bound is a concrete remaining ordinary-geometric question.

## 5. Scope and overlap check

The earlier retained-volume argument paid only Phi_j(t)/k and discarded the nonnegative multiplicity excess Omega. The current correction and all-subset LP follow from exact original-cap identities. Targeted searches of the local ledger for centroid-cut/overlap combinations found no prior result with this consumer; the earlier source `7fa5a28fe1ac6893` explicitly used a union bound. This is a local overlap check, not a claim of priority in the mathematical literature.

The result has not proved OC. In particular it must not be advertised as a closed bridge merely because (11) is a finite program. Its role is to retain information that the exact d=50 obstruction shows is absent from every universal-volume-only version of the argument.

## 6. Certified gain on the d=50 simplex obstruction for all facet-normal cut pairs

Consider the actual three-fiber body from `optimal-universal-centroid-contraction-phi-obstruction.md`, with d=50, w=1, endpoint masses s=3/5 and central simplex T. Let lambda_1,...,lambda_51 be its barycentric coordinates. Restrict, only for this calibration, each target cut normal to a facet-normal direction: the removed halfspace has the form lambda_i>=c or lambda_i<=c, where c is its value at the current remainder centroid.

For EVERY such two-cut sequence the LP (14) is strictly above the exact OC target

    T_OC=(11/10)gamma, gamma=(50/51)^50.                (16)

This is a rigorous positive test of the shape-dependent invariant on the body where every volume-only universal contraction consumer fails. It does not prove (16) for arbitrary oblique cut normals, so it does not by itself imply the full mixed-depth conclusion.

Use the exact estimates from the obstruction certificate:

    102/275<gamma<2/5, q=1-gamma>3/5,
    q<173/275, q^2<2/5, T_OC<11/25.                   (17)

If the first removed cap is lambda_i<=1/51, its original target mass is q>3/5>T_OC; the LP already exceeds the target. By symmetry the remaining case is first cap lambda_1>=1/51, of original target mass gamma. The first retained body is lambda_1<=1/51.

Its centroid has coordinate values

    c = 1/51+gamma/(51^2 q)       in coordinates i>=2,
    c'=1/51-50gamma/(51^2 q)     in coordinate 1.       (18)

These follow by subtracting the removed simplex's first moments from the original centroid. We now exhaust all possible second facet-normal cuts.

**Different-coordinate vertex side.** If the second removed side is lambda_i>=c for i>=2, its original target mass is b=(1-c)^50. The bound gamma<2/5 implies c<1/50: equivalently 101gamma<51, which is weaker than gamma<2/5. Therefore

    b>(49/50)^50>9/25.                                 (19)

The last strict rational comparison has the exact positive numerator

    25*49^50-9*50^50
     =925854967607678873114714124966357771430079972615635023347383284792286490923201500025.

The remaining target mass r is at most q^2<2/5, by applying centroid Gruenbaum twice. Therefore the full-set constraint in (14) gives

    L >= [gamma+b+(s-r)]/2
       > [102/275+9/25+1/5]/2
        =128/275 >11/25>T_OC.                          (20)

**Different-coordinate opposite side.** If the removed side is lambda_i<=c, its original mass is 1-b. Since c>1/51, b<gamma<2/5 and hence 1-b>3/5>T_OC.

**Same-coordinate vertex side.** If the removed side is lambda_1>=c', the original cap mass is (1-c')^50. The lower bound on gamma in (17) implies gamma>51/151, equivalently c'<1/102. Bernoulli's inequality then gives

    (1-c')^50>(101/102)^50>=1-50/102=26/51>1/2>T_OC.

Again the LP exceeds the target by its own-cap constraint alone.

**Same-coordinate opposite side.** The remaining case is the second removed cap lambda_1<=c'. These two removed original caps are disjoint up to null boundaries. The remainder has volume

    r=(1-c')^50-gamma.

Moreover c'>1/153: rearranging (18), this is equivalent to gamma<17/42, which follows from gamma<2/5. We have the elementary exact bound

    (152/153)^50<3/4.

Indeed, for 0<x<1 the binomial series gives (1-x)^(-50)>1+50x+1275x^2. At x=1/153 this exceeds 4/3, because

    3*(153^2+50*153+1275)-4*153^2=3366>0.

Thus r<3/4-gamma<3/5=s. Since a+b=1-r in this disjoint-cap case, the full-set term in (14) is

    [a+b+s-r]/2 =4/5-r
       >gamma+1/20 > (11/10)gamma=T_OC,                (21)

where the final inequality uses gamma<1/2.

These four cases exhaust all second facet normals and complete the calibration.

For every k>=3, an arbitrary facet-normal extension of the first two cuts retains this conclusion. Any feasible all-subset LP vector for k caps, when its cap atoms are projected to the first two indices and empty projected atoms discarded, gives a feasible vector for the first-two-cut LP with the same first two cap costs. Therefore L_k>=L_2>T_OC. No assumption on later overlap or centroid locations enters this monotonicity argument.

The remaining question for this concrete body is now sharply localized: can an oblique through-centroid cut pair bring the shape-dependent infimum below T_OC? The facet-normal test proves that the directions responsible for the asymptotically extremal universal retained-volume constants do not do so. It supplies no reduction of arbitrary directions to facet directions; such a reduction would need proof.

## 7. A certified non-facet first-cut family on the same simplex

The positive calibration also extends to a genuine one-parameter family of oblique first cuts. Take

    G_1={lambda_1-t lambda_2 >= (1-t)/51},  0<=t<=1,

and let the second cut have normal lambda_2, with either orientation through the centroid of the first remainder. For every t in this interval, the two-cut LP exceeds T_OC.

The first cap is a simplex at vertex 1: its edge contraction is (50+t)/51 on edges to vertices other than 2, and is (50+t)/[51(1+t)] on the edge to vertex 2. Consequently its original mass and its centroid coordinate lambda_2 are exactly

    a(t)=[(50+t)/51]^50/(1+t),
    m_2(t)=(50+t)/[51^2(1+t)].                         (22)

Its removed boundary passes through the original centroid, as required. If a(t)>=T_OC the assertion follows already from the first own-cap cost. Otherwise use the exact stronger bound gamma<41/110, so T_OC<41/100. The function a(t) is increasing: its logarithmic derivative is 49t/[(50+t)(1+t)]>=0. The exact comparison

    a(3/5)=(5/8)(253/255)^50>41/100

therefore implies t<3/5. In this regime m_2(t)>125/10404 and a(t)<41/100. The remaining centroid value c_2 obeys

    c_2=[1/51-a(t)m_2(t)]/[1-a(t)]
       <[1/51-(41/100)(125/10404)]/(59/100)
        =15275/613836 <1/40.                          (23)

The first strict inequality follows because, for any fixed m<1/51, the displayed quotient is increasing in a and decreasing in m. If the second removed side is lambda_2>=c_2, its original mass b satisfies

    b>(39/40)^50>7/25.

Again the remaining target volume r<=q^2<2/5. Thus

    L >=[a(t)+b+s-r]/2
       >[102/275+7/25+1/5]/2
        =117/275>41/100>T_OC.                         (24)

Here a(t)>=gamma also follows directly from monotonicity and a(0)=gamma (or from centroid Gruenbaum). For the other second orientation, m_2(t)<1/51 implies c_2>1/51, so the removed mass is 1-(1-c_2)^50>1-gamma>3/5>T_OC.

The three additional rational comparisons have exact positive cross-multiplication numerators:

    41*51^50-110*50^50
     =3154003209873767140947911624980894046483464634207831465906416405105514138539950665041;

    125*253^50-82*255^50
     =4924566937256154132724837036519312063411436065899045406918409576091035299445485227686552079009507142941993391602339249875;

    25*39^50-7*40^50
     =6300547814447154622721970523321654084850980784067515344954149345471962288950025.

Also 1/40-15275/613836=709/6138360>0. These establish every numerical comparison in this section exactly. In particular t=1/2 gives a non-facet first cap with mass (2/3)(101/102)^50 below T_OC; its gain requires the overlap-sensitive second-cut constraint, not just exclusion by the first cap's mass.

No reduction of arbitrary first or second normals to this one-parameter family is claimed. This test shows that the improved consumer continues to recover the target for a family that the facet-normal calculation alone does not cover.
