from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash 


class Reminder:
    def __init__( self , data ):
        self.id = data['id']
        self.subject = data['subject']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM reminders;"
        results = connectToMySQL('maces_schema').query_db(query)
        reminders = []
        for reminder in results:
            reminders.append( cls(reminder) )
        return reminders

    @classmethod
    def save(cls, data):
        query = "INSERT INTO reminders (subject, text, created_at, updated_at, user_id ) VALUES (%(subject)s, %(text)s, NOW() , NOW(), %(user_id)s );"
        return connectToMySQL('maces_schema').query_db( query, data )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM reminders WHERE id = %(id)s;"
        results = connectToMySQL('maces_schema').query_db(query, data)
        return cls(results[0])
    
        
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM reminders WHERE id = %(id)s"
        return connectToMySQL('maces_schema').query_db(query, data)
