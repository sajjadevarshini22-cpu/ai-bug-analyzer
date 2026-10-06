def create_bug_analysis_prompt(bug_report):
    return f"""
You are a Senior QA Engineer and Software Testing Expert.
Analyze the following bug report carefully:
Bug Report:
{bug_report}
Your task is to analyze the defect and provide a professional QA assessment.
IMPORTANT RULES:

1. Analyze ONLY the information provided in the bug report.
2. Do NOT invent technical details that are not supported by the report.
3. Clearly distinguish between facts and possible assumptions.
4. Severity represents the impact of the bug.
5. Priority represents how urgently the bug should be fixed.
6. Provide a reasonable possible root cause,but clearly treat it as a possibility.
7. Suggested fixes should be practical and relevant.
8. Recommended test cases should help verify the bug fix and prevent regression.
9. Avoid duplicate test cases.

Aalyze the following:

1. Bug Summary
2. Possible Root Cause
3. Severity
4. Priority
5. Bug Category
6. Affected Module
7. Steps to Reproduce
8. Expected Result
9. Actual Result
10. Suggested Fix
11. Recommended Test Cases

Allowed Severity:

- Critical
- High
- Medium
- Low

Allowed Priority:

- P0 
- P1 
- P2 
- P3 

Allowed Bug Categories:

- Functional
- Performance
- Security
- UI
- Compatibility
- Validation
- Integration
- Data
- Other

Return ONLY valid JSON.

Use exactly this structure:

{{
    "bug_summary": "",
    "possible_root_cause": "",
    "severity": "",
    "priority": "",
    "bug_category": "",
    "affected_module": "",
    "steps_to_reproduce": [],
    "expected_result": "",
    "actual_result": "",
    "suggested_fix": "",
    "recommended_test_cases": []
}}

"""