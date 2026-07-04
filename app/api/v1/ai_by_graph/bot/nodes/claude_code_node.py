from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

from app.api.v1.ai_by_graph.bot.state import LangGraphState
from app.api.v1.ai_by_graph.bot.prompts.claude_prompt import prompt

async def claude_node(state: LangGraphState):
    result = ""
    async for msg in query(
        prompt = prompt,
        options = ClaudeAgentOptions(
            allowed_tools = ["read", "edit..."],
            cwd = "/path/to/repo"
        ),
    ):
        if isinstance(msg, ResultMessage):
            result = msg.result
    return {"implementation_report": result}