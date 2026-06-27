from langchain_openai import OpenAI

#access openai api key from .env, python-dotenv is already in requiremts.txt

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")

print(result)