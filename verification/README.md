# Reproduce the finite constructive checks

The written [Dicke proof](../science/dicke_calibration.md) establishes the uniform finite success guarantee. This directory supplies independent matrix and polynomial evaluations of its identities on specified finite cases. The [mixed-query lower bound](../science/mixed_query_lower_bound.md), [Haar-simulation extension](../science/haar_simulation.md), and asymptotic resource laws are analytical results; they are not numerically certified by this suite.

## Run

The recorded environment is Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. From the repository root, install the pinned numerical dependencies in your chosen Python environment and run:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The runner executes [check_dicke_calibration.py](check_dicke_calibration.py), checks the program's assertions, and compares the complete report against [the committed expected output](expected/dicke_check_results.json). It writes the newly generated report to `verification/actual/`, which is ignored by Git. It does not overwrite the expected report.

The random generator is deterministically seeded with `4062026`. Expected integers and report structure are compared exactly; floating-point values use relative tolerance `1e-8` and absolute tolerance `2e-10` to allow platform-dependent linear-algebra rounding. The scientific program itself independently asserts that every reported identity error is below `1e-10` and that the finite moment and success inequalities hold.

## What is checked

| Check | Cases | Meaning |
|---|---:|---|
| Full complex-unitary tensor construction | 378 | Calibration sign, cancellation of the arbitrary completion, occupation probabilities, and the survival-amplitude formula |
| Collective-generator moments | 5,150 | Direct symmetric-spin matrix evaluation of the second and fourth moments, including the fourth-moment bound |
| Rounded budget schedule | 571 | Admissible integer budgets, enough probe slots, and the interval used by the finite-angle proof |

The full tensor checks use dimensions 3, 4 and 5, with up to 7, 5 and 4 probe registers respectively, all allowed occupations at those sizes, and separation values 0, 0.07 and 0.25. Zero separation is an algebraic boundary check, outside the positive-separation decision theorem. The complement of the fixed reference vector is sampled using complex Gaussian QR, giving unitary completions with complex phases as well as real components.

The moment checks use every occupation for probe sizes 1 through 100. The schedule checks use 101 geometrically spaced separations from `1e-5` to `0.25`, with selected occupations including zero and the maximum admissible inverse budget. A further table of finite examples evaluates success, rather than inferring it solely from the variance.

For evaluation, the exact survival amplitude has the Jacobi-polynomial representation

```math
a_{F,K}(\epsilon)
=c^{F-2m}P_m^{(0,F-2m)}(1-2\epsilon^2),
\qquad m=\min\{K,F-K\}.
```

The tensor calculations independently evaluate the rotated state and compare its unchanged-occupation probability with $`a_{F,K}^2`$. The proof's fourth-moment expression is compared with the norm of two applications of the collective generator in the symmetric Dicke basis. This avoids testing only a formula against itself.

## Recorded result and limits

The committed report records `PASS`, with maximum identity errors below `4e-15` and moment relative errors below `5e-16`. Its finite budget cases have $`1.500000000018\le\gamma\le1.66190`$. The smallest sampled conditional detection probability is greater than `0.7768`; the proved uniform lower guarantee is $`735/1024\approx0.71777`$. A sampled minimum is not asserted to be the true worst case.

The suite does not exhaust unitary completions, implement the universal inversion circuit, simulate every adaptive strategy, test hardware noise, or turn a finite calculation into an asymptotic converse. Its role is to make the central constructive algebra reproducible. Exact resource quantifiers and the dimension restrictions remain in the [model](../science/model.md) and their respective proofs.
