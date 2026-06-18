import streamlit as st

from src.dependency_analyzer import get_dependencies
from src.report_generator import (
    generate_report
)

from src.graph_generator import (
    create_dependency_graph
)
from src.vulnerability_checker import check_vulnerabilities
from src.license_checker import get_license
from src.risk_calculator import (
    calculate_risk_score,
    get_risk_level
)

st.sidebar.title(
    "Project Information"
)

st.sidebar.markdown("""
### Features

✅ Dependency Analysis

✅ Vulnerability Detection

✅ License Detection

✅ Risk Scoring

Built using:

- Python
- Streamlit
- PyPI API
- OSV API
""")

st.set_page_config(
    page_title="Intelligent Risk Analyzer",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Intelligent Vulnerability & License Risk Analyzer")

st.markdown("""
Analyze Python packages for:

- Dependencies
- Vulnerabilities
- License Information
- Overall Risk Score
""")

package_name = st.text_input(
    "Enter Python Package Name",
    placeholder="Example: requests"
)

analyze_button = st.button(
    "Analyze Package"
)

if analyze_button:

    if not package_name.strip():

        st.warning(
            "Please enter a package name."
        )

    else:

        with st.spinner(
            "Analyzing package..."
        ):

            dependencies = get_dependencies(
                package_name
            )

            vulnerabilities = (
                check_vulnerabilities(
                    package_name
                )
            )

            license_info = get_license(
                package_name
            )

            risk_score = (
                calculate_risk_score(
                    vulnerabilities,
                    dependencies,
                    license_info["risk"]
                )
            )

            risk_level = (
                get_risk_level(
                    risk_score
                )
            )

        st.success(
            "Analysis Complete"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Dependencies",
                len(dependencies)
            )

        with col2:
            st.metric(
                "Vulnerabilities",
                len(vulnerabilities)
            )

        with col3:
            st.metric(
                "Risk Score",
                risk_score
            )

        st.divider()

        st.subheader(
            "Risk Assessment"
        )

        if risk_level == "Low":
            st.success(
                f"Risk Level: {risk_level}"
            )

        elif risk_level == "Medium":
            st.warning(
                f"Risk Level: {risk_level}"
            )

        elif risk_level == "High":
            st.error(
                f"Risk Level: {risk_level}"
            )

        else:
            st.error(
                f"Risk Level: {risk_level}"
            )

        st.divider()

        st.subheader(
            "License Information"
        )

        st.write(
            f"License: {license_info['license']}"
        )

        st.write(
            f"License Risk: {license_info['risk']}"
        )

        st.divider()

        st.subheader(
            "Dependencies"
        )

        if dependencies:

            for dep in dependencies:
                st.write(f"• {dep}")

        else:
            st.info(
                "No dependencies found."
            )

        st.divider()

        st.subheader(
            "Vulnerabilities"
        )

        if vulnerabilities:

            for vuln in vulnerabilities:

                st.error(
                    f"{vuln['id']}"
                )

                st.write(
                    vuln['summary']
                )

                st.write("---")

        else:

            st.success(
                "No vulnerabilities found."
            )


st.divider()

st.caption(
    "Developed by Abhi Vaddi | NIT Durgapur"
)
