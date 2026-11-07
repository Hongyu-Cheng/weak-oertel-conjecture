# A covering-pair certificate for distinct-apex planar (1,1,2) fans

Research theorem, 6 November 2026. The ordinary planar sector inequality in accepted fact2a8c2bc6d7992c5e is used only to prove the ordinary top-two-cap lemma in Section1. Every source-capacity assertion below is proved directly. No center or source deformation is asserted.

## 1. Statement and an ordinary two-cap bound

Let B be a triangle of area vV, where V>0 and0<v<=1. Let three affine functions vanish at an interior point, have spanning gradients and a strictly positive linear dependence. Suppose exactly two rows have one strictly positive original vertex value and two strictly negative values, with DIFFERENT positive original vertices. The third row has two strictly positive and one strictly negative original vertex values. Let source triangles P_m subset B have areas at least V/4, with nonnegative weights e_m summing to E=1-v. A row is hit if its support maximum on the source is strictly positive; maximum zero is a miss.

Then some pair of rows jointly hits every qualifying source and has own-cap fraction sum at least8/9. Consequently the maximum normalized score, own-cap area/V plus strict-hit weights, is at least

    4/9+E/18.                                            (1)

We use this elementary consequence of the accepted ordinary planar sector inequality: for ANY full positive three-fan in a planar convex body, some two own-cap fractions sum to at least8/9. For completeness, normalize the body area to1. Let A_i be the singleton-hit sector areas, and D_i the opposite double-hit sector areas. Then

    sum(A_i+D_i)=1,
    p_j+p_k=1+D_i-A_i,
    sum D_i/A_i>=3/2.                                    (2)

The last inequality is the ordinary auxiliary assertion of accepted2a8c2bc6d7992c5e; all sectors are positive because the point is interior. If all three pair sums were below8/9, then A_i>D_i+1/9. Writing D=sum D_i gives D<1/3, while concavity of x/(x+1/9) gives

    sum D_i/A_i <sum D_i/(D_i+1/9)
                 <=3D/(D+1/3)<3/2,

contradicting(2). Thus the asserted ordinary pair bound holds. Only this ordinary bound, not any mixed-integer conclusion of that predecessor, is used here.

## 2. Exact concurrent-line coordinates

Relabel original vertices as A,B,C, with the first row positive only at A and the second positive only at B. Positive dependence implies every original vertex has some positive row value. Hence the third row is positive at C and one of A,B; exchanging the first two rows if necessary makes it negative at A and positive at B,C.

Use affine coordinates A=(0,0), B=(1,0), C=(0,1). Write the center as (b,c), with barycentric coordinates(a,b,c), all positive and a+b+c=1. Put

    q=b/(1-c)=b/(a+b).

Every vertex-side cap at A through the center is the triangle K(t) with edge intercepts

    t on AB,       z(t)=c t/(t-b) on AC,
    q<t<1,
    p(t)=|K(t)|/|B|=c t^2/(t-b).                        (3)

The first row is K(t_1), and the third row is the opposite orientation of K(t_3). The second row is a vertex-side cap at B; write t_2 for its zero on AB measured from A. Strict signs give0<t_2<q. Its area fraction is

    p_2=c(1-t_2)^2/(b+c-t_2).                           (4)

The positive dependence forces t_1<t_3. Indeed at the first-row zero on AB the second row is strictly positive because t_1>q>t_2, so the third row must be strictly negative. Its complementary A-cap function is consequently positive there, which says t_1<t_3. Thus

    0<t_2<q<t_1<t_3<1.                                 (5)

Set p_1=p(t_1), p_0=p(t_3), and z_3=z(t_3). The three OWN cap fractions are

    p_1,       p_2,       1-p_0.                        (6)

The closed region missed by rows1,3 is the triangle with apex at the center and base on AB between t_1,t_3. Its area fraction is exactly

    r_2=c(t_3-t_1).                                    (7)

The region missed by rows2,3 is the quadrilateral with vertices

    (0,0), (t_2,0), (b,c), (0,z_3).                    (8)

Its four vertex-triangle area ratios are t_2 z_3, t_2 c, b z_3, and t_2 c+b z_3-t_2 z_3. A maximum inscribed triangle may be chosen at polygon vertices by successive maximization of the absolute affine determinant. If the fourth quantity uniquely exceeds both t_2 c and b z_3, then t_2<b and z_3<c, and it is strictly below bc<1/4. The other cases leave one of the first three as a maximizer. Since z_3>c, the quadrilateral contains a triangle of relative area at least1/4 if and only if

    q_1:=z_3 max(t_2,b)>=1/4.                           (9)

Here q_1 is a threshold test; it need not equal the full capacity below1/4. A positive-area source cannot miss all three rows. Thus whenever r_2<1/4 the pair1,3 covers all qualifying sources, and whenever q_1<1/4 the pair2,3 does so. The larger actual source threshold1/(4v) causes no issue.

We also use the following elementary cap-lobe observation. If two triangles with the same original apex have crossing edge intercepts (u,V),(U,w), with u<U and w<V, put r=u/U,s=w/V. The ratio of the first triangle's area to the scale UV is r, and of the second is s. If the first has no larger area, r<=s, and its outside lobe has area ratio

    UV r(1-s)^2/(1-rs)
       <=r(1-r)/(1+r)<=3-2sqrt(2)<1/4.                 (10)

The first inequality follows because (1-s)^2/(1-rs) decreases in s; the scalar maximum occurs at r=sqrt(2)-1. Swapping axes handles the other crossing order. Therefore if p_0<=p_1, the pair1,3 has own sum1+p_1-p_0>=1 and its missed region is the outside lobe of the smaller A-cap, of area below1/4. This proves(1) in this branch.

For the rest assume

    p_0>p_1.                                          (11)

Since p'(t)=c t(t-2b)/(t-b)^2, this forces t_3>2b and hence z_3<2c. Strict convexity p''(t)=2cb^2/(t-b)^3>0 also gives

    p_0<p(1)=c/(1-b)=c/(a+c),                         (12)

because t_1<t_3<1 and p(t_3)>p(t_1).

## 3. The unmatched vertex C has a maximal coordinate

Suppose c>=a,b. The first two rows are vertex-side caps at A and B. The ordinary cap optimization at these two vertices gives

    p_1+p_2>=8/9.                                     (13)

Here is the precise calculation. For a row positive at A, normalize its positive height to1, with negative heights-u at C and-w at B. The center equation is u c+w b=a, equivalently (1+u)c+(1+w)b=1. If c<=1/2, AM-GM gives its cap fraction at least4bc; the B row similarly contributes at least4ac, so the sum is at least4c(1-c)>=8/9. If c>=1/2, the product X Y under cX+bY=1 and X,Y>1 is at most(1-c)/b, because X(1-cX) decreases for X>=1. Thus the A cap is at least b/(1-c), and similarly the B cap is at least a/(1-c), giving pair sum at least1.

Their common closed negative region is a quadrilateral based at C, with the center and their zero crossings on CA,CB as its other vertices. There is no common negative point on AB by t_2<t_1. The two intercept fractions from C are respectively less than a/(a+c)<=1/2 and b/(b+c)<=1/2, by their strict center equations. Also a,b<1/2. The four vertex-triangle ratios are AB',Ab,B'a,Ab+B'a-AB', using these two intercepts A,B'. The first three are below1/4; the fourth bilinear expression is bounded by its values at corners of[0,1/2]^2, namely0,a/2,b/2,1/4-c/2, all below1/4. Hence no qualifying source misses pair1,2. Together with(13), this proves the claimed pair certificate.

## 4. The double-hit vertex B has a maximal coordinate

Suppose b>=a,c. If b>=1/2, p is decreasing on its whole feasible interval t<1<=2b, contradicting(11). Thus b lies in[1/3,1/2). Also c<1/2. AM-GM gives p_1>=4bc. Equation(12) yields

    p_0-p_1<c/(1-b)-4bc
       =c(1-2b)^2/(1-b)<1/9,                         (14)

because c<=b<1/2, so c/(1-b)<1, while(1-2b)^2<=1/9. The own sum of pair1,3 is therefore greater than8/9. Its missed triangle satisfies

    r_2<c(1-q)=ac/(a+b)<=c/2<1/4,                     (15)

using a<=b. Hence pair1,3 covers all qualifying sources and proves the theorem in this case.

## 5. The matched vertex A has a maximal coordinate

Assume a>=b,c. Then b,c<1/2 and a>=1/3. Any vertex-side cap at A has fraction strictly less than max(b,c)/(a+max(b,c))<=1/2: after normalizing its positive height, the center equation gives the sum of its two negative heights at least a/max(b,c), and their product is positive. Thus p_1<1/2. Equation(12) gives p_0<c/(a+c)<=1/2, so the third own cap1-p_0 is strictly greater than1/2. In particular the largest two OWN caps always include row3.

### 5.1 The two troublesome singleton regions cannot both qualify

From(9), max(t_2,b)<q, so q_1<q z_3. Also r_2<c(t_3-q). Therefore

    q_1 r_2
      <q c^2 t_3(t_3-q)/(t_3-b)
      <ab c^2/[(1-c)^2(1-b)].                         (16)

For the second inequality, t(t-q)/(t-b) is strictly increasing for t>q: its derivative numerator is (t-b)^2+b(q-b)>0. Its endpoint value at t=1 gives exactly the right side.

Put u=b/a and w=c/a; both lie in(0,1]. The last expression equals

    u w^2/[(1+u+w)(1+u)^2(1+w)]
      <=u/[2(2+u)(1+u)^2]<1/16.                       (17)

The expression increases in w, as follows from2/w-1/(1+u+w)-1/(1+w)>0. At w=1, use2+u>2 and(1+u)^2>=4u to obtain the final strict inequality. Thus q_1 and r_2 cannot both be at least1/4.

### 5.2 If singleton2 qualifies, pair2,3 has own sum greater than one

Suppose r_2>=1/4. Equation(17) gives q_1<1/4, so pair2,3 covers every source. It remains to compare p_2 to p_0.

If a>=1/2, the same constrained-product calculation as in Section3 gives p_2>=c/(1-a)=c/(b+c)>=c/(a+c)>p_0. If a<=1/2, then a,c<=1/2 and AM-GM gives p_2>=4ac. From r_2<c(1-q)=ac/(a+b) and r_2>=1/4 one gets4ac>1-c. Since a>=c and c<1/2,

    4a(a+c)>=8ac>2(1-c)>1.

Consequently p_2>=4ac>c/(a+c)>p_0. In both cases p_2+1-p_0>1, proving the pair certificate.

### 5.3 If singleton1 qualifies, the matched pair has own sum greater than seventeen eighteenths

Suppose q_1>=1/4. Equation(17) gives r_2<1/4, so pair1,3 covers all sources. We prove the stronger own-cap estimate p_0-p_1<1/18.

Since z_3<2c and bc<=1/9 (as a>=1/3), b z_3<2/9<1/4. Thus(9) forces t_2 z_3>=1/4. Because t_2<q, this gives

    z_3>L:=(1-c)/(4b),     while z_3<2c.              (18)

We have L>c: indeed c<1/2 and bc<=1/9 give c+4bc<17/18<1. Solving(3) for t_3 gives p_0=b z_3^2/(z_3-c). AM-GM gives p_1>=4bc. The function (2c-z)^2/(z-c) strictly decreases on c<z<2c. Hence

    p_0-p_1
      <=b(z_3-2c)^2/(z_3-c)
      < F(b,c):=[c(1+8b)-1]^2/[4(1-c(1+4b))].        (19)

The numerator before squaring is positive by L<2c. On this domain F increases as c increases: its positive numerator increases and its positive denominator decreases. Maximality of a gives

    c<=min((1-b)/2,1-2b).                             (20)

If b<=1/3, substitute c=(1-b)/2 into F to obtain

    F <=(-1+7b-8b^2)^2/[8(1-3b+4b^2)]<=1/18.         (21)

The numerator's unsquared quantity is positive (because the actual positive numerator is bounded by it), increases on0<b<=1/3, and is at most4/9. The denominator's parenthesis decreases on that interval and is at least4/9. These two estimates give the last inequality exactly.

If b>=1/3, substitute c=1-2b. Positivity of the numerator implies b<3/8, and

    F <= b(3-8b)^2/[2(4b-1)]<=1/18.                  (22)

Indeed b/(4b-1)<=1 for b>=1/3, while0<3-8b<=1/3. Equations(19)-(22) prove p_0-p_1<1/18. Thus pair1,3 has own sum greater than17/18 and covers every source.

### 5.4 Neither singleton qualifies

If q_1<1/4 and r_2<1/4, both pairs1,3 and2,3 cover all qualifying sources. The ordinary top-two-cap bound from Section1 supplies a pair with own sum at least8/9. As shown at the start of Section5, the largest two own caps include row3, so one of these two covering pairs has the required own sum.

This exhausts the matched-maximal-coordinate case.

## 6. Score, boundaries, and scope

The cases cover every interior barycentric point, including maximal-coordinate ties. In each case one deterministic pair has own-cap sum at least8/9 and every qualifying source hits at least one of its rows. Its two scores therefore sum to at least(8/9)v+E, proving(1).

All missed-source tests use closed regions. A source whose support maximum is zero misses the row and is included in those same closed intersections; the strict capacity bounds exclude it whenever needed. Intersections of finitely many boundary lines have area zero. Area qualification at exactly V/4, equal source weights or unequal weights, and E=0 are all included. No approximation or general-position step is used beyond the explicit strict original-vertex signs.

This theorem addresses the distinct-apex(1,1,2) sign pattern only. It is a fixed-fan certificate and does not by itself select a center for arbitrary orientations, cover zero vertex heights, or prove OC.
