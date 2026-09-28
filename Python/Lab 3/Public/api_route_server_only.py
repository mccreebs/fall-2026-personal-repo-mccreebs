import flask

app = flask.Flask(__name__)

@app.get("/")
def handle_naked_domain():
    return "Do you think about me now and then?"

@app.get("/api/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Running Flask")
    app.run(host = '0.0.0.0', port = 8081, debug=True)