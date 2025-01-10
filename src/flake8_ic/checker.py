import ast
from typing import Generator, Tuple


class IcecreamChecker:
    """
    Flake8 plugin to check for usage of the `ic()` method from the `icecream` package.
    """

    IC_ERROR_CODE = "IC100"

    def __init__(self, tree: ast.Module):
        self.tree = tree

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        """
        Generator that yields issues found in the AST.
        """
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id == "ic":
                    yield (
                        node.lineno,
                        node.col_offset,
                        (
                            f"{self.IC_ERROR_CODE} Avoid using `ic()` from the "
                            "`icecream` package in production code."
                        ),
                        type(self),
                    )
