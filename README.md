<!-- Shields -->
<p align="center">
<a href="https://github.com/maekind/flake8-ic/actions/workflows/testing.yaml"><img src="https://img.shields.io/github/actions/workflow/status/maekind/flake8-ic/testing.yaml?style=for-the-badge&label=Tests 🧪" hspace="5" vspace="2"></a>
<a href="https://codecov.io/gh/maekind/flake8-ic"><img src="https://img.shields.io/codecov/c/github/maekind/flake8-ic?style=for-the-badge&color=yellow&label=COVERAGE 📊" hspace="5" vspace="2"></a>
<br>
<a href="https://github.com/maekind/flake8-ic/actions/workflows/release.yaml"><img src="https://img.shields.io/github/actions/workflow/status/maekind/flake8-ic/release.yaml?style=for-the-badge&label=Release and Publish ✨" hspace="5" vspace="2"></a>
<a href="https://pypi.org/project/flake8-ic"><img src="https://img.shields.io/github/v/release/maekind/flake8-ic?color=blue&label=pypi 📦&style=for-the-badge" hspace="5" vspace="2"></a>
<br>  
<a href="https://github.com/maekind/flake8-ic/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge&label=license 📜" hspace="5" vspace="2"></a>
<a href="https://github.com/maekind/flake8-ic"><img src="https://img.shields.io/github/repo-size/maekind/flake8-ic?color=red&style=for-the-badge&label=repo size 🗄️" hspace="5" vspace="2"></a>
<a href="https://github.com/maekind/flake8-ic"><img src="https://img.shields.io/github/last-commit/maekind/flake8-ic?color=black&style=for-the-badge&label=last commit ⏳" hspace="5" vspace="2"></a>
<br>
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python%20versions%20🐍-3.11%20|%203.12%20|%203.13-lightblue?style=for-the-badge" hspace="5" vspace="2"></a>
</p>

# 🌟 flake8-ic

A **Flake8 plugin** that helps detect the usage of the `ic()` function from the `icecream` package in your codebase.

---

## 📜 Description

The `flake8-ic` plugin ensures clean and production-ready code by identifying any instances of the `ic()` function, commonly used for debugging. This tool integrates seamlessly with `flake8` to provide automated checks.

---

## 🚨 Detected Errors

The `flake8-ic` plugin checks for the usage of the `ic()` function and related methods from the `icecream` package in your codebase. Below is a list of errors it detects:

| **Error Code** | **Description**                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------|
| `IC100`        | Avoid using `ic()` from the `icecream` package in production code.                                  |
| `IC101`        | Avoid using `ic.disabled()` from the `icecream` package in production code.                         |
| `IC102`        | Avoid using `ic.enabled()` from the `icecream` package in production code.                          |

---

### 🚫 Disabling Checks

You can disable specific checks for `flake8-ic` using the `--disable-ic-checks` option. This is useful if you only want to enforce certain rules. The following options are available:

- `IC100`: Disables checks for the `ic()` function.
- `IC101`: Disables checks for the `ic.disabled()` method.
- `IC102`: Disables checks for the `ic.enabled()` method.

#### Examples

1. **Disable a Single Check**:

   ```bash
   flake8 --disable-ic-checks=IC100
   ```

   This will disable only the `IC100` check.

2. **Disable Multiple Checks**:

   ```bash
    flake8 --disable-ic-checks=IC100,IC101
    ```

    This will disable both the `IC100` and `IC101` checks.

3. **Configuration in setup.cfg or tox.ini**:
   You can set this option in your configuration file to apply it automatically:

   ```bash
   [flake8]
   disable-ic-checks = IC100,IC102
   ```

4. **Configuration in pyproject.toml**:
   Add the configuration under the [tool.flake8] section:

   ```bash
   [tool.flake8]
   disable-ic-checks = "IC100,IC102"
   ```

By disabling checks, you can tailor the plugin to match your project’s requirements while maintaining a clean and focused codebase.

## 📦 Installation

Install the plugin via `pip`:

```bash
pip install flake8-ic
```

---

## ✅ Verifying Installation

To confirm the plugin is installed, run:

```bash
flake8 --version
```

You should see `flake8-ic` listed among the installed plugins, along with the Flake8 version.

---

## 🤝 Contributors

A big thank you to everyone who contributed to this project! 💖

<a href="https://github.com/maekind/flake8-ic/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=maekind/flake8-ic" alt="Contributors" />
</a>

---

## 📧 Contact

(c) 2025, Created with ❤️ by [Marco Espinosa](mailto:marco@marcoespinosa.com)
