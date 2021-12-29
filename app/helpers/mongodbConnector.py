from mongoengine import connect

class Connection:
    def connect_mongodb(self, connection_string="192.241.144.225:27017", database_name="my_database"):

        connect(host="mongodb://"+connection_string+"/"+database_name)
