"""Run and compare the finite constructive checks; not an analytical-proof checker."""

from pathlib import Path
import json
import math
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


def compare(actual, expected, path="report"):
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or actual.keys() != expected.keys():
            raise AssertionError(f"{path}: different report fields")
        for key, value in expected.items():
            compare(actual[key], value, f"{path}.{key}")
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise AssertionError(f"{path}: different list length")
        for index, value in enumerate(expected):
            compare(actual[index], value, f"{path}[{index}]")
    elif isinstance(expected, float):
        if not math.isfinite(actual) or not math.isclose(
            actual, expected, rel_tol=1e-8, abs_tol=2e-10
        ):
            raise AssertionError(f"{path}: {actual!r} differs from {expected!r}")
    elif actual != expected:
        raise AssertionError(f"{path}: {actual!r} differs from {expected!r}")


def main():
    completed = subprocess.run(
        [sys.executable, str(ROOT / "check_dicke_calibration.py")],
        capture_output=True,
        text=True,
    )
    if completed.returncode:
        sys.stderr.write(completed.stdout + completed.stderr)
        raise SystemExit(completed.returncode)
    actual = json.loads((ROOT / "actual/dicke_check_results.json").read_text())
    expected = json.loads((ROOT / "expected/dicke_check_results.json").read_text())
    compare(actual, expected)
    print(json.dumps({
        "status": "PASS",
        "expected_report_matches": True,
        "full_tensor_instances": actual["full_tensor_instances"],
        "moment_instances": actual["moment_instances"],
        "budget_schedule_instances": actual["budget_schedule_instances"],
        "largest_reported_error": max(actual["max_errors"].values()),
        "scope": "Finite constructive identities and budgets; no numerical lower-bound proof.",
    }, indent=2))


if __name__ == "__main__":
    main()
