import os
from langchain_openai import ChatOpenAI
from deepagents import create_deep_agent
model = ChatOpenAI(
    model=os.environ.get("MODEL_NAME", "Qwen/Qwen2.5-7B-Instruct"),
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    print("工具被调用了，city=", city)
    return f"It's always sunny in {city}!"
agent = create_deep_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant.",
)
result = agent.invoke(
    {"messages": [{"role": "user", "content": "北京今天天气怎么样？"}]}
)
print(result["messages"][-1].content)
