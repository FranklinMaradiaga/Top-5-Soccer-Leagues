import requests
import pandas as pd
import sqlalchemy as db

class League:

    def __init__(self, league_url):
        self.league_json = self._get_json(league_url)
        self.names = self.get_team_names()
        self.wins = self.get_team_wins()
        self.losses = self.get_team_losses()
        self.ties = self.get_team_ties()
        self.points = self.get_team_points()
        self.positions = self.get_team_positions()
        self.df = self.create_database()


    def _get_json(self, url):
        return requests.get(url).json()


    def get_team_names(self):
        response = self.league_json
        names = []

        for data in response['data']['standings']:
            names.append(data['team']['name'])

        return names


    def get_team_wins(self):
        response = self.league_json
        wins = []

        for data in response['data']['standings']:
            wins.append(data['stats'][0]['displayValue'])

        return wins


    def get_team_losses(self):
        response = self.league_json
        losses = []
        for data in response['data']['standings']:
            losses.append(data['stats'][1]['displayValue'])

        return losses


    def get_team_ties(self):
        response = self.league_json
        ties = []

        for data in response['data']['standings']:
            ties.append(data['stats'][2]['displayValue'])

        return ties


    def get_team_points(self):
        response = self.league_json
        points = []

        for data in response['data']['standings']:
            points.append(data['stats'][6]['displayValue'])

        return points
        

    def get_team_positions(self):
        response = self.league_json
        positions = []

        for data in response['data']['standings']:
            positions.append(data['stats'][8]['displayValue'])

        return positions


    def create_dict(self):

        dict = {
            'names': self.names,
            'wins': self.wins,
            'losses': self.losses,
            'ties': self.ties,
            'points': self.points,
            'position': self.positions
        }

        return dict


    def create_database(self):
        dict = self.create_dict()
        data = pd.DataFrame.from_dict(dict)

        engine = db.create_engine('sqlite:///League.db')
        data.to_sql("Teams", con=engine, if_exists='replace', index=False)

        query_result = engine.execute("SELECT * FROM Teams;")
        query_result = query_result.fetchall()

        df = pd.DataFrame(query_result)
        df.columns = ['names', 'wins', 'losses', 'ties', 'points', 'rank']

        return df
