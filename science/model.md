# Model and exact results

A state-preparation unitary contains more information than the state it prepares on one reference input. With forward access alone, the unused columns can prevent an algorithm from coherently amplifying a small difference between two known outputs. An inverse call can reveal some of those columns. This project determines how a finite inverse budget changes the forward cost of a precise binary decision problem.

The forward-only problem is studied by [Wang, Carolan and Childs](../references/RELATED_WORK.md#wcc2026), following inverse-access separations in quantum algorithms. The question here is the full tradeoff between separately charged query directions. The unitary completion is fixed throughout each experiment, so information acquired from it can remain correlated with later queries.

## The known-state promise

Let $`\mathcal H=\mathbb C^d`$, $`d\ge2`$, with known orthonormal vectors $`|0\rangle,|1\rangle`$. For the main mixed-budget theorem, fix a known number $`0<\epsilon\le1/4`$, and define

```math
c=\sqrt{1-\epsilon^2},\qquad \alpha=\arcsin\epsilon.
```

An unknown unitary $`W`$ obeys one of the two promises

```math
\begin{array}{ll}
b=0:& W|0\rangle=|0\rangle,\\[2mm]
b=1:& W|0\rangle=c|0\rangle+\epsilon|1\rangle.
\end{array}
```

Every other column is unrestricted, subject to unitarity. A single algorithm, given $`d`$ and $`\epsilon`$, must output the correct classical bit with probability at least $`2/3`$ for every completion under either promise. It receives no classical description, extra training states or uncharged oracle-dependent advice.

Define the known rotation

```math
R=\begin{pmatrix}c&-\epsilon\\ \epsilon&c\end{pmatrix}
\oplus I_{d-2},\qquad R_0=I,\quad R_1=R.
```

For every allowed $`W`$, there is a unitary $`V_b`$ fixing $`|0\rangle`$ such that $`W=R_bV_b`$. The upper algorithm works for each such $`V_b`$ independently; it does not assume that the unknown completion is the same under the two alternatives. The lower proof is entitled to choose a correlated pair of completions as a hard ensemble.

## Query and control contract

An ordinary use of $`W`$ counts as one forward query; an ordinary use of $`W^\dagger`$ counts as one inverse query. Their allowed total numbers are $`F,K\in\mathbb Z_{\ge0}`$. The same unknown $`W`$ is reused at all calls. Parallel queries count by the number of oracle ports, not by circuit depth.

The algorithm can use arbitrary oracle-independent ancillas, known unitaries, instruments and intermediate measurements. It may retain its complete measurement record and choose future operations and query directions from that classical record. Every possible measurement history has at most $`F`$ forward and $`K`$ inverse calls. These are hard caps, including branches that stop early, rather than expected query counts.

For the lower bound, one may strengthen this interface by allowing a coherent controlled skip of the currently selected direction. The corresponding physical call still consumes one unit of that direction's budget, even when a component of the query state skips it. The upper algorithms use ordinary, uncontrolled oracle calls. A coherent superposition of the two directions with separately discounted counterfactual costs is not part of the model.

The query lower bound makes no restriction on the amount of known computation or workspace. The constructive results separately provide [gate and memory estimates](implementations.md). Thus an asymptotic improvement in oracle calls does not silently assert the same improvement in elementary gates or elapsed time.

For density operators, use half the trace norm,

```math
D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1.
```

The same formula is used for the subnormalized positive operators that occur inside the proof. They are intermediate mathematical objects; the actual algorithm outputs normalized states and a classical decision.

## U1. Finite calibrated-probe upper bound

For every dimension $`d\ge2`$ and every integer

```math
0\le K\le\left\lfloor\frac1{2\alpha}\right\rfloor,
\qquad
F=\left\lceil\frac{3/(2\alpha^2)+2K^2}{2K+1}\right\rceil,
```

there is an algorithm using at most $`F`$ forward and $`K`$ inverse calls, with zero false positives under $`b=0`$ and success at least $`735/1024>2/3`$ under $`b=1`$, uniformly over all completions.

The algorithm either detects the alternative while calibrating, or obtains $`K`$ exact copies of the unknown state $`|x\rangle=V_b^\dagger|1\rangle`$. It prepares a fixed-occupation symmetric probe from those copies and $`F-K`$ reference states, queries each register once, and measures the total number of outputs orthogonal to $`|0\rangle`$. The null count is exactly $`K`$.

The proof uses exact second and fourth moments of the collective rotation generator and global cosine inequalities. It supplies a finite binary-decision guarantee, not only a local sensitivity or Fisher-information statement. See [Dicke calibration](dicke_calibration.md). The hidden-basis preparation primitive is established by [Ioannou and Mosca](../references/RELATED_WORK.md#im2010).

## L1. Mixed-query distinguishability bound

Let $`n=d-1`$ be a power of two, $`T=F+K\le n/2`$, and choose one Haar-random unitary $`U\in U(n)`$. Put

```math
V=1\oplus U,\qquad W_0=V,\qquad W_1=RV.
```

Let $`\bar\rho_b`$ be the algorithm's final state averaged over this single random completion, including any retained classical record. Then

```math
\begin{aligned}
D(\bar\rho_0,\bar\rho_1)\le{}&
K\sqrt{2(1-c)}
 +\sqrt{2F(1-c)+4\epsilon\sqrt{FK}}\\
&+\frac{4T}{\sqrt{n-T}}
 +\frac{18T(T+1)}{n^{1/8}}.
\end{aligned}
```

The proof covers the complete control contract above. Its central estimate is a potential for inverse-generated path records: the total probability of selected forward outputs is at most the number of inverse calls. The two explicit dimension-dependent terms charge projection leakage and mixed-query Haar simulation. See [the lower-bound proof](mixed_query_lower_bound.md), supported by [the source-derived simulator extension](haar_simulation.md).

In particular, suppose

```math
n\ge 2T+[432T(T+1)]^8+(96T)^2.
```

Then worst-case success at least $`2/3`$ implies

```math
F(K+1)+K^2>10^{-4}\epsilon^{-2}.
```

This is a sufficient dimension condition, not an optimized threshold. It is of order $`T^{16}`$; the register width remains logarithmic in $`T`$ if one chooses the smallest permitted power of two. This observation concerns the number of qubits addressing a black box. It does not construct an efficient physical Haar-random oracle.

## U2. Inverse-only endpoint

For every completion, an inverse-only algorithm uses

```math
F=0,\qquad K=\left\lceil\frac1\alpha\right\rceil
```

and has zero null false positives and alternative success at least $`\sin^2(1)>2/3`$. An explicit sequential construction converts the unknown projective measurement into a deterministic phase rotation of a memory qubit. Its implementation and attribution to established [measurement-discrimination results](../references/RELATED_WORK.md#ppkko2021) are given in [Implementations](implementations.md).

U1, U2 and L1 give the attainable resource boundary

```math
F(K+1)+K^2\asymp\epsilon^{-2}
```

up to universal factors in the sufficiently large dimension regime. The exact rounded constructive budgets and finite necessary condition above take precedence over the informal boundary notation. In particular, when $`K=o(\epsilon^{-1})`$,

```math
F=\Theta\!\left(\frac1{\epsilon^2(K+1)}\right).
```

The [resource account](resource_tradeoffs.md) makes the constant-factor meaning and the expensive-inverse optimization precise.

## C1. Weighted oracle cost

If an inverse call costs $`r\ge1`$ forward-cost units, the minimum cost $`F+rK`$ in the same sufficiently large dimension regime is

```math
\Theta\!\left(\min\left\{\frac{\sqrt r}{\epsilon},\frac1{\epsilon^2}\right\}\right).
```

Here the lower theorem's dimension condition must hold for the budgets under comparison. Known-gate synthesis and memory are separate resources. The proof and an integer allocation rule appear in [Resource tradeoffs](resource_tradeoffs.md).

## C2. Dimension-dependent native-forward upper bound

For every $`d\ge2`$ and $`0<\epsilon\le1`$, the same known-state decision problem can be solved with fewer than

```math
5\min\{\epsilon^{-2},d/\epsilon\}
```

ordinary forward calls and no native inverse calls. This combines U1 with [QURA](../references/RELATED_WORK.md#qura), synthesizing only its calibration inverses. The full interface, phase and integer-rounding argument are in [Forward-only discrimination](forward_only.md).

This is an all-dimension upper bound. L1 does not prove its optimality in fixed dimension. The promise gives two known vectors; it does not give an algorithm for general amplitude estimation with an unknown output state or arbitrary target subspace.

## Proof dependencies and evidence

The upper construction and lower proof are independent. The upper imports a hidden-basis loading method and proves the stated finite-angle guarantee. The lower imports the strong path-recording construction of Ma and Huang, proves the needed controlled-skip and classical-adaptivity extension, and derives a new potential estimate for this discrimination task. The inverse-only endpoint and universal inversion circuit are attributed external constructions. Their combination with the mixed-budget result gives the stated resource consequences.

The [related-work account](../references/RELATED_WORK.md) explains these interfaces and the nearest multiple-resource predecessors. The [finite checks](../verification/README.md) evaluate the constructive algebra on specified cases. They do not constitute a computational verification of the unrestricted adaptive lower bound.
