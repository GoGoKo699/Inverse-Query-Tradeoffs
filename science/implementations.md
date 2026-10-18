# Implementations and resource accounting

The [calibrated Dicke theorem](dicke_calibration.md#finite-upper-bound) supplies the finite success guarantee. This note implements its loading and measurement operations and accounts for known gates, live quantum memory, and actual oracle calls.

Use the [model](model.md), with an oracle register encoded in $`m=\lceil\log_2d\rceil`$ qubits and known states $`|0\rangle,|1\rangle`$. Let $`P_0=|0\rangle\langle0|`$ and $`Q=I-P_0`$. After calibration, the data consist of $`K`$ copies of an unknown $`|x\rangle\perp|0\rangle`$ and known zero registers. Neither construction uses QRAM or controlled access to the unknown oracle.

Flag and label erasure use the coherent gate

```math
T_Q=P_0\otimes I+Q\otimes X
```

on a data register and a flag. The zero tests during loading are not measurements. Measurement occurs during calibration and after oracle interrogation.

## Resource summary

Let $`\eta>0`$ be the allowed error in loading, measured in trace distance. Known reversible arithmetic and rotation synthesis contribute a factor polynomial in $`\log(F/\eta)`$; $`\operatorname{polylog}`$ below denotes such a factor. The resource counts are sufficient upper bounds.

| Realization | Actual oracle calls | Known-gate work | Live quantum workspace |
|---|---|---|---|
| Wide loading and sorting | At most $`K`$ inverse and $`F`$ forward | $`O(F\,\operatorname{polylog}(F/\eta)+Fm\log^2(F+2))`$ | $`O(Fm+F\log^2(F+2)+\operatorname{polylog}(F/\eta))`$ |
| Streaming reservoir | At most $`K`$ inverse and $`F`$ forward | $`O(FK(\log(K+1)+m)+Fm+F\,\operatorname{polylog}(F/\eta))`$ | $`O((K+1)m+\operatorname{polylog}(F/\eta))`$ |
| Inverse-only phase accumulation | $`q`$ inverse and no forward | $`O(qm)`$ | $`O(m)`$ |

The first two realizations also use an $`O(\log F)`$-bit classical weight counter. The last uses an $`O(\log q)`$-bit classical loop counter. Each reports one final decision bit. The streaming expression includes the $`Fm`$ cost of zero tests and resets explicitly, including at $`K=0`$; for $`K\ge1`$ this is absorbed by the displayed $`FKm`$ term.

These counts separate oracle invocations from known gates. Parallel invocations each count as a query. The [weighted oracle-cost optimization](resource_tradeoffs.md) must be combined with the known-gate costs here when evaluating a total runtime.

## Wide loading with reversible sorting

The target is

```math
|D_{F,K}(x)\rangle
=\binom{F}{K}^{-1/2}
\sum_{|S|=K}|x\rangle_S|0\rangle_{\overline S}.
```

Every summand contains exactly $`K`$ unknown excitations. This fixed occupation makes the target insensitive to the unknown phase of $`x`$. The hidden-basis preparation principle is established by Ioannou and Mosca, [Theorem 1 and Section 2.2](https://arxiv.org/pdf/0810.2780v3). The following circuit makes its resource use explicit.

### Prepare a known occupation register

First prepare the ordinary qubit Dicke state

```math
|Z\rangle=\binom{F}{K}^{-1/2}\sum_{|z|=K}|z\rangle.
\tag{I1}
```

Initialize a coherent count $`r=K`$. At a step with $`L`$ positions remaining, rotate a fresh occupation bit from zero to

```math
\sqrt{1-r/L}\,|0\rangle+\sqrt{r/L}\,|1\rangle,
\tag{I2}
```

then decrement $`r`$ if that bit is 1. After $`F`$ steps, $`r=0`$. Each allowed string has probability $`K!(F-K)!/F!=\binom{F}{K}^{-1}`$, so (I1) is obtained with no count garbage.

For a finite gate set, compute the rotation angle from the quantum count $`r`$ and classical $`L`$, apply the controlled rotation, and uncompute the angle workspace before decrementing $`r`$. The arithmetic must act coherently on $`r`$. With per-step operator error $`O(\eta/F)`$, reversible arithmetic and synthesis use

```math
F\,\operatorname{polylog}(F/\eta)
```

known gates. The boundary cases $`r=0`$ and $`r=L`$ are exact deterministic operations. Consequently approximate interior angles still produce a state supported on weight $`K`$.


### Route the unknown states and erase the labels

Initialize the $`F`$ data registers as

```math
|x\rangle^{\otimes K}|0\rangle^{\otimes(F-K)}.
```

Use a fixed sorting network on the occupation bits, with $`O(F\log^2(F+2))`$ binary comparators.

1. Reversibly sort the occupation string in descending order, keeping every swap decision in a history register $`h(z)`$. The occupation string becomes the constant $`1^K0^{F-K}`$.
2. Apply the same recorded swaps to the data registers in **reverse comparator order**. These swaps take the ordered data into the arrangement specified by the original $`z`$.
3. Invert the sorting computation on the occupation and history registers. This restores $`|z\rangle`$ and clears $`h(z)`$.
4. XOR each data register's $`Q`$-occupation into its occupation bit. A data register is exactly zero when its bit is 0 and is exactly $`x\perp0`$ when its bit is 1. Thus every occupation bit is erased, while the data remain unchanged.

The output is $`|D_{F,K}(x)\rangle`$ with all routing ancillas clean. Sorting acts on known binary occupation keys; no information about the amplitudes of $`x`$ is accessed.

Padding the sorting network to a power of two uses fewer than $`2F`$ positions. Padded occupation bits start at zero, and their data registers return to zero after routing. Only the original $`F`$ positions receive forward oracle calls.

### Gate and memory counts

A controlled swap of two $`m`$-qubit registers uses $`O(m)`$ known gates. A coherent zero test costs $`O(m)`$ known reversible gates with workspace. The sorting decisions occupy $`O(F\log^2(F+2))`$ qubits if each is retained explicitly.

Including calibration tests and final weight counting, the wide realization therefore uses

```math
G_{\rm wide}
=O\!\left(
F\,\operatorname{polylog}(F/\eta)
+Fm\log^2(F+2)
\right)
\tag{I3}
```

known gates and

```math
M_{\rm wide}
=O\!\left(
Fm+F\log^2(F+2)+\operatorname{polylog}(F/\eta)
\right)
\tag{I4}
```

live qubits. The calibration work is absorbed because the theorem has $`F\ge K`$.

Applying the $`F`$ forward invocations in one layer requires $`F`$ physical oracle ports. With a single port, the invocations can be applied successively while retaining the data registers. The query count is $`F`$ in either case.

## Streaming with a coherent reservoir

The full output register need not be stored. Instead retain $`K`$ reservoir registers and a coherent count $`r`$. On a component with count $`r`$, the reservoir is

```math
|R_r(x)\rangle
=|x\rangle^{\otimes r}|0\rangle^{\otimes(K-r)}.
\tag{I5}
```

The joint state can be a coherent superposition of different components $`|r\rangle|R_r(x)\rangle`$, entangled with previously emitted systems or their measurement records.

### One emission step

At a step with $`L`$ output positions remaining:

1. Introduce a fresh zero data register and a flag. Rotate the flag with the amplitudes in (I2), controlled on the quantum count $`r`$.
2. Conditioned on the flag being 1, transfer the reservoir's $`r`$-th register into the fresh register by a controlled swap. Then decrement $`r`$.
3. Erase the flag by XORing the fresh register's $`Q`$-occupation into it. This occurs before applying the unknown oracle.
4. Apply $`W_b`$ to the fresh register, measure its $`Q`$-occupation, add the result to the classical output-weight counter, and discard or reset that register.

Before the interrogation, this isometry acts as

```math
\begin{aligned}
|r\rangle|R_r(x)\rangle|0\rangle
\longmapsto{}&
\sqrt{\frac{L-r}{L}}\,
|r\rangle|R_r(x)\rangle|0\rangle\\
&+\sqrt{\frac rL}\,
|r-1\rangle|R_{r-1}(x)\rangle|x\rangle.
\end{aligned}
\tag{I6}
```

The second term is absent for $`r=0`$. Iterating (I6) from $`r=K`$ produces the Dicke recursion

```math
|D_{L,r}(x)\rangle
=\sqrt{\frac{L-r}{L}}\,|0\rangle|D_{L-1,r}(x)\rangle
+\sqrt{\frac rL}\,|x\rangle|D_{L-1,r-1}(x)\rangle.
\tag{I7}
```

After the final step, the count and reservoir are zero.

### Why the output can be measured immediately

Future generation operations act on the reservoir and new registers. They have disjoint support from the oracle call and measurement on an already emitted register. Interchanging these operations therefore preserves the joint outcome distribution. The streaming implementation gives the same total-weight statistics as preparing the full Dicke state and then applying $`W_b^{\otimes F}`$.

Under the rotated hypothesis, an emitted-register measurement can leave coherent superpositions of distinct values of $`r`$. Retaining this coherence is necessary: replacing $`r`$ by a measured classical count changes the experiment. The output-weight counter is classical; the reservoir count is quantum.

### An explicit multiplexer

To select reservoir slot $`r`$ without QRAM, loop through $`j=1,\ldots,K`$. Compute the equality predicate $`r=j`$ into a temporary bit, perform the data swap controlled on that bit and the emission flag, and uncompute the equality predicate. Change $`r`$ only after this loop.

This costs $`O(K(\log(K+1)+m))`$ known gates per emission, with reusable temporary workspace. Including rotation arithmetic, zero tests, and resets yields

```math
G_{\rm stream}
=O\!\left(
FK(\log(K+1)+m)
+Fm+F\,\operatorname{polylog}(F/\eta)
\right),
\tag{I8}
```

and

```math
M_{\rm stream}
=O\!\left((K+1)m+\operatorname{polylog}(F/\eta)\right).
\tag{I9}
```

For $`K\ge1`$, the $`Fm`$ term is absorbed in $`FKm`$. At $`K=\Theta(1/\epsilon)`$, the explicit routing work can scale as $`FK=\Theta(\epsilon^{-2})`$, even though the total oracle count is $`\Theta(1/\epsilon)`$. The wide and streaming circuits thus provide different gate/memory tradeoffs.

## Loading precision

The exact theorem uses known real rotations. With a finite gate set, suppose the prepared probe differs from the ideal one by at most $`\eta`$ in trace distance. Contractivity under oracle calls and measurements changes each decision probability by at most $`\eta`$.

The ideal success margin is

```math
\frac{735}{1024}-\frac23=\frac{157}{3072}>0.051.
```

Taking $`\eta=1/64`$ leaves success above $`2/3`$. The rotation count is polynomial in $`F`$, so synthesis precision logarithmic in $`F/\eta`$ suffices.

The loading circuits preserve exact total occupation even when the interior rotation angles are approximate, provided the boundary cases are exact. Thus, with exact oracle calls, the null hypothesis still has zero false positives. This statement concerns loading error; an approximate synthesized inverse has its own error contribution.

## Inverse-only phase accumulation

The inverse-only endpoint uses one memory qubit and one fresh probe register per invocation. It is a concrete realization of the known measurement-discrimination setting studied by Puchała et al., [arXiv:1810.05122v4, Theorem 1 and Corollary 1](https://arxiv.org/pdf/1810.05122v4), [Quantum 5, 425 (2021)](https://quantum-journal.org/papers/q-2021-04-06-425/).

Put $`\theta_b=b\alpha`$, and define

```math
|\pm_y\rangle=\frac{|0\rangle\pm i|1\rangle}{\sqrt2}.
```

For $`|x_b\rangle=V_b^\dagger|1\rangle`$, direct calculation gives

```math
W_b^\dagger|\pm_y\rangle
=\frac{e^{\pm i\theta_b}}{\sqrt2}
\left(|0\rangle\pm i|x_b\rangle\right).
\tag{I10}
```

Coherently prepare a probe in $`|+_y\rangle`$ if the memory is 0 and $`|-_y\rangle`$ if the memory is 1. Apply $`W_b^\dagger`$ to the probe and measure $`\{P_0,Q\}`$. The memory Kraus operators are

```math
K_0=\frac1{\sqrt2}D_{\theta_b},\qquad
K_Q=\frac{i}{\sqrt2}ZD_{\theta_b},\qquad
D_\theta=\operatorname{diag}(e^{i\theta},e^{-i\theta}).
\tag{I11}
```

After outcome $`Q`$, apply known $`Z`$ to the memory. Both outcomes then implement the same unitary $`D_{\theta_b}`$ up to overall phase. Each outcome has probability $`1/2`$, and the conditioned probe is either $`0`$ or $`x_b`$, independent of the memory state. It can be discarded. The procedure remains valid when the memory is entangled with a reference.

Starting from memory state $`|+\rangle`$, after $`q`$ invocations an $`X`$-basis measurement returns minus with probability

```math
\sin^2(q\theta_b).
\tag{I12}
```

The rounded choices of $`q`$ and their finite success guarantees are stated in the [endpoint theorem](dicke_calibration.md#the-inverse-only-endpoint).

Probe preparation uses only known gates on the $`0,1`$ subspace and a known controlled $`Z`$. Zero tests and resets cost $`O(m)`$ known gates per round. The implementation therefore uses $`O(qm)`$ known gates, $`O(m)`$ live qubits, and $`q`$ actual inverse invocations.

The measurement interpretation follows from

```math
W_bP_0W_b^\dagger=|\psi_b\rangle\langle\psi_b|.
```

On the known two-dimensional span, the effect and its complement form a qubit projective measurement. Puchała et al.'s general result allows perfect discrimination after $`\lceil\pi/(2\alpha)\rceil`$ uses of this measurement channel with an appropriate entangled probe. The elementary circuit above supplies the stated bounded-error endpoint with explicit memory and gate costs.

## Resources with synthesized inverses

The [forward-only construction](forward_only.md) synthesizes only the calibration inverses. Let $`L_d`$ be the number of ordinary forward calls in the chosen inverter. For QURA,

```math
L_d=d\left\lceil\frac{\pi}{2\arcsin(1/d)}\right\rceil-1,
```

and the total number of native forward calls is at most $`F+L_dK`$. The inversion interface and its phase convention are specified in [Forward-only state discrimination](forward_only.md).

QURA reports $`O(d\log d)`$ ancillary qubits; its stated parallel amplification depth is a different resource from an elementary-gate count. See Chen et al., [arXiv:2403.04704v3, Theorem 1, Appendix A, and Table 1](https://arxiv.org/pdf/2403.04704v3).

The inversion ancillas can be reset and reused between calibrations. Including them gives

```math
M_{\rm wide+inv}
=O\!\left(
(F+d)m+F\log^2(F+2)+\operatorname{polylog}(F/\eta)
\right),
\tag{I13}
```

or, with a streaming reservoir,

```math
M_{\rm stream+inv}
=O\!\left(
(K+d+1)m+\operatorname{polylog}(F/\eta)
\right).
\tag{I14}
```

The comparator-history term in (I13) is part of the wide implementation and remains present after inverse synthesis is added.

For a finite gate set, retain the inverter's known-gate cost as a separately charged quantity $`G_{\rm QURA}(d,\delta)`$. Here $`\delta`$ bounds its channel error in half diamond norm. If the loading error is at most $`\eta_{\rm load}`$, then choosing

```math
\eta_{\rm load}+K\delta\le\eta
```

bounds the total additional decision error by $`\eta`$. The known-gate accounting is

```math
G_{\rm total}
=G_{\rm loading}(F,K,d,\eta_{\rm load})
+K\,G_{\rm QURA}(d,\delta).
\tag{I15}
```

The zero-false-positive property holds for the exact oracle/inverter construction; approximate inverse synthesis is covered by the total error budget. No inference of a total elementary-gate bound from QURA's query count or parallel depth is used.

## Connections

The [finite Dicke theorem](dicke_calibration.md), [mixed-query lower bound](mixed_query_lower_bound.md), and [weighted resource tradeoffs](resource_tradeoffs.md) use the actual-call model in [Model](model.md). The synthesized-calibration consequence and its dimension-dependent query bound are developed in [Forward-only state discrimination](forward_only.md). Primary-source comparisons are collected in [Related work](../references/RELATED_WORK.md).
