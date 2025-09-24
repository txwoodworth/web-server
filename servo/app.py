from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/open")
def open_motor():
    return jsonify({"status": "motor opened"})

@app.route("/home")
def home_motor():
    return jsonify({"status": "motor homed"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
