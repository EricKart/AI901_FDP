"""
Lab 3 — Create & run a single agent with the Foundry Agent Service.
Exam objective: create/test a single-agent solution; build a client for an agent.

NOTE: The Agent SDK surface evolves. This script shows the STANDARD SHAPE and
prints each lifecycle step. If a method name differs in your installed SDK
version, check the docs — the concepts (agent -> thread -> message -> run -> read)
are what the exam tests. Requires az login OR a key-based credential.

Run:  az login   then   python agent.py
"""
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()

project = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
MODEL = os.getenv("CHAT_DEPLOYMENT", "gpt-4o-mini")

# 1) Create an agent = model + instructions (+ optional tools)
print("1) creating agent ...")
agent = project.agents.create_agent(
    model=MODEL,
    name="ai901-study-buddy",
    instructions="You are an AI-901 tutor. Answer in one concise sentence.",
)

# 2) A thread holds the conversation
print("2) creating thread ...")
thread = project.agents.create_thread()

# 3) Add a user message
print("3) adding user message ...")
project.agents.create_message(
    thread_id=thread.id, role="user",
    content="In one line, what is grounding (RAG)?",
)

# 4) Run the agent over the thread (it may call tools, then answer)
print("4) running ...")
project.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)

# 5) Read the messages
print("5) messages:")
for m in project.agents.list_messages(thread_id=thread.id):
    print(f"   {m.role}: {m.content}")

# cleanup (optional)
project.agents.delete_agent(agent.id)
