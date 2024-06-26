from flask import Flask, render_template, request, redirect, url_for
import sqlite3 
from datetime import datetime

app = Flask(__name__)


def init_db():
    with sqlite3.connect('plants.db') as conn:
        conn.execute('''
        CREATE TBALE IF NOT EXIST plants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_watered TEXT))
        )
 ''') 
