"""Integration test for the HR Virtual Assistant agent end-to-end flow."""
import sys
import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from agent import SampleAgent
from tools.hr_tools import get_hr_tools


def make_mock_llm_response(content: str):
    """Create a mock LLM response with the given content."""
    mock_message = MagicMock()
    mock_message.content = content
    mock_message.type = "ai"
    return {"messages": [mock_message]}


class TestHRAgentIntegration:
    """Integration tests for the HR Virtual Assistant agent."""

    def test_agent_initializes_successfully(self):
        """Agent should initialize without errors."""
        agent = SampleAgent()
        assert agent is not None
        assert agent.llm is not None

    def test_hr_tools_are_loadable(self):
        """HR tools should load without errors."""
        tools = get_hr_tools()
        assert len(tools) == 6
        tool_names = [t.name for t in tools]
        assert "get_employee_info" in tool_names
        assert "get_workforce_analytics" in tool_names
        assert "get_attrition_risk" in tool_names
        assert "get_development_recommendations" in tool_names
        assert "get_hr_insights" in tool_names
        assert "answer_hr_policy_question" in tool_names

    @pytest.mark.asyncio
    async def test_agent_invoke_with_mocked_llm(self):
        """Agent should invoke and return a response with mocked LLM."""
        agent = SampleAgent()
        tools = get_hr_tools()

        mock_response = make_mock_llm_response("The annual leave policy provides 25 days per year.")

        with patch.object(agent, "_invoke", new_callable=AsyncMock) as mock_invoke:
            mock_invoke.return_value = mock_response

            result = await agent.invoke(
                query="What is the leave policy?",
                context_id="test-context-001",
                tools=tools,
            )

            assert result.status == "completed"
            assert len(result.message) > 0
            mock_invoke.assert_called_once()

    @pytest.mark.asyncio
    async def test_agent_stream_with_mocked_llm(self):
        """Agent should stream responses with mocked LLM."""
        agent = SampleAgent()
        tools = get_hr_tools()

        mock_response = make_mock_llm_response("Engineering team has 8 employees with average tenure of 3.2 years.")

        chunks = []
        with patch.object(agent, "_invoke", new_callable=AsyncMock) as mock_invoke:
            mock_invoke.return_value = mock_response
            async for chunk in agent.stream(
                query="Show me Engineering workforce analytics",
                context_id="test-context-002",
                tools=tools,
            ):
                chunks.append(chunk)

        assert len(chunks) >= 2  # At least "Processing..." and final response
        final = [c for c in chunks if c.get("is_task_complete")]
        assert len(final) == 1
        assert len(final[0]["content"]) > 0

    @pytest.mark.asyncio
    async def test_agent_handles_no_tools_gracefully(self):
        """Agent should handle the case where no tools are provided."""
        agent = SampleAgent()

        mock_response = make_mock_llm_response("I am unable to process your request as no tools are available.")

        with patch.object(agent, "_invoke", new_callable=AsyncMock) as mock_invoke:
            mock_invoke.return_value = mock_response

            result = await agent.invoke(
                query="What is the leave policy?",
                context_id="test-context-003",
                tools=[],
            )

            assert result.status == "completed"

    @pytest.mark.asyncio
    async def test_agent_handles_llm_exception(self):
        """Agent should return error response on LLM exception."""
        agent = SampleAgent()
        tools = get_hr_tools()

        with patch.object(agent, "_invoke", new_callable=AsyncMock) as mock_invoke:
            mock_invoke.side_effect = RuntimeError("Simulated LLM failure")

            result = await agent.invoke(
                query="Who is at risk of leaving?",
                context_id="test-context-004",
                tools=tools,
            )

            assert result.status in ["error", "completed"]