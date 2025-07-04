from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic import BaseModel
import tools

ollama_model = OpenAIModel(
    model_name='llama3.2', provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)
agent = Agent(ollama_model, system_prompt='请根据这些天气信息，用女朋友的口吻，语气温柔的告诉我今天应该穿什么衣服（不要表情包）', tools=[tools.get_weather])

def main():
    user_input: str = input("输入： ")
    weather_data = tools.get_weather(user_input)
    # 将天气数据作为上下文传递给AI
    context = f"当前{user_input}的天气信息: {weather_data['lives'][0]}"

    resp = agent.run_sync(context)
    print(resp.output)

if __name__ == '__main__':
    main()