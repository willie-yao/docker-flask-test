from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/get-data')
def get_data():
    flask_b_address = os.environ['FLASK_B_ADDRESS']
    res = requests.get('{0}/test'.format(flask_b_address)).content
    print(res)
    return res

if __name__ == "__main__":
  app.run()