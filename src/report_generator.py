

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    package_name,
    dependencies,
    vulnerabilities,
    license_info,
    risk_score,
    risk_level
):

    filename = (
        f"reports/{package_name}_report.pdf"
    )

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Intelligent Risk Analyzer Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Package: {package_name}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"License: {license_info['license']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"License Risk: {license_info['risk']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Score: {risk_score}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Level: {risk_level}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Dependencies",
            styles["Heading2"]
        )
    )

    for dep in dependencies:
        content.append(
            Paragraph(
                dep,
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Vulnerabilities",
            styles["Heading2"]
        )
    )

    if vulnerabilities:

        for vuln in vulnerabilities:

            content.append(
                Paragraph(
                    vuln["id"],
                    styles["Normal"]
                )
            )

            content.append(
                Paragraph(
                    vuln["summary"],
                    styles["Normal"]
                )
            )

    else:

        content.append(
            Paragraph(
                "No vulnerabilities found.",
                styles["Normal"]
            )
        )

    doc.build(content)

    return filename
