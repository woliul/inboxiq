import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('emails.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    query = "SELECT id, subject FROM emails"  # Only get what you need for the list view
    args = []

    # Simple search filter
    search_query = request.args.get('search', '')
    if search_query:
        query += " WHERE subject LIKE ? OR body LIKE ?"
        args = [f"%{search_query}%", f"%{search_query}%"]

    emails = conn.execute(query, args).fetchall()
    conn.close()
    return render_template('index.html', emails=emails)


# This is for a dashboard/detail view
@app.route('/email/<int:email_id>')
def view_email(email_id):
    conn = get_db_connection()
    # Retrieve the 'raw_body' column
    email = conn.execute('SELECT id, subject, raw_body FROM emails WHERE id = ?', (email_id,)).fetchone()
    conn.close()

    if email is None:
        return "Email not found.", 404

    return render_template('view_email.html', email=email)