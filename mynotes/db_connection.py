import pymongo

url = "mongodb+srv://adi:root@user-data.wbw7fev.mongodb.net/Notes"
client = pymongo.MongoClient(url)
db = client["Transcribe"]
