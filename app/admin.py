from flask import Blueprint, render_template
import sqlite3

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/dashboard")
def admin_dashboard():
    conn = sqlite3.connect("hrchatbot.db")
    cur = conn.cursor()
    cur.execute("SELECT category, COUNT(*) FROM chatbot_logs GROUP BY category")
    data = cur.fetchall()
    conn.close()

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("dashboard_admin.html", labels=labels, values=values)
