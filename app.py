from flask import Flask
from aws_lambda_wsgi import response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, flask"

@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return f"Hello, {name}!"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    return "Goodbye, World!"

def lambda_handler(event, context):
    return response(app, event, context)

