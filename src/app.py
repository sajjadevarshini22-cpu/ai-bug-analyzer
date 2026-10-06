import streamlit as st

from ai_analyzer import analyze_bug
from validator import validate_bug_analysis
from excel_generator import create_bug_report_excel
# Session state
if "bug_analysis" not in st.session_state:
    st.session_state.bug_analysis = None


st.title("🐞 AI Bug Analyzer")

st.caption(
    "Analyze bug reports using AI and generate structured QA insights"
)


bug_report = st.text_area(
    "Enter Bug Report",
    placeholder=(
        "Example: Login button is not working when I enter "
        "valid username and password. The user remains on "
        "the login page."
    ),
    height=200
)


# Analyze Bug
if st.button("Analyze Bug"):

    if not bug_report.strip():

        st.warning("Please enter a bug report.")

    else:

        with st.spinner("Analyzing bug..."):

            try:

                analysis = analyze_bug(bug_report)

                st.session_state.bug_analysis = analysis

                st.success(
                    "Bug analysis completed successfully!"
                )

            except ValueError as error:

                st.error(f"⚠️ {error}")

            except RuntimeError as error:

                st.error(f"❌ {error}")

            except Exception:

                st.error(
                    "❌ Something went wrong. Please try again."
                )


# Display Analysis
if st.session_state.bug_analysis:

    analysis = st.session_state.bug_analysis

    errors = validate_bug_analysis(analysis)

    if errors:

        st.error("❌ Bug analysis validation failed")

        for error in errors:
            st.write("•", error)

    else:

        st.subheader("📋 Bug Summary")

        st.write(
            analysis["bug_summary"]
        )

        st.subheader("🔍 Possible Root Cause")

        st.write(
            analysis["possible_root_cause"]
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Severity",
                analysis["severity"]
            )

        with col2:

            st.metric(
                "Priority",
                analysis["priority"]
            )

        with col3:

            st.metric(
                "Category",
                analysis["bug_category"]
            )

        with col4:

            st.metric(
                "Module",
                analysis["affected_module"]
            )
        st.subheader("📦 Affected Module")

        st.write(
            analysis["affected_module"]
        )

        st.subheader("🔁 Steps to Reproduce")

        for step in analysis["steps_to_reproduce"]:

            st.write("➡️", step)

        st.subheader("✅ Expected Result")

        st.write(
            analysis["expected_result"]
        )

        st.subheader("❌ Actual Result")

        st.write(
            analysis["actual_result"]
        )

        st.subheader("🛠️ Suggested Fix")

        st.write(
            analysis["suggested_fix"]
        )

        st.subheader("🧪 Recommended Test Cases")

        for test_case in analysis[
            "recommended_test_cases"
        ]:

            st.write("➡️", test_case)
        st.subheader("📥 Download Report")

        excel_file = create_bug_report_excel(analysis)

        st.download_button(
            label="📥 Download Bug Analysis Excel",
            data=excel_file,
            file_name="ai_bug_analysis.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
