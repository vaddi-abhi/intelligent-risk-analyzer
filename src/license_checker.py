# src/license_checker.py

import requests


def get_license(package_name):

    url = f"https://pypi.org/pypi/{package_name}/json"

    try:

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code != 200:
            return {
                "license": "Unknown",
                "risk": "Medium"
            }

        data = response.json()

        license_name = (
            data.get("info", {})
            .get("license", "")
        )

        if not license_name:
            license_name = "Unknown"

        risk = classify_license_risk(
            license_name
        )

        return {
            "license": license_name,
            "risk": risk
        }

    except Exception:

        return {
            "license": "Unknown",
            "risk": "Medium"
        }


def classify_license_risk(license_name):

    license_name = license_name.lower()

    if "mit" in license_name:
        return "Low"

    if "apache" in license_name:
        return "Low"

    if "bsd" in license_name:
        return "Low"

    if "gpl" in license_name:
        return "High"

    return "Medium"
