import pandas as pd

def create_dim_teams(df):

    teams = pd.concat([
        df["home_team"],
        df["away_team"]
    ]).unique()

    dim_teams = pd.DataFrame({
        "team_id": range(1, len(teams) + 1),
        "team_name": teams
    })

    dim_teams.to_csv("data/processed/dim_teams.csv", index=False)

    print("dim_teams criada")

    return dim_teams