from typing import Dict, List
import requests
import json


class LLMMarketApi:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.chat = Chat(api_key)


class Chat:
    def __init__(self, api_key: str) -> None:
        self.completions = Completion(api_key)


class Completion:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def create(self, model: str, messages: List[Dict[str, str]], **kwargs) -> str:
        response = requests.post(
            "https://api.llmmarket.cloud/engine/inference",
            json={
                "model_name": "openai/gpt-3.5-turbo",
                "input_text": json.dumps(messages),
                "max_tokens": 1024,
                "api_key": self.api_key,
                **kwargs,
            },
        )
        llm_answer = response.json()["output"]
        llm_response = LLMResponse(llm_answer)
        return llm_response


class Choice:
    def __init__(self, llm_answer: str) -> None:
        self.message = Message(llm_answer)


class Message:
    def __init__(self, llm_answer: str) -> None:
        self.content = llm_answer


class LLMResponse:
    def __init__(self, llm_answer: str) -> None:
        self.choices = [Choice(llm_answer)]