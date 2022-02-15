from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash 


class Eligible_email:
    def __init__( self , data ):
        self.id = data['id']
        self.emails = data['emails']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM eligible_emails;"
        results = connectToMySQL('maces_schema').query_db(query)
        eligible_emails = []
        for eligible_email in results:
            eligible_emails.append( cls(eligible_email) )
        return eligible_emails

    @classmethod
    def save(cls, data):
        query = "INSERT INTO eligible_emails (emails, created_at, updated_at, user_id ) VALUES (%(emails)s NOW() , NOW(), %(user_id)s );"
        return connectToMySQL('maces_schema').query_db( query, data )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM eligible_emails WHERE id = %(id)s;"
        results = connectToMySQL('maces_schema').query_db(query, data)
        return cls(results[0])
    

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM eligible_emails WHERE id = %(id)s"
        return connectToMySQL('maces_schema').query_db(query, data)


