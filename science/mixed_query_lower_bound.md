# A lower bound for mixed forward and inverse queries

The promise is to decide whether an unknown unitary prepares $`|0\rangle`$ or the known nearby state $`c|0\rangle+\epsilon|1\rangle`$, where $`c=\sqrt{1-\epsilon^2}`$. The algorithm may query the unitary in both directions, with separate hard budgets. We prove that constant-success discrimination requires

```math
F(K+1)+K^2=\Omega(\epsilon^{-2})
```

in sufficiently large dimension. Here $`F`$ counts forward calls and $`K`$ counts inverse calls. The proof gives an explicit finite-dimensional trace-distance estimate and a sufficient dimension, rather than inferring a tradeoff from the two endpoint query complexities.

## 1. Model and theorem

Let the query space be

```math
\mathcal H=\operatorname{span}\{|0\rangle\}\oplus\mathcal H_Q,
\qquad \dim\mathcal H_Q=n=d-1,
```

where $`n`$ is a power of two. Label an orthonormal basis of $`\mathcal H_Q`$ by $`1,\ldots,n`$. Define

```math
R_\epsilon=
\begin{pmatrix}c&-\epsilon\\ \epsilon&c\end{pmatrix}
\oplus I_{d-2},
\qquad c=\sqrt{1-\epsilon^2},
\qquad \delta_\epsilon=\|R_\epsilon-I\|=\sqrt{2(1-c)}.
```

For the lower-bound distribution, sample $`U`$ once from Haar measure on $`U(n)`$ and set

```math
V=1\oplus U,\qquad W_0=V,\qquad W_1=R_\epsilon V.
```

The same sampled unitary is reused at every query. Each ensemble is supported on the corresponding first-column promise. An algorithm that succeeds for every allowed completion must therefore succeed on these ensembles.

The algorithm starts in an oracle-independent state and may use arbitrary ancillary registers, known operations, intermediate measurements, and classical randomness. The next query direction may depend on the classical measurement history. On every history, it makes at most $`F`$ forward calls and at most $`K`$ inverse calls. A coherently controlled invocation, which applies the oracle only on one control sector, counts as one physical call of its chosen direction, regardless of the control amplitude. No separate discounted budgets are assigned to the counterfactual branches of a coherent forward/inverse superposition.

Write $`T=F+K`$. We assume $`T\le n/2`$. All measurements and discarded registers may be purified for analysis, retaining immutable copies of the classical outcomes. Let $`\bar\rho_b`$ be the Haar-averaged final accessible state under hypothesis $`b`$. We use

```math
D(X,Y)=\frac12\|X-Y\|_1
```

also for subnormalized positive operators. The physical states $`\bar\rho_b`$ themselves are normalized.

### Theorem MQ.1 — Finite-dimensional distinguishability

For the model above and $`0<\epsilon\le1`$,

```math
\boxed{
\begin{aligned}
D(\bar\rho_0,\bar\rho_1)
\le {}&K\delta_\epsilon
+\sqrt{2F(1-c)+4\epsilon\sqrt{FK}}\\
&+\frac{4T}{\sqrt{n-T}}
+\frac{18T(T+1)}{n^{1/8}}.
\end{aligned}}
\tag{1}
```

The first two terms quantify the separate query budgets. The third is a projection error proved below. The fourth comes from strong Haar simulation.

### Corollary MQ.2 — Constant success

Suppose $`0<\epsilon\le1/2`$ and $`n`$ is a power of two satisfying

```math
n\ge 2T+\bigl(432T(T+1)\bigr)^8+(96T)^2.
\tag{2}
```

If the equal-prior, Haar-averaged binary decision success is at least $`2/3`$, then

```math
\boxed{F(K+1)+K^2>10^{-4}\epsilon^{-2}.}
\tag{3}
```

In particular, the same conclusion holds for a worst-case success guarantee over all promised completions. The large exponent in (2) is sufficient for this proof; it is not asserted to be necessary.

## 2. Imported Haar-simulation result

We use [Lemma HS.1, Controlled strong Haar simulation](haar_simulation.md#lemma-hs1-controlled-strong-haar-simulation). Its assumptions are precisely the dimension and physical-query conventions above: $`n`$ is a power of two, $`T\le n/2`$, the same Haar matrix is used throughout, and classical adaptive directions are represented with retained outcome histories. The lemma permits coherently inactive sectors.

With empty initial record registers, replacing $`U,U^\dagger`$ by a common strong path-recording contraction $`M,M^\dagger`$ changes the averaged accessible output by at most

```math
\eta_n(T)=\frac{9T(T+1)}{n^{1/8}}
\tag{4}
```

in half trace norm. The simulator output may be subnormalized and is never renormalized. The result applies to $`1\oplus U`$ through its known inactive one-dimensional sector. For $`W_1`$, the known factor $`R_\epsilon`$ is placed after a forward query and before an inverse query.

The cited chapter proves the control/history extension of the source argument; it is not a verbatim consequence of an uncontrolled-query statement. Its source is Ma–Huang [MH, Theorem 8, Eq. (9.5)]. We import that extension as a proved lemma. The stronger error from the source's forward-only theorem is not used here. Applying (4) separately to the two hypotheses contributes $`2\eta_n(T)`$ to (1).

We next define the record operations needed for the rest of the proof. These are [MH, Definition 25, Eqs. (8.1)–(8.2), and Definition 26, Eq. (8.6)], with the source's strong oracle $`V`$ renamed $`M`$.

## 3. Record space and oracle

A relation is a multiset of pairs $`(x,y)\in[n]^2`$. Its size counts multiplicity. Its domain and image are ordinary sets:

```math
\operatorname{Dom}(L)=\{x:(x,y)\in L\text{ for some }y\},
\qquad
\operatorname{Im}(L)=\{y:(x,y)\in L\text{ for some }x\}.
```

The inaccessible database has orthonormal basis vectors $`|L,R\rangle`$, indexed by two relations. Equal multisets give the same basis vector; different multisets give orthogonal vectors. This is the relation-state representation of [MH, Section 2.1]. The combined record length is $`|L|+|R|`$.

On inputs of combined length at most $`n-1`$, define the left and right append maps

```math
\begin{aligned}
A|x,L,R\rangle
&=\frac1{\sqrt{n-|\operatorname{Im}(L\cup R)|}}
\sum_{y\notin\operatorname{Im}(L\cup R)}
|y,L\cup\{(x,y)\},R\rangle,\\
B|y,L,R\rangle
&=\frac1{\sqrt{n-|\operatorname{Dom}(L\cup R)|}}
\sum_{x\notin\operatorname{Dom}(L\cup R)}
|x,L,R\cup\{(x,y)\}\rangle.
\end{aligned}
\tag{5}
```

They are zero on the orthogonal complement of their domains. The fresh image label in $`A`$ identifies the appended left pair; the fresh domain label in $`B`$ identifies the appended right pair. Their images for distinct input basis vectors are orthogonal, and each image has norm one. Thus $`A`$ and $`B`$ are partial isometries. Their adjoints delete a compatible record, with the corresponding normalization.

The strong path oracle is

```math
M=A(I-BB^\dagger)+(I-AA^\dagger)B^\dagger.
\tag{6}
```

It is a partial isometry and hence a contraction [MH, Claim 15]. Both $`M`$ and $`M^\dagger`$ change the total record length by at most one. Consequently every state after $`t`$ physical query layers is supported on lengths at most $`t`$. Coherent skips do not increase the length.

## 4. A projected oracle and its exact number identity

Let $`\Gamma`$ be the database projector onto relations with **no left pair whose output label is $`1`$**. Right pairs with that output label are allowed. Define the nonnegative number operator

```math
N|L,R\rangle
=\left(\sum_{x=1}^n\operatorname{mult}_R(x,1)\right)|L,R\rangle,
\qquad P=|1\rangle\langle1|.
\tag{7}
```

Thus $`N`$ counts right pairs with output $`1`$, including multiplicity. It acts only on the inaccessible database and commutes with every known algorithm operation.

Because $`B`$ does not modify $`L`$, both $`B`$ and $`B^\dagger`$ commute with $`\Gamma`$. Deleting a left record cannot create a forbidden output label, so $`A^\dagger`$ preserves the range of $`\Gamma`$. On that range put

```math
A_0=\Gamma A\Gamma,\qquad C=\Gamma M\Gamma.
```

Compression preserves contractivity. Moreover,

```math
C=A_0(I-BB^\dagger)+(I-A_0A_0^\dagger)B^\dagger,
\tag{8}
```

where the identities are on the range of $`\Gamma`$. To obtain (8), use $`A^\dagger\Gamma=\Gamma A^\dagger\Gamma`$, which implies $`\Gamma AA^\dagger\Gamma=A_0A_0^\dagger`$.

The append rules give four exact identities:

```math
[A_0,N]=0,\qquad PA_0=0,\qquad
NB=B(N+P),\qquad [BB^\dagger,N]=0.
\tag{9}
```

The first holds because a left append leaves the right database unchanged. The second holds because any left append with query output $`1`$ is removed by $`\Gamma`$. For the third, a right append increases $`N`$ exactly when its query input is $`1`$. Taking its adjoint gives $`B^\dagger N=(N+P)B^\dagger`$, which also proves the fourth identity.

Substitution into (8) yields the main algebraic relation:

```math
\boxed{(N+P)C=CN.}
\tag{10}
```

For the left-append term, $`(N+P)A_0=A_0N`$ and $`N`$ commutes with $`BB^\dagger`$. For the other term, write $`H=A_0A_0^\dagger`$. Then $`[H,N]=0`$ and $`PH=HP=0`$. Since $`NB^\dagger=B^\dagger N-PB^\dagger`$,

```math
\begin{aligned}
(N+P)(I-H)B^\dagger
&=(I-H)(B^\dagger N-PB^\dagger)+PB^\dagger\\
&=(I-H)B^\dagger N.
\end{aligned}
```

Extend the projected oracle to the physical query space as $`C\mapsto 1\oplus C`$. The identity sector acts on $`|0\rangle`$ and leaves the database unchanged. Equation (10) still holds, with $`P`$ zero on that sector. We henceforth use $`C`$ for this extension when the query register has dimension $`d`$.

## 5. Forward use consumes the number potential

Equation (10) and its adjoint imply

```math
[C^\dagger C,N]=0,
\qquad
[CC^\dagger,N+P]=0.
```

Since $`C^\dagger C\le I`$ and $`CC^\dagger\le I`$, for every possibly subnormalized vector $`z`$,

```math
\begin{aligned}
\langle Cz|(N+P)|Cz\rangle
&=\langle z|NC^\dagger C|z\rangle
\le\langle z|N|z\rangle,\\
\langle C^\dagger z|N|C^\dagger z\rangle
&=\langle z|(N+P)CC^\dagger|z\rangle
\le\langle z|(N+P)|z\rangle.
\end{aligned}
\tag{11}
```

The products in these inequalities are ordered correctly because the stated operators commute and are positive. No state is normalized after applying $`C`$.

A forward query therefore reduces the expected value of $`N`$ by at least its output probability on $`|1\rangle`$. An inverse query increases the expectation by at most its input probability on $`|1\rangle`$, and hence by at most its input squared norm. Known gates, measurements with their outcomes retained, and the known factor $`R_\epsilon`$ commute with $`N`$.

For an additional coherent query control $`E`$, use

```math
\widehat C=(I-E)\otimes I+E\otimes C,
\qquad P_E=E\otimes P.
```

Equation (10) becomes $`(N+P_E)\widehat C=\widehat C N`$. Thus the consumed probability is restricted to the active control sector, while the cost remains the entire physical invocation.

Starting with an empty database, sum (11) over the computation. If $`p_{b,t}`$ is the active forward-output probability on $`|1\rangle`$ at physical time slot $`t`$ in either of the projected comparison processes used below, then

```math
\boxed{\sum_t p_{b,t}\le K.}
\tag{12}
```

Indeed, every inverse contributes at most its prequery weight, all forward contributions decrease the potential, and the final potential is nonnegative.

### Hard budgets for subnormalized adaptive histories

The weighted statement in (12) needs the hard budget, rather than an assumption that every time slot has the same query direction. Retain the measurement history, including the counters of physical forward and inverse calls. Let $`w_{b,t}`$ denote the prequery weight of histories requesting a physical forward call at time slot $`t`$. The coherent skip control is not used to discount $`w_{b,t}`$.

Then

```math
\sum_t w_{b,t}\le F,
\qquad
\sum_t w^{\mathrm{inv}}_{b,t}\le K.
\tag{13}
```

These inequalities also hold in a projected process. Complete each contraction by a failure outcome, retain that outcome, and halt on failure. The prequery weights in the successful component are unchanged, and every resulting trajectory respects the original hard caps.

Equivalently, let $`B_f`$ be the diagonal operator giving the remaining forward budget on each classical-history sector, and let $`\Pi_f`$ select sectors requesting a forward call. On legal inputs $`B_f-\Pi_f\ge0`$. The successful query contraction preserves each history sector except for incrementing its counter. Therefore

```math
\mathbb E[B_f\text{ after success}]
\le \mathbb E[B_f\text{ before}]-\|\Pi_f z\|^2.
```

Known operations leave the remaining budget unchanged. Telescoping from the initial value $`F`$ proves the first inequality in (13); the inverse case is identical. Combining the second inequality with (11) proves (12) for adaptive schedules.

## 6. Removing the inverse rotations

The two compressed processes query

```math
\begin{array}{c|cc}
 &\text{forward}&\text{inverse}\\ \hline
b=0&C&C^\dagger\\
b=1&R_\epsilon C&C^\dagger R_\epsilon^\dagger
\end{array}
```

with the appropriate coherent controls when present. First compare the rotated process with a hybrid that keeps its forward operation $`R_\epsilon C`$ but replaces every inverse operation by $`C^\dagger`$.

For one such replacement,

```math
\|C^\dagger R_\epsilon^\dagger-C^\dagger\|
\le\|R_\epsilon-I\|=\delta_\epsilon.
\tag{14}
```

An ordinal inverse-event hybrid makes this a $`K\delta_\epsilon`$ bound even when the query direction is chosen adaptively.

For $`j=1,\ldots,K`$, collect the branches just before their $`j`$th requested inverse call. The boundary space is a direct sum over immutable classical histories, including the routing of the query register and the original position in the computation. Branches that have halted occupy a permanent done sector. Between two such boundaries, let $`B_j`$ be the common Stinespring contraction that runs all intervening known operations, measurements, and forward queries until the next inverse is requested or the branch halts. These maps are the same in the two compared processes because their forward operations are held fixed.

At boundary $`j`$, let

```math
J_j(A)=\bigoplus_{h\text{ active}}A_h\ \oplus I_{\mathrm{done}},
```

where $`A_h`$ is the inverse operation on that history's query register. Any coherent skip is inside $`A_h`$. Orthogonality of the history sectors and (14) give

```math
\|J_j(C^\dagger R_\epsilon^\dagger)-J_j(C^\dagger)\|
\le\delta_\epsilon.
```

Padding done sectors with identity expresses the complete process as

```math
B_KJ_K(A)B_{K-1}\cdots B_1J_1(A)B_0.
```

Every factor is a contraction. A product hybrid over its $`K`$ inverse boundaries therefore proves

```math
\|\Psi_1-\Psi_{\mathrm{hyb}}\|\le K\delta_\epsilon.
\tag{15}
```

The argument uses classical histories to collect inverse events of the same ordinal number even when they occur at different physical times. It does not make the invalid inference that a bound on the sum of inverse-query probabilities also bounds the sum of their square roots. It applies to the subnormalized projected process without any renormalization.

## 7. Comparing the forward operations

It remains to compare the null process and the hybrid. They have the common inverse $`C^\dagger`$; their forward operations are $`C`$ and $`R_\epsilon C`$.

First consider a forward call without an additional control. For prequery vectors $`u,v`$, put $`a=Cu`$ and $`b=Cv`$. Because $`R_\epsilon`$ is unitary,

```math
\|a-R_\epsilon b\|^2
=\|a-b\|^2+2\operatorname{Re}\langle a|(I-R_\epsilon)b\rangle.
\tag{16}
```

Write $`P_0=|0\rangle\langle0|`$. On the distinguished plane,

```math
I-R_\epsilon
=(1-c)(P_0+P)
+\epsilon|0\rangle\langle1|-\epsilon|1\rangle\langle0|.
```

The diagonal term is bounded by $`(1-c)\|a\|\|b\|`$. For the off-diagonal terms, use

```math
\begin{aligned}
|\langle a|0\rangle\langle1|b\rangle|
&\le\|a\|\,\|Pb\|,\\
|\langle a|1\rangle\langle0|b\rangle|
&\le\|Pa\|\,\|b\|.
\end{aligned}
```

With ancillary registers, these are the same inequalities after Cauchy–Schwarz on the remaining factors. Contractivity of $`C`$ and vector norms at most one imply

```math
\|a-R_\epsilon b\|^2
\le\|u-v\|^2+2(1-c)+2\epsilon(\|Pa\|+\|Pb\|).
\tag{17}
```

This elementary rotation comparison is also the type of squared-distance expansion used in [WCC, Section 4.2]. Here the cumulative control of its output-$`1`$ terms comes from the number identity (10).

### Weighted comparison for adaptive directions

Unroll the retained-history process into at most $`T`$ physical-query slots. At each slot, forward, inverse, and halted histories occupy orthogonal sectors. All inverse and halted operations are common contractions and cannot increase the squared distance. For the forward histories, let $`w_{0,t},w_{1,t}`$ be the prequery weights defined in (13). Let $`p_{0,t},p_{1,t}`$ be their active output-$`1`$ probabilities immediately after $`C`$ and before the extra rotation.

Apply (16) only to the active forward controls. Bounding the two output norms by the corresponding prequery norms gives the squared-distance increment

```math
\Delta_t\le
2(1-c)\sqrt{w_{0,t}w_{1,t}}
+2\epsilon\left(
\sqrt{w_{0,t}p_{1,t}}+
\sqrt{p_{0,t}w_{1,t}}
\right).
\tag{18}
```

The first term may use the larger physical-call weights even when part of the control is inactive. The other terms retain the active output probabilities needed by (12). The history-sector decomposition is orthogonal in the common purification, so no incoherent averaging of a quantum query control is being assumed.

Equations (12)–(13) and Cauchy–Schwarz imply

```math
\begin{aligned}
\sum_t\sqrt{w_{0,t}w_{1,t}}&\le F,\\
\sum_t\sqrt{w_{0,t}p_{1,t}}&\le\sqrt{FK},\\
\sum_t\sqrt{p_{0,t}w_{1,t}}&\le\sqrt{FK}.
\end{aligned}
```

Known interleaving operations are common isometries in the purification. Summing (18), starting from identical initial vectors, proves

```math
\|\Psi_0-\Psi_{\mathrm{hyb}}\|^2
\le 2F(1-c)+4\epsilon\sqrt{FK}.
\tag{19}
```

Combining (15) and (19) gives the first two terms of (1) for the compressed processes.

For clarity, the passage to half trace norm does not require normalization. Whenever $`\|u\|,\|v\|\le1`$,

```math
\begin{aligned}
D(|u\rangle\langle u|,|v\rangle\langle v|)
&\le\tfrac12(\|u\|+\|v\|)\|u-v\|\\
&\le\|u-v\|.
\end{aligned}
\tag{20}
```

This follows by writing the difference of rank-one operators as $`|u-v\rangle\langle u|+|v\rangle\langle u-v|`$. Partial trace is contractive for this Hermitian difference.

## 8. Leakage from the projected database

We now bound the cost of replacing the full path oracle $`M`$ by $`C=\Gamma M\Gamma`$. This is separate from the imported Haar-simulation error.

On inputs of combined record length at most $`t`$ in the range of $`\Gamma`$, define

```math
D_L=(I-\Gamma)A\Gamma.
```

We claim

```math
\|D_L\|\le\frac1{\sqrt{n-t}}.
\tag{21}
```

If label $`1`$ already occurs in the right image, the append rule forbids that output and the leaking component is zero. Otherwise the only leaking summand appends $`(x,1)`$ to $`L`$ and has coefficient

```math
\frac1{\sqrt{n-|\operatorname{Im}(L\cup R)|}}
\le\frac1{\sqrt{n-t}}.
```

The new left relation has a unique pair with output $`1`$, since there was none before. Deleting that pair recovers both $`x`$ and the old left relation, while the right relation is unchanged. Different input basis vectors therefore give orthogonal leaking outputs. This proves the operator-norm estimate on arbitrary superpositions, including relations with multiplicities; it is not just a bound for basis-state inputs.

Using the commutation of $`B,B^\dagger`$ with $`\Gamma`$ and preservation of its range by $`A^\dagger`$, equation (6) gives

```math
\begin{aligned}
(I-\Gamma)M\Gamma
&=D_L(I-BB^\dagger)\Gamma-D_LA^\dagger B^\dagger\Gamma,\\
(I-\Gamma)M^\dagger\Gamma
&=-BD_LA^\dagger\Gamma.
\end{aligned}
\tag{22}
```

All factors other than $`D_L`$ are contractions. Every intermediate input to $`D_L`$ in (22) has length at most $`t`$. Thus

```math
\|(I-\Gamma)M\Gamma\|\le\frac2{\sqrt{n-t}},
\qquad
\|(I-\Gamma)M^\dagger\Gamma\|\le\frac1{\sqrt{n-t}}.
\tag{23}
```

The fixed $`|0\rangle`$ block has zero leakage, and coherent query controls cannot enlarge these operator norms. Known algorithm operations and $`R_\epsilon`$ commute with $`\Gamma`$.

In a product hybrid between the full path process and its compression, choose the factors before each replaced query from the compressed process. Its input is then in the range of $`\Gamma`$. There are at most $`T`$ physical slots and all remaining factors are contractions. Using the common denominator $`\sqrt{n-T}`$ in (23), the Euclidean error for each hypothesis is at most

```math
\frac{2T}{\sqrt{n-T}}.
\tag{24}
```

Equation (20) and partial trace give the same half-trace-norm bound. Comparing both hypotheses pays twice (24), yielding the third term of (1).

## 9. Completing the theorem and evaluating the constants

There are three comparisons: each physical Haar ensemble with its full path simulator, each full simulator with its compression, and the two compressed processes with one another. Their respective total bounds are

```math
2\eta_n(T),\qquad
\frac{4T}{\sqrt{n-T}},\qquad
K\delta_\epsilon+\sqrt{2F(1-c)+4\epsilon\sqrt{FK}}.
```

The triangle inequality proves Theorem MQ.1.

To obtain the constant-success consequence, put

```math
S=F(K+1)+K^2.
```

For $`0<\epsilon\le1/2`$, we have $`\delta_\epsilon\le\sqrt2\epsilon`$ and $`2(1-c)\le2\epsilon^2`$. Since $`F`$, $`FK`$, and $`K^2`$ are each at most $`S`$, the first two terms of (1) are bounded by

```math
\sqrt{2\epsilon^2S}
+\sqrt{2\epsilon^2S+4\epsilon\sqrt S}.
\tag{25}
```

For any $`\eta>0`$, the sufficient dimension condition

```math
n\ge 2T+
\left(\frac{36T(T+1)}\eta\right)^8+
\left(\frac{8T}\eta\right)^2
\tag{26}
```

puts each finite-dimensional term in (1) at most $`\eta/2`$. Taking $`\eta=1/12`$ gives (2). A power of two at least the threshold, and at least one, is sufficient.

If $`\epsilon^2S\le10^{-4}`$, expression (25) is at most

```math
\sqrt{0.0002}+\sqrt{0.0402}<0.215.
```

After adding $`1/12`$, equation (1) gives $`D(\bar\rho_0,\bar\rho_1)<0.299<1/3`$. For normalized states with equal priors, binary discrimination success is at most $`(1+D)/2`$. Success at least $`2/3`$ would require $`D\ge1/3`$, a contradiction. This proves Corollary MQ.2.

## 10. Meaning and limits of the bound

The number operator is a private record potential, not an observable supplied to the algorithm. After the small leakage sector is removed, inverse queries can increase that potential, while forward output amplitude on the distinguished direction consumes it. This allows a single forward output probability to be large and still bounds its accumulated contribution over the whole algorithm.

The proof grants unlimited oracle-independent computation and workspace. It makes no efficient-circuit claim for the sampled Haar completion. The dimension condition is inherited largely from the available mixed-query simulation estimate and leaves the optimal finite-dimensional tradeoff unresolved. The trace-distance dependence at very small distinguishing advantage is also not claimed to be tight.

All separate-budget arguments above use fixed or classically adaptive query directions. Coherent skipping is included at full physical-call cost. A model assigning separate discounted budgets to branches of a coherent direction superposition would require an additional query-accounting argument and is outside Theorem MQ.1.

## References

- **[MH]** Fermi Ma and Hsin-Yuan Huang, *How to Construct Random Unitaries*, arXiv:2410.10116v3, 21 May 2025. [Versioned HTML](https://arxiv.org/html/2410.10116v3), [versioned PDF](https://arxiv.org/pdf/2410.10116v3). Relevant locations: Section 2.1; Definition 25, Eqs. (8.1)–(8.2); Definition 26, Eq. (8.6); Claim 15; Theorem 8, Eq. (9.5). The controlled simulation proof and its source dependencies are given in [Haar simulation](haar_simulation.md).
- **[WCC]** Emma Wang, Joseph Carolan and Andrew M. Childs, *On State Distinguishing Without Inverse Queries*, arXiv:2610.05389v1, 4 October 2026. [Versioned HTML](https://arxiv.org/html/2610.05389v1), [versioned PDF](https://arxiv.org/pdf/2610.05389v1). Section 1.1 defines the known-column decision promise; Section 4.2 develops the elementary rotation-based squared-distance comparison for its forward-only lower bound.
