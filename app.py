

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import psycopg2

app = Flask(__name__)


# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/jardineria_clases'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


    
@app.route("/empleados", methods=['GET'])
def empleados():
     with db.engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM empleado;"))
        app.logger.info(result)
        empleados = [dict(row._mapping) for row in result]  # ✅ Convertir a diccionario
        return render_template('empleados.html', empleados=empleados)  # Enviar a la plantilla HTML

@app.route('/')
def home():
    return render_template('home.html')
if __name__=='__main__':
    app.run(debug=True)