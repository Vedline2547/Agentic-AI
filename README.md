# LangChain Tools: Built-in & Custom Tools

## Overview

This project explores tool integration and development in LangChain, focusing on how Large Language Models (LLMs) can use tools to interact with external systems and execute specific tasks.

The project covers two main areas: using LangChain's built-in tools and developing custom tools using different approaches.

## 1. LangChain Built-in Tools

Explored existing tools available in LangChain through `langchain_community`.

### Tools Explored

- **DuckDuckGoSearchRun:** Performs web searches and retrieves information based on user queries.
- **ShellTool:** Executes shell commands through LangChain.
- **WikipediaQueryRun:** Imported for Wikipedia-based information retrieval.
- **WikipediaAPIWrapper:** Provides the API wrapper used for Wikipedia integration.

### Implementation

The project demonstrates:
- Initializing built-in LangChain tools.
- Executing searches using DuckDuckGo.
- Running shell commands through ShellTool.
- Inspecting tool names, descriptions, and argument schemas.
- Invoking tools using `.invoke()`.

## 2. LangChain Custom Tools

Explored three approaches to building custom tools in LangChain using a multiplication function as an example.

### Method 1: Using the `@tool` Decorator

Created a custom multiplication tool using LangChain's `@tool` decorator.

Key concepts:
- Converting Python functions into LangChain tools.
- Defining tool names and descriptions.
- Invoking tools with structured inputs.
- Accessing tool metadata and arguments.

### Method 2: Using `StructuredTool` and Pydantic

Created a structured tool using `StructuredTool` and Pydantic.

Key concepts:
- Defining input schemas with Pydantic `BaseModel`.
- Using `Field` to describe tool arguments.
- Converting existing Python functions into structured tools.
- Validating tool inputs.

### Method 3: Using `BaseTool`

Developed a custom tool class by inheriting from LangChain's `BaseTool`.

Key concepts:
- Creating reusable custom tool classes.
- Defining tool names and descriptions.
- Specifying argument schemas.
- Implementing execution logic using `_run()`.

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

Navigate into the project directory:

```bash
cd LangChain-Tools
```

Install the dependencies:

```bash
pip install langchain langchain-community pydantic ddgs wikipedia
```

## Key Learning Outcomes

- Understanding LangChain's tool ecosystem.
- Working with built-in tools for search and shell execution.
- Creating custom tools using Python functions.
- Defining structured tool schemas with Pydantic.
- Understanding inheritance and custom tool development using `BaseTool`.
- Exploring how tools extend the capabilities of LLM applications and AI agents.

## Future Learning

- Integrating custom tools with LLMs.
- Exploring tool calling and function calling.
- Building AI agents capable of selecting and executing tools.
- Connecting multiple tools into agentic workflows.

## Author

**Vedline Ochieng**

Civil Engineering Student | ML Enthusiast | Python Developer | Future AI Engineer

[GitHub Profile](https://github.com/Vedline2547)
