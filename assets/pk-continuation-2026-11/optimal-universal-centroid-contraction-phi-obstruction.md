# A finite-dimensional obstruction to every universal centroid-contraction Phi consumer

Status: proved auxiliary obstruction. This is not a counterexample to OC. It shows that even the optimal universal retained-volume constants for arbitrarily many successive ordinary centroid cuts cannot complete the sharp Phi/k bridge. The counterexample is an actual convex body with n=1, d=50 and three positive fibers; all inequalities below have explicit exact integer certificates.

## 1. The precise consumer being tested

For d>=1 and k>=1 let sigma_{d,k} be the supremum of |K_k|/|K_0| over all d-dimensional convex bodies K_0 and all sequences in which K_i is obtained by retaining either closed halfspace through the ordinary centroid of K_{i-1}. Thus sigma_{d,k} is the best universal contraction constant for k such cuts. In particular sigma_{d,1}=q_d=1-gamma_d, by classical centroid Gruenbaum and its simplex equality example. Each finite-k supremum is attained by the compactness argument in `uniform-two-centroid-cut-gap.md`, though only the lower bounds from explicit cut sequences are needed here.

For the actual-fiber root-retention functional Phi_j defined in `nested-root-retention-depth-functional.md`, the strongest possible consumer that uses only these universal constants is

    B(C) = max_j sup_{k>=1} Phi_j(sigma_{d,k})/k.        (1)

The nested-cut argument proves that maximum mixed depth is at least B(C). The statement that B(C) always reaches the sharp OC target is false.

## 2. Actual convex body and its exact Phi profiles

Let d=50. Take any 50-dimensional simplex T containing the origin and of volume one. Put s=3/5, a=s^(1/50), and

    C = conv( {-1} x aT, {0} x T, {1} x aT )
          subset R x R^50.

This is a full-dimensional compact convex body. Its only integer bases are -1,0,1. The endpoint fibers are aT. Because aT subset T, every convex combination at base zero lies in T, so the central fiber is exactly T. Hence its mixed-volume table is (s,1,s) and total volume is W=11/5.

At either endpoint the only minimal affinely independent root support is its singleton. At the central base the supports are its singleton and {-1,1}, the latter with barycentric weights 1/2,1/2 and cost log(1/s). It follows directly from the finite minimization defining Phi that

    Phi_0(t) = 1-t+(s-t)_+,
    Phi_{-1}(t)=Phi_1(t)=s(1-t),             0<=t<=1.    (2)

In particular Phi_0(t)<=1+s=8/5. The sharp OC target, in unnormalized mixed volume, is

    T_OC = gamma_50 W/2 = (11/10) gamma_50.             (3)

We prove that every term in (1) is strictly below (3), with a uniform gap for all k>=4.

## 3. Explicit lower bounds on the universal contraction constants

Use barycentric coordinates lambda_1,...,lambda_51 in a 50-simplex with total volume one. A cap lambda_i>=b has volume (1-b)^50. Intersections of several such caps have volume (1-sum b_i)_+^50, by translation and homothety of the simplex.

For two successive centroid cuts first retain lambda_1<=1/51. The centroid value of lambda_2 in that retained body is

    c_2=1/51 + gamma_50/[51^2(1-gamma_50)] > 1/51.

Thus the second retained body contains {lambda_1<=1/51,lambda_2<=1/51}. Inclusion-exclusion gives

    sigma_{50,2} >= p_2,
    p_2=1-2(50/51)^50+(49/51)^50.                     (4)

For three successive cuts retain lambda_j<=c_j at the current centroid, for j=1,2,3. Before cut j the uncut coordinates are exchangeable, so

    c_j = [1-sum_{i<j} E(lambda_i | preceding cuts)]/(52-j).

Consequently 0<c_i<=1/(52-i)<=1/49 for i<=3. The preceding retained conditions give E(lambda_i | preceding cuts)<=c_i. For j<=3 the numerator is therefore at least 1-2/49=47/49, and the denominator is at most 51. Thus

    c_j >= 47/2499=:b  for j=1,2,3.

The final retained body contains {lambda_1,lambda_2,lambda_3<=b}. Inclusion-exclusion now gives

    sigma_{50,3} >= p_3,
    p_3=1-3(2452/2499)^50+3(2405/2499)^50
                                      -(2358/2499)^50. (5)

These are lower bounds on worst-case retained volumes, as required: because Phi decreases, they give upper bounds on the proposed consumer. No direction of an inequality is reversed.

## 4. Exact rational estimates

The following four strict inequalities suffice:

    102/275 < gamma_50=(50/51)^50 < 2/5,
    p_2 > 49/125,
    p_3 > 1/5.                                        (6)

For completeness each follows by cross multiplication from the indicated positive integer, so these are exact certificates rather than decimal estimates:

    275*50^50-102*51^50
      =4068043986047429985602706053949018164846014812458565621403549431200916045583537369898;

    2*51^50-5*50^50
      =3403287057921129734944673741972200624218705591912577144678361775858805567733656130002;

    76*51^50-250*50^50+125*49^50
      =727420084022539442635372648876975077461212355756106614514663906596044028494940440201;

    4*2499^50-15*2452^50+15*2405^50-5*2358^50
      =9787215075048633955976402806724642126219384023004732660407207393224944221178287780859324176777815665169962716026084743921308916718526931957767094815401368817365986111899.

In particular (3) and the first lower bound give

    T_OC > (11/10)(102/275)=51/125.                    (7)

The accompanying verifier contains only exact integer and Fraction arithmetic and checks these displayed identities and all comparisons.

## 5. Exhaustion of every target and every number of cuts

At the central target:

* k=1: gamma_50<2/5 implies q_50>3/5=s, so (2) gives Phi_0(sigma_{50,1})=gamma_50<T_OC.
* k=2: by (4), monotonicity, and (6),

      Phi_0(sigma_{50,2})/2
        <= Phi_0(p_2)/2
         < Phi_0(49/125)/2
         = 51/125 < T_OC.

  Strict monotonicity of Phi_0 on [0,1] justifies the strict inequality; the explicit point 49/125 is below s.

* k=3: by (5)--(6),

      Phi_0(sigma_{50,3})/3
         <=Phi_0(p_3)/3
          <Phi_0(1/5)/3
          =2/5 <51/125<T_OC.

* k>=4: the uniform bound in (2) gives

      Phi_0(sigma_{50,k})/k <=(8/5)/4=2/5<T_OC.

At either endpoint, for k=1 the consumer is s gamma_50<T_OC. For k>=2 it is at most s/k<=3/10<T_OC. Hence the supremum over all k and all three targets is strictly below the sharp target. In fact it is bounded above by max(gamma_50,51/125,2/5,3/10)=51/125, whereas T_OC>51/125.

This completes the counterexample to the global scalar bridge (1).

## 6. Implication for proof design

The obstruction already uses the optimal universal k-cut constants simultaneously for every k. Improving a two-step gap, choosing a longer finite block, or proving a d+1-step uniform contraction cannot by itself repair (1). The missing information must enter beyond a universal retained-volume number followed by the additive original-cap union bound divided by k. Possibilities not ruled out here include retaining the shape of the current target together with its root supports, a sharper accounting of overlapping removed caps, or replacing the prescribed ordinary centroid selection rule by a different adaptive center construction. This note asserts no result about those alternatives and no failure of OC itself.
