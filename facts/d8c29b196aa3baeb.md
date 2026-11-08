---
fact_id: d8c29b196aa3baeb
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-tied-log-scale
depends_on: ["4bf4936eff4d698d"]
verifier_run: 0a27b1bdc8c79cf3
target_match: null
---

## Source

- [26455afca6af9c16](../candidates/26455afca6af9c16.json), §4 first paragraph.

## Statement

Assume the compact-sublevel setting and the fixed-scale value inequalities $\beta_*+c_1\varepsilon\le\inf_K\beta_\varepsilon(K)\le\beta_*+C\varepsilon$ of the body-tied attainment theorem. Choose $0<\bar\varepsilon\le1$ in their range. For all sufficiently small $\tau>0$, the infimum of $\beta_\varepsilon(K)-\tau\log\varepsilon$ over all positive compatible families on $P$ and $0<\varepsilon\le\bar\varepsilon$ is attained. Every minimizer is an attained body minimum at its scale, with $\varepsilon/\tau$ bounded above and below by positive constants independent of small $\tau$, hence with interior scale.

## Proof

The trial $\varepsilon=\tau/C$ and the upper value bound give infimum at most $\beta_*+\tau-\tau\log(\tau/C)$, which is below $b$ for sufficiently small $\tau$. Since $\bar\varepsilon\le1$, the penalty is nonnegative and a minimizing sequence is in the original strict sublevel. At fixed $\tau$ the penalty tends to infinity as $\varepsilon\downarrow0$, whereas $\beta_\varepsilon\ge0$. Joint continuity on the compact representative class at scales bounded away from zero gives attainment. For a minimizer write $\varepsilon=\tau s$. The lower value bound and the trial imply $c_1 s-\log s\le1+\log C$, so $s$ stays in a fixed compact subinterval of $(0,\infty)$, giving the interior assertion. A minimizer must minimize the body value at its chosen scale since its penalty then is constant.
