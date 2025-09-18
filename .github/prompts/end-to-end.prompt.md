---
agent: agent
---
Your task is to run a provided scenario of end-to-end test against a running instance of this project. Use locally running MCP tools to interact with the system. Before executing REST API calls, list all available endpoints to confirm the target endpoint exists.

# Steps

1. Start the uvicorn server using the `start_uvicorn` tool.
2. Verify that the server is running using the `is_uvicorn_running` tool.
3. Execute the scenario provided below.
4. Stop the uvicorn server using the `stop_uvicorn` tool.
