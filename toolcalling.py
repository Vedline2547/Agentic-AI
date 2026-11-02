# Import necessary libraries
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
# Create a tool
@tool
def multiply(a:int,b:int) -> int:
    """Given 2 numbers a and b, this tool returns their product"""
    c = a * b
    return c
print(multiply.invoke({"a":5,"b":3}))
print(multiply.name)
print(multiply.description)
print(multiply.args)
# Tool binding
llm = ChatOllama(model='qwen2.5:3b',temperature=0)
# print(llm.invoke("Hey"))
llm_with_tools = llm.bind_tools([multiply])
# Tool execution
result = llm_with_tools.invoke('Can you multiply 3 with 10')
print(result.tool_calls[0])
print(result.tool_calls['args'])
query = HumanMessage("Can you multiply 3 with 10")
messages = [query]
# # print(messages)
# messages.append(result)
tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)
print(messages)
print(llm_with_tools.invoke(messages).content)