import toml


def get_project_metadata():
    """
    Load the project metadata from pyproject.toml.
    Returns:
        dict: Project metadata including name and version.
    """
    try:
        with open("pyproject.toml", "r", encoding="utf-8") as f:
            pyproject = toml.load(f)
        project = pyproject.get("project", {})
        return {
            "name": project.get("name", "flake8-ic"),
            "version": project.get("version", "0.1.0"),
        }
    except Exception:
        return {"name": "flake8-ic", "version": "0.1.0"}
