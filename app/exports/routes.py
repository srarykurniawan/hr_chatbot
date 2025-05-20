# Export to Excel/PDF


from flask import Blueprint, send_file, request
import sqlite3
import pandas as pd
from xhtml2pdf import pisa
from io import BytesIO, StringIO
from flask import render_template

export_bp = Blueprint('export', __name__)

DB_PATH = 'hrchatbot.db'

@export_bp.route('/export/excel')
def export_excel():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM chatbot_logs", conn)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Logs')
    output.seek(0)
    return send_file(output, as_attachment=True, download_name='chatbot_logs.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@export_bp.route('/export/pdf')
def export_pdf():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM chatbot_logs", conn)
    html = render_template('pdf_template.html', data=df.to_dict(orient='records'))

    result = BytesIO()
    pisa.CreatePDF(StringIO(html), dest=result)
    result.seek(0)
    return send_file(result, as_attachment=True, download_name='chatbot_logs.pdf', mimetype='application/pdf')
