import ast
from flake8_ic import IcecreamChecker


def check_icecream_usage(code: str, expected_error: str, expected_count: int = 1):
    """
    Utility function to parse code, run the checker, and assert errors.

    Args:
        code (str): The source code to check.
        expected_error (str): The expected error message.
        expected_count (int): The expected number of errors. Default is 1.
    """
    tree = ast.parse(code)
    checker = IcecreamChecker(tree)
    errors = list(checker.run())

    assert_message = f"Expected {expected_count} errors, found {len(errors)}"
    assert len(errors) == expected_count, assert_message

    if expected_count > 0:
        assert_message = f"Expected error '{expected_error}', found '{errors[0][2]}'"
        assert errors[0][2] == expected_error, assert_message


def test_ic_usage():
    code = """
from icecream import ic

ic("Debug message")
    """
    expected_error = (
        "IC100 Avoid using `ic()` from the `icecream` package in production code."
    )
    check_icecream_usage(code, expected_error)


def test_ic_disabled_usage():
    code = """
from icecream import ic

ic.disabled()
    """
    expected_error = (
        "IC101 Avoid using `ic.disabled()` from the `icecream` "
        "package in production code."
    )
    check_icecream_usage(code, expected_error)


def test_ic_enabled_usage():
    code = """
from icecream import ic

ic.enabled()
    """
    expected_error = (
        "IC102 Avoid using `ic.enabled()` from the `icecream` "
        "package in production code."
    )
    check_icecream_usage(code, expected_error)


def run_checker_with_options(code, disabled_checks=None):
    """
    Helper function to simulate running the checker with specific options.

    Args:
        code (str): The code to analyze.
        disabled_checks (list, optional): List of check codes to disable.

    Returns:
        list: List of errors found by the checker.
    """
    tree = ast.parse(code)
    checker = IcecreamChecker(tree)
    if disabled_checks:
        checker.disabled_checks = disabled_checks
    return list(checker.run())


def test_disable_ic100_check():
    code = """
from icecream import ic

ic("Debug message")
    """
    # Simulate disabling IC100
    errors = run_checker_with_options(code, disabled_checks=["IC100"])
    assert len(errors) == 0  # No errors should be reported


def test_disable_ic101_check():
    code = """
from icecream import ic

ic.disabled()
    """
    # Simulate disabling IC101
    errors = run_checker_with_options(code, disabled_checks=["IC101"])
    assert len(errors) == 0  # No errors should be reported


def test_disable_ic102_check():
    code = """
from icecream import ic

ic.enabled()
    """
    # Simulate disabling IC102
    errors = run_checker_with_options(code, disabled_checks=["IC102"])
    assert len(errors) == 0  # No errors should be reported


def test_disable_multiple_checks():
    code = """
from icecream import ic

ic("Debug message")
ic.disabled()
    """
    # Simulate disabling both IC100 and IC101
    errors = run_checker_with_options(code, disabled_checks=["IC100", "IC101"])
    assert len(errors) == 0  # No errors should be reported


def test_no_checks_disabled():
    code = """
from icecream import ic

def my_function():
    ic("Debug message")
    ic.disabled()
    """
    # Run with no checks disabled
    errors = run_checker_with_options(code)
    assert len(errors) == 2  # Both IC100 and IC101 should be reported
    assert errors[0][2].startswith("IC100")
    assert errors[1][2].startswith("IC101")
