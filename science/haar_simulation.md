# Haar simulation with coherent skips and classical adaptation

This section proves an extension of the strong path-recording simulation in Fermi Ma and Hsin-Yuan Huang, *How to Construct Random Unitaries*, [arXiv:2410.10116v3, 21 May 2025](https://arxiv.org/html/2410.10116v3), abbreviated **MH** ([MH2025](../references/RELATED_WORK.md#mh2025)). The extension is derived below; it is not the printed statement of MH Theorem 8.

Throughout this section, **n denotes the dimension of the Haar block**, not a number of qubits. Thus MH's dimension N is our n, and MH's number of qubits is $`\log_2 n`$. We retain the conservative condition T≤n/2 because the proof restatement MH Lemma 11.2 uses that range, although the earlier statement of MH Lemma 9.2 gives a larger range.

## Lemma HS.1 Controlled strong Haar simulation

Let n be a power of two and let T be a nonnegative integer with T≤n/2. Sample U from Haar measure on U(n) once and reuse this same matrix throughout an algorithm. The algorithm starts independently of U and has arbitrary workspace and arbitrary U-independent interventions. It may make at most T physical oracle invocations, selecting forward or inverse direction classically from retained measurement histories. A physical invocation may be coherently skipped on a control register; its query cost is independent of the control amplitude. Early termination is allowed.

Replace each active U by the strong path-recording contraction M defined below, each active U† by M†, and each inactive block by the identity, with initially empty left and right records. Retain the same interventions, controls, histories, and final output channel. Let ρ_U be the physical output state and let τ_M be the resulting, possibly subnormalized, simulator output after tracing out the records. Then

```math
D_{\rm tr}\left(\mathbb E_U\rho_U,\tau_M\right)
\le \eta_n(T):=\frac{9T(T+1)}{n^{1/8}},
\qquad
D_{\rm tr}(X,Y):=\frac12\|X-Y\|_1.
\tag{HS.1}
```

The initial state may be entangled with a reference independent of U; that reference can be included in the workspace. The statement makes no efficiency assumption on the interventions. It makes no claim about expected query costs or about charging a coherent choice of direction by its branch amplitudes.

The proof actually establishes (HS.1) for the mathematical switched-query model below with T layers, including coherent superpositions of the two directions. That stronger interface is used only to purify the chosen classical adaptive model; no implementation of a coherent direction switch at the cost of one physical query is assumed.

### The switched-query interface

Let A≅Cⁿ be the oracle data register and let S be a separate control register. At layer j, let P₀,j, P₊,j, P₋,j be known, mutually orthogonal projectors on S summing to the identity. The projectors may vary with j. For a map X on A and any inaccessible record registers, set

```math
\mathsf S_j(X)=P_{0,j}\otimes I
 +P_{+,j}\otimes X
 +P_{-,j}\otimes X^\dagger.
\tag{HS.2}
```

The identity in its first summand acts on both A and the record registers. All controls are on S, so they commute with maps confined to A or the records. A known intervention can compute any desired control into S before this layer. Between layers the algorithm may act jointly on A, S, and its other accessible registers.

Every $`\mathsf S_j(U)`$ is unitary. When X is a contraction, $`\mathsf S_j(X)`$ is a contraction because it is an orthogonal direct sum of I, X, and X†. The proof below permits arbitrary coherent inputs to S.

### Norm conventions

We use the operator norm for maps, Euclidean norm for vectors, and half the trace norm for Hermitian differences. Simulator vectors are never renormalized. For vectors a,b of norm at most one,

```math
D_{\rm tr}(|a\rangle\langle a|,|b\rangle\langle b|)
\le\frac{\|a\|+\|b\|}{2}\|a-b\|
\le\|a-b\|.
\tag{HS.3}
```

The first inequality follows by writing the difference as
$`|a-b\rangle\langle a|+|b\rangle\langle a-b|`$.
Partial trace and a common final quantum channel contract the trace norm of a Hermitian difference, also for subnormalized inputs.

## 1. Records and the two recording maps

A relation is a finite multiset of pairs from [n]×[n]. Write |L| for its size with multiplicities, Dom(L) and Im(L) for the sets of first and second coordinates, and ⊎ for multiset union. The record spaces can be taken to be

```math
\mathcal H_L=\bigoplus_{\ell=0}^{n}
 \operatorname{Sym}^{\ell}(\mathbb C^n\otimes\mathbb C^n),
\qquad
\mathcal H_R=\bigoplus_{r=0}^{n}
 \operatorname{Sym}^{r}(\mathbb C^n\otimes\mathbb C^n).
```

The normalized symmetric vectors |L⟩, indexed by multisets L, form an orthonormal basis in each length sector. Define Π≤t to project onto |L|+|R|≤t. Only those sectors occur after t query layers. All maps below are zero on unspecified input sectors.

For |L|+|R|≤n−1 define left and right creation maps Aₗ and Aᵣ by

```math
\begin{aligned}
A_\ell|x,L,R\rangle
 &=\frac{1}{\sqrt{n-|\operatorname{Im}(L\uplus R)|}}
   \sum_{y\notin\operatorname{Im}(L\uplus R)}
   |y,L\uplus\{(x,y)\},R\rangle,\\
A_r|y,L,R\rangle
 &=\frac{1}{\sqrt{n-|\operatorname{Dom}(L\uplus R)|}}
   \sum_{x\notin\operatorname{Dom}(L\uplus R)}
   |x,L,R\uplus\{(x,y)\}\rangle.
\end{aligned}
\tag{HS.4}
```

These are MH's Vᴸ,Vᴿ, respectively (Definition 25, Eqs. (8.1)–(8.2)). The strong recording map used in (HS.1) is

```math
M=A_\ell(I-A_rA_r^\dagger)
 +(I-A_\ell A_\ell^\dagger)A_r^\dagger.
\tag{HS.5}
```

This is MH's V from Definition 26. MH Claim 15 proves it is a partial isometry. In particular, M and M† are contractions. Each takes record length at most t to length at most t+1. An inactive block leaves the length unchanged.

For comparison, call (L,R) **bijective** when the concatenated multiset L⊎R has no repeated first coordinate and no repeated second coordinate. In particular L and R cannot share a pair. Let Πbij be the projector onto such record pairs, and Πbij,≤t=ΠbijΠ≤t.

Restrict Aₗ to bijective records and inputs x outside Dom(L⊎R), obtaining Bₗ. Restrict Aᵣ to bijective records and inputs y outside Im(L⊎R), obtaining Bᵣ. Define

```math
J=B_\ell+B_r^\dagger,
\qquad P_D=J^\dagger J,
\qquad P_I=JJ^\dagger.
\tag{HS.6}
```

Here J is MH's W, not the physical oracle W_b. MH Claim 11 proves that J is a partial isometry. Its domain and image lie in the bijective record space. Its domain/image projectors commute with record length (MH Claim 12). Consequently

```math
B_{D,t}=\Pi_{\mathrm{bij},\le t}-P_D\Pi_{\le t},
\qquad
B_{I,t}=\Pi_{\mathrm{bij},\le t}-P_I\Pi_{\le t}
\tag{HS.7}
```

are orthogonal projectors. The restriction identities needed below are

```math
J^\dagger M=P_D,
\qquad JM^\dagger=P_I.
\tag{HS.8}
```

They are MH Corollary 8.3, Eqs. (8.27)–(8.28). The J and J† processes preserve bijectivity and increase total length by at most one; arbitrary accessible interventions preserve both record properties.

## 2. The common environment transformation and imported estimates

For C,D∈U(n), define

```math
Q[C,D]
 =(C\otimes D^{\mathsf T})_L^{\otimes *}
  \otimes(\overline C\otimes D^\dagger)_R^{\otimes *}.
\tag{HS.9}
```

Tensor-star denotes the direct sum of the corresponding tensor power on every record-length sector, restricted to the symmetric space. Thus Q is a unitary, preserves each pair of lengths, and fixes |∅,∅⟩. The complex conjugation on C in the right factor is essential. This is MH Definition 27, Eq. (8.7).

For clarity, the only quantitative source inputs are the following two operator estimates. Set

```math
e_t=16\sqrt{\frac{2t(t+1)}n},
\qquad b_t=6t\sqrt{\frac tn}.
\tag{HS.10}
```

**Local invariance.** Writing M≤t=MΠ≤t, MH Claim 16, Eqs. (8.8)–(8.9), gives, for 0≤t≤n−1,

```math
\begin{aligned}
\|(D M_{\le t}C)Q-QM_{\le t}\|_{\rm op}&\le e_t,\\
\|(C^\dagger M^\dagger\Pi_{\le t}D^\dagger)Q
          -QM^\dagger\Pi_{\le t}\|_{\rm op}&\le e_t.
\end{aligned}
\tag{HS.11}
```

C,D act on A; Q acts on LR. Products involving these distinct registers carry implicit identities. The notation in the second line is M†Π≤t, not (MΠ≤t)†.

**Averaged bad-projector bound.** For independent C,D from an exact unitary 2-design, MH Lemma 9.2, Eqs. (9.10)–(9.11), with the conservative range confirmed in Lemma 11.2, Eqs. (11.83)–(11.84), gives, for 0≤t≤n/2,

```math
\begin{aligned}
\left\|\mathbb E_{C,D}
 Q^\dagger C^\dagger B_{D,t}C Q\right\|_{\rm op}&\le b_t,\\
\left\|\mathbb E_{C,D}
 Q^\dagger D B_{I,t}D^\dagger Q\right\|_{\rm op}&\le b_t.
\end{aligned}
\tag{HS.12}
```

We will use Haar measure itself as this 2-design. The estimates (HS.11)–(HS.12) concern operators on every length sector up to t, not only states of a fixed homogeneous query degree.

### A precise purification of C,D

Let μ be the product Haar probability measure on U(n)×U(n). To avoid formal uncountable orthonormal kets, use the Hilbert space $`\mathcal E_{CD}=L^2(\mu)`$, with normalized constant vector 1. A vector in the enlarged space is a square-integrable function of (C,D). Define $`\mathsf Q`$ pointwise by

```math
(\mathsf Q f)(C,D)=Q[C,D]f(C,D).
\tag{HS.13}
```

This is the environment unitary denoted cQ in MH Definition 31, Eq. (9.9). It acts only on LRCD and commutes with every accessible intervention and every Pα,j. It is the **same** transformation for forward, inverse, and inactive branches and at every layer. Taking a partial trace over CD means integrating the rank-one operator of the vector-valued function.

## 3. Local estimates for the switched maps

For X=M or J, define a twirled switched map, acting pointwise in C,D,

```math
\mathsf S_j^{C,D}(X)
 =P_{0,j}I+P_{+,j}D X C
                 +P_{-,j}C^\dagger X^\dagger D^\dagger.
\tag{HS.14}
```

The error in intertwining $`\mathsf S_j(M)`$ and $`\mathsf S_j^{C,D}(M)`$ through Q has zero inactive block and two active blocks bounded by (HS.11). Orthogonality of their control domains and ranges gives

```math
\left\|
 \big(\mathsf S_j^{C,D}(M)Q-Q\mathsf S_j(M)\big)
 \Pi_{\le t}\right\|_{\rm op}\le e_t.
\tag{HS.15}
```

The norm of a block-diagonal operator is the maximum of its block norms, so no factor of two, number of histories, or inverse-query count is incurred. The same pointwise bound holds for the multiplication operators on L²(μ).

Define the controlled bad projector at layer j by

```math
\mathsf B_{j,t}(C,D)
 =P_{+,j}C^\dagger B_{D,t}C
  +P_{-,j}D B_{I,t}D^\dagger.
\tag{HS.16}
```

It is an orthogonal projector: its summands are projectors supported on orthogonal control sectors. Since the controls do not act on A, LR, or CD, (HS.12) also yields

```math
0\le
\mathbb E_{C,D}Q^\dagger\mathsf B_{j,t}(C,D)Q
\le b_t I.
\tag{HS.17}
```

Indeed, this expectation is an orthogonal direct sum of the two operators in (HS.12) and zero. This argument is an operator bound; it does not condition on a measurement history or assume that the twirled algorithm state is independent of C,D.

## 4. Overlap induction, including the inactive block

Purify all accessible interventions, adding unused registers if necessary, into known unitaries G₁,…,G_T. A final known unitary or channel can be handled afterward. Define simulator vectors

```math
\begin{aligned}
v_0&=|a_0\rangle|\varnothing,\varnothing\rangle,\qquad
&v_j&=\mathsf S_j(M)G_jv_{j-1},\\
w_0(C,D)&=v_0,\qquad
&w_j(C,D)&=\mathsf S_j^{C,D}(J)G_jw_{j-1}(C,D).
\end{aligned}
\tag{HS.18}
```

Here a₀ is normalized and independent of U,C,D. The vector v_j is independent of C,D. We regard it as the constant function v_j⊗1 when applying $`\mathsf Q`$. Both vectors have norm at most one. The records of v_j have total length at most j, and those of w_j are bijective with total length at most j. Inactive layers do not change either assertion.

Set

```math
h_t=\operatorname{Re}\langle w_t,\mathsf Q(v_t\otimes1)\rangle.
\tag{HS.19}
```

The initial overlap is h₀=1. For the next layer abbreviate
$`v'=G_{t+1}v_t`$, $`w'=G_{t+1}w_t`$, and omit the layer index on the switch. Using (HS.15) and ∥w′∥,∥v′∥≤1 gives

```math
h_{t+1}\ge
\operatorname{Re}\langle w',
 (\mathsf S^{C,D}(J))^\dagger
 \mathsf S^{C,D}(M)\mathsf Q(v'\otimes1)\rangle-e_t.
\tag{HS.20}
```

There are no cross terms between the three control sectors. By (HS.8), the product in (HS.20) is

```math
P_0 I+P_+C^\dagger P_D C+P_-D P_I D^\dagger.
\tag{HS.21}
```

On the left vector w′, Πbij,≤t is the identity. Substituting (HS.7) into the active terms of (HS.21) therefore replaces this product, inside the overlap, by $`I-\mathsf B_{t+1,t}`$. The identity sector contributes the full previous overlap on that sector; it carries no projection loss. Consequently

```math
h_{t+1}\ge h_t-e_t
 -\left|\langle w',\mathsf B_{t+1,t}
                  \mathsf Q(v'\otimes1)\rangle\right|.
\tag{HS.22}
```

The remaining matrix element is at most

```math
\begin{aligned}
\|\mathsf B_{t+1,t}\mathsf Q(v'\otimes1)\|
&=\left(
 \langle v'|\mathbb E_{C,D}
 Q^\dagger\mathsf B_{t+1,t}(C,D)Q|v'\rangle
 \right)^{1/2}\\
&\le\sqrt{b_t}.
\end{aligned}
\tag{HS.23}
```

We used that $`\mathsf B_{t+1,t}`$ is a projector, followed by (HS.17). The vector v′, unlike w′, is independent of C,D. This distinction is what licenses taking the expectation of the operator; no unjustified independence of an adaptively generated twirled history is used.

For t≥1,

```math
e_t+\sqrt{b_t}
\le \frac{32t}{\sqrt n}
   +\frac{\sqrt6\,t^{3/4}}{n^{1/4}}
\le\frac{35t}{n^{1/4}}.
\tag{HS.24}
```

Both terms vanish for t=0. Summing (HS.22) gives, in particular, the convenient source-compatible bound

```math
h_T\ge1-\frac{35T^2}{n^{1/4}}.
\tag{HS.25}
```

This is the switched counterpart of MH Claim 18, Eq. (9.16), derived explicitly rather than quoted for a different oracle model. Since both vectors have norm at most one,

```math
\|w_T-\mathsf Q(v_T\otimes1)\|^2
\le2-2h_T\le\frac{70T^2}{n^{1/4}}.
\tag{HS.26}
```

Tracing out LRCD, using (HS.3), and noting that $`\mathsf Q`$ acts only on the traced environment gives

```math
D_{\rm tr}(\tau_J,\tau_M)
\le\sqrt{70}\,Tn^{-1/8}\le9Tn^{-1/8},
\tag{HS.27}
```

where τ_J is the reduced state of w_T. The same overlap also implies

```math
\|w_T\|^2\ge1-70T^2n^{-1/4}.
\tag{HS.28}
```

To check (HS.28) when the bound is useful, put $`a=35T^2n^{-1/4}\le1/2`$. Then $`\|w_T\|\ge h_T\ge1-a`$, hence $`\|w_T\|^2\ge1-2a`$. When $`a>1/2`$ the claimed right-hand side is nonpositive and the inequality is automatic. No squaring of a negative lower bound on h_T is needed.

## 5. Purified permutation oracle and exact compression

Let P and F be inaccessible registers whose bases label a permutation π∈S_n and a ternary function f:[n]→{0,1,2}. With ω=e^(2πi/3), define

```math
\mathsf O_{\rm pf}|x,\pi,f\rangle
 =\omega^{f(x)}|\pi(x),\pi,f\rangle.
\tag{HS.29}
```

Initially π and f are in independent uniform superpositions. The normalization is $`(n!\,3^n)^{-1/2}`$. This agrees with MH Definitions 18–19 and Eq. (6.5); the binary prefactor for the function register appearing in the prose statement of MH Claim 6 is a typographical inconsistency and is not used here.

For a bijective pair (L,R), m=|L|+|R|, define the normalized vector

```math
|p_{L,R}\rangle
 =\frac1{\sqrt{(n-m)!\,3^n}}
 \sum_{\pi:\,\pi\supseteq L\uplus R}\ \sum_f
 \omega^{\sum_{(x,y)\in L}f(x)-\sum_{(x,y)\in R}f(x)}
 |\pi,f\rangle.
\tag{HS.30}
```

These vectors are orthonormal over **all** bijective pairs, allowing different m, |L|, and |R|. One can see the absence of a fixed-degree restriction directly: the ternary Fourier label of f has value 1 on Dom(L), 2 on Dom(R), and 0 elsewhere. It identifies those two disjoint domains, including their sizes. If these domains agree but the assigned images differ, the allowed permutation supports are disjoint. This is the content of MH Claim 7, Eqs. (6.6)–(6.11).

Define the partial isometry

```math
\mathsf C=\sum_{(L,R)\,\mathrm{bijective}}
 |L,R\rangle\langle p_{L,R}|,
\qquad
\Pi_{\rm pf}=\mathsf C^\dagger\mathsf C,
\qquad \mathsf C\mathsf C^\dagger=\Pi_{\rm bij}.
\tag{HS.31}
```

This is MH's Comp. It acts only on the inaccessible environment. In particular it commutes with all controls and accessible interventions. Its initial vector is $`|p_{\varnothing,\varnothing}\rangle`$, which it takes to the empty records.

The source compression identities, MH Claim 13, Eqs. (7.9)–(7.10), are

```math
J=\mathsf C\mathsf O_{\rm pf}\mathsf C^\dagger P_D,
\qquad
J^\dagger=\mathsf C\mathsf O_{\rm pf}^\dagger\mathsf C^\dagger P_I.
\tag{HS.32}
```

Set $`\widetilde P_D=\mathsf C^\dagger P_D\mathsf C`$ and
$`\widetilde P_I=\mathsf C^\dagger P_I\mathsf C`$.
Both are orthogonal projectors supported in Πpf (MH Definition 35).

### Why compression preserves every projected state

It is insufficient to treat $`\mathsf C`$ as an isometry on its entire source space. We need the following support observation. If z∈Ran(P_D), then ∥Jz∥=∥z∥. Equation (HS.32), the unitarity of $`\mathsf O_{\rm pf}`$, and the isometry of $`\mathsf C^\dagger`$ on the bijective space imply

```math
\|\mathsf C\mathsf O_{\rm pf}\mathsf C^\dagger z\|
=\|\mathsf O_{\rm pf}\mathsf C^\dagger z\|.
```

Equality for this partial isometry implies
$`\mathsf O_{\rm pf}\mathsf C^\dagger z\in\operatorname{Ran}(\Pi_{\rm pf})`$.
Thus

```math
\mathsf O_{\rm pf}\mathsf C^\dagger P_D
 =\mathsf C^\dagger J,
\qquad
\mathsf O_{\rm pf}^\dagger\mathsf C^\dagger P_I
 =\mathsf C^\dagger J^\dagger
\tag{HS.33}
```

on the bijective record space. The inverse identity follows by the same argument. It explicitly rules out a hidden component outside the compression domain.

### The switched projected process

The unprojected switched purified oracle is the unitary

```math
\mathsf U_j^{C,D}
 =P_{0,j}I+P_{+,j}D\mathsf O_{\rm pf}C
 +P_{-,j}C^\dagger\mathsf O_{\rm pf}^\dagger D^\dagger.
\tag{HS.34}
```

Insert on its input side the orthogonal projector

```math
\mathsf P_j^{C,D}
 =P_{0,j}I+P_{+,j}C^\dagger\widetilde P_D C
               +P_{-,j}D\widetilde P_I D^\dagger.
\tag{HS.35}
```

Their product is

```math
\mathsf U_j^{C,D}\mathsf P_j^{C,D}
 =P_{0,j}I+P_{+,j}D\mathsf O_{\rm pf}\widetilde P_D C
 +P_{-,j}C^\dagger\mathsf O_{\rm pf}^\dagger
                         \widetilde P_I D^\dagger.
\tag{HS.36}
```

Initialize the records of this process in $`|p_{\varnothing,\varnothing}\rangle`$, the CD component in 1, and the accessible state in a₀. Let q_j be the unprojected process and p_j the process using (HS.36), with the same G_j as before. Inductively, p_j belongs to Ran(Πpf): an inactive layer preserves it, an active layer preserves it by (HS.33), and C,D,G_j do not act on PF. Moreover,

```math
w_j=\mathsf C p_j,
\qquad p_j=\mathsf C^\dagger w_j,
\qquad \|p_j\|=\|w_j\|.
\tag{HS.37}
```

These equalities follow sector by sector from (HS.33) and hold on coherent superpositions of different directions and record lengths. They give the exact switched extension of MH Claim 19, Eq. (9.65). Since compression acts only on an inaccessible system and is an isometry on the entire support of p_j, the accessible reduced states of p_j and w_j are equal.

## 6. Removing the projections and identifying Haar measure

Write $`\mathsf Z_j=\mathsf U_j^{C,D}G_j`$, a unitary on the enlarged space, and
$`\widehat{\mathsf P}_j=\mathsf U_j^{C,D}\mathsf P_j^{C,D}(\mathsf U_j^{C,D})^\dagger`$, an orthogonal projector. Then the unprojected layer is $`\mathsf Z_j`$ and the projected layer is $`\widehat{\mathsf P}_j\mathsf Z_j`$. There is one such projection per layer, including a harmless identity block on skipped branches.

The sequential gentle-measurement inequality (MH Lemma 2.3, Eq. (2.47)) now applies to the single enlarged normalized initial vector, giving

```math
\|q_T-p_T\|
\le T\sqrt{1-\|p_T\|^2}
 =T\sqrt{1-\|w_T\|^2}
\le \sqrt{70}\,T^2n^{-1/8}
\le9T^2n^{-1/8}.
\tag{HS.38}
```

The estimate can also be proved directly by a telescoping hybrid: the loss caused by any one projection is at most $`\sqrt{1-\|p_T\|^2}`$, because the squared norm of every intermediate projected state is at least its final squared norm. This argument is valid on the L² purification and does not normalize any intermediate branch.

After tracing the hidden environment, (HS.3), (HS.37), and (HS.38) show that the unprojected purified process is within $`9T^2n^{-1/8}`$ of τ_J. Combining with (HS.27) gives

```math
D_{\rm tr}(\tau_{\rm pf},\tau_M)
\le9T(T+1)n^{-1/8}.
\tag{HS.39}
```

Tracing out PFCD in the unprojected process is exactly equivalent to sampling π,f,C,D at the beginning and reusing the matrix

```math
U=D P_\pi F_f C,
\qquad
P_\pi|x\rangle=|\pi(x)\rangle,
\quad F_f|x\rangle=\omega^{f(x)}|x\rangle
\tag{HS.40}
```

at every active forward layer, and its adjoint at every active inverse layer. The sampled description registers are not changed by any query. Because C,D are independently Haar, this matrix is Haar-distributed. This is equality of distributions of matrices, including their global phases, and therefore remains valid for controlled use and repeated access. It is not merely an equality of single-use conjugation channels. Equation (HS.39) is thus (HS.1) for switched layers.

## 7. Recovering the physical adaptive model and the block 1⊕U

For a finite measurement-adaptive algorithm, purify an instrument with Kraus operators K_h by recording its outcome twice,

```math
|\psi\rangle\longmapsto
\sum_h K_h|\psi\rangle\otimes|h\rangle_H\otimes|h\rangle_E.
\tag{HS.41}
```

The history H is available for subsequent classical control. The copy E is retained and never erased, so distinct classical histories remain orthogonal when E is traced out. Known operations between successive physical query events can be collected into G_j; the next direction is computed from H into the separate control register S. An early-terminated branch takes the identity sector in all remaining layers. The number of layers can be padded to the same deterministic T on all histories.

This construction reproduces the original algorithm after tracing out the immutable copies. The preceding proof is uniform over its known interventions. It neither conditions on a realized history nor assumes that histories are independent of the reused oracle. A hard cap F on forward and K on inverse calls implies T=F+K suffices. The padding is only a mathematical identity operation; it does not grant an additional physical inverse call. The simulation lemma itself uses T alone. The separate F/K accounting belongs to the subsequent lower bound.

The logical (n+1)-dimensional oracle 1⊕U fits (HS.2). Fix any |a*⟩∈Cⁿ and embed

```math
|0\rangle\mapsto|0\rangle_S|a_*\rangle_A,
\qquad
|j\rangle\mapsto|1\rangle_S|j\rangle_A
\quad(j\in[n]).
\tag{HS.42}
```

The inactive block acts as identity on the first encoded vector and the active block acts as U on its orthogonal complement. Any known logical intervention has a known extension to this larger space. M and M† preserve the encoded logical space together with LR, so the replacement is exactly $`I_{\{0\}}\oplus M`$ or its adjoint.

For the two physical hypotheses, put $`\theta=\arcsin\epsilon`$ and write

```math
W_b=R_{b\theta}(1\oplus U),
\tag{HS.43}
```

the known rotation is after the Haar-block call in a forward query and before the Haar-block call in an inverse query. For each fixed b it is a fixed, U-independent intervention, so the lemma applies separately. This decomposition is a proof representation of the two hypotheses; it does not give the actual algorithm the value of b. If their averaged outputs are $`\bar\rho_b`$ and their recording outputs are τ_b, then

```math
D_{\rm tr}(\bar\rho_b,\tau_b)\le\eta_n(T),
\quad b=0,1,
\qquad
D_{\rm tr}(\bar\rho_0,\bar\rho_1)
\le D_{\rm tr}(\tau_0,\tau_1)+2\eta_n(T).
\tag{HS.44}
```

Thus the finite-dimensional term supplied to the mixed-query lower bound is exactly $`18T(T+1)n^{-1/8}`$. A later projection such as M↦ΓMΓ has its own leakage error and is not included in (HS.44). This completes the proof of Lemma HS.1 for the stated physical model.

## 8. Source dependence and dimension range

The source-to-extension dependencies are:

| Input from MH v3 | Use in this proof |
|---|---|
| Definitions 22, 25, 26; Claims 11, 15 | Explicit J,M and contraction properties |
| Claim 12; Corollaries 7.1 and 8.3, Eqs. (8.27)–(8.28) | Record cutoff, bad projectors, overlap product |
| Definition 27, Eq. (8.7); Definition 31, Eq. (9.9) | One common environment transformation |
| Claim 16, Eqs. (8.8)–(8.9) | Both local intertwining estimates |
| Lemma 9.2, Eqs. (9.10)–(9.11), with Lemma 11.2's range | Both averaged bad-projector estimates |
| Claim 7; Claim 13, Eqs. (7.9)–(7.10) | Compression over all record lengths |
| Lemma 2.3, Eq. (2.47) | Removing T controlled projections |
| Theorem 8, Eq. (9.5) | The ordinary fixed-direction result being extended |

Equations (HS.15)–(HS.28) supply the control extension of the overlap argument; (HS.33)–(HS.38) supply the controlled compression and gentle-measurement argument. These are the additional derivations needed beyond citing the printed theorem.

For a desired per-hypothesis error ζ>0, it suffices to choose a power-of-two n satisfying

```math
n\ge\max\left\{2T,\left(\frac{9T(T+1)}\zeta\right)^8\right\}.
\tag{HS.45}
```

At fixed ζ this sufficient dimension is $`O(T^{16})`$, while $`\log n=O(\log T)`$. The estimate is loose; it makes no assertion about a small fixed dimension or efficient implementation of an individual Haar-random physical oracle. The sharper forward-only $`O(T^2/n)`$ simulation bound from Part I of MH is not used for these mixed directions.
