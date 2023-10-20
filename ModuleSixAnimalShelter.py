from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30415
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print ("Hello you! Module 6 connected!")

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)  # data should be a dictionary
            return True
        else:
            raise Exception("Nothing to save because the data parameter is empty")

    def read(self, data):
        cursor = self.collection.find(data)
        results = []
        
        for document in cursor:
            dictionary = dict(document)
            results.append(dictionary)
           
        return results
    
    def update(self, query, update_data):
        result = self.collection.update_many(query, {"$set": update_data})
        return result.modified_count

    def delete(self, query):
        result = self.collection.delete_many(query)
        return result.deleted_count
