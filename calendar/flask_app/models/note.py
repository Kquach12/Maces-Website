from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash 
from flask_app.models import game

class Note:
    def __init__( self , data ):
        self.id = data['id']
        self.notes = data['notes']
        self.game_id = data['game_id']
        self.games = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM notes ORDER BY game_id ASC;"
        results = connectToMySQL('maces_schema').query_db(query)
        notes = []
        for note in results:
            notes.append( cls(note) )
        return notes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO notes (notes, game_id ) VALUES (%(notes)s, %(game_id)s );"
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
