VALID_SEVERITIES = [
    "Critical",
    "High",
    "Medium",
    "Low"
]


VALID_PRIORITIES = [
    "P0",
    "P1",
    "P2",
    "P3"
]

VALID_CATEGORIES = [
    "Functional",
    "UI",
    "Performance",
    "Security",
    "Compatibility",
    "Validation",
    "Integration",
    "Data",
    "Other"
]


def validate_bug_analysis(analysis):

    errors = []

    required_fields = [
        "bug_summary",
        "possible_root_cause",
        "severity",
        "priority",
        "bug_category",
        "affected_module",
        "steps_to_reproduce",
        "expected_result",
        "actual_result",
        "suggested_fix",
        "recommended_test_cases"
    ]

    for field in required_fields:

        if field not in analysis:
            errors.append(f"Missing field: {field}")

        elif not analysis[field]:
            errors.append(f"Empty field: {field}")

    if analysis.get("severity") not in VALID_SEVERITIES:
        errors.append("Invalid severity")
    if analysis.get("priority") not in VALID_PRIORITIES:
        errors.append("Invalid Priority")

    if analysis.get("bug_category") not in VALID_CATEGORIES:
        errors.append("Invalid bug category")

    if not isinstance(
        analysis.get("steps_to_reproduce"), list):
        errors.append( "Steps to reproduce must be a list")  

    if not isinstance(
        analysis.get("recommended_test_cases"),list):
        errors.append("Recommended test cases must be a list")
    return errors

            





