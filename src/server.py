from fastapi import FastAPI, HTTPException
from mcp import ServerSession
from mcp.types import RunPythonRequest, RunPythonResponse

app = FastAPI()
server = ServerSession()

@app.post("/run_python")
async def run_python(request: RunPythonRequest) -> RunPythonResponse:
    try:
        # Mock response for now
        return RunPythonResponse(
            status="success",
            result={
                "output": "Mock output",
                "error": None
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
