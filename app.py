from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://adams_database_user:NK079LqRtrMghxVhVpKQtK2dFrzzYNiL@dpg-cgiaf9vdvk4vd526vf10-a/adams_database")
    conn.close()
    return 'Database connection successful'

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgres://adams_database_user:NK079LqRtrMghxVhVpKQtK2dFrzzYNiL@dpg-cgiaf9vdvk4vd526vf10-a/adams_database")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table created'