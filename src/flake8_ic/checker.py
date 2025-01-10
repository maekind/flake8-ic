import ast
from typing import Generator, Tuple


class IcecreamChecker:
    """
    Flake8 plugin to check for usage of the `ic()` method from the `icecream` package.
    """

    # Error codes
    IC_ERROR_CODE = "IC100"
    IC_DISABLED_ERROR_CODE = "IC101"
    IC_ENABLED_ERROR_CODE = "IC102"

    # Store disabled codes
    disabled_checks = []

    def __init__(self, tree):
        self.tree = tree

    @staticmethod
    def add_options(option_manager):
        """Add options for the plugin."""
        option_manager.add_option(
            "--disable-ic-checks",
            type=str,
            parse_from_config=True,
            help="Comma-separated list of IC checks to disable (e.g., IC100, IC101).",
        )

    @classmethod
    def parse_options(cls, options):
        """Parse the options provided by the user."""
        if options.disable_ic_checks:
            cls.disabled_checks = options.disable_ic_checks.split(",")

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        """
        Generator that yields issues found in the AST.
        """
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == "ic":
                    error_code = self.IC_ERROR_CODE
                    error_message = (
                        f"{error_code} Avoid using `ic()` from the "
                        "`icecream` package in production code."
                    )
                elif isinstance(node.func, ast.Attribute):
                    if node.func.attr == "enabled":
                        error_code = self.IC_ENABLED_ERROR_CODE
                        error_message = (
                            f"{error_code} Avoid using `ic.enabled()`"
                            " from the `icecream` package in production code."
                        )
                    elif node.func.attr == "disabled":
                        error_code = self.IC_DISABLED_ERROR_CODE
                        error_message = (
                            f"{error_code} Avoid using `ic.disabled()`"
                            " from the `icecream` package in production code."
                        )
                else:
                    continue

                # Skip if the error code is disabled
                if error_code in self.disabled_checks:
                    continue

                yield (node.lineno, node.col_offset, error_message, type(self))
