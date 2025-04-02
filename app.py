

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import psycopg2

app = Flask(__name__)

conn= psycopg2.connect(
    database="jardineria_clases", 
    user="postgres", 
    password="123456", 
    host="localhost", 
    port="5432"
)

@app.route("/procedimientos_bd")
def procedimientos_bd():
    cursor = conn.cursor()
    cursor.execute("SELECT * from oficina")
    oficinas = cursor.fetchall()
    cursor.close()
    conn.close()
    return oficinas
    
@app.route('/')
def home():
    return render_template('home.html')
if __name__=='__main__':
    app.run(debug=True)