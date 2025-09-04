# Flask backend starter
from flask import Flask, request, jsonify
from models.summarizer_model import summarize_text
from models.chatbot_model import answer_query
from utils.preprocess import clean_text, split_into_paragraphs
from utils.alerts import create_alert, generate_alert_for_circular
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), "database", "regalert.db")
conn = sqlite3.connect(DB_PATH)

# Route to summarize regulatory text
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    cleaned_text = clean_text(text)
    summary = summarize_text(cleaned_text)

    # Store circular in DB
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO circulars (title, content, summary) VALUES (?, ?, ?)",
                   ("User Provided Circular", text, summary))
    circular_id = cursor.lastrowid
    conn.commit()
    conn.close()

    # Generate alerts based on summary
    alert_messages = generate_alert_for_circular(circular_id, summary)

    return jsonify({'summary': summary, 'alerts': alert_messages})

# Route for chatbot Q&A
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    context = data.get('context', '')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    answer = answer_query(question, context)

    # Store question and answer in DB
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO queries (question, context, answer) VALUES (?, ?, ?)",
                   (question, context, answer))
    conn.commit()
    conn.close()

    return jsonify({'answer': answer})

# Route to get all alerts
@app.route('/alerts', methods=['GET'])
def get_alerts_route():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT a.id, c.title, a.alert_message, a.date_created "
                   "FROM alerts a JOIN circulars c ON a.circular_id = c.id "
                   "ORDER BY a.date_created DESC")
    alerts = cursor.fetchall()
    conn.close()

    alert_list = []
    for alert in alerts:
        alert_list.append({
            'id': alert[0],
            'circular_title': alert[1],
            'message': alert[2],
            'date_created': alert[3]
        })
    return jsonify({'alerts': alert_list})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
