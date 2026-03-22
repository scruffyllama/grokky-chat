from typing import Dict, Any, List
import json

tool_registry: Dict[str, Any] = {}

def register_tool(name: str, function):
    tool_registry[name] = function

# Example tool: add two numbers
def add_numbers(a: int, b: int) -> int:
    return a + b

register_tool("add_numbers", add_numbers)

# Another example tool: simple search (mock)
def mock_search(query: str) -> str:
    # Mock search result
    return f"Mock search results for '{query}': Found some info."

register_tool("mock_search", mock_search)

def get_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "add_numbers",
                "description": "Add two numbers together.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "integer", "description": "First number"},
                        "b": {"type": "integer", "description": "Second number"}
                    },
                    "required": ["a", "b"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "mock_search",
                "description": "Perform a mock search on the web.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "The search query"}
                    },
                    "required": ["query"]
                }
            }
        }
    ]