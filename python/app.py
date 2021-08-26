import os
from flask import Flask


app = Flask(__name__)
env = os.environ.get('ENV', 'dev')

@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/ping')
def ping():
    return 'pong'
    

if __name__ == '__main__':
    debug = env == 'dev'
    app.run(debug=debug, host='0.0.0.0')
