# PK intake pilot proof review

The initial screen covered 36 notes across six topics in 6 minutes 8 seconds of parallel work. It produced 248 preliminary claim records. This report covers the independent proof review of the first three priority notes. The [crosswalk](../../assets/pk-nov6/CROSSWALK.md) gives the scope and disposition of each extracted claim.

| Source | Admitted result | Independent review |
| --- | --- | --- |
| [edf02845b3275e8c](../../candidates/edf02845b3275e8c.json), opening theorem and §§1–5 | [Simultaneous convex realization of feasible base moments](../../facts/bf1ea1ab1ca2de45.md) | [668486706f3f3873](../../verifications/668486706f3f3873.json) |
| [edf02845b3275e8c](../../candidates/edf02845b3275e8c.json), §6 | [Sharp partition bound of $2^n$ cells with integer-base centroids](../../facts/e4ec84652a3059bf.md) | [77998a37e8887dbf](../../verifications/77998a37e8887dbf.json) |
| [d0cb383fd9782a9f](../../candidates/d0cb383fd9782a9f.json), §§1–5 | [Local-depth obstruction for integer-centroid partitions](../../facts/22eef9feeab3bd98.md) | [cb111ce07ec9f56f](../../verifications/cb111ce07ec9f56f.json) |
| [0ce014ed03a74ef8](../../candidates/0ce014ed03a74ef8.json), §§1 and 3 | [Planar projective shadow of an actual convex body with depth below $4/9$](../../facts/12d2b1d23b041387.md) | [63770f6dbbf7c90a](../../verifications/63770f6dbbf7c90a.json) |

The simultaneous realization gives convex affine-score cells with prescribed mass and base moments, including relative boundary targets. The [previous binary cap result](../../facts/a8cfba4caf85ff82.md) realizes the two-label full-fiber case with an integral target for one label. The [previous finite allocation result](../../facts/57c57a5fe0d4d1cc.md) already proves the lattice count and empty centroid hull for globally extendable tables. Its count argument uses only positive weights and complete support. The sharp partition theorem includes that finite argument and uses the new realization theorem to produce actual convex cells.

For the local-depth obstruction, the reviewer derived both possible interval traces and recomputed the obstructing cap mass. Its normalized mass within the relevant piece is $7/16$. For the shadow obstruction, the reviewer checked [the applicable three-fiber hull lemma](../../facts/2a8c2bc6d7992c5e.md) and independently clipped the two slope triangles using rational arithmetic. The closed caps cover the whole slope plane. The largest has mass $458329/1040000$, with gap $35039/9360000$ below $4/9$.

## Time and rework

Separate GPT-6.1 Sol high reviewers examined the four frozen proofs. The recorded window from first review start to last final approval was 4 minutes 31 seconds.

| Result | Normalization | First proof review | Revision check |
| --- | ---: | ---: | ---: |
| Affine-score realization | 4m 57s for both partition claims | 2m 37s | 15s |
| Sharp count | Included above | 3m 09s | 21s |
| Local-depth obstruction | 2m 49s | 2m 08s | — |
| Projective-shadow obstruction | 3m 25s | 2m 45s | — |

The sharp-count reviewer first recorded the time after an initial read, so its intervals omit that read. The four initial proof audits account for 10 minutes 39 seconds of recorded reviewer time. Two punctuation edits required checking the revised hashes, accounting for another 36 seconds. All four proofs passed the initial review and no mathematical changes were requested after submission.

The first three notes yielded four admissions, three verified reuse mappings, and seven supporting entries. At this checkpoint, 33 of the 36 screened notes still had provisional dispositions. The graph, intake archive, crosswalk, and existing parity-core checks passed. The new admissions carry the repository's `LLM-verified` assurance.
