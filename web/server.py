from flask import Flask, send_from_directory, Response
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# Proxy servo API
@app.route("/api/open")
def api_open():
    r = requests.get("http://servo:5000/open")
    return r.json()

@app.route("/api/home")
def api_home():
    r = requests.get("http://servo:5000/home")
    return r.json()

# Proxy webcam stream
@app.route("/webcam")
def webcam_proxy():
    r = requests.get("http://webcam:8081", stream=True)
    return Response(r.iter_content(chunk_size=1024),
                    content_type=r.headers.get("Content-Type", "image/jpeg"))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
