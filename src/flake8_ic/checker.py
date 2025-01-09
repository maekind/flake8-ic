import ast
from typing import Generator, Tuple

from flake8_ic.metadata import get_project_metadata


class IcecreamChecker:
    """
    Flake8 plugin to check for usage of the `ic()` method from the `icecream` package.
    """

    IC_ERROR_CODE = "IC100"

    def __init__(self, tree: ast.Module):
        self.tree = tree
        self._load_metadata()

    def _load_metadata(self) -> dict:
        """
        Load the project metadata from the `pyproject.toml` file.
        """
        metadata = get_project_metadata()
        self.name = metadata["name"]
        self.version = metadata["version"]

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
