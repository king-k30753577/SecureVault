from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DB_PATH = os.path.join(BASE_DIR, 'vault.db')
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')


def init_db():

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_name TEXT
    )
    """)

    conn.commit()
    conn.close()


@app.route('/')
def index():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM files ORDER BY id DESC')

    files = cursor.fetchall()

    conn.close()

    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload():

    uploaded_files = request.files.getlist('files')

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for file in uploaded_files:

        if file.filename != '':

            file_path = os.path.join(UPLOAD_FOLDER, file.filename)

            file.save(file_path)

            cursor.execute(
                'INSERT INTO files (original_name) VALUES (?)',
                (file.filename,)
            )

    conn.commit()
    conn.close()

    return redirect(url_for('index'))


@app.route('/open/<filename>')
def open_file(filename):

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.exists(file_path):
        return send_file(file_path)

    return 'File not found', 404


@app.route('/delete/<int:file_id>', methods=['POST'])
def delete_file(file_id):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT original_name FROM files WHERE id=?',
        (file_id,)
    )

    file_data = cursor.fetchone()

    if file_data:

        filename = file_data[0]

        file_path = os.path.join(UPLOAD_FOLDER, filename)

        if os.path.exists(file_path):
            os.remove(file_path)

    cursor.execute(
        'DELETE FROM files WHERE id=?',
        (file_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({'status': 'deleted'})


if __name__ == '__main__':

    init_db()

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
  )
  
