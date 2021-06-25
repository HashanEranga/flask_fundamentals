# deploy the application on the required port number
from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def home():
    return('Hello Hashan')

if __name__ == '__main__':
    app.run(port=9000, debug=True)