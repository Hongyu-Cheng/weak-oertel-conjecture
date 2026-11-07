# Exact triangle depth and a higher-face obstruction in dimension three

Research note, 6 November 2026. The first calculation is elementary background for the two-dimensional hitting model. The second identifies why restricting its cap geometry to one-vertex cuts cannot extend verbatim to all d.

## Exact triangle depth

Let T be a full-dimensional triangle and let x have barycentric coordinates a<=b<=c. Then its normalized ordinary halfspace depth is exactly4ab.

It suffices to consider lines through x, since a containing halfplane can be moved parallel to x without increasing captured area. If x is on the boundary then a=0 and a supporting line gives zero area, as required. Assume henceforth x is interior.

First consider a triangular cap cutting off vertex i. In the affine coordinates at that vertex, let its intercepts on the two incident edges be A,B in (0,1], and write x's other barycentric coordinates as lambda_j,lambda_k. The through-x equation is

    lambda_j/A+lambda_k/B=1,

and the relative cap area is AB. Arithmetic-geometric mean gives

    AB>=4 lambda_j lambda_k>=4ab.

At the vertex whose barycentric coordinate is c, the other two coordinates are a,b. Since b<=1/2, the intercepts A=2a,B=2b are both admissible and give an actual through-x triangular cap of area4ab. Thus triangular cuts have exactly the required minimum.

Now consider a quadrilateral cap, complementary to a triangular cap at some vertex i. For the latter triangle the same intercept relation holds, and its area is AB. Put lambda_j=p and lambda_k=q. Eliminating B gives

    AB=q A^2/(A-p),
    p/(1-q)<=A<=1.

The derivative has the sign of A-2p. Hence the maximum over the displayed interval occurs at an endpoint, and the quadrilateral area is at least

    min(1-q/(1-p),1-p/(1-q))
      =min(lambda_i/(1-p),lambda_i/(1-q)).

Among all ordered distinct barycentric coordinates, the smallest quotient lambda_i/(1-lambda_j) is a/(1-b). To check this, for fixed numerator choose the largest permissible denominator. The only competing smallest-numerator choices are a/(1-b) and b/(1-a); the former is no larger because a<=b<=1/2 implies a(1-a)<=b(1-b). Every choice with numerator c is larger still. Finally

    a/(1-b)>=4ab,

since4b(1-b)<=1. Thus quadrilateral caps cannot improve the triangular minimum. Degenerate caps through vertices follow by continuity, or directly from the endpoint formulas. All boundaries have zero area. This proves the exact formula for every point and every proper closed halfplane.

## A genuine two-vertex cap improvement for a tetrahedron

Let T be a full-dimensional tetrahedron, and let x have barycentric vector

    (9/20,9/20,1/20,1/20).

The two-vertex cap lambda2+lambda3<=1/10 contains x on its boundary and has relative volume

    3(1/10)^2-2(1/10)^3=7/250.

This is the exact beta(2,2) subset-cap formula, also recorded in accepted fact290ddd8516d76865.

For comparison, every triangular-pyramid cap cutting off only one vertex has relative volume at least4/121. Indeed if that vertex is one of the two with coordinate9/20, the other coordinates are9/20,1/20,1/20. Write A1,A2,A3 in (0,1] for the three edge intercepts. The through-x equation is

    (9/20)/A1+(1/20)/A2+(1/20)/A3=1.

For fixed A1, arithmetic-geometric mean minimizes A2 A3 when A2=A3, yielding

    A1 A2 A3 >= A1 [ (1/10)/(1-(9/20)/A1) ]^2.

The right side is (1/100) A1^3/(A1-9/20)^2. Its derivative has the sign of A1-27/20, so it decreases throughout the feasible interval A1<=1. At A1=1 it equals4/121, attained by A2=A3=2/11.

If instead the retained vertex has coordinate1/20, then its three other coordinates are9/20,9/20,1/20. The unrestricted AM-GM intercept bound already gives

    A1 A2 A3 >=27(9/20)^2(1/20)=2187/8000>4/121.

Therefore every cap of one-vertex pyramid type has volume at least4/121, whereas

    7/250<4/121

because847<1000. The minimum over all halfspaces is thus strictly smaller than the minimum within that one-vertex family. Any all-dimensional extension of a triangle argument must account for cuts supported on higher-dimensional vertex subsets, rather than only tilted one-vertex caps.
