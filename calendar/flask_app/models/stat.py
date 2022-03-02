from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_app.models import player


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
        self.player = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM stats;"
        results = connectToMySQL('maces_schema').query_db(query)
        stats = []
        for stat in results:
            stats.append( cls(stat) )
        return stats

    @classmethod
    def get_average_of_all_players_by_season(cls, data):
        query = "SELECT stats.id, AVG(points) AS points, AVG(rebounds) AS rebounds, AVG(assists) AS assists, AVG(steals) AS steals, AVG(blocks) AS blocks, AVG(turnovers) AS turnovers, AVG(made_shots) AS made_shots, AVG(attempted_shots) AS attempted_shots, first_name, last_name, number, stats.created_at, stats.updated_at, player_id, game_id, season_id  FROM stats LEFT JOIN players ON stats.player_id = players.id WHERE season_id = %(season_id)s GROUP BY player_id;"
        results = connectToMySQL('maces_schema').query_db(query,data)
        stats = []
        for i in range(len(results)):
            stats.append(cls(results[i]))
            p = {
                'id': results[i]['player_id'],
                'first_name': results[i]['first_name'],
                'last_name': results[i]['last_name'],
                'number': results[i]['number'],
                'level': None,
                'description': None,
                'created_at': None,
                'updated_at': None,
                'season_id': results[i]['season_id']
            }
            stats[i].player = player.Player(p)
            
        return stats

    @classmethod
    def get_average_of_team_by_season(cls, data):
        query = "SELECT stats.id, SUM(points)/(SELECT COUNT( DISTINCT game_id ) FROM stats) AS points, SUM(rebounds)/(SELECT COUNT( DISTINCT game_id ) FROM stats)  AS rebounds, SUM(assists)/(SELECT COUNT( DISTINCT game_id ) FROM stats) AS assists, SUM(steals)/(SELECT COUNT( DISTINCT game_id ) FROM stats) AS steals, SUM(blocks)/(SELECT COUNT( DISTINCT game_id ) FROM stats) AS blocks, SUM(turnovers)/(SELECT COUNT( DISTINCT game_id ) FROM stats) AS turnovers, SUM(made_shots)/(SELECT COUNT( DISTINCT game_id ) FROM stats) AS made_shots, SUM(attempted_shots)/(SELECT COUNT( DISTINCT game_id ) FROM stats) AS attempted_shots, stats.created_at, stats.updated_at, player_id, game_id, season_id  FROM stats LEFT JOIN players ON stats.player_id = players.id WHERE season_id = %(season_id)s;"
        results = connectToMySQL('maces_schema').query_db(query,data)
        return cls(results[0])

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
