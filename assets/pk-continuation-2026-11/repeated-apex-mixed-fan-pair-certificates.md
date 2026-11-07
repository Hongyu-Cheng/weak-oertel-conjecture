# Repeated-apex mixed planar fans admit a covering pair

Research draft, 6 November 2026. This proves a fixed-fan source-score certificate for the mixed sign patterns in which the two vertex-side cap rows have the same original apex, and for the sign-reversed pattern. All original vertex signs are strict and the common center is interior. The remaining mixed patterns with different original apexes are not asserted here.

## 1. A sharp elementary lobe bound

Use affine coordinates in which the original triangle has vertices O=(0,0), (1,0), (0,1); areas below are ratios to its area. A vertex-side cap with apex O is

    K(u,v)=conv{O,(u,0),(0,v)},     0<u,v<1.

Suppose P=K(U,v), Q=K(u,V), where 0<u<U<1 and 0<v<V<1. Their cutting lines cross inside the triangle. Set r=u/U and s=v/V. The area ratios of Q and P are respectively UV r and UV s. If |Q|<=|P| then r<=s. The portion Q outside P is a triangle. Direct line intersection gives its area ratio

    L=UV r(1-s)^2/(1-rs).

For fixed r in(0,1), (1-s)^2/(1-rs) is strictly decreasing for 0<s<1, since its logarithmic derivative is -2/(1-s)+r/(1-rs)<0. Therefore

    L <= UV r(1-r)/(1+r)
      <= 3-2 sqrt(2) <1/4.                         (1)

The maximum of r(1-r)/(1+r) on[0,1] occurs at r=sqrt(2)-1 and equals3-2sqrt(2). The last comparison follows from sqrt(2)>11/8. Interchanging the coordinate axes treats the reverse crossing order. Nested caps have zero outside lobe. Thus for any two same-apex vertex caps, the part of the smaller outside the larger has area strictly below |B|/4. The numerical constant3-2sqrt(2) is an upper bound uniform over the triangle, point, and directions; no volume comparison of their unions is used.

## 2. Three same-apex cutting lines through one center

Let the common interior point have coordinates (b,c), with b,c>0 and a=1-b-c>0. Every strict vertex-side cap at O whose boundary passes through this point has the form

    K(t)=K(t,v(t)),
    v(t)=c t/(t-b),
    b/(1-c)<t<1.

Its area ratio is

    p(t)=c t^2/(t-b),
    p''(t)=2 c b^2/(t-b)^3>0.                        (2)

Consider three distinct parameters t_1<t_0<t_2. The normals of the two vertex-side halfplanes K(t_1), K(t_2), together with the opposite orientation of K(t_0), form a full positive fan. Conversely, a positive fan with two vertex-side rows at this same apex and one two-positive row whose negative original vertex is that apex has this ordering, after relabeling. To see the ordering, normalize each apex-positive affine function to have value1 at O. The positive dependence writes the function of the opposite row as a strict convex combination of the two other apex-positive functions. Their coefficient vectors are (1/t,1/v(t)); because b/t+c/v(t)=1, these vectors lie on a line and the convex combination lies strictly between them. The same argument applies after reversing all orientations.

Write p_i=p(t_i). Strict convexity gives

    p_0 < max(p_1,p_2).                              (3)

The following scalar bound will also be used:

    min(p_1,p_2)-p_0 <1/9.                           (4)

Here is a complete proof. Convexity on the left and right of t_0 gives

    p_1 <= max(p_0,L),   p_2 <= max(p_0,R),
    L=b/(1-c),         R=c/(1-b),

where L and R are the endpoint values of p on the closed feasible interval. If b<=c then L<=R. If c>=1/2, the function p is increasing throughout the feasible interval, so min(p_1,p_2)<=p_0 and(4) holds. If c<1/2, both b,c<1/2 and the global minimum of p is4bc, attained at t=2b. Thus

    min(p_1,p_2)-p_0
      <= max(0,L-4bc)
      = b(1-2c)^2/(1-c)
      <= c(1-2c)^2/(1-c) <1/9.

For0<c<=1/3, use1/(1-c)<=3/2 and the elementary maximum u(1-u)^2<=4/27 for u=2c to obtain at most1/9; equality is impossible because equality in the denominator bound would require c=1/3, whereas equality in the cubic maximum requires c=1/6. For1/3<=c<1/2, use c/(1-c)<1 and(1-2c)^2<=1/9, again strictly. If c<b, interchange the axes and replace the parameter by its other edge intercept; the ordered cuts and the expression min(p_1,p_2)-p_0 are unchanged. This proves(4).

There is also a useful lobe estimate for a minimum-area outer cap. If p_1<=p_2, then

    |K(t_1)\K(t_0)|/|B| <1/4.                       (5)

If p_1<=p_0, this is(1). Otherwise p_0<p_1<=p_2; continuity gives a parameter t_* in(t_0,t_2] with p(t_*)=p_1. The lobe K(t_1)\K(t_0) is contained in K(t_1)\K(t_*): in the relevant side of the two crossing lines the intercept v(t) decreases as t increases, or directly the lobe areas are b[v(t_1)-v(t)]. Formula(1), applied to the two equal-area caps K(t_1),K(t_*), proves(5). The case p_2<=p_1 follows by exchanging the two axes.

## 3. Pair certificates for both mixed orientations

Normalize the area of B as vV, where0<v<=1 and V>0. Let finitely many source triangles P_m subset B have area at least V/4, with nonnegative weights summing to E=1-v. A row is hit when its oriented affine function has strictly positive maximum on the source. The normalized score is v times the own-cap fraction plus the weights of its hits. A source misses a pair of rows precisely when it is contained in their common closed negative region.

First orient the rows as K(t_1), K(t_2), and B\int K(t_0). Choose r in{1,2} with p_r>p_0, possible by(3). The corresponding vertex-side row and the opposite K(t_0) row have own-cap sum

    p_r+(1-p_0)>1.

Their common closed negative region is K(t_0)\int K(t_r). Its area is below |B|/4 by(1), since K(t_0) has smaller area. Thus no qualifying source can miss this pair. The pair of scores has sum greater than v+E=1, and hence some row has score strictly greater than1/2.

Now reverse every orientation: the rows are B\int K(t_1), B\int K(t_2), and K(t_0). Choose r in{1,2} with p_r=min(p_1,p_2). The corresponding opposite row and the K(t_0) row have own-cap sum

    1-p_r+p_0>8/9                                  (6)

by(4). Their common closed negative region is K(t_r)\int K(t_0), whose area is below |B|/4 by(5). Again every qualifying source hits at least one of the selected rows. Consequently one row has score strictly greater than

    (4/9)v+E/2 =4/9+E/18.                           (7)

All boundary lines have zero area, and the missed regions are closed for the source-containment test. The strict support convention causes no exception: if a source misses both rows, it lies in their closed common negative region, already too small in area. The argument even allows arbitrary measurable sources of area at least V/4 in these repeated-apex cases; their triangular shape is not needed for the final exclusion.

## 4. Exact scope

The proof gives a deterministic covering pair at an arbitrary interior center for the repeated-apex mixed positive fans and their sign reversals. It neither moves the center nor proves a center that works for all orientations. It does not cover the mixed pattern whose two one-positive vertex-side rows have different original apexes. The lobe and scalar inequalities above are elementary geometric inputs independent of the Oertel conjecture.
