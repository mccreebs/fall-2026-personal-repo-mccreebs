import flask

app = flask.Flask(__name__, static_url_path="", static_folder="Public")

@app.route("/")
def hello_route():
    return "Hello World!"


if __name__ == "__main__":
    print("Running Flask")
    app.run(host = '0.0.0.0', port = 8081, debug=True)