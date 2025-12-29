# Agentic Memory and Agents - Learning Repository

A comprehensive collection of Jupyter notebooks for learning LangChain, agentic AI systems, memory management, and SQL agents with practical examples.

## 📋 Prerequisites

- **Python**: 3.13 or higher
- **uv**: Fast Python package installer ([Installation Guide](https://github.com/astral-sh/uv))

## 🚀 Installation

### 1. Install uv (if not already installed)

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone the Repository

```bash
git clone <repository-url>
cd agentic-memory-and-agents
```

### 3. Install Dependencies

Use `uv sync` to create a virtual environment and install all dependencies from `pyproject.toml`:

```bash
uv sync
```

This command will:
- Create a virtual environment (`.venv`)
- Install all dependencies specified in `pyproject.toml`
- Lock the dependencies in `uv.lock`

### 4. Activate the Virtual Environment

```bash
# On macOS and Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

## 🔑 Environment Configuration

### Create `.env` File

Create a `.env` file in the project root directory:

```bash
touch .env
```

### Add API Keys

Open the `.env` file and add your API keys:

```env
# OpenAI API Key (required for most notebooks)
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Other API keys if needed
# ANTHROPIC_API_KEY=your_anthropic_key_here
# GOOGLE_API_KEY=your_google_key_here
```

**Important**: 
- Never commit your `.env` file to version control
- Get your OpenAI API key from: https://platform.openai.com/api-keys
- Replace `your_openai_api_key_here` with your actual API key

## 📚 Project Structure

### LangChain Agent Tutorials
- `langchain_agent_basic.ipynb` - Introduction to LangChain agents
- `langchain_agent_advanced.ipynb` - Advanced agent patterns and techniques

### Memory Management
- `short_term_memory.ipynb` - Short-term memory implementation
- `long-term-memory-tutorial.ipynb` - Long-term memory with persistence
- `messages_append.ipynb` - Message handling and appending

### SQL Agents & Tutorials
- `sql_agent_tutorial.ipynb` - Complete SQL agent tutorial
- `sql_agent_human_in_the_loop.ipynb` - Human-in-the-loop SQL agents
- `sql_agent_human_in_the_loop_v2.ipynb` - Enhanced version with improvements
- `sql_tutorial.ipynb` - Basic SQL tutorial
- `sql_tutorial_beginners.ipynb` - SQL for beginners
- `sql_joins_tutorial.ipynb` - SQL joins explained

### Chatbot Development
- `chatbot_basics_tutorial.ipynb` - Chatbot fundamentals

### Data & Utilities
- `sql_banking_dummy_data_creator.ipynb` - Generate dummy banking data
- `banking_customers_indian.db` - Sample SQLite database
- `students.db` - Sample student database

## 🎯 Usage

### Running Notebooks

1. Ensure your virtual environment is activated
2. Start Jupyter:

```bash
jupyter notebook
```

3. Open any notebook and run the cells

### Suggested Learning Path

1. **Start with basics**: `chatbot_basics_tutorial.ipynb`
2. **Learn LangChain agents**: `langchain_agent_basic.ipynb` → `langchain_agent_advanced.ipynb`
3. **Explore memory**: `short_term_memory.ipynb` → `long-term-memory-tutorial.ipynb`
4. **Master SQL agents**: `sql_tutorial_beginners.ipynb` → `sql_agent_tutorial.ipynb`
5. **Advanced topics**: Human-in-the-loop agents

## 🛠️ Dependencies

Key dependencies (managed via `pyproject.toml`):
- `langchain` - LangChain framework
- `langchain-openai` - OpenAI integration
- `langchain-community` - Community integrations
- `mem0ai` - Memory management
- `pandas` - Data manipulation
- `python-dotenv` - Environment variable management

## 📝 Notes

- All notebooks use environment variables from `.env` for API keys
- Make sure to have sufficient API credits for running examples
- Some notebooks require active database files (included in repository)

## 🤝 Contributing

Feel free to add new tutorials or improve existing ones!

## 📄 License

This is a learning repository for educational purposes.