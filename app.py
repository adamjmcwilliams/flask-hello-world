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

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgres://adams_database_user:NK079LqRtrMghxVhVpKQtK2dFrzzYNiL@dpg-cgiaf9vdvk4vd526vf10-a/adams_database")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table populated'

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgres://adams_database_user:NK079LqRtrMghxVhVpKQtK2dFrzzYNiL@dpg-cgiaf9vdvk4vd526vf10-a/adams_database")
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    rows = cur.fetchall()
    conn.close()
    template_string = "<table>"
    for player in rows:
        template_string += f"<tr> <td>{player[0]}</td> <td>{player[1]}</td> <td>{player[2]}</td> <td>{player[3]}</td> <td>{player[4]}</td> </tr>"
    template_string += "</table>"
    return template_string

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgres://adams_database_user:NK079LqRtrMghxVhVpKQtK2dFrzzYNiL@dpg-cgiaf9vdvk4vd526vf10-a/adams_database")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table dropped'

