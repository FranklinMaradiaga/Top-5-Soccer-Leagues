from league import League

"""
Top 5 Leagues In Europe:
Ligue 1. -> France League
Serie A. -> Italian League
Bundesliga. -> German League
La Liga. -> Spain League
Premier League. -> England League
"""


def get_url(league, season):

    league = league.lower().title()

    d = {
        "Ligue 1": "fra.1",
        "Serie A": "ita.1",
        "Bundesliga": "ger.1",
        "La Liga": "esp.1",
        "Premier League": "eng.1",
    }
    f1 = f"https://api-football-standings.azharimm.site/leagues/{d[league]}/"
    f2 = f"standings?season={season}&sort=asc"
    return f1 + f2


def main():
    print(
        "\nWe will give you all the information you want from"
        " the Top 5 Leagues in Europe & the World!"
    )

    while True:

        league = input("\nWhat Soccer league are you interested in?\n")
        s = input("\nWhat season are you interested in?\n")

        my_league = League(get_url(league, s))
        print("\n\n", my_league.df)

        user = input(
            "\n\nWould you like to get information about another league (yes/no)?\n"
        )

        if user.lower() == "yes":
            continue
        else:
            print("\nHope to see you again soon!\n")
            break


main()
