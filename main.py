from league import League

'''
Top 5 Leagues In Europe:
Ligue 1. -> France League
Serie A. -> Italian League
Bundesliga. -> German League
La Liga. -> Spain League
Premier League. -> England League
'''


def get_url(league, season):
    league = league.lower().title()

    d = {
        'Ligue 1': 'fra.1',
        'Serie A': 'ita.1',
        'Bundesliga': 'ger.1',
        'La Liga': 'esp.1',
        'Premier League': 'eng.1'
    }

    return f'https://api-football-standings.azharimm.site/leagues/{d[league]}/standings?season={season}&sort=asc'


print("\nWe will give you all the information you want from"\
      "the Top 5 Leagues in Europe & the World!\n")

l = input("What Soccer league are you interested in?\n")
s = input("What season are you interested in?\n")

my_league = League(get_url(l, s))

# team = input("What is your favorite team?")
print(my_league.df)