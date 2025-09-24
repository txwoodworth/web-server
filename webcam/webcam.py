from flask import Flask, send_file
app = Flask(__name__)
@app.route("/webcam/snapshot")
def snap():
    # create a tiny image or ship a placeholder file
    return send_file("test_image.jpg", mimetype="image/jpeg")
if __name__ == "__main__": app.run(host="0.0.0.0", port=8082)
