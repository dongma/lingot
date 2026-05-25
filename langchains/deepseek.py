import os

from langchain.agents import create_agent

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
