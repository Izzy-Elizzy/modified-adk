from setuptools import setup, find_packages

setup(
    name="google-adk-custom",
    version="0.1.0",
    description="Modified Google ADK with PUT method for session state updates",
    author="Izzy",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "pydantic>=2.0.0",
        "google-genai>=0.1.0",
        "google-cloud-aiplatform>=1.38.0",
        "google-auth>=2.23.0",
        "sqlalchemy>=2.0.0",
        "opentelemetry-api>=1.20.0",
        "opentelemetry-sdk>=1.20.0",
        "python-dotenv>=1.0.0",
        "watchdog>=3.0.0",
        "graphviz>=0.20.0",
        "typing-extensions>=4.8.0",
    ],
)
