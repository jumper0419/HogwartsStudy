from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "hello world"


@app.route("/get_params")
def get_params():
  return request.args


@app.route("/get_body", methods=['POST'])
def get_post_res():
  return request.body


if __name__ == "__main__":
  app.run(debug=True)