"""
Operations Analysis MCP Server

Acts as the interface between the AI Core and the Operations MCP.
"""

from tool import execute


def handle_request(query: str):
    """
    Receives a request from the AI Core
    and forwards it to the Operations Tool.
    """
    return execute(query)


if __name__ == "__main__":
    response = handle_request("Can we expand production?")
    print(response)