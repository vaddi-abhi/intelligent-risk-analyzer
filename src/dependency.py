import requests

def get_dependencies(package_name):
    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        requires = data["info"].get("requires_dist", [])

        dependencies = []
        if requires:
            for dep in requires:
                dependencies.append(dep.split(";")[0].strip())

        return dependencies

    except Exception as e:
        print(f"Error fetching dependencies: {e}")
        return []