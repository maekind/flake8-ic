import ast
from typing import Generator, Tuple


class IcecreamChecker:
    """
    Flake8 plugin to check for usage of the `ic()` method from the `icecream` package.
    """

    IC_ERROR_CODE = "IC100"
    IC_DISABLED_ERROR_CODE = "IC101"
    IC_ENABLED_ERROR_CODE = "IC102"

    def __init__(self, tree: ast.Module):
        self.tree = tree

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        """
        Generator that yields issues found in the AST.
        """
        for node in ast.walk(self.tree):
            if error := self._check_call(node):
                yield (
                    node.lineno,
                    node.col_offset,
                    error,
                    type(self),
                )

    def _check_call(self, node: ast.AST) -> str:
        """
        Check if a node is a problematic call and return an error message if applicable.
        """
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "ic":
                return (
                    f"{self.IC_ERROR_CODE} Avoid using `ic()` from the "
                    "`icecream` package in production code."
                )

            if isinstance(node.func, ast.Attribute):
                return self._check_attribute(node.func)

        return None

    def _check_attribute(self, func: ast.Attribute) -> str:
        """
        Check if an attribute call is problematic and return an error message
        if applicable.
        """
        attribute_errors = {
            "enabled": self.IC_ENABLED_ERROR_CODE,
            "disabled": self.IC_DISABLED_ERROR_CODE,
        }

        if func.attr in attribute_errors:
            return (
                f"{attribute_errors[func.attr]} Avoid using `ic.{func.attr}()` "
                "from the `icecream` package in production code."
            )

        return None
