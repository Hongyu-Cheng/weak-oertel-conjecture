# Exact deficit-hitting obstruction when the midpoint set is not a simplex

Research note, 6 November 2026. This is a direct corollary/adaptation of the equal-large-partner construction in candidate 5e8a8af95fa24a1d. It isolates the shape assumption in the proposed limiting hitting theorem. It does not refute that theorem for simplex midpoint sets, and it does not refute OC.

Let T be the standard4-simplex, V=|T|=1/24, and Gamma=256/625. Let

    R=T intersect {x1,x2,x3<=19/100},
    rho=|R|/V=2942511/25000000,
    s=rho^(-1/4), P=(s/2)R,
    e=1/100, v=99/100, r=v^(1/4), B=rT.

Then |B|=vV, |P|=V/16, and P subset B. The deficit mass is exactly E=eV=V-|B|. Consider the strict hitting score

    D(y)=inf_(f nonconstant affine)
      [|B intersect {f>=f(y)}|+E 1{h_P(f)>f(y)}],
      y in B.

No y in B has D(y)>=Gamma V. The same obstruction holds if the strict support sign in the definition is replaced by >=: the certifying missed directions have strict support gaps.

Proof of the geometric data. Inclusion-exclusion gives rho as displayed. Exact arithmetic gives

    (9/5)^4 rho-1=3680814671/15625000000>0,

so s<9/5. Also

    v-1/(16rho)=135058589/294251100>0.

Thus (s/2)^4<v=r^4, and P subset (s/2)T subset rT=B. The exact volume is |P|=(s/2)^4|R|=V/16.

Proof that every center fails. Let lambda0,...,lambda4 denote the barycentric coordinates of B. Suppose y were a successful center. Every one of its five positive barycentric caps has B-volume v(1-lambda_i(y))^4V and hitting bonus at most eV. Consequently

    lambda_i(y)<=1-q for all i,
    q=((Gamma-e)/v)^(1/4).

The exact calculation

    (Gamma-e)/v-(159/200)^4=73581429/17600000000>0

shows q>159/200. Summing the other four coordinates therefore gives

    lambda_i(y)>=4q-3>9/50 for all i.

For i=1,2,3, however,

    max_P lambda_i=(s/(2r))(19/100)
       < ((9/5)/(2(99/100)))(19/100)=19/110<9/50,

where r=v^(1/4)>v=99/100. Thus the three positive caps in these directions strictly miss P. Their score condition forces

    lambda_i(y)<=1-(Gamma/v)^(1/4), i=1,2,3.

Combining these three bounds with the first two remaining-coordinate bounds yields

    1=sum_i lambda_i(y)
      <=5-3(Gamma/v)^(1/4)-2((Gamma-e)/v)^(1/4).

We show the right side is strictly below1. For 0<=u<=1/100 put

    F(u)=3 Gamma^(1/4)+2(Gamma-u)^(1/4)-4(1-u)^(1/4).

Then F(0)=0 because Gamma^(1/4)=4/5. Differentiation gives

    F'(u)=(1-u)^(-3/4)-(1/2)(Gamma-u)^(-3/4).

The ratio (Gamma-u)/(1-u) decreases in u, and at u=1/100 it exceeds2/5 by exactly1/275. Moreover (2/5)^3=8/125>1/16, so 2/5>2^(-4/3). It follows that F'(u)>0 throughout the displayed interval. Therefore F(e)>0, which after division by v^(1/4) gives

    3(Gamma/v)^(1/4)+2((Gamma-e)/v)^(1/4)>4.

This contradicts the barycentric sum, and completes the exact certificate.

The obstruction obeys every volume and deficit relation in the proposed hitting model, but P is the nonsimplex truncation of a simplex. Therefore any proof of that model using only P subset B and |P|>=2^(-d)V, while discarding the simplex or near-Grunbaum shape information, cannot succeed. The shape information must enter the proof substantively.
