# Related work and attribution

The scientific question is the [known-first-column discrimination problem](../science/model.md), with separate hard total budgets for forward and inverse queries to one fixed unknown unitary. The contribution is the matching large-dimension law $`F(K+1)+K^2\asymp\epsilon^{-2}`$, its adaptive record-potential proof, and the dimension-dependent upper bound obtained by synthesizing only calibration inverses.

Hidden-basis loading, collective Dicke sensitivity, measurement discrimination, universal inversion, quantum program reuse, and the broader study of correlated sample/query resources are established ingredients and themes. The comparisons below identify which source interfaces are used and which conclusions are derived here. They are a bounded theorem-level comparison, not an exhaustive certification of priority.

| Ingredient or nearby result | Role in this project |
|---|---|
| WCC known-state discrimination | Same decision promise and forward-only benchmark |
| Ma–Huang strong path recording | Imported simulator; the control/history extension and task-specific potential are proved here |
| Ioannou–Mosca hidden-basis computation | Preparation of symmetric fixed-occupation states from unknown orthogonal basis states |
| Puchała et al. measurement discrimination | Established inverse-only endpoint |
| QURA universal inversion | Ordinary-forward implementation of the calibration inverses |
| Chen inverse-free estimation | Dimension-dependent comparison; broader amplitude-estimation conjecture remains distinct |
| Belovs–Rosmanis approximate counting | Multiple correlated sample/oracle resources; generator and inverse share one budget |
| Akshima et al. permutation inversion | Correlated quantum advice with continued access to the same oracle |
| Yang–Renner–Chiribella programming | Genuine quantum program recycling under a different decoder interface |

## WCC2026

Emma Wang, Joseph Carolan and Andrew M. Childs, **On State Distinguishing Without Inverse Queries**, arXiv:2610.05389v1, 4 October 2026. [Versioned text](https://arxiv.org/html/2610.05389v1).

Section 1.1 defines the two-known-state promise used here. The paper establishes the forward-only quadratic regime in sufficiently large dimension; Section 4 develops its completion-based lower-bound method. Section 1.3 lists an $`O(d^{3/2}/\epsilon)`$ dimension-dependent upper bound and asks about improved joint dimension/separation tradeoffs.

The [native-forward corollary](../science/forward_only.md) improves that stated upper bound for the same promise to $`O(\min\{\epsilon^{-2},d/\epsilon\})`$. The separate inverse-budget law is a further resource question. The permutation family in WCC does not remain hard with even one inverse query: the [classical calibration example](../science/resource_tradeoffs.md#a-readable-calibration-can-be-reused-classically) derives this observation explicitly. WCC's continuous-time and Zeno formulations use different access interfaces from the hard total-call model adopted here.

## TW2026

Ewin Tang and John Wright, **Amplitude amplification and estimation require inverses**, arXiv:2507.23787v2, 23 April 2026. [Versioned text](https://arxiv.org/html/2507.23787v2).

This is a direct algorithmic predecessor for the importance of inverse access in amplitude amplification and estimation. The present project does not introduce the inverse-free obstruction or identify its binary promise with general amplitude estimation. It resolves separately charged total query directions for the more specific known-state problem. Dimension-dependent comparisons here use the later bound explicitly stated in WCC and Chen's estimation result, rather than treating every earlier conjecture as current.

## IYM2026

Natsuto Isogai, Satoshi Yoshida and Mio Murao, **Advantage of Sample Complexity in Quantum PAC Learning Requires Inverse Access to State-Preparation Unitaries**, arXiv:2609.38403v1. [Versioned text](https://arxiv.org/html/2609.38403v1).

Theorem 3.3 simulates forward access by copies of the prepared state in its specified Haar-completion model, with explicit dimension-dependent error. This gives another closely related forward-only endpoint. Inverse-generated information about the completion is correlated with later oracle calls; conditioning on that information changes the distribution used in a forward-only copy-simulation statement. The [mixed-query proof](../science/mixed_query_lower_bound.md) therefore controls the retained completion records throughout the experiment instead of applying that theorem after calibration.

## MH2025

Fermi Ma and Hsin-Yuan Huang, **How to Construct Random Unitaries**, arXiv:2410.10116v3, 21 May 2025. [Versioned HTML](https://arxiv.org/html/2410.10116v3), [versioned PDF](https://arxiv.org/pdf/2410.10116v3).

The imported objects are the left/right record maps of Definition 25, the strong path-recording oracle of Definition 26, and the mixed-query simulation estimate in Theorem 8, Eq. (9.5). The source's mixed-query error, $`9T(T+1)n^{-1/8}`$, is used once for each hypothesis. Its stronger forward-only error is not substituted into a mixed-query argument.

[Haar simulation](../science/haar_simulation.md) gives the source-to-lemma derivation needed for coherent skipping and classically adaptive directions with retained histories. That extension is identified as a derivation here, not a statement quoted from the source. [The lower bound](../science/mixed_query_lower_bound.md) then introduces the projection forbidding one left-record output and proves the exact number identity that yields the direction-sensitive resource law.

## IM2010

Lawrence M. Ioannou and Michele Mosca, **Universal quantum computation in a hidden basis**, arXiv:0810.2780v3. [Versioned text](https://arxiv.org/html/0810.2780v3).

Theorem 1 and its symmetric fixed-weight preparation establish the hidden-basis primitive: given copies of orthogonal basis states, suitable known operations can prepare states in a phase-invariant fixed-occupation sector without a classical description of that basis. The [probe construction](../science/dicke_calibration.md) uses this principle, with [explicit routing and streaming implementations](../science/implementations.md).

The calibrated state is obtained here through a charged inverse query. The full result additionally needs a finite-angle decision guarantee and a converse for arbitrary adaptive strategies. Neither preparing a Dicke state nor evaluating its collective variance alone is presented as the new resource theorem.

## PPKKO2021

Zbigniew Puchała, Łukasz Pawela, Aleksandra Krawiec, Ryszard Kukulski and Michał Oszmaniec, **Multiple-shot and unambiguous discrimination of von Neumann measurements**, *Quantum* **5**, 425 (2021). [Published paper](https://quantum-journal.org/papers/q-2021-04-06-425/), [versioned preprint](https://arxiv.org/pdf/1810.05122v4).

Applying $`W^\dagger`$ and then measuring the reference subspace implements the projective measurement associated with the prepared state. Multiple-shot discrimination of the two known measurements supplies the inverse-only $`O(\epsilon^{-1})`$ endpoint. The [implementation page](../science/implementations.md) gives an elementary sequential phase-memory construction for the present promise.

Optimality within a measurement-only interface is not itself a lower bound against every coherent use of $`W^\dagger`$. The latter endpoint lower bound follows here from the full mixed-query theorem in its dimension range. The endpoint construction remains established prior work.

## QURA

Yu-Ao Chen, Yin Mo, Yingjian Liu, Lei Zhang and Xin Wang, **Quantum Algorithm for Reversing Unknown Unitary Evolutions**, arXiv:2403.04704v3, 9 October 2025. [Versioned PDF including Appendix A](https://arxiv.org/pdf/2403.04704v3), [HTML](https://arxiv.org/html/2403.04704v3).

Theorem 1 supplies deterministic universal inversion with $`L_d=d\lceil\pi/[2\arcsin(1/d)]\rceil-1`$ forward queries. Appendix A, including Eqs. (A.15), (A.16) and (A.25), specifies the ordinary-call encoder/decoder interface and returned ancillas. The $`d-1`$ calls used for each complex conjugation are included in $`L_d`$.

The [forward-only proof](../science/forward_only.md) checks the $`U(d)`$ global phase and uses inversion only for calibration. Its $`d/\epsilon`$ consequence is derived by combining that source construction with the calibrated-probe tradeoff and an integer allocation. The source's parallel-layer complexity is not used as an elementary-gate estimate.

## Chen2025

Kean Chen, **Inverse-free quantum state estimation with Heisenberg scaling**, arXiv:2510.25750v1, 29 October 2025. [Versioned text](https://arxiv.org/html/2510.25750v1).

Corollary 1.5 gives $`O(\min\{d^{3/2}/\epsilon,\epsilon^{-2}\})`$ queries for general amplitude estimation. Section 1.4 conjectures $`\Theta(\min\{d/\epsilon,\epsilon^{-2}\})`$ for that broader problem.

The upper bound here attains the latter expression for two known candidate output vectors. It does not supply the general amplitude-estimation algorithm in that conjecture, nor an optimal lower bound at every fixed dimension. The distinction is part of the [theorem statement](../science/forward_only.md), not merely a bibliographic qualification.

## BR2024

Aleksandrs Belovs and Ansis Rosmanis, **Tight Quantum Lower Bound for Approximate Counting with Quantum States**, arXiv:2002.06879v2, 7 May 2024. [Versioned text](https://arxiv.org/html/2002.06879v2).

Theorem 1.1 and Table 1 analyze approximate subset counting with copies of a uniform subset state, membership queries, generating-or-inverse queries, and reflection queries. Copies and continued oracle access refer to the same unknown subset. Their mixed conditions include products of generator or reflection queries with square roots of copy resources.

This is a substantive predecessor for multiple correlated quantum resources. Its generator and inverse share one query budget, and its unknown-subset counting promise differs from two known columns with an arbitrary unitary completion. No reduction from that evaluated theorem to the separate $`F,K`$ law is used here. Its general adversary framework is not confused with an already evaluated bound for this promise.

## ABCGY2025

Akshima, Tyler Besselman, Kai-Min Chung, Siyao Guo and Tzu-Yi Yang, **Tight Quantum Time-Space Tradeoffs for Permutation Inversion**, arXiv:2510.12112v1, 14 October 2025. [Versioned text](https://arxiv.org/html/2510.12112v1).

Theorem 1 allows unbounded preprocessing access to a permutation, retains an $`S`$-qubit advice state, and then gives a random challenge with $`T`$ further queries to the same permutation. It bounds average success by $`O((ST+T^2)/N)`$. The oracle is a reversible classical-function evaluation oracle. The result genuinely permits advice correlated with continued oracle access.

Our resource $`K`$ counts interleaved inverse calls with no workspace cap, rather than advice width after unbounded preprocessing. Substituting $`S\approx K\log d`$ and $`T=F`$ into that theorem yields a different polynomial and does not constitute a reduction. The product-plus-square shape is an important algebraic precedent; the directional law requires the task-specific [record potential](../science/mixed_query_lower_bound.md).

## YRC2020

Yuxiang Yang, Renato Renner and Giulio Chiribella, **Optimal universal programming of unitary gates**, *Physical Review Letters* **125**, 210501 (2020); arXiv:2007.10363v3. [Versioned text](https://arxiv.org/html/2007.10363v3).

The universal processor is independent of the unknown unitary and receives its information through a program state. Theorem 1 and Appendix A use genuine program recycling to obtain the optimal program-size dependence. Repeated usefulness of a quantum program is therefore established prior work.

The present sensing algorithm continues to query the unknown $`W`$. Absorbing those calls into a supposedly unitary-independent decoder changes the programming model, and binary discrimination does not implement a universal channel on arbitrary inputs. This is why a program-size lower bound does not replace the mixed-query analysis.

## ML2025

Iman Marvian and Seth Lloyd, **Efficient Quantum Emulation of Unknown Unitaries**, *PRX Quantum* **6**, 030346 (2025). [Published paper](https://journals.aps.org/prxquantum/pdf/10.1103/PRXQuantum.6.030346).

Proposition 1 characterizes when input/output sample states determine coherent action on their supported subspace: the input density operators must generate its full operator algebra. The two orthogonal projectors used as calibration tokens here generate only a diagonal algebra on their span. They therefore do not satisfy that coherent-emulation hypothesis by themselves.

This observation is an interface comparison, not a converse for all inverse-query strategies, which can acquire additional coherent information. The Dicke experiment needs a fixed-occupation decision experiment and continued correlated oracle access, rather than universal emulation from samples alone.

## Attribution boundaries

The [model page](../science/model.md) assigns each theorem an exact scope and an authoritative proof. The bibliography fixes source versions so that numbered statements can be located. The direction-sensitive potential, finite constructive decision guarantee and synthesized-calibration consequence are derived in this repository; their imported ingredients retain the attributions above. Numerical reproduction checks are evidence for their enumerated identities, not evidence that a literature search is exhaustive or that an analytical theorem has been externally certified.
