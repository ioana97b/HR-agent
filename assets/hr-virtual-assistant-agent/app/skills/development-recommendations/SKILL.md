---
name: development-recommendations
description: Instructions for generating personalised employee development recommendations based on skills, performance, and career goals
---

# Development Recommendations

## When to Use This Skill

Load this skill when a user asks for development suggestions, career guidance, training recommendations, or growth plans for a specific employee.

## Instructions

### Step 1: Retrieve Employee Profile

Use `get_employee_info` with the employee's ID to retrieve their current role, skills, performance rating, engagement score, and tenure.

If the user does not provide an employee ID, ask for it: "Could you please provide the employee ID? (e.g. E001)"

### Step 2: Generate Development Plan

Use `get_development_recommendations` with the employee ID. The tool returns prioritised recommendations across these categories:

| Category                  | Trigger Condition                                   |
|---------------------------|-----------------------------------------------------|
| Performance Improvement   | Performance rating ≤ 2                              |
| Skill Enhancement         | Performance rating = 3                              |
| Technical Certification   | Missing cloud or language skills for engineers      |
| Leadership Development    | Manager or director roles                           |
| Promotion Readiness       | High performer, 1.5+ years since last promotion     |
| Engagement & Wellbeing    | Engagement score ≤ 5                                |
| Cross-Functional Exposure | Tenure ≥ 2 years, fewer than 5 other recommendations|

### Step 3: Present Recommendations Clearly

Format the recommendations as a numbered list with:
- **Type**: Category of the development action
- **Action**: The specific, actionable step
- **Priority**: High / Medium / Low
- **Why**: Briefly explain why this recommendation is relevant to this employee

### Step 4: Link to Resources

Where relevant, suggest:
- SAP SuccessFactors Learning portal for certifications and courses
- Internal mentorship programme for leadership development
- HR portal for promotion eligibility check

### Step 5: Offer Next Steps

End with: "Would you like me to help draft a development goal for this employee, or explain any of these recommendations in more detail?"

## Important Notes

- Recommendations are generated from simulated data — real recommendations should also incorporate the employee's own stated career goals
- Never share development recommendations with peers — only with the employee and their manager
- High-priority items should be addressed within the current quarter
