from flask import Blueprint, render_template, request, jsonify
import sqlite3
import datetime

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/chatbot")
def chatbot_page():
    return render_template("chatbot_ui.html")

@chatbot_bp.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    category = "General"

    response = f"Echo: {user_input}"

    conn = sqlite3.connect("hrchatbot.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO chatbot_logs (question, response, category, timestamp) VALUES (?, ?, ?, ?)",
        (user_input, response, category, datetime.datetime.now()),
    )
    conn.commit()
    conn.close()

    return jsonify({"response": response})
