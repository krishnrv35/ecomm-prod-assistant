import importlib.metadata
packages = [
    "beautifulsoup4",
    "ddgs",
    "FASTAPI",
    "html5lib",
    "jinja2",
    "langchain",
    "langchain-astradb",
    "langchain-google-genai",
    "langchain-groq",
    "langchain-mcp-adapters",
    "langchain-openai",
    "langchain_core",
    "langgraph",
    "lxml",
    "mcp",
    "python-dotenv",
    "python-multipart",
    "pypdf",
    "ragas",
    "selenium",
    "streamlit",
    "structlog",
    "undetected-chromedriver",
    "uvicorn"
]

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")