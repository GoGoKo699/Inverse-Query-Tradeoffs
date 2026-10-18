# Thirty milestones for inverse-query tradeoffs

How does a limited supply of inverse calls change the number of forward calls needed to distinguish two known possible outputs of an unknown unitary? These thirty milestones connect the objects in that question to the constructions, converse, and resource consequences in this repository.

The allocation follows the scientific structure. **M01–M10 are background/preliminaries:** states and operations lead to a complete access model and the methods for analyzing it. **M11–M30 are narrative/innovation:** calibration leads to a finite decision algorithm; a separate record-potential argument supplies the converse; their combination explains the resource frontier and the finite-dimensional forward-only consequence. Each phase ends by joining its components into the larger question.

The single educational anchor is Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, **17 April 2025** ([official notes](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), [author's source page](https://www.cs.umd.edu/~amchilds/qa/)). The [Childs bridge](CHILDS_BRIDGE.md) supplies the translations and project-specific intermediate explanations. The anchor links below identify conceptual preparation. Primary research ingredients and project proofs retain their separate attribution in the linked scientific pages and [related-work account](../references/RELATED_WORK.md).

The map is defined by the scientific project and is common to every reader, including LLMs. Every entry records a shared understanding target, its earlier dependencies, its role in the scientific story, and exact source pointers. The full statements and derivations have their authoritative homes in `science/`; this map connects them without creating a second proof account.

## Route through the project

| Phase | Milestones | Conceptual connection |
|---|---|---|
| Background/preliminaries | [M01](#m01)–[M03](#m03) | From state vectors and unitary completion to the resources charged for accessing the unknown operation. |
| Background/preliminaries | [M04](#m04)–[M07](#m07) | From coherent amplification and circuit control to composite probes and operational error bounds. |
| Background/preliminaries | [M08](#m08)–[M10](#m10) | From correlations in a fixed random oracle to the proof methods and complete decision model. |
| Narrative/innovation | [M11](#m11)–[M17](#m17) | From inverse calibration to collective sensing, finite success, concrete implementations, and the inverse-only endpoint. |
| Narrative/innovation | [M18](#m18)–[M25](#m25) | From strong Haar records to a direction-sensitive potential and the general adaptive converse. |
| Narrative/innovation | [M26](#m26)–[M30](#m30) | From the matched frontier to priced inverse access, forward-only synthesis, and the contribution's full scope. |

## Phase I — Background/preliminaries

### M01 — States, rotations and measurements

<a id="m01"></a>

**Central question.** What physical distinction is encoded by the two candidate state vectors?

**Understanding target.** Interpret $`|0\rangle`$ and $`|1\rangle`$ as known orthogonal states in a register of dimension $`d`$. Read $`c|0\rangle+\epsilon|1\rangle`$ as a normalized state with $`c=\sqrt{1-\epsilon^2}`$ and rotation angle $`\alpha=\arcsin\epsilon`$. Distinguish the amplitude $`\epsilon`$ from the probability $`\epsilon^2`$ of finding the register orthogonal to $`|0\rangle`$.

**Dependencies and story role.** No earlier milestone. This supplies the local states, signal size, and measurement used throughout both proof chains.

**Conceptual connection.** A geometric separation between state vectors becomes the probability of a classical event; repeated oracle interrogation must make that event informative enough for a decision.

**Source pointers.** Anchor: [Childs §1.1][childs-data]. Project: [the known-state promise](../science/model.md#the-known-state-promise) and [the measurement conventions](../science/dicke_calibration.md#model-and-conventions).

### M02 — State preparation and unitary completion

<a id="m02"></a>

**Central question.** How much of a unitary is specified by the state it prepares on one input?

**Understanding target.** Explain why knowing $`W|0\rangle`$ fixes one column while leaving the other columns subject only to unitarity. Interpret $`W=R_bV_b`$, where $`V_b`$ fixes $`|0\rangle`$, and distinguish the state-preparation action from the full forward and adjoint transformations. The unused columns can affect later coherent queries.

**Dependencies and story role.** Uses [M01](#m01). It moves from one prepared state to the unknown operation that generates it, exposing the resource question.

**Conceptual connection.** Reversibility is a property of the mathematical operation. Access to its inverse is a separate property of the oracle interface.

**Source pointers.** Anchor: [Childs §1.2][childs-circuits]. Project: [the known-state promise and completion decomposition](../science/model.md#the-known-state-promise).

### M03 — Physical query costs and other resources

<a id="m03"></a>

**Central question.** Which operations are counted when an algorithm uses an unknown device?

**Understanding target.** Separate the forward count $`F`$, inverse count $`K`$, known-gate work, live quantum memory, and final classical output. Explain why simultaneous calls through several oracle ports cost several queries, and why an oracle-count improvement alone does not establish a runtime improvement. Initial states and advice correlated with the oracle cannot be supplied for free.

**Dependencies and story role.** Uses [M02](#m02). It attaches an operational cost to the available transformations before any speedup is discussed.

**Conceptual connection.** The query model isolates access to unknown information; explicit circuit and memory accounting reconnects that abstraction to an implementation.

**Source pointers.** Anchor: [Childs Ch. 21][childs-queries] and [§1.2][childs-circuits]. Project: [query and control contract](../science/model.md#query-and-control-contract) and [resource summary](../science/implementations.md#resource-summary).

### M04 — Coherent amplification and its access assumptions

<a id="m04"></a>

**Central question.** What access makes coherent amplification possible?

**Understanding target.** Explain the difference between repeating a preparation and implementing a coherent transformation that accumulates its signal. Identify the reflections or walk operations required by an amplification construction and ask how they are supplied. Childs presents amplitude amplification through quantum walk search; the translation to a general state-preparation oracle requires an explicit access argument.

**Dependencies and story role.** Uses [M01](#m01)–[M03](#m03). It connects familiar quantum amplification to the missing inverse resource in this problem.

**Conceptual connection.** A quadratic improvement concerns an algorithm together with its available operations. The present project makes the number of uses in each direction part of that statement.

**Source pointers.** Anchor: [Childs §19.3][childs-amplification]. Project: [model and exact results](../science/model.md), with the notation and access translation in the [Childs bridge](CHILDS_BRIDGE.md#amplification).

### M05 — Classical histories and coherent controls

<a id="m05"></a>

**Central question.** How can an adaptive quantum experiment have a precise resource budget?

**Understanding target.** Distinguish a measured classical history that selects the next query direction from a coherent control that skips the selected direction. Explain why every classical history must respect the hard $`F,K`$ caps and why a coherent skip still charges the full physical invocation. Retaining an immutable copy of each measured outcome permits purification without changing these meanings.

**Dependencies and story role.** Uses [M02](#m02)–[M03](#m03). It specifies the allowed control structure that both the algorithms and the converse must respect.

**Conceptual connection.** Deferring measurement is a representation of a computation, not permission to replace physical query budgets by probabilities of coherent branches.

**Source pointers.** Anchor: [Childs Ch. 21][childs-queries]. Project: [query and control contract](../science/model.md#query-and-control-contract) and [recovery of the physical adaptive model](../science/haar_simulation.md#7-recovering-the-physical-adaptive-model-and-the-block-1u). The latter supplies the history-purification details.

### M06 — Composite probes and clean reversible routing

<a id="m06"></a>

**Central question.** What changes when several quantum registers are arranged coherently?

**Understanding target.** Distinguish a tensor product, a coherent superposition of arrangements, and a classical mixture of arrangements. Explain how reversible labels can route states without learning their amplitudes, and why those labels must be erased to leave the intended probe. A known test separating $`|0\rangle`$ from its orthogonal subspace can support that erasure.

**Dependencies and story role.** Uses [M01](#m01)–[M03](#m03). It builds the circuit language for using a fixed stock of unknown states collectively.

**Conceptual connection.** Coherence can concern the positions of unknown states even when their internal amplitudes are unavailable as classical data.

**Source pointers.** Anchor: [Childs §1.1][childs-data] and [§1.4][childs-reversible]. Project: [known occupation-register preparation](../science/implementations.md#prepare-a-known-occupation-register) and [routing with label erasure](../science/implementations.md#route-the-unknown-states-and-erase-the-labels).

### M07 — Distinguishability and composable error

<a id="m07"></a>

**Central question.** How does a bound on quantum states limit the reliability of a classical decision?

**Understanding target.** Interpret half trace distance $`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$ and the equal-prior binary-success bound $`(1+D)/2`$. Distinguish operator, vector, and trace norms. Explain why common physical processing cannot increase distinguishability and why a projected simulator's lost norm must remain part of the comparison instead of being removed by renormalization.

**Dependencies and story role.** Uses [M01](#m01), [M03](#m03), and [M05](#m05). It connects mathematical error estimates to the actual output requirement.

**Conceptual connection.** The same norm bookkeeping controls both implementation error in an upper algorithm and replacement error in a lower-bound proof.

**Source pointers.** Anchor: [Childs §2.1][childs-errors] for composition of circuit errors. Project: [norm conventions](../science/haar_simulation.md#norm-conventions), [the subnormalized comparison, Eq. (20)](../science/mixed_query_lower_bound.md#7-comparing-the-forward-operations), and [the binary-success step](../science/mixed_query_lower_bound.md#9-completing-the-theorem-and-evaluating-the-constants). These project pages supply the additional state-discrimination machinery.

### M08 — Fixed random oracles and hard ensembles

<a id="m08"></a>

**Central question.** Why does the way an oracle is randomized matter for a lower bound?

**Understanding target.** Explain the difference between sampling one completion and reusing it, and sampling a fresh operation at each call. Information obtained early stays correlated with later uses of the same oracle. A worst-case guarantee over every completion implies success on any chosen supported ensemble; it therefore permits a lower proof to select a shared Haar completion for its two hypotheses.

**Dependencies and story role.** Uses [M02](#m02), [M05](#m05), and [M07](#m07). It enlarges the analysis from individual calls to a whole experiment with retained information.

**Conceptual connection.** A random-oracle ensemble is a tool for proving difficulty against algorithms that continue to exploit the correlations they have acquired.

**Source pointers.** Anchor: [Childs Ch. 26][childs-recording]. Project: [the lower ensemble and its quantifiers](../science/mixed_query_lower_bound.md#1-model-and-theorem) and [the completion distinction in the promise](../science/model.md#the-known-state-promise).

### M09 — Progress bounds and compressed records

<a id="m09"></a>

**Central question.** How can a lower proof control every allowed algorithm without describing each one?

**Understanding target.** Explain the strategy of following a progress quantity, bounding its change per query, and relating its final value to decision success. Interpret an inaccessible oracle-record register as part of a proof representation. Distinguish Childs's exact random-function recording construction from the separate simulation theorem needed for mixed queries to a Haar unitary.

**Dependencies and story role.** Uses [M05](#m05), [M07](#m07), and [M08](#m08). It joins control, distinguishability, and oracle correlations into a general proof method.

**Conceptual connection.** The adversary viewpoint supplies progress accounting; compressed records make a useful quantity accessible to the analyst while keeping it hidden from the algorithm.

**Source pointers.** Anchor: [Childs Chs. 23][childs-adversary] and [26][childs-recording]. Project: [the imported Haar-simulation interface](../science/mixed_query_lower_bound.md#2-imported-haar-simulation-result). Its proof is developed separately in [Haar simulation](../science/haar_simulation.md).

### M10 — The complete operational question

<a id="m10"></a>

**Central question.** What exactly must an attainable algorithm and a matching converse establish?

**Understanding target.** Assemble the known pair of outputs, arbitrary fixed completion, ordinary forward and inverse access, hard caps on every classical history, charged coherent skips, and one-bit success requirement into one problem. Use $`0<\epsilon\le1/4`$ for the main mixed-query result. State why an upper algorithm must work for independently arbitrary completions, while a lower proof may use a correlated hard ensemble. Keep known computation and workspace distinct from query cost.

**Dependencies and story role.** Integrates [M01](#m01)–[M09](#m09). This closes the background phase with the framework that makes the two proof chains comparable.

**Conceptual connection.** Algorithm design and impossibility arguments answer the same question only when their promises, costs, and success quantifiers agree.

**Source pointers.** Anchor: [Childs Ch. 21][childs-queries], with [§19.3][childs-amplification] as motivation. Project: [Model and exact results](../science/model.md), especially [the query contract](../science/model.md#query-and-control-contract).

## Phase II — Narrative/innovation

### M11 — Inverse calibration without tomography

<a id="m11"></a>

**Central question.** What useful information does one inverse invocation provide?

**Understanding target.** Follow $`W_b^\dagger|1\rangle`$ and the known zero-state measurement. Under the null it produces $`|x_b\rangle=V_b^\dagger|1\rangle`$; under the alternative it either certifies the answer or leaves exactly that unknown orthogonal state. After at most $`K`$ calls, every branch has either decided or retained $`K`$ exact copies. No retry allowance or classical reconstruction is needed.

**Dependencies and story role.** Uses [M01](#m01), [M02](#m02), and [M10](#m10). It identifies the local resource from which the constructive chain grows.

**Conceptual connection.** Inverse access supplies usable quantum calibration correlated with the future oracle, even when it supplies no readable description of the completion.

**Source pointers.** Anchor: [Childs §1.2][childs-circuits]. Project: [calibration, Eq. (D3)](../science/dicke_calibration.md#calibration). The [bridge's worked example](CHILDS_BRIDGE.md#worked-example) follows the same experiment.

### M12 — When calibration is a readable classical label

<a id="m12"></a>

**Central question.** Why can one inverse call be much more powerful for a structured completion?

**Understanding target.** For a completion given by a permutation fixing zero, explain how calibration reveals the label $`x=\pi^{-1}(1)`$ unless it has already certified the alternative. The known transposition applied before each forward call makes $`W_bS_{1x}`$ equal the signal rotation on the known plane. The label can be reused to obtain $`O(\epsilon^{-1})`$ forward cost with one inverse.

**Dependencies and story role.** Uses [M04](#m04), [M08](#m08), and [M11](#m11). It identifies which completion property a general converse must account for.

**Conceptual connection.** A measured basis label supports reusable classical control; an arbitrary calibrated vector supports a different kind of resource. Neither no-cloning alone nor a forward-only endpoint proves their mixed-query cost.

**Source pointers.** Anchor: [Childs §19.3][childs-amplification] and [Ch. 21][childs-queries]. Project: [the readable-calibration construction](../science/resource_tradeoffs.md#a-readable-calibration-can-be-reused-classically).

### M13 — Distributing a fixed stock of unknown states

<a id="m13"></a>

**Central question.** How can the algorithm spread $`K`$ unknown states across $`F`$ positions coherently?

**Understanding target.** For $`0\le K\le F`$, interpret $`|D_{F,K}(x)\rangle`$ as the equal coherent superposition of arrangements containing exactly $`K`$ copies of $`x`$ and $`F-K`$ zeros. Explain how known occupation labels, reversible permutations, and zero tests prepare it from the supplied stock with clean ancillas. Every term has the same number of unknown states, so their phase contributes only an overall phase.

**Dependencies and story role.** Uses [M06](#m06) and [M11](#m11). It turns local calibration into a collective probe using an established hidden-basis preparation primitive.

**Conceptual connection.** The enhancement comes from coherent arrangements of a conserved stock of states, with no cloning, tomography, or extra oracle calls during loading.

**Source pointers.** Anchor: [Childs §1.4][childs-reversible]. Project: [loading and interrogation, Eq. (D4)](../science/dicke_calibration.md#loading-and-forward-interrogation), [the routing circuit](../science/implementations.md#wide-loading-with-reversible-sorting), and [Ioannou–Mosca attribution](../references/RELATED_WORK.md#im2010).

### M14 — Collective rotation and Dicke enhancement

<a id="m14"></a>

**Central question.** Why do the distributed calibration states increase the probe's response?

**Understanding target.** Explain the cancellation $`V_b|x_b\rangle=|1\rangle`$: after the forward batch, the unknown completion leaves a known Dicke state acted on by a collective rotation. Interpret its generator $`G=\sum_jY_j`$ and second moment $`v=F+2K(F-K)`$. Identify the role of coherent correlations and the restriction of the accompanying optimality statement to fixed-occupation parallel probes.

**Dependencies and story role.** Uses [M01](#m01), [M06](#m06), and [M13](#m13). It identifies the amplification mechanism before converting that mechanism into a finite success guarantee.

**Conceptual connection.** Calibration transforms an unknown-unitary problem into a controlled collective-rotation experiment. The scale $`F(K+1)`$ becomes visible in its response.

**Source pointers.** Anchor: [Childs §19.3][childs-amplification] for coherent signal amplification. Project: [completion cancellation, Eq. (D5)](../science/dicke_calibration.md#loading-and-forward-interrogation), [the second moment](../science/dicke_calibration.md#second-and-fourth-moments), and [restricted parallel optimality](../science/dicke_calibration.md#optimality-within-a-fixed-occupation-parallel-batch).

### M15 — Finite-angle success and rounded budgets

<a id="m15"></a>

**Central question.** How does the collective response become a uniformly reliable binary algorithm?

**Understanding target.** Explain why a large variance alone is insufficient at a finite angle. Follow how the fourth-moment bound and global cosine inequalities control the probability of retaining weight $`K`$. For integer $`0\le K\le\lfloor1/(2\alpha)\rfloor`$, the budget choice ensures $`3/2\le\alpha^2v<2`$, giving alternative success at least $`735/1024`$. Include conclusive calibration outcomes and retain zero null false positives.

**Dependencies and story role.** Uses [M07](#m07), [M11](#m11), and [M14](#m14). It closes the calibrated-probe correctness argument with actual integer resources and a finite decision probability.

**Conceptual connection.** A collective sensitivity calculation becomes an algorithmic theorem only after measurement, finite angle, branch probabilities, and rounding are controlled together.

**Source pointers.** Anchor: [Childs Ch. 21][childs-queries] for bounded-error query claims. Project: [finite-angle proof](../science/dicke_calibration.md#finite-angle-success-proof), [rounded budgets](../science/dicke_calibration.md#checking-the-rounded-budgets), and [the finite upper theorem](../science/dicke_calibration.md#finite-upper-bound).

### M16 — Wide and streaming implementations

<a id="m16"></a>

**Central question.** What gate and memory choices implement the same calibrated decision experiment?

**Understanding target.** Compare the wide circuit's $`F`$ data registers and reversible sorting history with the streaming circuit's $`K`$-register coherent reservoir and one emitted register. Explain why immediate output measurement preserves the statistics while measuring the reservoir count would change them. Include the wide comparator-history memory, streaming $`FK`$-scale routing work, exact boundary occupations, and separately budgeted loading error.

**Dependencies and story role.** Uses [M03](#m03), [M05](#m05), [M07](#m07), and [M13](#m13)–[M15](#m15). It makes the constructive theorem operational beyond query counts.

**Conceptual connection.** Equivalent oracle statistics can have different gate/memory costs. Keeping the reservoir count coherent preserves the resource responsible for the enhancement.

**Source pointers.** Anchor: [Childs §1.4][childs-reversible] and [§2.1][childs-errors]. Project: [resource summary](../science/implementations.md#resource-summary), [wide loading](../science/implementations.md#wide-loading-with-reversible-sorting), [streaming reservoir](../science/implementations.md#streaming-with-a-coherent-reservoir), and [loading precision](../science/implementations.md#loading-precision).

### M17 — The inverse-only phase endpoint

<a id="m17"></a>

**Central question.** How can inverse access alone determine the promised output state?

**Understanding target.** Explain how an inverse followed by the known zero test implements a measurement associated with the prepared state. In the explicit sequential circuit, either measurement outcome produces the same signal-dependent phase on a memory qubit after known feedforward. Repetition gives alternative probability $`\sin^2(q\alpha)`$ and a sufficient inverse-only budget $`q=\lceil1/\alpha\rceil`$, with small quantum memory.

**Dependencies and story role.** Uses [M01](#m01), [M02](#m02), [M05](#m05), and [M15](#m15). It completes the constructive range beyond the calibrated-probe budget.

**Conceptual connection.** Coherent phase accumulation can survive a measured probe when both corrected outcomes implement the same memory operation. The endpoint is an established measurement-discrimination ingredient.

**Source pointers.** Anchor: [Childs §1.2][childs-circuits]. Project: [phase-memory construction, Eqs. (I10)–(I12)](../science/implementations.md#inverse-only-phase-accumulation), [endpoint guarantee](../science/dicke_calibration.md#the-inverse-only-endpoint), and [Puchała et al. attribution](../references/RELATED_WORK.md#ppkko2021).

### M18 — Strong left/right Haar records

<a id="m18"></a>

**Central question.** What record representation can follow continued access in both oracle directions?

**Understanding target.** Interpret left and right records as inaccessible multisets of input/output pairs, with size counting multiplicity. Explain the append maps, their adjoints, and the strong path-recording contraction that combines creation and deletion. A query changes total record length by at most one, but inverse access changes the structure of the information that can be retained.

**Dependencies and story role.** Uses [M08](#m08)–[M10](#m10) and the caution from [M12](#m12). It starts the independent converse chain with the actual research-level recording object.

**Conceptual connection.** Childs's random-function records motivate the representation. Ma–Huang's mixed-unitary construction supplies a different object whose contraction and correlation properties the present proof needs.

**Source pointers.** Anchor: [Childs Ch. 26][childs-recording]. Project: [record space and oracle, Eqs. (5)–(6)](../science/mixed_query_lower_bound.md#3-record-space-and-oracle) and [Ma–Huang attribution](../references/RELATED_WORK.md#mh2025).

### M19 — Controlled Haar simulation and its error

<a id="m19"></a>

**Central question.** Why is it legitimate to replace the physical Haar oracle by those records?

**Understanding target.** State the interface of Lemma HS.1: one reused Haar block of power-of-two dimension $`n`$, at most $`T\le n/2`$ physical calls, retained classical histories, and fully charged coherent skips. Explain the role of one common environment transformation, orthogonal control sectors, and support-preserving compression. Its per-hypothesis error is $`9T(T+1)n^{-1/8}`$; simulator outputs remain subnormalized.

**Dependencies and story role.** Uses [M05](#m05), [M07](#m07), [M08](#m08), and [M18](#m18). It establishes the rigorous link between the physical problem and the record analysis.

**Conceptual connection.** An intuitive record model becomes a usable converse ingredient only after its source theorem, control extension, and replacement error match the allowed experiment.

**Source pointers.** Anchor: [Childs Ch. 26][childs-recording] for the recording viewpoint only. Authoritative project proof: [Lemma HS.1 and its derivation](../science/haar_simulation.md#lemma-hs1-controlled-strong-haar-simulation), including [source dependence and dimension range](../science/haar_simulation.md#8-source-dependence-and-dimension-range). This is a source-derived extension, not a theorem attributed to Childs.

### M20 — Projection and charged leakage

<a id="m20"></a>

**Central question.** How can a simpler record process be used without silently discarding useful information?

**Understanding target.** Interpret $`\Gamma`$ as forbidding left records with output label $`1`$, while allowing such right records. The projected record oracle $`C=\Gamma M\Gamma`$ is a contraction whose output states can be subnormalized. Explain why the unique newly appended forbidden pair makes leaking outputs orthogonal even for multiset records, yielding an operator-norm estimate and a total two-hypothesis leakage cost $`4T/\sqrt{n-T}`$.

**Dependencies and story role.** Uses [M07](#m07), [M18](#m18), and [M19](#m19). It isolates the tractable sector and explicitly pays for everything excluded from it.

**Conceptual connection.** A projection is an analytical simplification with a quantified error. Its leakage is separate from Haar simulation, and neither comparison permits renormalizing a favored branch.

**Source pointers.** Anchor: [Childs Ch. 26][childs-recording] and [§2.1][childs-errors]. Project: [the projected oracle](../science/mixed_query_lower_bound.md#4-a-projected-oracle-and-its-exact-number-identity) and [leakage proof, Eqs. (21)–(24)](../science/mixed_query_lower_bound.md#8-leakage-from-the-projected-database).

### M21 — The exact record-number identity

<a id="m21"></a>

**Central question.** Which quantity distinguishes forward consumption from inverse replenishment?

**Understanding target.** Interpret $`N`$ as the number of right records with output label $`1`$ and $`P=|1\rangle\langle1|`$ as a query-register projector. Explain the exact intertwining identity

```math
(N+P)C=CN.
```

It implies that forward output probability on the distinguished state consumes the record potential, while an inverse can replenish it by at most its prequery weight. The potential belongs to the inaccessible proof database.

**Dependencies and story role.** Uses [M18](#m18)–[M20](#m20). It supplies the task-specific local accounting relation that makes a directional converse possible.

**Conceptual connection.** The operator identity connects a hidden record count to an observable query output, while positivity and contractivity turn that connection into cumulative inequalities.

**Source pointers.** Anchor: [Childs Ch. 23][childs-adversary] for progress accounting. Project: [exact identity, Eqs. (7)–(10)](../science/mixed_query_lower_bound.md#4-a-projected-oracle-and-its-exact-number-identity) and [potential inequalities, Eq. (11)](../science/mixed_query_lower_bound.md#5-forward-use-consumes-the-number-potential).

### M22 — Hard-budget accounting across adaptive histories

<a id="m22"></a>

**Central question.** Why does the potential budget remain valid when query directions depend on measurements?

**Understanding target.** Distinguish the weight of histories requesting a physical call from the probability that its coherent control is active. Explain how immutable histories and remaining-budget counters give sums of forward and inverse prequery weights at most $`F`$ and $`K`$, including subnormalized processes. Starting from empty records, the accumulated active forward-output probability is consequently at most $`K`$.

**Dependencies and story role.** Uses [M05](#m05), [M07](#m07), and [M21](#m21). It extends the local identity to the full hard-cap adaptive model.

**Conceptual connection.** Charging each trajectory enforces a global resource bound even when different trajectories call different directions at different times.

**Source pointers.** Anchor: [Childs Chs. 21][childs-queries] and [23][childs-adversary]. Project: [potential consumption](../science/mixed_query_lower_bound.md#5-forward-use-consumes-the-number-potential) and [hard-budget proof, Eqs. (12)–(13)](../science/mixed_query_lower_bound.md#hard-budgets-for-subnormalized-adaptive-histories).

### M23 — Hybridizing ordinal inverse events

<a id="m23"></a>

**Central question.** How can inverse-query error be charged exactly $`K`$ times in an adaptive computation?

**Understanding target.** Explain the hybrid that removes the known rotation from inverse calls while holding all forward operations fixed. Group branches at their first inverse, then second inverse, and so on, keeping halted branches in a permanent done sector. Common contractions between these boundaries give a vector-distance cost at most $`K\sqrt{2(1-c)}`$. A bound on summed query probabilities would not alone bound their summed square roots.

**Dependencies and story role.** Uses [M05](#m05), [M07](#m07), and [M22](#m22). It separates direct inverse discrimination from the remaining forward comparison without losing adaptive budget control.

**Conceptual connection.** The appropriate hybrid parameter is the ordinal occurrence of the paid resource, which can differ from its physical time slot.

**Source pointers.** Anchor: [Childs §2.1][childs-errors] and [Ch. 23][childs-adversary]. Project: [ordinal inverse-event argument, Eqs. (14)–(15)](../science/mixed_query_lower_bound.md#6-removing-the-inverse-rotations).

### M24 — Weighted forward progress

<a id="m24"></a>

**Central question.** How does limited inverse-generated potential constrain all later forward discrimination?

**Understanding target.** Follow the squared-distance comparison between a forward contraction and its rotated version. Explain why the cross terms depend on both physical forward-call weights and selected output probabilities. Cauchy–Schwarz combines their cumulative bounds $`F`$ and $`K`$, producing

```math
\|\Psi_0-\Psi_{\mathrm{hyb}}\|^2
\le 2F(1-c)+4\epsilon\sqrt{FK}.
```

Common inverse operations and known interventions cannot increase this distance.

**Dependencies and story role.** Uses [M07](#m07), [M21](#m21)–[M23](#m23). It turns the record potential into a bound on the entire remaining experiment, irrespective of its chosen probe architecture.

**Conceptual connection.** A large output amplitude at one query is allowed; the lower proof constrains its accumulated usefulness across all forward queries.

**Source pointers.** Anchor: [Childs Ch. 23][childs-adversary]. Project: [rotation comparison, Eqs. (16)–(17)](../science/mixed_query_lower_bound.md#7-comparing-the-forward-operations) and [weighted adaptive comparison, Eqs. (18)–(20)](../science/mixed_query_lower_bound.md#weighted-comparison-for-adaptive-directions).

### M25 — The finite-dimensional mixed-query converse

<a id="m25"></a>

**Central question.** Under what explicit conditions do the preceding comparisons forbid successful discrimination?

**Understanding target.** Assemble the inverse hybrid, weighted forward distance, projection leakage, and two Haar-simulation errors into Theorem MQ.1. For $`n=d-1`$ a power of two and $`T=F+K\le n/2`$, recognize the sufficient condition

```math
n\ge 2T+[432T(T+1)]^8+(96T)^2.
```

In that range, success at least $`2/3`$ requires $`F(K+1)+K^2>10^{-4}\epsilon^{-2}`$. The large threshold is sufficient, not optimal.

**Dependencies and story role.** Integrates [M19](#m19)–[M24](#m24), using the success criterion from [M07](#m07). It closes the general converse chain.

**Conceptual connection.** The restricted record calculation becomes a physical impossibility statement only after all replacement errors fit within the decision-distance gap.

**Source pointers.** Anchor: [Childs Ch. 23][childs-adversary]. Project: [Theorem MQ.1 and Corollary MQ.2](../science/mixed_query_lower_bound.md#1-model-and-theorem), [constant evaluation](../science/mixed_query_lower_bound.md#9-completing-the-theorem-and-evaluating-the-constants), and [meaning and limits](../science/mixed_query_lower_bound.md#10-meaning-and-limits-of-the-bound).

### M26 — The matched resource frontier

<a id="m26"></a>

**Central question.** What do the independent upper and lower chains establish together?

**Understanding target.** Explain the constant-factor frontier $`F(K+1)+K^2\asymp\epsilon^{-2}`$ in the sufficiently large dimension regime. Interpret the no-inverse, intermediate-calibration, and inverse-only ranges using the actual rounded constructions. Distinguish the necessary lower constant from a sufficient upper budget: the frontier is not an exact equality satisfied by every feasible pair.

**Dependencies and story role.** Joins [M15](#m15), [M17](#m17), and [M25](#m25) under the common model of [M10](#m10). This is the global synthesis of the two proof chains.

**Conceptual connection.** The forward-sensing scale $`F(K+1)`$ and inverse-only scale $`K^2`$ account for two ways of acquiring constant decision information.

**Source pointers.** Anchor: [Childs Chs. 21][childs-queries] and [23][childs-adversary]. Project: [meaning of the boundary and its quantified sufficient budgets](../science/resource_tradeoffs.md#meaning-of-the-boundary).

### M27 — Optimizing expensive inverse access

<a id="m27"></a>

**Central question.** How should the algorithm allocate calls when inverse access costs more?

**Understanding target.** For inverse price $`r\ge1`$, explain how the frontier controls total oracle cost $`F+rK`$. Interpret the intermediate allocation $`K\asymp1/(\epsilon\sqrt r)`$, the integer transition to direct sampling, and the optimum $`\Theta(\min\{\sqrt r/\epsilon,\epsilon^{-2}\})`$. The matching lower assertion retains the dimension condition for the budgets being compared.

**Dependencies and story role.** Uses [M03](#m03), [M16](#m16), and [M26](#m26). It converts a two-resource theorem into a concrete allocation rule.

**Conceptual connection.** An inverse need not have the same price as a forward call. Balancing calibration expense against its future benefit turns the resource frontier into an operational choice.

**Source pointers.** Anchor: [Childs Ch. 21][childs-queries]. Project: [expensive inverse access and its integer allocation](../science/resource_tradeoffs.md#expensive-inverse-access), with [implementation costs](../science/implementations.md#resource-summary) charged separately.

### M28 — Exact inverse synthesis and its phase interface

<a id="m28"></a>

**Central question.** Can the inverse price be supplied by a circuit using only forward oracle calls?

**Understanding target.** Interpret QURA's exact cost $`L_d=d\lceil\pi/[2\arcsin(1/d)]\rceil-1=O(d^2)`$ as the price of one synthesized calibration inverse. Explain its ordinary-call interface and returned ancillas. For $`U(d)`$, the synthesis phase is harmless here because calibration uses a fixed-occupation stock of states, with no coherent comparison against skipping the synthesis.

**Dependencies and story role.** Uses [M02](#m02), [M11](#m11), [M13](#m13), and [M27](#m27). It supplies a physical realization of the inverse price and advances toward a native-forward algorithm.

**Conceptual connection.** The abstract weighted cost becomes $`F+L_dK`$ only after the imported inverter's direction, control, phase, and ancilla interfaces match the calibration procedure.

**Source pointers.** Anchor: [Childs §§1.2–1.4][childs-circuits] for circuit composition. Project: [exact ordinary-call inversion](../science/forward_only.md#exact-ordinary-call-inversion), [synthesis only for calibration](../science/forward_only.md#use-synthesis-only-for-calibration), and [QURA attribution](../references/RELATED_WORK.md#qura).

### M29 — The native-forward dimension bound

<a id="m29"></a>

**Central question.** What forward-only improvement follows from synthesizing only the calibration resource?

**Understanding target.** Explain the integer choice $`K=\lfloor1/(2d\epsilon)\rfloor`$ for $`\epsilon\le1/4`$, its transition to zero calibration, and direct sampling for larger separation. Together they give fewer than $`5\min\{\epsilon^{-2},d/\epsilon\}`$ native forward calls for every $`d\ge2`$ and $`0<\epsilon\le1`$. Include reusable inverter ancillas, the chosen wide or streaming loading cost, and a separate synthesis-error budget.

**Dependencies and story role.** Uses [M15](#m15)–[M16](#m16), [M27](#m27), and [M28](#m28). It closes the resource-conversion argument with a uniform, integer-valued all-dimension upper bound.

**Conceptual connection.** A scarce operation can be synthesized only where it prepares the calibration states. This yields a dimension-dependent query consequence without equating oracle count, parallel depth, and known-gate work.

**Source pointers.** Anchor: [Childs Ch. 21][childs-queries] and [§2.1][childs-errors]. Project: [the forward-only theorem](../science/forward_only.md#theorem), [uniform integer allocation](../science/forward_only.md#integer-allocation-and-the-uniform-constant), and [ancillas, known gates and precision](../science/forward_only.md#ancillas-known-gates-and-precision).

### M30 — The complete contribution and its boundaries

<a id="m30"></a>

**Central question.** What does the complete result establish, and which evidence supports each part?

**Understanding target.** Integrate the mixed-query frontier, its arbitrary-completion upper algorithm and large-dimension adaptive converse, weighted inverse costs, and the all-dimension native-forward upper bound. Locate the established loading, simulation, measurement-discrimination, and inversion ingredients separately from the derived resource law. Explain why the known-pair decision result does not settle general amplitude estimation or finite-dimensional optimality, and why finite circuit checks do not verify the unrestricted lower proof.

**Dependencies and story role.** Integrates [M10](#m10), [M12](#m12), [M16](#m16), and [M25](#m25)–[M29](#m29). It completes the narrative by joining the mechanism, theorem domains, physical costs, attribution, and evidence.

**Conceptual connection.** The contribution concerns how useful information acquired from one fixed oracle can be retained and spent under explicitly charged directional access. Its interpretation depends on keeping the scientific promise, proof interfaces, and implementation resources aligned.

**Source pointers.** Anchor: [Childs §19.3][childs-amplification], [Ch. 21][childs-queries], [Ch. 23][childs-adversary], and [Ch. 26][childs-recording]. Project: [model and proof dependencies](../science/model.md#proof-dependencies-and-evidence), [physical resource summary](../science/implementations.md#resource-summary), [dimension-dependent comparison](../science/forward_only.md#relation-to-existing-dimension-dependent-bounds), [related work and attribution](../references/RELATED_WORK.md), and [the scope of finite verification](../verification/README.md).

## Anchor locations

All anchor references above point to the same **17 April 2025** Childs notes. Page numbers here are the printed page labels; PDF links include the front matter.

- §§1.1–1.4: quantum data, circuits, gate sets, and reversible computation, printed pp. 1–3.
- §2.1: subadditivity of errors, printed p. 7.
- §19.3: amplitude amplification and quantum counting, printed pp. 88–89.
- Chapter 21: query complexity and the polynomial method, printed pp. 97–102.
- Chapter 23: the quantum adversary method, printed pp. 109–114.
- Chapter 26: the compressed oracle method, printed pp. 125–130.

[childs-data]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9
[childs-circuits]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9
[childs-reversible]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=10
[childs-errors]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=15
[childs-amplification]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96
[childs-queries]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105
[childs-adversary]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=117
[childs-recording]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=133
