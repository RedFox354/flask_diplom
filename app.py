import sqlite3
from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import abort
from flask_mongoengine import MongoEngine

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'mongo_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class logs(db.Document):
    url = db.StringField()
    created = db.StringField()
    isAutomated = db.StringField()
    appName = db.StringField()
    appVersion = db.StringField()
    cookieEnabled = db.StringField()
    geolocation = db.StringField()
    platform = db.StringField()
    userAgent = db.StringField()
    javaEnabled = db.StringField()
    Height = db.StringField()
    Width = db.StringField()
    OutHeight = db.StringField()
    OutWidth = db.StringField()
    Opener = db.StringField()
    evalBrowser = db.StringField()
    result = db.StringField()
    def to_json(self):
        return {"url": self.url,
        "created": self.created,
        "isAutomated": self.isAutomated,
        "appName": self.appName,
        "appVersion": self.appVersion,
        "cookieEnabled": self.cookieEnabled,
        "geolocation": self.geolocation,
        "platform": self.platform,
        "userAgent": self.userAgent,
        "javaEnabled": self.javaEnabled,
        "Height": self.Height,
        "Width": self.Width,
        "OutHeight": self.OutHeight,
        "OutWidth": self.OutWidth,
        "Opener": self.Opener,
        "evalBrowser": self.evalBrowser,
        "result": self.result}


@app.route('/', methods=['GET'])
def index():
    '''
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM data').fetchall()
    conn.close()
    '''
    data = db.col.find()
    return render_template('index.html', data=data)

@app.route('/', methods=['POST'])
def process_data():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    data = cur.execute('INSERT INTO data (url, isAutomated, appName, appVersion, cookieEnabled, geolocation, platform, userAgent, javaEnabled, Height, Width, OutHeight, OutWidth, Opener, evalBrowser, result) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (str(data[0]),str(data[1]),str(data[2]),str(data[3]),str(data[4]),str(data[5]),str(data[6]),str(data[7]),str(data[8]),str(data[9]),str(data[10]),str(data[11]),str(data[12]),str(data[13]),str(data[14]),str(data[15])))
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
