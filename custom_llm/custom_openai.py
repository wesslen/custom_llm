import openai
import requests
from openai import util

class CustomRequestor(util.Requestor):
    """Custom requestor to handle SSL and custom 'user' header for OpenAI API."""

    def __init__(self):
        super().__init__()
        self._session = requests.Session()
        self._session.verify = False  # Disable SSL verification

    def request(self, method, url, params=None, headers=None, files=None, stream=False, request_id=None, **kwargs):
        if headers is None:
            headers = {}
        headers['user'] = 'your-api-key-here'  # Custom 'user' API key
        return super().request(method, url, params, headers, files, stream, request_id, **kwargs)

def setup_openai(api_key: str, base_url: str):
    """Configures OpenAI to use the custom requestor and base URL."""
    openai.util.requestor.Requestor = CustomRequestor
    openai.api_base = base_url
    openai.api_key = api_key
