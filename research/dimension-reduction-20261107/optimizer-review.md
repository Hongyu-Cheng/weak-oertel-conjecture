# Independent numerical optimizer review

Date: 2026-11-07. Agent: `small_dimension_optimizer`.

## Result and status

An independent asymmetric three-cut triangle search found a floating-point candidate with **integer dimension n = 167, continuous dimension d = 99**, using block counts `(55, 56, 56)`. Its smallest scalar margin was approximately **0.00008560431838**. The complete numerical tuple is in `asymmetric-sharp-n167-numerical.json`.

This file records numerical discovery evidence, not an exact counterexample certificate. The parent subsequently reported that a different n = 167 tuple was rationalized by the `asymmetric_fan_search` agent, given a full proof, and independently reviewed. That later certificate should be used for the mathematical claim. My numerical search concerns the sharp threshold `Gamma_d / 2^n`, where `Gamma_d = (d/(d+1))^d`; it does not establish the threshold `1/(e 2^n)`.

## Family and objective

Start with the triangle with vertices `(0,0)`, `(1,0)`, `(0,1)`. Three cuts pass through an interior point p. Their outward normals have consecutive angular gaps strictly less than pi, so positive rescaling of the three functionals gives a positive dependence. For each index a, clip the triangle by the two other nonpositive halfspaces. Among triangles with one vertex p and the other two vertices in this clipped polygon, choose the maximum area triangle. Its relative area is `theta_a`. The relative area of the positive halfspace for cut a is `beta_a`.

Joining the planar middle body and these source triangles with the remaining simplex vertices gives dimension d = 99 while preserving the volume ratios. For a common positive fiber volume m and block counts N_a, the limiting equal inner and outer scale calculation is

```
delta_a = (m / theta_a)^(1/99) - 1
E_a = theta_a * sum_{r=1}^{N_a} binom(N_a,r)
                         * max(1-r*delta_a, 0)^99
Gamma_99 = (99/100)^99.
```

The optimization maximized the minimum of four margins:

```
1 + E_0 + E_1 + E_2 - m
Gamma_99*m - beta_0 - E_0
Gamma_99*m - beta_1 - E_1
Gamma_99*m - beta_2 - E_2.
```

The geometric realization needs a strictly larger negative-fiber erosion scale, small translations, and an origin-fiber argument. Strictly positive numerical margins provide room for those perturbations but do not replace checking them. In particular, the optimized p is not the centroid, and the three delta values differ.

## Asymmetric candidate

| Quantity | Block 0 | Block 1 | Block 2 |
| --- | ---: | ---: | ---: |
| N | 55 | 56 | 56 |
| theta | 0.13969294261293785 | 0.13832410724433666 | 0.13833726088233558 |
| beta | 0.45600230687696397 | 0.45255317730421485 | 0.4523140811837161 |
| delta | 0.03248305655857069 | 0.0325857594405389 | 0.03258476765427432 |
| E | 0.7670322859367606 | 0.7704813515577563 | 0.770719558655779 |
| Central-cut margin | 0.0000856176061034 | 0.0000856815578568 | 0.0000865705803329 |

Here `m = 3.3081475918319123`, `p = (0.33377647912696873, 0.3345814365383487)`, and the total-volume margin is `0.0000856043183837`.

I used the clipping and determinant geometry routine in `triangle_fan_search.py`, with SciPy differential evolution over two parameters for p, three for the cut directions, and m. Binomial weights were evaluated using `gammaln`. The six parameters encode

```
p = (x[0], (1-x[0])*x[1])
angles = (x[2], x[2]+x[3], x[2]+x[3]+x[4])
m = x[5].
```

Search bounds were `[(.31,.36),(.47,.53),(3.95,4.2),(2.35,2.56),(1.53,1.76),(3.1,3.5)]`; settings were population multiplier 16, maximum 450 generations, tolerance `1e-9`, seed 1971, polishing enabled, one worker. The saved optimizer status is `success: false` because the generation limit was reached. This does not negate the positive objective at the returned point, but no convergence or global optimality claim is made.

## Symmetric controls

For the cyclic triangle parameter a, I used

```
theta = (1-a)/(3*(2-a))
beta  = 1/((1+a)*(2-a)).
```

Optimizing a and the common scale at d = 99 gave these floating-point results:

| Equal block size | n | Best minimum margin found |
| ---: | ---: | ---: |
| 56 | 168 | +0.000382686465798 |
| 55 | 165 | -0.000499351104956 |
| 54 | 162 | -0.00138490882368 |
| 53 | 159 | -0.00227404337951 |

The n = 168 point used `a = 0.2876369340268483` and `delta = 0.03258626965043199`. Keeping the geometry cyclic while making the counts `(55,56,56)` gave a negative best margin of approximately `-0.00669594`; `(55,55,56)` gave approximately `-0.01370424`. Thus changing only the block counts did not give the improvement. Allowing the cut geometry and source volumes to adapt to the counts did.

These are optimizer outcomes within the tested parametrizations. Negative results are not global impossibility certificates.

## Remaining directions and limitations

- This search found no example with both dimensions below 100. Its positive contribution is the independent numerical n = 167, d = 99 discovery.
- Mixed paid patterns, including sources charged to two or all three central cuts, were suggested but not completed in this independent branch. Their larger source volumes must be balanced against additional central-cut costs.
- More general facet-dependent expansion and erosion prices, and positive source simplices that need not contain the common cut point, remain untested here.
- I did not certify a minimum possible n for asymmetric three-cut fans. The search was bounded and local in its parameter ranges.
- The parent's polygon, tetrahedral, and other geometric searches are separate evidence; their outcomes are not claimed as independent computations in this report.
