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

def my_function():
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
