import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "BBO TikTok OAuth Callback",
        "status": "running"
    }), 200


@app.route("/callback", methods=["GET"])
def tiktok_callback():
    error = request.args.get("error")
    code = request.args.get("code")
    state = request.args.get("state")

    if error:
        return jsonify({
            "status": "authorization_failed",
            "message": "TikTok authorization was not completed."
        }), 400

    if not code or not state:
        return jsonify({
            "status": "invalid_callback",
            "message": "Authorization response is incomplete."
        }), 400

    # Penerimaan callback sahaja.
    # Pengesahan state dan pertukaran code kepada token
    # mesti disediakan sebelum digunakan untuk penerbitan sebenar.
    return jsonify({
        "status": "callback_received",
        "message": (
            "Callback received. Token exchange is not configured yet."
        )
    }), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
