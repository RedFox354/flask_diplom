import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO data (isautomated, appName, appVersion, cookieEnabled, geolocation, platform, userAgent, javaEnabled, Height, Width, OutHeight, OutWidth, Opener, evalBrowser) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('nonautomated', 'TestApp', 'TestVersion', 'true', 'testlocation', 'testplatform', 'testagent', 'true', '1000', '500', '1100', '600', 'testopener', '5')
            )

cur.execute("INSERT INTO data (isautomated, appName, appVersion, cookieEnabled, geolocation, platform, userAgent, javaEnabled, Height, Width, OutHeight, OutWidth, Opener, evalBrowser) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('automated', 'TestApp2', 'TestVersion2', 'true2', 'testlocation2', 'testplatform2', 'testagent2', 'true2', '1002', '502', '1102', '602', 'testopener2', '6')
            )

connection.commit()
connection.close()
