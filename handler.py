from app import lambda_handler  # Import the lambda_handler from app.py

def hello(event, context):
    # You no longer need this because `lambda_handler` in app.py will handle the event.
    return lambda_handler(event, context)

