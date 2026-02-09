from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/dictar", methods=["POST"])
def dictar():
    subprocess.Popen([
        "bash",
        "/home/gabot3/whisper-lab/dictar.sh"
    ])
    return jsonify({"status": "dictado iniciado"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8765)
