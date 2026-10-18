# Resource tradeoffs and operational meaning

The [model](model.md) fixes a binary known-state decision problem with separately charged forward and inverse oracle calls. The [calibrated-probe construction](dicke_calibration.md) and [mixed-query lower bound](mixed_query_lower_bound.md) identify the same budget dependence in sufficiently large dimension. This page explains that dependence, optimizes a weighted cost, and compares quantum calibration with a structured classical calibration.

## Meaning of the boundary

Write

```math
S(F,K)=F(K+1)+K^2.
```

The lower theorem states that every successful algorithm in its dimension range has $`S(F,K)>10^{-4}\epsilon^{-2}`$. For upper bounds, the exact budget family in U1 has

```math
F=O\!\left(\frac1{\epsilon^2(K+1)}+K+1\right)
\quad\text{for }K\le\frac1{2\alpha}.
```

In that range $`K+1=O(\epsilon^{-1})`$, so the first term also bounds the other terms up to constants. Larger inverse budgets can use the inverse-only endpoint U2. Thus the boundary scales as $`S(F,K)\asymp\epsilon^{-2}`$; this is not an equality imposed on all feasible budget pairs.

A fully quantified constant-factor interpretation is useful. Set $`k=\min\{K,\lfloor1/(2\alpha)\rfloor\}`$. The U1 circuit is available whenever the allowed forward budget is at least its displayed rounded $`F(k)`$; alternatively U2 is available whenever $`K\ge\lceil1/\alpha\rceil`$. Together these constructions and the necessary inequality give the same asymptotic resource frontier. For example, if $`S(F,K)\ge100\epsilon^{-2}`$, one of these constructions fits within the allowed budgets: if $`K\ge\lceil1/\alpha\rceil`$, use U2; otherwise $`K<1/\alpha`$, so $`K^2<\epsilon^{-2}`$ and $`F(K+1)>99\epsilon^{-2}`$. If $`K\le\lfloor1/(2\alpha)\rfloor`$, the U1 formula gives $`F(K)<4/[\epsilon^2(K+1)]`$. If $`K`$ exceeds that value, choosing $`k=\lfloor1/(2\alpha)\rfloor`$ gives $`k+1>1/(2\alpha)`$ and $`K+1<1/\alpha+1`$; their ratio is less than $`2+2\alpha<3`$, so $`F(k)<12/[\epsilon^2(K+1)]`$. Both fit the available $`F`$.

For $`K=o(\epsilon^{-1})`$, the $`K^2`$ term is negligible compared with $`\epsilon^{-2}`$, giving the particularly simple matched statement

```math
F=\Theta\!\left(\frac1{\epsilon^2(K+1)}\right).
```

| Inverse allocation | Forward scale | Interpretation |
|---|---|---|
| $`K=0`$ | $`\epsilon^{-2}`$ | Direct state preparation and sampling |
| A fixed positive $`K`$ | $`\epsilon^{-2}`$ | A constant calibration budget changes only the constant factor |
| $`K\asymp\epsilon^{-1/2}`$ | $`\epsilon^{-3/2}`$ | A growing calibration budget gives an intermediate gain |
| $`K\asymp\epsilon^{-1}`$ | As small as zero for suitable constants | Inverse-only measurement discrimination reaches the endpoint |

The exact constants at the last row matter: $`K=\Theta(\epsilon^{-1})`$ denotes a scale, while U2 supplies a sufficient integer budget. It is not a claim that every coefficient at that scale permits zero forward calls.

## How inverse calls supply a useful probe

One inverse on $`|1\rangle`$, followed by a known zero test, either determines the answer or gives a copy of $`|x\rangle=V_b^\dagger|1\rangle`$. The state is unknown, but its orthogonality to $`|0\rangle`$ is exact. Coherent routing can therefore arrange $`K`$ such copies among $`F`$ slots without learning their amplitudes.

The fixed-occupation Dicke probe has collective-generator variance

```math
v=F+2K(F-K).
```

For $`K`$ below the inverse-only scale, the useful part of this quantity is proportional to $`F(K+1)`$. The finite-angle proof converts that variance, together with a fourth-moment bound, into a decision experiment. Variance alone would not guarantee a uniform finite success probability.

The lower proof has a corresponding operational accounting: inverse calls create a private record potential, and the selected forward outputs consume it. This gives a global bound even when the algorithm retains and processes everything it has learned. The proof does not assume that calibration copies are independent classical data, that they must be discarded, or that the algorithm follows the upper construction.

## Expensive inverse access

Suppose one inverse costs $`r\ge1`$ forward-cost units. Define $`C=F+rK`$. In the dimension range of L1,

```math
C_{\min}=\Theta\!\left(\min\{\sqrt r/\epsilon,\epsilon^{-2}\}\right).
```

For the lower bound, the elementary estimates $`F\le C`$, $`FK\le C^2/(4r)`$ and $`K^2\le C^2/r^2\le C^2/r`$ imply

```math
S(F,K)\le C+\frac{5C^2}{4r}.
```

If $`C`$ were a sufficiently small constant times both $`\epsilon^{-2}`$ and $`\sqrt r/\epsilon`$, this would violate the necessary bound on $`S`$. This proves the weighted lower bound without assuming any particular allocation.

For an explicit upper allocation, take

```math
k=\left\lfloor\frac1{4\epsilon\sqrt r}\right\rfloor.
```

If $`k\ge1`$, then $`k\ge1/(8\epsilon\sqrt r)`$ and $`k\le1/(4\epsilon)\le1/(2\alpha)`$, using $`\alpha\le2\epsilon`$. U1 gives

```math
F(k)\le\frac{3}{4\alpha^2k}+k+1
\le\frac{6\sqrt r}{\epsilon}+\frac1{4\epsilon\sqrt r}+1,
\qquad rk\le\frac{\sqrt r}{4\epsilon}.
```

Hence $`F(k)+rk=O(\sqrt r/\epsilon)`$. If $`k=0`$, sampling uses $`O(\epsilon^{-2})`$ calls; the condition $`k=0`$ also gives $`\sqrt r/\epsilon>1/(4\epsilon^2)`$, so sampling is within a constant factor of the displayed minimum. The known-gate and memory costs are those of the selected [implementation](implementations.md).

The optimal intermediate allocation is therefore $`K\asymp1/(\epsilon\sqrt r)`$, until integer rounding makes the no-inverse strategy competitive. This is an oracle-cost conclusion. It does not assume that reversing a particular experimental device has a known price or that its noise matches the exact-oracle model.

## A readable calibration can be reused classically

The arbitrary-completion assumption is consequential. Consider the restricted family $`W_b=R_bP_\pi`$, where a permutation $`\pi`$ fixes label $`0`$. One inverse call on $`|1\rangle`$ gives $`|\pi^{-1}(1)\rangle`$ under the null, or

```math
\epsilon|0\rangle+c|\pi^{-1}(1)\rangle
```

under the alternative. A basis measurement either detects label $`0`$, proving the alternative, or produces the classical label $`x=\pi^{-1}(1)`$.

Let $`S_{1x}`$ be the known transposition of labels $`1`$ and $`x`$, fixing $`0`$. Apply this transposition first and then query $`W_b`$. On the two-dimensional signal subspace,

```math
W_bS_{1x}|_{\operatorname{span}\{|0\rangle,|1\rangle\}}=R_b.
```

The order is $`W_bS_{1x}`$. Repeating it $`q=\operatorname{round}(\pi/(2\alpha))`$ times and testing the output gives alternative detection at least $`\cos^2(\alpha/2)`$, with $`F=O(\epsilon^{-1})`$ and $`K=1`$. The label can be stored in $`O(\log d)`$ classical bits and the known transposition implemented with a polynomial number of gates in $`\log d`$.

This is a consequence for the structured permutation family used in [forward-only state-distinguishing work](../references/RELATED_WORK.md#wcc2026). It explains why that family cannot prove the present mixed-budget lower bound. A general calibrated vector does not supply this readable label. Nevertheless, the inability to clone an arbitrary vector would not by itself prove the lower bound: the Dicke experiment uses the available copies collectively and continues querying the correlated oracle. L1 explicitly controls that full process.

## Dimension and implementation

The mixed-query lower bound becomes useful only when its two dimension-error terms are small. Its sufficient dimension has deliberately loose polynomial growth in $`F+K`$. For a fixed smaller dimension, a universal inversion circuit can eventually be worthwhile. Synthesizing only the calibration inverses yields the separate [native-forward bound](forward_only.md), $`O(\min\{\epsilon^{-2},d/\epsilon\})`$.

Two implementations of the calibrated probe are available. The wide circuit uses nearly linear known-gate work in $`F`$ up to logarithmic factors, with $`F`$ data registers and reversible sorting history. Streaming retains only $`K`$ calibration registers and one emitted register, while an explicit multiplexer incurs $`FK`$-scale gate work. The inverse-only endpoint has a small memory implementation. These are different concrete resource choices, all with a one-bit final answer and no QRAM assumption.
