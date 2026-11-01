# Method 1
from langchain_core.tools import tool
@tool
def multiply(a:int,b:int) -> int:
    "Multiply two numbers"
    c = a * b
    return c
print(multiply.invoke({"a":5,"b":3}))
print(multiply.name)
print(multiply.description)
print(multiply.args)
# Method 2 (Structured tool and pydentic)
from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field
class MultiplyInput(BaseModel):
    a : int = Field(required=True,description='The first number to add')
    b : int = Field(reqired=True,description='The second number to add')
def multiply_func(a:int,b:int) -> int:
    return a * b
multiply_tool = StructuredTool(
    func=multiply_func,
    name='multiply',
    description='Multiply two numbers',
    args_schema=MultiplyInput
)
result = multiply_tool.invoke({'a':5,'b':3})
print(result)
print(multiply_tool.name)
print(multiply.description)
print(multiply.args)

# Method 3 : Custom tools using base tools
from langchain_core.tools import BaseTool
from typing import Type
# Arg schema using pydantic
class MultiplyInput(BaseModel):
    a : int = Field(required=True,description='The first number to add')
    b : int = Field(reqired=True,description='The second number to add')
class MultiplyTool(BaseTool):
    name : str = 'multiply'
    description : str = 'Multiply two numbers'
    args_schema : Type[BaseModel] = MultiplyInput
    def _run(self,a:int,b:int) -> int:
        return a * b
multiply_tool = MultiplyTool()
result = multiply_tool.invoke({'a':5,'b':3})
print(result)
print(multiply_tool.name)
print(multiply.description)
print(multiply.args)
