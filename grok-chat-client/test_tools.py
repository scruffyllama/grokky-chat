import pytest
from tools import tool_registry, get_tools

def test_tool_registry():
    assert "add_numbers" in tool_registry
    assert "mock_search" in tool_registry

def test_add_numbers():
    result = tool_registry["add_numbers"](2, 3)
    assert result == 5

def test_mock_search():
    result = tool_registry["mock_search"]("test query")
    assert "test query" in result

def test_get_tools():
    tools = get_tools()
    assert len(tools) == 2
    assert tools[0]["function"]["name"] == "add_numbers"
    assert tools[1]["function"]["name"] == "mock_search"