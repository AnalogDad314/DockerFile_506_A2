from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world from Tom Swanson'

@app.route('/datetime')
def current_datetime():
    return str(datetime.datetime.now())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
