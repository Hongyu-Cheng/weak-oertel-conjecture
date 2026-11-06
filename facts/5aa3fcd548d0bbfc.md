---
fact_id: 5aa3fcd548d0bbfc
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: scalar-amplitude-3316-template-no-go
depends_on: ["3316a7b28eca6a19","6496cb3b0fd44f9d","876a152563efe052","be359f8a6c628483"]
verifier_run: 024669ca75f6401d
target_match: null
---

## Statement

For \(n\geq2\), retain the following notation from accepted fact
`3316a7b28eca6a19`:
\[
 R_n:=2^{n^3},\qquad B_n:=R_nB_2^n,\qquad
 D_n:=B_n\cap\mathbb Z^n,\qquad N_n:=|D_n|,
\tag{1}
\]
\[
 b_n:=2R_n+1,\qquad
 \ell_n(x):=\sum_{j=1}^n b_n^{j-1}x_j,\qquad
 H_n:=2R_n\sum_{j=0}^{n-1}b_n^j=b_n^n-1.
\tag{2}
\]
Let \(\widehat\delta_n\geq0\), and put
\[
 \varepsilon_n:=\frac{\widehat\delta_n}{N_nH_n},\qquad
 \psi_{n,w}(x):=1-\varepsilon_n
 |\ell_n(x)-\ell_n(w)|\quad(w\in D_n).
\tag{3}
\]
With continuous coordinates \(y=(y_w)_{w\in D_n}\in\mathbb R^{N_n}\), define
\[
 C_n(\widehat\delta_n):=
 \left\{(x,y):
 \begin{array}{l}
 x\in B_n,\\
 y_w\geq-\psi_{n,w}(x)\quad(w\in D_n),\\
 \displaystyle\sum_{w\in D_n}y_w\leq1
 \end{array}\right\}.
\tag{4}
\]
For \(z\in D_n\), set
\[
 d_{n,z,w}:=|\ell_n(z)-\ell_n(w)|,\qquad
 d_{n,z}:=(d_{n,z,w})_{w\in D_n},\qquad
 p_{n,z}:=\sum_{w\in D_n}d_{n,z,w},
\tag{5}
\]
\[
 S_{n,z}:=N_n+1-\varepsilon_np_{n,z}.
\tag{6}
\]
Call the amplitude admissible precisely when
\[
 S_{n,z}>0\qquad\text{for every }z\in D_n.
\tag{7}
\]
For nonnegative amplitude, (4) is compact and convex. Condition (7) is
equivalent to saying that the positive-volume lattice-fiber support is
exactly \(D_n\), and it also makes the body full-dimensional.

Put
\[
 \boldsymbol\psi_n(z):=(\psi_{n,w}(z))_{w\in D_n},\qquad
 \Delta_{N_n}:=\left\{u\in\mathbb R^{N_n}:
 u_w\geq0,\ \sum_{w\in D_n}u_w\leq1\right\}.
\]
For every admissible amplitude and every \(z\in D_n\), the fiber, its volume,
its centroid, and its covariance are exactly
\[
 (C_n)_z=-\boldsymbol\psi_n(z)+S_{n,z}\Delta_{N_n},\qquad
 a_{n,z}:=\operatorname{vol}_{N_n}((C_n)_z)
 =\frac{S_{n,z}^{N_n}}{N_n!},
\tag{8}
\]
\[
 c_{n,z}=\varepsilon_n\left(
 d_{n,z}-\frac{p_{n,z}}{N_n+1}\mathbf1\right),
\tag{9}
\]
\[
 \Sigma_{n,z}=S_{n,z}^2
 \frac{(N_n+1)I-J}{(N_n+1)^2(N_n+2)},\qquad
 \Sigma_{n,z}^{-1}=
 \frac{(N_n+1)(N_n+2)}{S_{n,z}^2}(I+J),
\tag{10}
\]
where \(J:=\mathbf1\mathbf1^{\mathsf T}\). Write
\[
 W_n:=\sum_{z\in D_n}a_{n,z},\qquad
 L_n:=\{x\in\mathbb R^n:x_n=0\},
\tag{11}
\]
and define
\[
 \nu_n:=\left|
 \left(\frac{R_n}{4}B_2^{n-1}\right)\cap\mathbb Z^{n-1}
 \right|,
\qquad
 \boxed{
 T_n:=\frac{4H_n(N_n+1)\log N_n}
 {\nu_nb_n^{n-1}}.}
\tag{12}
\]
Then
\[
 \frac{T_n}{\sqrt{N_n}}\longrightarrow0.
\tag{13}
\]
For every \(n\geq2\) and every admissible amplitude,
\[
 \widehat\delta_n\geq T_n
 \quad\Longrightarrow\quad
 \sum_{z\in D_n\cap L_n}a_{n,z}\geq\frac12W_n.
\tag{14}
\]
In particular, if strict no-rank-drop holds at index \(n\), in the precise
sense
\[
 \forall A\subsetneq\mathbb R^n\
 \left[
 \begin{array}{c}
 A\text{ is a proper primitive affine lattice subspace}
 \end{array}
 \ \Longrightarrow\
 \sum_{z\in D_n\cap A}a_{n,z}
 <2^{\dim A-n}W_n
 \right],
\tag{15}
\]
then
\[
 \widehat\delta_n<T_n.
\tag{16}
\]

Consequently, let \((\widehat\delta_n)_{n\geq2}\) be any admissible sequence
for which strict no-rank-drop holds eventually, meaning
\[
 \exists n_0\ \forall n\geq n_0\ \forall A\subsetneq\mathbb R^n:
 \quad
 A\text{ is a proper primitive affine lattice subspace}
 \ \Longrightarrow\
 \sum_{z\in D_n\cap A}a_{n,z}<2^{\dim A-n}W_n.
\tag{17}
\]
Then
\[
 \frac{\widehat\delta_n}{\sqrt{N_n}}\longrightarrow0,\qquad
 \max_{z\in D_n}
 c_{n,z}^{\mathsf T}\Sigma_{n,z}^{-1}c_{n,z}
 \longrightarrow0.
\tag{18}
\]
For all sufficiently large \(n\), the constant affine map \(s\equiv0\)
satisfies
\[
 \sqrt{c_{n,z}^{\mathsf T}\Sigma_{n,z}^{-1}c_{n,z}}
 \leq\frac1{128}\qquad(z\in D_n),
\tag{19}
\]
and hence
\[
 0\in\mathsf M_{a_{n,z}/2}((C_n)_z)\qquad(z\in D_n),
\tag{20}
\]
\[
 \boxed{
 G(C_n)\geq\frac12W_n,\qquad
 R_{\rm sel}(C_n)\geq\frac{\gamma_{N_n}}2W_n
 >\frac1{2e}W_n,}
 \qquad
 \gamma_{N_n}:=\left(\frac{N_n}{N_n+1}\right)^{N_n}.
\tag{21}
\]
For every exact minimum-unmatched centroid matching \(q_n\) supplied by
accepted fact `be359f8a6c628483`, and every load-minimal dual optimizer
in accepted fact `6496cb3b0fd44f9d`, one has, with the empty-matching
convention when \(q_n=0\),
\[
 \boxed{\Delta_{C_n}(q_n)=0,\qquad\Omega_n=0.}
\tag{22}
\]

The following two-branch conclusion holds for every admissible sequence,
whether or not (17) is assumed. For all sufficiently large \(n\), the hard
package is ruled out for one of two exact reasons:

* If \(\widehat\delta_n\geq T_n\), strict no-rank-drop fails at the proper
  primitive hyperplane \(L_n\). Its required bound is the strict inequality
  \(\sum_{z\in D_n\cap L_n}a_{n,z}<W_n/2\), while (14) gives the reverse weak
  inequality.
* If \(\widehat\delta_n<T_n\), equations (19) through (22) hold. Hence any
  hard premise \(G(C_n),R_{\rm sel}(C_n)<\epsilon W_n\) with
  \(0<\epsilon\leq1/64\) fails, the required stress lower bound
  \(\Omega_n\geq W_n/(4e)\) fails, and the positive-load midpoint support is
  empty rather than full affine rank. The inequality
  \(\Delta_{C_n}(q_n)\geq\delta_0\Omega_n\) does not fail. It reduces to the
  vacuous equality \(0\geq0\).

## Proof

For \(\widehat\delta_n\geq0\), each function
\[
 -\psi_{n,w}(x)=-1+\varepsilon_n|\ell_n(x)-\ell_n(w)|
\]
is convex. Hence (4) is convex. Its base lies in the compact set \(B_n\),
all continuous coordinates have finite lower bounds, and the sum constraint
gives finite upper bounds, so it is compact. At a fixed \(z\in D_n\), make
the change of variables
\[
 u_w:=y_w+\psi_{n,w}(z).
\]
The fiber constraints become
\[
 u_w\geq0,\qquad \sum_wu_w\leq
 1+\sum_w\psi_{n,w}(z)=S_{n,z}.
\]
Under (7), this proves the fiber identity and volume formula in (8). Since
the base projection is contained in \(B_n\), there are no lattice fibers
outside \(D_n\), so (7) is equivalent to \(D_+(C_n)=D_n\). Moreover,
\(0\in\operatorname{int}B_n\cap D_n\), and \(S_{n,0}>0\). Continuity gives
a base neighborhood on which the simplex scale remains positive. A point
strictly inside one such simplex satisfies every inequality in (4) strictly.
Thus (7) also makes \(C_n\) full-dimensional.

The standard simplex has centroid \(\mathbf1/(N_n+1)\) and covariance
\[
 \frac{(N_n+1)I-J}{(N_n+1)^2(N_n+2)}.
\]
Translation by \(-\boldsymbol\psi_n(z)\) and scaling by \(S_{n,z}\) give
(9) and the first formula in (10). Since
\[
 ((N_n+1)I-J)(I+J)=(N_n+1)I,
\]
the inverse formula in (10) follows. This proves all exact fiber formulas.

We prove (14). The set \(D_n\) is centrally symmetric and
\(\ell_n(-w)=-\ell_n(w)\). For \(t\in\mathbb R\), put
\[
 P_n(t):=\sum_{w\in D_n}|t-\ell_n(w)|.
\]
Pairing \(w\) with \(-w\) and using
\[
 |t-u|+|t+u|-2|u|
 =2(\max\{|t|,|u|\}-|u|)\geq0
\]
gives \(P_n(t)\geq P_n(0)\).

Let \(z\in D_n\setminus L_n\). Because \(z_n\) is a nonzero integer and
\(|z_j|\leq R_n\),
\[
 |\ell_n(z)|
 \geq b_n^{n-1}-R_n\sum_{j=0}^{n-2}b_n^j
 =\frac{b_n^{n-1}+1}{2}.
\tag{23}
\]
For every
\[
 w=(w',0),\qquad
 w'\in\frac{R_n}{4}B_2^{n-1}\cap\mathbb Z^{n-1},
\]
one has
\[
 |\ell_n(w)|\leq
 \frac{R_n}{4}\sum_{j=0}^{n-2}b_n^j
 =\frac{b_n^{n-1}-1}{8}
 <\frac14|\ell_n(z)|.
\tag{24}
\]
Writing \(t=\ell_n(z)\), each of these \(\nu_n\) points contributes at least
\[
 |t-\ell_n(w)|-|\ell_n(w)|
 \geq |t|-2|\ell_n(w)|
 \geq\frac12|t|
 \geq\frac14b_n^{n-1}.
\]
The selected set and its complement in \(D_n\) are centrally symmetric.
The complement has nonnegative total contribution by the preceding pair
identity. Consequently
\[
 p_{n,z}-p_{n,0}
 =P_n(\ell_n(z))-P_n(0)
 \geq\frac{\nu_nb_n^{n-1}}4.
\tag{25}
\]

Admissibility makes both simplex scales below positive. Thus
\[
 \begin{aligned}
 \frac{a_{n,z}}{a_{n,0}}
 &=\left(1-
 \frac{\varepsilon_n(p_{n,z}-p_{n,0})}{S_{n,0}}
 \right)^{N_n}\\
 &\leq\exp\left(
 -\frac{N_n\varepsilon_n(p_{n,z}-p_{n,0})}{S_{n,0}}
 \right)\\
 &\leq\exp\left(
 -\widehat\delta_n
 \frac{\nu_nb_n^{n-1}}{4H_n(N_n+1)}
 \right),
 \end{aligned}
\tag{26}
\]
where \(S_{n,0}\leq N_n+1\) and
\(N_n\varepsilon_n=\widehat\delta_n/H_n\). If
\(\widehat\delta_n\geq T_n\), (26) is at most \(1/N_n\). Hence
\[
 \sum_{z\in D_n\setminus L_n}a_{n,z}
 \leq N_n\frac{a_{n,0}}{N_n}=a_{n,0}
 \leq\sum_{z\in D_n\cap L_n}a_{n,z},
\]
which proves (14). The hyperplane \(L_n\) is a proper primitive affine
lattice subspace of dimension \(n-1\), so (15) requires its mass to be
strictly less than \(W_n/2\). This proves (16).

It remains to establish (13). Put
\(\kappa_m:=\operatorname{vol}_m(B_2^m)\). Coordinate rounding in dimension
\(n-1\) gives, for all sufficiently large \(n\),
\[
 \nu_n\geq\kappa_{n-1}\left(\frac{R_n}{8}\right)^{n-1}
 \geq\left(\frac{R_n}{4\sqrt{n-1}}\right)^{n-1}.
\tag{27}
\]
Indeed, the unit cubes centered at the lattice points of
\((R_n/4)B_2^{n-1}\) cover
\((R_n/4-\sqrt{n-1}/2)B_2^{n-1}\), which contains
\((R_n/8)B_2^{n-1}\) for large \(n\), and
\(\kappa_{n-1}\geq(2/\sqrt{n-1})^{n-1}\). Also
\[
 N_n\leq(2R_n+1)^n=b_n^n\leq(3R_n)^n.
\tag{28}
\]
Using \(H_n/b_n^{n-1}<b_n\) and \(N_n+1\leq2N_n\), equations (12), (27),
and (28) give
\[
 \begin{aligned}
 \frac{T_n}{\sqrt{N_n}}
 &<\frac{8b_n\sqrt{N_n}\log N_n}{\nu_n}\\
 &\leq24\,3^{n/2}4^{n-1}(n-1)^{(n-1)/2}
 (\log N_n)R_n^{\,2-n/2}.
 \end{aligned}
\tag{29}
\]
Since \(R_n=2^{n^3}\) and
\(\log N_n\leq n\log(3R_n)\), the last expression tends to zero. This
proves (13), and (16) then gives the first limit in (18).

We next calculate the covariance distance exactly. From (9),
\[
 (I+J)c_{n,z}=\varepsilon_nd_{n,z}.
\]
Combining this identity with (10) gives
\[
 \begin{aligned}
 \tau_{n,z}(0)^2
 &:=c_{n,z}^{\mathsf T}\Sigma_{n,z}^{-1}c_{n,z}\\
 &=\frac{(N_n+1)(N_n+2)\varepsilon_n^2}{S_{n,z}^2}
 \left(\|d_{n,z}\|_2^2-
 \frac{p_{n,z}^2}{N_n+1}\right).
 \end{aligned}
\tag{30}
\]
For \(z,w\in D_n\), the definition of \(H_n\) gives
\(d_{n,z,w}\leq H_n\). Hence
\[
 \|d_{n,z}\|_2^2\leq N_nH_n^2,\qquad
 S_{n,z}\geq N_n+1-\widehat\delta_n.
\]
Once \(n\) is large enough that the latter lower bound is positive,
\[
 \max_{z\in D_n}\tau_{n,z}(0)^2
 \leq
 \frac{(N_n+1)(N_n+2)}{(N_n+1-\widehat\delta_n)^2}
 \frac{\widehat\delta_n^2}{N_n}.
\tag{31}
\]
Under (17), the first limit in (18) makes the right side tend to zero
uniformly in \(z\). This proves the second limit in (18) and then (19).
More generally, on the branch \(\widehat\delta_n<T_n\), replace
\(\widehat\delta_n\) by \(T_n\) in the right side of (31). This is valid
for large \(n\), because (13) gives \(T_n<N_n+1\) and that right side is
increasing in \(\widehat\delta_n\) on \([0,N_n+1)\). Equations (13) and
(31) then show that (19) holds uniformly over every admissible low-branch
amplitude for all sufficiently large \(n\).

Apply accepted fact `876a152563efe052` to the affine map \(s\equiv0\).
Equation (19) says that its covariance-near set is all of \(D_n\), and the
fiberwise half-metronoid inclusion in that fact gives (20). The set \(D_n\)
has affine rank \(n\), since it contains \(0,e_1,\ldots,e_n\). The two
capacity conclusions of the same accepted fact give
\[
 G(C_n)\geq\frac12\sum_{z\in D_n}a_{n,z}=\frac12W_n,
\]
\[
 R_{\rm sel}(C_n)\geq
 2^{n-n}\frac{\gamma_{N_n}}2
 \sum_{z\in D_n}a_{n,z}
 =\frac{\gamma_{N_n}}2W_n.
\]
Finally, \(\log(1+1/N_n)<1/N_n\) implies
\(\gamma_{N_n}=(1+1/N_n)^{-N_n}>e^{-1}\), proving (21).

Fix an exact minimum-unmatched centroid matching \(q_n\) from accepted fact
`be359f8a6c628483`. If it is the zero matching, (22) holds by the
stated empty-matching convention. Otherwise, in the notation of accepted
fact `6496cb3b0fd44f9d`, put
\[
 \mathcal K_{n,z}:=\mathsf M_{a_{n,z}/2}((C_n)_z),\qquad
 L_e:=\frac12(\mathcal K_{n,z}+\mathcal K_{n,z'})
 \quad(e=\{z,z'\}).
\]
Equation (20) gives \(0\in\mathcal K_{n,z}\) for every endpoint, and hence
\(0\in L_e\) for every matching edge. The affine map \(s\equiv0\) therefore
hits every edge body. The exact characterization in accepted fact
`6496cb3b0fd44f9d` gives \(\Delta_{C_n}(q_n)=0\). The zero dual field
is feasible and has dual value zero, so it is a dual optimizer. Its gauge
load is zero, while every gauge load is nonnegative. Thus the minimum load
among dual optimizers is zero, and every load-minimal dual optimizer has
\(\Omega_n=0\). This proves (22) and completes the dichotomy.

## External sources

none
