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
    "rawPath": "/",
    "rawQueryString": "",
    "headers": {
      "sec-fetch-mode": "cors",
      "content-length": "17",
      "referer": "http://localhost:3000/",
      "x-amzn-tls-version": "TLSv1.2",
      "sec-fetch-site": "cross-site",
      "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
      "x-forwarded-proto": "https",
      "origin": "http://localhost:3000",
      "x-forwarded-port": "443",
      "x-forwarded-for": "2601:647:4000:2ac0:745e:d1a2:a8bf:f39b",
      "accept": "*/*",
      "x-amzn-tls-cipher-suite": "ECDHE-RSA-AES128-GCM-SHA256",
      "sec-ch-ua": "'Google Chrome';v='111', 'Not(A:Brand';v='8', 'Chromium';v='111'",
      "sec-ch-ua-mobile": "?0",
      "x-amzn-trace-id": "Root=1-6418dc60-360418b6302432e036f2f926",
      "sec-ch-ua-platform": "'macOS'",
      "host": "j635an2edqmaoyggrqy4sritge0qlsqf.lambda-url.us-east-2.on.aws",
      "content-type": "text/plain;charset=UTF-8",
      "accept-encoding": "gzip, deflate, br",
      "sec-fetch-dest": "empty",
      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    },
    "requestContext": {
      "accountId": "anonymous",
      "apiId": "j635an2edqmaoyggrqy4sritge0qlsqf",
      "domainName": "j635an2edqmaoyggrqy4sritge0qlsqf.lambda-url.us-east-2.on.aws",
      "domainPrefix": "j635an2edqmaoyggrqy4sritge0qlsqf",
      "http": {
        "method": "POST",
        "path": "/",
        "protocol": "HTTP/1.1",
        "sourceIp": "2601:647:4000:2ac0:745e:d1a2:a8bf:f39b",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
      },
      "requestId": "d85f0362-f66c-43b2-bbb2-28aef748c6a1",
      "routeKey": "$default",
      "stage": "$default",
      "time": "20/Mar/2023:22:21:20 +0000",
      "timeEpoch": 1679350880872
    },
    "body": "{'keyword':'egg'}",
    "isBase64Encoded": "False"
  }
  ```
  