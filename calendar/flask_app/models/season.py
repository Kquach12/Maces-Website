from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash 


class Season:
    def __init__( self , data ):
        self.id = data['id']
        self.start_year = data['start_year']
        self.end_year = data['end_year']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM seasons;"
        results = connectToMySQL('maces_schema').query_db(query)
        seasons = []
        for season in results:
            seasons.append( cls(season) )
        return seasons

    @classmethod
    def save(cls, data):
        query = "INSERT INTO seasons (start_year, end_year, created_at, updated_at ) VALUES (%(start_year)s, %(end_year)s, NOW() , NOW() );"
        return connectToMySQL('maces_schema').query_db( query, data )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM seasons WHERE id = %(id)s;"
        results = connectToMySQL('maces_schema').query_db(query, data)
        return cls(results[0])


    @classmethod
    def get_most_recent(cls):
        query = "SELECT * FROM seasons ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL('maces_schema').query_db(query)
        return cls(results[0])
    
        
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM seasons WHERE id = %(id)s"
        return connectToMySQL('maces_schema').query_db(query, data)
