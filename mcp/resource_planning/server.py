"""
Resource Planning MCP Server
"""

from tool import execute


def handle_request(query: str):
    return execute(query)


if __name__ == "__main__":
    print(handle_request("Can we hire 10 more engineers?"))