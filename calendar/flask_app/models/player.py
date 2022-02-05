from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash 


class Player:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.number = data['number']
        self.level = data['level']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.season_id = data['season_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM players;"
        results = connectToMySQL('maces_schema').query_db(query)
        players = []
        for player in results:
            players.append( cls(player) )
        return players

    @classmethod
    def save(cls, data):
        query = "INSERT INTO players (first_name, last_name, number, level, description, created_at, updated_at ) VALUES (%(first_name)s, %(last_name)s, %(number)s, %(level)s, %(description)s, NOW() , NOW() );"
        return connectToMySQL('maces_schema').query_db( query, data )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM players WHERE id = %(id)s;"
        results = connectToMySQL('maces_schema').query_db(query, data)
        return cls(results[0])
    

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM players WHERE id = %(id)s"
        return connectToMySQL('maces_schema').query_db(query, data)


