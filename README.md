# MCP Python Execution Server

A Python implementation of a Model Context Protocol server that supports Python code execution requests.

## Features

- Handles `run_python` requests
- Returns mock responses (to be implemented with actual Python execution)
- Built using the MCP Python SDK

## Installation

1. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

This will install the MCP Python SDK directly from GitHub along with other dependencies.

## Usage

```bash
python src/server.py
```

## Testing with MCP Inspector

1. Start the server:
```bash
python src/server.py
```

2. In a new terminal, run the inspector:
```bash
npx @modelcontextprotocol/inspector
```

3. Use provided test configurations:
```bash
npx @modelcontextprotocol/inspector --config tests/basic_test.json
```

See `docs/inspector/README.md` for detailed testing instructions.

## API

### run_python

Executes Python code and returns the result.

Request format:
```json
{
    "code": "print('Hello, World!')"
}
```

Response format:
```json
{
    "status": "success",
    "output": "Hello, World!",
    "result": null
}
```

## Development

1. Clone the repository
2. Install dependencies
3. Run the server
4. Test with MCP inspector

See the `tests/` directory for example test cases and configurations.
