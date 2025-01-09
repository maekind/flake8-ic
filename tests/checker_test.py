import ast
from flake8_ic import IcecreamChecker


def test_ic_usage():
    code = """
from icecream import ic

def my_function():
    ic("Debug message")
    """
    tree = ast.parse(code)
    checker = IcecreamChecker(tree)
    errors = list(checker.run())
    assert len(errors) == 1
    assert errors[0][2] == (
        "IC100 Avoid using `ic()` from the `icecream` package in production code."
    )
