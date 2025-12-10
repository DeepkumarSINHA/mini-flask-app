from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # Renders templates/index.html
    return render_template("index.html")


@app.route("/api/message")
def get_message():
    # Simple API returning JSON
    return jsonify({"msg": "Hello from Flask Backend 👋"})


if __name__ == "__main__":
    # host='0.0.0.0' so it is accessible from outside (Ubuntu server)
    app.run(host="0.0.0.0", port=5000, debug=True)
