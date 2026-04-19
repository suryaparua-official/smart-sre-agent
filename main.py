import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.agents import Tool
from tools import read_app_logs, create_config_fix

# Disable LangSmith tracing to avoid warnings
os.environ["LANGSMITH_TRACING"] = "false"

# Load environment variables from .env file
load_dotenv()

def main():
    # 1. Initialize LLM (Using Groq Llama 3.3)
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile", 
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0
    )

    # 2. Define Toolset
    tools = [
        Tool(
            name="LogAnalyzer",
            func=read_app_logs,
            description="Useful for reading application logs to identify errors. Input: filename string."
        ),
        Tool(
            name="ConfigFixer",
            func=create_config_fix,
            description="Useful for creating or repairing config.yaml files. Input: raw string content for the file."
        )
    ]

    # 3. Pull ReAct Prompt Template
    try:
        prompt = hub.pull("hwchase17/react")
    except Exception:
        print("Error: Could not pull prompt from LangChain Hub. Check internet connection.")
        return

    # 4. Construct the Agent
    agent = create_react_agent(llm, tools, prompt)

    # 5. Initialize Agent Executor
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True, 
        handle_parsing_errors=True,
        max_iterations=5
    )

    print("--- Smart SRE Agent Initialized ---")
    
    # 6. Execution Goal
    task = (
        "1. Analyze the logs in app.log to find the root cause of the error. "
        "2. Once identified, use ConfigFixer to create a config.yaml file "
        "with correct database settings: host='localhost', port=5432, timeout=30."
    )

    try:
        agent_executor.invoke({"input": task})
    except Exception as e:
        print(f"\nAgent Execution Error: {e}")

if __name__ == "__main__":
    main()
