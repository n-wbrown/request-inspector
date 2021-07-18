import argparse
from flask import Flask, request
from werkzeug.routing import Rule

app = Flask(__name__)


app.url_map.add(Rule('/', endpoint='index'))

@app.endpoint('index')
def hello_world():
    # app.logger.warning(f"{request}")
    print("request          ", request)
    print("request.path:    ", request.path)
    print("request.method:  ", request.method)
    print("request.args:    ", request.args)
    print("request.files:   ", request.files)
    print("request.json:    ", request.json)
    print("request.data:    ", request.data)
    return ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="request_inspector")
    parser.add_argument(
        "--host", 
        default="127.0.0.1",
        type=str,
        help="Designate host IP address",
    )
    parser.add_argument(
        "--port", 
        default=8080,
        type=int,
        help="Designate host port",
    )

    args = vars(parser.parse_args())

    app.run(
        host=args['host'],
        port=args['port'],
        debug=False,
    )
