# Personal CFO - AI-Powered Financial Management

> Your AI financial command center. Stop tracking expenses—start optimizing them.

[![Python 3.12+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange.svg)](https://github.com/joaomdmoura/crewAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Overview

Personal CFO is an AI-powered financial management platform that goes beyond passive expense tracking. Built on a multi-agent architecture using CrewAI, it features 8 specialized AI agents that actively optimize, negotiate, and execute financial decisions on your behalf.

**The Problem:** The average US household leaves $5,000-$15,000 on the table annually through suboptimal financial decisions, yet only 30% can afford a human financial advisor.

**The Solution:** An AI CFO that automates financial optimization for everyone.

## 🤖 The Eight AI Agents

| Agent | Purpose | Key Actions |
|-------|---------|-------------|
| **Budget Optimizer** | Analyzes spending patterns and optimizes allocation | Identifies waste, suggests cuts, reallocates funds |
| **Bill Negotiator** | Reduces recurring expenses | Monitors bills, finds better deals, negotiates or switches |
| **Tax Strategist** | Maximizes tax efficiency year-round | Tax-loss harvesting, Roth conversions, quarterly estimates |
| **Investment Advisor** | Optimizes portfolio allocation | Goal-based allocation, rebalancing, fee reduction |
| **Debt Payoff Strategist** | Accelerates debt elimination | Calculates optimal strategies, monitors refinancing |
| **Savings Goal Coordinator** | Manages multiple savings goals | Automates contributions, adapts to income changes |
| **Credit Score Guardian** | Monitors and improves credit health | Error detection, actionable suggestions, dispute filing |
| **Financial Educator** | Provides personalized financial education | Contextual lessons, transparent explanations, Q&A |

## 🏗️ Project Structure

```
CFO_APP/
├── Agents/          # Individual AI agent definitions
├── Tasks/           # Agent task configurations
├── Tools/           # Custom tools for agents (APIs, utilities)
├── .venv/           # Virtual environment
├── requirements.txt # Python dependencies
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- pip package manager
- API keys for financial data providers (Plaid, Finicity, etc.)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/prathamchopra001/CFO_APP
cd CFO_APP
```

2. **Create and activate virtual environment**
```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install uv
```

```bash
uv pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Create .env file in root directory
cp .env.example .env

# Add your API keys:
# OPENAI_API_KEY=your_openai_key
# ANTROPIC_API=your_antropic_api
```

5. **Run the application**
```bash
python app.py
```

## 📦 Dependencies

The project uses the following core technologies:

- **CrewAI**: Multi-agent orchestration framework
- **CrewAI Tools**: Pre-built tools for agent interactions
- **LiteLLM**: Unified interface for multiple LLM providers
- **python-dotenv**: Environment variable management

See `requirements.txt` for complete dependency list.

## 🎯 What Makes This Different

| Traditional Finance Apps | Personal CFO |
|--------------------------|--------------|
| Shows you spent $200 on subscriptions | Cancels 3 unused subscriptions, saves $47/month |
| Tells you cable is expensive | Negotiates bill down or switches to better plan |
| Displays investment allocation | Rebalances portfolio and harvests tax losses |
| Tracks debt balances | Executes optimal payoff strategy automatically |

## 🔧 Development

### Project Architecture

Built on **CrewAI**, each agent operates autonomously while collaborating through a central orchestrator:

- **Agent Communication**: Shared memory allows agents to coordinate (e.g., Investment Advisor and Tax Strategist sync on tax-loss harvesting)
- **Priority System**: Critical tasks (debt payoff) can override lower-priority actions
- **Conflict Resolution**: Built-in logic prevents conflicting recommendations

### Adding New Agents

1. Define agent in `Agents/` directory
2. Create associated tasks in `Tasks/`
3. Add custom tools in `Tools/` if needed
4. Register agent in main orchestrator

### Adding New Tools

Create custom tools in `Tools/` directory following CrewAI tool structure:

```python
from crewai_tools import BaseTool

class CustomTool(BaseTool):
    name: str = "Tool Name"
    description: str = "What this tool does"
    
    def _run(self, argument: str) -> str:
        # Tool implementation
        return result
```


## 🔐 Security & Compliance

- **Encryption**: Bank-grade AES-256 encryption for all data
- **Authentication**: OAuth 2.0 (no credential storage)
- **Compliance**: SOC 2 Type II, GDPR, CCPA ready
- **Privacy**: User data never shared without explicit consent
- **Auditing**: Regular third-party security assessments

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write or update tests
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add docstrings to all functions and classes
- Write unit tests for new features
- Update documentation as needed
- Keep dependencies minimal and justified

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [CrewAI](https://github.com/joaomdmoura/crewAI) for multi-agent orchestration
- Financial data via Plaid, Finicity, and Yodlee APIs
- Credit monitoring through Credit Karma API
- Inspired by the belief that everyone deserves financial optimization, not just the 1%


---

**Built with ❤️ for the 99% who can't afford a human CFO**

*Currently in active development. Star ⭐ this repo to follow our progress!*
