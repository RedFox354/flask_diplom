import sqlite3
from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM data').fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/', methods=['POST'])
def process_data():
    if request.method == "POST":
        data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()
        #data = cur.execute('INSERT INTO data (who,automated) VALUES ("test","test2")')
        data = cur.execute('INSERT INTO data (who,automated) VALUES (?,?)',(str(data[3]),str(data[0])))
        conn.commit()
        conn.close()
        return jsonify({'result': 'ok'})

def get_data(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM data WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/<int:post_id>')
def post(post_id):
    post = get_data(post_id)
    return render_template('post.html', post=post)
