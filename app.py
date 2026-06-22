from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import os
from datetime import datetime

app = Flask(__name__, static_folder='.')
CORS(app)

DB_NAME = 'notes.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/notes', methods=['GET'])
def get_notes():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes ORDER BY id DESC')
    notes = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(notes)

@app.route('/api/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    content = data.get('content', '').strip()
    if not content:
        return jsonify({'error': 'Note cannot be empty'}), 400
    created_at = datetime.now().strftime('%b %d, %I:%M %p')
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (content, created_at) VALUES (?, ?)', (content, created_at))
    conn.commit()
    note_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': note_id, 'content': content, 'created_at': created_at}), 201

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Note deleted'})

if __name__ == '__main__':
    init_db()
    print("✅ QuickNote App running at http://localhost:5000")
    app.run(debug=True, port=5000)
