from fastmcp import FastMCP, Request, Response

app = FastMCP()

@app.post('/run_python')
async def run_python(request: Request) -> Response:
    """Handle Python code execution requests (currently mocked)"""
    # Mock response for now
    return Response({
        'status': 'success',
        'output': 'Hello from Python execution!',
        'result': 42
    })

if __name__ == '__main__':
    app.run()
