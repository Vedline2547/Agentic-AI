from langchain_core.tools import tool
@tool
def multiply(a:int,b:int) -> int:
    "Multiply two numbers"
    c = a * b
    return c

@tool
def add(a : int,b : int) -> int:
    "Add two numbers"
    return a + b

# Creating a toolkit
class MathToolKit:
    def get_tools(self):
        return [add,multiply]
toolkit = MathToolKit()
for tool in toolkit.get_tools():
    print(tool.name)