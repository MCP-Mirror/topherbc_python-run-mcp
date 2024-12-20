from model_context_protocol import MCPServer, RunPythonRequest, RunPythonResponse

def handle_run_python(request: RunPythonRequest) -> RunPythonResponse:
    # Mock response as per requirements
    return RunPythonResponse(
        result="mock_result",
        stdout="mock output",
        stderr=""
    )

def main():
    server = MCPServer(
        name="mcp-server",
        version="0.1.0"
    )
    
    server.register_handler("run_python", handle_run_python)
    server.start()

if __name__ == "__main__":
    main()