from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def home():
    return"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Assignment1</title>
        </head>
        <body>
            <h1>Hello World</h1>
        </body>
        </html>
    """

if __name__ == '__main__':
    app.run(port=5000, debug=True)