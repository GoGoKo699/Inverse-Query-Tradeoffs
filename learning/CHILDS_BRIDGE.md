# From Childs's notes to inverse-query tradeoffs

A device prepares one of two known quantum states that are close together. Repeated preparations can reveal which state it produces. If the device can also be run backward, a different question becomes possible: how much can a limited number of backward calls reduce the number of forward calls?

The answer depends on the device's action on inputs other than its reference state. This bridge explains how that unused part of a unitary enters the algorithm, why a symmetric probe makes a small inverse budget useful, and how a lower bound controls algorithms with arbitrary intervening computation.

The [common map](MILESTONES.md) contains 10 background milestones and 20 narrative milestones. Its understanding targets determine the route here. Exact statements and full proofs have their authoritative homes in [the model](../science/model.md) and the linked science chapters.

<a id="selected-source"></a>
## 1. Selected source and precise entry points

The single educational anchor is **Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, author-hosted edition dated 17 April 2025**: [official page](https://www.cs.umd.edu/~amchilds/qa/), [official PDF](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), [bibliographic entry](../references/RELATED_WORK.md#childs2025).

Page numbers below are printed page numbers. The PDF has 191 pages; printed page $`p`$ is PDF viewer page $`p+8`$.

| Source location | Foundation | Project destination |
|---|---|---|
| [§§1.1–1.4, pp. 1–3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9) | States, circuits, reversible computation | [Access](#access), [loading](#loading) |
| [§2.1, p. 7, Lemma 2.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=15) | Accumulated gate error | [Physical resources](#physical-resources) |
| [§19.3, pp. 88–89](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96) | Amplification through quantum walks | [Access assumptions](#amplification) |
| [Ch. 21, pp. 97–102; especially §§21.1–21.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105) | Query models and polynomials | [Separate budgets](#access) |
| [Ch. 23, pp. 109–114; Fact 23.1 and §23.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=117) | Overlap and progress bounds | [Distinguishability](#distinguishability), [hybrids](#hybrids) |
| [Ch. 26, pp. 125–130; especially §§26.1–26.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=133) | Random-function compression | [Haar records](#haar-records) |

Three translations matter. Chapter 21's binary oracle is self-inverse; this project's unknown unitary need not be. Chapter 26's exact random-function compression is different from strong Haar simulation. The reflection circuit below is a local access calculation, rather than the presentation in §19.3.

<a id="access"></a>
## 2. Translate the task before transferring an algorithm

**Map connection:** [M01–M03](MILESTONES.md#m01), [M05](MILESTONES.md#m05), and the complete operational model in [M10](MILESTONES.md#m10). **Canonical statement:** [Model and exact results](../science/model.md).

### A known output does not determine a unitary

A pure state $`|\psi\rangle`$ is a normalized vector. A projector $`P`$ represents a yes/no test: its yes probability is $`\langle\psi|P|\psi\rangle`$. Here the known, orthogonal reference vectors are $`|0\rangle`$ and $`|1\rangle`$. The device is an unknown unitary $`W`$, promised to satisfy

```math
\begin{array}{ll}
b=0:& W|0\rangle=|0\rangle,\\[1mm]
b=1:& W|0\rangle=c|0\rangle+\epsilon|1\rangle,
\end{array}
\qquad
c=\sqrt{1-\epsilon^2},\quad \alpha=\arcsin\epsilon.
```

The bit $`b`$ is the required answer. The known angle $`\alpha`$ measures the separation of the two possible output vectors; $`\epsilon^2`$ is the probability of detecting the second direction in one direct preparation. The main mixed-budget theorem uses $`0<\epsilon\le1/4`$.

Knowing this first column leaves all other columns unrestricted. To isolate them, introduce the known rotation and the actual completion:

```math
R=
\begin{pmatrix}c&-\epsilon\\ \epsilon&c\end{pmatrix}\oplus I_{d-2},
\qquad
R_0=I,\quad R_1=R,\qquad
W_b=R_bV_b,\quad V_b|0\rangle=|0\rangle.
```

This factorization places the promised difference in $`R_b`$ and everything else in $`V_b`$. It is a mathematical description for analysis; the algorithm does not receive $`b`$ or $`V_b`$. The upper algorithm must work for each completion separately, including unrelated $`V_0`$ and $`V_1`$.

The following dictionary fixes the project's notation. Symbols reused in different source chapters should be translated by their role.

| Symbol here | Meaning |
|---|---|
| $`d`$ | Dimension of one physical oracle register |
| $`m=\lceil\log_2d\rceil`$ | Qubits used to encode that register |
| $`n=d-1`$ | Dimension of the random block in the lower proof |
| $`\epsilon,\alpha`$ | Known state separation and its angle |
| $`F,K`$ | Hard upper bounds on forward and inverse calls |
| $`T=F+K`$ | A uniform bound on physical query events |
| $`P_0,Q`$ | The known zero-state test and its complement |
| $`\eta`$ | An implementation-error allowance |
| $`r`$ | Inverse price in the cost section; a coherent remaining count only in the streaming construction |

In particular, $`\epsilon`$ is not the algorithm's allowed failure probability. That probability is at most $`1/3`$. An unknown matrix entry, a state amplitude, and a decision error are distinct quantities.

### What counts as access

A call to $`W`$ consumes one forward query; a call to $`W^\dagger`$ consumes one inverse query. Repeating a gate sequence implementing a known unitary backward is ordinary reversible computation. An unknown device is specified by an oracle interface, so its adjoint must be explicitly supplied or synthesized at a charged cost.

Known gates may act on all accessible registers. The direction of each physical call is selected from the classical measurement history. Every possible history must respect both caps, including histories that stop early. Neither expected query counts nor the probability of a branch replaces these caps. A coherent forward/inverse switch with separately discounted branch costs is outside this contract.

The lower bound grants coherent skipping of a chosen query direction. Even then, the physical invocation costs one call of that direction. This strengthens the interface for the converse. The constructions use ordinary, uncontrolled calls, and never require a free controlled version of the unknown device.

Parallel invocation is also a resource choice: thirteen ports used once cost thirteen queries. A single port can instead be used thirteen times. The available workspace and known-gate work are counted separately below.

<a id="amplification"></a>
### Why the usual amplification intuition needs an access calculation

**Map connection:** [M04](MILESTONES.md#m04).

One direct trial prepares $`W|0\rangle`$ and measures $`\{P_0,Q\}`$, where $`P_0=|0\rangle\langle0|`$ and $`Q=I-P_0`$. The null always gives zero occupation; the alternative gives nonzero occupation with probability $`\epsilon^2`$. With $`s`$ independent trials,

```math
\Pr[\text{all trials miss}\mid b=1]
=(1-\epsilon^2)^s\le e^{-s\epsilon^2}.
```

Thus $`s=\lceil(\ln3)/\epsilon^2\rceil`$ is a valid forward-only upper bound. This experiment shows where the inverse-square scale comes from; it does not establish a lower bound against coherent strategies.

For a prepared state $`|\psi\rangle=W|0\rangle`$, reflection about that state can be written

```math
I-2|\psi\rangle\langle\psi|
=W(I-2P_0)W^\dagger.
```

The equality follows by conjugating the known rank-one projector. Reading the product as a circuit, the adjoint acts first, followed by the known reflection and the forward call. This is an explicit place where both query directions enter a coherent amplification routine.

For the present promise, reflections about each candidate vector are known operations. That fact still does not identify the unknown device with the known rotation $`R_b`$: its completion acts on every other input. An algorithm that repeatedly queries $`W`$ must account for that completion. The project asks how a limited inverse budget can make the subsequent forward inputs useful.

<a id="calibration"></a>
## 3. One inverse produces an exact unknown calibration state

**Map connection:** [M11](MILESTONES.md#m11) and [M12](MILESTONES.md#m12). **Canonical derivation:** [Calibration](../science/dicke_calibration.md#calibration).

Define $`|x_b\rangle=V_b^\dagger|1\rangle`$. Because $`V_b`$ fixes zero and is unitary, $`x_b`$ is orthogonal to zero. Its amplitudes are unknown, but its forward image under $`V_b`$ is the known vector $`|1\rangle`$.

The rotation convention fixes the sign in the inverse calculation:

```math
W_0^\dagger|1\rangle=|x_0\rangle,
\qquad
W_1^\dagger|1\rangle
=\epsilon|0\rangle+c|x_1\rangle.
```

The positive coefficient of zero comes from $`R^\dagger|1\rangle=\epsilon|0\rangle+c|1\rangle`$. This identity determines both the calibration state and the conclusive outcome.

Apply the inverse to a fresh known $`|1\rangle`$, then measure $`\{P_0,Q\}`$. A zero outcome is impossible under the null, so the algorithm immediately outputs 1. A nonzero outcome leaves the normalized state exactly equal to $`|x_b\rangle`$.

After at most $`K`$ such calls, either the answer is already known or the algorithm holds $`K`$ exact copies. Under the alternative, the probability that every calibration reaches this second branch is $`c^{2K}`$. All branches belong to the algorithm; there is no retry loop or uncharged selection of favorable outcomes.

The useful information is embodied in quantum registers. It does not have to become a classical description before it affects later queries.

### A structured completion can make calibration reusable classically

If the completion is a permutation $`P_\pi`$ fixing zero, a basis measurement reveals the label $`x=\pi^{-1}(1)`$, unless zero already certifies the alternative. Let $`S_{1x}`$ be the known swap of labels 1 and $`x`$. Then

```math
W_bS_{1x}\big|_{\operatorname{span}\{|0\rangle,|1\rangle\}}=R_b.
```

This identity turns the measured label into a reusable correction before every forward call. Starting at zero and repeating this corrected call about $`\pi/(2\alpha)`$ times yields a large alternative signal after just one inverse calibration.

That behavior explains the choice of a less structured hard ensemble in the lower proof. A permutation family that is hard without inverses need not remain hard with one inverse. The arbitrary-completion construction below works even when $`x_b`$ is an unknown superposition. Its success also shows why an appeal to no-cloning alone cannot settle the mixed-budget question. See [the structured comparison](../science/resource_tradeoffs.md#a-readable-calibration-can-be-reused-classically).

<a id="loading"></a>
## 4. Distribute a fixed stock of unknown states coherently

**Map connection:** [M06](MILESTONES.md#m06), [M13](MILESTONES.md#m13), and [M16](MILESTONES.md#m16). **Canonical circuits:** [Implementations](../science/implementations.md).

Suppose calibration has provided $`K`$ copies of $`x_b`$. Choose $`F\ge K`$ data positions and add $`F-K`$ known zeros. The desired state is

```math
|D_{F,K}(x_b)\rangle
=\binom FK^{-1/2}
\sum_{\substack{S\subseteq\{1,\ldots,F\}\\|S|=K}}
|x_b\rangle_S|0\rangle_{\overline S}.
```

Each term places the same $`K`$ unknown states in a different subset of positions. Orthogonality to zero makes distinct placements orthogonal, so the binomial coefficient normalizes the superposition. This is a Dicke state in the hidden logical basis formed by zero and $`x_b`$.

No term contains more than the $`K`$ supplied copies. An unknown phase of $`x_b`$ also contributes the same overall phase to every term. Both facts follow from fixed occupation.

### Clean loading with known operations

The primitive needed from reversible computation is a coherent permutation whose routing labels can be erased afterward. The following circuit never inspects the amplitudes of $`x_b`$.

1. Prepare an ordinary qubit register in a uniform superposition of all binary strings $`z`$ with exactly $`K`$ ones.
2. Start the data in the ordered arrangement of $`K`$ copies followed by $`F-K`$ zeros. Reversibly sort the occupation bits into that same order, retaining every comparator's swap decision.
3. Apply those recorded swaps to the data in reverse comparator order. This sends the ordered data to the original arrangement $`z`$.
4. Reverse the sorting computation on the occupation bits and its history, restoring $`z`$ and clearing the comparator history.
5. Coherently compute whether each data register is orthogonal to zero and XOR that flag into its occupation bit. The bit is erased because it agrees exactly with that register's occupation.

After the last step, no routing information remains entangled with the data. The coherence between placements survives. Measuring the occupation labels instead would select a placement and lose the desired superposition.

The initial ordinary Dicke register can itself be generated with a coherent remaining count. With $`r`$ ones still required among $`L`$ positions, rotate the next bit to

```math
\sqrt{\frac{L-r}{L}}\,|0\rangle
+\sqrt{\frac rL}\,|1\rangle,
```

then decrement the count on the one component. These conditional probabilities produce every weight-$`K`$ string with equal probability. Computing and uncomputing the rotation angle before changing the count keeps the arithmetic workspace clean.

The known zero-state test can be implemented coherently by $`P_0\otimes I+Q\otimes X`$. During loading it is a gate, not a measurement. The exact fixed-weight preparation principle is a primary-research ingredient from [Ioannou and Mosca, Theorem 1 and §2.2](../references/RELATED_WORK.md#im2010); the resource-explicit routing circuit is supplied in the project.

### Why the unknown completion disappears

Query each data register once. The two identities $`V_b|0\rangle=|0\rangle`$ and $`V_b|x_b\rangle=|1\rangle`$ give

```math
W_b^{\otimes F}|D_{F,K}(x_b)\rangle
=R_b^{\otimes F}|D_{F,K}(1)\rangle.
```

The right-hand side contains only known logical states and the promised rotation. Calibration and the later queries are correlated through the same actual completion, which is exactly what makes the cancellation possible. It remains valid for arbitrary hypothesis-specific $`V_b`$.

Measure each output's zero/nonzero occupation and sum the results. Under the null the total is exactly $`K`$. A different total certifies the alternative. The final output is one classical bit, even though the probe spans many registers.

<a id="worked-example"></a>
## 5. Complete example: one inverse and thirteen forward calls

**Map connection:** [M11–M15](MILESTONES.md#m11).

Take $`\epsilon=1/5`$, so $`c=\sqrt{24/25}`$ and $`\alpha=\arcsin(1/5)`$. Set $`K=1`$. The finite theorem below selects $`F=13`$. The dimension can be any $`d\ge2`$ and the completion is arbitrary.

| Stage | Operation | Charged calls | Observation |
|---|---|---|---|
| Calibration | Apply the inverse to known state 1; test zero/nonzero | At most 1 inverse | Zero gives the answer 1; otherwise retain one calibration state |
| Loading | Coherently distribute the retained state among 13 positions | Known gates | No occupation measurement |
| Interrogation | Apply the forward oracle to every data position | 13 forward | Calls may use one port successively |
| Readout | Test zero/nonzero in each output; add the outcomes | Known measurements | Output 1 exactly when the total differs from 1 |

On the surviving calibration branch, the probe is

```math
|D_{13,1}(x_b)\rangle
=\frac1{\sqrt{13}}\sum_{j=1}^{13}
|0\rangle^{\otimes(j-1)}|x_b\rangle
|0\rangle^{\otimes(13-j)}.
```

This formula is the coherent version of placing one retained state in thirteen possible positions. It uses one unknown state and twelve blank registers, with clean routing ancillas.

After the forward calls, the null returns weight 1 with certainty. For a symmetric single-excitation Dicke probe with $`F`$ positions, the alternative's amplitude to return to that same state is

```math
a_{F,1}=c^{F-2}(1-F\epsilon^2).
```

To see the interference in this expression, fix one final occupied position. The transition from the same initially occupied position has amplitude $`c^F`$; each of the other $`F-1`$ initial positions contributes $`-\epsilon^2c^{F-2}`$. Every initial position has coefficient $`1/\sqrt F`$, so the final coefficient is $`a_{F,1}/\sqrt F`$ at each position. Taking the overlap with the normalized symmetric state recovers $`a_{F,1}`$. The negative exchange terms are lost if the initial placement is made classical.

Including the possibility of a conclusive calibration outcome gives

```math
\begin{aligned}
\Pr[\widehat b=1\mid b=1]
&=1-c^2|a_{13,1}|^2\\
&=1-\left(\frac{24}{25}\right)^{12}
       \left(\frac{12}{25}\right)^2\\
&\approx0.8588316719.
\end{aligned}
```

The prefactor $`c^2`$ is the probability of reaching the probe stage under the alternative. All remaining branches already answered correctly. The null has no false positives. The resource guarantee is at most one inverse and thirteen forward calls on every history; a conclusive calibration uses no forward calls.

This fixed-$`K`$ example illustrates a constant-factor gain and the interference mechanism. An asymptotically growing gain uses a growing inverse budget, as quantified next.

<a id="finite-angle"></a>
## 6. From enhanced rotation sensitivity to finite success

**Map connection:** [M14](MILESTONES.md#m14) and [M15](MILESTONES.md#m15). **Canonical proof:** [Finite-angle success](../science/dicke_calibration.md#finite-angle-success-proof).

Write $`Y`$ for Pauli $`Y`$ on the known logical plane, and let $`G=\sum_{j=1}^F Y_j`$. The tensor product of rotations is $`e^{-i\alpha G}`$. For the known Dicke state $`|D\rangle=|D_{F,K}(1)\rangle`$,

```math
v:=\langle D|G^2|D\rangle
=F+2K(F-K).
```

The first term is the single-register contribution. The second comes from correlations between distinct registers. For $`K\ll F`$, the result is of order $`F(K+1)`$, giving a larger collective response than a zero-excitation probe.

A large second moment alone controls only the initial curvature of a return amplitude. It does not exclude a later return close to one at the chosen finite angle. The project therefore also proves

```math
\langle D|G^4|D\rangle\le3v^2.
```

This fourth-moment bound limits the contribution of large generator values. It follows by resolving $`G^2|D\rangle`$ into its orthogonal weight-$`K-2,K,K+2`$ components.

The collective rotation preserves permutation symmetry. Within that symmetric logical space, the weight-$`K`$ sector has dimension one. Thus its survival probability is $`|a|^2`$, where $`a=\langle D|e^{-i\alpha G}|D\rangle`$. Weight parity makes every odd moment vanish, so $`a`$ is real. Global cosine inequalities, combined with the fourth moment, give

```math
1-\frac{\gamma}{2}
\le a
\le1-\frac{\gamma}{2}+\frac{\gamma^2}{8},
\qquad \gamma=\alpha^2v.
```

These inequalities apply at the actual finite angle. Choosing $`3/2\le\gamma<2`$ keeps the lower bound nonnegative and puts the upper bound at most $`17/32`$.

For every allowed integer inverse budget, the following rounding achieves that interval:

```math
0\le K\le\left\lfloor\frac1{2\alpha}\right\rfloor,
\qquad
F=\left\lceil
\frac{3/(2\alpha^2)+2K^2}{2K+1}
\right\rceil.
```

Indeed, $`v=(2K+1)F-2K^2`$, so the ceiling puts $`\alpha^2v`$ at least $`3/2`$ and less than $`3/2+\alpha^2(2K+1)<2`$. It also ensures enough data positions to hold the $`K`$ states.

The complete experiment then satisfies

```math
\Pr[\widehat b=1\mid b=0]=0,
\qquad
\Pr[\widehat b=1\mid b=1]
=1-c^{2K}|a|^2
\ge1-\left(\frac{17}{32}\right)^2
=\frac{735}{1024}>\frac23.
```

This is a uniform finite decision guarantee. It includes the calibration branches, works in every dimension, and uses the stated integer budgets. In the example, $`v=37`$ and $`\alpha^2v\approx1.50016545`$.

Dicke probes also maximize this second moment among probes confined to the same fixed-occupation logical sector, including ancillary entanglement. That is a useful architecture-specific fact, proved in [the fixed-batch analysis](../science/dicke_calibration.md#optimality-within-a-fixed-occupation-parallel-batch). A converse for all interleaved algorithms needs the separate record argument below.

<a id="physical-resources"></a>
## 7. Query savings, known gates, and live memory

**Map connection:** [M03](MILESTONES.md#m03) and [M16](MILESTONES.md#m16). **Full accounting:** [Resource summary](../science/implementations.md#resource-summary).

The loading circuit manipulates physical registers. A controlled swap of two $`m`$-qubit registers has $`O(m)`$ elementary-gate cost, and a coherent zero test has the same scale with workspace. The estimates assume ordinary one- and two-qubit gates between selected registers; no geometric communication cost or QRAM is hidden in the query count.

For loading error at most $`\eta`$, two explicit realizations have the following costs. The logarithmic factors include coherent arithmetic and known-gate synthesis.

| Realization | Known elementary gates | Live qubits |
|---|---|---|
| Wide reversible sorting | $`O(F\,\operatorname{polylog}(F/\eta)+Fm\log^2(F+2))`$ | $`O(Fm+F\log^2(F+2)+\operatorname{polylog}(F/\eta))`$ |
| Streaming reservoir | $`O(FK(\log(K+1)+m)+Fm+F\,\operatorname{polylog}(F/\eta))`$ | $`O((K+1)m+\operatorname{polylog}(F/\eta))`$ |

Both use the same at-most-$`F,K`$ physical query counts. The wide circuit retains the full data array and its reversible comparator history during loading. The $`F\log^2(F+2)`$ history contribution is part of its memory requirement, even though that history is eventually erased.

### Streaming preserves a quantum count

The streaming circuit keeps a reservoir of $`K`$ registers and a coherent count $`r`$. In the component labeled $`r`$, the first $`r`$ reservoir registers contain $`x_b`$ and the others contain zero. One emission step implements

```math
\begin{aligned}
|r\rangle|R_r(x_b)\rangle|0\rangle
\longmapsto{}&
\sqrt{\frac{L-r}{L}}\,
|r\rangle|R_r(x_b)\rangle|0\rangle\\
&+\sqrt{\frac rL}\,
|r-1\rangle|R_{r-1}(x_b)\rangle|x_b\rangle.
\end{aligned}
```

This is the Dicke recursion expressed as a physical transfer from the reservoir. The state $`|R_r(x_b)\rangle`$ denotes its ordered contents; the fresh register is the last factor. An explicit loop over all reservoir slots implements the selection without QRAM, causing the $`FK`$ gate-work term.

The emission flag is erased with the fresh register's coherent zero test before that register encounters $`W_b`$. The forward call and its output measurement can then happen immediately. They commute with all future generation operations, which act on the reservoir and fresh registers, so the final count has the same distribution as in the full wide experiment.

The reservoir count must remain quantum. Under the alternative, an output measurement can leave different remaining counts in coherent superposition. Measuring $`r`$ would change the probe statistics. The separate counter of observed output occupations is classical.

Streaming reduces live quantum memory, but at $`F,K=\Theta(\epsilon^{-1})`$ its routing cost already contains an $`FK=\Theta(\epsilon^{-2})`$ factor before the register-width and count-arithmetic costs. The oracle improvement and the gate/memory choice therefore describe different physical resources.

### Accuracy is charged through the complete experiment

Trace distance at most $`\eta`$ between ideal and loaded probes changes any eventual decision probability by at most $`\eta`$. The ideal margin above $`2/3`$ is $`157/3072>0.051`$, so $`\eta=1/64`$ is sufficient. Exact deterministic boundary operations in the count recursion preserve fixed occupation even with approximate interior angles.

Approximate inversion, when used later, has a separate channel-error budget. The errors of the full instruments are composed without conditioning on successful calibration, so no inverse probability of a selected branch appears. The [precision account](../science/implementations.md#loading-precision) gives the exact conventions.

<a id="inverse-endpoint"></a>
## 8. Enough inverse calls can accumulate a phase without forward calls

**Map connection:** [M17](MILESTONES.md#m17). **Circuit and attribution:** [Inverse-only phase accumulation](../science/implementations.md#inverse-only-phase-accumulation).

The end of the resource frontier is not obtained by setting $`F=0`$ in the Dicke-loading formula, which requires data positions. There is a direct inverse-only experiment with one memory qubit.

Let $`\theta_b=b\alpha`$ and prepare the known probe states $`|\pm_y\rangle=(|0\rangle\pm i|1\rangle)/\sqrt2`$. Their inverse images are

```math
W_b^\dagger|\pm_y\rangle
=\frac{e^{\pm i\theta_b}}{\sqrt2}
\bigl(|0\rangle\pm i|x_b\rangle\bigr).
```

The promised rotation becomes an opposite phase on the two preparations. The unknown completion affects their common nonzero state in the same way.

Use the memory coherently to choose the plus or minus probe, then make one ordinary inverse call and measure the probe's zero/nonzero occupation. The two induced memory operations are

```math
K_0=\frac1{\sqrt2}D_{\theta_b},
\qquad
K_Q=\frac{i}{\sqrt2}Z D_{\theta_b},
\qquad
D_\theta=\operatorname{diag}(e^{i\theta},e^{-i\theta}).
```

The symbols $`K_0,K_Q`$ here denote the measurement's linear branch operators, not query budgets. A known $`Z`$ correction after the nonzero outcome makes either branch implement $`D_{\theta_b}`$ up to an overall phase. Each outcome has probability one half, and the probe factors from the memory afterward. It can be discarded.

Starting the memory in $`|+\rangle`$, repeat the procedure $`q`$ times and measure in the $`X`$ basis:

```math
\Pr[X=-1\mid b]=\sin^2(q\theta_b).
```

This is phase accumulation across the same memory, with each round consuming one inverse. Taking $`q=\lceil1/\alpha\rceil`$ gives no null false positives and alternative success at least $`\sin^2(1)>2/3`$ in the main parameter range. It uses $`F=0`$, $`K=q`$, $`O(qm)`$ known gates, and $`O(m)`$ live qubits.

The underlying interface is established measurement discrimination. Applying $`W_b^\dagger`$ and then testing zero implements the known effect $`W_bP_0W_b^\dagger=|\psi_b\rangle\langle\psi_b|`$. [Puchała et al.](../references/RELATED_WORK.md#ppkko2021) give the relevant general multiple-use results. Their optimality statements concern that measurement channel; the unrestricted mixed-oracle converse has a larger interface.

<a id="distinguishability"></a>
## 9. What a lower bound must control

**Map connection:** [M07–M09](MILESTONES.md#m07), [M18](MILESTONES.md#m18), and [M19](MILESTONES.md#m19). **Canonical arguments:** [Mixed-query lower bound](../science/mixed_query_lower_bound.md), [Haar simulation](../science/haar_simulation.md).

The upper construction is one permitted algorithm. A query lower bound must also cover algorithms that entangle every register, retain calibration information in another form, interleave both directions, and choose later calls from earlier measurement outcomes.

For this purpose a density operator $`\rho`$ describes the statistics of an accessible quantum state, including mixtures and retained classical records. A pure state has density operator $`|\psi\rangle\langle\psi|`$. Discarding a subsystem is represented by a partial trace. The operational distance is

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1,
\qquad
P_{\rm succ}^{\rm opt}=\frac{1+D(\rho,\sigma)}2
\quad\text{for equal priors}.
```

The trace norm sums singular values. The formula says that constant binary success requires a constant separation of the final states: success at least $`2/3`$ requires $`D\ge1/3`$. A common quantum operation, including discarding hidden registers, cannot increase this distance.

### Choose a hard ensemble that respects every promise

For the lower proof only, draw one Haar-random $`U\in U(n)`$, with $`n=d-1`$ a power of two. Haar measure is the probability distribution invariant under multiplying $`U`$ on either side by any fixed unitary. Choose

```math
V=1\oplus U,\qquad W_0=V,\qquad W_1=RV.
```

This correlated pair is permitted by the promise. A worst-case algorithm must work for these completions too. Averaging its final state over the chosen $`U`$ therefore gives a legitimate route to a worst-case lower bound.

The same sampled matrix is reused throughout a run. A model that resampled it at each call would destroy the useful correlations between calibration and later queries and would address a different task.

<a id="haar-records"></a>
### From hidden randomness to directional records

For analysis, the hidden random choice can be represented by an inaccessible environment. A recording representation tracks how oracle calls correlate the algorithm with that environment while preserving the accessible behavior to a controlled error.

For a unitary with both directions available, orthogonality constraints couple input and output labels. The project uses the strong Haar path-recording construction of [Ma and Huang](../references/RELATED_WORK.md#mh2025), with left and right record registers. Their records contain input-output pairs. A forward call can append a fresh left record or undo compatible right-record information; an inverse call has the adjoint behavior.

The recording map $`M`$ is a contraction, with $`M^\dagger`$ representing inverse queries. Its outputs may have squared norm below one. The lost norm is charged as simulation error; it is never normalized away or treated as free postselection.

The [controlled simulation lemma HS.1](../science/haar_simulation.md#lemma-hs1-controlled-strong-haar-simulation) states, for $`T\le n/2`$,

```math
D(\text{Haar-averaged output},\text{recording output})
\le\eta_n(T):=\frac{9T(T+1)}{n^{1/8}}.
```

This is the cost of replacing the physical Haar ensemble by its recording representation for one hypothesis. Comparing two hypotheses pays it twice.

The control and classical-adaptivity extension is proved in the project. Its essential requirement is a single environment transformation compatible with both directions and every skipped sector. Orthogonal control blocks retain the source operator bounds, and immutable copies of measurement outcomes preserve the classical-history decomposition. This source-level argument is needed before a mixed-query lower bound can use the simulator.

<a id="potential"></a>
## 10. An inverse-generated potential limits accumulated forward progress

**Map connection:** [M20–M22](MILESTONES.md#m20). **Canonical proof:** [The projected number identity and its consequences](../science/mixed_query_lower_bound.md#4-a-projected-oracle-and-its-exact-number-identity).

The crucial quantity is in the inaccessible database, not a register available to the algorithm.

Let $`\Gamma`$ project onto records having no left pair with output label 1. Right records with that output remain allowed. Let $`N`$ count those right records, including multiplicity, and let $`P=|1\rangle\langle1|`$ act on the query register. Compress the recording oracle to $`C=\Gamma M\Gamma`$, retaining its known identity action on the zero state.

The append/delete rules imply the exact relation

```math
(N+P)C=CN.
```

This is a number-accounting identity. In the projected process, a forward output in the distinguished direction must be paid for by a decrease in the right-record count. The operator equation controls superpositions, not just individual database configurations.

Because $`C`$ is a contraction and the relevant positive operators commute, it yields

```math
\begin{aligned}
\langle Cz|(N+P)|Cz\rangle
&\le\langle z|N|z\rangle,\\
\langle C^\dagger z|N|C^\dagger z\rangle
&\le\langle z|(N+P)|z\rangle
\le\langle z|N|z\rangle+\|z\|^2.
\end{aligned}
```

The first line says that forward output probability consumes potential. The second says that an inverse can supply at most its prequery probability weight. Known operations act only on accessible systems and cannot alter the private number operator.

Start with empty records and sum these inequalities over the algorithm. The final potential is nonnegative. If $`p_{b,t}`$ is the active forward probability on label 1 immediately after $`C`$ and before any extra rotation, then

```math
\sum_t p_{b,t}\le K.
```

This bound concerns the sum over the whole computation. A single forward probability can be one after a useful inverse call; a pointwise estimate that made every such probability small would be false. The potential controls repeated use of the accumulated information.

### Why adaptive histories still obey the same budget

Purify each measurement while retaining immutable copies of its outcome. Histories remain orthogonal, and their physical forward and inverse counters are explicit. If $`w_{b,t}`$ is the prequery weight of histories requesting a forward call, hard caps imply

```math
\sum_t w_{b,t}\le F,
\qquad
\sum_t w^{\rm inv}_{b,t}\le K.
```

These inequalities also hold in the projected process. One can complete each contraction with a failure outcome and halt that outcome: the retained successful weights stay unchanged, and all resulting histories respect the original caps. The first sum counts physical forward requests, while $`p_{b,t}`$ retains only the coherently active distinguished outputs.

Projection has a cost. Excluding a new left output label 1 causes at most $`2/\sqrt{n-t}`$ operator leakage in a forward step and $`1/\sqrt{n-t}`$ in an inverse step. Telescoping over both hypotheses contributes $`4T/\sqrt{n-T}`$ to the final distance estimate. This is separate from Haar-simulation error.

<a id="hybrids"></a>
## 11. Turn the potential into a mixed-query converse

**Map connection:** [M23–M25](MILESTONES.md#m23). **Canonical theorem:** [MQ.1 and MQ.2](../science/mixed_query_lower_bound.md#1-model-and-theorem).

In the projected representation, the null uses forward $`C`$ and inverse $`C^\dagger`$. The alternative uses forward $`RC`$ and inverse $`C^\dagger R^\dagger`$. A hybrid argument compares processes by replacing one kind of operation while leaving the other fixed.

### First remove the inverse rotations

One inverse replacement has operator error at most $`\delta_\epsilon=\|R-I\|=\sqrt{2(1-c)}`$. Group operations by the first requested inverse, second requested inverse, and so on. The intervening forward computations are common contractions in this comparison, even when different histories reach a given inverse at different times.

This ordinal grouping yields total vector error at most $`K\delta_\epsilon`$. It is what justifies the linear dependence on the hard inverse cap. Summing square roots of inverse-request probabilities at arbitrary time slots would not give that bound.

### Then compare the forward rotations

After the inverse replacement, both processes use the same $`C^\dagger`$. Let $`w_{0,t},w_{1,t}`$ be their forward-request weights and $`p_{0,t},p_{1,t}`$ their distinguished-output probabilities. Expanding the squared distance across a forward call gives the increment bound

```math
\Delta_t
\le2(1-c)\sqrt{w_{0,t}w_{1,t}}
+2\epsilon\left(
\sqrt{w_{0,t}p_{1,t}}+\sqrt{p_{0,t}w_{1,t}}
\right).
```

The diagonal part of $`I-R`$ gives the first term. Its two off-diagonal entries couple zero to label 1 and give the other terms. This is where the number potential enters a distinguishability calculation.

Cauchy–Schwarz converts the accumulated probabilities into a mixed resource factor:

```math
\sum_t\sqrt{w_{0,t}p_{1,t}}
\le
\sqrt{\left(\sum_t w_{0,t}\right)
      \left(\sum_t p_{1,t}\right)}
\le\sqrt{FK}.
```

The other cross term has the same bound; the sum of $`\sqrt{w_{0,t}w_{1,t}}`$ is at most $`F`$. Thus the total forward contribution to squared vector distance is at most $`2F(1-c)+4\epsilon\sqrt{FK}`$.

These vector bounds also control the subnormalized output operators. For vectors of norm at most one,

```math
\frac12\bigl\||u\rangle\langle u|-|v\rangle\langle v|\bigr\|_1
\le\frac{\|u\|+\|v\|}{2}\,\|u-v\|
\le\|u-v\|.
```

The first inequality follows by splitting the difference of the rank-one operators into two outer products involving $`u-v`$. Discarding the inaccessible records cannot increase trace distance. Taking the square root of the forward bound, adding the inverse hybrid, and charging both representation errors therefore gives

```math
\begin{aligned}
D(\bar\rho_0,\bar\rho_1)\le{}&
K\sqrt{2(1-c)}
+\sqrt{2F(1-c)+4\epsilon\sqrt{FK}}\\
&+\frac{4T}{\sqrt{n-T}}
+\frac{18T(T+1)}{n^{1/8}}.
\end{aligned}
```

Here $`\bar\rho_b`$ is the physical output averaged over one reused Haar completion. The four terms respectively charge inverse rotations, cumulative forward progress, projection leakage, and Haar simulation. The formula applies to arbitrary known computation and workspace under the stated physical-query contract.

For example, the explicit sufficient dimension condition

```math
n\ge2T+[432T(T+1)]^8+(96T)^2,
\qquad n\text{ a power of two},
```

makes the two dimension-dependent errors small enough to turn the distance estimate into the necessary condition

```math
F(K+1)+K^2>10^{-4}\epsilon^{-2}
```

for success at least $`2/3`$. This follows by contradiction: if the left side were smaller, the displayed distance bound would be below $`1/3`$. The precise finite calculation is in MQ.2.

The dimension condition is sufficient and deliberately loose, of order $`T^{16}`$. A logarithmic number of qubits can address that dimension, but the proof supplies no efficient physical circuit for an individual Haar-random oracle. It also supplies no matching converse in a small fixed dimension.

<a id="resource-frontier"></a>
## 12. Join the construction and converse, then price inverses

**Map connection:** [M26](MILESTONES.md#m26) and [M27](MILESTONES.md#m27). **Canonical synthesis:** [Resource tradeoffs](../science/resource_tradeoffs.md).

The upper construction creates a collective response of order $`F(K+1)`$ from a limited calibration stock. The inverse-only endpoint works at $`K=\Theta(\epsilon^{-1})`$. The general converse gives the same combined dependence in its dimension range:

```math
F(K+1)+K^2\asymp\epsilon^{-2}.
```

This expression describes the resource boundary up to universal factors, rather than an equality required of every successful algorithm. The exact integer upper constructions and the explicit necessary condition determine its finite meaning.

When $`K=o(\epsilon^{-1})`$, the $`K^2`$ term is negligible compared with $`\epsilon^{-2}`$, and the matched scale is $`F=\Theta(1/[\epsilon^2(K+1)])`$. A fixed number of inverse calls changes a constant factor. Taking $`K`$ of order $`\epsilon^{-1/2}`$ yields forward scale $`\epsilon^{-3/2}`$. At a sufficiently large constant times $`\epsilon^{-1}`$ inverses, forward calls can be eliminated. The constant at that last endpoint matters.

Now let one inverse cost $`r\ge1`$ units of forward-call cost. The objective is $`F+rK`$. Balancing the useful intermediate forward scale against inverse expense suggests $`K`$ of order $`1/(\epsilon\sqrt r)`$; once that is below one, direct sampling becomes competitive. The proved cost law is

```math
\min_{\text{successful algorithms}}(F+rK)
=\Theta\!\left(
\min\left\{\frac{\sqrt r}{\epsilon},\epsilon^{-2}\right\}
\right).
```

The lower theorem's dimension condition must hold for the budgets under comparison. The canonical cost proof supplies both an integer allocation and a lower bound over all allocations. Known-gate work and memory remain separate: a favorable oracle price does not remove a streaming circuit's routing cost.

<a id="finite-dimension"></a>
## 13. Finite dimension permits synthesized calibration

**Map connection:** [M28](MILESTONES.md#m28) and [M29](MILESTONES.md#m29). **Canonical theorem:** [Forward-only discrimination](../science/forward_only.md).

An unknown inverse can be constructed from enough ordinary forward calls in fixed dimension. The relevant imported circuit is [QURA](../references/RELATED_WORK.md#qura). Its exact call count is

```math
m_d=\left\lceil\frac{\pi}{2\arcsin(1/d)}\right\rceil,
\qquad
L_d=dm_d-1\le\frac{\pi}{2}d^2+d.
```

Thus one synthesized calibration inverse has $`O(d^2)`$ native-forward cost. The explicit circuit uses unconditional unknown-oracle calls surrounded by known operations, so it does not require free controlled access to $`W`$.

Its vector statement for a general $`U(d)`$ oracle produces $`\det(W)^{m_d}W^\dagger|\varphi\rangle`$. This is the desired inverse output times a global phase. Every use here acts on a separate known calibration input, and each surviving probe term contains exactly $`K`$ calibrated states. The phases consequently multiply into one overall phase of that branch. There is no coherent comparison with a branch skipping an inverter.

Synthesize only the $`K`$ calibration calls and keep the $`F`$ sensing calls native. The total is

```math
F_{\rm native}=F+L_dK,\qquad K_{\rm native}=0.
```

This accounting is the reason to optimize the intermediate calibration budget. Substituting the price $`L_d=\Theta(d^2)`$ suggests $`K=\Theta(1/(d\epsilon))`$ when that is at least one.

The exact choice $`K=\lfloor1/(2d\epsilon)\rfloor`$ in the small-separation regime, with direct sampling in the remaining regimes, gives for every $`d\ge2`$ and $`0<\epsilon\le1`$

```math
F_{\rm native}
<5\min\{\epsilon^{-2},d/\epsilon\}.
```

This is an all-dimension upper bound for the specified binary promise. It is consistent with the large-dimension lower theorem, whose dimension requirement excludes using it as a fixed-dimension matching converse.

Inverter ancillas require an additional $`O(d\log d)`$ qubits and can be reused between calibrations. Its known-gate synthesis cost remains the separately charged quantity $`K\,G_{\rm QURA}(d,\delta)`$; a parallel-depth estimate cannot substitute for this gate count. The wide loader still includes its comparator-history memory. With approximate inverses, a per-use half-diamond-norm error $`\delta`$ adds at most $`K\delta`$ to the complete experiment's error.

The two candidate vectors are known throughout. The [comparison with general amplitude estimation](../science/forward_only.md#relation-to-existing-dimension-dependent-bounds) explains why obtaining the same cost expression for this decision problem does not resolve that broader task.

<a id="research-dependencies"></a>
## 14. Research dependencies and the complete scientific route

**Map connection:** the final synthesis in [M30](MILESTONES.md#m30).

Childs is the educational anchor. The primary papers below have specific scientific roles; they are distinct from the explanations and derivations supplied locally.

| Research input | Exact role | Project proof or construction |
|---|---|---|
| [Ioannou–Mosca, arXiv:0810.2780v3, Theorem 1 and §2.2](https://arxiv.org/pdf/0810.2780v3) | Fixed-weight preparation in a hidden basis | [Explicit loading and resources](../science/implementations.md) |
| [Ma–Huang, arXiv:2410.10116v3, §§8–9 and Theorem 8](https://arxiv.org/html/2410.10116v3) | Strong forward/inverse Haar recording and source estimates | [Control/history extension](../science/haar_simulation.md), then [directional potential and converse](../science/mixed_query_lower_bound.md) |
| [Puchała et al., arXiv:1810.05122v4, Theorem 1 and Corollary 1](https://arxiv.org/pdf/1810.05122v4) | Multiple-use projective-measurement discrimination | [Explicit inverse-only memory circuit](../science/implementations.md#inverse-only-phase-accumulation) |
| [Chen et al., arXiv:2403.04704v3, Theorem 1 and Appendix A](https://arxiv.org/pdf/2403.04704v3) | Exact unknown-unitary inversion interface and query cost | [Synthesized-calibration consequence](../science/forward_only.md) |

The [related-work account](../references/RELATED_WORK.md) also places the known-state promise, earlier forward-only bounds, and other multiple-resource lower bounds. It distinguishes imported ingredients from the finite Dicke guarantee, the directional record potential, and the consequences derived here.

The whole result joins three different kinds of reasoning. Calibration makes arbitrary unknown columns useful without learning them classically. Collective interference converts a fixed stock of those states into an enhanced forward experiment with explicit loading and readout costs. The converse controls every permitted algorithm by tracking a hidden number potential and charging the approximation needed to represent a reused Haar oracle.

The exact scientific qualifications travel with that synthesis: arbitrary completions for the upper; hard physical-call caps for the converse; a sufficient large dimension for matching lower bounds; separately counted gates and memory; and a finite-dimension native-forward upper for two known candidate states. The [verification guide](../verification/README.md) identifies reproducible finite construction checks. Those checks support their listed finite identities and budget calculations; the unrestricted adaptive converse rests on the analytical lemmas in the science chapters.
