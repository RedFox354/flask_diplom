import sqlite3

def init_db():
    connection = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    cur.execute("INSERT INTO data (url, isAutomated, appName, appVersion, cookieEnabled, geolocation, platform, userAgent, javaEnabled, Height, Width, OutHeight, OutWidth, Opener, evalBrowser, result) VALUES (?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                ('testhref', 'nonautomated', 'TestApp', 'TestVersion', 'true', 'testlocation', 'testplatform', 'testagent', 'true', '1000', '500', '1100', '600', 'testopener', '5', 'undefined')
                )
    cur.execute("INSERT INTO data (url, isAutomated, appName, appVersion, cookieEnabled, geolocation, platform, userAgent, javaEnabled, Height, Width, OutHeight, OutWidth, Opener, evalBrowser, result) VALUES (?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                ('testhref2','automated', 'TestApp2', 'TestVersion2', 'true2', 'testlocation2', 'testplatform2', 'testagent2', 'true2', '1002', '502', '1102', '602', 'testopener2', '6', 'exactlybot')
                )
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
    print(data)
    print(str(data[15]))
    if (str(data[15])=="{'Result': 'undefined'}"):
        data[15] = "Result: Wasn't suspicious activity"
    elif (str(data[15])=="{'Result': 'csm'}"):
        data[15] = "Result: Constant cursor speed"
    elif (str(data[15])=="{'Result': 'gtlwm'}"):
        data[15] = "Result: Went to link without mouse"
    elif (str(data[15])=="{'Result': 'gthl'}"):
        data[15] = "Result: Went to hidden link"
    elif (str(data[15])=="{'Result': 'wsb'}"):
        data[15] = "Result: Window sizes such as bot"
    else:
        data[15] = "Result: strange result"
    conn = get_db_connection()
    cur = conn.cursor()
    data = cur.execute('INSERT INTO data (ip, url, isAutomated, appName, appVersion, cookieEnabled, geolocation, platform, userAgent, javaEnabled, Height, Width, OutHeight, OutWidth, Opener, evalBrowser, result) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (str(ip_address),str(data[0]),str(data[1]),str(data[2]),str(data[3]),str(data[4]),str(data[5]),str(data[6]),str(data[7]),str(data[8]),str(data[9]),str(data[10]),str(data[11]),str(data[12]),str(data[13]),str(data[14]),str(data[15])))
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
