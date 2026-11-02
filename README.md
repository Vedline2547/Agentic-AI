# LangChain Tools: Built-in, Custom Tools & Toolkits

## Overview

This project explores tool integration and development in **LangChain**, focusing on how Large Language Models (LLMs) can interact with external systems and execute specific tasks through tools.

It covers three main areas: working with LangChain's built-in tools, developing custom tools using different approaches, and organizing related tools into custom toolkits.

## 1. LangChain Built-in Tools

Explored existing tools available through `langchain_community`.

### Tools Explored
- **DuckDuckGoSearchRun:** Performs web searches and retrieves information based on user queries.
- **ShellTool:** Executes shell commands through LangChain.
- **WikipediaQueryRun:** Supports Wikipedia-based information retrieval.
- **WikipediaAPIWrapper:** Provides the API integration for Wikipedia.

### Implementation
- Initializing built-in LangChain tools.
- Executing web searches using DuckDuckGo.
- Running shell commands through ShellTool.
- Inspecting tool names, descriptions, and argument schemas.
- Executing tools using `.invoke()`.

## 2. LangChain Custom Tools

Explored three approaches to developing custom tools, using mathematical operations as examples.

### Method 1: Using the `@tool` Decorator

Created custom tools using LangChain's `@tool` decorator.

Key concepts:
- Converting Python functions into LangChain tools.
- Defining tool names and descriptions.
- Working with structured inputs.
- Invoking tools and accessing tool metadata.

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

Implemented a `MathToolKit` class containing custom mathematical tools such as `add` and `multiply`.

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

## Technologies & Libraries

- Python
- LangChain
- LangChain Community
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

Install dependencies:

```bash
pip install langchain langchain-community pydantic ddgs wikipedia
```

## Key Learning Outcomes

- Understanding LangChain's tool ecosystem.
- Working with built-in tools for search and shell execution.
- Creating custom tools using Python functions.
- Defining structured tool schemas with Pydantic.
- Understanding inheritance and custom tool development using `BaseTool`.
- Organizing related tools into reusable toolkits.
- Understanding how tools extend the capabilities of LLM applications and AI agents.

## Future Learning

- Integrating custom tools and toolkits with LLMs.
- Exploring tool calling and function calling.
- Building AI agents capable of selecting and executing tools.
- Connecting multiple tools into agentic workflows.
- Developing more advanced custom toolkits.

## Author

**Vedline Ochieng**

Civil Engineering Student | ML Enthusiast | Python Developer | Future AI Engineer

[GitHub Profile](https://github.com/Vedline2547)
