# Specification: hr-virtual-assistant-agent

> **Guidelines**: Read all applicable guidelines before executing ANY tasks below:
> - [guidelines.md](../guidelines.md) — Universal execution rules
> - [guidelines-agent.md](../guidelines-agent.md) — Universal agent patterns
> - [guidelines-agent-python.md](../guidelines-agent-python.md) — Python implementation details
> - [guidelines-agent-skills.md](../guidelines-agent-skills.md) — Runtime skills patterns
> - [guidelines-agent-mcp.md](../guidelines-agent-mcp.md) — MCP integration patterns

---

## Basic Setup

- [x] Read the project input (`product-requirements-document.md`, `intent.md`)
- [x] Bootstrap agent code in `assets/hr-virtual-assistant-agent/` using the `sap-agent-bootstrap` skill instructions (invoke from inside `assets/hr-virtual-assistant-agent/`, use copy commands — do NOT create files manually)
- [x] Install dependencies, validate the agent starts and responds at `/.well-known/agent.json`

---

## Runtime Skills

The HR domain has complex multi-step logic suitable for runtime skills:

- [x] Create `assets/hr-virtual-assistant-agent/app/skills/attrition-risk/SKILL.md` with:
  - Frontmatter: `name: attrition-risk`, `description: Step-by-step instructions for scoring employee attrition risk using HCM signals`
  - Body: Instructions on how to interpret tenure, performance, engagement, and role-change signals to compute a risk score and rank employees
- [x] Create `assets/hr-virtual-assistant-agent/app/skills/development-recommendations/SKILL.md` with:
  - Frontmatter: `name: development-recommendations`, `description: Instructions for generating personalised employee development recommendations based on skills, performance, and career goals`
  - Body: Instructions on matching skill gaps with learning paths, career ladders, and actionable next steps

---

## Project-Specific Tasks

### HCM Data Simulation

- [x] Create `assets/hr-virtual-assistant-agent/app/hcm_data.py` with simulated HCM dataset containing:
  - 30–50 employees with: `employee_id`, `name`, `department`, `role`, `tenure_years`, `performance_rating` (1–5), `engagement_score` (1–10), `skills` (list), `manager_id`, `last_promotion_years_ago`, `salary_band`, `status` (active/at-risk)
  - Functions: `get_all_employees()`, `get_employee_by_id(employee_id)`, `get_department_employees(department)`, `get_workforce_summary()`, `compute_attrition_risk(employee_id)`
  - `compute_attrition_risk` uses heuristic scoring: low performance (<3) + high tenure without promotion (>3 years) + low engagement (<5) → high risk
  - HR policy knowledge base as a Python dict mapping common questions to answers (leave policy, benefits, compensation bands, onboarding process, performance review cycle)

### Agent Tools (Custom Python Functions)

- [x] Create `assets/hr-virtual-assistant-agent/app/tools/hr_tools.py` with the following tools as LangChain `StructuredTool` instances:
  - `get_employee_info(employee_id: str)` — returns employee profile from simulated data
  - `get_workforce_analytics(department: str = None)` — returns headcount, avg tenure, turnover rate, avg performance, and engagement scores (optionally filtered by department)
  - `get_attrition_risk(department: str = None, top_n: int = 10)` — returns ranked list of at-risk employees with risk score and top contributing factors
  - `get_development_recommendations(employee_id: str)` — returns 3–5 personalised development suggestions based on skills and performance gaps
  - `get_hr_insights(scope: str = "all")` — returns a structured narrative summary of HR health (turnover trends, engagement, performance distribution)
  - `answer_hr_policy_question(question: str)` — returns best-matching HR policy answer using keyword matching from the policy knowledge base
- [x] All tools must use `hcm_data.py` as the sole data source — no external calls

### Agent System Prompt

- [x] In `assets/hr-virtual-assistant-agent/app/agent.py`, configure the system prompt to:
  - Introduce the agent as an HR Virtual Assistant for employees and HR managers
  - Instruct it to use the available tools for all data queries — never fabricate or guess HR data
  - Clarify that data is simulated and the agent is advisory only
  - Instruct it to decline requests for another employee's personal data (privacy guardrail)
  - Specify that all attrition risk outputs are advisory and require human validation before action
  - Note that when answering HR policy questions, the agent uses a built-in policy knowledge base

### Agent Wiring

- [x] In `assets/hr-virtual-assistant-agent/app/agent.py`, import and register tools from `tools/hr_tools.py`
- [x] Wire tools directly into the agent (no MCP server needed — all tools are local Python functions using simulated data)
- [x] Ensure tool list is passed to the LangChain agent graph correctly

---

## Business Instrumentation

- [x] Implement business step instrumentation for each milestone with structured logging + OpenTelemetry spans:
  - `M1.achieved: HR policy Q&A tool is operational and returning accurate answers`
  - `M1.missed: HR policy Q&A tool did not complete initialization or failed accuracy check`
  - `M2.achieved: Workforce analytics tool is operational and returning correct metrics`
  - `M2.missed: Workforce analytics tool failed to return expected metrics`
  - `M3.achieved: Attrition risk scoring tool is operational and returning ranked results with explanations`
  - `M3.missed: Attrition risk scoring tool did not return expected ranked output`
  - `M4.achieved: Development recommendation tool is operational and returning personalised suggestions`
  - `M4.missed: Development recommendation tool did not return personalised output`
  - `M5.achieved: HR insight reporting tool is operational and returning structured summaries`
  - `M5.missed: HR insight reporting tool did not return expected structured output`
- [x] Extract all business logic from `stream()` into a plain async helper `_run_agent()` to avoid `GeneratorExit` context errors when using OpenTelemetry spans
- [x] Verify `bootstrap(app)` is called after `app = server.build()` in `main.py`

---

## MCP Tool Integration

No external MCP server is required — all tools are local Python functions using simulated HCM data. Skip MCP discovery, translation, and mock generation steps.

---

## Testing

- [x] `conftest.py` only sets `IBD_TESTING=true`
- [x] Write unit tests in `assets/hr-virtual-assistant-agent/tests/` — one per tool:
  - `test_get_employee_info.py` — valid employee ID returns expected fields; invalid ID returns error
  - `test_get_workforce_analytics.py` — returns headcount and metrics; department filter works correctly
  - `test_get_attrition_risk.py` — returns ranked list with risk scores and factors; `top_n` parameter respected
  - `test_get_development_recommendations.py` — returns 3+ recommendations for a valid employee ID
  - `test_get_hr_insights.py` — returns structured summary with expected sections
  - `test_answer_hr_policy_question.py` — known HR questions return non-empty answers
- [x] Write one integration test in `assets/hr-virtual-assistant-agent/tests/test_integration.py` executing the end-to-end agent flow with mocked LLM responses
- [x] Run `pytest` from `assets/hr-virtual-assistant-agent/` (no args) — coverage: 81% ✓
- [x] Run `pytest` again (no args) to generate final `test_report.json`
- [x] Verify `test_report.json` exists in `assets/hr-virtual-assistant-agent/`
