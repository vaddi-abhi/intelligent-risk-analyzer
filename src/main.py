from dependency import get_dependencies
from vulnerability import get_vulnerabilities
from license import get_license
from risk import build_graph, calculate_risk


def analyze(package):
    print("\n--- Analysis Report ---")

    deps = get_dependencies(package)
    vulns = get_vulnerabilities(package)
    license_name = get_license(package)

    graph = build_graph(package, deps)
    risk = calculate_risk(vulns, license_name)

    print(f"\nPackage: {package}")
    print(f"Dependencies ({len(deps)}): {deps}")
    print(f"Vulnerabilities ({len(vulns)}): {vulns}")
    print(f"License: {license_name}")
    print(f"Risk Score: {risk}")

    print("\nSuggestions:")
    if vulns:
        print("- Update package to latest secure version")
    if "GPL" in license_name.upper():
        print("- Check license compatibility")

    print("\n-----------------------\n")


if __name__ == "__main__":
    while True:
        pkg = input("Enter package name (or 'exit'): ").strip()

        if pkg.lower() == "exit":
            break

        if pkg:
            analyze(pkg)