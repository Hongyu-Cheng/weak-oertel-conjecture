# Weak Oertel conjecture fact graph

This repository contains the fact graph of Hongyu Cheng and Phillip Kerger on the weak Oertel conjecture about mixed-integer halfspace depth. Each fact is a statement with a proof, linked to the facts it uses and to the verification record that approved it. The conjecture is still open, but the graph refutes its two stronger forms, Oertel's conjecture and the $1/e$ bound, and several of these counterexamples also have Lean proofs and exact-arithmetic checkers. The counterexample to Oertel's conjecture with $(n,d)=(12,5)$ is the subject of the paper

> Hongyu Cheng and Phillip Kerger, [*A counterexample to Oertel's conjecture on mixed-integer centerpoints*](output/pdf/oertel-sharp-dimension-17.pdf), manuscript, 2026.

## The problem

Let $n,d$ be positive integers, let $C\subset\mathbb R^{n+d}$ be a convex body, and let $S=C\cap(\mathbb Z^n\times\mathbb R^d)$. The mixed-integer volume $\mathcal H_d$ of a subset of $S$ is the sum of the $d$-dimensional volumes of its fibers over the integer points. The halfspace depth $h_S(\mathbf y)$ of a point $\mathbf y\in S$ is the infimum of $\mathcal H_d(S\cap H)$ over the closed halfspaces $H$ that contain $\mathbf y$. The [problem statement](problem_statement.md) asks to prove or disprove the weak Oertel conjecture:

> There is an absolute constant $c_0\in(0,1/e)$ such that every convex body $C$ with $S\neq\varnothing$ has a point $\mathbf y^\star\in S$ with $h_S(\mathbf y^\star)\ge c_0\,2^{-n}\,\mathcal H_d(S)$.

The constant may not depend on $n$, $d$ or $C$. Two stronger statements specify the constant. Oertel's conjecture, stated by Oertel and by Basu and Oertel as a mixed-integer analogue of Grünbaum's inequality, uses $\Gamma_d=(d/(d+1))^d$ in place of $c_0$; below it is also called the sharp bound, and the [dimension-17 paper](output/pdf/oertel-sharp-dimension-17.pdf) gives the references. The $1/e$ bound takes $c_0=1/e$. Since $\Gamma_d>1/e$, a counterexample to the $1/e$ bound also refutes Oertel's conjecture.

## Current state

The weak Oertel conjecture is open: no fact proves or refutes it. The graph contains the following results.

- The weak statement holds for $n=1$ and for $n=2$, for every $d$ ([`758103b1282d6b91`](facts/758103b1282d6b91.md), [`daef2580cdfec07b`](facts/daef2580cdfec07b.md)), and for every $n$ when $d\le199$, with $c_0=3/64000$ ([`245739007817b92a`](facts/245739007817b92a.md)). Further restricted cases are listed under [Highlights](#highlights).
- The full statement would follow from one aggregate inequality in a reduced setting ([`933fa3d0a98a6ce9`](facts/933fa3d0a98a6ce9.md)). The graph does not prove that inequality, and the corresponding subgoal is open.
- The counterexamples in the table refute Oertel's conjecture and the $1/e$ bound. None of them refutes the weak statement, which allows any smaller positive constant.

| Bound refuted | $n$ | $d$ | Fact | Proof or write-up | Exact checker | Lean proof |
| --- | ---: | ---: | --- | --- | --- | --- |
| sharp | 12 | 5 | [`ecbacdec2c429376`](facts/ecbacdec2c429376.md) | [paper](output/pdf/oertel-sharp-dimension-17.pdf), [proof](research/sharp-dimension-17/README.md) | [check.py](research/sharp-dimension-17/check.py) | [`Selector17`](lean/SharpOC/Selector17Counterexample.lean) |
| sharp | 14 | 5 | [`a39d93bee9bf2fe9`](facts/a39d93bee9bf2fe9.md) | [proof](research/sharp-dimension-19/README.md) | [check.py](research/sharp-dimension-19/check.py) | [`Selector`](lean/SharpOC/SelectorCounterexample.lean) |
| sharp | 153, 132, 129 | 34, 82, 104 | [`ad3e63c52f083457`](facts/ad3e63c52f083457.md) | [proof](research/sharp-dimension-187/README.md) | [checker](research/sharp-dimension-187/sharp-triangle-join-pareto-check.py) | none |
| sharp | $3\cdot10^{92}$ | 23 | [`022a26fa5001480a`](facts/022a26fa5001480a.md) | [proof](assets/pk-continuation-2026-11/direct-rational-sharp-oc-counterexample.md) | [checker](assets/pk-continuation-2026-11/check_direct_rational_sharp_oc_counterexample.py) | [`Counterexample`](lean/SharpOC/Counterexample.lean) |
| $1/e$ | 209 | 1178 | [`a02d398c0677c03a`](facts/a02d398c0677c03a.md) | [guide](research/one-over-e-dimension-1387/README.md) | [check.py](research/one-over-e-dimension-1387/check.py) | [`Witness1387`](lean/SharpOC/Witness1387/DepthBound.lean) |
| $1/e$ | 52 | 1,345,226,000,000,000,003 | [`cbe1f4518f7088a7`](facts/cbe1f4518f7088a7.md) | [construction](research/sharp-dimension-187/compress-simplex-factor.md) | [checker](research/sharp-dimension-187/compress-certificate.py) | none |
| $1/e$ | 52 | $274784+2^{61}$ | [`df488edae05a1702`](facts/df488edae05a1702.md) | [write-up](output/pdf/oertel-52-integer-variables.pdf) | [checker](assets/pk-continuation-2026-11/check_integer_dimension_52.py) | none |
| $1/e$ | 76 | $1372131+2^{93}$ | [`a5291bca09ba4b1e`](facts/a5291bca09ba4b1e.md) | [write-up](output/pdf/oertel-one-over-e-counterexample.pdf) | [checker](assets/pk-continuation-2026-11/check_integer_dimension_76.py) | [`BoxCounterexample`](lean/SharpOC/BoxMeasure.lean) |

In this graph, the smallest total dimension $n+d$ of a counterexample is 17 for Oertel's conjecture and 1387 for the $1/e$ bound. The [support-count theorem](facts/30b899ae9d94a523.md) shows that a body with $F$ positive-volume fibers has maximum normalized depth at least $\Gamma_d/F$. A $1/e$ counterexample therefore needs $F/2^n>e\Gamma_d$, so $d$ must be large when $F$ is close to $2^n$.

The LaTeX source of the paper and the commands that replay its counterexample are in [research/sharp-dimension-17](research/sharp-dimension-17/README.md).

## How the graph was produced

The research ran in Codex with GPT-6 Astra at Ultra reasoning effort, using a fact graph workflow similar to [Danus](https://arxiv.org/abs/2607.06447). Hongyu Cheng and Phillip Kerger ran it the same way. A worker model proposes a candidate (a lemma, theorem, or counterexample) for a registered subgoal. A separate verifier model run reads the candidate together with the accepted facts it cites and returns `APPROVED` or `REJECTED`. Only approved candidates become facts, and a candidate may cite only accepted facts. The research notes that Phillip Kerger contributed on 6 November 2026 were split into individual claims, and the 2,217 claims that became facts were verified by GPT-6.1 Sol.

Every fact carries the label `LLM-verified`, meaning that a model approved its proof. The five counterexamples with an entry in the Lean column of the table are also proved in Lean 4, and the [Lean guide](lean/README.md) states what each theorem covers. The paper and the two write-ups in [`output/pdf/`](output/pdf) present results from the graph, and Hongyu Cheng and Phillip Kerger take full responsibility for them.

## Size

| | count |
|---|---|
| accepted facts | 3,503 (1,721 theorems, 1,035 lemmas, 747 counterexamples) |
| pending candidates | 1,236 (1,235 research notes, 1 counterexample) |
| rejected candidates | 55 |
| registered subgoals | 3,782 (3,443 closed, 273 open, 66 abandoned) |
| largest depth in the graph | 44 |

The depth of a fact is the length of the longest dependency chain below it. The pending research notes are the notes Phillip Kerger contributed, kept whole; the [intake crosswalk](assets/pk-nov6/CROSSWALK.md) records how each claim in the notes of 6 November was handled. Most facts are lemmas, partial reductions, and counterexamples to proposed intermediate steps; such a counterexample refutes that step, not the conjecture.

## Highlights

The 21 facts below are the main results, reductions, and tools in the graph. Their short names are ours and are stored in [`assets/highlights.json`](assets/highlights.json). In the picture a fact sits in the row of its depth (depth 0 takes two rows), and an arrow means that the lower fact uses the upper one, possibly through facts that are not shown.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/highlights-dark.svg">
  <img alt="The 21 highlighted facts arranged by depth, with an arrow from each fact to the facts that use it" src="assets/highlights-light.svg">
</picture>

| depth | name | fact | statement |
|---|---|---|---|
| 0 | Support-count bound | [`30b899ae9d94a523`](facts/30b899ae9d94a523.md) | A body with $F$ positive-volume fibers has maximum normalized depth at least $\Gamma_d/F$ |
| 0 | 1/e fails at n + d = 1387 | [`a02d398c0677c03a`](facts/a02d398c0677c03a.md) | A counterexample to the $1/e$ bound with $(n,d)=(209,1178)$ |
| 0 | Oertel fails at n + d = 17 | [`ecbacdec2c429376`](facts/ecbacdec2c429376.md) | A counterexample to Oertel's conjecture with $(n,d)=(12,5)$ |
| 0 | Mixed-continuous comparison | [`4cfd86cd551df9e7`](facts/4cfd86cd551df9e7.md) | Mixed-integer and ordinary volume agree within factors $(1\pm\frac{1}{2k})^{n+d}$ when the projection contains a translate of $k[-1,1]^n$ with $k>1/2$ |
| 0 | Metronoid–Grünbaum sandwich | [`6769574fc1bd9f8d`](facts/6769574fc1bd9f8d.md) | Every point of depth $m$ lies in the metronoid of mass $m$, and every point of that metronoid has depth at least $\Gamma_d m$ |
| 0 | S-Helly centerpoint baseline | [`6d6fcf377e68c79c`](facts/6d6fcf377e68c79c.md) | The S-Helly centerpoint theorem: some point has depth at least $\mathcal H_d(S)/(2^n(d+1))$ |
| 1 | Cheng-Basu linear threshold | [`1787daa1dbe3fbb4`](facts/1787daa1dbe3fbb4.md) | If the projection of $C$ contains a translate of $k[-1,1]^n$ with $k\ge\frac{3e}{2}(n+d)$, some point has depth at least $(\frac1e-\frac{3(n+d)}{2k})\mathcal H_d(S)$ |
| 1 | O((n+d)/n) threshold | [`0790372855abe672`](facts/0790372855abe672.md) | A translate of $k[-1,1]^n$ in the projection with $k\ge\frac72\cdot\frac{n+d}{n}$ gives depth $\Gamma_{n+d}2^{-n}\mathcal H_d(S)$ |
| 1 | n = 1, every d | [`758103b1282d6b91`](facts/758103b1282d6b91.md) | The case $n=1$ for every continuous dimension $d$ |
| 2 | Sharp parity-core theorem | [`3fad02a5aa48ae2a`](facts/3fad02a5aa48ae2a.md) | The sharp bound when little mass lies outside a complete parity core |
| 2 | Stronger O((n+d)/n) threshold | [`95b9903fc7036094`](facts/95b9903fc7036094.md) | A translate of $k[-1,1]^n$ in the projection with $k\ge\frac{57}{14}\cdot\frac{n+d}{n}$ gives depth $\Gamma_d2^{-n}\mathcal H_d(S)$ |
| 3 | Cube mass threshold | [`daf10421c94b79ba`](facts/daf10421c94b79ba.md) | The factor $2^{-n}$ in the metronoid lifting lemma is sharp |
| 3 | n = 3 mechanism separation | [`c168604b1c021192`](facts/c168604b1c021192.md) | An $n=3$ family separating the accepted score mechanisms |
| 3 | n = 2, every d | [`daef2580cdfec07b`](facts/daef2580cdfec07b.md) | The case $n=2$ for every continuous dimension $d$ |
| 4 | Bounded support rank | [`9468b734966ba646`](facts/9468b734966ba646.md) | If the positive-volume fibers span an affine space of dimension at most $R$, the conjecture holds with a constant depending only on $R$ |
| 4 | Parity-midpoint residual depth | [`be359f8a6c628483`](facts/be359f8a6c628483.md) | Dominated-measure residual depth and parity midpoints |
| 5 | Fixed-normal simplex class | [`cb0d20326035a553`](facts/cb0d20326035a553.md) | Rigidity and depth for fixed-normal simplex fibers |
| 7 | Product-cloud reduction | [`6b09aae189415c70`](facts/6b09aae189415c70.md) | Canonical labeled product-cloud reduction |
| 9 | Every n, d ≤ 199 | [`245739007817b92a`](facts/245739007817b92a.md) | The conjecture for every $n$ and every $d\le199$, with $c_0=3/64000$ |
| 23 | Stopped-rank 311 closure | [`a728f1f23a4398e9`](facts/a728f1f23a4398e9.md) | A least-dimensional counterexample cannot be parity-concentrated |
| 26 | Conditional closure (AGG) | [`933fa3d0a98a6ce9`](facts/933fa3d0a98a6ce9.md) | Conditional closure: an aggregate ledger bound implies the conjecture |

For $d\ge2$, the [sharp complete-parity-core theorem](facts/3fad02a5aa48ae2a.md) proves the sharp bound for bodies with a positive-volume fiber over one point of each parity class, provided that all other fibers together have volume at most $\rho_d$ times the smallest of those fibers. The constant $\rho_d>0$ depends only on $d$.

## Repository layout

- `facts/<id>.md`: accepted statements and proofs, with `depends_on` and the approving verification run.
- `candidates/<id>.json`: every submitted statement and proof, whether accepted, pending, or rejected. Its status is in `state.json`.
- `verifications/<run>.json`: verifier verdicts, gaps, and explanations.
- `state.json`: the ledger of facts, candidates, verification runs, and research subgoals.
- [`INDEX.md`](INDEX.md): the list of accepted facts with their depth, kind, and subgoal.
- [`lean/`](lean): the Lean 4 project.
- [`research/`](research): proofs, checkers, and review notes for the counterexamples of total dimension 17, 19, 187, and 1387.
- [`assets/pk-nov6/`](assets/pk-nov6): the research notes that Phillip Kerger contributed on 6 November 2026, with the crosswalk and the supporting computations. [`contributions-PK-nov-6-merge.md`](contributions-PK-nov-6-merge.md) summarizes the results that came from them.
- [`assets/pk-continuation-2026-11/`](assets/pk-continuation-2026-11): later notes and checkers from the same line of work, including the $d=23$, $n=76$, and $n=52$ constructions.
- [`reviews/`](reviews): reports of model reviews and integration checks for the pull requests that added facts after the initial export, with their evidence files.
- [`output/pdf/`](output/pdf): the paper and the two write-ups.
- [`scripts/`](scripts): the graph and intake checkers and a generator for a Lean certificate.

The `author` field of a fact or candidate holds an agent label; `PK-research-agent` marks the work Phillip Kerger contributed. Prompts, handoffs, working memory, and copies of reference papers from the original research workspace are not included. Some records still name those files, for example under `.math-prover/`; they are provenance, not premises. [CONTRIBUTING.md](CONTRIBUTING.md) explains how to propose a result or a correction.

The problem statement and the fact files write mathematics with `\(...\)` and `\[...\]` delimiters, which GitHub's preview does not typeset. Use the Raw view or a Markdown viewer with LaTeX support.

## Rerun the checks

The graph and intake checkers use only the Python standard library. They check records, hashes, links, and finite regressions, not proofs.

```sh
python3 scripts/check_graph.py
python3 scripts/check_pk_nov6.py
python3 scripts/check_pk_crosswalk.py
python3 scripts/check_pk_parity_core.py
```

The exact checkers for the counterexamples, also standard-library only, replay the finite counts and strict inequalities of each construction in rational arithmetic. For example:

```sh
python3 -B research/sharp-dimension-17/check.py
python3 -B research/sharp-dimension-19/check.py
python3 -I -B research/one-over-e-dimension-1387/check.py
```

The other checkers are linked in the table, and [research/sharp-dimension-187](research/sharp-dimension-187/README.md) lists its own. Some checkers rewrite the JSON certificate stored beside them, so run them in a clean checkout and compare with `git diff`. The [Lean guide](lean/README.md#reproduce-the-verification) gives the build and axiom-audit commands.

## How to cite

To cite the fact graph, use the metadata in [CITATION.cff](CITATION.cff), which GitHub offers under "Cite this repository":

> Hongyu Cheng and Phillip Kerger. Weak Oertel conjecture fact graph. https://github.com/Hongyu-Cheng/weak-oertel-conjecture, 2026.

To cite the counterexample with $(n,d)=(12,5)$, cite the paper:

> Hongyu Cheng and Phillip Kerger. A counterexample to Oertel's conjecture on mixed-integer centerpoints. Manuscript, 2026.

## License

Copyright 2026 Hongyu Cheng and Phillip Kerger. The code is released under the [MIT License](LICENSE-CODE). It consists of every `.py` and `.lean` file, the other files under `lean/` except its Markdown files (`lake-manifest.json`, `lean-toolchain`, and `.gitignore`), the root `.gitignore` and `.gitattributes`, and `assets/pk-nov6/requirements-computations.txt`. Every other file except the two license texts is released under [CC BY 4.0](LICENSE). This covers the problem statement, the facts, candidates, and verification records, `state.json`, all Markdown and LaTeX documents, the PDFs, figures, certificates, logs, and data files. Published results that the proofs quote or cite remain the work of their authors.
