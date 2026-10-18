"""Finite checks for the limited-inverse Dicke calibration construction.

These checks supplement the analytic proof; they are not a general lower bound.
Run: python3 verification/check_dicke_calibration.py
Requires numpy and scipy. All randomness is deterministically seeded.
"""

from itertools import combinations
from math import asin, ceil, comb, floor, sqrt
from pathlib import Path
import json

import numpy as np
from scipy.special import eval_jacobi


def haar_fixing_zero(d, rng):
    z = rng.normal(size=(d - 1, d - 1)) + 1j * rng.normal(size=(d - 1, d - 1))
    q, r = np.linalg.qr(z)
    phases = np.diag(r) / np.abs(np.diag(r))
    v = np.eye(d, dtype=complex)
    v[1:, 1:] = q @ np.diag(phases)
    return v


def rotation(epsilon, d):
    c = sqrt(1 - epsilon**2)
    r = np.eye(d, dtype=complex)
    r[:2, :2] = [[c, -epsilon], [epsilon, c]]
    return r


def tensor_power_action(u, state, registers):
    d = u.shape[0]
    tensor = state.reshape((d,) * registers)
    for axis in range(registers):
        tensor = np.tensordot(u, tensor, axes=(1, axis))
        tensor = np.moveaxis(tensor, 0, axis)
    return tensor.reshape(-1)


def dicke_in_unknown_basis(registers, tokens, x):
    zero = np.eye(len(x), dtype=complex)[:, 0]
    result = np.zeros(len(x) ** registers, dtype=complex)
    for subset in combinations(range(registers), tokens):
        selected = set(subset)
        term = np.array([1.0 + 0j])
        for i in range(registers):
            term = np.kron(term, x if i in selected else zero)
        result += term
    return result / sqrt(comb(registers, tokens))


def same_weight_probability(state, registers, tokens, d):
    coordinates = np.indices((d,) * registers).reshape(registers, -1)
    mask = np.count_nonzero(coordinates, axis=0) == tokens
    return float(np.vdot(state[mask], state[mask]).real)


def generator_action(state):
    """G=sum_j Y_j, restricted to the symmetric Dicke basis."""
    n = len(state) - 1
    out = np.zeros_like(state, dtype=complex)
    for m in range(n):
        coupling = sqrt((m + 1) * (n - m))
        out[m + 1] += 1j * coupling * state[m]
        out[m] -= 1j * coupling * state[m + 1]
    return out


def variance(n, k):
    return n + 2 * k * (n - k)


def fourth_moment(n, k):
    v = variance(n, k)
    return (
        v * v
        + (k + 1) * (k + 2) * (n - k) * (n - k - 1)
        + k * (k - 1) * (n - k + 1) * (n - k + 2)
    )


def survival_amplitude(n, k, epsilon):
    """Exact Jacobi-polynomial expression, evaluated in floating point."""
    m = min(k, n - k)
    prefactor = np.exp(0.5 * (n - 2 * m) * np.log1p(-epsilon**2))
    return float(prefactor * eval_jacobi(m, 0, n - 2 * m, 1 - 2 * epsilon**2))


def forward_budget(epsilon, k):
    alpha = asin(epsilon)
    assert 0 <= k <= floor(1 / (2 * alpha))
    return ceil((3 / (2 * alpha**2) + 2 * k**2) / (2 * k + 1))


def main():
    rng = np.random.default_rng(4062026)
    errors = {
        "calibration_vector": 0.0,
        "forward_tensor_identity": 0.0,
        "inverse_weight_identity": 0.0,
        "survival_formula": 0.0,
        "second_moment_relative": 0.0,
        "fourth_moment_relative": 0.0,
    }
    full_instances = 0
    for d, max_n in [(3, 7), (4, 5), (5, 4)]:
        basis = np.eye(d, dtype=complex)
        for _ in range(2):
            v = haar_fixing_zero(d, rng)
            x = v.conj().T @ basis[:, 1]
            for epsilon in [0.0, 0.07, 0.25]:
                r = rotation(epsilon, d)
                w = r @ v
                target = epsilon * basis[:, 0] + sqrt(1 - epsilon**2) * x
                errors["calibration_vector"] = max(
                    errors["calibration_vector"],
                    float(np.linalg.norm(w.conj().T @ basis[:, 1] - target)),
                )
                for n in range(2, max_n + 1):
                    for k in range(n + 1):
                        hidden = dicke_in_unknown_basis(n, k, x)
                        known = dicke_in_unknown_basis(n, k, basis[:, 1])
                        out = tensor_power_action(w, hidden, n)
                        expected = tensor_power_action(r, known, n)
                        errors["forward_tensor_identity"] = max(
                            errors["forward_tensor_identity"],
                            float(np.linalg.norm(out - expected)),
                        )
                        inv_out = tensor_power_action(w.conj().T, known, n)
                        inv_reference = tensor_power_action(r.conj().T, known, n)
                        errors["inverse_weight_identity"] = max(
                            errors["inverse_weight_identity"],
                            abs(same_weight_probability(inv_out, n, k, d)
                                - same_weight_probability(inv_reference, n, k, d)),
                        )
                        observed = same_weight_probability(out, n, k, d)
                        formula = survival_amplitude(n, k, epsilon) ** 2
                        errors["survival_formula"] = max(
                            errors["survival_formula"], abs(observed - formula)
                        )
                        full_instances += 1

    moment_instances = 0
    for n in range(1, 101):
        for k in range(n + 1):
            ket = np.eye(n + 1, dtype=complex)[:, k]
            gket = generator_action(ket)
            ggket = generator_action(gket)
            v, m4 = variance(n, k), fourth_moment(n, k)
            assert m4 <= 3 * v * v
            errors["second_moment_relative"] = max(
                errors["second_moment_relative"], abs(np.vdot(gket, gket).real - v) / v
            )
            errors["fourth_moment_relative"] = max(
                errors["fourth_moment_relative"], abs(np.vdot(ggket, ggket).real - m4) / m4
            )
            moment_instances += 1

    schedule_instances = 0
    min_gamma, max_gamma = float("inf"), 0.0
    for epsilon in np.geomspace(1e-5, 0.25, 101):
        alpha = asin(float(epsilon))
        cap = floor(1 / (2 * alpha))
        ks = {0, cap, cap // 2, cap // 4, min(1, cap), min(2, cap)}
        for k in sorted(ks):
            n = forward_budget(float(epsilon), k)
            gamma = alpha**2 * variance(n, k)
            assert n >= k
            assert 1.5 - 1e-12 <= gamma <= 2 + 1e-12
            min_gamma, max_gamma = min(min_gamma, gamma), max(max_gamma, gamma)
            schedule_instances += 1

    examples = []
    for epsilon in [0.25, 0.2, 0.1, 0.03, 0.01, 0.003, 0.001]:
        alpha = asin(epsilon)
        cap = floor(1 / (2 * alpha))
        for k in sorted({0, min(1, cap), min(2, cap), cap // 2, cap}):
            n = forward_budget(epsilon, k)
            amplitude = survival_amplitude(n, k, epsilon)
            conditional = 1 - amplitude**2
            total = 1 - (1 - epsilon**2) ** k * amplitude**2
            assert conditional >= 735 / 1024 - 1e-7
            examples.append({
                "epsilon": epsilon, "inverse_K": k, "forward_F": n,
                "gamma": alpha**2 * variance(n, k),
                "conditional_detection": conditional,
                "total_detection": total,
            })

    report = {
        "status": "PASS",
        "interpretation": "Finite consistency checks only; analytic proofs establish the general upper bound. No unrestricted mixed-query lower bound was tested or proved.",
        "seed": 4062026,
        "full_tensor_instances": full_instances,
        "moment_instances": moment_instances,
        "budget_schedule_instances": schedule_instances,
        "max_errors": errors,
        "gamma_range": [min_gamma, max_gamma],
        "proved_conditional_detection_lower_bound": 735 / 1024,
        "minimum_sampled_conditional_detection": min(x["conditional_detection"] for x in examples),
        "examples": examples,
    }
    for error in errors.values():
        assert error < 1e-10
    output = Path(__file__).parent / "actual" / "dicke_check_results.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "examples"}, indent=2))


if __name__ == "__main__":
    main()
