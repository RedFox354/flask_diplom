import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
'''
cur.execute("INSERT INTO data (ip, url, isAutomated, appName, appVersion, cookieEnabled, geolocation, platform, userAgent, javaEnabled, Height, Width, OutHeight, OutWidth, Opener, evalBrowser, result) VALUES (?,?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('1.1.1.1','testhref', 'nonautomated', 'TestApp', 'TestVersion', 'true', 'testlocation', 'testplatform', 'testagent', 'true', '1000', '500', '1100', '600', 'testopener', '5', 'undefined')
            )

cur.execute("INSERT INTO data (ip, url, isAutomated, appName, appVersion, cookieEnabled, geolocation, platform, userAgent, javaEnabled, Height, Width, OutHeight, OutWidth, Opener, evalBrowser, result) VALUES (?,?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('2.1.1.1','testhref2','automated', 'TestApp2', 'TestVersion2', 'true2', 'testlocation2', 'testplatform2', 'testagent2', 'true2', '1002', '502', '1102', '602', 'testopener2', '6', 'exactlybot')
            )
'''
connection.commit()
connection.close()
