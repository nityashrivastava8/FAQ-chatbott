"""
Step 5 (optional): simple chat UI.
Run:  python app.py   then open http://127.0.0.1:5000
"""

from flask import Flask, jsonify, request, send_from_directory

from chatbot import get_answer

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory(".", "chat.html")


@app.route("/ask", methods=["POST"])
def ask():
    return jsonify(answer=get_answer(request.json.get("message", "")))


if __name__ == "__main__":
    app.run(debug=False)