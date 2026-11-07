# Exact one-copy depth and failure of reverse tensorization

Status: proposed mathematical lemma/counterexample; not an accepted fact. The target weak problem and exact OC are unchanged. This rules out two stronger auxiliary claims, not either Oertel statement.

## Theorem

For an integer r>=1, set v_0=(-1,...,-1), v_i=e_i (1<=i<=r), P_r=conv{v_0,...,v_r}, and C_r=P_r x [0,1] in R^r x R. Its entire integer support is A_r={0,v_0,...,v_r}, each fiber has length one, and W_r=r+2. Write D(C) for maximum halfspace depth divided by total mixed volume. Then

    D(C_r)=3/[2(r+2)].                                      (1)

The unique deepest point is (0,1/2). If p is the uniform law on A_r, the exponential capacity

    E(p)=max_{j in A_r} inf_{a in R^r}
                 sum_{z in A_r} p_z exp(a dot (z-j))

is exactly one. In particular no positive absolute c can satisfy D(C)>=c E(p) for all convex bodies of arbitrary integer dimension, even with continuous dimension one.

For every m>=1, regroup C_r^m into rm integer coordinates and m continuous coordinates. The point ((0,1/2),...,(0,1/2)) is an actual mixed-integer point and satisfies, against every closed ambient halfspace,

    depth_normalized >= 1/[4(r+2)].                        (2)

Consequently there are no absolute A>0 and polynomial Q(m,n,d), positive on positive integer arguments, such that

    D(C^m) <= Q(m,n,d) [A D(C)]^m                         (3)

for every mixed convex body C and every m>=1. The obstruction remains if a dimension-dependent factor bounded above and below by positive absolute constants, such as gamma_{md}, is inserted on either side.

## Proof of the exact support

Write a point of P_r as sum_{i=0}^r alpha_i v_i, with alpha_i>=0 and sum alpha_i=1. Its coordinates are z_i=alpha_i-alpha_0. If z is integral and 0<alpha_0<1, every z_i is a nonnegative integer, while (r+1)alpha_0+sum_i z_i=1. The sum of the z_i cannot be >=1, so z=0. The cases alpha_0=0 and alpha_0=1 respectively give one of e_i and v_0. All the listed points are present. P_r is a full-dimensional simplex and C_r a convex body.

## A scalar clipping identity

Let N>=2, q in [0,1], and clip(s)=min(1,max(0,s)). Then

    min_{s_1+...+s_N=0} sum_i clip(q+s_i)=min(Nq,1).       (4)

If some q+s_i>=1, the sum is at least one. Otherwise clip(q+s_i)>=q+s_i for every i, so the sum is at least Nq. If Nq<=1, the choice s_i=0 attains Nq. If Nq>=1, use s_1=...=s_{N-1}=-q and s_N=(N-1)q, which attains one. All these choices are finite.

## Exact depth at every possible base

At the central base, take y=(0,t), t in [0,1]. A halfspace containing y can be shifted parallel until its boundary contains y; this only decreases its measure. For a nonzero continuous normal, divide its defining inequality by the absolute value of that normal. For positive continuous normal it becomes

    a dot z + x >= t.

The central interval contributes q=1-t. The outer fibers contribute clip(q+s_i), where s_i=a dot v_i and sum_i s_i=0. Conversely every zero-sum vector (s_0,...,s_r) arises in this way: set a_i=s_i for i>=1, so a dot v_0=-sum_{i>=1}s_i=s_0. By (4), the infimum over such halfspaces is F(1-t), where

    F(q)=q+min((r+1)q,1).

The negative continuous normal similarly gives F(t). A vertical through-point halfspace contains the central fiber and at least one outer fiber because sum_i a dot v_i=0, so its mass is at least two. Therefore

    h_{S_r}(0,t)=min(F(t),F(1-t)).                        (5)

The expression is attained by finite nonvertical normals. F is strictly increasing; thus (5) has its unique maximum at t=1/2, with value 3/2.

Every outer base v_i is an exposed vertex of P_r. For a point (v_i,t), the own interval gives the lower bound min(t,1-t). Choose a linear functional exposing v_i strictly above all other bases. Adding a sufficiently large positive multiple of that functional, anchored to vanish at v_i, to an own-fiber halfspace excluding the other bases isolates precisely the chosen interval cap. Hence its full mixed depth is exactly min(t,1-t)<=1/2. Equations (1) and uniqueness follow.

No halfspace orientation was omitted. Vertical boundaries may carry whole fibers and were treated with their actual closed-boundary mass.

## Capacity

The mean of p is zero since sum_i v_i=0. Jensen's inequality gives sum_z p_z exp(a dot z)>=1, while a=0 gives equality. Thus the capacity at j=0 is one. At every j its infimum is at most one by a=0, proving E(p)=1.

## A direct all-product lower bound

Let Z be uniform on A_r and let T be uniform on [-1/2,1/2], independently. The normalized mixed measure on C_r is the law of (Z,T+1/2). For any a in R^r, X=a dot Z is centered. If b_i=a dot v_i, then

    E X^4 = (sum_i b_i^4)/(r+2)
          <= (sum_i b_i^2)^2/(r+2)
          = (r+2)(E X^2)^2.                            (6)

Every scalar multiple of T has fourth moment (9/5) times its variance squared. If independent centered real variables X_i satisfy E X_i^4<=K(Var X_i)^2 with K>=3, expansion of the fourth power gives

    E(sum_i X_i)^4
      =sum_i E X_i^4 + 6 sum_{i<j} Var X_i Var X_j
      <=K(sum_i Var X_i)^2.                            (7)

Thus every scalar projection Y of the centered product law of m independent copies has mean zero and E Y^4<=(r+2)(E Y^2)^2. Its variance is positive for every nonzero ambient normal, since A_r spans R^r and T has positive variance.

For any centered Y of variance sigma^2>0 and fourth moment at most K sigma^4, Holder gives

    E|Y| >= sigma^3/(E Y^4)^(1/2) >= sigma/sqrt(K).

Also E Y_+=E|Y|/2 and Cauchy--Schwarz gives

    E Y_+ <= sigma sqrt(P(Y>0)).

Hence P(Y>=0)>=P(Y>0)>=1/(4K). With K=r+2 this proves (2) at the displayed deterministic point for every through-point halfspace; containing halfspaces have at least that mass.

Fix A>0 and choose r with 3A/[2(r+2)]<1. If (3) held, (1)--(2) would give

    1/[4(r+2)] <= Q(m,r,1) [3A/(2(r+2))]^m

for every m. The right-hand side tends to zero because an exponential with base below one dominates a fixed polynomial. This is a contradiction.

## Relation to the existing records and novelty scope

Accepted candidate 01c991c9f33e83df already proves that E(p) is the asymptotic tensor root rate of actual maximum depth. Accepted candidate 5d0f9e78ced711d6 uses this same base simplex family to disprove one-copy capacity comparison and reverse tensorization for its different *coupled entropy certificate* E_script(C). The present theorem concerns actual halfspace depth D(C), not that certificate, and gives its exact value and a direct product lower bound independent of the asymptotic theorem.

Pending candidate ffc34ddb869ec7d5, section 5, proves an analogous exact product-simplex depth formula for n=d>=2, using simplex fibers and a cyclic coupling. Its geometric mechanism is related. The present interval-fiber formula holds for every integer dimension r with d=1, and the explicit actual-depth reverse-tensorization impossibility is the additional conclusion. This scope must be retained when deciding whether to create a new candidate or append a corollary to an existing packet.
