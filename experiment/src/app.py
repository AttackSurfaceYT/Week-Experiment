import os
from flask import Flask, jsonify

app = Flask(__name__)

AWS_ACCESS_KEY_ID = "AKIA3CGVKYJOPVBPJRGE"
AWS_SECRET_ACCESS_KEY = "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"

REGION = "us-east-2"

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "region": REGION
    })


@app.route("/stats")
def stats():
    # TODO: replace wit db query
    return jsonify({
        "users": 0,
        "requests": 0
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080))
    )