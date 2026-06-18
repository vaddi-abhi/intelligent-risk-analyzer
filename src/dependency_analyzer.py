# src/dependency_analyzer.py

import requests


def get_dependencies(package_name):
    """
    Fetch dependency information from PyPI.
    """

    url = f"https://pypi.org/pypi/{package_name}/json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return []

        data = response.json()

        dependencies = (
            data.get("info", {})
            .get("requires_dist", [])
        )

        if dependencies is None:
            dependencies = []

        cleaned_dependencies = []

        for dep in dependencies:
            cleaned_dependencies.append(
                dep.split(";")[0].strip()
            )

        return cleaned_dependencies

    except Exception:
        return []
