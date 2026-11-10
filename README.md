# Weak Oertel conjecture fact graph

This repository holds the weak Oertel conjecture fact graph of Hongyu Cheng and Phillip Kerger. The weak Oertel conjecture concerns mixed-integer halfspace depth. Each accepted fact in the graph is a statement with a proof, linked to the accepted facts it uses and to the verification record that approved it. The repository also holds Lean formalizations and exact-arithmetic checkers for several counterexamples to stronger forms of the conjecture, among them the counterexample to Oertel's conjecture in the paper *A counterexample to Oertel's conjecture on mixed-integer centerpoints*.

The results were obtained mainly by AI research agents, and each accepted proof was approved by a language-model verifier. Every accepted fact carries the assurance label `LLM-verified`, which does not assert human review or formal verification. The [AI disclosure](#ai-disclosure) gives the details.

## The problem

Let $n,d$ be positive integers, let $C\subset\mathbb R^{n+d}$ be a convex body, and let $S=C\cap(\mathbb Z^n\times\mathbb R^d)$. The mixed-integer volume $\mathcal H_d$ of a subset of $S$ is the sum of the $d$-dimensional volumes of its fibers over the integer points. The halfspace depth $h_S(\mathbf y)$ of a point $\mathbf y\in S$ is the infimum of $\mathcal H_d(S\cap H)$ over the closed halfspaces $H$ that contain $\mathbf y$. The [problem statement](problem_statement.md) asks to prove or disprove the weak Oertel conjecture:

> There is an absolute constant $c_0\in(0,1/e)$ such that every convex body $C$ with $S\neq\varnothing$ has a point $\mathbf y^\star\in S$ with $h_S(\mathbf y^\star)\ge c_0\,2^{-n}\,\mathcal H_d(S)$.

The constant may not depend on $n$, $d$ or $C$. Two stronger statements specify the constant. Oertel's conjecture, stated by Oertel and by Basu and Oertel as a mixed-integer analogue of Grünbaum's inequality, uses $\Gamma_d=(d/(d+1))^d$ in place of $c_0$; below it is also called the sharp bound, and the [dimension-17 paper](output/pdf/oertel-sharp-dimension-17.pdf) gives the references. The $1/e$ bound takes $c_0=1/e$. Since $\Gamma_d>1/e$, a counterexample to the $1/e$ bound also refutes Oertel's conjecture.

## Current state

The weak Oertel conjecture is open: no accepted fact proves or refutes it. All of the following are accepted facts with the `LLM-verified` label.

- The weak statement holds for $n=1$ and for $n=2$, for every $d$ ([`758103b1282d6b91`](facts/758103b1282d6b91.md), [`daef2580cdfec07b`](facts/daef2580cdfec07b.md)), and for every $n$ when $d\le199$, with $c_0=3/64000$ ([`245739007817b92a`](facts/245739007817b92a.md)). Further restricted cases are listed under [Highlights](#highlights).
- The full statement would follow from one aggregate inequality in a reduced setting ([`933fa3d0a98a6ce9`](facts/933fa3d0a98a6ce9.md)). The graph does not prove that inequality, and the corresponding subgoal is open.
- The counterexamples in the table refute Oertel's conjecture and the $1/e$ bound. None of them refutes the weak statement, which allows any smaller positive constant.
- Most of the remaining facts are lemmas, partial reductions, and counterexamples to proposed intermediate steps. A counterexample to an intermediate step refutes that step, not the conjecture.

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

The counterexample with $(n,d)=(12,5)$ is the subject of the paper *A counterexample to Oertel's conjecture on mixed-integer centerpoints* by Hongyu Cheng and Phillip Kerger. The [PDF](output/pdf/oertel-sharp-dimension-17.pdf), its LaTeX source, and the replay commands are linked from [research/sharp-dimension-17](research/sharp-dimension-17/README.md).

## Assurance

Accepted facts. Every file in `facts/` carries `LLM-verified`: a language-model verifier approved its proof, and the approving record is under `verifications/`. The label does not assert human review or formal verification.

Lean. The five counterexamples with an entry in the Lean column have Lean 4 proofs built against a pinned mathlib, and their axiom audits allow only `propext`, `Classical.choice`, and `Quot.sound`. The Lean statements measure a body by counting measure on the integer bases times Lebesgue measure on the fibers. They do not separately formalize the identification with the Hausdorff measure of the problem statement or the rationality of the polytopes. The [Lean guide](lean/README.md) states the scope of each theorem.

Exact checkers. The Python checkers in the table use exact rational arithmetic to replay the finite counts and strict inequalities of each construction. The geometric arguments are in the proofs, not in the checkers.

Graph checker. `scripts/check_graph.py` checks the records (dependency closure, acyclicity, metadata, hashes, and private-path patterns). It does not check mathematics.

## AI disclosure

The results in this graph were obtained mainly by AI research agents, using a fact graph system similar to [Danus](https://arxiv.org/abs/2607.06447). The `author` field of every candidate is an agent label, not a person: `research-agent`, `PK-research-agent` for the work Phillip Kerger contributed, or `dimension-reduction-research-agent`. The graph contains 3,503 accepted facts. A separate model verification run approved each of them, so each carries the label `LLM-verified`, which does not assert human review or formal verification. Where a verification record names the model, it is almost always GPT-6.1 Sol, with GPT-6 Astra or ChatGPT in a few runs; the records made before 30 October 2026 name no model. The review reports under [`reviews/`](reviews) and the pull request reviews describe further model reviews of particular results. Hongyu Cheng and Phillip Kerger maintain the repository and take full responsibility for it.

The repository began as an export of a local research workspace. Prompts, handoffs, source archives, working memory, personal configuration, and copies of reference papers were left out, and agent identifiers were normalized. Some records still name files from that workspace, for example under `.math-prover/`, or refer to unshared research notes. Those files are not in the repository; the [contribution rules](CONTRIBUTING.md) treat them as provenance, not as premises.

## Where to start

1. The [problem statement](problem_statement.md).
2. The [dimension-17 paper](output/pdf/oertel-sharp-dimension-17.pdf) for a complete counterexample to Oertel's conjecture.
3. The [highlights](#highlights) for the main positive results and reductions. From any fact, follow the IDs in its `depends_on` field.
4. The [fact index](INDEX.md), which lists every accepted fact with its depth, kind, and subgoal identifier.
5. For the research notes that Phillip Kerger contributed on 6 November 2026, the [intake crosswalk](assets/pk-nov6/CROSSWALK.md) and the [contribution guide](contributions-PK-nov-6-merge.md).

The problem statement and the fact files use `\(...\)` and `\[...\]` math delimiters, which GitHub may show as source. A Markdown viewer with LaTeX support displays them.

## Highlights

The names are curated labels stored in [`assets/highlights.json`](assets/highlights.json). Depth is the length of the longest dependency chain below a fact, starting at zero. An arrow means that the lower fact depends on the upper one, possibly through facts not shown.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/highlights-dark.svg">
  <img alt="Highlighted facts arranged by dependency depth" src="assets/highlights-light.svg">
</picture>

| depth | name | fact |
|---|---|---|
| 0 | S-Helly centerpoint baseline | [`6d6fcf377e68c79c`](facts/6d6fcf377e68c79c.md) |
| 0 | Mixed-continuous comparison | [`4cfd86cd551df9e7`](facts/4cfd86cd551df9e7.md) |
| 0 | Metronoid–Grünbaum sandwich | [`6769574fc1bd9f8d`](facts/6769574fc1bd9f8d.md) |
| 1 | n = 1, every d | [`758103b1282d6b91`](facts/758103b1282d6b91.md) |
| 1 | Cheng-Basu linear threshold | [`1787daa1dbe3fbb4`](facts/1787daa1dbe3fbb4.md) |
| 1 | O((n+d)/n) threshold | [`0790372855abe672`](facts/0790372855abe672.md) |
| 2 | Stronger O((n+d)/n) threshold | [`95b9903fc7036094`](facts/95b9903fc7036094.md) |
| 3 | n = 2, every d | [`daef2580cdfec07b`](facts/daef2580cdfec07b.md) |
| 3 | Cube mass threshold | [`daf10421c94b79ba`](facts/daf10421c94b79ba.md) |
| 3 | n = 3 mechanism separation | [`c168604b1c021192`](facts/c168604b1c021192.md) |
| 4 | Bounded support rank | [`9468b734966ba646`](facts/9468b734966ba646.md) |
| 4 | Parity-midpoint residual depth | [`be359f8a6c628483`](facts/be359f8a6c628483.md) |
| 5 | Fixed-normal simplex class | [`cb0d20326035a553`](facts/cb0d20326035a553.md) |
| 7 | Product-cloud reduction | [`6b09aae189415c70`](facts/6b09aae189415c70.md) |
| 9 | Every n, d ≤ 199 | [`245739007817b92a`](facts/245739007817b92a.md) |
| 23 | Stopped-rank 311 closure | [`a728f1f23a4398e9`](facts/a728f1f23a4398e9.md) |
| 26 | Conditional closure (AGG) | [`933fa3d0a98a6ce9`](facts/933fa3d0a98a6ce9.md) |

For $d\ge2$, the [sharp complete-parity-core theorem](facts/3fad02a5aa48ae2a.md) proves the sharp bound for bodies with a positive-volume fiber over one point of each parity class, provided that all other fibers together have volume at most $\rho_d$ times the smallest of those fibers. The constant $\rho_d>0$ depends only on $d$.

## Repository layout

- `facts/<id>.md`: accepted statements and proofs, with `depends_on` and the approving verification run.
- `candidates/<id>.json`: every submitted statement and proof, whether accepted, pending, or rejected. Its status is in `state.json`.
- `verifications/<run>.json`: verifier verdicts, gaps, and explanations.
- `state.json`: the ledger of facts, candidates, verification runs, and research subgoals.
- [`INDEX.md`](INDEX.md): the list of accepted facts.
- [`lean/`](lean): the Lean 4 project.
- [`research/`](research): proofs, checkers, and review notes for the counterexamples of total dimension 17, 19, 187, and 1387.
- [`assets/pk-nov6/`](assets/pk-nov6): the research notes that Phillip Kerger contributed on 6 November 2026, kept as pending candidates, with the crosswalk that records how each claim in them was handled and the supporting computations.
- [`assets/pk-continuation-2026-11/`](assets/pk-continuation-2026-11): later notes and checkers from the same line of work, including the $d=23$, $n=76$, and $n=52$ constructions.
- [`reviews/`](reviews): reports of model reviews and integration checks, with their evidence files.
- [`output/pdf/`](output/pdf): the dimension-17 paper and two write-ups.
- [`scripts/`](scripts): the graph and intake checkers and a generator for a Lean certificate.

At the time of writing, `state.json` records 3,503 accepted facts (1,721 theorems, 1,035 lemmas, and 747 counterexamples), 4,794 candidates (of which 1,236 are pending and 55 rejected), and 3,563 verification runs. The longest dependency chain has depth 44. `python3 scripts/check_graph.py` prints the current counts. All but one pending candidate are composite research notes kept under their original status. For the 1,217 notes of the 6 November intake, the crosswalk records how every claim in them was handled, and 2,217 of those claims entered the graph as separate facts. The ledger also records 3,782 research subgoals. Their statuses are a record of the research process, not a reviewed list of open problems.

## Rerun the checks

The graph and intake checkers use only the Python standard library. They check records, hashes, links, and finite regressions, not proofs.

```sh
python3 scripts/check_graph.py
python3 scripts/check_pk_nov6.py
python3 scripts/check_pk_crosswalk.py
python3 scripts/check_pk_parity_core.py
```

The exact checkers for the counterexamples also use only the standard library. For example:

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

## History

The first 1,235 accepted facts came from the initial export; the last of them was accepted on 29 October 2026. Every later fact, including the counterexamples and the intake of the 6 November notes, was added through a merged pull request. The pull request descriptions and the reports under [`reviews/`](reviews) and [`research/sharp-dimension-187/`](research/sharp-dimension-187) record what each one added and how it was reviewed. Counts quoted there describe the graph at that time.

[CONTRIBUTING.md](CONTRIBUTING.md) explains how to propose a result or a correction. The layout follows [oertel-three-slices-2d](https://github.com/Hongyu-Cheng/oertel-three-slices-2d).
