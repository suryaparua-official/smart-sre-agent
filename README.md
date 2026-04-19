# Smart-SRE-Agent: Autonomous Log Analyzer & Fixer

**Smart-SRE-Agent** is a production-ready Agentic AI tool designed for Site Reliability Engineers (SRE). It doesn't just notify you about errors; it actively investigates logs, identifies the root cause using LLMs, and executes tools to fix the infrastructure.

---

## Key Features

- **Autonomous Troubleshooting**: Uses a ReAct (Reasoning and Acting) loop to think and act.
- **Log Analysis**: Dynamically reads local application logs to detect failures.
- **Auto-Remediation**: Can automatically generate `config.yaml` or other fixes based on the error.
- **Blazing Fast**: Powered by **Groq (Llama 3.3 70B)** for low-latency reasoning.

---

## Technical Stack

- **AI Orchestration**: [LangChain](https://langchain.com)
- **Large Language Model**: [Groq](https://groq.com) (Llama-3.3-70b-versatile)
- **Programming Language**: Python 3.11+
- **Containerization**: Docker (Multi-stage build for 60% smaller image size)
- **Infrastructure**: YAML-based configuration management

---

## Project Structure

```text
smart-sre-agent/
├── main.py          # The Brain (Agent Logic)
├── tools.py         # The Hands (File & System Operations)
├── app.log          # Simulated Application Logs
├── config.yaml      # Generated Fixes (Output)
├── Dockerfile       # Optimized Production Build
├── .env             # API Credentials (Private) - DO NOT UPLOAD TO GITHUB
└── requirements.txt # Python Dependencies
```

## Getting Started

1. Prerequisites
   - Python 3.11 or higher installed.
   - A Groq API Key (Get it from Groq Console).
2. Installation
   Clone the repository and install dependencies:

   ```bash
   git clone https://github.com
   cd smart-sre-agent
   python -m venv venv
   source venv/bin/activate # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

   Use code with caution.

3. Environment Configuration
   Create a .env file in the root directory:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```
   Use code with caution.
4. Running the Agent
   ```bash
   python main.py
   ```
   Use code with caution.
   Docker Production Deployment
   To build a highly compressed, production-ready Docker image:
   bash

# Build the image

```
docker build -t smart-sre-agent:latest .
```

# Run the container with your secrets

```
docker run --env-file .env smart-sre-agent:latest
```

Use code with caution.

## Security & Guardrails

- Read/Write Restrictions: The agent only has access to specific files defined in tools.py.
- Environment Isolation: Uses Docker to isolate the execution environment from the host system.
- Secret Management: API keys are never hardcoded and are managed via .env.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
