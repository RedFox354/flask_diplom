import sqlite3
from flask import Flask, render_template, request, jsonify

def init_db():
    connection = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    connection.commit()
    connection.close()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM data').fetchall()
    conn.close()
    return data

def process_data(data, ip_address):
    if 'URL' in data:
        url = data['URL']
    if 'Automated' in data:
        automated = data['Automated']
    if 'AppName' in data:
        appname = data['AppName']
    if 'AppVersion' in data:
        appversion = data['AppVersion']
    if 'CookieEnabled' in data:
        cookieenabled = data['CookieEnabled']
    if 'GeoLocation' in data:
        geolocation = data['GeoLocation']
    if 'Platform' in data:
        platform = data['Platform']
    if 'Useragent' in data:
        useragent = data['Useragent']
    if 'JavaEnabled' in data:
        javaenabled = data['JavaEnabled']
    if 'WindowHeight' in data:
        windowheight = data['WindowHeight']
    if 'WindowWidth' in data:
        windowwidth = data['WindowWidth']
    if 'WindowOutHeight' in data:
        windowoutheigth = data['WindowOutHeight']
    if 'WindowOutWidth' in data:
        windowoutwidth = data['WindowOutWidth']
    if 'Opener' in data:
        opener = data['Opener']
    if 'Eval' in data:
        eval = data['Eval']
    if 'Result' in data:
        result = data['Result']

    if (result =='undefined'):
        result = "Was not suspicious activity"
    elif (result =='wsb'):
        result = "browser is automated"
    elif (result =='csm'):
        result = "Constant cursor speed"
    elif (result =='gtlwm'):
        result = "Went to link without mouse"
    elif (result =='gthl'):
        result = "Went to hidden link"
    elif (result =='wsb'):
        result = "Window sizes such as bot"
    else:
        result = "strange result"

    conn = get_db_connection()
    cur = conn.cursor()
    data = cur.execute('INSERT INTO data (ip, url, isAutomated, appName, appVersion, cookieEnabled, geolocation, platform, userAgent, javaEnabled, Height, Width, OutHeight, OutWidth, Opener, evalBrowser, result) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (str(ip_address),str(url),str(automated),str(appname),str(appversion),str(cookieenabled),str(geolocation),str(platform),str(useragent),str(javaenabled),str(windowheight),str(windowwidth),str(windowoutheigth),str(windowoutwidth),str(opener),str(eval),str(result)))
    conn.commit()
    conn.close()
    return 0

def get_data(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM data WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
