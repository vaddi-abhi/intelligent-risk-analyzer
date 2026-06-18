# test.py

from src.dependency_analyzer import (
    get_dependencies
)

from src.vulnerability_checker import (
    check_vulnerabilities
)

from src.license_checker import (
    get_license
)

from src.risk_calculator import (
    calculate_risk_score,
    get_risk_level
)

package = "requests"

dependencies = get_dependencies(
    package
)

vulnerabilities = check_vulnerabilities(
    package
)

license_info = get_license(
    package
)

score = calculate_risk_score(
    vulnerabilities,
    dependencies,
    license_info["risk"]
)

print("\nDependencies:")
print(dependencies)

print("\nVulnerabilities:")
print(vulnerabilities)

print("\nLicense:")
print(license_info)

print("\nRisk Score:")
print(score)

print(
    "\nRisk Level:",
    get_risk_level(score)
)
