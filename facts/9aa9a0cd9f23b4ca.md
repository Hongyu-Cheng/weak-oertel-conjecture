---
fact_id: 9aa9a0cd9f23b4ca
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-affine-log-normalization-derivatives
depends_on: []
verifier_run: b3b65686be6e536c
target_match: null
---

## Source

- [108870e8f9aac2e9](../candidates/108870e8f9aac2e9.json), §7, (10)–(13).

## Statement

Let $V_z(t)>0$ be differentiable volumes indexed by finitely many bases, $M=\sum_z V_z$, $w_z=V_z/M$, and $E_z(t)>0$ differentiable fixed-mark energies. Suppose $V_z'=-D_z$, $D=\sum_zD_z$, $E_z'=-C_z$ at the old pair. Let $\ell_z>0$ be affine samples with $\sum_z w_z\log\ell_z=0$, $A_\ell=\sum_z w_z\ell_z$ and $f_z=(\ell_zE_z/M)^{1/N}$ with $N=d+1$. Rescaling a fixed affine shape by a common factor to preserve the logarithmic constraint gives
$$
s:=\ell_z'/\ell_z=M^{-1}\sum_zD_z\log\ell_z,\qquad
f_z'/f_z=(-C_z/E_z+D/M+s)/N,\qquad
A_\ell'=M^{-1}\sum_zD_z[A_\ell(1+\log\ell_z)-\ell_z].
$$
At a fixed body the geometrically normalized affine path with raw values $\ell_z+t\phi(z)$ instead gives $\ell_z'=\phi(z)-\ell_zA_\phi$ and $A_\ell'=\sum_z w_z\phi(z)-A_\ell A_\phi$, with $A_\phi=\sum_z w_z\phi(z)/\ell_z$.

## Proof

The quotient rule gives $w_z'=(w_zD-D_z)/M$. For the common rescaling the logarithmic derivative of every $\ell_z$ is $s$. Differentiating the constraint gives $0=\sum_z w_z'\log\ell_z+s$, and the old constraint cancels the $D$ term, giving the first formula. Taking the logarithmic derivative of $f_z$ yields the second. The product rule on $A_\ell$ gives $A_\ell'=M^{-1}\sum_z D_z(A_\ell-\ell_z)+sA_\ell$, which is the third formula.

At fixed body the normalization factor is $\exp[-\sum_z w_z\log(\ell_z+t\phi(z))]$. Its derivative at zero is $-A_\phi$ and its value there is one. The product rule gives the two fixed-body formulas.
