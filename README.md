# MCP Python Execution Server

A Python implementation of a Model Context Protocol server that supports Python code execution requests.

## Features

- Handles `run_python` requests
- Returns mock responses (to be implemented with actual Python execution)
- Built using the MCP SDK

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python src/server.py
```

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
4. Test with an MCP client
