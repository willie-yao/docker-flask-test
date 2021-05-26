from flask import Flask
from flask import Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/test")
def test():
  return Response("{'test': 'Hello World!'}", status=201, mimetype='application/json')

if __name__ == "__main__":
  app.run()