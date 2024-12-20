# MCP Server

A Python implementation of the Model Context Protocol (MCP) server for handling run_python requests.

## Overview

This server provides a simple implementation of the MCP specification for executing Python code. It currently supports the basic run_python endpoint with mock responses.

## Features

- FastAPI-based MCP server
- Support for run_python requests
- Mock response implementation (real execution coming soon)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python main.py
   ```

## API Endpoints

### POST /run_python

Execute Python code and return results.

Request format:
```json
{
    "code": "print('Hello World')",
    "context": {}
}
```

Response format:
```json
{
    "result": "success",
    "output": "Hello World\n",
    "error": null
}
```

## Development

Currently implementing core MCP functionality with a focus on:
- Basic request handling
- Mock responses
- Protocol compliance