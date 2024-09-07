import pymongo
import certifi
connection_string = "mongodb+srv://xemr99:bems3kTq7VJAocqg@cluster0.6lqit.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(connection_string, tlsCAfile = certifi.where())
dataBase = client.get_database("Organika")
