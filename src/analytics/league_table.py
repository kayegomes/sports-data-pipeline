import pandas as pd

def generate_league_table(df):

    teams = set(df["home_team"]).union(set(df["away_team"]))

    table = []

    for team in teams:

        home = df[df["home_team"] == team]
        away = df[df["away_team"] == team]

        wins = (
            (home["winner"] == "HOME_TEAM").sum() +
            (away["winner"] == "AWAY_TEAM").sum()
        )

        draws = (
            (home["winner"] == "DRAW").sum() +
            (away["winner"] == "DRAW").sum()
        )

        losses = (
            (home["winner"] == "AWAY_TEAM").sum() +
            (away["winner"] == "HOME_TEAM").sum()
        )

        matches = len(home) + len(away)

        points = wins * 3 + draws

        table.append({
            "team": team,
            "matches": matches,
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "points": points
        })

    league_df = pd.DataFrame(table)

    league_df = league_df.sort_values("points", ascending=False)

    league_df.to_csv("data/processed/league_table.csv", index=False)

    print("\nTabela do campeonato:")
    print(league_df.head(10))

    return league_df