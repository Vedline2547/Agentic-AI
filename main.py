# Built-In tools
# DUckDuckGoSearchRun
from langchain_community.tools import DuckDuckGoSearchRun,ShellTool, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke("Top news in Kenya today")
# print(results)
print(search_tool.name)
print(search_tool.description)
print(search_tool.args)
shell_tool = ShellTool()
results = shell_tool.invoke('rmdir random')
print(results)
