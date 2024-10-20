from langchain.llms import OpenAI
import requests

class CustomOpenAI(OpenAI):
    """Custom LangChain OpenAI wrapper to handle SSL and custom 'user' header."""

    def __init__(self, api_key: str, base_url: str, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key  # 'user' header API key
        self.base_url = base_url

    def _call(self, prompt: str, stop=None) -> str:
        headers = {
            "user": self.api_key,
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
        }
        response = requests.post(
            f"{self.base_url}/v1/completions", 
            json=payload, 
            headers=headers, 
            verify=False
        )
        response.raise_for_status()
        return response.json()["choices"][0]["text"]
