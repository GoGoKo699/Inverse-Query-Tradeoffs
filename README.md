# Inverse Query Tradeoffs

**How much can a limited ability to reverse an unknown quantum operation reduce the number of forward uses needed to distinguish two known states?**

An unknown unitary prepares either the reference state or a known nearby state. Its remaining columns are arbitrary. The task is to output one classical decision bit, and the resources are the total numbers of forward and inverse oracle calls.

In the sufficiently large dimension regime specified in the [model and exact results](science/model.md), the constant-success resource boundary is, up to universal constant factors,

```math
F(K+1)+K^2\asymp\epsilon^{-2}.
```

Here $`F`$ counts forward calls, $`K`$ counts inverse calls, and $`\epsilon`$ is the amplitude separating the two candidate states. This describes the boundary of attainable budgets; an algorithm may always spend fewer than its allowed calls. The lower bound permits arbitrary known processing and classical adaptation of query direction, with a hard cap on each direction along every measurement history.

The construction turns inverse queries into copies of an unknown calibration state, arranges those copies coherently in a Dicke probe, and detects a change in its occupation count. Its finite success guarantee holds uniformly over all unitary completions, in every dimension. The lower bound tracks how inverse queries supply the completion information that subsequent forward queries can use.

| Resource regime | Consequence | Scope |
|---|---|---|
| A fixed number of inverse calls | $`F=\Theta(\epsilon^{-2})`$ | Matching in sufficiently large dimension |
| $`K=o(\epsilon^{-1})`$ | $`F=\Theta(1/[\epsilon^2(K+1)])`$ | Matching in sufficiently large dimension |
| Inverse access alone | $`F=0,\ K=\Theta(\epsilon^{-1})`$ | Established measurement-discrimination construction; matching lower bound here |
| Inverse price $`r\ge1`$ | Optimal oracle cost $`\Theta(\min\{\sqrt r/\epsilon,\epsilon^{-2}\})`$ | Same large-dimension model |
| Forward access alone in dimension $`d`$ | $`O(\min\{\epsilon^{-2},d/\epsilon\})`$ calls | Upper bound for every $`d\ge2`$ |

The last result synthesizes only the calibration inverses with the [QURA inversion circuit](references/RELATED_WORK.md#qura). It improves the dimension-dependent upper bound listed for this particular known-state decision problem by [Wang, Carolan and Childs](references/RELATED_WORK.md#wcc2026). It is not a result for general amplitude estimation, and the optimal finite-dimensional lower bound is not established here.

## Read the science

Start with the [question, oracle contract and exact statements](science/model.md). Then read the [calibration construction](science/dicke_calibration.md) and the [mixed-query lower bound](science/mixed_query_lower_bound.md). The [resource interpretation](science/resource_tradeoffs.md) explains their joint meaning and the weighted-cost consequence.

| Question | Authoritative account |
|---|---|
| What is the promise, and which calls are counted? | [Model and exact results](science/model.md) |
| Why do calibrated copies give a finite decision advantage? | [Dicke calibration](science/dicke_calibration.md) |
| How are the probe, memory and measurements implemented? | [Implementations and physical resources](science/implementations.md) |
| Why can an adaptive algorithm not use a small inverse budget more effectively? | [Mixed-query lower bound](science/mixed_query_lower_bound.md) |
| Which Haar-simulation theorem is used, and what extension is proved? | [Haar simulation with query controls](science/haar_simulation.md) |
| How should one allocate expensive inverse calls? | [Resource tradeoffs](science/resource_tradeoffs.md) |
| What can be achieved using only native forward access? | [Dimension-dependent forward algorithm](science/forward_only.md) |
| Which ingredients are established, and what conclusion is added? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Which calculations can be reproduced? | [Verification](verification/README.md) |

## Reproduce the finite checks

From the repository root, with the packages in [verification/requirements.txt](verification/requirements.txt) installed, run:

```bash
python3 verification/run_all.py
```

The checks evaluate complex-unitary calibration identities, the Dicke occupation probability, collective-generator moments and integer query budgets. They support the finite upper-bound algebra. The adaptive lower bound and its Haar-simulation extension are analytical arguments, not conclusions of numerical sampling.

## Scope and physical costs

Both candidate states and their separation are known. No QRAM or classical description of the unknown completion is supplied. The output is one bit. Every oracle port is counted, including ports used in parallel. The two explicit implementations trade quantum memory against known-gate work; their best features cannot be combined into a single unproved resource estimate. Exact oracle calls are assumed, with a separately stated allowance for compiling known gates.

The matching lower theorem uses $`d-1`$ a power of two and an explicit, deliberately loose lower bound on dimension relative to $`F+K`$. Coherent skipping may be allowed when the physical call is charged. Separate discounted budgets for counterfactual branches of a coherent forward/inverse switch are outside the theorem's model.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
