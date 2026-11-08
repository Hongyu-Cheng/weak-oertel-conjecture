---
fact_id: 7ecdb7713aca3e1c
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-endpoint-trimming-means-of-log-concave-sequence
depends_on: []
verifier_run: adc873799ce94f53
target_match: null
---

## Source

- [9afb6a8708a420d7](../candidates/9afb6a8708a420d7.json), 9afb6a8708a420d7:02 §5, endpoint-trimming means, (4).

## Statement

Let $w_0,\ldots,w_L$ be positive and log-concave, $L\ge2$. Keep all interior weights and independently allow the endpoint weights at $0,L$ to vary between zero and $w_0,w_L$, respectively. The set of weighted means is the interval with endpoints
$$
m_-=\frac{\sum_{i=0}^{L-1}i w_i}{\sum_{i=0}^{L-1}w_i},\qquad
m_+=\frac{\sum_{i=1}^{L}i w_i}{\sum_{i=1}^{L}w_i}.
$$
Its length $m_+-m_-$ is at most one, and the bound is attained for constant weights.

## Proof

Adding weight at $0$ lowers the mean and adding weight at $L$ raises it. Thus the extremes occur at the displayed endpoint choices, and the continuous image of the connected rectangle of endpoint weights contains every intermediate value. The denominator stays positive because at least one interior weight is fixed and positive.

Compare the means of the laws with weights $w_i$ and $w_{i+1}$ on $i=0,\ldots,L-1$. They are $m_-$ and $m_+-1$, respectively. If $A=\sum_{i=0}^{L-1}w_i$ and $B=\sum_{i=0}^{L-1}w_{i+1}$, the second mean minus the first, multiplied by $AB$, equals
$$
\sum_{0\le i<j\le L-1}(j-i)(w_{j+1}w_i-w_{i+1}w_j)\le0,
$$
since $w_{i+1}/w_i$ is nonincreasing. This gives $m_+-m_-\le1$. Constant weights make all the summands zero.
