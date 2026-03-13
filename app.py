from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# create database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        marks INTEGER
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# add student
@app.route('/add', methods=['POST'])
def add_student():
    data = request.json
    name = data['name']
    marks = data['marks']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO students(name,marks) VALUES (?,?)",(name,marks))

    conn.commit()
    conn.close()

    return jsonify({"message":"Student Added"})

# get students
@app.route('/students')
def get_students():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    conn.close()

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)