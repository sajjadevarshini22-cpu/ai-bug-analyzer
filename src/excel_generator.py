from openpyxl import Workbook
from io import BytesIO


def create_bug_report_excel(analysis):

    workbook = Workbook()

    sheet = workbook.active
    sheet.title = "Bug Analysis"

    sheet.append([
        "Field",
        "Analysis"
    ])

    sheet.append([
        "Bug Summary",
        analysis["bug_summary"]
    ])

    sheet.append([
        "Possible Root Cause",
        analysis["possible_root_cause"]
    ])

    sheet.append([
        "Severity",
        analysis["severity"]
    ])

    sheet.append([
        "Priority",
        analysis["priority"]
    ])

    sheet.append([
        "Bug Category",
        analysis["bug_category"]
    ])

    sheet.append([
        "Affected Module",
        analysis["affected_module"]
    ])

    sheet.append([
        "Steps to Reproduce",
        "\n".join(analysis["steps_to_reproduce"])
    ])

    sheet.append([
        "Expected Result",
        analysis["expected_result"]
    ])

    sheet.append([
        "Actual Result",
        analysis["actual_result"]
    ])

    sheet.append([
        "Suggested Fix",
        analysis["suggested_fix"]
    ])

    sheet.append([
        "Recommended Test Cases",
        "\n".join(analysis["recommended_test_cases"])
    ])

    excel_file = BytesIO()

    workbook.save(excel_file)

    excel_file.seek(0)

    return excel_file