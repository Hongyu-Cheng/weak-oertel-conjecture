# Nonuniform centers obstruct the planar circulation-rescaling flow

Research draft, 6 November 2026. This is an exact counterexample to extending the uniform-centroid cyclic rescaling argument to a fixed nonuniform barycentric center. It is not a bad-fan or OC counterexample.

## 1. A positive fan with fixed nonuniform center

Let B be a planar simplex, with barycentric coordinates lambda=(lambda_1,lambda_2,lambda_3). Fix

    s=(1/6,1/2,1/3),
    C=[[0,1,-1],[-1,0,1],[1,-1,0]],
    G(t)=3I-11^T+t C,
    F(t)=G(t) diag(6,2,3),       0<=t<=1/4.

The ith cut is the closed halfspace whose affine barycentric value (F(t)lambda)_i is nonnegative. Since diag(6,2,3)s=1, every row vanishes at s. Since the column sums of G(t) are zero, 1^T F(t)=0. The rank is two: G(t) is invertible on 1^perp because x^T G(t)x=3|x|^2 there, and multiplication by an invertible diagonal matrix preserves rank. Thus these are a genuine positive three-fan through s, with positive dependence coefficients all equal to1. The two balanced kernels are fixed along the flow. In particular F(t)diag(s)=G(t) has both row and column sums zero.

The endpoint matrices are exactly

    F(0)=[[12,-2,-3],[-6,4,-3],[-6,-2,6]],

    F(1/4)=[[12,-3/2,-15/4],
            [-15/2,4,-9/4],
            [-9/2,-5/2,6]].

Every row has exactly one positive vertex height and two negative heights. The signs stay fixed throughout the flow.

## 2. Exact cap fractions

For a triangle cut with positive vertex height a and negative heights -b,-c, its positive cap is the vertex triangle whose edge ratios are a/(a+b) and a/(a+c). Its area fraction is therefore a^2/[(a+b)(a+c)]. Applying this formula gives

    (p_1(0),p_2(0),p_3(0))=(24/35,8/35,3/8),

    (p_1(1/4),p_2(1/4),p_3(1/4))
       =(128/189,128/575,48/119).

In both triples the first entry is the unique maximum. Consequently

    max_j p_j(0)-max_j p_j(1/4)=8/945>0.

Deleting the circulation increases the maximum own-cap fraction. This differs from the uniform-centroid family, whose own-cap fractions are equal and have a common minimum at t=0.

## 3. A feasible source pattern for which every allowed volume increase fails

Normalize the reference area to V>0 and choose

    |B|=vV,       v=99/100.

Take a single source P=B with normalized source weight E=1-v=1/100. Its area is at least V/4, so it is a qualifying simplex source. Each row strictly hits P, since it has a positive vertex height; hence its pattern is the all-hit pattern. At t=1/4 the three fan scores, normalized by V, are

    S_j=v p_j(1/4)+(1-v).

Their exact maximum is

    max_j S_j=(99/100)(128/189)+1/100=1429/2100.

Now delete the circulation entirely and allow ANY enlarged middle-volume parameter v' in [v,1]. Keep the original normalized triangle shape and center s, and realize the all-hit source pattern by any qualifying triangle of that pattern. Rescale the total source weight to 1-v' as in the joint deformation. The resulting maximum score is necessarily

    v' max_j p_j(0)+(1-v')=v'(24/35)+1-v'.

It is decreasing in v', so even the best permitted choice v'=1 gives maximum24/35. Thus every such deformation increases the maximum by at least

    24/35-1429/2100=11/2100>0.

The endpoint v'=1 simply removes all source weight; the cap score remains24/35. For v'<1, all-hit source feasibility is automatic, since B itself remains a qualifying triangle. There is therefore no hidden failure of source realization or source-volume qualification in this counterexample.

More generally the same obstruction occurs for every

    v>297/305,

because this is exactly the condition

    1-v+v(128/189)<24/35.

## 4. Scope and arbitrary positive fan coefficients

This disproves a universal extension of the uniform-centroid planar cyclic monotonicity that keeps the nonuniform barycentric center, deletes the same balanced circulation, preserves the hit-pattern fractions, and only increases the middle volume while rescaling the remaining total source weight. It allows arbitrary such volume increase, so the failure is not repaired merely by selecting a different feasible threshold v'.

The choice of positive dependence coefficients does not remove this example. For any prescribed positive numbers ell_1,ell_2,ell_3, replace F(t) by diag(ell)^{-1}F(t). This preserves every oriented halfspace, source pattern, and cap fraction, while making ell the positive left kernel. Thus the same failure occurs with any prescribed positive fan coefficients.

All scores in the example are above Gamma_2=4/9. Accordingly this is not an OC obstruction, and it does not refute a deformation theorem restricted to hypothetical bad fans. It identifies the exact unproved extra step that such a restricted theorem would need: equal own-cap fractions cannot be discarded without a new comparison or an allowed change of center/pattern.
