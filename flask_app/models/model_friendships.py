

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

model_db = "friendships_schema"


class Friendships:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name FROM users JOIN friendships ON users.id = friendships.user_id LEFT JOIN users AS users2 ON friendships.friend_id = users2.id;"
        results = connectToMySQL(model_db).query_db(query)
        print('!!!!')
        print(results)
        # (userS/no()) = []
        # for user in results:
        #     (userS/no()).append(cls(user))
        return results