[![AWS](https://img.shields.io/badge/AWS-Amazon%20Web%20Services-orange)](https://aws.amazon.com/)

# AWS Lambda Function for Handling GET and POST Requests

This repository contains an AWS Lambda function designed to handle HTTP GET and POST requests. The function is configured to authenticate requests using an API key and route them based on the HTTP method and request path.

## Features

  - GET Requests: Handles requests to retrieve data for clients and users.
  - POST Requests: Manages requests to insert new client and user data.
  - Authentication: Verifies API key from request headers to ensure secure access.
  - Logging: Logs events and errors using Python's built-in logging module.

## Project Structure

- lambda_function.py: Contains the main Lambda function code.
 - utils.py: Provides utility functions to handle specific data operations (get_clients, get_user, insert_client, insert_user).

## Setup

To deploy this Lambda function, follow these steps:

**Prerequisites:** Ensure you have an AWS account and AWS CLI configured.

**Environment Setup:** Set up a virtual environment and install dependencies.

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**Configuration:** Set your API_KEY environment variable in AWS Lambda console or .env file.

**Deployment:** Zip the files and upload to AWS Lambda console or use AWS SAM for automated deployments.

## Usage:

GET Requests: Send GET requests to /{resource} where resource is clients or users.
![image](https://github.com/DavidCastro88/AWSLambdaFunctionGetAndPost/assets/91480088/99f7ddb8-56ca-45bd-b222-49c147eaf827)

POST Requests: Send POST requests to /{resource} with JSON body containing data for clients or users.
![image](https://github.com/DavidCastro88/AWSLambdaFunctionGetAndPost/assets/91480088/3c4f29b0-49ea-4e50-af96-c692755f3d6d)

