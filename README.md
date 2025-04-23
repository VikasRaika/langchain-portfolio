# LangChain Portfolio

This portfolio showcases various applications and implementations using LangChain, a framework for developing applications powered by language models.

## Project Structure

```
langchain-portfolio/
├── src/                    # Source code
│   ├── agents/            # Agent implementations
│   ├── chains/            # Chain implementations
│   ├── memory/            # Memory implementations
│   ├── prompts/           # Prompt templates
│   └── utils/             # Utility functions
├── tests/                 # Test files
├── notebooks/             # Jupyter notebooks
├── data/                  # Data files
├── .env                   # Environment variables
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Features

- Agent implementations for various tasks
- Chain compositions for complex workflows
- Memory management for conversation history
- Custom prompt templates
- Integration with various LLM providers
- Vector store implementations
- Document loaders and processors

## Setup

1. Clone the repository:
```bash
git clone https://github.com/VikasRaika/langchain-portfolio.git
cd langchain-portfolio
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
```

## Development

- Format code: `black src tests`
- Sort imports: `isort src tests`
- Lint code: `flake8 src tests`
- Type checking: `mypy src tests`
- Run tests: `pytest tests/`

## License

MIT License 