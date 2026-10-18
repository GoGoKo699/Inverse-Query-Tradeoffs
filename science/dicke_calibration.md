# State discrimination by calibrated Dicke probes

Inverse queries can supply unknown states that are coherently distributed across a larger forward probe. For the two-known-state promise, the construction below uses

```math
F=\Theta\!\left(\frac{1}{\epsilon^2(K+1)}\right)
```

forward calls and at most $`K`$ inverse calls for the inverse-budget range in the theorem below, uniformly over every compatible unitary completion. Its finite success guarantee follows from a fourth-moment bound. The gate and memory costs are given in [Implementations](implementations.md); optimization of the two query budgets is in [Resource tradeoffs](resource_tradeoffs.md).

## Model and conventions

Use the [state-discrimination model](model.md). The oracle register has dimension $`d\ge2`$, and the known first-column states are

```math
|\psi_0\rangle=|0\rangle,\qquad
|\psi_1\rangle=c|0\rangle+\epsilon|1\rangle,
\qquad c=\sqrt{1-\epsilon^2}.
```

For the finite theorem assume $`0<\epsilon\le1/4`$, and put

```math
\alpha=\arcsin\epsilon,\qquad
R_0=I,\qquad
R_1=
\begin{pmatrix}
c&-\epsilon\\
\epsilon&c
\end{pmatrix}\oplus I.
```

Under hypothesis $`b`$, write the actual oracle as

```math
W_b=R_bV_b,\qquad V_b|0\rangle=|0\rangle.
```

Each $`V_b`$ is arbitrary. The construction is uniform over the completions and imposes no relation between $`V_0`$ and $`V_1`$. Define

```math
P_0=|0\rangle\langle0|,\qquad Q=I-P_0.
```

These projectors are known. The output is a classical decision bit. Every invocation of $`W_b`$ or $`W_b^\dagger`$ is charged individually, including invocations made in parallel. The algorithm does not require a controlled unknown oracle.

## Finite upper bound

**Theorem.** For any integer

```math
0\le K\le K_{\max}:=\left\lfloor\frac{1}{2\alpha}\right\rfloor,
\qquad
F=\left\lceil
\frac{3/(2\alpha^2)+2K^2}{2K+1}
\right\rceil,
\tag{D1}
```

there is an algorithm using at most $`K`$ inverse calls and at most $`F`$ forward calls such that

```math
\Pr[\widehat b=1\mid b=0]=0,\qquad
\Pr[\widehat b=1\mid b=1]\ge\frac{735}{1024}>\frac23.
\tag{D2}
```

The bounds hold for every compatible completion. The algorithm can stop after a conclusive calibration outcome; the stated counts are hard upper bounds on every measurement history.

### Calibration

Let

```math
|x_b\rangle=V_b^\dagger|1\rangle.
```

Unitarity and $`V_b|0\rangle=|0\rangle`$ imply $`x_b\perp0`$. With the rotation convention above, the relevant adjoint action has a positive sign:

```math
R_1^\dagger|1\rangle=\epsilon|0\rangle+c|1\rangle.
```

One inverse invocation on $`|1\rangle`$ therefore gives

```math
W_0^\dagger|1\rangle=|x_0\rangle,\qquad
W_1^\dagger|1\rangle=\epsilon|0\rangle+c|x_1\rangle.
\tag{D3}
```

Measure $`\{P_0,Q\}`$. Outcome $`P_0`$ is impossible under $`b=0`$, so it certifies $`b=1`$. Otherwise the normalized retained state is exactly $`|x_b\rangle`$.

Repeat this procedure at most $`K`$ times, stopping and outputting 1 after any $`P_0`$ outcome. Conditional on obtaining $`Q`$ throughout, there are exactly $`K`$ copies of $`|x_b\rangle`$. This branch has probability 1 under $`b=0`$ and $`c^{2K}`$ under $`b=1`$. No retries or postselection allowance are needed.

### Loading and forward interrogation

From those copies and $`F-K`$ known blanks, prepare

```math
|D_{F,K}(x_b)\rangle
=\binom{F}{K}^{-1/2}
\sum_{\substack{S\subseteq[F]\\|S|=K}}
|x_b\rangle_S|0\rangle_{\overline S}.
\tag{D4}
```

The [explicit loading circuit](implementations.md#wide-loading-with-reversible-sorting) uses known occupation labels, controlled permutations, and the known zero-state test. It requires no further oracle calls and leaves its routing ancillas clean. Fixed-weight state preparation in such a hidden basis is established by Ioannou and Mosca, [Theorem 1 and Section 2.2](https://arxiv.org/pdf/0810.2780v3).

Apply $`W_b`$ once to each of the $`F`$ data registers. Since $`V_b|x_b\rangle=|1\rangle`$ and $`V_b|0\rangle=|0\rangle`$,

```math
W_b^{\otimes F}|D_{F,K}(x_b)\rangle
=R_b^{\otimes F}|D_{F,K}(1)\rangle.
\tag{D5}
```

Measure the number of output registers in $`Q`$. Output 1 if this weight differs from $`K`$, and output 0 otherwise. Under $`b=0`$, the weight is exactly $`K`$.

The same procedure is insensitive to an unknown overall phase of the state-preparation unitary. Writing $`W_b=e^{i\phi_b}R_bV_b`$, the $`K`$ calibrated states and the $`F`$ forward calls contribute the common overall phase $`e^{i(F-K)\phi_b}`$ to the probe. A phase choice for $`x_b`$ is likewise global because every term in (D4) contains exactly $`K`$ copies.

## Finite-angle success proof

Let $`Y`$ denote Pauli $`Y`$ on $`\operatorname{span}\{|0\rangle,|1\rangle\}`$, extended by zero on its orthogonal complement. Define

```math
G=\sum_{j=1}^{F}Y_j,\qquad
R_1^{\otimes F}=e^{-i\alpha G},\qquad
|D\rangle=|D_{F,K}(1)\rangle.
```

The collective rotation preserves the symmetric logical subspace. Its weight-$`K`$ sector is one-dimensional. Hence the probability of seeing weight $`K`$ under the rotated hypothesis is

```math
|a|^2,\qquad
a=\langle D|e^{-i\alpha G}|D\rangle.
\tag{D6}
```

Weight parity conjugates $`G`$ to $`-G`$ and has $`|D\rangle`$ as an eigenvector. Thus every odd moment vanishes and

```math
a=\langle D|\cos(\alpha G)|D\rangle\in\mathbb R.
```

### Second and fourth moments

Put $`L=F-K`$ and

```math
A=K(L+1),\qquad B=(K+1)L.
```

The operators $`S_+=\sum_j|1\rangle\langle0|_j`$ and $`S_-=S_+^\dagger`$ obey

```math
S_+|D_{F,K}(1)\rangle=\sqrt B\,|D_{F,K+1}(1)\rangle,\qquad
S_-|D_{F,K}(1)\rangle=\sqrt A\,|D_{F,K-1}(1)\rangle.
```

Since $`G=i(S_+-S_-)`$,

```math
v:=\langle D|G^2|D\rangle=A+B=F+2K(F-K).
\tag{D7}
```

Applying $`G`$ twice produces only weights $`K-2,K,K+2`$. Orthogonality of those sectors gives

```math
\begin{aligned}
\langle D|G^4|D\rangle
={}&v^2+K(K-1)(L+1)(L+2)\\
&+(K+1)(K+2)L(L-1).
\end{aligned}
\tag{D8}
```

Terms outside the allowed weight range are zero. The two extra terms are at most $`2A^2`$ and $`2B^2`$, respectively, because

```math
(K-1)(L+2)\le2K(L+1),\qquad
(K+2)(L-1)\le2(K+1)L.
```

Consequently,

```math
\langle G^4\rangle
\le v^2+2(A^2+B^2)\le3v^2.
\tag{D9}
```

### A uniform finite-angle estimate

For every real $`t`$,

```math
1-\frac{t^2}{2}\le\cos t
\le1-\frac{t^2}{2}+\frac{t^4}{24}.
```

Functional calculus and (D9), with $`\gamma=\alpha^2v`$, imply

```math
1-\frac{\gamma}{2}
\le a
\le1-\frac{\gamma}{2}+\frac{\gamma^2}{8}.
\tag{D10}
```

For $`3/2\le\gamma\le2`$, the lower bound is nonnegative. The polynomial on the right decreases on that interval and equals $`17/32`$ at $`\gamma=3/2`$. Therefore

```math
0\le a\le\frac{17}{32},\qquad
1-|a|^2\ge\frac{735}{1024}.
\tag{D11}
```

This is a finite-angle bound, so no local-sensitivity or small-angle approximation is required.

### Checking the rounded budgets

The real expression inside the ceiling in (D1) exceeds $`K`$ by

```math
\frac{3/(2\alpha^2)-K}{2K+1}>0,
```

so $`F\ge K`$. Moreover, $`v=(2K+1)F-2K^2`$ gives

```math
\frac32
\le\alpha^2v
<\frac32+\alpha^2(2K+1)
\le\frac32+\alpha+\alpha^2<2,
\tag{D12}
```

using $`\alpha\le\arcsin(1/4)<0.253`$. Thus (D11) applies.

Including the calibration outcomes, the exact false-negative probability under $`b=1`$ is

```math
c^{2K}|a|^2\le\left(\frac{17}{32}\right)^2.
\tag{D13}
```

This proves (D2). In the range (D1), the ceiling and additive $`K`$ term are $`O(1/[\alpha^2(K+1)])`$, while $`\alpha=\Theta(\epsilon)`$. Hence $`F=\Theta(1/[\epsilon^2(K+1)])`$ uniformly in the permitted integer budget.

For the remaining range $`\epsilon>1/4`$, direct preparation followed by the known occupation measurement uses at most $`\lceil(\ln3)/\epsilon^2\rceil`$ forward calls. Its false-negative probability is at most $`(1-\epsilon^2)^{\lceil(\ln3)/\epsilon^2\rceil}\le1/3`$.

## The inverse-only endpoint

The [single-memory-qubit construction](implementations.md#inverse-only-phase-accumulation) uses $`q`$ inverse calls, no forward calls, and has

```math
\Pr[\widehat b=1\mid b=0]=0,\qquad
\Pr[\widehat b=1\mid b=1]=\sin^2(q\alpha).
\tag{D14}
```

For $`0<\epsilon\le1/4`$, either of the following is sufficient:

```math
q=\left\lceil\frac1\alpha\right\rceil
\quad\Longrightarrow\quad
\Pr[\widehat b=1\mid b=1]\ge\sin^2(1)>\frac23,
```

or

```math
q=\operatorname{round}\!\left(\frac{\pi}{2\alpha}\right)
\quad\Longrightarrow\quad
\Pr[\widehat b=1\mid b=1]\ge\cos^2(\alpha/2)>0.984.
```

This endpoint is an instance of multiple-use von Neumann measurement discrimination: applying $`W_b^\dagger`$ and then testing $`P_0`$ implements the measurement effect $`|\psi_b\rangle\langle\psi_b|`$. The relevant established general results are Puchała et al., [Theorem 1 and Corollary 1](https://arxiv.org/pdf/1810.05122v4), [Quantum 5, 425 (2021)](https://quantum-journal.org/papers/q-2021-04-06-425/). Their measurement-channel optimality statement has that channel interface; the oracle lower bound for the present access model is developed in [Mixed-query lower bound](mixed_query_lower_bound.md).

## Optimality within a fixed-occupation parallel batch

There is a precise restricted statement behind the Dicke enhancement. Consider any probe supported on the logical space $`\{|0\rangle,|x\rangle\}^{\otimes F}`$ with exactly $`K`$ excitations, allowing arbitrary entanglement with an ancilla. Let $`P_K`$ project onto that sector.

After identifying the logical basis with $`0,1`$, put $`\boldsymbol J=\tfrac12\sum_j\boldsymbol\sigma_j`$. The magnetic number is $`m_z=F/2-K`$. Terms changing weight by two vanish between $`P_K`$'s, so

```math
P_KG^2P_K=2P_K(\boldsymbol J^2-J_z^2)P_K.
```

The largest allowed total spin is $`j=F/2`$. It follows that

```math
\|P_KG^2P_K\|
=2\left[\frac F2\left(\frac F2+1\right)
-\left(\frac F2-K\right)^2\right]
=F+2K(F-K).
\tag{D15}
```

The symmetric Dicke state attains this value. For any purification $`|\Phi\rangle`$ in that sector, with the ancilla implicit, the trace distance between the null and rotated probes satisfies

```math
\begin{aligned}
D\!\left(
|\Phi\rangle\langle\Phi|,
e^{-i\alpha G}|\Phi\rangle\langle\Phi|e^{i\alpha G}
\right)
&\le\|(e^{-i\alpha G}-I)|\Phi\rangle\|\\
&\le|\alpha|\sqrt{F+2K(F-K)}.
\end{aligned}
\tag{D16}
```

The second inequality follows from $`|e^{-it}-1|\le|t|`$. Contractivity under partial trace gives the same bound for mixed probes and retained ancillas.

Thus Dicke states maximize the second moment within this fixed-occupation parallel architecture. For paired hypotheses with a common completion, including the conclusive calibration branch adds at most $`1-c^{2K}\le K\epsilon^2`$ to the trace-distance bound. Arbitrary preprocessing and interleaved oracle access require the separate [general lower-bound argument](mixed_query_lower_bound.md).

## Related results

The [implementation note](implementations.md) charges loading gates, coherent storage, and measurements. The [resource-tradeoff note](resource_tradeoffs.md) optimizes $`F`$ and $`K`$, and the [forward-only construction](forward_only.md) replaces just the calibration inverses by a charged synthesis circuit. The result here concerns the fixed two-known-state decision promise in [Model](model.md).

Further comparisons and primary sources are collected in [Related work](../references/RELATED_WORK.md).
