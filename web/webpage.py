from flask import Flask, send_file, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "<html><body><h1>Dashboard</h1><img src='/webcam/snapshot' /><br><button onclick=\"fetch('/api/open')\">Open</button></body></html>"

@app.route("/static/hello.txt")
def s(): return "static"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
