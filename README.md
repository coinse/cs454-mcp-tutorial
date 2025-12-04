# CS454 MCP Tutorial (251204)

* Slides link: [TBD]

### PlayWright MCP Agent

- Run a simple MCP server w/ the given client without modification
    - `python web_tester_chat.py`
    
- after connecting Playwright MCP server using NPX command:
    - `python web_tester_chat_ref.py`
    
- Hardcoding tool calling for initiating testing run for the target website:
    - `python web_tester_actor_ref.py [https://sciencedirect.com](https://sciencedirect.com/)`

### Pytest Agent

- `python pytest_mcp_client.py pytest_mcp_server.py "please list files”` (For checking `list_files` MCP function call)
    - Print execution trace as a JSON file
