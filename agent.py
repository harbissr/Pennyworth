from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

llm = ChatOpenAI(model="deepseek-chat", temperature=0, openai_api_key=OPENAI_API_KEY)

output = llm.invoke("What is the AI equivalent of 'Hello World'?")
print(output)
