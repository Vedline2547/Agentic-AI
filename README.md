# LangChain Tools: Built-in Tools, Custom Tools & Tool Calling

## Overview

This project explores tool integration and development in **LangChain**, focusing on how Large Language Models (LLMs) can interact with external systems, execute specific tasks, and extend their capabilities through tools.

The project covers four main areas:
- Working with LangChain's built-in tools.
- Developing custom tools using different approaches.
- Organizing related tools into custom toolkits.
- Integrating custom tools with LLMs through tool binding and execution.

## 1. LangChain Built-in Tools

Explored existing tools available through `langchain_community`.

### Tools Explored
- **DuckDuckGoSearchRun:** Performs web searches and retrieves information based on user queries.
- **ShellTool:** Executes shell commands through LangChain.
- **WikipediaQueryRun:** Supports Wikipedia-based information retrieval.
- **WikipediaAPIWrapper:** Provides API integration for Wikipedia.

### Implementation
- Initializing built-in LangChain tools.
- Executing web searches using DuckDuckGo.
- Running shell commands through ShellTool.
- Inspecting tool names, descriptions, and argument schemas.
- Executing tools using `.invoke()`.

## 2. LangChain Custom Tools

Explored three approaches to developing custom tools using mathematical operations as examples.

### Method 1: Using the `@tool` Decorator

Created custom tools using LangChain's `@tool` decorator.

Key concepts:
- Converting Python functions into LangChain tools.
- Defining tool names and descriptions.
- Working with structured inputs.
- Invoking tools using `.invoke()`.
- Accessing tool metadata and argument schemas.

### Method 2: Using `StructuredTool` and Pydantic

Developed structured tools using `StructuredTool` and Pydantic.

Key concepts:
- Defining input schemas with Pydantic `BaseModel`.
- Using `Field` to describe tool arguments.
- Converting Python functions into structured tools.
- Validating tool inputs.

### Method 3: Using `BaseTool`

Developed custom tool classes by inheriting from LangChain's `BaseTool`.

Key concepts:
- Creating reusable custom tool classes.
- Defining tool names and descriptions.
- Specifying argument schemas.
- Implementing execution logic using `_run()`.

## 3. Creating Custom Toolkits

Explored how to organize multiple related LangChain tools into a single toolkit using Python classes.

Implemented a `MathToolKit` class containing mathematical tools such as `add` and `multiply`.

Example:

```python
class MathToolKit:
    def get_tools(self):
        return [add, multiply]

toolkit = MathToolKit()

for tool in toolkit.get_tools():
    print(tool.name)
```

Key concepts:
- Grouping related tools into a single toolkit.
- Creating reusable toolkit classes.
- Retrieving tools through a `get_tools()` method.
- Iterating through tool collections.
- Accessing individual tool properties, including names and descriptions.

## 4. LLM Tool Binding and Execution

Integrated custom LangChain tools with a locally running LLM using **Ollama and Qwen 2.5 (3B)**.

Used `ChatOllama` to initialize the language model and `bind_tools()` to make custom tools available to the LLM.

### Implementation

Created a multiplication tool and connected it to the Qwen 2.5 model.

```python
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

llm_with_tools = llm.bind_tools([multiply])

result = llm_with_tools.invoke(
    "Can you multiply 3 with 10"
)

print(result.tool_calls)
```

### Tool Execution Workflow

Implemented manual tool execution using LangChain's message objects.

The workflow involves:

1. Sending a natural language query to the LLM.
2. Receiving the LLM's tool call request.
3. Extracting the tool name and arguments from `result.tool_calls`.
4. Executing the requested Python function using `.invoke()`.
5. Appending the AI response to the conversation history.
6. Returning the tool execution result using `ToolMessage`.
7. Sending the updated conversation back to the LLM to generate a final response.

### Message Types Explored

- **HumanMessage:** Represents the user's input.
- **AIMessage:** Contains the LLM response and any requested tool calls.
- **ToolMessage:** Returns the executed tool's result to the LLM.

### Key Concepts
- Binding custom tools to an LLM using `bind_tools()`.
- Understanding how LLMs generate tool calls.
- Extracting structured tool arguments.
- Executing tools based on LLM-generated requests.
- Managing conversation history using message objects.
- Connecting tool execution results back to the LLM.

## Technologies & Libraries

- Python
- LangChain
- LangChain Core
- LangChain Community
- LangChain Ollama
- Ollama
- Qwen 2.5 (3B)
- Pydantic
- DuckDuckGo Search
- Wikipedia API

## Installation

Clone the repository:

```bash
git clone https://github.com/Vedline2547/Agentic-AI.git
```

Navigate to the project directory:

```bash
cd LangChain-Tools
```

Install the dependencies:

```bash
pip install langchain langchain-core langchain-community langchain-ollama pydantic ddgs wikipedia
```

Install Ollama and pull the Qwen model:

```bash
ollama pull qwen2.5:3b
```

## Key Learning Outcomes

- Understanding LangChain's tool ecosystem.
- Working with built-in tools for search and shell execution.
- Creating custom tools using Python functions.
- Defining structured tool schemas with Pydantic.
- Developing reusable custom tool classes using `BaseTool`.
- Organizing related tools into custom toolkits.
- Binding tools to LLMs using `bind_tools()`.
- Understanding LLM-generated tool calls.
- Executing tools and managing conversation history.
- Using LangChain message objects to manage tool interactions.

## Future Learning

- Automating tool execution using tool-calling loops.
- Handling multiple tool calls.
- Integrating multiple tools and toolkits with LLMs.
- Building AI agents capable of selecting and executing tools.
- Exploring LangGraph for stateful agent workflows.
- Developing more advanced agentic applications.

## Author

**Vedline Ochieng**

Civil Engineering Student | ML Enthusiast | Python Developer | Future AI Engineer

[GitHub Profile](https://github.com/Vedline2547)

