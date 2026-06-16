import os

from langchain.agents import create_agent
from langchain.messages import AIMessage, HumanMessage
api_key_val = os.getenv("DEEPSEEK_API_KEY")

def get_weather(city: str) -> str:
    """Get weather for a given city, 定义查询天气的tool"""
    return f"It's always sunny in {city}!"

if __name__ == '__main__':
    agent = create_agent(
        model="deepseek-chat",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )
    # noinspection PyTypeChecker
    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "What's the weather in San Francisco?"}
            ]
        }
    )
    print(result["messages"][-1].content_blocks)

    # agent流式调用，输出"## Recent AI News Summary": xxxxx
    for chunk in agent.stream(
            {"messages": [{"role": "user", "content": "Search for AI news and summarize the findings"}]
    }, stream_mode="values"):
        # Each chunk contains the full state at that point
        latest_message = chunk["messages"][-1]
        if latest_message.content:
            if isinstance(latest_message, HumanMessage):
                print(f"User: {latest_message.content}")
            elif isinstance(latest_message, AIMessage):
                print(f"Agent: {latest_message.content}")
        elif latest_message.tool_calls:
            print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")
