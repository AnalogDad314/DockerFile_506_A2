from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/tomswanson')
def hello_tom():
    return 'Hello world from Tom Swanson'

@app.route('/datetime')
def current_datetime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

