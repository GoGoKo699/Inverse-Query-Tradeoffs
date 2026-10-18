# Forward-only discrimination in finite dimension

The calibrated-probe algorithm needs inverse access only to prepare its calibration states. A universal inversion circuit can synthesize those calls, leaving the larger sensing experiment unchanged. This gives a dimension-dependent forward-only algorithm for the [two-known-state promise](model.md).

## Theorem

For every $`d\ge2`$ and $`0<\epsilon\le1`$, ordinary forward calls to the unknown $`W`$ suffice for a classical decision with worst-case success at least $`2/3`$ using

```math
Q<5\min\{\epsilon^{-2},d/\epsilon\},\qquad K_{\mathrm{native}}=0.
```

The candidate states and $`\epsilon`$ are known, and the rest of $`W`$ is arbitrary. This is a query upper bound. The gate cost of the known universal inversion circuit and its ancillary registers are charged separately below.

## Exact ordinary-call inversion

The QURA construction of [Chen, Mo, Liu, Zhang and Wang](../references/RELATED_WORK.md#qura), Theorem 1 and Appendix A of arXiv:2403.04704v3, implements an unknown inverse using

```math
m_d=\left\lceil\frac{\pi}{2\arcsin(1/d)}\right\rceil,
\qquad
L_d=dm_d-1\le\frac\pi2 d^2+d
```

forward calls. Its Appendix A gives the exact-vector statement for $`SU(d)`$ and returns the ancillary registers to their initial state. The encoder and decoder in Eqs. (A.15), (A.16) and (A.25) use known controlled clock/shift operations around unconditional uses of the unknown unitary or its complex conjugate. The conjugate is implemented with $`d-1`$ ordinary forward calls. Consequently, the inversion interface needed here does not assume a free controlled-$`W`$ oracle.

The $`SU(d)`$ formulation extends to this use of $`U(d)`$ with a harmless global phase. Write $`W=e^{i\phi}V`$, with $`V\in SU(d)`$. The fixed circuit has $`L_d=dm_d-1`$ unconditional oracle calls, so its output on an input $`|\varphi\rangle`$ is

```math
e^{iL_d\phi}V^\dagger|\varphi\rangle
=\det(W)^{m_d}W^\dagger|\varphi\rangle.
```

Every synthesized inverse in the present algorithm acts separately on $`|1\rangle`$. There is no coherent comparison against a branch that skips the synthesis. When calibration succeeds, the probe contains exactly $`K`$ calibrated states, so their individual global phases multiply to one global phase of the whole probe. The phase therefore has no effect on any decision probability.

## Use synthesis only for calibration

For the actual completion, write $`W=R_bV_b`$, $`V_b|0\rangle=|0\rangle`$, and define $`|x\rangle=V_b^\dagger|1\rangle`$. One synthesized inverse on $`|1\rangle`$ gives $`|x\rangle`$ under the null and, up to the common irrelevant synthesis phase,

```math
\epsilon|0\rangle+c|x\rangle
```

under the alternative. The zero outcome of the known projective measurement certifies the alternative. Otherwise the remaining state is exactly $`|x\rangle`$. After at most $`K`$ calibrations, the algorithm either already knows the answer or has $`K`$ exact copies. It never retries a failed calibration, so its query cap is unconditional.

For $`0<\epsilon\le1/4`$, let $`\alpha=\arcsin\epsilon`$. The [finite Dicke theorem](dicke_calibration.md) uses

```math
0\le K\le\left\lfloor\frac1{2\alpha}\right\rfloor,
\qquad
F=\left\lceil\frac{3/(2\alpha^2)+2K^2}{2K+1}\right\rceil
```

and succeeds with probability at least $`735/1024`$ under the alternative, with no null false positives. Replacing just its calibration calls therefore uses at most

```math
Q=F+L_dK
```

native forward queries. In particular, synthesis is not repeated at every sensing step of an amplitude-amplification routine.

## Integer allocation and the uniform constant

For $`0<\epsilon\le1/4`$, choose

```math
K=\left\lfloor\frac1{2d\epsilon}\right\rfloor.
```

Since $`\alpha\le2\epsilon\le d\epsilon`$, this satisfies the upper theorem's restriction. That theorem also gives $`F\ge K`$.

### When calibration is useful

If $`d\epsilon\le1/2`$, then $`K\ge1`$ and

```math
\frac1{4d\epsilon}\le K\le\frac1{2d\epsilon}.
```

Using $`\alpha\ge\epsilon`$ and the ceiling bound gives

```math
F\le\frac{3}{4\alpha^2K}+K+1
\le\frac{3d}{\epsilon}+\frac1{2d\epsilon}+1,
\qquad
L_dK\le\frac{\pi d}{4\epsilon}+\frac1{2\epsilon}.
```

Hence

```math
Q\le\frac d\epsilon
\left(3+\frac\pi4+\frac1{2d^2}+\frac1{2d}+\frac\epsilon d\right)
<\frac{5d}{\epsilon}.
```

Here $`\min\{\epsilon^{-2},d/\epsilon\}=d/\epsilon`$.

### When the integer calibration budget is zero

If $`d\epsilon>1/2`$, then $`K=0`$ and

```math
Q=F\le\frac{3}{2\epsilon^2}+1
\le\frac{25}{16}\epsilon^{-2}
\le\frac{25}{8}\min\{\epsilon^{-2},d/\epsilon\}.
```

The last inequality also covers the crossover $`1/2<d\epsilon<1`$. No assumption that the real-valued optimum is an integer is needed.

### Larger state separation

For $`\epsilon>1/4`$, prepare $`W|0\rangle`$ and test whether it is orthogonal to $`|0\rangle`$ on each of

```math
N=\left\lceil\frac{\ln3}{\epsilon^2}\right\rceil
```

independent trials. The alternative failure probability is at most $`(1-\epsilon^2)^N\le e^{-N\epsilon^2}\le1/3`$. Also

```math
\frac{N}{\epsilon^{-2}}\le\ln3+\epsilon^2<5,
\qquad
\frac{N}{d/\epsilon}\le\frac{\ln3}{d\epsilon}+\frac\epsilon d
<2\ln3+\frac12<5,
```

because $`d\epsilon>1/2`$. This proves the uniform constant in the theorem over its entire parameter range.

## Ancillas, known gates and precision

Let $`\eta`$ be the probe-loading trace-error tolerance. QURA reports $`O(d\log d)`$ ancillary qubits. Its returned ancillas can be reset and reused between calibrations. Combined with the [wide probe implementation](implementations.md), the live quantum memory is

```math
O\!\left((F+d)\log d+F\log^2(F+2)+\operatorname{polylog}(F/\eta)\right).
```

The reversible comparator history contributes the $`F\log^2(F+2)`$ term. With the streaming reservoir instead, quantum memory is

```math
O\!\left((K+d+1)\log d+\operatorname{polylog}(F/\eta)\right),
```

with the larger, explicitly charged streaming gate work described in the implementation page.

Let $`G_{\mathrm{QURA}}(d,\delta)`$ denote the number of known elementary gates used to compile the specified QURA circuit to half-diamond-norm channel error at most $`\delta`$. The complete known-gate cost is the chosen probe implementation plus

```math
K\,G_{\mathrm{QURA}}\!\left(d,\frac{\eta_{\mathrm{inv}}}{\max\{K,1\}}\right).
```

This term is not declared negligible or identified with the number of amplification layers. QURA's stated $`O(d)`$ computational-depth figure counts parallel layers containing multiple oracle uses; it is not an elementary-gate bound. The query theorem uses its explicit inversion circuit, and makes no end-to-end runtime claim uniform in $`d`$.

With ideal known gates, inversion is exact and the one-sided guarantee above applies. With compiled gates, a telescoping channel-error bound and trace-distance contractivity through the full calibration instrument give total degradation at most $`\eta_{\mathrm{inv}}+\eta_{\mathrm{prep}}`$. No division by a postselection probability is needed because all branches, including early decisions, are retained. A total error of $`0.01`$ still leaves success above $`2/3`$. Approximate inversion need not preserve exactly zero false positives. No tomography of $`x`$, QRAM or classical description of the unknown unitary is supplied.

## Relation to existing dimension-dependent bounds

[Wang, Carolan and Childs](../references/RELATED_WORK.md#wcc2026), Sections 1.1 and 1.3, formulate this same two-known-state decision problem and list an $`O(d^{3/2}/\epsilon)`$ dimension-dependent upper bound. Together with direct sampling, the comparison stated there is $`O(\min\{\epsilon^{-2},d^{3/2}/\epsilon\})`$. The construction above improves that bound to $`O(\min\{\epsilon^{-2},d/\epsilon\})`$ for the specified promise.

[Kean Chen](../references/RELATED_WORK.md#chen2025), Corollary 1.5, obtains the former scale for general amplitude estimation, and Section 1.4 conjectures a $`\Theta(\min\{d/\epsilon,\epsilon^{-2}\})`$ law for that broader problem. Attaining its expression here does not prove the broader conjecture: this algorithm uses two explicitly known possible output vectors. Nor does the present [large-dimension lower bound](mixed_query_lower_bound.md) establish an optimal finite-dimensional converse.
