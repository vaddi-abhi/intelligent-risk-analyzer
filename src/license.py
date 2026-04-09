import requests

def get_license(package_name):
    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        return data["info"].get("license", "Unknown")

    except Exception as e:
        print(f"Error fetching license: {e}")
        return "Unknown"