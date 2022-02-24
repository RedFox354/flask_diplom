import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mongo_database"]
col = db["logs"]
dict = {"url":"testurl1","created":"testtime","isAutomated":"true","appName":"testapp",
    "appVersion":"testver","cookieEnabled":"true","geolocation":"testloc",
    "platform":"testplatform","userAgent":"testagent","javaEnabled":"true",
    "Height":"1","Width":"1","OutHeight":"1","OutWidth":"1","Opener":"trueopener",
    "evalBrowser":"111","result":"exactly_bot"}
#x = col.insert_one(dict)
#insert_many([{},{}])
#print(x.inserted_ids)
x = col.find_one()
print(x)
