from mcp.server import Server, RPCServer, RequestHandler
import sys
import logging
import asyncio

# Set up logging to stderr since stdout is used for stdio server
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

class PythonRequestHandler(RequestHandler):
    async def run_python(self, request):
        logger.info("Received run_python request")
        # Mock response for now
        return {
            "result": "mock_result",
            "stdout": "mock output",
            "stderr": ""
        }

async def main():
    try:
        logger.info("Starting server...")
        server = Server("python-executor")
        handler = PythonRequestHandler()
        server.add_handler(handler)

        rpc_server = RPCServer(
            server,
            read_stream=sys.stdin.buffer,
            write_stream=sys.stdout.buffer
        )
        
        logger.info("Server created, waiting for connections...")
        await rpc_server.serve()
    except Exception as e:
        logger.error(f"Error starting server: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())