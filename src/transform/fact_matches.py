import pandas as pd

def create_fact_matches(df, dim_teams):

    team_map = dict(zip(dim_teams.team_name, dim_teams.team_id))

    fact = df.copy()

    fact["home_team_id"] = fact["home_team"].map(team_map)
    fact["away_team_id"] = fact["away_team"].map(team_map)

    fact = fact[[
        "date",
        "matchday",
        "home_team_id",
        "away_team_id",
        "home_score",
        "away_score",
        "winner"
    ]]

    fact.to_csv("data/processed/fact_matches.csv", index=False)

    print("fact_matches criada")

    return fact