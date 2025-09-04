# alert functions placeholder
import sqlite3
from datetime import datetime

DB_PATH = "backend/database/regalert.db"

def create_alert(circular_id, message):
    """
    Insert a new alert into the alerts table.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO alerts (circular_id, alert_message, date_created)
        VALUES (?, ?, ?)
    """, (circular_id, message, datetime.now()))
    conn.commit()
    conn.close()
    print(f"Alert created for circular_id {circular_id}: {message}")

def get_alerts():
    """
    Retrieve all alerts from the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT a.id, c.title, a.alert_message, a.date_created FROM alerts a "
                   "JOIN circulars c ON a.circular_id = c.id "
                   "ORDER BY a.date_created DESC")
    alerts = cursor.fetchall()
    conn.close()
    return alerts

def generate_alert_for_circular(circular_id, summary):
    """
    Example function to generate alerts based on keywords in the summary.
    """
    keywords = ["deadline", "compliance", "risk", "penalty", "mandatory"]
    messages = []
    for word in keywords:
        if word.lower() in summary.lower():
            msg = f"Attention: {word} mentioned in circular summary."
            create_alert(circular_id, msg)
            messages.append(msg)
    return messages

# Example usage:
if __name__ == "__main__":
    # Suppose circular_id 1 exists
    example_messages = generate_alert_for_circular(1, "This circular contains compliance deadlines and mandatory updates.")
    print("Generated alerts:", example_messages)
