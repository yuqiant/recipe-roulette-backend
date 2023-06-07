import json
from urllib.parse import parse_qs
from typing import Callable
from bson import json_util
import re


class Router():

    def __init__(self):
        self.__routes = {
            "get": {},
            "post": {},
            "put": {},
            "delete": {}
        }

    def parse_event(event):
        query_string = event['rawQueryString']
        headers = event['headers']
        http = event['requestContext']['http']
        path = http['path']
        method = http['method']
        query_parameters = parse_qs(query_string)
        body = event['body'] if "body" in event else {}
        return {
            "method": method,
            "path": path,
            "query_parameters": query_parameters,
            "body": body
        }

    def parse_dynamic_url(url_pattern, url):
        regex_pattern = re.sub(r':(\w+)', r'(?P<\1>[^/]+)', url_pattern)
        match = re.match(regex_pattern, url)
        if match:
            return match.groupdict()
        else:
            return None

    def get(self, path: str, handler: Callable):
        self.__routes['get'][path] = handler

    def post(self, path: str, handler: Callable):
        self.__routes['post'][path] = handler

    def put(self, path: str, handler: Callable):
        self.__routes['put'][path] = handler

    def delete(self, path: str, handler: Callable):
        self.__routes['delete'][path] = handler

    def handle(self, event):
        parsed_event = Router.parse_event(event)
        method = parsed_event['method']
        path = parsed_event['path']
        query_parameters = parsed_event['query_parameters']
        body = parsed_event.get('body', {})
        if method == 'GET':
            handler = self.__routes['get'].get(path, None)
        elif method == 'POST':
            handler = self.__routes['post'].get(path, None)
        else:
            handler = None

        if handler is not None:
            statusCode = 200
            data = handler(query_parameters, body)
        else:
            statusCode = 404
            data = {
                "message": "No route found"}

        response = {
            "statusCode": statusCode,
            "headers": {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*'
            },
            "data": data
        }
        return json_util.dumps(response)

    # GET /ingredients
    # get all ingredients

    # GET /user?userId=some-id
    # get the user's profile

    # GET /user/inventory?userId=some-id
    # get the user's inventory

    # POST /user/inventory?userId=some-id
    # updates the user's inventory
    # body: {
    #   ingredientName: string,
    #   action: string "ADD" or "REMOVE"
    # }

    # GET /user/settings?userId=some-id
    # get the user's settings

    # POST /user/settings?userId=some-id
    # updates the user's settings
    # body: {
    #    setting: some object (TBD)
    # }

    # POST /recipes
    # get a list of recipes based on the ingredients in the request body
    # body: {
    #   ingredients: [string]
    # }

    # # perform logic based on the inputs
    # if method == 'POST':
    #     # do something with the POST request
    #     response_body = {'message': 'This is a POST request.'}
    #     status_code = 200
    # else:
    #     # handle other types of requests
    #     response_body = {'message': 'This is not a POST request.'}
    #     status_code = 400

    # # return the response
    # response = {
    #     'statusCode': status_code,
    #     'headers': {
    #         'Content-Type': 'application/json'
    #     },
    #     'body': json.dumps(response_body)
    # }
    # return response


if __name__ == "__main__":

    event = {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/user/inventory",
        "rawQueryString": "userId=12345",
        "headers": {
            "sec-fetch-mode": "cors",
            "referer": "http://localhost:3000/",
            "x-amzn-tls-version": "TLSv1.2",
            "sec-fetch-site": "cross-site",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "x-forwarded-proto": "https",
            "origin": "http://localhost:3000",
            "x-forwarded-port": "443",
            "x-forwarded-for": "2601:647:4000:2ac0:acce:eb4:7ba3:6641",
            "accept": "*/*",
            "x-amzn-tls-cipher-suite": "ECDHE-RSA-AES128-GCM-SHA256",
            "sec-ch-ua": "'Google Chrome';v='113', 'Chromium';v='113', 'Not-A.Brand';v='24'",
            "sec-ch-ua-mobile": "?0",
            "x-amzn-trace-id": "Root=1-6463b5e4-16e46c377bbb778c19b1d7ce",
            "sec-ch-ua-platform": "'macOS'",
            "host": "j635an2edqmaoyggrqy4sritge0qlsqf.lambda-url.us-east-2.on.aws",
            "accept-encoding": "gzip, deflate, br",
            "sec-fetch-dest": "empty",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        },
        "queryStringParameters": {
            "userId": "12345"
        },
        "requestContext": {
            "accountId": "anonymous",
            "apiId": "j635an2edqmaoyggrqy4sritge0qlsqf",
            "domainName": "j635an2edqmaoyggrqy4sritge0qlsqf.lambda-url.us-east-2.on.aws",
            "domainPrefix": "j635an2edqmaoyggrqy4sritge0qlsqf",
            "http": {
                "method": "POST",
                "path": "/user/inventory",
                "protocol": "HTTP/1.1",
                "sourceIp": "2601:647:4000:2ac0:acce:eb4:7ba3:6641",
                "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
            },
            "requestId": "cd9302b4-e46a-4370-9be5-9c580b6f1dce",
            "routeKey": "$default",
            "stage": "$default",
            "time": "16/May/2023:16:57:08 +0000",
            "timeEpoch": 1684256228574
        },
        "body": {},
        "isBase64Encoded": False
    }

    def test(qp, b):
        return qp["userId"]

    router = Router()
    router.get('/ingredient', lambda _: 'get all ingredients')
    router.get('/user', lambda _: 'get the user\'s profile')
    router.post('/user/inventory', test)
    print(router.handle(event))

    # print(Router.parse_event(event))
