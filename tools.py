import os

import requests
from typing import Dict, Any
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('GAOde_KEY')
def get_weather(city: str) -> Dict[str, Any]:
    """获取指定城市的天气信息"""
    try:
        # 这里使用模拟API，实际使用时替换为真实API
        response = requests.get(
            f"https://restapi.amap.com/v3/weather/weatherInfo?key={api_key}&city={city}&output=json"
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e), "function": "get_weather"}

if __name__ == "__main__":
    response = get_weather('北京')
    weather_details = response['lives'][0]  # lives是包含天气详情的列表
    print(f"城市: {weather_details.get('city')}")
    print(f"天气: {weather_details.get('weather')}")
    print(f"温度: {weather_details.get('temperature')}°C")
    print(f"风向: {weather_details.get('winddirection')}")
    print(f"风力: {weather_details.get('windpower')}级")
    print(f"湿度: {weather_details.get('humidity')}%")
    print(f"更新时间: {weather_details.get('reporttime')}")