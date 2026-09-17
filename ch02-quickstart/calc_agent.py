import os
from langchain_openai import ChatOpenAI
from deepagents import create_deep_agent
model = ChatOpenAI(
    model=os.environ.get("MODEL_NAME", "Qwen/Qwen2.5-7B-Instruct"),
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)
def calculate(expression: str) -> float:
    """Evaluate a math expression and return the result.
    Args:
        expression: A math expression, e.g. "1 + 2 * 3".
    """
    # 仅做演示，实际项目应使用安全的解析库而非 eval
    print("调用 calculate，expression=", expression)
    return eval(expression)
def convert_currency(amount: float, from_currency: str, to_currency: str = "CNY") -> dict:
    """Convert an amount from one currency to another.
    Args:
        amount: The amount to convert.
        from_currency: The source currency code, e.g. "USD".
        to_currency: The target currency code, defaults to "CNY".
    """
    print("调用 convert_currency，", amount, from_currency, "->", to_currency)
    rates = {"USD": 7.2, "CNY": 1.0, "EUR": 7.8}
    cny = amount * rates[from_currency]
    return {"amount": round(cny / rates[to_currency], 2), "currency": to_currency}
agent = create_deep_agent(
    model=model,
    tools=[calculate, convert_currency],
    system_prompt="你是一个计算助手，能帮用户做数学运算和货币换算。",
)
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "帮我把 100 美元换算成人民币，再用它乘以 1.08 的通胀系数。",
            }
        ]
    }
)
print(result["messages"][-1].content)
