# Local Setup

To set up the repo for local development, follow the steps:

1. Clone the repo.
2. Create a virtual environment (my python version is 3.9, versions around that should be fine?).
3. Once you have the venv created, run `source venv/bin/activate` to activate the venv.
4. Run `pip install -r requirements.txt` to install dependencies, use pip3 if needed (should not be needed if you have
   venv activated).
5. Install MongoDB community edition if not
   already [from here for mac](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/
   ).
6. Create a .env file and put the value `ENV="DEV"` and `MONGODB_URI_DEV = "mongodb://localhost:27017"` to connect to
   local MongoDB client.
7. Start coding 🚀

# Structure

Code should live in the `src` folder and create subdirectories when necessary (but this seems to be a suboptimal
structure?).

I was not able to figure out how to properly setup `__init__.py` files in subdirectories (or if that is needed at all),
so if you can figure it out, feel free to restructure the project.

# Build and deployment

The AWS Lambda function code is built with the `build.sh` and automatically deployed upon push/merge.

To manually create a distribution, run `build.sh` and it will create a `dist.zip`.

# Local AWS Lambda Testing

For local testing and troubleshooting, build a docker image with

`docker build -t my-lambda-image .`

then run the image with

`docker run -p 9000:8080 my-lambda-image`

The function can be invoked at the endpoint

`http://localhost:9000/2015-03-31/functions/function/invocations`

The invocation mimics the test runs from the AWS console, in production, the event passed to the lambda function is a
full HTTP passthrough as if from API Gateway (due to us using function url), so consider adding necessary info in the
body. The event and context would be the same as the console if the invocation is through a restful API Gateway.

## example request payload

```json
{
  "version": "2.0",
  "routeKey": "$default",
  "rawPath": "/my/path",
  "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
  "cookies": [
    "cookie1",
    "cookie2"
  ],
  "headers": {
    "header1": "value1",
    "header2": "value1,value2"
  },
  "queryStringParameters": {
    "parameter1": "value1,value2",
    "parameter2": "value"
  },
  "requestContext": {
    "accountId": "123456789012",
    "apiId": "<urlid>",
    "authentication": null,
    "authorizer": {
        "iam": {
                "accessKey": "AKIA...",
                "accountId": "111122223333",
                "callerId": "AIDA...",
                "cognitoIdentity": null,
                "principalOrgId": null,
                "userArn": "arn:aws:iam::111122223333:user/example-user",
                "userId": "AIDA..."
        }
    },
    "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
    "domainPrefix": "<url-id>",
    "http": {
      "method": "POST",
      "path": "/my/path",
      "protocol": "HTTP/1.1",
      "sourceIp": "123.123.123.123",
      "userAgent": "agent"
    },
    "requestId": "id",
    "routeKey": "$default",
    "stage": "$default",
    "time": "12/Mar/2020:19:03:58 +0000",
    "timeEpoch": 1583348638390
  },
  "body": "Hello from client!",
  "pathParameters": null,
  "isBase64Encoded": false,
  "stageVariables": null
}