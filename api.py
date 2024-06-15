"""
Lambda Function Request Handler

This Lambda function serves as a request handler for handling HTTP GET and POST requests.
It verifies an API key from headers, validates the request method, and delegates
operations to appropriate functions based on the request path for GET and POST methods.

Functions:
- `manage_get_request(path)`: Handles GET requests for specific paths ("/clients", "/users").
- `manage_post_request(path, body)`: Handles POST requests for specific paths ("/clients", "/users").

Dependencies:
- Requires environment variable `API_KEY` to authenticate API requests.

Logging:
- Logs events and errors at the INFO level using the default logger configuration.
"""

import json
import logging
import os
from handlers import manage_get_request, manage_post_request

# Configuring the logger to log information at the INFO level
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Getting the API key from environment variables
API_KEY = os.environ['API_KEY']

def lambda_handler(event, context):
    # Extracting headers from the incoming event
    headers = event.get("headers")
    # Getting the API key from the headers
    api_key = headers.get("x-api-key")
    
    # Verifying if the provided API key matches the expected API key
    if api_key != API_KEY:
        # If it doesn't match, return a 401 Unauthorized error
        return {"statusCode": 401, "body": json.dumps('Unauthorized')}
    
    # Extracting HTTP request context information
    http = event.get("requestContext").get("http")
    method = http.get("method")
    path = http.get("path")
    
    # Checking if the HTTP method is not GET or POST
    if method not in ["GET", "POST"]:
        # If it's not, return a 405 Method Not Allowed error
        return {'statusCode': 405, "body": json.dumps("Method Not Allowed")}
    
    # Handling GET requests
    if method == "GET":
        # Use manage_get_request function to handle the request
        response_body = manage_get_request(path)
        return {'statusCode': 200, "body": json.dumps(response_body)}
        
    # Handling POST requests
    if method == "POST":
        # Parse the body of the request
        request_body = json.loads(event.get("body"))
        # Use manage_post_request function to handle the request
        response_body = manage_post_request(path, request_body)
        return {'statusCode': 201, "body": json.dumps(response_body)}
        
    # If something unexpected happens, return a 500 Internal Server Error
    return {
        'statusCode': 500,
        'body': json.dumps('Error')
    }