import unittest
from league import League
import random


class TestLeague(unittest.TestCase):
    def get_url(self, league, season):
        league = league.lower().title()

        d = {
            "Ligue 1": "fra.1",
            "Serie A": "ita.1",
            "Bundesliga": "ger.1",
            "La Liga": "esp.1",
            "Premier League": "eng.1",
        }
        url = (
            f"https://api-football-standings.azharimm.site/leagues/{d[league]}"
            f"/standings?season={season}&sort=asc"
        )
        return url

    def get_teams(self):
        return ["Ligue 1", "Serie A", "Bundesliga", "La Liga", "Premier League"]

    def test_get_team_names(self):
        teams = self.get_teams()

        for value in teams:
            url = self.get_url(value, random.randint(2001, 2022))
            league = League(url)
            test = League(url)
            self.assertEqual(league.get_team_names(), test.get_team_names())

    def test_get_team_wins(self):
        teams = self.get_teams()

        for value in teams:
            url = self.get_url(value, random.randint(2001, 2022))
            league = League(url)
            test = League(url)
            self.assertEqual(league.get_team_wins(), test.get_team_wins())

    def test_get_team_losses(self):
        teams = self.get_teams()

        for value in teams:
            url = self.get_url(value, random.randint(2001, 2022))
            league = League(url)
            test = League(url)
            self.assertEqual(league.get_team_losses(), test.get_team_losses())

    def test_get_team_ties(self):
        teams = self.get_teams()

        for value in teams:
            url = self.get_url(value, random.randint(2001, 2022))
            league = League(url)
            test = League(url)
            self.assertEqual(league.get_team_ties(), test.get_team_ties())

    def test_get_team_points(self):
        teams = self.get_teams()

        for value in teams:
            url = self.get_url(value, random.randint(2001, 2022))
            league = League(url)
            test = League(url)
            self.assertEqual(league.get_team_points(), test.get_team_points())

    def test_get_team_positions(self):
        teams = self.get_teams()

        for value in teams:
            url = self.get_url(value, random.randint(2001, 2022))
            league = League(url)
            test = League(url)
            self.assertEqual(league.get_team_positions(), test.get_team_positions())

    def test_create_dict(self):
        teams = self.get_teams()

        for value in teams:
            url = self.get_url(value, random.randint(2001, 2022))
            league = League(url)
            test = League(url)
            self.assertEqual(league.create_dict(), test.create_dict())


if __name__ == "__main__":
    unittest.main()
