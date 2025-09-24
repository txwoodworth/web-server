from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/api/open", methods=["POST","GET"])
def open_servo(): 
    print("servo: open called")
    return jsonify({"status":"opened"})
@app.route("/api/status")
def status(): return jsonify({"ok":True})
if __name__ == "__main__": app.run(host="0.0.0.0", port=8081)
