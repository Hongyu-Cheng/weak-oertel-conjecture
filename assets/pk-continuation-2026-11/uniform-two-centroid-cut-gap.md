# A strict two-step centroid-cut contraction in each fixed dimension

Status: proposed ordinary-geometric lemma and its mixed-depth consumer. The only external geometric inputs are classical centroid Grünbaum with its single-cap equality characterization, and elementary compactness of bounded convex bodies. The pending maximal-depth simplex-rigidity theorem is NOT needed. This does not assert a dimension-uniform quantitative gap or a complete OC proof.

## 1. The ordinary theorem

Fix d>=2 and put

    gamma_d=(d/(d+1))^d, q_d=1-gamma_d.

There exists a constant c_d with

    0<c_d<q_d^2                                           (1)

such that the following holds. Start with ANY d-dimensional convex body K. Choose ANY closed halfspace H_1 whose boundary passes through the ordinary centroid g(K), and put K_1=K intersect H_1. Choose ANY closed halfspace H_2 whose boundary passes through g(K_1), and put K_2=K_1 intersect H_2. Then

    |K_2| <= c_d |K|.                                    (2)

The same c_d works for every K and both arbitrary cut directions. The supremum defining the optimal c_d is attained after affine normalization. In d=1 the sharp two-step constant is q_1^2=1/4, so strictness in (1) correctly excludes that dimension.

## 2. Elementary geometric fact: a proper pyramid frustum is not a pyramid

Let F be a (d-1)-dimensional convex body in an affine hyperplane, let v lie outside that hyperplane, and let 0<a<1. The proper frustum

    L=conv(F,(1-a)F+a v)

is not a pyramid when d>=2.

The two displayed sets are exposed faces of L in distinct parallel hyperplanes, each of dimension d-1. Every extreme point of L belongs to one of these faces: a point at a strictly intermediate height is a nontrivial convex combination of points at the two endpoint heights. Each face has at least two extreme points and its extreme points affinely span its (d-1)-dimensional hyperplane, by the elementary finite-dimensional extreme-point description of a compact convex set.

If L were a pyramid with apex p, that apex would be an extreme point, and every other extreme point would belong to its base hyperplane. Suppose p is in the lower face (the other case is identical). The extreme points of the upper face force the alleged base hyperplane to be exactly the upper face's affine hyperplane. But there is another extreme point of the lower face, and it does not lie in that hyperplane. This is a contradiction.

## 3. Compactness and attainment, including both changing cuts

Let T=conv(0,e_1,...,e_d) and let

    K_class={K: K compact convex, T subset K subset [-1,1]^d}.

This is a compact class in Hausdorff distance and every member has positive d-volume. To see compactness directly, the support functions are uniformly bounded and uniformly Lipschitz on the unit sphere; a uniformly convergent subsequence determines the Hausdorff limit, and both inclusions persist. Equivalently this is the standard bounded convex-body selection theorem.

Every d-body can be affinely normalized into K_class. Choose a maximum-volume inscribed simplex (existence follows by compactness of its vertex tuples) and send it to T. Replacing any one of its vertices by a point x of the normalized body shows that the absolute value of every barycentric coordinate of x is at most one. In particular each Euclidean coordinate lies in [-1,1]. Affine transformations preserve centroid cuts and every retained-volume ratio, so this normalization loses no case. It is used only for an ordinary continuous body; no mixed lattice is transformed.

For a unit vector u write

    R(K,u)=K intersect {x:u dot (x-g(K))<=0}.

Classical centroid Grünbaum, applied to both through-centroid closed sides and using zero hyperplane volume, gives

    gamma_d |K| <= |R(K,u)| <= q_d |K|.                   (3)

The centroid map is continuous under Hausdorff convergence to a full-dimensional convex body. Indeed indicators converge almost everywhere off the null boundary, so volumes and first moments converge by dominated convergence.

The map (K,u)->R(K,u) is Hausdorff continuous on K_class times the unit sphere. For the upper inclusion, take convergent points in the intersections. For the lower inclusion, fix x in the limiting intersection, choose an interior point p of K on the strict retained side (the centroid is interior, so such p exists), and move x slightly toward p. The resulting point is interior to K and strictly on the retained side. It belongs to all sufficiently close convex bodies and the corresponding nearby halfspaces. Letting the displacement tend to zero proves the lower inclusion. A finite covering, or compactness of the limiting intersection, makes this uniform over its points.

By (3), first remainders have volume at least gamma_d |T|>0. Thus their Hausdorff limits remain full-dimensional, their centroids are continuous, and the same argument applies to the second intersection. It follows that

    F(K,u_1,u_2)=|R(R(K,u_1),u_2)|/|K|

is continuous on the compact space K_class x S^{d-1} x S^{d-1}. It has an attained maximum c_d. Equation (3) gives gamma_d^2<=c_d<=q_d^2. In particular c_d is positive.

## 4. Equality cannot persist for two consecutive cuts

Suppose c_d=q_d^2 at an attaining triple. Put K_1=R(K,u_1), K_2=R(K_1,u_2). Each of the factors

    |K_1|/|K| and |K_2|/|K_1|

is at most q_d by (3), so both must equal q_d.

The first removed cap consequently has exactly gamma_d|K| volume and its boundary passes through g(K). The classical equality characterization of centroid Grünbaum for d>=2 says that K is a pyramid conv(v,F), the removed cap is on the apex side, and its parallel cutting plane has affine pyramid height 1/(d+1), where the base has height zero and the apex height one. Hence K_1 is precisely the proper frustum

    conv(F, [d/(d+1)]F+[1/(d+1)]v).

By Section 2 this is not a pyramid. But the second removed cap also has exactly gamma_d|K_1| volume at the centroid of K_1, so the same classical equality theorem says that K_1 IS a pyramid. This contradiction proves c_d<q_d^2 and completes the ordinary theorem.

This strict gap is uniform over all bodies because the maximum was shown to exist before equality was excluded. No unproved assertion that all nearly extremal bodies are simplices is used: a one-cut equality body may be a pyramid over an arbitrary convex base.

## 5. Iteration in pairs

Let K_0,...,K_k be any sequence where K_{s+1} is obtained by retaining either closed halfspace through the true centroid of K_s. Applying (2) to consecutive disjoint pairs and (3) to a possible final cut gives

    |K_k| <= b_{d,k}|K_0|,
    b_{d,k}=c_d^floor(k/2) q_d^(k mod 2).                 (4)

All intermediate bodies have positive volume by (3). Thus b_{d,k}<q_d^k for k>=2. This is a strict improvement of the repeated one-step contraction in every fixed d>=2, but no positive lower bound on q_d^2-c_d uniform in d has been established.

## 6. Consequence for the nested root-retention functional

Use exactly D,w_j,L_E,Phi_j(t) from pending candidate `6fa5d5dfe3ee4559` (the companion `nested-root-retention-depth-functional.md`). Let C be any positive mixed-volume convex body with arbitrary n>=0 and d>=2. Then

    max_{x in C_j} h_S((j,x))
           >= sup_{k>=1} Phi_j(b_{d,k})/k.               (5)

In particular the two-step term is Phi_j(c_d)/2, replacing Phi_j(q_d^2)/2. This conclusion still concerns a single actual point in the original target fiber and every closed ambient halfspace.

To prove it, repeat the finite cut-search proof of that note. If every original target point had depth less than Phi_j(b_{d,k})/k, choose delta strictly between these values. At each stage use the true centroid of the CURRENT target fiber, select a containing cap of original mixed measure below delta, and keep its opposite side. The vertical-hitting bound rules out a zero continuous normal. Thus the target sections undergo precisely the ordinary centroid cuts of (4). Their final volume is at most b_{d,k}w_j. The proved remainder-loss lemma gives removed original mixed mass at least Phi_j(b_{d,k}), whereas the k selected original caps remove less than k delta. Contradiction. The original fiberwise depth maximum is attained, as proved with all closed-boundary mass in the predecessor note, so (5) gives a deterministic actual point.

No independence of the successive cuts is required: (2) holds for all first and second directions. No normalization is applied to the mixed body in this argument; the ordinary theorem is applied separately to its current continuous target fiber.

## 7. An explicit qualitative improvement on a three-fiber family

For three positive fibers at integer bases -1,0,1 with weights (s,1,s), where 0<s<=1, the root supports at the central base are only {0} and {-1,1}, the latter with cost log(1/s). Hence

    Phi_0(t)=1-t+(s-t)_+.

Write gamma=gamma_d, q=q_d, eta_d=q^2-c_d>0. For s>=c_d, the improved two-cut bound is

    Phi_0(c_d)/2=(1+s-2c_d)/2.

It reaches the sharp OC target gamma(1+2s)/2 whenever

    s >= q - 2eta_d/(1-2gamma).                         (6)

This follows by subtracting the two expressions: twice their difference is (1-2gamma)(s-q)+2eta_d. Since d>=2, the denominator in (6) is positive. In particular there is a nonempty interval of parameters immediately below q where this improved certificate succeeds and the old q^k-based two-step term does not. This statement uses only actual fiber weights and convexity; endpoint shapes are arbitrary compatible bodies. It is a scoped consequence and does not cover every parameter or arbitrary supports.

## 8. Exact simplex calibration: the strict gap vanishes with dimension

The primary classical equality statement used above is also stated in Marín Sola--Yepes Nicolás, *On Grünbaum type inequalities*, page 1, https://webs.um.es/jesus.yepes/publicaciones_files/paper_grunbaum.pdf . This is background for the ordinary theorem, not an external mixed-integer result.

In a d-simplex use barycentric coordinates lambda_1,...,lambda_N, N=d+1, and normalize total volume to one. Put b=1/N, gamma=gamma_d, q=1-gamma. First retain lambda_1<=b. Its volume is q. The removed cap lambda_1>=b is the homothetic simplex based at the first vertex, of volume gamma. Its centroid has lambda_2=(1-b)/N=d/N^2. Therefore the retained centroid has

    c=E[lambda_2 | lambda_1<=b]
      =[1/N-gamma*d/N^2]/q
       =1/N+gamma/(N^2 q).

Retain lambda_2<=c at the second centroid. Inclusion-exclusion and the exact simplex cap formula give final volume

    p_d=q-(1-c)^d+(1-b-c)_+^d.                           (7)

These are legitimate successive centroid cuts, so p_d<=c_d. Since d c->1 and d(b+c)->2,

    (1-c)^d -> exp(-1),
    (1-b-c)_+^d -> exp(-2),
    p_d -> (1-exp(-1))^2.

Also q_d^2 has that same limit. Thus

    0<q_d^2-c_d<=q_d^2-p_d ->0.                          (8)

In particular no dimension-independent positive gap can replace q_d^2-c_d in the ordinary theorem.

More generally, let sigma_{d,k} be the optimal universal retained-volume fraction after k successive centroid cuts. The same compactness proof, iterated a finite number of times, proves attainment and 0<sigma_{d,k}<=q_d^k. For every FIXED k,

    lim_{d->infinity} sigma_{d,k}=(1-exp(-1))^k.           (9)

Here is a direct lower construction. In a simplex cut successively the first k distinct barycentric coordinates at their current centroid values c_1,...,c_k. Before cut j the uncut coordinates are exchangeable, and the sum of all barycentric coordinates is one, so

    c_j=[1-sum_{i<j} E(lambda_i | previous cuts)]/(N-j+1).

Consequently 0<c_j<=1/(N-j+1), while the cut conditions lambda_i<=c_i give

    c_j>=[1-sum_{i<j}c_i]/(N-j+1).

For fixed j these inequalities imply N c_j->1. The final retained volume is exactly

    sum_{I subset {1,...,k}} (-1)^|I|
                       (1-sum_{i in I}c_i)_+^d.

Every term tends to exp(-|I|), so the finite sum tends to (1-exp(-1))^k. This gives the lower limit in (9), while q_d^k gives the upper limit. Thus a fixed finite number of universal contraction improvements cannot have a uniform positive advantage as d grows. Equation (9) is a proved limitation, not a volume/depth interchange.
