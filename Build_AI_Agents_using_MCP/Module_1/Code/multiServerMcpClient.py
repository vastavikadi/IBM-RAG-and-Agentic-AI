from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents.factory import create_agent
from langchain_openai.chat_models import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
import os
import asyncio


async def main():
    client = MultiServerMCPClient(
        {
            "context7": {
                "url": "https://mcp.context7.com/mcp",
                "transport": "streamable_http",
            },
            "met-museum": {
                "command": "npx",
                "args": ["-y", "metmuseum-mcp"],
                "transport": "stdio",
            },
        }
    )

    tools = await client.get_tools()
    print("\n=== Available tools ===")
    for tool in tools:
        print(f" - {tool}")

        print(f"   - description: {tool.description}")

        print(f"   - input_schema: {tool.input_schema}")

    openai_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, api_key=os.environ.get("OPENAI_API_KEY"))

    checkpointer = InMemorySaver()
    config = {"configurable": {"thread_id": "conversation_id"}}

    agent = create_agent(
        {
            "model": openai_model,
            "tools": tools,
            "checkpointer": checkpointer,
        }
    )

    response = await agent.anivoke(
        {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a smart, useful agent with tools to access code library documentation and the Met museum collection.",
                },
                {
                    "role": "user",
                    "content": "Give a brief introduction of what you do and the tools you have access to.",
                },
            ]
        },
        config=config,
    )

    print (response["messages"][-1]["content"])


# runs the main function if this script is executed directly and if importable as a module, it won't run the main function automatically.
if __name__ == "__main__":
    asyncio.run(main())
