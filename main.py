from flask import Flask, render_template, request, redirect, url_for
import sqlite3 
from datetime import datetime

app = Flask(__name__)


def init_db():
    with sqlite3.connect('plants.db') as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS plants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_watered TEXT
        )
    ''') 

@app.route('/')
def home():
    with sqlite3.connect('plants.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM plants')
        plants = cur.fetchall()
    return render_template('home.html', plants=plants)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    species = request.form['species']
    with sqlite3.connect('plants.db') as conn:
        conn.execute('INSERT INTO plants (name, species) VALUES (?, ?)', (name, species))
    return redirect(url_for('home'))

@app.route('/water/<int:id>')
def water(id):
    with sqlite3.connect('plants.db') as conn:
        conn.execute('UPDATE plants SET last_watered = ? WHERE id = ?', (datetime.utcnow(), id))
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
