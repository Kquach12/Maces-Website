from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash 


class Note:
    def __init__( self , data ):
        self.id = data['id']
        self.notes = data['notes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM notes;"
        results = connectToMySQL('maces_schema').query_db(query)
        notes = []
        for note in results:
            notes.append( cls(note) )
        return notes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO notes (notes, created_at, updated_at ) VALUES (%(notes)s, NOW() , NOW() );"
        return connectToMySQL('maces_schema').query_db( query, data )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM notes WHERE id = %(id)s;"
        results = connectToMySQL('maces_schema').query_db(query, data)
        return cls(results[0])
    
        
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM notes WHERE id = %(id)s"
        return connectToMySQL('maces_schema').query_db(query, data)
