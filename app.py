import sqlite3
from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import abort
import import_module as module

'''
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
'''
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = module.index()
    return render_template('index.html', data=data)

@app.route('/', methods=['POST'])
def process_data():
    ip_address = request.remote_addr
    data = request.get_json()
    module.process_data(data, ip_address)
    return jsonify({'result': 'ok'})

'''
def get_data(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM data WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
'''

@app.route('/<int:post_id>')
def post(post_id):
    post = module.get_data(post_id)
    return render_template('post.html', post=post)
