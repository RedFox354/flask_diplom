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
    data = request.get_json()
    module.process_data(data)
    #conn = get_db_connection()
    #cur = conn.cursor()
    #data = cur.execute('INSERT INTO data (url, isAutomated, appName, appVersion, cookieEnabled, geolocation, platform, userAgent, javaEnabled, Height, Width, OutHeight, OutWidth, Opener, evalBrowser, result) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
    #                (str(data[0]),str(data[1]),str(data[2]),str(data[3]),str(data[4]),str(data[5]),str(data[6]),str(data[7]),str(data[8]),str(data[9]),str(data[10]),str(data[11]),str(data[12]),str(data[13]),str(data[14]),str(data[15])))
    #conn.commit()
    #conn.close()
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
