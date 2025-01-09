<!-- Shields -->
<p align="center">
<a href="https://github.com/maekind/pylembic"><img src="https://img.shields.io/github/actions/workflow/status/maekind/pylembic/.github%2Fworkflows%2Ftesting.yaml?label=tests&color=green" hspace="5"></a>
<a href="https://codecov.io/gh/maekind/pylembic"><img src="https://codecov.io/gh/maekind/pylembic/graph/badge.svg?token=JcGna50uJL" hspace="5"/></a>
<a href="https://github.com/maekind/pylembic/releases"><img src="https://img.shields.io/github/actions/workflow/status/maekind/pylembic/.github%2Fworkflows%2Frelease.yaml?label=build package&color=green" hspace="5"></a>
<a href="https://pypi.org/project/pylembic"><img src="https://img.shields.io/github/v/release/maekind/pylembic?color=blue&label=pypi latest" hspace="5"></a>
<br>
<a href="https://github.com/maekind/pylembic/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-orange.svg" hspace="5"></a>
<a href="https://github.com/maekind/pylembic"><img src="https://img.shields.io/github/repo-size/maekind/pylembic?color=red" hspace="5"></a>
<a href="https://github.com/maekind/pylembic"><img src="https://img.shields.io/github/last-commit/maekind/pylembic?color=black" hspace="5"></a>
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/github/languages/top/maekind/pylembic?color=darkgreen" hspace="5"></a>
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python%20version-%3E3.11-lightblue" hspace="5"></a>
</p>

# pylembic

## Description

This package provides validation of Alembic migrations for Python projects.

It will check:

- Linearity: Ensures a clean and predictable migration chain.
- Circular dependencies: Prevents migration failures due to loops in the
dependency chain.
- Orphan migrations: Identifies migrations improperly created without linking
to any other migration.
- Multiple bases/heads: Identifies multiple bases or heads in the migration graph.
- Branching: Detects branching in the migration graph.
- Graph visualization: Provides a visual way to catch anomalies and understand the
migration flow.

## Installation

You can install this package using pip:

```bash
pip install pylembic
```

## Usage

### Testing

You can use this module with your preferred testing framework as follows:

```python
from os import path

from pytest import fixture

from pylembic.validator import Validator


@fixture
def with_alembic_config_path():
    # We assume the migrations folder is at the root of the project,
    # and this test file is in the tests folder, also at the root of the project.
    # TODO: Feel free to adjust the path to your project's migrations folder.
    return path.abspath(
        path.join(path.dirname(path.dirname(__file__)), "migrations")
    )


def test_migrations(with_alembic_config_path):
    migration_validator = Validator(with_alembic_config_path)
    assert migration_validator.validate()
```

### Visualizing the migration graph

You can show the migrations graph by calling the method `show_graph`:

```python

from os import path

from pylembic.validator import Validator

alembic_config_path = path.abspath(path.join("your path", "migrations"))

migration_validator = Validator(alembic_config_path)

migration_validator.show_graph()
```

### Command line interface

You can also use the command line for:

- Validating migrations:

    ```bash
    pylembic ./path/to/migrations validate
    ```

- Validating migrations with branch detection:

    ```bash
    pylembic ./path/to/migrations validate --detect-branches
    ```

- Visualizing the migration graph:

    ```bash
    pylembic ./path/to/migrations show-graph
    ```

CLI is implemented using `typer`, so you can use the `--help` flag to get more information about the available options in every command.

- Show general help:

    ```bash
    pylembic --help
    ```

- Show help for a specific command:

    ```bash
    pylembic validate --help
    ```

#### Caveats

##### Using project imports in migrations

When you are using the command line interface to validate the migrations and you have specific imports from your project in the migrations,
you will probably need to add the path to your project to the `PYTHONPATH` environment variable.
Otherwise, the command line interface will not be able to find the modules.

## Contributors

<a href="https://github.com/maekind/pylembic/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=maekind/pylembic" />
</a>
<br/>
<br/>

(c) <a href="mailto:marco@marcoespinosa.com">Marco Espinosa</a>, 2024
