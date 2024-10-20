from setuptools import setup, find_packages

setup(
    name="custom_llm",
    version="0.1.0",
    description="Custom LLM package for OpenAI and LangChain with SSL off and custom headers.",
    author="Ryan Wesslen",
    author_email="rwesslen@gmail.com",
    packages=find_packages(),
    python_requires='>=3.11',
    install_requires=[
        "requests>=2.28.0",
        "openai>=0.27.0",
        "langchain>=0.0.180",
    ],
)
