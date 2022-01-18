from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash 


class Stat:
    def __init__( self , data ):
        self.id = data['id']
        self.points = data['points']
        self.rebounds = data['rebounds']
        self.assists = data['assists']
        self.steals = data['steals']
        self.blocks = data['blocks']
        self.turnovers = data['turnovers']
        self.made_shots = data['made_shots']
        self.attempted_shots = data['attempted_shots']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.game_id = data['game_id']
        self.player_id = data['player_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM stats;"
        results = connectToMySQL('maces_schema').query_db(query)
        stats = []
        for stat in results:
            stats.append( cls(stat) )
        return stats

    @classmethod
    def save(cls, data):
        query = "INSERT INTO stats (points, rebounds, assists, steals, blocks, turnovers, made_shots, attempted_shots, created_at, updated_at, game_id, player_id ) VALUES (%(points)s, %(rebounds)s, %(assists)s, %(steals)s, %(blocks)s, %(turnovers)s, %(made_shots)s, %(attempted_shots)s, NOW() , NOW(), %(game_id)s, %(player_id)s);"
        return connectToMySQL('maces_schema').query_db( query, data )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM stats WHERE id = %(id)s;"
        results = connectToMySQL('maces_schema').query_db(query, data)
        return cls(results[0])
    
        
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM stats WHERE id = %(id)s"
        return connectToMySQL('maces_schema').query_db(query, data)
