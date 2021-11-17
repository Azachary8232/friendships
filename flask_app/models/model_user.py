# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

modeldb = "friendship_schema"





class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ***CREATE***

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        user_id = connectToMySQL(modeldb).query_db(query,data)
        return user_id





    # ***Retreive***






    # ***Update***







    # ***Delete***