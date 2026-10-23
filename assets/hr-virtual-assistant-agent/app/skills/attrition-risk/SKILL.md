---
name: attrition-risk
description: Step-by-step instructions for scoring employee attrition risk using HCM signals and presenting findings to HR managers
---

# Attrition Risk Analysis

## When to Use This Skill

Load this skill when a user requests attrition risk information, asks which employees are at risk of leaving, or asks for retention recommendations.

## Instructions

### Step 1: Identify Scope

Determine whether the user wants:
- Company-wide attrition risk
- Department-specific attrition risk (ask for department name if not specified)
- Risk for a specific employee

### Step 2: Retrieve Risk Data

Call the appropriate tool:
- For company or department scope: use `get_attrition_risk` with optional `department` and `top_n` parameters
- For a specific employee: use `get_employee_info` first, then `get_attrition_risk` for the department context

### Step 3: Interpret and Present Results

When presenting attrition risk results:

| Risk Level | Score Range | Recommended Action |
|------------|-------------|-------------------|
| High       | 60–100      | Immediate 1-on-1 retention conversation this month |
| Medium     | 30–59       | Monitor closely, discuss in next 1-on-1              |
| Low        | 0–29        | No immediate action required                         |

### Step 4: Highlight Key Risk Factors

For each at-risk employee, explain the contributing factors in plain language:
- Low performance rating: "This employee's recent performance reviews suggest they may be disengaged."
- Long time without promotion: "They have been in the same role for X years without advancement, which is a common attrition trigger."
- Low engagement score: "Their engagement score indicates they may not feel connected to the team or company goals."

### Step 5: Recommend Actions

Always end with 2–3 concrete actions the manager can take:
1. Schedule a career conversation with the employee this week
2. Review their development plan and ensure they have growth opportunities
3. Escalate to HR Business Partner if the risk is High

## Important Notes

- Attrition risk scores are advisory only — always recommend that managers validate before acting
- Never share one employee's risk data with another employee (only share with the manager of that employee)
- Focus on constructive, supportive language — the goal is retention, not discipline
