import json


def handler(event, context):
    # main entry point for lambda
    # return scrape.handler({"keyword": "egg"}, None)
    return json.dumps({"message": "To be implemented"})


if __name__ == '__main__':
    print(handler({"key": "value"}, None))




